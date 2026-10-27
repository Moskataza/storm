"""One browser journey; business assertions belong to test_task_workflow."""

import os
from contextlib import contextmanager
import socket
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen

from playwright.sync_api import expect, sync_playwright


@contextmanager
def workbench_server(workspace, log_path):
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    env = dict(os.environ, STORM_WORKSPACE=str(workspace))
    with log_path.open("w") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                "frontend/workbench/app.py",
                "--server.address=127.0.0.1",
                f"--server.port={port}",
                "--server.headless=true",
                "--browser.gatherUsageStats=false",
            ],
            env=env,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        url = f"http://127.0.0.1:{port}"
        try:
            for _ in range(200):
                if process.poll() is not None:
                    raise AssertionError(log_path.read_text())
                try:
                    with urlopen(url + "/_stcore/health", timeout=1) as response:
                        if response.status == 200:
                            break
                except (URLError, TimeoutError):
                    time.sleep(0.1)
            else:
                raise AssertionError("Streamlit did not become ready")
            yield url
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


def test_browser_create_run_restart_and_reopen(tmp_path):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        with workbench_server(tmp_path / "tasks", tmp_path / "first.log") as url:
            page = browser.new_page()
            page.goto(url)
            page.get_by_label("Title", exact=True).fill("Browser task 研究")
            page.get_by_label("Purpose", exact=True).fill("Inspect saved local notes")
            page.get_by_role("button", name="Save worksheet", exact=True).click()
            expect(
                page.get_by_role("button", name="Run task", exact=True)
            ).to_be_enabled(timeout=60000)
            page.get_by_role("button", name="Run task", exact=True).click()
            expect(page.get_by_text("Outcome: completed", exact=True)).to_be_visible(
                timeout=60000
            )
            revision = (
                page.get_by_test_id("stCaptionContainer")
                .filter(has_text="Report revision:")
                .inner_text()
            )
            expect(
                page.get_by_role("link", name="Evidence 1", exact=True)
            ).to_be_visible()
            page.get_by_text(
                "Outcome: completed", exact=True
            ).scroll_into_view_if_needed()
            page.screenshot(path=str(tmp_path / "workbench.png"), full_page=True)
            page.close()
        # Restart the Python process and start a fresh browser session.
        with workbench_server(tmp_path / "tasks", tmp_path / "restarted.log") as url:
            page = browser.new_page()
            page.goto(url)
            page.get_by_role("button", name="Open task", exact=True).click()
            expect(page.get_by_label("Purpose", exact=True)).to_have_value(
                "Inspect saved local notes", timeout=60000
            )
            expect(page.get_by_text(revision, exact=True)).to_be_visible()
            expect(page.get_by_text("Outcome: completed", exact=True)).to_be_visible()
            expect(
                page.get_by_test_id("stText").filter(
                    has_text="本地笔记可以保存并重新打开。"
                )
            ).to_be_visible()
            page.close()
        browser.close()

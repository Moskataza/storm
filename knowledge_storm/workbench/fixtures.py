"""Offline source/model inputs for the first workbench demonstration."""

import re
from typing import Any

import dspy

from .models import EvidenceInput


class FixtureRetriever:
    """Implement STORM's existing retrieval-model interface without network I/O."""

    def __init__(self, records: list[dict[str, Any]]):
        self.records = [EvidenceInput.model_validate(record) for record in records]
        self.queries = 0

    def __call__(self, query_or_queries, exclude_urls=()):
        self.queries += len(query_or_queries)
        return [
            {
                "url": record.origin,
                "title": record.title,
                "description": "Supplied evidence fixture",
                "snippets": [record.content],
                "meta": record.model_dump(mode="json"),
            }
            for record in self.records
            if record.origin not in exclude_urls
        ]

    def get_usage_and_reset(self):
        queries, self.queries = self.queries, 0
        return {"fixture": queries}


class FixtureLM(dspy.dsp.LM):
    """Extract supplied snippets into a cited section; never invent analysis.

    This is an explicitly labeled fixture model, not an LLM service. A configured
    DSPy model can be injected through TaskWorkflow using the same STORM seam.
    """

    def __init__(self, response: str | None = None):
        super().__init__("fixture-extractive")
        self.response = response

    def basic_request(self, prompt, **kwargs):
        if self.response is not None:
            return self.response
        # These delimiters belong to STORM's existing WriteSection signature.
        info = prompt.rsplit("The collected information:", 1)[-1]
        info = info.split("The topic of the page:", 1)[0]
        snippets = re.findall(
            r"\[(\d+)\][ \t]*\n(.*?)(?=\n\[\d+\][ \t]*\n|\Z)", info, re.S
        )
        return "# Findings\n\n" + "\n\n".join(
            f"{text.strip()} [{index}]" for index, text in snippets
        )

    def __call__(self, prompt, only_completed=True, return_sorted=False, **kwargs):
        response = self.basic_request(prompt, **kwargs)
        self.history.append({"prompt": prompt, "response": response})
        return [response]

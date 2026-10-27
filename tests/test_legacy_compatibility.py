from knowledge_storm import (
    STORMWikiLMConfigs,
    STORMWikiRunner,
    STORMWikiRunnerArguments,
)
from knowledge_storm.storm_wiki.modules.storm_dataclass import StormArticle
from knowledge_storm.workbench.fixtures import FixtureLM, FixtureRetriever


def test_legacy_topic_runner_retrieves_and_polishes_saved_article(tmp_path):
    model = FixtureLM(response="Local notes support saving and reopening.[1]")
    configs = STORMWikiLMConfigs()
    configs.set_conv_simulator_lm(model)
    configs.set_question_asker_lm(model)
    configs.set_outline_gen_lm(model)
    configs.set_article_gen_lm(model)
    configs.set_article_polish_lm(model)
    retriever = FixtureRetriever(
        [
            {
                "source_id": "notes",
                "service_id": "fixture",
                "origin": "https://example.test/notes",
                "title": "Local notes",
                "content": "Local notes support saving and reopening.",
                "retrieved_at": "2026-10-01T00:00:00Z",
                "coverage": ["text"],
            }
        ]
    )
    runner = STORMWikiRunner(
        STORMWikiRunnerArguments(output_dir=str(tmp_path), max_thread_num=1),
        configs,
        retriever,
    )
    # The legacy staged entry point supports continuing from its own saved draft.
    information = runner.retriever.retrieve("Local notes")
    draft = StormArticle(topic_name="Local notes")
    draft.update_section(
        current_section_content="# Features\nLocal notes support saving and reopening.[1]",
        current_section_info_list=information,
        parent_section_name="Local notes",
    )
    output = tmp_path / "Local_notes"
    output.mkdir()
    draft.dump_article_as_plain_text(output / "storm_gen_article.txt")
    draft.dump_reference_to_file(output / "url_to_info.json")
    runner.run(
        topic="Local notes",
        do_research=False,
        do_generate_outline=False,
        do_generate_article=False,
        do_polish_article=True,
    )
    runner.post_run()
    article = (output / "storm_gen_article_polished.txt").read_text()
    assert "saving and reopening" in article
    assert "[1]" in article
    assert "summary" in article
    assert (output / "run_config.json").is_file()
    assert runner.time["run_article_polishing_module"] >= 0

"""A bounded worksheet-to-article adapter using STORM's existing stages."""

import copy
import json
from pathlib import Path
from typing import Callable

from ..interface import Information
from ..storm_wiki.engine import (
    STORMWikiLMConfigs,
    STORMWikiRunner,
    STORMWikiRunnerArguments,
)
from ..storm_wiki.modules.storm_dataclass import (
    DialogueTurn,
    StormArticle,
    StormInformationTable,
)
from .models import Capture, Worksheet


class CaptureRetriever:
    """Save raw captures before Retriever cleans snippets or STORM merges URLs."""

    def __init__(
        self, retriever, save: Callable[[dict], Capture], worksheet: Worksheet
    ):
        self.retriever = retriever
        self.save = save
        self.allowed = {s.service_id for s in worksheet.selected_sources}
        self.queries = 0

    def __call__(self, query_or_queries, exclude_urls=()):
        self.queries += len(query_or_queries)
        records = self.retriever(
            query_or_queries=query_or_queries, exclude_urls=exclude_urls
        )
        projected = []
        for record in records:
            if record.get("meta", {}).get("service_id") not in self.allowed:
                raise ValueError("Evidence service must be selected in the worksheet.")
            capture = self.save(record)
            view = copy.deepcopy(record)
            # STORM keys references by URL. Project capture IDs as its URLs while
            # keeping real origins and unmodified snapshots in the report bundle.
            view["url"] = f"urn:storm:capture:{capture.capture_id}"
            view["meta"]["capture_id"] = capture.capture_id
            projected.append(view)
        return projected

    def get_usage_and_reset(self):
        return {"workbench": self.queries}


class SuppliedInformationTable(StormInformationTable):
    """Use every supplied capture in this small fixture, without model downloads."""

    def prepare_table_for_retrieval(self):
        pass

    def retrieve_information(self, queries, search_top_k):
        return copy.deepcopy(list(self.url_to_info.values())[:search_top_k])


class StormAdapter:
    def __init__(self, retriever, model):
        self.retriever = retriever
        self.model = model

    def generate(
        self,
        worksheet: Worksheet,
        output_dir: Path,
        save_capture: Callable[[dict], Capture],
    ) -> tuple[str, dict[int, str], dict]:
        configs = STORMWikiLMConfigs()
        configs.set_conv_simulator_lm(self.model)
        configs.set_question_asker_lm(self.model)
        configs.set_outline_gen_lm(self.model)
        configs.set_article_gen_lm(self.model)
        configs.set_article_polish_lm(self.model)
        capturing = CaptureRetriever(self.retriever, save_capture, worksheet)
        runner = STORMWikiRunner(
            STORMWikiRunnerArguments(
                output_dir=str(output_dir), max_thread_num=1, retrieve_top_k=100
            ),
            configs,
            capturing,
        )
        context = (
            "Answer the requester's purpose and priority questions using only the "
            "supplied evidence. Preserve qualifications; do not invent numbers. "
            "Demand worksheet:\n"
            + json.dumps(worksheet.model_dump(), ensure_ascii=False)
        )
        information: list[Information] = runner.retriever.retrieve(context)
        if not information:
            return "", {}, {"retrieval_queries": capturing.queries}
        table = SuppliedInformationTable(
            [("Supplied evidence", [DialogueTurn(search_results=information)])]
        )
        # The runner's public staged API avoids the legacy topic-based directory
        # identity and its autonomous research/persona phase for this fixture slice.
        runner.topic = context
        runner.article_output_dir = str(output_dir)
        outline = StormArticle.from_outline_str(topic=context, outline_str="# Findings")
        article = runner.run_article_generation_module(
            outline=outline, information_table=table
        )
        citations = {
            index: url.removeprefix("urn:storm:capture:")
            for url, index in article.reference["url_to_unified_index"].items()
        }
        return (
            article.to_string(),
            citations,
            {
                "retrieval_queries": capturing.queries,
                "stage_seconds": runner.time,
                "model_usage": runner.lm_cost,
            },
        )

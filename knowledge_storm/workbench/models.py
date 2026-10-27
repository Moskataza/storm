"""Version 1 of the shared JSON-plus-files report bundle.

Paths are relative to the task directory. IDs identify saved objects, never titles
or URLs. Empty analysis sections are deliberate extension points for later slices.
"""

from datetime import datetime
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

NonemptyText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)


class SourceSelection(Record):
    service_id: str = Field(min_length=1)
    required: bool = False


class Worksheet(Record):
    title: str = Field(min_length=1)
    purpose: str = Field(min_length=1)
    priority_questions: list[NonemptyText] = Field(min_length=1)
    scope: str = Field(min_length=1)
    value_criteria: list[NonemptyText] = Field(min_length=1)
    completion_criteria: list[NonemptyText] = Field(min_length=1)
    processing_needs: str = Field(min_length=1)
    audience: str = Field(min_length=1)
    language: str = Field(min_length=1)
    requested_outputs: list[NonemptyText] = Field(min_length=1)
    selected_sources: list[SourceSelection]
    time_allowance_minutes: float = Field(gt=0, allow_inf_nan=False)
    cost_allowance: float = Field(ge=0, allow_inf_nan=False)
    cost_currency: str = Field(min_length=1)


class EvidenceInput(Record):
    """A supplied capture, including its actual coverage and original content."""

    source_id: str = Field(min_length=1)
    service_id: str = Field(min_length=1)
    origin: str = Field(min_length=1)
    title: str = Field(min_length=1)
    content: Annotated[str, StringConstraints(strip_whitespace=False, min_length=1)]
    retrieved_at: datetime
    published_at: datetime | None = None
    observed_at: datetime | None = None
    coverage: list[NonemptyText] = Field(min_length=1)
    acquisition_method: str = "supplied_fixture"
    acquisition_outcome: str = "success"


class Capture(Record):
    capture_id: str
    source_id: str
    service_id: str
    origin: str
    title: str
    retrieved_at: datetime
    published_at: datetime | None
    observed_at: datetime | None
    coverage: list[str]
    acquisition_method: str
    acquisition_outcome: str
    content_path: str
    record_path: str


class Finding(Record):
    finding_id: str
    text: str
    evidence_ids: list[str]
    kind: str = "source_claim"
    qualification: str = "Supplied evidence; not independently verified."


class Artifact(Record):
    artifact_id: str
    kind: str
    path: str
    media_type: str
    revision_id: str


class Usage(Record):
    elapsed_seconds: float = 0
    retrieval_queries: int | None = None
    model_usage: dict[str, Any] = Field(default_factory=dict)
    stage_seconds: dict[str, float] = Field(default_factory=dict)
    estimated_cost: float | None = None
    cost_status: str = "unknown; not provider billing"


class ReportBundle(Record):
    schema_version: Literal[1] = 1
    task_id: str
    task_created_at: datetime
    revision_id: str
    parent_revision_id: str | None
    revision_number: int
    created_at: datetime
    status: Literal["draft", "completed", "insufficient_evidence", "failed"]
    worksheet: Worksheet
    purpose: str
    findings: list[Finding] = Field(default_factory=list)
    evidence: list[Capture] = Field(default_factory=list)
    datasets: list[dict[str, Any]] = Field(default_factory=list)
    chart_specifications: list[dict[str, Any]] = Field(default_factory=list)
    methods: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    usage: Usage = Field(default_factory=Usage)
    budget: dict[str, Any]
    artifacts: list[Artifact] = Field(default_factory=list)

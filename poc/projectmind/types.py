"""ProjectMind types."""
from __future__ import annotations
from dataclasses import dataclass, field

CONTINUITY_OK = "CONTINUITY_OK"
CONTINUITY_DRIFT = "CONTINUITY_DRIFT"
AUTHORITY_VIOLATION = "AUTHORITY_VIOLATION"
STALE_FRONTIER = "STALE_FRONTIER"
INCOMPLETE_EVIDENCE = "INCOMPLETE_EVIDENCE"
CONTRACT_MISMATCH = "CONTRACT_MISMATCH"
PENDING = "PENDING"

@dataclass
class Claim:
    claim_id: str
    statement: str
    authenticity: float
    confidence: float
    authority: str
    freshness: float
    completeness: float

@dataclass
class Frontier:
    commit: str
    node_ids: list[str]
    digest: str

@dataclass
class ConsequenceContract:
    contract_id: str
    predicted_nodes: list[str]
    predicted_tests: list[str]
    authority: str
    digest: str

@dataclass
class ObservedDelta:
    nodes_changed: list[str]
    tests_changed: list[str]

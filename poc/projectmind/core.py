"""ProjectMind core — frontier digests + continuity classification."""
from __future__ import annotations
import hashlib
import json
from typing import Any

from .types import (
    AUTHORITY_VIOLATION,
    CONTINUITY_DRIFT,
    CONTINUITY_OK,
    CONTRACT_MISMATCH,
    INCOMPLETE_EVIDENCE,
    PENDING,
    STALE_FRONTIER,
)

def stable(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)

def frontier_digest(commit: str, node_ids: list[str]) -> str:
    return hashlib.sha256(f"{commit}|{','.join(sorted(node_ids))}".encode()).hexdigest()

def contract_digest(predicted_nodes: list[str], predicted_tests: list[str], authority: str) -> str:
    payload = f"{','.join(sorted(predicted_nodes))}|{','.join(sorted(predicted_tests))}|{authority}"
    return hashlib.sha256(payload.encode()).hexdigest()

def receipt_digest(parts: dict[str, Any]) -> str:
    return hashlib.sha256(stable(parts).encode()).hexdigest()

def classify_continuity(
    *,
    has_frontier: bool,
    has_contract: bool,
    has_observed: bool,
    frontier_fresh: bool,
    claim_complete: bool,
    authority_ok: bool,
    predicted_nodes: list[str],
    predicted_tests: list[str],
    observed_nodes: list[str],
    observed_tests: list[str],
) -> tuple[str, list[str]]:
    if not has_frontier or not has_contract:
        return PENDING, ["frontier or contract missing"]
    if not authority_ok:
        return AUTHORITY_VIOLATION, ["authority ledger rejects actor"]
    if not frontier_fresh:
        return STALE_FRONTIER, ["evidence frontier stale vs target commit"]
    if not claim_complete:
        return INCOMPLETE_EVIDENCE, ["claim completeness below threshold"]
    if not has_observed:
        return PENDING, ["observed delta not recorded"]
    node_mismatch = sorted(set(observed_nodes) - set(predicted_nodes))
    test_mismatch = sorted(set(observed_tests) - set(predicted_tests))
    if node_mismatch or test_mismatch:
        return CONTRACT_MISMATCH, [
            f"unpredicted nodes={node_mismatch[:5]} tests={test_mismatch[:5]}"
        ]
    # Drift: predicted but not observed (incomplete realization) — still continuity ok if subset
    missing = sorted(set(predicted_nodes) - set(observed_nodes))
    if missing and len(observed_nodes) < len(predicted_nodes) * 0.5:
        return CONTINUITY_DRIFT, [f"large unrealized prediction: {missing[:5]}"]
    return CONTINUITY_OK, ["observed delta within Change Consequence Contract"]

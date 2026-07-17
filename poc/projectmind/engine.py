"""ProjectMindEngine — evidence frontier + continuity receipts.
Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765
"""
from __future__ import annotations
from typing import Any

from .core import classify_continuity, contract_digest, frontier_digest, receipt_digest
from .types import Claim, ConsequenceContract, Frontier, ObservedDelta
from .validators import require_id, require_text, require_unit

_LIMITS = (
    "Bounded project-continuity evidence only. ProjectMind does not claim "
    "perfect code understanding, production agent memory, peer review, or "
    "independent replication."
)

class ProjectMindEngine:
    """Evidence Frontier -> claims -> Change Consequence Contract -> Continuity Receipt.

    Usage:
        e = ProjectMindEngine()
        e.set_frontier("abc123", ["mod.auth", "mod.api"])
        e.add_claim("C1", statement="auth depends on api", authenticity=1, confidence=0.8,
                    authority="alice", freshness=1.0, completeness=1.0)
        e.compile_contract("CC1", predicted_nodes=["mod.auth"], predicted_tests=["test_auth"],
                           authority="alice")
        e.record_observed(nodes_changed=["mod.auth"], tests_changed=["test_auth"])
        print(e.reconcile()["verdict"])
    """

    def __init__(self, freshness_threshold: float = 0.5, completeness_threshold: float = 0.7) -> None:
        self._frontier: Frontier | None = None
        self._claims: dict[str, Claim] = {}
        self._ledger: list[dict[str, Any]] = []
        self._contract: ConsequenceContract | None = None
        self._observed: ObservedDelta | None = None
        self._authorized: set[str] = set()
        self._freshness_threshold = freshness_threshold
        self._completeness_threshold = completeness_threshold

    def authorize(self, actor: str) -> None:
        self._authorized.add(require_text("actor", actor))
        self._ledger.append({"event": "authorize", "actor": actor})

    def set_frontier(self, commit: str, node_ids: list[str], *, fresh: bool = True) -> Frontier:
        commit = require_id("commit", commit)
        nodes = [require_id("node", n) for n in node_ids]
        digest = frontier_digest(commit, nodes)
        self._frontier = Frontier(commit=commit, node_ids=nodes, digest=digest)
        self._frontier_fresh = bool(fresh)
        return self._frontier

    def add_claim(
        self,
        claim_id: str,
        *,
        statement: str,
        authenticity: float,
        confidence: float,
        authority: str,
        freshness: float,
        completeness: float,
    ) -> Claim:
        c = Claim(
            claim_id=require_id("claim_id", claim_id),
            statement=require_text("statement", statement),
            authenticity=require_unit("authenticity", authenticity),
            confidence=require_unit("confidence", confidence),
            authority=require_text("authority", authority),
            freshness=require_unit("freshness", freshness),
            completeness=require_unit("completeness", completeness),
        )
        if c.claim_id in self._claims:
            raise ValueError(f"duplicate claim: {c.claim_id}")
        self._claims[c.claim_id] = c
        self._ledger.append({"event": "claim", "claim_id": c.claim_id, "authority": c.authority})
        return c

    def compile_contract(
        self,
        contract_id: str,
        *,
        predicted_nodes: list[str],
        predicted_tests: list[str],
        authority: str,
    ) -> ConsequenceContract:
        authority = require_text("authority", authority)
        digest = contract_digest(predicted_nodes, predicted_tests, authority)
        self._contract = ConsequenceContract(
            contract_id=require_id("contract_id", contract_id),
            predicted_nodes=list(predicted_nodes),
            predicted_tests=list(predicted_tests),
            authority=authority,
            digest=digest,
        )
        self._ledger.append({"event": "contract", "contract_id": contract_id, "authority": authority})
        return self._contract

    def record_observed(self, *, nodes_changed: list[str], tests_changed: list[str]) -> ObservedDelta:
        self._observed = ObservedDelta(
            nodes_changed=list(nodes_changed),
            tests_changed=list(tests_changed),
        )
        return self._observed

    def reconcile(self) -> dict[str, Any]:
        claims = list(self._claims.values())
        claim_complete = (
            bool(claims)
            and min(c.completeness for c in claims) >= self._completeness_threshold
        )
        authority = self._contract.authority if self._contract else ""
        authority_ok = (not self._authorized) or (authority in self._authorized)
        frontier_fresh = getattr(self, "_frontier_fresh", True)
        verdict, reasons = classify_continuity(
            has_frontier=self._frontier is not None,
            has_contract=self._contract is not None,
            has_observed=self._observed is not None,
            frontier_fresh=frontier_fresh,
            claim_complete=claim_complete if claims else True,
            authority_ok=authority_ok,
            predicted_nodes=self._contract.predicted_nodes if self._contract else [],
            predicted_tests=self._contract.predicted_tests if self._contract else [],
            observed_nodes=self._observed.nodes_changed if self._observed else [],
            observed_tests=self._observed.tests_changed if self._observed else [],
        )
        parts = {
            "frontier": self._frontier.digest if self._frontier else None,
            "contract": self._contract.digest if self._contract else None,
            "verdict": verdict,
            "reasons": reasons,
            "ledger_len": len(self._ledger),
        }
        return {
            "verdict": verdict,
            "reasons": reasons,
            "continuity_receipt": receipt_digest(parts),
            "limits": _LIMITS,
            "details": parts,
        }

    def issue_continuity_receipt(self) -> dict[str, Any]:
        r = self.reconcile()
        return {
            "type": "continuity_receipt",
            "verdict": r["verdict"],
            "receipt_digest": r["continuity_receipt"],
            "limits": _LIMITS,
        }

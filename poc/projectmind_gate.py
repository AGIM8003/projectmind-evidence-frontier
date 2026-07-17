#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path
from projectmind import (
    AUTHORITY_VIOLATION, CONTINUITY_DRIFT, CONTINUITY_OK, CONTRACT_MISMATCH,
    INCOMPLETE_EVIDENCE, PENDING, STALE_FRONTIER, ProjectMindEngine,
)
OUT = Path(__file__).with_name("projectmind_gate_results.json")
def t(name, fn):
    try: return {"name": name, "pass": bool(fn()), "error": None}
    except Exception as e: return {"name": name, "pass": False, "error": str(e)}
def main():
    def ok():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"])
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"]); return e.reconcile()["verdict"]==CONTINUITY_OK
    def mismatch():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"])
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1","n2"], tests_changed=["t"]); return e.reconcile()["verdict"]==CONTRACT_MISMATCH
    def auth():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"])
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="b")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"]); return e.reconcile()["verdict"]==AUTHORITY_VIOLATION
    def stale():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"], fresh=False)
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"]); return e.reconcile()["verdict"]==STALE_FRONTIER
    def incomplete():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"])
        e.add_claim("k", statement="s", authenticity=1, confidence=1, authority="a", freshness=1, completeness=0.2)
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"]); return e.reconcile()["verdict"]==INCOMPLETE_EVIDENCE
    def pending():
        e=ProjectMindEngine(); e.set_frontier("c",["n1"]); return e.reconcile()["verdict"]==PENDING
    def drift():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1","n2","n3","n4"])
        e.compile_contract("x", predicted_nodes=["n1","n2","n3","n4"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"]); return e.reconcile()["verdict"]==CONTINUITY_DRIFT
    def receipt():
        e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n1"])
        e.compile_contract("x", predicted_nodes=["n1"], predicted_tests=["t"], authority="a")
        e.record_observed(nodes_changed=["n1"], tests_changed=["t"])
        r=e.issue_continuity_receipt(); return len(r["receipt_digest"])==64 and r["verdict"]==CONTINUITY_OK
    results=[t(n,f) for n,f in [
        ("continuity_ok",ok),("contract_mismatch",mismatch),("authority_violation",auth),
        ("stale_frontier",stale),("incomplete_evidence",incomplete),("pending",pending),
        ("continuity_drift",drift),("receipt_digest",receipt)]]
    payload={"gate":"ProjectMind Reality Gate","passed":sum(r["pass"] for r in results),
             "total":len(results),"all_pass":all(r["pass"] for r in results),
             "timestamp":datetime.now(timezone.utc).isoformat(),"results":results}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Gate {payload['passed']}/{payload['total']}"); return 0 if payload["all_pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

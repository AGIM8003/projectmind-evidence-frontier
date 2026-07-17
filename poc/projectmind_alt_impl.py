#!/usr/bin/env python3
import json
from pathlib import Path
from projectmind import ProjectMindEngine
from projectmind.core import classify_continuity
OUT = Path(__file__).with_name("projectmind_replication_evidence.json")
def main():
    rows=[]
    specs=[
        dict(has_frontier=True,has_contract=True,has_observed=True,frontier_fresh=True,claim_complete=True,
             authority_ok=True,predicted_nodes=["a"],predicted_tests=["t"],observed_nodes=["a"],observed_tests=["t"]),
        dict(has_frontier=True,has_contract=True,has_observed=True,frontier_fresh=True,claim_complete=True,
             authority_ok=True,predicted_nodes=["a"],predicted_tests=["t"],observed_nodes=["a","b"],observed_tests=["t"]),
        dict(has_frontier=True,has_contract=True,has_observed=True,frontier_fresh=False,claim_complete=True,
             authority_ok=True,predicted_nodes=["a"],predicted_tests=["t"],observed_nodes=["a"],observed_tests=["t"]),
    ]
    for i,s in enumerate(specs):
        oracle=classify_continuity(**s)[0]
        e=ProjectMindEngine(); 
        if s["authority_ok"]: e.authorize("a")
        e.set_frontier("c", s["predicted_nodes"], fresh=s["frontier_fresh"])
        e.compile_contract("x", predicted_nodes=s["predicted_nodes"], predicted_tests=s["predicted_tests"], authority="a")
        e.record_observed(nodes_changed=s["observed_nodes"], tests_changed=s["observed_tests"])
        eng=e.reconcile()["verdict"]
        rows.append({"i":i,"engine":eng,"oracle":oracle,"match":eng==oracle})
    ok=all(r["match"] for r in rows)
    OUT.write_text(json.dumps({"rows":rows,"replication_pass":ok}, indent=2), encoding="utf-8")
    print("replication", ok); return 0 if ok else 1
if __name__ == "__main__":
    raise SystemExit(main())

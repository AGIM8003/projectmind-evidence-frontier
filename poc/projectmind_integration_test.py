#!/usr/bin/env python3
import json
from pathlib import Path
from projectmind import ProjectMindEngine, CONTINUITY_OK
OUT = Path(__file__).with_name("projectmind_integration_results.json")
def main():
    e=ProjectMindEngine(); e.authorize("a"); e.set_frontier("c",["n"])
    e.add_claim("k", statement="s", authenticity=1, confidence=1, authority="a", freshness=1, completeness=1)
    e.compile_contract("cc", predicted_nodes=["n"], predicted_tests=["t"], authority="a")
    e.record_observed(nodes_changed=["n"], tests_changed=["t"])
    d=e.reconcile(); r=e.issue_continuity_receipt()
    ok=d["verdict"]==CONTINUITY_OK and r["receipt_digest"]==d["continuity_receipt"]
    OUT.write_text(json.dumps({"pass":ok,"verdict":d["verdict"]}, indent=2), encoding="utf-8")
    print("integration", ok); return 0 if ok else 1
if __name__ == "__main__":
    raise SystemExit(main())

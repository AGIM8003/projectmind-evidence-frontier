#!/usr/bin/env python3
import json
from pathlib import Path
from projectmind import ProjectMindEngine, CONTINUITY_OK, CONTRACT_MISMATCH
OUT = Path(__file__).with_name("projectmind_evidence.json")
def main():
    e = ProjectMindEngine()
    e.authorize("alice")
    e.set_frontier("c0", ["mod.auth", "mod.api"])
    e.add_claim("K1", statement="auth->api", authenticity=1, confidence=0.9,
                authority="alice", freshness=1, completeness=1)
    e.compile_contract("CC", predicted_nodes=["mod.auth"], predicted_tests=["t_auth"], authority="alice")
    e.record_observed(nodes_changed=["mod.auth"], tests_changed=["t_auth"])
    ok = e.reconcile()
    e2 = ProjectMindEngine(); e2.authorize("alice")
    e2.set_frontier("c0", ["mod.auth"])
    e2.compile_contract("CC", predicted_nodes=["mod.auth"], predicted_tests=["t_auth"], authority="alice")
    e2.record_observed(nodes_changed=["mod.auth", "mod.billing"], tests_changed=["t_auth"])
    bad = e2.reconcile()
    payload = {"ok": ok["verdict"], "bad": bad["verdict"],
               "pass": ok["verdict"]==CONTINUITY_OK and bad["verdict"]==CONTRACT_MISMATCH}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

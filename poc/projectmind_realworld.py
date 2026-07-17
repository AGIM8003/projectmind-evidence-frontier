#!/usr/bin/env python3
"""Agent context claims auth module change; observed delta also hits billing — mismatch."""
import json
from pathlib import Path
from projectmind import ProjectMindEngine, CONTINUITY_OK, CONTRACT_MISMATCH, AUTHORITY_VIOLATION
OUT = Path(__file__).with_name("projectmind_realworld_evidence.json")
def main():
    e=ProjectMindEngine(); e.authorize("tech-lead")
    e.set_frontier("deadbeef", ["mod.auth", "mod.session", "mod.billing", "mod.api"])
    e.add_claim("dep", statement="session depends on auth", authenticity=1, confidence=0.85,
                authority="tech-lead", freshness=1, completeness=1)
    e.compile_contract("CCC", predicted_nodes=["mod.auth","mod.session"], predicted_tests=["test_login"],
                       authority="tech-lead")
    # Agent actually also changed billing
    e.record_observed(nodes_changed=["mod.auth","mod.session","mod.billing"], tests_changed=["test_login"])
    drift=e.reconcile()
    e2=ProjectMindEngine(); e2.authorize("tech-lead")
    e2.set_frontier("deadbeef", ["mod.auth","mod.session"])
    e2.compile_contract("CCC", predicted_nodes=["mod.auth","mod.session"], predicted_tests=["test_login"], authority="tech-lead")
    e2.record_observed(nodes_changed=["mod.auth","mod.session"], tests_changed=["test_login"])
    ok=e2.reconcile()
    e3=ProjectMindEngine(); e3.authorize("tech-lead")
    e3.set_frontier("deadbeef", ["mod.auth"])
    e3.compile_contract("CCC", predicted_nodes=["mod.auth"], predicted_tests=["t"], authority="intern-bot")
    e3.record_observed(nodes_changed=["mod.auth"], tests_changed=["t"])
    auth=e3.reconcile()
    payload={"mismatch":drift["verdict"],"ok":ok["verdict"],"auth":auth["verdict"],
             "numbers":{"frontier_nodes":4,"predicted":2,"observed_extra":1},
             "pass": drift["verdict"]==CONTRACT_MISMATCH and ok["verdict"]==CONTINUITY_OK and auth["verdict"]==AUTHORITY_VIOLATION}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

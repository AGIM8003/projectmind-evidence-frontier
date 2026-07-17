#!/usr/bin/env python3
from projectmind import ProjectMindEngine
e = ProjectMindEngine()
e.authorize("you")
e.set_frontier("HEAD", ["src/app.py"])
e.compile_contract("CC1", predicted_nodes=["src/app.py"], predicted_tests=["test_app"], authority="you")
e.record_observed(nodes_changed=["src/app.py"], tests_changed=["test_app"])
d = e.reconcile()
print("Verdict:", d["verdict"])
print("Receipt:", d["continuity_receipt"][:24], "...")

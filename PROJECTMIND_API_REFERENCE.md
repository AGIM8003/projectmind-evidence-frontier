# ProjectMind API v5.0.0
```python
from projectmind import ProjectMindEngine
e = ProjectMindEngine()
e.authorize("you")
e.set_frontier("HEAD", ["src/app.py"])
e.compile_contract("CC1", predicted_nodes=["src/app.py"], predicted_tests=["test_app"], authority="you")
e.record_observed(nodes_changed=["src/app.py"], tests_changed=["test_app"])
print(e.reconcile()["verdict"])
```
Verdicts: CONTINUITY_OK, CONTINUITY_DRIFT, AUTHORITY_VIOLATION, STALE_FRONTIER, INCOMPLETE_EVIDENCE, CONTRACT_MISMATCH, PENDING.

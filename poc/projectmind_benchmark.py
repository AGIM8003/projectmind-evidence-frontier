#!/usr/bin/env python3
import json, time
from pathlib import Path
from projectmind import ProjectMindEngine, CONTINUITY_OK
OUT = Path(__file__).with_name("projectmind_benchmark_results.json")
def main():
    e=ProjectMindEngine(); e.authorize("a")
    nodes=[f"n{i}" for i in range(500)]
    t0=time.perf_counter(); e.set_frontier("c", nodes)
    e.compile_contract("cc", predicted_nodes=nodes[:50], predicted_tests=["t"], authority="a")
    e.record_observed(nodes_changed=nodes[:50], tests_changed=["t"])
    d=e.reconcile(); sec=time.perf_counter()-t0
    cases=[{"name":"frontier_500","pass":d["verdict"]==CONTINUITY_OK,"seconds":round(sec,6)}]
    OUT.write_text(json.dumps({"cases":cases,"all_pass":all(c["pass"] for c in cases)}, indent=2), encoding="utf-8")
    print(cases); return 0 if cases[0]["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

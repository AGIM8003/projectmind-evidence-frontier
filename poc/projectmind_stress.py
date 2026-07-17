#!/usr/bin/env python3
import json, time, tracemalloc
from pathlib import Path
from projectmind import ProjectMindEngine, CONTINUITY_OK
OUT = Path(__file__).with_name("projectmind_stress_results.json")
def main():
    tracemalloc.start(); e=ProjectMindEngine(); e.authorize("a")
    n=2000; nodes=[f"n{i}" for i in range(n)]
    t0=time.perf_counter(); e.set_frontier("c", nodes)
    e.compile_contract("cc", predicted_nodes=nodes[:100], predicted_tests=["t"], authority="a")
    e.record_observed(nodes_changed=nodes[:100], tests_changed=["t"])
    d=e.reconcile(); sec=time.perf_counter()-t0; _,peak=tracemalloc.get_traced_memory(); tracemalloc.stop()
    payload={"nodes":n,"verdict":d["verdict"],"seconds":round(sec,4),"peak_kib":round(peak/1024,1),
             "pass": d["verdict"]==CONTINUITY_OK and sec<30}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

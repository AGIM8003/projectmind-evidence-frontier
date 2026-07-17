#!/usr/bin/env python3
import json
from pathlib import Path
from projectmind.core import classify_continuity
from projectmind.types import AUTHORITY_VIOLATION, CONTINUITY_OK, CONTRACT_MISMATCH, STALE_FRONTIER
OUT = Path(__file__).with_name("projectmind_mutation_results.json")
BASE=dict(has_frontier=True,has_contract=True,has_observed=True,frontier_fresh=True,claim_complete=True,
          authority_ok=True,predicted_nodes=["a"],predicted_tests=["t"],observed_nodes=["a"],observed_tests=["t"])
def main():
    results=[]
    # ignore authority
    c=classify_continuity(**{**BASE,"authority_ok":False})[0]
    m=classify_continuity(**{**BASE,"authority_ok":True})[0]  # mutant forces ok
    # proper mutant: force authority_ok True
    def mut_auth(**kw):
        kw=dict(kw); kw["authority_ok"]=True; return classify_continuity(**kw)[0]
    results.append({"name":"ignore_authority","killed": mut_auth(**{**BASE,"authority_ok":False}) != AUTHORITY_VIOLATION or True})
    results[-1]["killed"] = mut_auth(**{**BASE,"authority_ok":False}) != classify_continuity(**{**BASE,"authority_ok":False})[0]
    def mut_fresh(**kw):
        kw=dict(kw); kw["frontier_fresh"]=True; return classify_continuity(**kw)[0]
    results.append({"name":"ignore_stale","killed": mut_fresh(**{**BASE,"frontier_fresh":False}) != classify_continuity(**{**BASE,"frontier_fresh":False})[0]})
    def mut_mismatch(**kw):
        kw=dict(kw); kw["observed_nodes"]=list(kw["predicted_nodes"]); return classify_continuity(**kw)[0]
    results.append({"name":"rewrite_observed","killed": mut_mismatch(**{**BASE,"observed_nodes":["a","b"]}) != CONTRACT_MISMATCH})
    def mut_always(**kw):
        return CONTINUITY_OK
    results.append({"name":"always_ok","killed": mut_always(**{**BASE,"authority_ok":False}) != classify_continuity(**{**BASE,"authority_ok":False})[0]})
    def mut_complete(**kw):
        kw=dict(kw); kw["claim_complete"]=True; return classify_continuity(**kw)[0]
    from projectmind.types import INCOMPLETE_EVIDENCE
    results.append({"name":"ignore_incomplete","killed": mut_complete(**{**BASE,"claim_complete":False}) != INCOMPLETE_EVIDENCE})
    def mut_pending(**kw):
        kw=dict(kw); kw["has_observed"]=True; kw["observed_nodes"]=kw["predicted_nodes"]; kw["observed_tests"]=kw["predicted_tests"]; return classify_continuity(**kw)[0]
    from projectmind.types import PENDING
    results.append({"name":"fake_observed","killed": mut_pending(**{**BASE,"has_observed":False}) != PENDING})
    def mut_drift(**kw):
        kw=dict(kw); kw["observed_nodes"]=list(kw["predicted_nodes"]); return classify_continuity(**kw)[0]
    from projectmind.types import CONTINUITY_DRIFT
    results.append({"name":"hide_drift","killed": mut_drift(**{**BASE,"predicted_nodes":["a","b","c","d"],"observed_nodes":["a"]}) != CONTINUITY_DRIFT})
    def mut_no_frontier(**kw):
        kw=dict(kw); kw["has_frontier"]=True; kw["has_contract"]=True; return classify_continuity(**kw)[0]
    results.append({"name":"fake_frontier","killed": mut_no_frontier(**{**BASE,"has_frontier":False,"has_contract":False}) != PENDING})
    def mut_tests(**kw):
        kw=dict(kw); kw["observed_tests"]=list(kw["predicted_tests"]); return classify_continuity(**kw)[0]
    results.append({"name":"ignore_test_mismatch","killed": mut_tests(**{**BASE,"observed_tests":["other"]}) != CONTRACT_MISMATCH})
    def mut_stale_label(**kw):
        return CONTINUITY_OK if not kw.get("frontier_fresh", True) else classify_continuity(**kw)[0]
    results.append({"name":"stale_as_ok","killed": mut_stale_label(**{**BASE,"frontier_fresh":False}) != STALE_FRONTIER})
    killed=sum(1 for r in results if r["killed"]); rate=killed/len(results)
    payload={"killed":killed,"total":len(results),"kill_rate":round(rate,4),"pass":rate>=0.9,"results":results}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"mutation {killed}/{len(results)}"); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())

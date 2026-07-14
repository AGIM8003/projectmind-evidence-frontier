# ProjectMind Technical Contribution Map

This is a research and implementation map, not patent claims or legal advice.

| ID | Proposed contribution | Known overlap | Narrow distinguishing limitations | Required proof |
|---|---|---|---|---|
| PM-C1 | Commit-DAG Evidence Frontier | Git reachability, provenance manifests, temporal graphs | Admissible evidence and active claims are deterministically selected for a target commit, policy, extractor set, invalidations, conflicts, and completeness requirements; manifest uses canonical bytes and a stable digest. | Tests 61-65 and frontier reproducibility benchmark. |
| PM-C2 | Orthogonal claim-quality vector | Trust scores, confidence labels, policy authority | Authenticity, confidence, authority, freshness, and completeness cannot substitute for each other; weaker evidence cannot reduce caution. | Tests 66 and 69 plus property-based monotonicity testing. |
| PM-C3 | Authority Promotion Ledger | Audit logs, event sourcing, signed approvals | Every enforceable transition binds prior/new claim hashes, frontier, authority identity, reason, evidence disclosure, scope, and ledger head. | Tests 67-68 and ledger replay verification. |
| PM-C4 | Change Consequence Contract | Change plans, policy manifests, impact analysis | Expected graph/test/policy effects are compiled from one frontier and frozen before observed candidate analysis. | Test 72 and mutation/adversarial fixtures. |
| PM-C5 | Predicted/observed reconciliation | Change-impact analysis, regression selection | Candidate effects are independently reconstructed and classified as required, allowed, review, forbidden, missing, insufficient, mismatch, or unknown. | Tests 73-75 and labeled repository tasks. |
| PM-C6 | Context Receipt | MCP logs, retrieval traces, provenance | Receipt binds target commit, frontier, canonical query, claims, evidence, limits, omissions, tool manifest, and response digest. | Tests 70-71 and replay verification. |
| PM-C7 | Continuity Receipt | DSSE, in-toto/SLSA attestations | Receipt binds context receipts, authority-ledger head, frozen CCC, candidate tree, observed delta, tests, reconciliation, and limitations for offline verification. | Tests 76-79 and independent verifier. |
| PM-C8 | Complete continuity-control chain | Combination of all cited fields | C1 through C7 operate as one reproducible before/after project-state acceptance evidence chain. | End-to-end fixture and controlled comparative evaluation. |

## Essential Research Question

Does the complete PM-C8 chain measurably reduce silent context drift,
branch-confusion errors, unauthorized knowledge promotion, and unexpected
project-state effects compared with static instructions, event memory, or a
structural graph alone?

## Failure to Prove

The contribution should be narrowed or rejected if independent experiments show
that the frontier is not reproducible, authority cannot be meaningfully audited,
contracts are too incomplete to detect unexpected effects, receipts cannot be
verified offline, or the complete chain provides no material benefit over simpler
baselines.

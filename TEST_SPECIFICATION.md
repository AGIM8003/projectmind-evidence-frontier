# Test Specification and Coverage Trace

This specification defines the validation criteria for confirming the ProjectMind
evidence-frontier and continuity-control chain architecture.

## Frontier Resolution and Reproducibility (PM-C1)

### Test 61: Target Commit Selection and Canonical Pathing
- **Input:** Target commit hash, policy requirements list, active extractor configuration.
- **Assertion:** Extracted frontier returns identical canonical bytes and stable digests regardless of platform-specific line endings or retrieval paths.

### Test 62: Policy-Filtered Claim Admissibility
- **Input:** Source DAG containing active, expired, and revoked claims.
- **Assertion:** Filtered claims exclude any signature that does not match the active policy's root of trust.

### Test 63: Deterministic Frontier Extraction
- **Input:** Repository state with conflicting claim histories.
- **Assertion:** Extraction function yields exactly one reproducible graph frontier following deterministic precedence rules.

### Test 64: Signature Verification and Invalidations
- **Input:** Admissible claim with an expired certificate or revoked key.
- **Assertion:** Frontier selection invalidates the claim and marks its dependencies as unproven.

### Test 65: Active Claim completeness Checks
- **Input:** Frontier containing incomplete validation paths.
- **Assertion:** Validation fails and logs missing upstream evidence elements.

## Orthogonal Quality Evaluation (PM-C2)

### Test 66: Monotonicity of Claim-Quality Components
- **Input:** Quality score vector where confidence increases but authenticity decreases.
- **Assertion:** Evaluated quality does not increase; components must remain strictly independent (authenticity, confidence, authority, freshness, completeness).

### Test 69: Weaker Evidence Caution Constraints
- **Input:** Weak confidence claim mixed with high-authority signatures.
- **Assertion:** Quality evaluator retains the lowest confidence warning; high authority cannot override weak evidence.

## Authority-Governed Promotion (PM-C3)

### Test 67: Valid Authority Transitions and State Audit
- **Input:** Promotion request signed by authorized key with valid transition parameters.
- **Assertion:** Promotion ledger appends the transition; transition record binds prior/new claim hashes, target frontier, and authority identity.

### Test 68: Ledger Replay and Verification
- **Input:** Complete promotion ledger log.
- **Assertion:** Independent replayer reconstructs identical ledger states and validates cryptographic chain of custody.

## Change Consequence Contracts (PM-C4)

### Test 72: Expected Effect Compilation and Freeze
- **Input:** Frontier state, target change plan.
- **Assertion:** Contract generator compiles expected graph, test, and policy consequences, then freezes the contract hash before candidate verification.

## Predicted vs. Observed Reconciliation (PM-C5)

### Test 73: Observed Effect Reconstruction
- **Input:** Candidate commit, post-change repository state.
- **Assertion:** Observed test failures, modified files, and policy mutations are independently reconstructed.

### Test 74: Candidate Consequence Reconciliation
- **Input:** Frozen Change Consequence Contract, reconstructed observed effects.
- **Assertion:** Reconciliation matches observed vs. expected and classifies each effect: required, allowed, review, forbidden, missing, insufficient, mismatch, or unknown.

### Test 75: Forbidden State and Out-of-Contract Blockers
- **Input:** Reconciliation output containing forbidden or out-of-contract effects.
- **Assertion:** Repository validation fails and rejects promotion.

## Context and Continuity Receipts (PM-C6 & PM-C7)

### Test 70: Context Receipt Generation
- **Input:** Query target commit, frontier state, executed retrieval tools.
- **Assertion:** Generated receipt binds query, retrieved claims, tool manifest, and response digest.

### Test 71: Receipt Playback and Verification
- **Input:** Context receipt, target repository.
- **Assertion:** Replay confirms the tool output matches the receipt digest.

### Test 76: Continuity Receipt Construction (DSSE)
- **Input:** Context receipts, ledger head, frozen CCC, candidate tree, tests, reconciliation.
- **Assertion:** Receipt is structured as a valid DSSE envelope with in-toto/SLSA layout.

### Test 77: Offline Verification of Continuity Chain
- **Input:** Signed continuity receipt.
- **Assertion:** Verification script validates the entire chain offline without accessing active GitHub API or live network resources.

### Test 78: Cryptographic Signature Binding
- **Input:** Continuity receipt with detached signature.
- **Assertion:** Envelope verification fails if any signature does not match the signing authority.

### Test 79: Tamper Detection and Invalid Envelope Formats
- **Input:** Receipt with altered payload.
- **Assertion:** Envelope parser detects mismatch and rejects the receipt.

## E2E Continuity-Control Integration (PM-C8)

### Test 80: Comprehensive E2E Verification
- **Input:** Sample repository lifecycle from initial commit to promotion.
- **Assertion:** Complete PM-C8 chain executes successfully, producing verified receipts and ledger states.

### Test 81: Comparative Drift and branch-confusion Evaluation
- **Input:** Simulation of branch-confusion attacks.
- **Assertion:** Control chain detects and blocks unauthorized promotion, showing measurable reduction in silent context drift compared to baseline.

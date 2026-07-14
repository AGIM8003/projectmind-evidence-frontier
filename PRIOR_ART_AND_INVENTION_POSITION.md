# ProjectMind Prior-Art and Invention-Position Report

Research date: July 13, 2026  
Author assessed: Agim Haxhijaha  
Assessment type: technical publication positioning, not a patent opinion

## Executive Finding

ProjectMind remains publication-worthy, but broad claims about project memory,
repository knowledge graphs, temporal agent memory, MCP access, test impact,
provenance, or memory-as-governance are not defensible as new categories.

The strongest narrower contribution is the linked method that:

1. computes a canonical, commit-DAG-correct Evidence Frontier;
2. governs claim authority through an append-only transition ledger;
3. freezes expected effects in a Change Consequence Contract;
4. records the exact project context delivered to the agent;
5. independently reconstructs and reconciles the observed project-state delta;
6. emits a Continuity Receipt binding the complete chain.

This combination is an invention candidate, not proof of novelty or
patentability.

## Research Method

The review prioritized current primary research, official specifications,
official project documentation, and official standards. It examined repository
graphs, coding-agent memory, change-impact planning, test selection, temporal
knowledge graphs, provenance, attestations, MCP security, policy languages, Git
history, and embedded-storage behavior.

No exhaustive patent-claim, prosecution-history, trademark, or
freedom-to-operate search was performed. Keyword web searches cannot substitute
for a professional patent search using jurisdiction-specific databases and
classification codes.

## Closest Technical Prior Art

| Work | Material overlap | Remaining distinction in ProjectMind v4.0 |
|---|---|---|
| Codebase-Memory (2026) | Persistent Tree-sitter knowledge graph, MCP, impact analysis | No equivalent full frontier-authority-contract-reconciliation-receipt chain identified in the reviewed paper. |
| Repository Intelligence Graph (2026) | Deterministic evidence-backed build and test graph | ProjectMind binds active claims to Git ancestry, authority transitions, frozen expectations, and post-change receipts. |
| PROJECTMEM (2026) | Local event-sourced memory, MCP, provenance, pre-action governance | ProjectMind focuses on branch-correct evidence admissibility and verifiable before/after consequence evidence. |
| KGCompass (2025) | Repository artifacts and code entities linked for repair | ProjectMind is not principally a repair generator; it governs project-state evidence and acceptance handoff. |
| Prometheus (2025) | Multilingual repository graph for issue resolution | ProjectMind adds explicit authority, frontier, contract, and reconciliation semantics. |
| RepoDoc (2026) | Repository graph and incremental impact propagation | Documentation regeneration is different from authority-governed change continuity. |
| Zep/Graphiti (2025) | Temporal knowledge graph for agent memory | ProjectMind uses Git reachability, policy authority, and software-change receipts. |
| CodePlan (2023) | Dependency-based may-impact planning for repository edits | ProjectMind freezes expectations and compares them to independently observed deltas. |
| Codified Context (2026) | Persistent hot/cold project context across many sessions | ProjectMind makes context a digest-bound artifact with declared omissions. |
| Fine-Grained Assertion-Based Test Selection (2024/2025) | Assertion-level regression-test selection | ProjectMind does not claim test selection itself; it governs how test evidence affects authority and contracts. |

## Established Components That Are Not Novelty Claims

- property graphs, code property graphs, ASTs, control/data-flow graphs;
- SCIP and Tree-sitter extraction;
- build, dependency, and impact analysis;
- JUnit, LCOV, Istanbul, and per-test coverage contexts;
- temporal knowledge graphs and event-sourced memory;
- local SQLite storage, WAL, transactions, and backups;
- CloudEvents, DSSE, W3C PROV, in-toto, SLSA, and canonical JSON;
- MCP resources and tools;
- declarative policy evaluation;
- SBOMs, signed releases, and secure-development frameworks.

## Research-Driven Corrections

1. A signature proves source and integrity, not factual correctness.
2. Git history is a DAG; a global `valid_from/valid_to` interval is insufficient.
3. Claims and entities must be distinct, and evidence must be many-to-many.
4. Context responses must disclose omissions and retrieval limits.
5. A consequence contract must be frozen before observed analysis to prevent
   after-the-fact prediction.
6. Reduced evidence must not yield a less cautious decision.
7. Local MCP remains executable supply-chain risk even when it is read-only.
8. SQLite must use 3.51.3+ or an official corrected backport because the
   official WAL documentation describes a rare corruption bug fixed in 2026.
9. The original seven-day build promise is only credible as a feasibility
   spike, not as a complete implementation schedule.

## Preliminary Differentiation Assessment

| Mechanism | Differentiation estimate | Reason |
|---|---:|---|
| Commit-DAG Evidence Frontier | 72% | Narrow, deterministic admissibility and digest mechanism; still built from known Git/provenance ideas. |
| Orthogonal quality/authority vector | 62% | Strong correction, but multi-axis trust and policy models exist. |
| Authority Promotion Ledger | 68% | Useful specific governance record; append-only audit ledgers are established. |
| Change Consequence Contract | 70% | Distinct task-specific freezing of expected project effects; contracts and policies are established. |
| Predicted/observed delta reconciliation | 74% | Strong technical center when independently reconstructed and rule-compared. |
| Context and Continuity Receipts | 69% | Strong application-specific chain; provenance and attestation receipts are established. |
| Complete linked method | 77% | Best invention candidate, subject to formal prior-art and patent search. |

Percentages are analytical estimates, not legal probabilities.

## Publication and Patent Position

Publish as a proposed independent technical architecture, not as a proven or
patented invention. WIPO states that novelty and inventive step are central
patent requirements and that public disclosure before filing may become prior
art in many jurisdictions. Decide whether to seek professional advice before
public release.

## Primary Sources

1. https://arxiv.org/abs/2603.27277
2. https://arxiv.org/abs/2601.10112
3. https://arxiv.org/abs/2606.12329
4. https://arxiv.org/abs/2503.21710
5. https://arxiv.org/abs/2507.19942
6. https://arxiv.org/abs/2604.26523
7. https://arxiv.org/abs/2501.13956
8. https://arxiv.org/abs/2309.12499
9. https://arxiv.org/abs/2602.20478
10. https://arxiv.org/abs/2403.16001
11. https://www.w3.org/TR/prov-o/
12. https://modelcontextprotocol.io/specification/2025-06-18
13. https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
14. https://sqlite.org/wal.html
15. https://www.rfc-editor.org/rfc/rfc8785.html
16. https://slsa.dev/spec/v1.2/provenance
17. https://in-toto.io/
18. https://www.wipo.int/en/web/patents/faq_patents

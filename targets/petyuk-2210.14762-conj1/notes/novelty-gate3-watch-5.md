# Gate 3 Novelty Re-Check — `petyuk-2210.14762-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:40:57Z`
- **Target:** `targets/petyuk-2210.14762-conj1/TARGET.md`
- **Verdict:** **PASS** (no public refutation or proof of Petyuk `arXiv:2210.14762v2` Conjecture 1 found across live arXiv, OpenAlex citing check, Zenodo, `470` snapshots, or all 15 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"... 2210.14762 Petyuk ..."` -> only `watch/snapshots/arxiv/citing/petyuk-2210.14762-conj1.json` and `openalex_works_cache.json`.

2. **GitHub Live Checks (`gh api` trees across 15 competing repos, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, and `Varun-Dudipala/sun-conjectures-lean` -> `0` matches (`CrocSwap` `check-2210` is an unrelated efficient1200 packet ID).

3. **arXiv Live API, OpenAlex Citing Cache, & Zenodo:**
   - `2210.14762v2` (`2022-10-20`, v2 `2023-07-12`) sole/latest version.
   - `watch/snapshots/arxiv/citing/petyuk-2210.14762-conj1.json` (`2026-11-27T01:59:54Z`): `citing_count: 0`, `errors: []`.
   - Zenodo `q=2210.14762` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- Knisley–Nigussie–Pór (*JCMCC* 73, 2010) proved $\chi(S(4,3)) = 3$ (noted in `notes/audit-helper-petyuk.md`), without addressing word-representability (`2210.14762`); `2312.10377` (*DAM* 2024) and `2605.02268v2` leave Conjecture 1 open.
- `CONTESTED.md`: absent from `targets/petyuk-2210.14762-conj1/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

# Gate 3 Novelty Receipt — `targets/radici-2609.07769-open/` (`watch-1`)

- **Target:** `targets/radici-2609.07769-open/` (*A Note on Binary Quadratic Systems and Their Relation to Complexity Theory*, Gabriele Radici & Massimiliano Sala, `arXiv:2609.07769v2`, §9 *Open problems*: $\alpha_1 > \alpha_0$ over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$)
- **Checked At (UTC):** `2026-11-28T00:29:22Z`–`2026-11-28T00:29:47Z` (extending Gate 2 at `2026-11-27T23:33:03Z`)
- **Verdict:** **PASS** (novel; `0` prior resolutions over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$ found)

## Exact Checks Run & Observed Results

1. **Snapshot grep (from Gate 2, `880` files):** `watch/snapshots/arxiv/*` (`2609.07769v2` + `last_sweep_report.json`) and `AlexenderSokolov__cross-theory-formal-database.json` (`CC-BY-4.0.txt` license) only (`0` settlements).
2. **GitHub PRs / Issues (`00:29:22Z`):**
   - `gh search prs "2609.07769"` -> `[]`
   - `gh search issues "2609.07769"` -> `[]`
3. **Live `1337isnot1337/solved-conjectures` HEADs (`00:29:22Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `07d52b8f6b5ab5b086e43cb0eb381397d14fd44c` (*"Extend window rigidity to arbitrary weights by domination compression"*) — unrelated.
4. **arXiv / Zenodo / ECCC / Web Search (`00:29:22Z`–`00:29:47Z`):**
   - arXiv API (`id_list=2609.07769`): latest version `2609.07769v2` (`2026-11-25T13:37:50Z`).
   - Zenodo API (`q=2609.07769`): `0` hits.
   - `search_web` (`site:eccc.weizmann.ac.il` and general web): returns only `arXiv:2609.07769` itself (`0` ECCC hits, `0` follow-up resolutions over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$).
5. **Independent Check Execution & AST Audit (`#2158`):**
   - Command: `.venv/bin/python -u targets/radici-2609.07769-open/notes/check-check-1.py`
   - Exit status: `0`, raw output ending in `PASS` (all 15 `BASE_N2` exact pairs, `LEMMA5_COEFFS`, `CASE2`–`CASE6`, `EXACT GRM_5(2,3)^perp A_0..7`).
   - AST check: `AST_FLOATS: []`, `FLOAT_CALLS: []`.

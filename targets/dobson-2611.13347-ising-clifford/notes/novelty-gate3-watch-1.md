# Gate 3 Novelty Receipt — `targets/dobson-2611.13347-ising-clifford/` (`watch-1`)

- **Target:** `targets/dobson-2611.13347-ising-clifford/` (*Computational Power of Clifford and Ising Quantum Computers*, Sawyer Dobson and Zhenghan Wang, `arXiv:2611.13347v1` [`quant-ph`, `cs.CC`, `math.QA`], §5 `sections/5.tex` L11 Problem (3): ancilla-assisted Ising braiding vs Clifford, `PUSB`/`LUSB` vs `PUSC`/`LUSC`)
- **Checked At (UTC):** `2026-11-28T01:14:57Z`–`2026-11-28T01:15:16Z` (live refresh after Gate 2 at `2026-11-27T22:36:41Z`)
- **Verdict:** **PASS** (novel; `0` prior resolutions of §5 Problem (3) found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep (`01:14:57Z`):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.13347" "PUSB" "LUSB" "Computational Power of Clifford and Ising"`
   - Result: `0` settlements across `936` snapshot files (`watch/snapshots/arxiv/*` indexing `2611.13347v1` itself with `cited_by=0`/`S2=0`, plus unrelated substring hits).
2. **GitHub PRs / Issues (`01:14:57Z`):**
   - `gh search prs "2611.13347"` -> `[]`
   - `gh search issues "2611.13347"` -> `[]`
   - (Earlier Gate 2 GH code search `"2611.13347"` returned only automated Nov 11–12 arXiv digest JSONs; `"PUSB" "LUSB"` and `"LUSC" "Ising"` returned `[]`.)
3. **Live `1337isnot1337/solved-conjectures` HEADs (`01:14:57Z`):**
   - `main`: `4207a936b7bc1b722ad3f8d1b0fa090e8763b048` (*Heinig’s Andrásfai bipartification conjecture*) — unrelated.
   - `research`: `611e7d49832c535b30a6e2d7c25dc68ab51670dd` (*"Strengthen the seven-draw pentagon constraints with root-aware cuts"*) — unrelated.
4. **arXiv / Zenodo / ECCC / Web Search (`01:14:57Z`–`01:15:09Z`):**
   - arXiv API (`id_list=2611.13347`): sole version `2611.13347v1` (`2026-11-09T23:19:02Z`).
   - Zenodo API (`q=2611.13347`): `0` hits.
   - `search_web` (`site:eccc.weizmann.ac.il` and general web): returns only `arXiv:2611.13347` itself (`0` ECCC hits, `0` follow-up resolutions of §5 Problem (3)).
5. **Independent Check Execution (`#2178`):**
   - Command: `.venv/bin/python -u targets/dobson-2611.13347-ising-clifford/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `MAJORANA_AND_NOGO: PASS`
     - `ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS`
     - `ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS`
     - `PASS`

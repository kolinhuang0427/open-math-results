# Gate 3 Novelty Check — `vasilyev-2611.20344-q7.10` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:09:07Z`–`2026-11-27T17:09:14Z`
- **Target:** `targets/vasilyev-2611.20344-q7.10/` — Oleg Vasilyev, *"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"* (`arXiv:2611.20344v2`, `2026-11-18`), Subsection 5.4 & Section 7 Question 7.10 (`q:supremum`)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**YES**: $\sup_{S, C} \pi_C(S) = \log_3 2$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.20344" "q:supremum"`):**
   - `18` lines across `9/745` files (`watch/snapshots/arxiv/*` tracking `2611.20344v2` itself + `s66lem`/`OjasMor`/`andrheabacor` covering Q7.1 only); `0` hits on `q:supremum` or Question 7.10.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:09:07Z`):**
   - `main` = `c68da92f29d66e63c62c720508423f922eecc0f5` (`2026-11-27T17:04:54Z`, PR `#1066`, Chen–Khare–Sahi Conjecture 4) — unrelated.
   - `research` = `481bc25b4755950453c5e984dbfd102dd99ba700` (`2026-11-27T17:08:05Z`, complementary uncountably chromatic graphs) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.20344"` -> `0` hits (`[]`).
   - `gh search issues "2611.20344"` -> `1` hit (`the-omega-institute/trureturing#32194`, open, Q7.7 forcing divergence only — not Q7.10).
   - `gh search code "q:supremum" "Vasilyev"` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2611.20344`) -> `2611.20344v2` (`2026-11-18T03:50:40Z`), latest version.
   - Zenodo API (`q=2611.20344`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Vasilyev's paper.
   - Web search -> only Vasilyev's `arXiv:2611.20344` paper and index entries; `0` resolutions of Question 7.10 (`q:supremum`).
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:09:14Z`; private repositories and non-indexed preprints remain unobservable.

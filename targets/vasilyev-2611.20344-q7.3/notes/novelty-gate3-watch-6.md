# Gate 3 (<1h) Live Novelty Receipt (`watch-6`) — `targets/vasilyev-2611.20344-q7.3/`

- **Checked UTC:** `2026-11-27T14:02:07Z`–`2026-11-27T14:02:11Z` (extending Gate 2 live check at `13:56:28Z`)
- **Target:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (2026-11-18), Section 7 **Question 7.3** (`\label{q:types}` / Remark 4.4 `\label{rem:types}`).
- **Audit Status:** `@audit-1` **PASS** (`AUDIT.md`, `#1497`, zero-float `notes/check-check-2.py` `PASS`).
- **Verdict:** **OPEN / CLEAR FOR GATE 5 REPORTING**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `721` post-Sweep-11 snapshot files):**
   - `2611.20344` -> hits only `watch/snapshots/arxiv/*` indices and `OjasMor`/`andrheabacor`/`s66lem` (all Question 7.1 only, NOT Question 7.3 `q:types`).
   - `q:types`, `rem:types` -> **`0` hits** (`0/721`).
2. **Live arXiv, GitHub & Zenodo:**
   - `export.arxiv.org/api/query?id_list=2611.20344` -> sole latest version `http://arxiv.org/abs/2611.20344v2` (`2026-11-18T03:50:40Z`).
   - `gh search repos/prs "2611.20344"` -> `[]`; `gh search issues "2611.20344"` -> solely `the-omega-institute/trureturing#32194` (open, Question 7.7 only).
   - `zenodo.org/api/records?q=2611.20344` -> `0` hits.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all public channels searched confirm Question 7.3 (`q:types`) remains open.

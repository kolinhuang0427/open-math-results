# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/campbell-2509.16034-conj1/` (Campbell–Currie–Rampersad `arXiv:2509.16034v1` / *INTEGERS* 26 #A34 §3 open problems on Thue–Morse reduced abelian complexity)
- **Verdict:** **CONTESTED**
- **Checked UTC:** `2026-11-26T23:57:39Z`
- **Requested by:** `@scout2-4` (board #451)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files):**
   - Command: `.venv/bin/python tools/novelty_grep.py A360949 2509.16034 2505.12035 "Campbell" "Rampersad" "Li-Lu-Luo"`
   - Result: `0` hits for `2509.16034` (`trureturing` git tree truncated in API snapshot; caught via live `gh search code`).
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search code "2509.16034"` -> **HIT** in `the-omega-institute/trureturing`:
     - `Problems/campbell-currie-rampersad-eq-11.md` (commit `04a561c88d`, `2026-09-08` & commit `96baee8682`, `2026-09-14` nonautomaticity)
     - `Problems/thue-morse-reduced-abelian-odd.md`
     - `Library/Words/campbell2025reduced.md`
     - `Blueprint/D5/S1/Words/Complexity/ThueMorseReducedAbelianEven.md`
   - Also appeared in `the-omega-institute/trureturing-pages` (`site/assets/research-news.json`, `claim-audit.v1.json`) and `the-omega-institute/trureturing-source-theories`.
3. **arXiv (`tools/arxiv_fetch.py`) & Web Search (`search_web`):**
   - `2509.16034v1` (`2025-09-19`) is sole arXiv version; journal publication *INTEGERS* 26 (2026) #A34 retains §3 open problems.

## Match Summary
Filed `targets/campbell-2509.16034-conj1/CONTESTED.md` documenting prior settlement in `the-omega-institute/trureturing`.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts.

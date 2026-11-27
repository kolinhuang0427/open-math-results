# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/oeis-A360949/` (`OEIS A360949` rev 15, Paul D. Hanna Mar 2023 conjecture: $a(0)=1$, $a(2\,\mathrm{A161674}(k)+1) \equiv 2 \pmod 4$, else $a(n) \equiv 0 \pmod 4$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:47:02Z`
- **Requested by:** `@scout-6` (board #449)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A360949 2509.16034 2505.12035 "Campbell" "Rampersad" "Li-Lu-Luo"`
   - Result: `0` hits for `A360949` across all 356 snapshot files.
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A360949&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A360949 rev: 15 time: 2023-03-05T12:37:19-05:00`; comment still reads `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4).`
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A360949 OR 2509.16034 OR 2505.12035"` -> `[]`
   - `gh search issues "\"A360949\" OR \"2509.16034\" OR \"2505.12035\""` -> `[]`
   - `gh search code "A360949"` -> only `gfis/OEIS-prog/prog/gp/a360/A360949.gp` plus unrelated binary/CSV/ID strings; no proof.
4. **arXiv (`tools/arxiv_fetch.py`) & Web Search (`search_web`):**
   - `arxiv_fetch.py query 'all:"A360949" ...'` -> `0` hits for `A360949`.
   - `search_web` -> no prior proof found.

## Near Misses
- `gfis/OEIS-prog` (`A360949.gp`) computes sequence terms only.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not citing `A360949`.

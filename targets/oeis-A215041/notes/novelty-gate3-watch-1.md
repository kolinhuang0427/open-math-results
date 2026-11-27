# Gate 3 Novelty Receipt — `targets/oeis-A215041/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:30Z`
- **Target:** OEIS `A215041` (`rev. 10`, `2023-12-25`), Wolfdieter Lang's conjectured formula for $n^{\delta(n)} / \mathrm{Disc}(C(n,x))$ (`arXiv:1210.1018v2` Open Problem #1).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`653` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Cohen Zenodo `24384895`, Zenodo `23112421`/`23114921`, `OtherMindset/congress-lean`):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A215041" "1210.1018"` -> `0` lines across `0/653` files.
2. **Newly Discovered Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86` `2026-11-19`) -> `0` matches for `A215041` or `1210.1018`.
   - Zenodo `10.5281/zenodo.24366920` (Lien-Hung Su, `2026-11-20`) & Zenodo `10.5281/zenodo.23760779` (`2026-10-29`) -> `0` matches for `A215041` or `1210.1018`.
3. **Live OEIS JSON:**
   - `https://oeis.org/search?q=id:A215041&fmt=json` -> `rev. 10` (`2023-12-25T18:06:42-05:00`), unchanged, conjectures remain open.
4. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A215041" OR all:"1210.1018"'` -> `total_results: 0`.
   - `curl -s "https://zenodo.org/api/records?q=A215041&size=5"` & `q=1210.1018` -> `0` hits each.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"A215041"'` -> `0` hits; `gh search prs '"A215041"'` -> `1` unrelated PR (`safariarash7777-source...#403`).
   - `search_web` (`"A215041" proof OR "1210.1018" "Open Problem 1"`) -> cites only OEIS `A215041` and Lang `arXiv:1210.1018`; no proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** `A193681` (discriminants of $C(n,x)$) and `arXiv:1210.1018v2` itself (poses Open Problem #1 without proof).
- **Coverage limits:** Unindexed private notes or preprints not mentioning `A215041`/`1210.1018` are not covered.

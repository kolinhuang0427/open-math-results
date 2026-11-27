# Gate 3 Novelty Receipt — `targets/oeis-A176126/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:34Z`
- **Target:** OEIS `A176126` (`rev. 18`, `2022-08-27`), R. J. Mathar's Dec 12 2010 conjectured g.f. `(x^4-x^3+3*x^2-x+1)*(x^4-x^3-2*x^2-x+1) / ((x-1)^3*(x^2+1)^3)` and 9-term recurrence.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A176126"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` & `10.5281/zenodo.23760779` -> `0` hits.
3. **Live OEIS JSON (`11:34Z`):**
   - `https://oeis.org/search?q=id:A176126&fmt=json` -> `rev. 18` (`2022-08-27T03:13:41-04:00`), unchanged, Mathar's formula/recurrence still marked `Conjecture:`.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A176126"'` -> `0`; Zenodo `q=A176126` -> `0`; `gh search issues '"A176126"'` -> `0`; `search_web` -> no proof of `A176126` found.

## Near-Misses & Coverage Limits
- **Near-misses:** `A127276` (settled independently in Lemma 1 of this target; no external `A176126` proof found).
- **Coverage limits:** Private repositories and works without `A176126` identifiers are not covered.

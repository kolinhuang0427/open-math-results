# Gate 3 Novelty Receipt — `targets/marberg-2611.19371-conj/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:29Z`
- **Target:** `arXiv:2611.19371v1` (Eric Marberg, Alejandro H. Morales, Tianyi Yu), Section 3.3 **Conjecture 3.8** (`\label{iG-conj}`) — Bumpless pipe dream formula for involution Grothendieck polynomials $\widehat{\mathfrak{G}}_z^{(\beta)}$.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`653` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.19371" "iG-conj" "Conjecture 3.8" "InvBPD"` -> `14` lines across `6/653` files: only the arXiv metadata entries for `2611.19371v1` itself (`watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,last_sweep_report.json,state.json}`), plus two unrelated false positives (`trureturing-requests#720` citing a journal Conjecture 3.8 on reciprocal-norm sums, and `mt0-svg__adversarial-bco.json` filename `config-conj1.json`).
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "Bumpless pipe dreams for involutions" "Marberg"` -> `8` lines across `3/653` files: only `2611.19371v1` and `2611.34697v1` (Hamaker–Weigandt, symplectic BPDs; Remark `rem:orthogonal` explicitly leaves involution/orthogonal Grothendieck BPDs open).
2. **Live arXiv API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2611.19371` -> `total_results: 1`, `2611.19371v1` (`2026-11-14T12:23:48Z`) remains the sole version.
3. **Live Zenodo API:**
   - `curl -s "https://zenodo.org/api/records?q=2611.19371&size=5"` -> `0` hits.
4. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"2611.19371"'` -> `0` issues.
   - `gh search prs '"2611.19371"'` -> `0` PRs.
   - `search_web` (`"2611.19371" OR "Bumpless pipe dreams for involutions and shifted plane partitions" proof OR conjecture 3.8`) -> returns only the original preprint `arXiv:2611.19371v1`; no published solution.

## Near-Misses & Coverage Limits
- **Near-miss:** `arXiv:2611.34697v1` (Hamaker–Weigandt) studies symplectic bumpless pipe dreams and notes the involution/orthogonal Grothendieck BPD problem remains open.
- **Coverage limits:** Unindexed preprints posted after the most recent arXiv/Zenodo sweep or private repositories are not covered.

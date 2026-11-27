# Gate 3 Novelty Receipt — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T12:09Z`
- **Target:** Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, Yuchen Xu (`arXiv:2609.13361v1`, `2026-09-11`), Section 7 **Conjecture 7.5** (`\label{conj:C>=3 ind}`), **Conjecture 7.4** (`\label{conj:unique}`), and cographic vertex-star characterization (Corollary 2).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`709` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, Sweep 7 `529` repos incl. `cmu-l3/reuF2F`, `insorrowmeow/oeis-sequence-proofs`, Zenodo compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2609.13361" "conj:C>=3 ind" "conj:unique"` (`12:09Z`) -> `5` lines across `1/709` files: `tamnd__arxiv.json` (arXiv metadata/census index only).
   - Direct `gh api` inspection of `cmu-l3/reuF2F/lean/reuF2F/dochtermann2026matroids.lean` (`12:09Z`): contains only an unproved Lean statement stub `theorem conjecture_7_5 ... := by sorry`.
2. **Live arXiv & Zenodo APIs (`12:09Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2609.13361,2509.11460,2609.17446`: `2609.13361v1` (`2026-09-11`) and `2509.11460v1` (`2025-09-14`) remain sole versions; `2609.17446v2` (SuHo Oh, `2026-09-19`) studies relaxed coparking for Stanley's conjecture and does not resolve Conjecture 7.4 or 7.5.
   - `curl -s "https://zenodo.org/api/records?q=2609.13361&size=3"` -> `0` hits.
3. **Live GitHub & Web Search (`12:00Z`–`12:09Z`):**
   - `gh search issues`/`prs` for `"2609.13361"` and `"circuit system" matroid` -> `0` hits each.
   - `search_web` -> returns only `2609.13361v1` itself; no settlement of Conjecture 7.4 or 7.5 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `cmu-l3/reuF2F/lean/reuF2F/dochtermann2026matroids.lean` (`conjecture_7_5` statement stub with `sorry`); `arXiv:2609.17446v2` (relaxed coparking functions).
- **Coverage limits:** Private repositories and works without `2609.13361` or `conj:C>=3 ind` identifiers are not covered.

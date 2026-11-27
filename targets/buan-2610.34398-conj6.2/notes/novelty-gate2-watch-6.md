# Gate 2 Novelty Check (`watch-6`): `targets/buan-2610.34398-conj6.2/`

- **Checked UTC:** `2026-11-27T11:34:38Z`
- **Target:** Aslak B. Buan, Eric J. Hanson, and Bethany R. Marsh, *"Lifting $\tau$-exceptional sequences"*, `arXiv:2610.34398v1` (`2026-10-25`), Section 7.1, **Conjecture 7.2** (`\label{conj:TFordered}`).
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2610.34398 Buan "TF-ordered"` -> `# 0 lines across 0/658 files in 0.54s`.
2. **Live arXiv (`.venv/bin/python -u tools/arxiv_fetch.py abs 2610.34398`):**
   - `2610.34398v1` remains the sole and latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=2610.34398`):**
   - `hits.total: 0`.
4. **GitHub search (`gh search repos 2610.34398 --limit 5`, `gh search issues 2610.34398 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
5. **Web search (`search_web` for `"2610.34398" Buan Hanson Marsh "Conjecture 7.2" OR "TF-ordered" proof`):**
   - Returned only `arXiv:2610.34398` and Buan–Hanson–Marsh's earlier `arXiv:2402.10301`; no resolution of Conjecture 7.2 found.

## Coverage Limits

- arXiv query did not run an author-citing search for follow-up `math.RT` papers beyond the `search_web` sweep and `658`-file snapshot index; offline or unindexed manuscripts are outside direct visibility.

# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A176126/`

- **Checked UTC:** `2026-11-27T11:24:50Z`
- **Target:** OEIS `A176126` (`rev. 18`, `2022-08-27T03:13:41-04:00`) — R. J. Mathar's Dec 12 2010 conjectured 9-term linear recurrence and generating function `(x^4-x^3+3*x^2-x+1)*(x^4-x^3-2*x^2-x+1) / ((x-1)^3*(x^2+1)^3)` for `Numerator of -A127276(n)/A001788(n)`.
- **Verdict:** **PASS** (no prior settlement found)

## Exact Queries & Results

1. **Snapshot grep (653 files incl. Blanco Gómez Zenodo `23112421`/`23114921`, Cohen Zenodo `24384895`, `OtherMindset/congress-lean`, Su Zenodo `24366920`/`23760779`):**
   - `.venv/bin/python -u tools/novelty_grep.py A176126 176126` -> `# 0 lines across 0/653 files in 1.20s`
   - Cross-check against Su Zenodo `24366920` (46 OEIS IDs) & `23760779` (12 OEIS IDs): `False` (`0` matches).
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A176126&fmt=json`):**
   - `rev: 18`, `time: 2022-08-27T03:13:41-04:00`; Mathar's Dec 12 2010 recurrence and g.f. remain labeled `Conjecture:`.
3. **Zenodo API (`https://zenodo.org/api/records?q=A176126`):**
   - `hits.total: 0`.
4. **arXiv metadata API (`.venv/bin/python -u tools/arxiv_fetch.py query "all:A176126"`):**
   - `total_results: 0`.
5. **GitHub search (`gh search repos A176126 --limit 5`, `gh search issues A176126 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
6. **Web search (`search_web` for `"A176126" Mathar generating function recurrence proof`):**
   - Returned only OEIS `A176126` and generic Mathar/D-finite methodology; `0` proofs of Mathar's `A176126` recurrence/g.f. conjecture surfaced.

## Near-Misses

- OEIS `A127276` (numerator source, `targets/oeis-A127276/`) proves the closed form `2^n - n(n+1)2^{n-2}` for `A127276(n)`, which is only an auxiliary ingredient; `A176126` depends on the gcd reduction `-A127276(n)/A001788(n) = (n^2+n-4)/(n^2+n)` modulo `gcd(4, n^2+n)`.

## Coverage Limits

- arXiv query searches metadata fields rather than PDF full text; private/offline manuscripts not indexed by Zenodo, arXiv metadata, GitHub, or web search are outside direct visibility.

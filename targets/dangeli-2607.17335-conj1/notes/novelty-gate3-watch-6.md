# Gate 3 Novelty Check (`watch-6`): `targets/dangeli-2607.17335-conj1/`

- **Checked UTC:** `2026-11-27T11:32:31Z`
- **Target:** Daniele D'Angeli & Emanuele Rodaro, *"On totally synchronizing graphs"*, `arXiv:2607.17335v1` (`2026-07-19`), Section 4, **Conjecture 4.6** (`\label{conj:typical-total-simplicity}`) — disproved at $k = 2$ via $\Pr(\text{totally simple} \mid \mathrm{SCC}_n) \le 29/30$ for all $n \ge 4000$.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior disproof or settlement found)

## Exact Queries & Results

1. **Snapshot grep (657 files incl. Blanco Gómez `23112421`/`23114921`, Cohen `24384895`, `OtherMindset/congress-lean`, Su `24366920`/`23760779`, `mylesparslow-collab`, and 2026 Zenodo compendia):**
   - `.venv/bin/python -u tools/novelty_grep.py 2607.17335 DAngeli "totally simple"` -> `# 1 lines across 1/657 files`: `AlexenderSokolov__cross-theory-formal-database.json:38204` (`editable-corpus/licenses/arxiv-2607.17335-CC-BY-4.0.txt`, source license metadata only, no resolution).
2. **Live arXiv API (`.venv/bin/python -u tools/arxiv_fetch.py abs 2607.17335`):**
   - `2607.17335v1` (`2026-07-19`) remains the sole and latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=2607.17335`):**
   - `hits.total: 0`.
4. **GitHub search (`gh search repos 2607.17335 --limit 5`, `gh search issues 2607.17335 --limit 5`):**
   - `[]` (repos) and `[]` (issues).
5. **Web search (`search_web` for `"2607.17335" D'Angeli "total simplicity" OR "Conjecture 4.6" counterexample`):**
   - Returned only the original `arXiv:2607.17335` preprint; no prior disproof found.

## Coverage Limits

- arXiv API does not search PDF full text of unrelated papers; offline or unindexed manuscripts are outside direct visibility.

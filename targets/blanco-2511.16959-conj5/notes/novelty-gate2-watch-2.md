# Gate 2 Novelty Receipt — `blanco-2511.16959-conj5`

- **UTC Time:** 2026-11-27T01:48:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #587)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2511.16959" "prefix_reversal" "F_k(n)"`: 0 matches for `2511.16959` across 369 snapshot files (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2511.16959,2610.30892`: `2511.16959v3` (DMTCS 28:1, 2026, `10.46298/dmtcs.16975`) remains latest; `2610.30892v1` (Lei–Zhao–Zhu–Wu) proves Conjectures 2–4 only, not Conjecture 5 (`con:F_k(n)`).
3. **Live GitHub (`gh api`, read-only):**
   - Inspected `the-omega-institute/trureturing#20814` (`Preregister: whole arXiv2511.16959 Conjecture 5 maximum generating middle-prefix count`): **open**, `comments: 0`, 0 linked PRs or settled files (`trureturing` settled Conjecture 4 and refuted Conjecture 1 only).
   - Inspected `rainwangphy/aftd-platform` `PrefixReversal*.lean` (8 files: `NotPrefixReversalSumBoundNecessary.lean`, `PrefixReversal.lean`, `PrefixReversalGcdDiffNecessary.lean`, `PrefixReversalGroup.lean`, `PrefixReversalGroupLeIff.lean`, `PrefixReversalInvolutive.lean`, `PrefixReversalNecessaryConditionsNotSufficient.lean`, `PrefixReversalSixFiveThreeNotTop.lean`): formalizes `arXiv:2610.30892` non-generation/Conjecture 1 counterexample conditions, not Conjecture 5 (`con:F_k(n)`).
   - Checked `JENW1N/complete-math-solutions` (425 files), `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, `valyuAI/research`, `facebookresearch/atlas-lean`, `TheJustinSunPrize/awards`: 0 hits for `2511.16959`.
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=2511.16959+OR+%22prefix+reversal%22+symmetric&size=10` (top 5 unrelated; no `2511.16959` record).
   - `search_web` for `"2511.16959" OR "F_k(n)" "prefix reversal" OR "2610.30892"`: returns only `2511.16959` and `2610.30892`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2610.30892v1` (Lei–Zhao–Zhu–Wu) and `rainwangphy/aftd-platform` (`PrefixReversal*.lean`): prove non-generation conditions / Conjecture 2–4 / Conjecture 1 refutation, not the exact maximum $\max_{n > k+1} |F_k(n)|$ in Conjecture 5.
- `the-omega-institute/trureturing#20814`: open preregistration for Conjecture 5 with 0 comments and no solution PRs/files.

## What Was Not Covered

- Closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, or web search.

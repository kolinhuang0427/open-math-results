# Gate 2 Novelty Receipt — `blanco-2511.16959-conj5`

- **UTC Time:** 2026-11-27T01:35:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 11 (`2026-11-27T01:16:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2511.16959 "F_k(n)" Golubyatnikov "prefix reversal" 2610.30892` -> 0 hits on `2511.16959` or prefix reversals.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing*`, `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math`, `facebookresearch/atlas-lean` (`gh api`, read-only):**
   - `repos/the-omega-institute/trureturing/issues/20814` -> state `open` (`closed: None`), timeline shows only cross-reference `#22875` (Conj 1), no PR or solution. `trureturing` code hits for `2511.16959` cover only Conj 4 (`PrefixReversalTriple{Odd,Even}NonGeneration`) and Conj 1 refutation (`PrefixReversalTripleCountRefutation`), NOT Conjecture 5 (`con:F_k(n)`).
   - `rainwangphy/aftd-platform` (`web/data/traces/prefix_reversal_*.json`) covers only necessary conditions / `sum_bound` / `gcd_diff` / `six_five_three_not_top` (Conj 1–4), not `con:F_k(n)`.
   - `1337isnot1337/solved-conjectures`, `trureturing-tools`, `facebookresearch/atlas-lean`, `aliromman/math`, `KnowledgeSense/math`, `valyuAI/research` -> 0 matches.
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2511.16959,2610.30892` -> `2511.16959v3` & `2610.30892v1` (proves Conj 2–4 only, not Conj 5).
   - `https://zenodo.org/api/records?q=2511.16959&size=5` -> `total: 0`.
   - `search_web` for `"2511.16959" ("Conjecture 5" OR "F_k(n)" OR "2610.30892")` -> no prior proof of Conjecture 5 found.

## Near Misses

- `2610.30892v1`, `trureturing#7558`/`#7577` (Conj 4), `trureturing#22875` (Conj 1), and `rainwangphy/aftd-platform` prefix-reversal traces (Conj 1–4), none addressing `con:F_k(n)`.
- `trureturing#20814` is an open empty preregistration.

## What Was Not Covered

- Private repositories and offline manuscripts.

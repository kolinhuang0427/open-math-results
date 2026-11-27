# Gate 3 Novelty Receipt (`watch-3`) — `targets/daugherty-2610.29291-conj6.1/`

- **Checked (UTC):** `2026-11-27T03:09:32Z` – `2026-11-27T03:12:42Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Conjecture 6.1 `conj:box` of `arXiv:2610.29291v1`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 469 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py 2610.29291 Daugherty "conj:box" "6,5,5,3,3,1" "Latin tableaux"` -> `7` lines across `5/469` files (citing cache + `rainwangphy/aftd-platform` Conjecture 6.3 description).
2. **Live competing GitHub repository trees (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`18,812` files, `pushed=2026-11-27T03:09:32Z`), `aliromman/math` (`787` files), `KnowledgeSense/math` (`4,941` files), `JENW1N/complete-math-solutions` (`325` files), `GuillaumeBAUD-coder/open-math-agents` (`1,453` files), `DomTheDeveloper/open-math-agents` (`377` files), `DomTheDeveloper/ProofPlaygrond` (`60` files), `CrocSwap/integer-mult-bounds` (`47,048` files, `trunc=True`), `linustalacko/small-true-things` (`29` files) -> `0` matches for `2610.29291`, `daugherty`, `conj:box`, `6,5,5,3,3,1`.
   - `rainwangphy/aftd-platform` (`28,138` files, `pushed=2026-11-27T03:00:24Z`) -> `LatinDoubleThreeTail*` covers ONLY Conjecture 6.3 (plus `IsLatinTableau`/`IsLatinPartition` definitions and unrelated game theory).
   - `valyuAI/research` (`5,110` files, `pushed=2026-10-27T16:11:42Z`) -> `maths/combinatorics/latin-squares/latin-tableaux-staircase-count/README.md` covers ONLY Conjecture 6.3 (`32`-cell staircase shapes).
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`) -> `0` matches.
3. **Live GitHub issue searches (`gh api`):**
   - `the-omega-institute/trureturing`: `2610.29291` / `Daugherty` -> `#20269` & `#20329` (Conj 6.3), `#26377` (Conj 6.2), `#24283`/`#24265` (Tamari); `0` hits for Conjecture 6.1 (`conj:box`).
   - `facebookresearch/atlas-lean`: `2610.29291` -> `0`; `Daugherty` -> `10` hits on metered parking functions only.
   - `TheJustinSunPrize/awards`: `2610.29291`, `"Latin tableaux"` -> `0` hits.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=...` for `2610.29291`, `"6,5,5,3,3,1"`, `"conj:box"` -> `total=0` for all 3 queries.

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing#20329`, `rainwangphy/aftd-platform` (`LatinDoubleThreeTailCountFormula.lean`), `valyuAI/research` (`latin-tableaux-staircase-count`): Settle Conjecture 6.3 ($LT((k,k-1,\dots,3,3)) = 9\cdot 4^{k-3}$), not Conjecture 6.1 (`conj:box`, box-addition monotonicity).
- `the-omega-institute/trureturing#26377`: Open research issue targeting Conjecture 6.2 (column-addition monotonicity), not Conjecture 6.1.

## What Was Not Covered
- `CrocSwap/integer-mult-bounds` tree was truncated past 47,048 entries (`trunc=True`). Unindexed private repositories and closed-access publications not mirrored in GitHub or Zenodo.

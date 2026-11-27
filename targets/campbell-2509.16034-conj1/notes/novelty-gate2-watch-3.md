# Gate 2 Novelty Receipt (`watch-3`) — `targets/campbell-2509.16034-conj1/`

- **Checked (UTC):** `2026-11-26T23:55:42Z` – `2026-11-27T00:09:39Z`
- **Verdict:** **CONTESTED** (`CONTESTED.md` already filed by `watch-6`; confirmed independently via `the-omega-institute/trureturing` PRs `#5701`, `#6106`, `#6463`, `#8026` and `trureturing-mdbook#5`)

## Sources Checked & Findings
1. **Local watch snapshots (`watch/snapshots/**`, 357 files):**
   - `.venv/bin/python tools/novelty_grep.py 2509.16034 Campbell Currie Rampersad "reduced abelian"` -> 37 lines across 21/357 files (`1337isnot1337/solved-conjectures#154` is Currie's complexity $2n+1$ Conjecture 19, unrelated).
2. **Live `the-omega-institute/trureturing` (`gh api`):**
   - **PR `#5701`** (`Problems/thue-morse-reduced-abelian-odd.md`, `D5/S1/Words/Complexity/ThueMorseReducedAbelianOdd`, `reducedAbelianComplexity_odd`, frozen 2026-09-06; also `trureturing#6106`, `trureturing-mdbook#5`): Proves and Lean-formalizes $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(2n+1) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1)$.
   - **PR `#6463`** (merged `2026-09-08T15:31:08Z`, `https://github.com/the-omega-institute/trureturing/pull/6463`, `reducedAbelianComplexity_even_difference`): Proves and Lean-formalizes Equation (11) / `\eqref{displayconjecture}` (`|(R(4n+2):Int) - R(4n)|.natAbs = if thueMorse n = thueMorse (3*n) then 0 else 1`) via `alternation_extrema_parity` and interval/shift arguments.
   - **PR `#8026`** (merged `2026-09-15T04:58:21Z`, `https://github.com/the-omega-institute/trureturing/pull/8026`): Documents non-$k$-automaticity of sequence (10) from the existing recurrences (`w(4n+1) = w(n)+1`).
3. **Live `the-omega-institute/trureturing-tools`, `aliromman/math`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, Zenodo:**
   - `trureturing-tools` `SCREENED-OUT*.md`: only unrelated `Campbell–Cohen` mention in `SCREENED-OUT-R71.md`.
   - `aliromman/math`: `#82` is Campbell's coupon-collection conjecture (unrelated).
   - `KnowledgeSense/math` (4,941 files), `1337` (`CONTENTS.md` / issues), Zenodo (`2509.16034`, `"reduced abelian complexity"`): 0 hits for `2509.16034`.

## Near Misses / Scope Note
- `facebookresearch/atlas-lean` (`#8579`, `#9025`, `#8223`): Doubling/quadrupling recurrences for Thue–Morse alternation extrema (discovered via GitHub issue search on `Campbell Rampersad` — reported to `@watch-6` as an unlisted competing repo).
- `trureturing#6463` already settles both the odd recurrence (`#5701`), equation (11) (`#6463`), and non-$k$-automaticity (`#8026`), leaving at most the explicit signed difference `(M_{n+1} mod 2) - (m_{n+1} mod 2)` (implied by `alternation_extrema_parity` + shift) and the sign of $\rho(4n+2)-\rho(4n)$.

## What Was Not Covered
- Unindexed private repositories and closed-access journals beyond arXiv/INTEGERS/GitHub/Zenodo.

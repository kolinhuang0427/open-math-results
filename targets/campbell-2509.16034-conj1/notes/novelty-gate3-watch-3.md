# Gate 3 Novelty Receipt (`watch-3`) — `targets/campbell-2509.16034-conj1/` (Rescoped `(c1)` + `(c2)`)

- **Checked (UTC):** `2026-11-27T02:32:42Z` – `2026-11-27T02:34:54Z`
- **Verdict:** **PASS** for the rescoped claims **(c1)** explicit sign of $\rho(4n+2)-\rho(4n)$ and **(c2)** explicit recursion for $\rho(4n)$ / full recursion & $2$-regularity (noting odd recurrence, eq. (11), and non-$k$-automaticity were settled in `the-omega-institute/trureturing` in Sept 2026 and are explicitly excluded/credited per `TARGET.md` and `contest-ruling-audit-3.md`).

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 413 files):**
   - `.venv/bin/python tools/novelty_grep.py 2509.16034 Campbell Currie Rampersad "reduced abelian"` -> `48` lines across `24/413` files (only unrelated `Currie` complexity $2n+1$ Conj 19 in `1337`).
2. **Live competing GitHub repo trees (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`18,803` files), `aliromman/math` (`747` files), `KnowledgeSense/math` (`4,941` files), `rainwangphy/aftd-platform` (`28,138` files — only unrelated `ThueMorseMinFactorCoverages*`/`ThueMorseRandomAttractor*`), `valyuAI/research` (`5,110` files), `JENW1N/complete-math-solutions` (`325` files), `trureturing-tools` (`SCREENED-OUT*.md`) -> `0` matches for `2509.16034` or `reducedAbelian`.
3. **Live GitHub issue searches (`gh api`):**
   - `2509.16034` and `reducedAbelian OR rho_red` in `facebookresearch/atlas-lean` -> `0` hits.
   - `the-omega-institute/trureturing` (`#5701`, `#6463`, `#8026`) -> explicitly scoped out `(c1)` nonzero sign and `(c2)` $\rho(4n)$ recursion (`Problems/thue-morse-reduced-abelian-odd.md`, PR `#6463`).
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=2509.16034&size=5` -> `total=0`.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in GitHub or Zenodo.

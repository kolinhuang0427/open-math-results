# Check Report — `oeis-A350963`

- Checker: `check-1`
- Checked UTC: `2026-11-27T02:58:09Z`
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source fetched live from OEIS:
  - `https://oeis.org/search?q=id:A350963&fmt=json` (author `_N. J. A. Sloane_`, Feb 25 2022; revision `54`, `2025-11-05T15:22:48-05:00`):
    - Name: `Coordination sequence for the XXOXX tiling with respect to a tile of type R.`
    - Comments: two tiles adjacent if they share a (long or short) edge; R touches 4 R's, 4 G's, 1 B; G touches 4 R's, 1 G, 3 B's; B touches 1 R, 3 G's, 4 B's.
    - Formula: `Conjectured g.f.: -(2*t^7-6*t^6-24*t^5-33*t^4-33*t^3-28*t^2-9*t-1)/((1-t^2)*(1-t^4)).`
    - Data (`offset 0`): 54 terms `1,9,29,42,...,843`.
  - `https://oeis.org/A350963/a350963.gp.txt` (Rémy Sigrist's OEIS-linked PARI/GP file): `DX = 4 - I`, `DY = 6*I`, `H = [0, 1, 3, 4]`, `V = I*H`, `T[1..6]` translates, unit-square edge adjacency `C[1..6]`, root `encode(4, 0)` (type R, `t=3`).
- Comparison against `TARGET.md` and `PROOF.md`: exact match with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Verification

- Verifier script: `targets/oeis-A350963/notes/check-check-1.py` (written strictly from live OEIS `A350963` + `a350963.gp.txt` and `PROOF.md`, without reading `verify.py` or author `notes/`).
- Verified in exact integer and rational/polynomial arithmetic:
  1. **Section 1:** All $6$ base tiles $T_0..T_5$ partition $\mathbb{Z}^2/\Lambda$ into $24$ distinct classes with zero overlaps/gaps (and cover $[-15,15]^2$ uniquely); unit-square edge adjacency across `dx,dy in [-3,3]` yields the exact $50$ directed edges `C[0..5]`, symmetric, with exact R/G/B breakdowns and half-turn automorphism $\iota(u,v)=(3-u,5-v)$ exchanging $T_0 \leftrightarrow T_3, T_1 \leftrightarrow T_2, T_4 \leftrightarrow T_5$.
  2. **Section 2.1:** $D^*(0,0,3)=0$, $1$-Lipschitz differences $|\Delta F_s| \le 1$ across all $50$ directed edges and all $r \equiv x+2y \pmod 3$, and $3$-ray $E_{\mathrm{exc}}$ boundary/descent checks for $0 \le k \le 80$.
  3. **Sections 2.2–2.3:** $-3 \le 3F_s - M_s \le 6$ over a complete period, all $20$ non-adjacent pair relations in `SymPy`, complete $B_{\mathrm{core}} = [-20,20] \times [-10,10] \times \{0..5\}$ ($5{,}166$ vertices: unique $D^* \le 0$ at $(0,0,3)$, every other vertex has a $D^* - 1$ neighbor), and the Case B descent table on $>10{,}000$ collar vertices in $([-35,35]\times[-20,20]) \setminus (B_{\mathrm{core}} \cup E_{\mathrm{exc}})$.
  4. **Section 3:** Exact BFS from $(0,0,3)$ through radius $55$ confirms $d(v) = D^*(v)$ on every reached vertex and matches all $54$ OEIS `A350963` terms; direct counting verifies all $24$ polynomials $|B_t(4m+r)|$ for $1 \le m \le 10$ plus affine ordering/nonnegativity differences for all $m \ge 1$; rational GF expansion matches $a(0..100)$ verbatim.

### Command & Raw Output

```bash
.venv/bin/python -u targets/oeis-A350963/notes/check-check-1.py
```

Raw output (exit code `0`):
```text
Section 1 (XXOXX tiling mod Lambda, [-15,15]^2 patch, 50 edges, R/G/B, half-turn): OK
Section 2.1 (1-Lipschitz F1..F8, D*, and 3 rays R1..R3 k<=80): OK
Sections 2.2-2.3 (B_core 5166 verts + Case B descent table on collar): OK
Section 3 (BFS r<=55 == D*, 54 OEIS A350963 terms, B_t(4m+r), & GF to t^100): OK (0.99s)
PASS
```

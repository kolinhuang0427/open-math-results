# Independent Check Report (`check-3`): `targets/oeis-A108449/`

## 1. Primary-Source Fidelity Check
Checked live OEIS JSON API (`https://oeis.org/search?q=id:A108449&fmt=json`) directly:
- **OEIS `A108449`** (rev `13`, `2025-11-05T15:35:31-05:00`, offset `0,3`):
  - **Name:** `Number of paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1),U=(1,2), or d=(1,-1) and having no pyramids (a pyramid is a sequence u^pd^p or U^pd^(2p) for some positive integer p, starting at the x-axis).`
  - **Formula (_R. J. Mathar_, Jul 26 2022):** `Conjecture D-finite with recurrence +n*(2*n+1)*(431*n-2895)*a(n) +2*(-9395*n^3+68622*n^2-64084*n+26109)*a(n-1) +2*(59288*n^3-508196*n^2+1044822*n-574587)*a(n-2) +2*(-94965*n^3+1070605*n^2-3607435*n+3485484)*a(n-3) +4*(29036*n^3-351474*n^2+1402336*n-1970505)*a(n-4) +6*(-6703*n^3+63052*n^2-99178*n-237177)*a(n-5) +6*(1012*n^3-14914*n^2+74580*n-127341)*a(n-6) +6*(1127*n^3-21429*n^2+135199*n-282762 )*a(n-7) +9*(29*n-165)*(2*n-15)*(n-8)*a(n-8)=0.`
  - **Data:** `1,0,4,32,252,2112,18484,...` (20 terms, `a(0)..a(19)`).

`TARGET.md` and `PROOF.md` match the primary OEIS statement verbatim (quantifier $n \ge 8$, offset `0`, lattice-path definition, and all 9 recurrence coefficients).

## 2. Mathematical Proof Check
Reviewed `targets/oeis-A108449/PROOF.md` Steps 1–4:
- Step 1: Primitive-excursion decomposition $A(x) = 1 + xA(x)^2 + xA(x)^3$, pyramid exclusion $K_{\mathrm{free}}(x) = xA(x)(1+A(x)) - \frac{2x}{1-x} \in x^2\mathbb{Z}[[x]]$, and $y(x) = 1/(1 - K_{\mathrm{free}}(x))$ are combinatorially exact.
- Step 2: Elimination of $A$ via $\mathrm{Res}_A(E_1, E_2) = x^2 P(x, y)$ gives $P(x, y(x)) = 0$ in $\mathbb{Z}[[x]]$. Exact.
- Step 3: $P_y(0, y(0)) = 1$ (unit in $\mathbb{Z}[[x]]$), inductive $N_k$ quotient-rule formula for $y^{(k)} = N_k / P_y^{2k-1}$, and exact $\mathbb{Z}[x, y]$ divisibility $Q(x, y) = P(x, y) R(x, y)$ give the order-3 formal ODE. Exact.
- Step 4: Coefficient extraction for $n \ge 8$ ($\deg p_{\mathrm{inhom}} = 7 < 8$, all shift indices $0 \le d - k \le 8$) yields Mathar's exact 9-term recurrence. Exact.

## 3. Independent Mechanical Verification
Written solely from live OEIS `A108449` definitions and `PROOF.md` without reading `verify.py` or author notes, using exact `int` / SymPy `ZZ` arithmetic (zero floats):
- Script: `targets/oeis-A108449/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/oeis-A108449/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/4] Direct lattice-path DP matches all 20 live OEIS A108449 terms.
[2/4] Step 1 OGF and Step 2 5x5 Sylvester resultant Res_A(E1,E2) = x^2 P(x,y) verified.
[3/4] Step 3 exact Z[x,y] division Q = P*R and order-3 ODE verified.
[4/4] Step 4 symbolic Z[n] coefficient match and recurrence verified for 8 <= n <= 100.
PASS
```

## 4. Verdict
- **PASS** (`Gate 2` `watch-6` PASS in `notes/novelty-gate2-watch-6.md`; `@watch-1`/`@watch-5` Gate 2 pending per `#237`).

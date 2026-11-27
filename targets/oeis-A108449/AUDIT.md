# Blind Audit Report: `oeis-A108449`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:24Z`
**Verdict:** **PASS** — Complete symbolic proof for all $n \ge 8$ (`"written proof, internally audited"`).

## 1. Primary-Source Fidelity
Verified verbatim against live OEIS JSON API (`https://oeis.org/search?q=id:A108449&fmt=json`, revision `13`, `2025-11-05T15:35:31-05:00`, offset `0,3`):
- **NAME:** `Number of paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1),U=(1,2), or d=(1,-1) and having no pyramids (a pyramid is a sequence u^pd^p or U^pd^(2p) for some positive integer p, starting at the x-axis).`
- **FORMULA (_R. J. Mathar_, Jul 26 2022):** Every single sign, factor, and coefficient of all nine cubic polynomials $C_0(n), \dots, C_8(n)$ in `TARGET.md` and `notes/check-check-3.py` matches the live OEIS `Conjecture D-finite with recurrence ... = 0` entry character-for-character, on the natural full domain $n \ge 8$ (offset $0$, $C_0(n) = n(2n+1)(431n-2895) > 0$ for all $n \ge 7$).
- **DATA:** All $20$ live OEIS terms `a(0)..a(19)` match the direct lattice-path DP.

## 2. Line-by-Line Mathematical Audit of `PROOF.md`
1. **Step 1 (Combinatorial OGF from NAME):**
   - Since all steps have $\Delta X > 0$, staying in the first quadrant starting from $(0, 0)$ is equivalent to $Y \ge 0$. Since $\Delta(X+Y) = 3$ for $u, U$ and $0$ for $d$, a path ending on $Y=0$ terminates at $(3n, 0)$ iff $\#u + \#U = n$.
   - First-return decomposition into primitive excursions gives $A(x) = 1 + K(x) A(x)$. A primitive excursion starts with $u$ (contributing $x A(x)$ after stripping initial $u$ and final $d$ and shifting height by $-1$) or $U$ (decomposing uniquely at the first visit to height $1$ via a $d$-step into $U \cdot P_1 \cdot d \cdot P_2 \cdot d$, contributing $x A(x)^2$). Thus $K(x) = xA(x)(1+A(x))$ and $A(x) = 1 + xA(x)^2 + xA(x)^3$.
   - Every pyramid $u^p d^p$ or $U^p d^{2p}$ ($p \ge 1$) starting on $Y=0$ remains strictly at $Y > 0$ internally and returns to $Y=0$ only at its end, so a path contains a pyramid iff one of its primitive excursions equals $u^p d^p$ or $U^p d^{2p}$ (these are pairwise distinct for all $p \ge 1$ since their first steps differ). Hence $K_{\mathrm{free}}(x) = xA(x)(1+A(x)) - \frac{2x}{1-x} \in x^2\mathbb{Z}[[x]]$, and $y(x) = (1 - K_{\mathrm{free}}(x))^{-1} = \frac{1-x}{1+x - x(1-x)A(1+A)}$ with unit denominator in $\mathbb{Z}[[x]]$. Completely rigorous.
2. **Step 2 (Algebraic equation via Sylvester resultant):**
   - Both $E_1(x, A(x)) = 0$ and $E_2(x, y(x), A(x)) = 0$ in $\mathbb{Z}[[x]]$. Because $\mathrm{Res}_A(E_1, E_2) = U E_1 + V E_2$ in $\mathbb{Z}[x, y, A]$ holds universally over any commutative ring (no nonvanishing leading-coefficient assumption required), evaluating at $(y(x), A(x))$ yields $x^2 P(x, y(x)) = 0$ in the integral domain $\mathbb{Z}[[x]]$, hence $P(x, y(x)) = 0$.
3. **Step 3 (Order-3 formal ODE):**
   - $P(0, y) = -1 + y \implies P_y(0, y(0)) = 1$, so $P_y(x, y(x))$ is a unit in $\mathbb{Z}[[x]]$.
   - Verified the quotient-rule induction for $N_{k+1} = (P_y \partial_x N_k + N_1 \partial_y N_k) P_y - (2k-1) N_k (P_y \partial_x P_y + N_1 \partial_y P_y)$ yielding $y^{(k)} = N_k / P_y^{2k-1}$ for $k = 1, 2, 3$, and the cleared numerator $Q(x, y) = P_y^5(p_{\mathrm{inhom}} + p_0 y) + P_y^4 p_1 N_1 + P_y^2 p_2 N_2 + p_3 N_3$.
   - Independently verified exact $\mathbb{Z}[x, y]$ divisibility $Q(x, y) = P(x, y) R(x, y)$ with zero remainder and confirmed the stated degrees $\deg_x R = 24$, $\deg_y R = 8$. Dividing by the unit $P_y(x, y(x))^5$ yields the formal order-3 ODE in $\mathbb{Q}[[x]]$.
4. **Step 4 (Coefficient extraction for $n \ge 8$):**
   - Verified the degree bounds of $p_{\mathrm{inhom}}$ ($\deg = 7 < 8$) and $p_0, p_1, p_2, p_3$ ($0 \le d - k \le 8$ for every monomial $c x^d$ in $p_k$), ensuring all shift indices $m = n - (d - k) \ge 0$ for every $n \ge 8$ and automatic vanishing of the falling factorial when $0 \le m < k$. Term-by-term symbolic identity in $\mathbb{Z}[n]$ recovers $C_0(n), \dots, C_8(n)$ identically.

## 3. Independent Mechanical Verification
Audited and executed `targets/oeis-A108449/notes/check-check-3.py` (exact `int` / SymPy `ZZ` arithmetic, zero floats):
- Command: `.venv/bin/python -u targets/oeis-A108449/notes/check-check-3.py`
- Result: exit `0`, raw `PASS` (direct lattice-path DP matches all 20 live OEIS terms; Step 1–2 OGF & Sylvester resultant verified; Step 3 exact $\mathbb{Z}[x,y]$ division $Q = PR$ and ODE up to $x^{42}$ verified; Step 4 symbolic $\mathbb{Z}[n]$ match to Mathar's $C_0, \dots, C_8$ and direct recurrence check for $8 \le n \le 100$).

## 4. Verdict & Handoff
**PASS.** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final coordinator verification.

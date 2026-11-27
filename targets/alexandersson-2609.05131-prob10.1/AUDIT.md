# Adversarial Audit Report (`audit-1`): `targets/alexandersson-2609.05131-prob10.1/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Per Alexandersson, *Real-rootedness and interlacing for parking functions and Chow polynomials*, `arXiv:2609.05131v2` (2026-09-23), Section 10 (*Further questions*), **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`, `parking-functions.tex` L1879–1881)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, primary source `tools/.arxiv_cache/eprint/2609.05131/parking-functions.tex` (`2609.05131v2`, confirmed latest version on arXiv), and `watch/snapshots/**` (689 files)
- **Verdict:** **PASS** (after Re-Audit #1 verifying `@check-3`'s `#1385` patches to `notes/check-check-3.{py,md}`; `PROOF.md` passed initial audit untouched)

---

## 1. Primary-Source, Version, & Statement Fidelity — PASS

- Verified verbatim against `tools/.arxiv_cache/eprint/2609.05131/parking-functions.tex` (`2609.05131v2`, confirmed latest on `abs/2609.05131.html`):
  - **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`, L1879–1881): *"Do $H_{\mathrm{NC}_{n+1}}(t)$ and $H_{\mathrm{NC}_{n+2}}(t)$ interlace for every $n$?"* — matches `TARGET.md` and `PROOF.md` verbatim.
  - All citations and definitions verified verbatim: Theorem 1.1 (`thm:mainChow`, L144), eq. `(1)` (`eq:introSmirnovTransfer`, L151–157), Proposition 4.1 (`prop:lastLetterRecurrence`, `eq:lastLetterRecurrence`, L479–489), interlacing convention (§4 L499–508), and Table 1 (`tab:ChowTriangle`, L588–611).
  - Gate 2 novelty clear (`watch-5` `#1300`, `watch-1` `#1304`, `watch-6` `#1309`; sole S2 citation `2611.07267` and `RealRooted#665` confirmed unrelated).

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

Every single section of `PROOF.md` was audited line by line and independently recomputed in 40-digit outward-rounded `mpmath.iv` arithmetic:
- **§1 Preliminaries, base cases ($n = 0, 1$), palindromicity, and Lemma 1.1 (rational g.f. (1.2)):** Airtight.
- **§2 Exact integer Sturm–Cauchy ($1 \le n \le 80$):** Proposition 2.1 ($\Gamma$-equivalence via strictly decreasing $u(s) = -s/(1-s)^2$ on $(0, 1)$, reciprocal pairing, and signed primitive PRS Cauchy index $I_{-\infty}^0(\Gamma_n/\Gamma_{n+1}) = d_{n+1}$) is airtight; independently verified for all 80 pairs $1 \le n \le 80$ via exact integer arithmetic.
- **§3 Analytic Identities A & B:** Lemma 3.1 (alternating Fuss–Catalan series + exact ratio bounds (3.4) for $E_0, E_k$) and Lemma 3.2 (Möbius residue $w$-sum (3.5)–(3.6), odd-$n$ sign formula (3.7) at $s = 1$, and harmonic modulus ratio (3.8)) are airtight.
- **§4 Phase analysis, Seam-B, and Regime B ($n \ge 80$):** Lemmas 4.1–4.3 and Proposition 4.4 (strict monotonicity of $\Phi_n$ for $n \ge 14$, Euler-product expansion (4.1), exact $g_p'(v)$ / $B_{n+1} - B_n$ / $d\Phi_n/du \ge D_\Phi$ bounds, $\eta_k$ deviation (4.5), power-law inequality (4.6), Seam-B, and exhaustive B3/B4/B5 certification) are airtight. Independent auditor 40-digit `mpmath.iv` check of the exact repaired formulas confirms:
  - B4: $E_B(n) \le 1.7448 \times 10^{-16}$, $E_B(n+1) \le 1.2332 \times 10^{-16}$ (matching `PROOF.md` L217 & Table §7);
  - B5: $E_B(n) \le 0.09079223$, $E_B(n+1) \le 0.07480146$ (matching `PROOF.md` L218 & Table §7 to 6 significant digits).
- **§5 Binomial asymptotics, Seam-A, and Regime A ($n \ge 80$):** Lemma 5.1 (strict monotonicity, Robbins–Stirling bounds (5.3)–(5.4), integral identities & convexity (5.5)–(5.7)) and Proposition 5.2 (global $s_{\max}$, disjointness, Seam-A, and symmetric pair-sum certification across $k = 1$, $k = 2$, $3 \le k \le 25$, and uniform $k \ge 26 \to \infty$) are airtight. Independent auditor 40-digit `mpmath.iv` check of fully rigorous bounds confirms `A(3..25) <= 0.4009897 < 1` and `A(>=26) <= 0.3500145 < 1` (`p1 <= 2.234e-36`, `p2 <= 1.562e-113`).
- **§6 Main Theorem assembly:** Both even ($n = 2q$) and odd ($n = 2q+1$) interlacing chains close cleanly via IVT, Lemma 3.2(1), and palindromicity.

No edits to `PROOF.md` are required.

---

## 3. Required Fixes in `notes/check-check-3.py` & `notes/check-check-3.md` (`@check-3`)

While `notes/check-check-3.py` is zero-float (`FLOATS: []`) and exits `0` (`PASS`), its analytic interval routines (`verify_regime_B_and_seam_B` and `verify_lemma_51_and_regime_A`) contain **4 blocking direction-of-bound bugs** that must be patched before Gate 3 handoff:

1. **Bug 1 (Blocking — B5 `tk_ub`, L409):**
   `tk_ub(k)` evaluates `(1 + 4*nu_k(k) / (m0_iv * S_sh**2 * Ya**2 + pi**2)) ** (-m0_iv / 2)` at `Ya**2` instead of `Yb**2`. Because $(1 + \frac{4\nu_k}{m_0 S_{\mathrm{sh}}^2 Y_N^2 + \pi^2})^{-m_0/2}$ is **strictly increasing** in $Y_N \in [Y_a, Y_b]$, evaluating at $Y_a$ yields a **lower** bound rather than an upper bound!
   - **Fix:** Replace `Ya**2` with `Yb**2` on L409. *(Also optionally drop the redundant factor of `2` in L353/389/395/433/434 since `c_k <= 2` already cancels the `2|T_1|` denominator in (3.5); both `mult=1` -> `0.090792` and `mult=2` -> `0.181585` pass cleanly.)*

2. **Bug 2 (Blocking — B4 & B5 tail polynomial domination, L391 & L434):**
   In B4 (L391, $r_0 = 7$) and B5 (L434, $r_0 = 19$), the tail bound multiplies `eta_over_u(r_0)` by $(r/r_0)^3$. However, `eta_over_u(r_0)` uses `r_0**3 - r_0`, and for $r > r_0$, $\frac{r^3 - r}{r_0^3 - r_0} > (\frac{r}{r_0})^3$ (since $1 - r^{-2} > 1 - r_0^{-2}$).
   - **Fix:** Replace `r**3 - r` by `r**3` (i.e., `r_0**3`) in the tail numerator at $r_0 = 7$ (B4) and $r_0 = 19$ (B5) so $(r/r_0)^3 r_0^3 = r^3 > r^3 - r$ strictly dominates every $r \ge r_0$.

3. **Bug 3 (Blocking — `[A-k=3..25]` interval endpoint & sign bugs, L599, L609, L611, L618):**
   - **L599:** `abs((iv.mpf(2*r+1) * g_iv * lnQk + CL - CR).b)` takes `abs(x.b)`, which is the **lower** bound on $|x|$ when $x < 0$ (at $\gamma = -1/3$). Change to `abs(iv.mpf(2*r+1) * g_iv * lnQk + CL - CR).b`. Also, for $|\delta_{k+i} - \delta_k|$ (L599), $\max(\delta_{k+i}, \delta_k) \le \frac{13}{12 M k(k-1)}$ (strictly larger than `del_R_ub` which uses $(k+i)(k+i-1)$); use `r * 13 / (12 * M_min_iv * k * (k - 1))` instead of `del_R_ub.b` inside `d_const`.
   - **L609 (`q_R`):** Uses `-(c_const(2*k) - c_const(2*k - 1))` (negative!) instead of `+(c_const(2*k) - c_const(k))` (positive, from $\ln(R_{2k}/R_k)$). Fix to `+(c_const(2*k) - c_const(k))`.
   - **L611 (`first_R`) & L618 (`u1_uk_ub`):** `(k-1) * g_iv.b * lnQk.b` (at $\gamma = -1/3 < 0$) and `-(k-1) * g_iv.a * lnQk.b` (at $\gamma > 0$) multiply a negative quantity by `lnQk.b` instead of `lnQk.a`. Replace with `((k - 1) * g_iv * lnQk).b` and `(-(k - 1) * g_iv * lnQk).b`.

4. **Bug 4 (Blocking — `[A-k>=26]` Piece 1 & Piece 2 bound bugs, L661, L679–693, L701–719):**
   - **L661 (`CL_k2`):** `1 + (2 - i)/k0` increases in $k$ for $i \ge 3$; replace `1 + (2 - i)/k0` with the unconditional upper bound `1 + (1/k0 if i == 1 else 0)` (and use the exact `|\delta_{k+i}-\delta_k| \le \frac{13}{12 M k(k-1)}` term in `del_sum_k2` for `d_c`).
   - **L679–682 (`c_pos` in Piece 1):** (i) For $r = 7$, $(r+1)/(r(r+1)) = 1/7$, not $1/8$ (`7 * k0_iv`, not `8 * k0_iv`); (ii) include the larger left-side `|C_L(r)|` bound $\frac{1}{2}\frac{k_0/2 + 2}{(k_0/2)((k_0/2)^2 - 1)}$ (not just `|C_R(r)|`).
   - **L688 (`c_poly` in Piece 1):** Uses `x_min / 16` instead of the valid bound `x_min * (40/49) / ((1 - 1/k0)^3 * (1 - (13/25)^2))` (off by $>13\times$, since $\sum_{i=1}^r 2i^2 = \frac{r(r+1)(2r+1)}{3} \le \frac{40}{49} r^3$ for $r \ge 7$ and $i/(k-1) \le 13/25$ for $k \ge 26, i \le k/2$); also include explicit bounds for $k(|C_L| + |C_R|)$ and $k\sum|\delta|$.
   - **L693 (`p1` $E$-perturbation):** Multiplying `|e^{A_r} - e^{B_r}|` by `(1 + eps_E1)` does not bound $k(e^{A_r} + e^{B_r})\varepsilon_{E_1}$; add `+ 2 * k_eps * exp(-56 * alpha1) / (1 - exp(-16 * alpha1))`.
   - **L701–719 (`p2` Piece 2):** (i) `C_L < 0` so `-C_L > 0` (the comment `C_L >= 0` on L706 has the wrong sign!); add the valid positive upper bound on $-C_L(r_h)$ (e.g., $\frac{3}{2}\frac{1/2 + 1/k_0}{1/2 - 2/k_0}$) to `nonM_left_ub`; (ii) replace `1/2` by `1/2 + 1/k0` (right) and `1/2 + 2/k0` (left), replace `1/8` by $\frac{1}{2}(\frac{1}{2}+\frac{1}{k_0})(\frac{1}{2}+\frac{2}{k_0})$ in `nonM_tail_ub`, and include `3/2` in `rho2` so it covers both $\rho_{2R}$ and $\rho_{2L}$ (with `1 + eps_E0` covering $u_0$ in the left tail).

*(Auditor independently executed all 4 fixes in 40-digit `mpmath.iv` arithmetic: every check passes cleanly with massive margin: `B4 <= 1.745e-16`, `B5 <= 0.090793` [`mult=1`] / `0.181585` [`mult=2`], `A(3..25) <= 0.400990`, `A(>=26) <= 0.350015`.)*

Update `notes/check-check-3.md` with the repaired output numbers and ping `@audit-1` for immediate re-audit PASS!

---

## 4. Re-Audit #1 (`2026-11-27T12:04Z`) — **PASS**

Inspected `@check-3`'s patched `notes/check-check-3.py` and `notes/check-check-3.md` (`#1385`) line by line:
1. **Bug 1 fixed (L405–406):** `tk_ub(k)` now evaluates at `Yb**2` (and redundant factor `2` in Regime B removed cleanly).
2. **Bug 2 fixed (L365–392, L408–433):** `eta_over_u_b4(7, True)` and `eta_over_u_b5(19, True)` now replace $r^3 - r$ with $r^3$ for cubic tail domination across all $r \ge 7$ (B4) and $r \ge 19$ (B5).
3. **Bug 3 fixed (L597–625):** `[A-k=3..25]` now uses `abs(...).b` and `del_R_abs` with $k(k-1)$ (L597–598), `+(c_const(2*k) - c_const(k))` in `q_R` (L611, justified by monotonicity $R_m \le R_{2k}$ for $m \ge 2k$), and full interval products `((k - 1) * g_iv * lnQk).b` (L615) and `(-(k - 1) * g_iv * lnQk).b` (L622).
4. **Bug 4 fixed (L658–721):** `[A-k>=26]` now uses unconditional `CL_k2` (`1 + 1/k0` for $i=1$, `1` for $i \ge 2$), `del_R_abs_k2` (`k*(k-1)`), `7 * k0_iv` + `cL_p1_unit` in `c_pos`, full `c_poly` (`40/49`, `13/25`, explicit $k(|C_L|+|C_R|)$ and $k\sum|\delta|$ terms), explicit `p1` $E$-perturbation `+ 2 * k_eps * exp(-56 * alpha1) / (1 - exp(-16 * alpha1))`, and valid `p2` bounds (`neg_CL_ub` for $-C_L > 0$, `1/2 + {1,2}/k0`, `rho2` with `3/2`, and `1 + eps_E0`).
5. **Independent re-execution:** AST check confirmed `FLOATS: [] FLOAT_CALLS: []`; `.venv/bin/python -u targets/alexandersson-2609.05131-prob10.1/notes/check-check-3.py` exited `0`, raw output:
   - `Seam-B margin >= [0.0315685, 0.0315685]; B3 <= [2.934e-28, 2.934e-28]; B4 <= [1.745e-16, 1.745e-16]; B5 <= [0.0907922, 0.0907922]`
   - `Seam-A <= [0.642618, 0.642618]; A(k=1) <= [6.882e-5, 6.882e-5]; A(k=2) <= [1.499e-5, 1.499e-5]; A(3..25) <= [0.40099, 0.40099]; A(>=26) <= [0.350014, 0.350014]`
   - `PASS`

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`).

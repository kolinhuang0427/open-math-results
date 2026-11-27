# Checker Report: `targets/alexandersson-2609.05131-prob10.1/` (`check-check-3`)

## Primary Source & Verbatim Statement Verification

- **Primary source checked:** `tools/.arxiv_cache/eprint/2609.05131/parking-functions.tex` (`arXiv:2609.05131v2`, Per Alexandersson, *Real-rootedness and interlacing for parking functions and Chow polynomials*, 2026-09-23).
- **Exact statement match:** Section 10 **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`, L1879–1881: *"Do $H_{\NC_{n+1}}(t)$ and $H_{\NC_{n+2}}(t)$ interlace for every $n$?"*), Theorem 1.1 / eq. (1) (`eq:introSmirnovTransfer`, L144–157), Proposition 4.1 (`eq:lastLetterRecurrence`, L479–489), interlacing convention (§4 L499–508), and Table 1 (`tab:ChowTriangle`, L588–611) match `TARGET.md` and `PROOF.md` verbatim.

## Proof Audit (`PROOF.md`)

- **§1 Preliminaries, base cases & Lemma 1.1:** Base cases $n = 0, 1$ ($H_{\mathrm{NC}_1} = C_1 = 1$, $C_2 = 1 + t$), palindromicity $C_n(t) = t^{n-1} C_n(1/t)$, and the closed rational generating function (1.2) hold cleanly and agree with Proposition 4.1 (`eq:lastLetterRecurrence`) and Table 1.
- **§2 Exact Sturm–Cauchy ($1 \le n \le 80$):** Proposition 2.1 ($\Gamma$-equivalence via $u(s) = -s/(1-s)^2$ strictly decreasing on $(0, 1)$) and signed primitive PRS Cauchy index $I_{-\infty}^0(\Gamma_n/\Gamma_{n+1}) = d_{n+1}$ hold for all $80$ consecutive pairs $1 \le n \le 80$ with exact zero remainder on $\Gamma_n$ extraction.
- **§3 Analytic Identities A & B:** Both the alternating Fuss–Catalan series (Lemma 3.1, with exact $E_0(N, s)$ and $E_k(N, s)$ bounds) and the Möbius residue $w$-sum (Lemma 3.2, including $s = 1$ odd-$n$ sign (3.7) and harmonic ratio bound (3.8)) match $C_n(-s)$ to $> 20$ digits on exact test points.
- **§4 Phase analysis, Seam-B & Regime B ($n \ge 80$):** Strict monotonicity of $\Phi_n$ ($n \ge 14$, Lemma 4.1), Euler-product phase expansion + $\Delta\Phi$ bounds + derivative $D_\Phi > 10$ (Lemma 4.2), harmonic deviation $\eta_k$ and power-law bound (4.6) (Lemma 4.3), Seam-B ($\ge 0.0315685$), and `E_B < 1` across exhaustive regimes `B3` ($\le 2.934 \times 10^{-28}$), `B4` ($\le 1.745 \times 10^{-16}$), and `B5` (18 bins, $\le 0.0907922 < 1$) hold for both $N = n$ and $N = n+1$.
- **§5 Binomial asymptotics, Seam-A & Regime A ($n \ge 80$):** Lemma 5.1 (monotonicity, Robbins–Stirling bounds, integral convexity (5.3)–(5.7)), global `s_max(m_0) <= 4.516e-9`, disjointness (`k=1` and `2 <= k < K_A`), Seam-A ($\le 0.642618 < 1$), and symmetric pair-sum relative error bounds for $k = 1$, $k = 2$, $3 \le k \le 25$ ($\le 0.40099 < 1$), and uniform $k \ge 26 \to \infty$ ($\le 0.350014 < 1$) hold across all four $\gamma$-cases.
- **§6 Assembly:** Both even ($n = 2q$) and odd ($n = 2q+1$) zero interlacing chains close cleanly via IVT, Lemma 3.2(1), and palindromicity.

## Independent Exact Verification (`notes/check-check-3.py`)

Repaired per `AUDIT.md` §3 (`B5 tk_ub` at `Yb**2`; `B4`/`B5` cubic tail domination via `r**3`; `[A-k=3..25]` `abs(...)` / `+(c_{2k}-c_k)` / full interval products; `[A-k>=26]` `CL_k2` / `c_pos` / `c_poly` / `p1` $E$-perturbation / `p2` `-C_L > 0` & `rho2`) and re-run cleanly after final edit (`FLOAT_COUNT: 0`, `FLOAT_CALLS: 0` via AST check):

```text
[1/4] Checking Lemma 1.1 rational GF against Smirnov DP (n=1..15) and Table 1...
      Exact match across n=1..15 and all 9 rows of Table 1.
[2/4] Verifying Gamma_n and Sturm-Cauchy Cauchy index I_{-inf}^0(Gamma_n/Gamma_{n+1}) = d_{n+1} for 1 <= n <= 80...
      All 80 consecutive pairs n=1..80 passed exact integer Sturm-Cauchy.
[3/4] Checking analytic identities (3.2)-(3.7) & Regime B + Seam-B bounds (40-digit iv)...
      Seam-B margin >= [0.0315685, 0.0315685]; B3 <= [2.934e-28, 2.934e-28]; B4 <= [1.745e-16, 1.745e-16]; B5 <= [0.0907922, 0.0907922]
[4/4] Checking Lemma 5.1, Seam-A, and Regime A bounds (all k >= 1 to inf, 40-digit iv)...
      Seam-A <= [0.642618, 0.642618]; A(k=1) <= [6.882e-5, 6.882e-5]; A(k=2) <= [1.499e-5, 1.499e-5]; A(3..25) <= [0.40099, 0.40099]; A(>=26) <= [0.350014, 0.350014]
PASS
FLOAT_COUNT: 0 FLOAT_CALLS: 0
```

## Verdict

**PASS** (`Gate 2` cleared by `@watch-5` `#1300`, `@watch-1` `#1304`, `@watch-6` `#1309`; ready for `@audit-1` re-audit).

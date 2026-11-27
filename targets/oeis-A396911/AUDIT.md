# Adversarial Audit Report: `targets/oeis-A396911/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-27T02:29Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (specifically, an internally audited analytic and Diophantine proof for $m \ge 17$ combined with a certified 60-digit interval-arithmetic (`mpmath.iv`) verification of the finite base case $0 \le n \le 460$ with strict nearest-neighbor separation $> 2.5 \times 10^{-3}$). Note: per `CHARTER.md`, internal auditing and interval-arithmetic certification are not external peer review.
- **Independent Verifier:** `targets/oeis-A396911/notes/check-check-1.py` (authored by `check-1` strictly from live OEIS `A396911`/`A131988` and `PROOF.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly): `A396911` (revision 48, `2026-06-22T17:16:16-04:00`) and `A131988` (revision 20, `2025-02-16T08:33:06-05:00`).
- `targets/oeis-A396911/TARGET.md`
- `targets/oeis-A396911/PROOF.md`
- `targets/oeis-A396911/notes/check-check-1.md` and `notes/check-check-1.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5}.md`), plus direct GitHub spot-checks (`JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`).

Author scratch files (`notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, `notes/helper-*`, `notes/explore.py`, `notes/sim_walk.py`, `notes/check_bounds.py`, `notes/h_iv_check.py`) and `verify.py` were **not** read.

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against live OEIS `A396911` (rev 48, Witold Tatkiewicz, Jun 09 2026) and `A131988` (rev 20):
- **Vogel spiral model:** $p_k = (\sqrt{k}\cos(k\theta), \sqrt{k}\sin(k\theta))$ for $k \in \mathbb{Z}_{\ge 0}$, where $\theta = (4 - 2\phi)\pi = \pi(3 - \sqrt{5}) = 2\pi\phi^{-2}$ (`A131988`).
- **Walk definition:** Starting at $p_0 = (0, 0)$ ($a(0) = 0$), move at step $n$ to a closest unvisited point $p_j$; $a(n) = j$. No tie-breaking rule is prescribed in OEIS — `PROOF.md` handles tie-breaking unconditionally (no ties occur for $1 \le n \le 460$, and for $m \ge 17$ the only possible tie at $k = k^*_m$ between $+F_m$ and $+F_{m+1}$ preserves the inductive invariant under *either* choice).
- **Conjecture:** `Conjecture: a(n) <= (3/2) * n^2. - _Sean A. Irvine_, Jun 21 2026`.
- **Bonus open questions by Pontus von Brömssen (Jun 10 2026):** strict monotonicity and Fibonacci first differences $F_2, F_4, F_5, \dots$ are also proved unconditionally.
- Zero quantifier, offset, definition, or hypothesis drift.

---

## 3. Adversarial Audit of `PROOF.md`

### 3.1 Exact Distance Formulas & Lemma 1 (Diophantine Gap)
- Verified $D^2(k, k+d) = (\sqrt{k+d}-\sqrt{k})^2 + 4\sqrt{k(k+d)}\sin^2(d\theta/2)$, $R_-(k, d) > R_+(k, d)$ for $0 < d \le k$, and $|\sin(d\theta/2)| = \sin(\pi \|d\phi^{-2}\|_{\mathbb{Z}})$.
- **Lemma 1(1):** Induction on $m \ge 2$ proving $F_m\phi^{-2} - F_{m-2} = (-1)^m \phi^{-m}$ and $\|F_m\phi^{-2}\|_{\mathbb{Z}} = \phi^{-m}$ is exact.
- **Lemma 1(2):** Unimodular lattice basis $\det\begin{pmatrix} F_m & F_{m-1} \\ F_{m-2} & F_{m-3} \end{pmatrix} = (-1)^m$ ($m \ge 3$) and exhaustive 6-case check on $(a, b) \in \mathbb{Z}^2$ (noting $a=b=0$ gives $d=0$, excluded) rigorously proves $\|d\phi^{-2}\|_{\mathbb{Z}} \ge \phi^{-(m-2)}$ for all $1 \le d < F_{m+1}$, $d \notin \{F_{m-1}, F_m\}$.

### 3.2 Lemmas 2–4 (Monotonicity of $f_m$, Transition Thresholds $k^*_m$, Backward & Plateau Dominance)
- **Lemma 2(1):** Every elementary algebraic inequality on $(0, 1)$ verified algebraically by hand.
- **Lemma 2(2):** Derivative formula $f'_m(k) > 0$ on $[F_{m+1}, \infty)$ ($m \ge 16$) verified exactly ($\sqrt{2}((\sqrt{2}+1)/2)^2 = (4+3\sqrt{2})/4 < 2.07 < 2.61 < (F_{18}/F_{17})^2 \le (F_{m+1}/F_m)^2$). Every single intermediate numerical coefficient in the bounds proving $f_m(K_m) > 0$ (line 92: $151.84 < 153$) and $f_m((1-6\phi^{-m})K_m) < 0$ (lines 95–102: $u > 0.99728$, $y_m < 7.794\phi^{-m}$, $y_{m+1} < 12.608\phi^{-m}$, error terms $[93.88, 18.86, 3.72, 12.29, 1.19] < [128, 19, 4, 13, 2]$) was independently certified in 50-digit `mpmath.iv` arithmetic.
- **Lemma 3(1)–(2):** Verified exact backward-vs-forward identity $D^2(k, k-d) - D^2(k, k+d) = 2d(2\cos(d\theta)/(\sqrt{1+x}+\sqrt{1-x}) - 1)$ and every constant in the integral lower bound on $f_{m-1}(k^*_{m-1} + F_m)$ (lines 127–136: $(1.0057)^2(1.00572)^{3/2} < 1.0202 < 1.021$, $(0.99998/1.021) > 0.979$, $1.00001/0.994 < 1.007$, net margin $> 0.94 \cdot \frac{4\pi^2}{\sqrt{5}}\phi^{1-m} > 0$).
- **Lemma 4(1)–(3):** Verified upper bound $D^2(k, k+F_m) < 3.161$ (endpoint convexity check $1.00135 < 1.0023$) and all three exhaustive cases ($d \ge F_{m+2} \implies > 5.90$; $1 \le d < F_{m+1}, d \notin \{F_{m-1}, F_m\} \implies > 5.86$; $F_{m+1} < d < F_{m+2} \implies > 7.23$), plus parts (2)–(3).

### 3.3 Proposition 1 & Theorem 1 (Base Case, Plateau Induction, and $a(n) \le \frac{3}{2}n^2$)
- **Verifier audit (`notes/check-check-1.py`):** Confirmed sound radial pruning (endpoints $j_{\min}-1, j_{\max}+1$ explicitly certified in 60-digit `mpmath.iv`) and safe angular pruning (`math.isqrt(k*j)` exact in float64 since $kj < 9 \times 10^{10} < 2^{53}$, with $10^{-12}$ downward margin on `sin2_lo_f` and $10^{-12}$ upward margin on `u_hi`, leaving $> 10^4$ ULPs of headroom), followed by strict 60-digit `mpmath.iv` separation across all survivors (`min_gap = 0.002514 > 2.5e-3` on $1 \le n \le 460$).
- **Theorem 1 Part 1 (Inductive Plateau Structure, $m \ge 17$):** Audited all 6 neighbor candidates $k \pm F_{m-1}, k \pm F_m, k \pm F_{m+1}$ at $r = 0$ and $r \ge 1$, confirming no circularity in the tie-breaking invariant at $k = k^*_m$ and complete coverage of all unvisited points.
- **Theorem 1 Part 2 (Effective Bound & $\limsup$):** Verified geometric identity $\phi^{18} + \sum_{r=17}^m \phi^r = \phi^{m+2}$, exact algebraic completing-the-square identity $\frac{B^2}{4(BN-A)} - \frac{A+Bj}{(N+j)^2} = \frac{(Bj-(BN-2A))^2}{4(BN-A)(N+j)^2} \ge 0$, all numerical inequalities yielding $a(n)/n^2 < 1.43 < 3/2$ for all $n \ge 460$, and $\limsup_{n\to\infty} a(n)/n^2 = \pi/\sqrt{5}$.

### 3.4 Independent Verifier Re-run
Re-executed `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A396911/notes/check-check-1.py` (exit code `0`):
```text
Base walk 0<=n<=500 & OEIS A396911 51 terms (min_gap=0.002514): OK (9.75s)
Lemma 1 (Fibonacci angles, det identity, best-approx gap 3<=m<=20): OK
Lemma 2 (elementary bounds & transition thresholds 16<=m<=50): OK
Lemma 3 & Lemma 4 (backward & plateau dominance bounds): OK
Theorem 1 Part 2 (asymptotic & effective 1.43 < 3/2 inequalities): OK
PASS
```

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A396911` (rev 48, `2026-06-22`) still lists `Conjecture: a(n) <= (3/2) * n^2` and Pontus von Brömssen's monotonicity/Fibonacci-difference questions as open.
- **Gate 3 receipts (all PASS, no `CONTESTED.md`):**
  - `targets/oeis-A396911/notes/novelty-gate3-watch-1.md` (`2026-11-27T03:18:00Z`, PASS): live OEIS rev 48, arXiv, Zenodo, local snapshots, `1337isnot1337/solved-conjectures`, `trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond` clear.
  - `targets/oeis-A396911/notes/novelty-gate3-watch-5.md` (`2026-11-27T02:44:00Z`, PASS): live OEIS rev 48, arXiv, Zenodo, 413 snapshots, and 10 competing repos clear (`atlas-lean`'s `IrvineConjecture.lean` verified unrelated Shallit 2024 Kimberling word).
  - `targets/oeis-A396911/notes/novelty-gate3-watch-6.md` (`2026-11-27T03:18:32Z`, PASS): live OEIS rev 48, 595 discovered repo snapshots (incl. `CrocSwap/integer-mult-bounds`), live `gh search code`, and Zenodo clear.
- Ready for final report to `@coordinator` with label `"written proof, internally audited"`.

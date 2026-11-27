# Adversarial Audit Report (`audit-1`): `targets/oeis-A178072/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A178072` (rev. 35, May 11 2025 `04:14:03`) — R. J. Mathar's Jun 14, 2016 7-term D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, live OEIS `A178072` rev. 35 (`fmt=text`), `watch/snapshots/**` (652 files incl. Zenodo `23112421`/`23114921` and Cohen `24384895`)
- **Verdict:** **PASS**

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A178072` (`#35 May 11 2025 04:14:03`):**
  - `%O`: `0,8`; all 34 `DATA` terms (`1, 0, -1, -1, -1, -1, 1, 8, 23, ...`) match `notes/check-check-3.py` verbatim.
  - `%N`, Michael Somos's Jun 13, 2010 algebraic equation `(2*x + x^3) * A(x)^2 - (1 + x)^2 * A(x) + 1 = 0` and closed-form g.f. `2 / (1 + 2*x + x^2 + sqrt(1 - 4*x + 6*x^2 + x^4))`, and R. J. Mathar's Jun 14, 2016 7-term recurrence conjecture match `TARGET.md` and `PROOF.md` verbatim.
- **Snapshot cross-check:** `.venv/bin/python tools/novelty_grep.py A178072` returned `0 lines across 0/652 files` (including Zenodo `23112421`/`23114921` and Cohen `24384895`).

---

## 2. Line-by-Line Proof Audit — PASS

- **Section 1 (First-order inhomogeneous ODE, L19–35):**
  - With $P(x) = 2x + x^3$, $R(x) = (1+x)^2 = 1 + 2x + x^2$, and $\Delta(x) = R(x)^2 - 4P(x) = 1 - 4x + 6x^2 + x^4$: completing the square in $PA^2 - RA + 1 = 0$ gives $(R - 2PA)^2 = \Delta$.
  - Since $(1+x)^2 \in \mathbb{Z}[[x]]^\times$ and $A(x) = (1+x)^{-2}(1 + (2x+x^3)A(x)^2)$, $A(x) \in 1 + x\mathbb{Z}[[x]]$, so $R - 2PA \in 1 + x\mathbb{Z}[[x]]$ equals the unique formal square root $y(x) = \sqrt{\Delta(x)}$ with $y(0) = 1$ (equivalently $A(x) = 2/(R + \sqrt{\Delta}) = (R - \sqrt{\Delta})/(2P)$).
  - Differentiating $y^2 = \Delta$ yields $2\Delta y' = \Delta' y$; substituting $y = R - 2PA$ and dividing by $4$ gives $A_1 A' + A_0 A = R_1$ with $A_1 = \Delta P$, $A_0 = \Delta P' - \frac{1}{2}\Delta' P$, $R_1 = \frac{1}{2}\Delta R' - \frac{1}{4}\Delta' R$ matching L31–33 identically.
- **Section 2 (Second-order ODE & coefficient extraction, L39–66):**
  - Applying $L = x(1+5x)\frac{d}{dx} + 4x$ to $A_1 A' + A_0 A = R_1$ yields $P_2 A'' + P_1 A' + P_0 A = R_2$ with exact polynomials matching L46, L48, L50, L52 and $\deg R_2 = 5$, so $[x^n] R_2(x) = 0$ for all $n \ge 6$.
  - Writing $P_2 = \sum_{k=0}^7 p_{2,k} x^{k+2}$, $P_1 = \sum_{k=0}^7 p_{1,k} x^{k+1}$, $P_0 = \sum_{k=0}^7 p_{0,k} x^k$ (with $p_{0,0} = 0$), extracting $[x^n]$ for every $n \ge 7$ gives $\sum_{k=0}^7 c_k(n) a(n-k) = 0$ where $c_k(n) = p_{2,k}(n-k)(n-k-1) + p_{1,k}(n-k) + p_{0,k}$ (automatic vanishing at $m = n - k \in \{0, 1\}$ matches $[x^{m-2}]A'' = [x^{m-1}]A' = 0$). All 8 quadratic polynomials $c_0(n), \dots, c_7(n)$ match Mathar's conjecture verbatim, and at $n = 6$ the $k = 7$ monomials have degree $\ge 7$ while $c_7(6) = (5\cdot 6 - 1)(6 - 6) = 0$, so the recurrence holds at $n = 6$ as well.

---

## 3. Independent Exact Verification — PASS

Executed `.venv/bin/python -u targets/oeis-A178072/notes/check-check-3.py`:
- Exit code `0`, output `PASS` (zero floats; pure exact integer and SymPy `QQ[x]`/`QQ[n]` arithmetic).
- Verified all 34 live OEIS `A178072` terms, Somos's algebraic equation through $x^{60}$, the double binomial sum ($n \le 25$), all Section 1 & Section 2 symbolic ODEs and coefficient polynomials $c_0(n), \dots, c_7(n)$, and Mathar's 7-term recurrence for $n = 6..60$.

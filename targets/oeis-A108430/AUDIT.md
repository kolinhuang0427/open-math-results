# Adversarial Audit Report: `targets/oeis-A108430/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T21:37Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (with exact-arithmetic verification of path combinatorics, Lagrange inversion, and the differential-algebraic reduction in $\mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/oeis-A108430/notes/check-check-1.py` (authored by `check-1` strictly from live OEIS `A108430` and `PROOF.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly): `A108430` (revision 14, 2025-11-05) and cross-referenced `A108429` (revision 9).
- `targets/oeis-A108430/TARGET.md`
- `targets/oeis-A108430/PROOF.md`
- `targets/oeis-A108430/notes/check-check-1.md` and `notes/check-check-1.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`), plus direct Zenodo and GitHub code checks.

Author scratch notes (`notes/screen-*`) and the finder's `verify.py` were **not** read.

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against live OEIS `A108430` (rev 14, 2025-11-05):
- **Name:** *"Number of d steps in all paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1), U=(1,2), or d=(1,-1)."*
- **Offset:** `1,1` ($n \ge 1$); all 18 tabulated terms match.
- **Formula:** `a(n) = (1/n)*sum(k*binomial(n,2n-k)*binomial(n+k,n-1), k=n..2n)` and `Conjecture D-finite with recurrence n*(2*n+1)*(23982*n-28681)*a(n) +(-640736*n^3+1168048*n^2-901220*n+247035)*a(n-1) +(1196488*n^3-6448608*n^2+10992587*n-5911365)*a(n-2) +2*(2*n-5)*(28283*n-6993)*(n-3)*a(n-3)=0. - _R. J. Mathar_, Jul 24 2022`.
- Zero quantifier, coefficient, offset, or definition drift in `TARGET.md`, `PROOF.md`, or `notes/check-check-1.py`.

---

## 3. Adversarial Audit of `PROOF.md`

### 3.1 Step 1 (Path Decomposition & Lagrange Inversion)
- Every step has $\Delta x \in \{1, 2\} > 0$, so $x \ge 0$ holds automatically. Returning to $y = 0$ forces $\# d = \# u + 2(\# U)$ and hence $x = 2(\# u) + (\# U) + (\# d) = 3(\# u + \# U)$, so $x = 3n \iff \# u + \# U = n$.
- Because $d = (1,-1)$ is the unique downward step (changing $y$ by $-1$), a nonempty valid path starting with $u = (2,1)$ has a unique first $d$-step returning to $y = 0$ ($u P_1 d P_2$), and one starting with $U = (1,2)$ has unique first $d$-steps hitting $y = 1$ and then $y = 0$ ($U P_1 d P_2 d P_3$). This yields $G(t, z) = 1 + t z G(t, z)^2(1 + t G(t, z))$ in $\mathbb{Z}[t][[z]]$.
- Writing $w = G(t, z) - 1 = z(t(1+w)^2 + t^2(1+w)^3)$, Lagrange inversion yields $[z^n]G(t,z) = \frac{1}{n}\sum_{j=0}^n \binom{n}{j}\binom{3n-j}{n-1} t^{2n-j}$ for all $n \ge 1$; setting $k = 2n - j$ and differentiating at $t = 1$ gives both $a(n) = [z^n]\left.\frac{\partial G}{\partial t}\right|_{t=1}$ and Deutsch's binomial sum $a(n) = \frac{1}{n}\sum_{k=n}^{2n} k \binom{n}{2n-k}\binom{n+k}{n-1}$. Completely airtight.

### 3.2 Step 2 (Differential-Algebraic Reduction in $\mathcal{A}$)
- $P(z, G) = z G^3 + z G^2 - G + 1 = z(G^3 + G^2) - (G - 1)$ is irreducible over $\mathbb{Q}(z)$ (linear in $z$ with coprime $G$-polynomials, also verified by SymPy). Hence $\mathcal{A} = \mathbb{Q}(z)[G]/(P)$ is a field.
- Evaluating $G \mapsto G_1(z) = G(1, z) \in 1 + z\mathbb{Z}[[z]]$ gives a nonzero homomorphism $\mathcal{A} \to \mathbb{Q}((z))$, which is therefore **injective** and commutes with $\frac{d}{dz}$ (since $D = 1 - 2z G_1 - 3z G_1^2 \in 1 + z\mathbb{Z}[[z]]$ is invertible in both $\mathcal{A}$ and $\mathbb{Q}[[z]]$).
- Implicit differentiation gives $A(z) = \left.\frac{\partial G}{\partial t}\right|_{t=1} = (z G_1^2 + 2z G_1^3)/D$ and $G_1'(z) = (G_1^3 + G_1^2)/D$ in $\mathcal{A}$.
- With $a(0) = a(-1) = a(-2) = 0$, $z^r A(z) = \sum_{n=1}^\infty a(n-r) z^n$ for each $r \in \{0,1,2,3\}$, so $\Phi(z) = \sum_{r=0}^3 c_r(\theta)[z^r A(z)] = \sum_{n=1}^\infty (\sum_{r=0}^3 c_r(n) a(n-r)) z^n$.
- Independent exact computation in $\mathcal{A}$ (`notes/check-check-1.py`) establishes $\Phi(z) = -42291 z - 49573 z^2 \in \mathbb{Q}[z]$ (zero $G_1$ and $G_1^2$ components). By injectivity of $\mathcal{A} \hookrightarrow \mathbb{Q}((z))$, $[z^n]\Phi(z) = 0$ for every $n \ge 3$ (note $c_3(3) = 0$, so the $n = 3$ identity holds even independently of $a(0)$).
- **Verifier Re-run:** `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A108430/notes/check-check-1.py` exited with code `0`:
  ```text
  Combinatorics, Lagrange T(n,k), OEIS data (n=1..18), and recurrence (n=3..30): OK
  Exact differential-algebraic reduction in Q(z)[G]/(P): Phi(z) = -49573*z**2 - 42291*z: OK
  PASS
  ```

### 3.3 Minor Non-Blocking Observations
- `PROOF.md` summarizes the final $\mathcal{A}$-reduction rather than printing the explicit 3-component rational-function intermediate expressions of $c_r(\theta)[z^r A(z)]$ in prose; however, the entire algebraic derivation was independently reconstructed from scratch in `notes/check-check-1.py` and verified exactly in $\mathbb{Q}(z)[G]/(P)$.

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A108430` (rev 14, 2025-11-05) still lists Mathar's Jul 24 2022 recurrence as `Conjecture D-finite`.
- Direct live Zenodo (`A108430`: 0 hits; `23982`: only biology hits) and GitHub code searches (`A108430`: only OEIS mirrors `joeis`, `loda-programs`, `gfis/OEIS-mat`, `oeis-alien`; `"23982" "28681"`: 0 math hits) found no prior proof.
- Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) all passed with no `CONTESTED.md`.
- **Gate 3 live pre-report re-check (all PASS within 1 hour of report, no `CONTESTED.md`):**
  - `targets/oeis-A108430/notes/novelty-gate3-watch-1.md` (`2026-11-26T22:18:00Z`, PASS)
  - `targets/oeis-A108430/notes/novelty-gate3-watch-5.md` (`2026-11-26T21:56:30Z`, PASS)
  - `targets/oeis-A108430/notes/novelty-gate3-watch-6.md` (`2026-11-26T21:46:56Z`, PASS)

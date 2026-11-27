# Independent Check Report: `oeis-A108430` (`check-1`)

- **Checked at (UTC):** `2026-11-26T21:18:08Z`
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity and independent exact verification of combinatorics, Lagrange inversion, and differential-algebraic reduction)

## 1. Primary-Source Fidelity Check

- **Primary source fetched:** Live OEIS JSON API (`https://oeis.org/search?q=id:A108430&fmt=json`), revision `14` (`2025-11-05T15:35:31-05:00`).
- **Exact fields checked:**
  - `name`: *"Number of d steps in all paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1), U=(1,2), or d=(1,-1)."*
  - `offset`: `"1,1"`
  - `data`: `3,31,311,3151,32299,334335,3488239,36627487,386618387,4098713631,43611791783,465496885231,4981942135611,53443871159551,574500093677535,6186886528903231,66735614131858723,720897596248427295`
  - `formula`:
    - `a(n) = (1/n)*sum(k*binomial(n,2n-k)*binomial(n+k,n-1), k=n..2n).`
    - `Conjecture D-finite with recurrence n*(2*n+1)*(23982*n-28681)*a(n) +(-640736*n^3+1168048*n^2-901220*n+247035)*a(n-1) +(1196488*n^3-6448608*n^2+10992587*n-5911365)*a(n-2) +2*(2*n-5)*(28283*n-6993)*(n-3)*a(n-3)=0. - _R. J. Mathar_, Jul 24 2022`
- **Word-for-word comparison against `TARGET.md` and `PROOF.md`:**
  - Name, offset (`1,1`, i.e., $n \ge 1$), 18 data terms, binomial formula, and every polynomial coefficient in Mathar's 2022 conjecture match verbatim.
  - Because `offset` is `1`, the 3rd-order recurrence genuinely begins at $n = 4$ (and also holds at $n = 3$ because the $a(0)$ coefficient $2(2n-5)(28283n-6993)(n-3)$ vanishes at $n=3$). Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from the live OEIS `A108430` JSON and the algebraic steps in `PROOF.md`, without reading `verify.py`.
- **Verifier script:** `targets/oeis-A108430/notes/check-check-1.py` (exact integer/rational arithmetic and SymPy polynomial/fraction-field reduction in $\mathbb{Q}(z)[G]/(z G^3 + z G^2 - G + 1)$).
- **Verified claims & lemmas:**
  1. **Combinatorial brute force & Lagrange bivariate count ($n = 1..6$):** Dynamic-programming enumeration of all first-quadrant paths from $(0,0)$ to $(3n,0)$ using $u=(2,1), U=(1,2), d=(1,-1)$ matches $T(n, k) = \frac{1}{n}\binom{n}{2n-k}\binom{n+k}{n-1}$ for every $k \in \{n, \dots, 2n\}$, and total $d$-steps match `a_binomial(n)` and OEIS `data`.
  2. **OEIS data & direct recurrence check:** `a_binomial(n)` matches all 18 OEIS `data` values (`n=1..18`); Mathar's recurrence holds identically for all `n=3..30` with leading coefficient $c_0(n) = n(2n+1)(23982n-28681) \neq 0$, and at $n=1, 2$ (with $a(0)=a(-1)=a(-2)=0$) equals $-42291$ and $-49573$ respectively.
  3. **Algebraic reduction in $\mathcal{A} = \mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$:**
     - Verified $P(z, G_1) = z G_1^3 + z G_1^2 - G_1 + 1$ is irreducible over $\mathbb{Q}(z)$.
     - Inverted $D = 1 - 2z G_1 - 3z G_1^2$ in $\mathcal{A}$, verified implicit derivative $G_1'(z) = (G_1^3+G_1^2)/D$, and confirmed the power series of $A(z) = (z G_1^2 + 2z G_1^3)/D$ matches `a_binomial(n)` for $n = 1..10$.
     - Applied $\theta = z \frac{d}{dz}$ in $\mathcal{A}$ to compute $\Phi(z) = \sum_{r=0}^3 c_r(\theta)[z^r A(z)]$ in exact $\mathbb{Q}(z)$-coordinates $\{1, G_1, G_1^2\}$: the $G_1$ and $G_1^2$ components vanish identically and the constant component simplifies exactly to $-49573 z^2 - 42291 z$, proving $[z^n]\Phi(z) = 0$ for all $n \ge 3$.

### Command & Raw Output

Command:
```bash
.venv/bin/python targets/oeis-A108430/notes/check-check-1.py
```

Raw output:
```text
Combinatorics, Lagrange T(n,k), OEIS data (n=1..18), and recurrence (n=3..30): OK
Exact differential-algebraic reduction in Q(z)[G]/(P): Phi(z) = -49573*z**2 - 42291*z: OK
PASS
```

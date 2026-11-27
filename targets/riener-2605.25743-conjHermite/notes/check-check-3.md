# Independent Check Report (`check-3`): `targets/riener-2605.25743-conjHermite/`

## 1. Primary-Source Fidelity Check
Checked directly against `arXiv:2605.25743v3` (`tools/.arxiv_cache/eprint/2605.25743v3/article.tex`, 2026-10-21):
- **Conjecture 1.1 (`conj:sos`, Section 1, lines 123–126):**
  `For every $n\ge2$ and every $0\le k\le n-2$, the polynomial $\D_k^{(n)}$ is a sum of squares of polynomials in the differences $x_i-x_j$.`
- **Conjecture 6.5 (`conj:hermite`, Section 6, lines 1983–1987):**
  `For every $n\ge2$ and $0\le k\le n-2$, the ordinary Hermite matrix of $P^{(k)}/\operatorname{lc}(P^{(k)})$ is an SOS matrix over $\bR[x_1,\ldots,x_n]$.`
- **Definitions (lines 95–105, 401–437, 1716–1730):** $P(t) = \prod_{i=1}^n (t - x_i)$, $\mathcal{D}_k^{(n)} = \mathrm{disc}(P^{(k)})$ with leading-coefficient scaling $c^{2m-2}\prod_{i<j}(\rho_i-\rho_j)^2 = (-1)^{m(m-1)/2}c^{-1}\mathrm{Res}(f,f')$, $H(f) = (s_{i+j}(f))_{0 \le i,j \le r-1}$, SOS-matrix factorization $H(f) = A^{\mathsf T}A$ with polynomial entries in $A$.
- **Result:** All quantifiers, domains ($n \ge 2$, $0 \le k \le n-2$), normalizations, and polynomial rings match verbatim between `article.tex`, `TARGET.md`, and `PROOF.md`.
- **Minor editorial note in `TARGET.md`:** `TARGET.md` header line 1 and `PROOF.md` cite `Section 6, Conjecture 6.5` accurately, whereas `TARGET.md` lines 12 and 16 contain the typo `Section 5` / `Conjecture 5.6` (and `\mathrm{D}_k^{(n)}` for `\mathcal{D}_k^{(n)}`). Does not affect the mathematical statement.

## 2. Independent Mechanical Verification
Written solely from primary-source definitions and `PROOF.md` without consulting `verify.py` or author notes, using exclusively exact `int` / `Fraction` / SymPy polynomial-ring arithmetic (zero floating-point operations):
- Script: `targets/riener-2605.25743-conjHermite/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/riener-2605.25743-conjHermite/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/5] Checking Lemma 1 symbolically for 2 <= n <= 6, 0 <= k <= n-2...
  Lemma 1: PASS (all 15 pairs for 2 <= n <= 6)
[2/5] Checking Lemma 2 symbolically for r = 2..6...
  Lemma 2: PASS (r = 2..6)
[3/5] Checking Lemma 3 symbolically for 2 <= r <= n <= 6...
  Lemma 3: PASS (all 15 pairs for 2 <= r <= n <= 6)
[4/5] Checking Lemma 4 in exact Fraction arithmetic for 2 <= r <= n <= 8...
  Lemma 4: PASS (all 28 pairs for 2 <= r <= n <= 8)
[5/5] Checking Theorem 1 and Corollary 2 (symbolic 2<=r<=n<=5 + exact open cases)...
    symbolic (n=2, k=0): PASS
    symbolic (n=3, k=0): PASS
    symbolic (n=3, k=1): PASS
    symbolic (n=4, k=0): PASS
    symbolic (n=4, k=1): PASS
    symbolic (n=4, k=2): PASS
    symbolic (n=5, k=0): PASS
    symbolic (n=5, k=1): PASS
    symbolic (n=5, k=2): PASS
    symbolic (n=5, k=3): PASS
    exact open/higher (6, 2): PASS
    exact open/higher (7, 2): PASS
    exact open/higher (7, 3): PASS
    exact open/higher (8, 2): PASS
    exact open/higher (8, 3): PASS
    exact open/higher (8, 4): PASS
    exact open/higher (9, 2): PASS
    exact open/higher (9, 3): PASS
    exact open/higher (9, 4): PASS
  Theorem 1 & Corollary 2: PASS (symbolic 2<=r<=n<=5 + full CB (6,2) + exact open cases up to (9,4))
PASS
```
Summary of independent checks:
- **Lemma 1:** Symbolic equality of $P^{(k)}/\mathrm{lc}(P^{(k)})$ and $J'_{n,r}$ with subset-average formulas for all 15 pairs $2 \le n \le 6$, $0 \le k \le n-2$.
- **Lemma 2:** Symbolic $B(f) = T(f)H(f)T(f)^{\mathsf T}$, $\det T(f) = (-1)^{\lfloor r/2\rfloor}$, Neumann-series inverse $T(f)^{-1} \in \mathbb{Z}[c_1,\dots,c_{r-1}]^{r\times r}$, and Vandermonde/Sylvester discriminant identity for $r = 2,\dots,6$.
- **Lemma 3:** Symbolic $B(J_{n,r}) = C(x)^{\mathsf T}\mathbf{W}_{n,r}C(x)$ over $\mathbb{Q}[x_1,\dots,x_n]$ for all 15 pairs $2 \le r \le n \le 6$.
- **Lemma 4:** Exact `Fraction` $\gamma_{n,s} > 0$, rank-1 Walsh–Hadamard decomposition of $\mathbf{W}_{n,r}$, and exact rational $L_0 D L_0^{\mathsf T}$ factorization with all $d_j > 0$ (certifying $\mathbf{W}_{n,r} \succ 0$) for all 28 pairs $2 \le r \le n \le 8$.
- **Theorem 1 & Corollary 2:** Symbolic SOS-matrix factorization (both $M^{\mathsf T}DM$ and explicit $\gamma_{n,|S|}$ rank-1 sum), translation invariance of $M(z)$ (polynomials in $\{x_i - x_j\}$), and full Cauchy–Binet expansion against Sylvester $\mathrm{disc}(P^{(k)})$ for $2 \le r \le n \le 5$ (plus 3 rational points at $(5,1)$), full 4845-minor Cauchy–Binet at $(6,2)$, and exact rational checks directly from $P^{(k)}$ on open cases $(7,2),(7,3),(8,2),(8,3),(8,4),(9,2),(9,3),(9,4)$.

## 3. Verdict
- **PASS** (`Gate 2` PASS receipts present: `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

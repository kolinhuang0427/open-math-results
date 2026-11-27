# Adversarial Audit Report: `targets/riener-2605.25743-conjHermite/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T09:06Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Primary source verbatim: `tools/.arxiv_cache/eprint/2605.25743v3/article.tex` (Cordian Riener and Boris Shapiro, *Discriminants of derivatives: square graphs and sums of squares*, `arXiv:2605.25743v3`, updated `2026-10-21`).
- `targets/riener-2605.25743-conjHermite/TARGET.md`
- `targets/riener-2605.25743-conjHermite/PROOF.md`
- `targets/riener-2605.25743-conjHermite/notes/check-check-3.md` and `targets/riener-2605.25743-conjHermite/notes/check-check-3.py`
- Confirmed no `targets/riener-2605.25743-conjHermite/CONTESTED.md` exists, and Gate 2 PASS receipts from `watch-1`, `watch-5`, and `watch-6`.

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Fidelity Audit (PASS)

- Verified word-for-word against `article.tex` (`arXiv:2605.25743v3`):
  - **Conjecture 1.1 (`\label{conj:sos}`, Section 1, L123–126):** *"For every $n \ge 2$ and every $0 \le k \le n - 2$, the polynomial $\mathcal{D}_k^{(n)}$ is a sum of squares of polynomials in the differences $x_i - x_j$."*
  - **Conjecture 6.5 (`\label{conj:hermite}`, Section 6, L1983–1987; verified exact numbering under `\newtheorem{...}[theorem]` after Theorem 6.1, Corollary 6.2, Theorem 6.3, Remark 6.4):** *"For every $n \ge 2$ and $0 \le k \le n - 2$, the ordinary Hermite matrix of $P^{(k)}/\mathrm{lc}(P^{(k)})$ is an SOS matrix over $\mathbb{R}[x_1,\ldots,x_n]$."*
  - Discriminant leading-coefficient normalization ($\mathrm{disc}(c\prod_{j=1}^m (t-\theta_j)) = c^{2m-2}\prod_{a<b}(\theta_a-\theta_b)^2$), ordinary Hermite matrix $H(f) = (s_{i+j}(f))_{0 \le i,j \le r-1}$, and SOS-matrix factorization $H(f) = A^{\mathsf T} A$ match `article.tex` L95–105, L401–450, L1716–1730 verbatim.
  - *(Minor editorial note: `TARGET.md` L12/L16 mistypes `Section 5 / Conjecture 5.6`, while `TARGET.md` L1 and `PROOF.md` cite `Section 6 / Conjecture 6.5` accurately; zero mathematical drift.)*

---

## 3. Line-by-Line Mathematical Audit (PASS)

Every step of `PROOF.md` is elementary, completely self-contained, and verified airtight for all $n \ge 2$ and $0 \le k \le n - 2$ ($r = n - k \in [2, n]$):

1. **Lemma 1 (Normalized derivative & subset averages):** Product rule yields $P^{(k)} = k! \sum_{S \in \binom{[n]}{r}} P_S$ with $\mathrm{lc}(P^{(k)}) = k!\binom{n}{r} = n!/r!$, giving $J_{n,r} = \binom{n}{r}^{-1}\sum_{|S|=r} P_S$ and $J'_{n,r} = r\binom{n}{r-1}^{-1}\sum_{|T|=r-1} P_T$. Exact.
2. **Lemma 2 (Unimodular Bezoutian–Hermite congruence):**
   - Verified partial-fraction sign $\frac{1}{s-t}\bigl(\frac{1}{t-\theta_\ell} - \frac{1}{s-\theta_\ell}\bigr) = \frac{1}{(s-\theta_\ell)(t-\theta_\ell)}$, giving $\sum_\ell \frac{f(s)}{s-\theta_\ell}\frac{f(t)}{t-\theta_\ell} = \frac{f(s)f'(t)-f'(s)f(t)}{s-t}$, and polynomial expansion yielding $B(f) = T(f) H(f) T(f)^{\mathsf T}$ in $\mathbb{Z}[c_1,\dots,c_r]^{r\times r}$.
   - Verified $L(f) = J T(f) = I_r + N(f)$ is unit lower triangular over $\mathbb{Z}[c_1,\dots,c_{r-1}]$ with $N(f)^r = 0$, $\det T(f) = (-1)^{\lfloor r/2\rfloor} = (-1)^{\binom{r}{2}}$, $T(f)^{-1} = L(f)^{-1} J \in \mathbb{Z}[c_1,\dots,c_{r-1}]^{r\times r}$, $H(f) = T(f)^{-1} B(f) (T(f)^{-1})^{\mathsf T}$, and $\det H(f) = (\det V(\theta))^2 = \mathrm{disc}(f)$. Exact.
3. **Lemma 3 (Constant-matrix Bezoutian factorization):**
   - Verified symmetry of $\mathbf{W}_{n,r}$ via $|U \setminus V| = |V \setminus U|$.
   - Verified bijection $(S, T, z) \mapsto (S \setminus \{z\}, T, z)$ between $\mathcal{X} = \{(S, T, z) : |S|=r, |T|=r-1, z \in S \setminus T\}$ and $\mathcal{Y} = \{(U, V, z) : |U|=|V|=r-1, z \in [n] \setminus (U \cup V)\}$ with two-sided inverse $(U, V, z) \mapsto (U \cup \{z\}, V, z)$ and $|S \setminus T| = |U \setminus V| + 1$.
   - Verified $x_z$ cancellation in $(s - x_z) - (t - x_z) = s - t$, exact count $n - |U \cup V|$ (including the empty-sum case $U \cup V = [n]$), division by $s - t$, and $B(J_{n,r}) = C(x)^{\mathsf T} \mathbf{W}_{n,r} C(x)$. Completely airtight.
4. **Lemma 4 (Walsh–Hadamard rank-1 decomposition & $\mathbf{W}_{n,r} \succ 0$):**
   - Verified substitution $x = u^2$ giving $\gamma_{n,s} = 2^{-(n-2)}\int_0^1 u(1+u)^{n-1-s}(1-u)^s\, du \in \mathbb{Q}_{>0}$ for all $0 \le s \le n-1$.
   - Verified pointwise identity $x^{|U \setminus V|} = (\sqrt{x})^{|U \triangle V|} = 2^{-(n-1)}\sum_{S \subseteq [n]\setminus\{z\}} (1+\sqrt{x})^{n-1-|S|}(1-\sqrt{x})^{|S|}(-1)^{|S\cap U|+|S\cap V|}$ for $U, V \in \binom{[n]\setminus\{z\}}{r-1}$, integration over $[0,1]$ giving $(|U\setminus V|+1)^{-1}$, and summation over $z \in [n]$ reproducing $\mathbf{W}_{n,r}$.
   - Verified strict positive definiteness via character orthogonality on $[n] \setminus \{z\}$ (for any $U_0 \in \binom{[n]}{r-1}$, $|U_0| = r-1 < n$ guarantees existence of $z \in [n] \setminus U_0$, forcing $2^{n-1} v_{U_0} = 0$), yielding both real Cholesky $\mathbf{W}_{n,r} = L^{\mathsf T} L$ and exact rational $\mathbf{W}_{n,r} = L_0 D L_0^{\mathsf T}$ ($d_j \in \mathbb{Q}_{>0}$). Completely airtight.
5. **Theorem 1 (`conj:hermite`) & Corollary 2 (`conj:sos`):**
   - Verified $A(x) = L C(x)(T(J_{n,r})^{-1})^{\mathsf T} \in \mathbb{R}[x_1,\dots,x_n]^{N\times r}$ satisfies $H(J_{n,r}) = A(x)^{\mathsf T} A(x)$, and explicit positive-rational-weighted rank-1 factorization over $\mathbb{Q}[x_1,\dots,x_n]$.
   - Verified translation invariance $J_{n,r}(t; z) = J_{n,r}(t+\overline{x}; x)$ with $z_i = \frac{1}{n}\sum_{j=1}^n(x_i - x_j)$, $N = \binom{n}{r-1} \ge \binom{r}{r-1} = r$, and Cauchy–Binet expansion (both over $\mathbb{R}[\{x_i-x_j\}]$ and positive-rational-weighted over $\mathbb{Q}[\{x_i-x_j\}]$) yielding $\mathcal{D}_k^{(n)}$. Completely airtight.

---

## 4. Independent Verifier Re-Execution (PASS)

Re-executed `.venv/bin/python targets/riener-2605.25743-conjHermite/notes/check-check-3.py`:
- Exit code `0`
- Raw output:
  ```text
  Lemma 1: PASS (all 15 pairs for 2 <= n <= 6)
  Lemma 2: PASS (r = 2..6)
  Lemma 3: PASS (all 15 pairs for 2 <= r <= n <= 6)
  Lemma 4: PASS (all 28 pairs for 2 <= r <= n <= 8)
  Theorem 1 & Corollary 2: PASS (symbolic 2<=r<=n<=5 + full CB (6,2) + exact open cases up to (9,4))
  PASS
  ```

---

## 5. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python targets/riener-2605.25743-conjHermite/notes/check-check-3.py` and paths `targets/riener-2605.25743-conjHermite/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.

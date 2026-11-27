# Blind Adversarial Audit Report: `targets/hartwig-2611.23687-conj1.4/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T10:13Z`
- **Verdict:** **PASS**
- **Files Audited (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2611.23687/main.tex` (`arXiv:2611.23687v1`), `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (`arXiv:2611.23687v1`)

- **Latest Version Check:** Live arXiv query (`tools/arxiv_fetch.py query --id-list 2611.23687`) confirms `2611.23687v1` (`2026-11-18`, Jonas T. Hartwig & Sagar Shrivastava, *"Extremal Projectors and the Virasoro Algebra"*) is the sole version, with no journal ref or DOI.
- **Numbering Check (`main.tex`):** `\newtheorem{lemma}{Lemma}[section]` shared across `theorem`, `proposition`, `corollary`, `conjecture`, `definition`, `example` (L8–18; `remark` uses an independent counter). In Section 1: Theorem 1.1 (`thm:existence-of-projector`, L87), Corollary 1.2 (L113), Theorem 1.3 (`denominator-theorem`, L155), **Conjecture 1.4** (`\label{conj_denominator_N-truncated}`, L163–169), Conjecture 1.5 (`\label{conj_denominator_full}`, L177–187). In Section 3: Lemma 3.1 (`lem:shift-property`, L414), eqs. `(3.24)–(3.31)` (L589–631).
- **Verbatim Match:** `TARGET.md` L12–21 and `PROOF.md` L5–14 match `main.tex` L130–187 verbatim (including $K_n$, $\varphi_{r,s}$, $\tau_n(L_0) = L_0 + n$, $D_N = \prod_{1\le n\le N} \tau_{-n}(K_n)$, and regularization $Q P_N \in U(\mathrm{Vir})$).
- **Harmless editorial nits noted (non-blocking):** `PROOF.md` L56 cites `eq. (1.7)` for Kac's determinant formula (`\label{eq_kac-denominator}`), which is **eq. (1.5)** (`main.tex` L122; eq. (1.7) is $K_n$), though L57 prints the exact formula; L59 writes $U(\mathrm{Vir})(c - c)$ reusing the symbol $c$ for both the central generator and the specialized scalar. Neither affects any mathematical deduction.

---

## 2. Adversarial Line-by-Line Proof Audit

- **Step 1 (PBW Regularization Criterion):** Verified from PBW for $\mathrm{Vir} = \mathrm{Vir}^- \oplus \mathfrak{h} \oplus \mathrm{Vir}^+$ and Lemma 3.1 (`L_\lambda^\dagger f(L_0,c) = f(L_0 - |\lambda|, c) L_\lambda^\dagger`, whose shift map $\tau_{-|\lambda|}$ is an automorphism of $\mathbb{C}[L_0, c]$) that $\{L_\lambda^\dagger L_\mu\}_{\lambda,\mu \in \mathcal{P}}$ is a free left $\mathbb{C}[L_0, c]$-basis of $U(\mathrm{Vir})$, reducing $Q P_N \in U(\mathrm{Vir})$ cleanly to $Q b^{(n)}_{\lambda,\mu} \in \mathbb{C}[L_0, c]$ for all $1 \le n \le N$ and $\lambda,\mu \vdash n$.
- **Step 2 (Irreducibility & Pairwise Coprimality of $\tau_{-n}(K_m)$):** Hand-verified:
  - $h_{r,r}(c) = \frac{(r^2-1)(1-c)}{24}$, linear monic in $L_0$, irreducible in $\mathbb{C}[L_0, c]$.
  - $P_{r,s}(L_0, c) = \varphi_{r,s}\varphi_{s,r}$ ($1 \le r < s$) is monic quadratic in $L_0$ with discriminant $4\bigl(\frac{s^2-r^2}{48}\bigr)^2 (c-1)(c-25)$, non-square in $\mathbb{C}(c)$, hence irreducible in $\mathbb{C}[L_0, c]$.
  - Comparing $L_0$-degree, $L_0$-discriminant ($s^2 - r^2$), $c$-coefficient of the $L_0^1$-term ($\frac{r^2+s^2-2}{24}$), and constant coefficient of $L_0^1$ ($-2n$) proves all $\tau_{-n}(\varphi_{r,r})$ and $\tau_{-n}(P_{r,s})$ are pairwise non-associate across all $n \in \mathbb{Z}$, $1 \le r \le s$, with constant leading $L_0$-coefficients (hence no nonconstant $c$-only divisors).
- **Step 3 (Local Smith Normal Form at Generic $c \notin Z_n$):** Verified carefully:
  - The finite excluded set $Z_n$ includes $1, 25$ and all roots of $\mathrm{Res}_{L_0}(Q_1, Q_2) \in \mathbb{C}[c]\setminus\{0\}$ across distinct irreducible factors of $\prod_{1\le m,k\le n} \tau_{-k}(K_m)$ and $\prod_{1\le m\le n} K_m(L_0 + j, c)$ ($0 \le j \le n$). Checked that $c \notin Z_n$ guarantees (1) all $h_{r,s}(c)$ ($1 \le rs \le n$) are simple and distinct, (2) all $h_{r,s}(c) + j$ ($0 \le j \le n$) are distinct, and (3) $D_{n-1}(h_0 + n, c) = \prod_{k=1}^{n-1} K_k(h_0 + n - k, c) \neq 0$ for every root $h_0 = h_{r,s}(c)$ of $K_m(L_0, c)$ ($1 \le m \le n$).
  - At $h_0 = h_{r,s}(c)$ ($rs = m \le n$), $\mathrm{ord}_\varepsilon(\det S^{(m)}) = p(0) = 1$ forces $\dim_{\mathbb{C}} \ker S^{(m)}(h_0, c) = 1$ with generator $v_0 = \hat{v}_0 \mathbf{1}$; non-degeneracy of $S^{(m-j)}(h_0, c)$ ($1 \le j \le m$) gives $L_j v_0 = 0$ for all $j \ge 1$ ($v_0$ singular of weight $h_0 + m$).
  - Since $\mathrm{gr} U(\mathrm{Vir}^-) \cong \mathrm{Sym}(\mathrm{Vir}^-)$ has no zero divisors, $\{L_\nu^\dagger v_0 : \nu \vdash n - m\}$ spans a $p(n-m)$-dimensional subspace of $\ker S^{(n)}(h_0, c)$. Together with $\sum e_i = \mathrm{ord}_\varepsilon(\det S^{(n)}) = p(n - m)$, Smith normal form over the DVR $\mathcal{O} = \mathbb{C}[L_0]_{(L_0 - h_0)}$ forces $e_i \in \{0, 1\}$ with exactly $p(n-m)$ ones and $\ker S^{(n)}(h_0, c) = \mathrm{span}_{\mathbb{C}}\{L_\nu^\dagger v_0 : \nu \vdash n - m\}$.
- **Step 4 (Inductive Proof of Claims 1 and 2):** Checked every shift sign and algebraic step:
  - $b^{(k)}_{\alpha,\beta}(L_0, c) L_\lambda^\dagger = L_\lambda^\dagger b^{(k)}_{\alpha,\beta}(L_0 + n, c)$ for $|\lambda| = n$ gives $B^{(n)}_{\mathrm{shifted}}(L_0, c) S^{(n)}(L_0, c) = R^{(n)}(L_0, c)$ with $D_{n-1}(L_0 + n, c) R^{(n)}(L_0, c) \in \mathrm{Mat}_{p(n)}(\mathbb{C}[L_0, c])$.
  - Note: by Cramer's rule + Kac's determinant + Step 2, $D_{n-1}(L_0 + n, c) \det S^{(n)}(L_0, c)$ already has constant leading $L_0$-coefficient and contains every irreducible factor of $D_{n-1}(L_0 + n, c)$ and $K_n(L_0, c)$ to multiplicity exactly $1$, making the cancellation proof completely self-contained (not even relying on Theorem 1.3 / Brown 2003).
  - **Cancellation of $K_m$ ($1 \le m < n$):** For $\nu \vdash n - m$, every term of $P[k](L_\nu^\dagger v_0)$ with $n - m < k \le n - 1$ has positive weight $k - (n - m) > 0$, hence annihilates singular $v_0$; thus $P_{n-1}(L_\nu^\dagger v_0) = P_{n-m}(L_\nu^\dagger v_0)$, which vanishes by specializing the universal identity $P_{n-m}|_{M[-(n-m)]} = 0$ via the Verma homomorphism $M(h_0+m, c) \to M(h_0, c)$, $\mathbf{1}_{h_0+m} \mapsto v_0$ (valid without poles because $D_{n-m}((h_0+m)+(n-m), c) = D_{n-m}(h_0+n, c) \neq 0$). Hence $R^{(n)}(h_0, c) \ker S^{(n)}(h_0, c) = 0$, so the $\varepsilon^{-1}$ entries in $S^{(n)}(L_0, c)^{-1}$ cancel over $\mathcal{O}$, yielding $B^{(n)}_{\mathrm{shifted}} \in \mathrm{Mat}_{p(n)}(\mathcal{O})$ and (by resultant avoidance on $c$) no divisor $q \mid K_m$ in any denominator.
  - **Necessity of every $q \mid K_n$:** Assuming $q \nmid g$ for all reduced denominators $g$ of $B^{(n)}_{\mathrm{shifted}}$ allows specializing $B^{(n)}_{\mathrm{shifted}}(h_0, c) S^{(n)}(h_0, c) = R^{(n)}(h_0, c)$ at generic $c$ and root $h_0$ of $q$, where applying both sides to the coordinate vector $u_0 \neq 0$ of the singular vector $v_0 \in \ker S^{(n)}(h_0, c)$ yields $0 = -P_{n-1}(v_0) = -u_0 \neq 0$, contradiction.
  - Consequently $D_N$ regularizes $P_N$ and divides every regularizing $Q \in \mathbb{C}[L_0, c]$ (hence has uniquely minimal degree, both total and in each variable, up to $\mathbb{C}^\times$, also settling Conjecture 1.5).

---

## 3. Independent Computational Verification & Gate 2 Novelty

- **Direct Re-Run of Independent Checker:** Executed `.venv/bin/python targets/hartwig-2611.23687-conj1.4/notes/check-check-3.py`:
  - **Exit code:** `0` (exact SymPy `QQ[L0, c]` / `DomainMatrix` arithmetic, zero floats).
  - **Raw output:**
    ```text
    [1/4] Checking Step 2: K_m primitivity, irreducibility, coprimality, D_1..D_6 & Kac formula...
    [2/4] Computing exact Virasoro extremal projector P_1..P_4 over Q(L0, c)...
    [3/4] Checking Step 3 (local SNF/singular vectors) & Step 4 (R*ker S = 0 / != 0) at c=899/35...
    [4/4] Checking Step 1 PBW shift automorphism L_lam^dagger f(L0,c) = f(L0-|lam|,c) L_lam^dagger...
    PASS
    ```
- **Gate 2 Novelty Receipts:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, and `notes/novelty-gate2-watch-6.md` all report **PASS** (open and uncontested; companion repo `sagarsmaths-afk/Virasoro-Extremal-Projector` verified to check only $N \le 6$).

**Conclusion:** Proof is complete, self-contained, mathematically rigorous, and independently verified. Ready for Gate 3 freshness check (`<1h`) before reporting.

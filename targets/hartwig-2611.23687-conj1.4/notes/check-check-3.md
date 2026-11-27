# Independent Check Report: `hartwig-2611.23687-conj1.4`

- **Checker:** `@check-3`
- **Verdict:** **PASS**
- **Primary Source:** `tools/.arxiv_cache/eprint/2611.23687/main.tex` (`arXiv:2611.23687v1`, Section 1, Conjecture 1.4 `\label{conj_denominator_N-truncated}`, L147–169).
- **Gate 2 Watch Status:** PASS (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

## 1. Primary-Source Fidelity Check

- **Verbatim match:** `TARGET.md` L12–21 reproduces the definitions of $K_n(L_0,c)$, $\tau_n$, $\varphi_{r,s}(L_0,c)$, regularization $Q P_N \in U(\mathrm{Vir})$, Theorem 1.3 (`D_N'`), and Conjecture 1.4 (`\label{conj_denominator_N-truncated}`, $D_N = \prod_{1\le n\le N} \tau_{-n}(K_n)$) verbatim from `main.tex` L130–169.
- **Numbering:** Section 1 (`\section{Introduction}`, L45) uses shared counter `lemma` per section: Theorem 1.1 (L87), Corollary 1.2 (L113), Theorem 1.3 (L155), **Conjecture 1.4** (L163), Conjecture 1.5 (L177). Matches `TARGET.md` and `PROOF.md`.
- **Minor editorial note on `PROOF.md`:** L56 parenthetically cites `eq. (1.7)` for Kac's determinant formula (`\label{eq_kac-denominator}`), which is actually **eq. (1.5)** (`main.tex` L122; eq. (1.7) is $K_n$), though L57 writes the exact formula accurately; L59 writes $U(\mathrm{Vir})(c - c)$ reusing $c$ for both the Virasoro central element and specialized scalar. Neither affects mathematical validity.

## 2. Proof Audit & Independent Mechanical Verification

- Checked `PROOF.md` Steps 1–4 against `main.tex` (`\ref{lem:shift-property}`, Theorem `\ref{denominator-theorem}`, eqs. `(3.22)–(3.31)`):
  - **Step 1:** Left $\mathbb{C}[L_0,c]$-freeness of $\{L_\lambda^\dagger L_\mu\}$ via $\tau_{-|\lambda|}$ gives exact coefficient-wise regularization criterion.
  - **Step 2:** Exact irreducibility in $\mathbb{C}[L_0,c]$ (via non-square discriminant $(c-1)(c-25)$) and pairwise non-associativity of $\tau_{-n}(\varphi_{r,r})$ and $\tau_{-n}(P_{r,s})$ across all $n \ge 1, 1 \le r \le s$.
  - **Step 3:** Local SNF over $\mathcal{O} = \mathbb{C}[L_0]_{(L_0 - h_0)}$ at generic $c \notin Z_n$: since $\mathrm{ord}_\varepsilon(\det S^{(n)}) = p(n - m)$ and $\dim_{\mathbb{C}} \ker S^{(n)}(h_0, c) \ge p(n - m)$ via free $U(\mathrm{Vir}^-)$-action on the level-$m$ singular vector $v_0$, all SNF exponents lie in $\{0, 1\}$ and $\ker S^{(n)}(h_0, c) = \mathrm{span}\{L_\nu^\dagger v_0 : \nu \vdash n - m\}$.
  - **Step 4:** Shifting $B^{(n)}_{\mathrm{shifted}}(L_0, c) S^{(n)}(L_0, c) = R^{(n)}(L_0, c)$, for $1 \le m < n$ the singular-descendant identity $P_{n-1}(L_\nu^\dagger v_0) = P_{n-m}(L_\nu^\dagger v_0) = 0$ (justified rigorously via $(U'\mathrm{Vir}^+) \cap U(\mathrm{Vir}) = U(\mathrm{Vir})\mathrm{Vir}^+$ and $D_{n-m}(h_0 + n, c) \neq 0$) cancels all $K_m$ ($m < n$) poles by Resultant specialization, while for $m = n$ ($v_0$ singular) $R^{(n)}(h_0, c) u_0 = -u_0 \neq 0$ forces every irreducible factor of $K_n$ to appear as a simple pole in $B^{(n)}_{\mathrm{shifted}}$.
- Wrote and executed independent verifier [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/hartwig-2611.23687-conj1.4/notes/check-check-3.py) directly from Virasoro commutators and `main.tex` L130–169 (AST `FLOAT_COUNT: 0`):
  1. `[1/4]` Verified Step 2 primitivity, irreducibility, squarefreeness, pairwise coprimality of $\tau_{-n}(K_m)$ ($1 \le m, n \le 6$), match with $D_1\dots D_6$ in `main.tex` L640–655, and Kac's determinant formula for $n = 1 \dots 5$.
  2. `[2/4]` Computed exact Virasoro extremal projector $P_1 \dots P_4$ over $\mathbb{Q}(L_0, c)$ from scratch via fraction-free `DomainMatrix.solve_den`, verifying Claims 1 & 2 (exact divisibility of denominators by $\tau_{-n}(K_n)$ and zero $K_m$ poles for $m < n$) and matching `main.tex` $P_1, P_2, P_3$.
  3. `[3/4]` Verified Step 3 (1D singular kernels, $L_k v_0 = 0$, $p(n-m)$-dimensional descendant kernels) and Step 4 ($R^{(n)} \ker S^{(n)} = 0$ for $m < n$; $R^{(n)} v_0 = -v_0 \neq 0$ for $m = n$) for all $n = 1 \dots 4$ and $rs = m \le n$ at generic $c = 899/35 \notin Z_4$.
  4. `[4/4]` Verified Step 1 PBW shift property $L_0 L_\lambda^\dagger \mathbf{1} = L_\lambda^\dagger (L_0 + |\lambda|)\mathbf{1}$ for $n = 1 \dots 4$.

### Raw Verifier Output

Command: `.venv/bin/python -u targets/hartwig-2611.23687-conj1.4/notes/check-check-3.py` (exit code `0`):
```text
[1/4] Checking Step 2: K_m primitivity, irreducibility, coprimality, D_1..D_6 & Kac formula...
[2/4] Computing exact Virasoro extremal projector P_1..P_4 over Q(L0, c)...
[3/4] Checking Step 3 (local SNF/singular vectors) & Step 4 (R*ker S = 0 / != 0) at c=899/35...
[4/4] Checking Step 1 PBW shift automorphism L_lam^dagger f(L0,c) = f(L0-|lam|,c) L_lam^dagger...
PASS
```

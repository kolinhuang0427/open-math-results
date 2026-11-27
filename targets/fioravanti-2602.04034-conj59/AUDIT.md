# Adversarial Audit Report (`audit-1`): `targets/fioravanti-2602.04034-conj59/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Audited UTC:** `2026-11-27T13:57Z`
- **Target:** Stefano Fioravanti, Michael Kompatscher, and Bernardo Rossi, *Clonoids over vector spaces*, `arXiv:2602.04034v1` (3 February 2026):
  - Section 7 (*Conclusion*), **Conjecture 59** (`\label{conjecture:strong}`, `main.tex` L1511–1515);
  - Section 1 (*Introduction*), **Conjecture 1** (`\label{conjecture:main}`, `main.tex` L221–223).
- **Files Inspected (Strict Isolation):** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, primary source `tools/.arxiv_cache/eprint/2602.04034/main.tex` (live `arxiv.org/abs/2602.04034` confirmed `[v1]` sole version), and Mayr–Wynne `tools/.arxiv_cache/eprint/2307.00076/main.tex` (`Theorem 1.3`, `\label{thm:notcoprime}`). Author `verify.py` and scratch `notes/` were **not** read.
- **Verdict:** **PASS** (`"written proof, internally audited"`)

---

## 1. Primary-Source, Version, & Citation Fidelity — PASS

- **Verbatim conjectures:** Both **Conjecture 59** (`conjecture:strong`, `main.tex` L1511–1513) and **Conjecture 1** (`conjecture:main`, `main.tex` L221–223) match `TARGET.md` and `PROOF.md` word-for-word, as does the Section 7 deduction paragraph (`main.tex` L1515).
- **Compiled numbering verified against `\newtheorem` counters in `main.tex`:** Every cited item matches the exact compiled number: `Conjecture 1` (`conjecture:main`), `Lemma 12` (`lemma:rkprod`), `Definition 14` (`def:unifgen`), `Definition 15` (`def:unifrep`), `Lemma 17` (`lemma:urobs`), `Theorem 18` (`theorem:unigen`), `Corollary 20` (`corollary:unigen`), `Proposition 21` (`proposition:ugproduct`), `Corollary 23` (`corollary:fingen`), `Lemma 27` (`lem:unifgenforpolyequiv`), `Lemma 30` (`lemma:ugsubalgebras`), `Corollary 35` (`corollary:orbitsupport`), `Theorem 49` (`theorem:main`), and `Conjecture 59` (`conjecture:strong`).
- **External citation verified:** Mayr–Wynne (2024), `arXiv:2307.00076v3`, **Theorem 1.3** (`\label{thm:notcoprime}`, `main.tex` L209–213) states verbatim that for any two finite modules $\mathbf{A}, \mathbf{B}$ whose orders are not coprime, there exists an infinite ascending chain of clonoids from $\mathbf{A}$ to $\mathbf{B}$.
- **Gate 2 novelty clear:** Passed by `@watch-6` (`#1464`), `@watch-5` (`#1466`), and `@watch-1` (`#1467`); confirmed `Hwzw/algebra-number-theory-drafts` `P32` (§6) covers only $\mathbb{Z}/p^2\mathbb{Z} \oplus (\mathbb{Z}/p\mathbb{Z})^s$ and explicitly leaves multiple $\mathbb{Z}/p^2\mathbb{Z}$ factors, higher exponents, Conjecture 59, and Conjecture 1 open.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

Every lemma, step, matrix dimension, exponent check, and edge case (trivial group $|A|=1$, trivial target $|B|=1$, trivial ring $1_R=0_R$, noncommutative unital rings, different rings $\mathbf{R}_A \neq \mathbf{R}_B$, $p=2$, $e \ge 3$, $s \ge 2$ with intermediate rank $1 \le \rk_{\mathbb{F}_p}(\mathbf{T}) < s$) was audited adversarially:

1. **§1 Preliminaries (L32–51) — PASS:** Central homomorphism $\iota \colon S = \mathbb{Z}[1/p] \to Z(\mathbf{R})$ is well-defined and unital for every unital associative ring $\mathbf{R}$ (possibly noncommutative or trivial) with $p \cdot 1_R \in R^\times$. Action $M(\mathbf{X}, \mathbf{Y}) = (M\mathbf{X}, \widetilde{M}\mathbf{Y})$ on $\mathbf{A} = (\mathbb{Z}/p^e\mathbb{Z})^s \times \mathbf{A}'$ ($p^{e-1}\mathbf{A}' = 0, e \ge 2$) and canonical isomorphism $\mathbb{F}_p \xrightarrow{\sim} p^{e-1}(\mathbb{Z}/p^e\mathbb{Z})$ are exact.
2. **Lemma 1 (Higher-Codimension Subspace Radon Inversion, L56–101) — PASS:**
   - $q$-Pascal `(P1)`, finite Cauchy product `(C1)`, and reciprocal Cauchy series `(C2)` in $\mathbb{Z}[[t]]$ are proved cleanly by induction; multiplying `(C1)` at $n = m - r$ by `(C2)` at $M = m - s \ge 1$ and extracting $[t^s]$ gives the exact orthogonality relation of Part (1), with exponent identity $\binom{c}{2} - \binom{s}{2} - s(m-s) = \binom{s-c+1}{2} - (m-c)s$ verified algebraically.
   - Part (2) subspace counting ($U \mapsto U/V_W$ gives $\binom{m-r}{c}_p$ codimension-$c$ subspaces containing $V_W = \mathrm{colspan}(W)$ of dimension $r \in \{0,\dots,s\}$) yields exact weight $\delta_{r, 0}$, hence $\phi(0)$, with integer outer coefficients and $p$-power inner denominators.
   - Part (3) additive convolution on $\mathrm{Mat}_{m \times s}(V_1) \times \mathrm{Mat}_{m \times s}(V_2) \to \mathrm{Mat}_{m \times s}(V_1 + V_2)$ with uniform fiber size $|V_1 \cap V_2|^s = |V_1|^s |V_2|^s / |V_1 + V_2|^s$ is airtight.
3. **Lemma 2 (Subgroup-Peeling Lemma, L104–125) — PASS:**
   - Factor lifting $M_{i, \nu} = U_{i, \nu} V_{i, \nu}$ over $\mathbb{Z}/p^e\mathbb{Z}$ preserves inner rank $\le k$ and matches $r_{i,\nu}$ on $C_i^m$ while preserving every subgroup $C_j^m$.
   - Recursive peeling $J_i = J_{i-1} + I_i - I_i \circ J_{i-1}$ has the exact right composition order: on $C_i^m$, $I_i(J_{i-1}(f))(X) = J_{i-1}(f)(X)$ and $I_i(f)(X) = f(X)$; on $C_j^m$ ($j < i$), $M_{i,\nu} X \in C_j^m \implies I_i(J_{i-1}(f))(X) = I_i(f)(X)$, giving $J_i(f)(X) = J_{i-1}(f)(X) = f(X)$.
4. **§3 Theorem 1 (Proof of Conjecture 59 / `conjecture:strong`, L128–231) — PASS:**
   - Strong induction on $N = \log_p |\mathbf{A}| \ge 0$ with $k(\mathbf{A}) = \max(1, N)$:
     - Trivial group $N = 0$ ($k = 1$, zero matrix $0_{m \times 1} 0_{1 \times m} \in R_1^{m, m}(\mathbf{A})$) and exponent-$p$ base case $e = 1, N = s \ge 1$ (via Theorem 49 `theorem:main` on $\mathbb{F}_p^s$ over $S = \mathbb{Z}[1/p]$) are exact.
     - Inductive step ($e \ge 2, N \ge 2$): $\mathbf{A} \cong (\mathbb{Z}/p^e\mathbb{Z})^s \times \mathbf{A}'$ with $p^{e-1}\mathbf{A}' = 0$, $s \ge 1$, $N \ge 2s \ge 2$, $k = N$, $m = N + 1 \ge 2s + 1$, $\overline{\mathbf{A}} = \mathbf{A}/p^{e-1}\mathbf{A}$ of exponent $p^{e-1}$ and order $p^{N-s}$ with $k' = N - s \ge s \ge 1$, $s + k' = k$, and $m - s = k' + 1 \ge 2$. Zero degenerate cases.
     - **Step 1:** Maximal subgroups $C_1, \dots, C_L$ ($L = \frac{p^d - 1}{p - 1} \ge 1$, order $p^{N-1} \ge p$, $N - 1 < k$) peeled by Lemma 2; complement $O = \{X : \langle X \rangle = \mathbf{A}\}$ verified $\mathrm{GL}_m(\mathbb{Z}/p^e\mathbb{Z})$-invariant, $p^{e-1}\mathbf{A}$-shift invariant (Nakayama/Frattini), and strictly full mod-$p$ column rank $\rk_{\mathbb{F}_p}(\bar{\mathbf{X}}) = s$ via $C_{\mathbf{c}} = \ker(\varphi_{\mathbf{c}})$.
     - **Step 2:** Matrix $M(\widetilde{B}, U', W') \in R_{s+k'}^{m,m}(\mathbf{A}) = R_k^{m,m}(\mathbf{A})$ acts on $\mathbf{Y}$ independently of $(W', U')$ as $\binom{\mathbf{Y}_1}{\widetilde{B}\mathbf{Y}'}$ and on $\mathbf{X}$ as $\binom{\mathbf{X}_1}{UV\mathbf{X}' + p^{e-1}[W', U']\mathbf{T}}$. Case 1 ($\rk_{\mathbb{F}_p}(\mathbf{T}) = s$) gives exact surjectivity via left inverse $\mathbf{L}\mathbf{T} = I_s$ with uniform multiplicity $p^{(m-s)k'}$. Case 2 ($\rk_{\mathbb{F}_p}(\mathbf{T}) < s$, including partial rank $1 \le \mathrm{rk}(\mathbf{T}) < s$ for $s \ge 2$ and higher-exponent $e \ge 3$ where $\widetilde{B}\widetilde{\mathbf{X}}' \not\equiv 0 \pmod{p^{e-1}}$ while $\bar{B}\bar{\mathbf{X}}'\mathbf{c} = \mathbf{0} \pmod p$) forces every evaluation on both sides into $C_{\mathbf{c}}^m \subseteq A^m \setminus O$, so both sides vanish identically.
     - **Step 3:** Conjugation via lifted $T_H \in \mathrm{GL}_m(\mathbb{Z}/p^e\mathbb{Z})$ builds $A_H$ for all codimension-$s$ $H$ while preserving $\mathrm{supp}(\cdot) \subseteq O$; explicit basis split $H_1 = \mathrm{span}(u_1, \dots, u_{m-s})$, $H_2 = \mathrm{span}(u_{s-c+1}, \dots, u_{m-c})$ satisfies $1 \le s - c + 1 \le m - s < m - c$ (since $m \ge 2s + 1$), giving $A_U = A_{H_1} \circ A_{H_2}$ for all codimension $c < s$ via Lemma 1(3); Radon sum $K$ recovers $K(h) = h$ on $\mathrm{supp}(h) \subseteq O$ by Lemma 1(2).
     - **Step 4:** $I = J_{\mathrm{prop}} + K - K \circ J_{\mathrm{prop}} = \mathrm{id}$ on $\mathcal{O}_{\mathbf{A}, S}^{(k+1)}$ lifts to all arities by Theorem 18 (`theorem:unigen`) and transfers to every unital ring $\mathbf{R}$ with $p \cdot 1_R \in R^\times$ via $\iota \colon S \to Z(\mathbf{R})$ applied to the exact scalar identity $\sum_{M_i X = Y} \alpha_i = \delta_{X, Y}$.
5. **§4 Theorem 2 (General Coprime Modules & Proof of Conjecture 1 / `conjecture:main`, L234–258) — PASS:**
   - Part 1: $|A|=1$ handled directly; for $|A|>1$, $|A|\cdot 1_R \in R^\times \implies p_j \cdot 1_R \in R^\times$; CRT yields exact clone factorization $\mathrm{Clo}(\mathbf{A}_{\mathrm{ab}}) = \prod_j \mathrm{Clo}(\mathbf{A}_{p_j})$; Proposition 21 (`proposition:ugproduct`) + reduct $\mathrm{Clo}(\mathbf{A}_{\mathrm{ab}}) \subseteq \mathrm{Clo}(\mathbf{A})$ + Corollary 35 (`corollary:orbitsupport`) + Corollary 20 (`corollary:unigen`) yield $k(\mathbf{A})$-ary uniform generation and clonoid generation for every left $\mathbf{R}$-module $\mathbf{B}$.
   - Part 2: Quotienting by annihilator $I_B$ gives faithful $\mathbf{R} = \mathbf{R}_B/I_B$-module $\mathbf{B}'$ with $n_B \cdot 1_R = 0_R$ ($n_B = \exp(B, +)$); $\gcd(|A|, |B|) = 1 \implies \gcd(|A|, n_B) = 1 \implies |A| \cdot 1_R \in R^\times$ (including $|B|=1$ trivial ring); finiteness ($2^{|B|^{|A|^{k(\mathbf{A})}}} < \infty$) and relational arity bound $|A|^{k(\mathbf{A})}$ follow from Part 1 and Corollary 23 (`corollary:fingen`). Converse follows directly from Mayr–Wynne (2024) Theorem 1.3 (`thm:notcoprime`).

---

## 3. Independent Exact Verification — PASS

- **Checker AST check:** `FLOATS: [] FLOAT_CALLS: []` on `targets/fioravanti-2602.04034-conj59/notes/check-check-1.py`.
- **Executed checker:** `.venv/bin/python -u targets/fioravanti-2602.04034-conj59/notes/check-check-1.py` -> exit code `0`, raw output `PASS` (verified Lemma 1 `(P1)`/`(C1)`/`(C2)` & exhaustive subspace checks; full exact inductive operators on $\mathbb{Z}_2$, $\mathbb{Z}_3$, $\mathbb{F}_2^2$, $\mathbb{Z}_4$, $\mathbb{Z}_9$; mixed $\mathbb{Z}_4 \times \mathbb{Z}_2$ and $\mathbb{Z}_8 \times \mathbb{Z}_2$ Step 2 collapse; CRT on $\mathbb{Z}_6$, $\mathbb{Z}_{12}$; raw noncommutative $M_2(\mathbb{Z}/5\mathbb{Z})$ and trivial-ring transfer).
- **Auditor adversarial $s = 2$ stress test:** Independently verified Step 2 on $\mathbf{A} = \mathbb{Z}_4 \times \mathbb{Z}_4$ ($p = 2, e = 2, s = 2, k' = 2, m = 5$, all $4096$ pairs $(W', U')$) on tuples $X \in O$ hitting **all three** mod-$2$ rank regimes of $\mathbf{T}$: Case 1 (`rk(T) = 2`, `lhs = 128 == rhs = 128`), Case 2 partial nonzero rank (`rk(T) = 1 < s`, `lhs = 0 == rhs = 0`), and Case 2 zero rank (`rk(T) = 0`, `lhs = 0 == rhs = 0`).

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Ready for Gate 3 freshness verification (`@watch-1`, `@watch-5`, `@watch-6`).

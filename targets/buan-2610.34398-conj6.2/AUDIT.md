# Adversarial Audit Report (`audit-1`): `targets/buan-2610.34398-conj6.2/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Aslak B. Buan, Eric J. Hanson, and Bethany R. Marsh, *Lifting $\tau$-exceptional sequences*, `arXiv:2610.34398v1` (2026-10-25), Section 7.1 (`\subsection{TF-ordered $\tau$-rigid modules}`, `\label{sec:conj1}`), **Conjecture 7.2** (`\label{conj:TFordered}`, L1932–1938 of `lifting_arxiv_25102026.tex`; tracked under legacy slug `targets/buan-2610.34398-conj6.2/`)
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, primary source `tools/.arxiv_cache/eprint/2610.34398/lifting_arxiv_25102026.tex` (`2610.34398v1`, sole version on arXiv), and `watch/snapshots/**`
- **Verdict:** **PASS** (Label: `written proof, internally audited`)

---

## 1. Primary-Source, Version, & Citation Verification — PASS

- **Version check (`tools/.arxiv_cache/abs/2610.34398.html`):** `2610.34398v1` (`2026-10-25`) is the sole version on arXiv.
- **Verbatim statement (`lifting_arxiv_25102026.tex`, L1916–1938):**
  - Over an arbitrary field $k$ and finite-dimensional $\tau$-tilting finite $k$-algebra $\Lambda$ (left modules $\mathrm{mod}\Lambda$, L282–284; NOT requiring $k$ algebraically closed or $\Lambda$ basic), two-sided ideal $I \subseteq \mathrm{rad}\Lambda$, $F = (\Lambda/I) \otimes_\Lambda -$, Mendoza–Treffinger bijections $\omega, \omega_I$ (`Theorem 7.1` `\label{thm:TF-bij}`, L1922–1927), and $L_I = \omega^{-1} \Delta_I \omega_I$:
  - **Conjecture 7.2** (`\label{conj:TFordered}`, L1932–1938): *"Let $(M_1, M_2, \ldots, M_t)$ be a TF-ordered $\tau$-rigid $\Lambda/I$-module and let $L_I(M_1, M_2, \ldots, M_t) = (N_1, N_2, \ldots, N_t)$. Then $F(N_i) = M_i^{r_i} \amalg X$ where $X \in \mathrm{add}(\coprod_{j=i+1}^t M_j)$ and $r_i \geq 1$ is an integer."*
  - Matches `TARGET.md` and `PROOF.md` verbatim (including explicit documentation of the legacy directory slug `conj6.2` vs compiled Section 7.1 Conjecture 7.2).
- **Compiled LaTeX counters (`lifting_arxiv_25102026.tex`, shared `theorem` counter within sections):** Every `[BHM]` citation in `PROOF.md` verified verbatim against the source:
  - `Thm. 1.1` (`thm:main1`, L224; recursive proof L1587–1672), `§2.2` (L359–399), `Setup 4.1` (`setupCZ`, L595), `Prop. 4.8(a),(b)` (`prop:FZaddC`, L783–791), `Thm. 5.1` (`thm:jasso-module-category`, L824), `Prop. 5.6` (`prop:FZ-defined`, L1014–1042), `Lem. 5.7` (`lem:fU-projectives`, L1144–1154), `Prop. 5.8` (`prop:FZ-projectives`, L1209–1218), `Thm. 5.10` (`thm:reduction-functor`, L1520–1556), `Lem. 5.11` (`lem:torsion-classes-under-FZ`, L1722), `Thm. 7.1` (`thm:TF-bij`, L1922–1927), `Conj. 7.2` (`conj:TFordered`, L1932–1938).
- **Gate 2 Novelty:** Cleared by `@watch-5` (`#1226`), `@watch-1` (`#1230`), and `@watch-6` (`#1261`); `tools/novelty_grep.py` confirms `0` hits across local snapshots.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

Checked every lemma, functoriality/naturality claim, left-vs-right convention, and arbitrary-field validity (never assuming $k = \bar{k}$ or $\Lambda$ basic):

1. **Section 1 & Eq. (1) (L10–52):**
   - Minimal projective presentation $P_X = (Q_1 \xrightarrow{d_X} Q_0)$ in degrees $[-1, 0]$ with $(X[1])^m = X^{m+1}, d_{X[1]} = -d_X$; truncation triangle $H^{-1}(P_Y)[1] \to P_Y \to Y \to H^{-1}(P_Y)[2]$ and Nakayama duality $D\mathrm{Hom}_A(Q, Y) \cong \mathrm{Hom}_A(Y, \nu Q)$ yield Eq. (1) $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(P_X, P_Y[1]) \cong D\mathrm{Hom}_A(Y, \tau_A X)$ cleanly over any field $k$.
   - **Corollary 2** (Conjecture 7.2 from Theorem 1): right exactness of $F$ gives $H^0(F(P_N)) \cong F(N)$, immediate.
   - **Corollary 3** ($r_i = 1$ and $F(Z) \cong C$): since $J \subseteq \mathrm{rad} A$, $G = (A/J) \otimes_A -$ preserves simple tops and induces a bijection on isomorphism classes of indecomposable projectives, hence an isomorphism $K_0(G) \colon K_0(\mathrm{proj} A) \xrightarrow{\sim} K_0(\mathrm{proj}(A/J)) \cong \mathbb{Z}^{\mathrm{rk} A}$ over any field $k$. Because $P_Z$ is an indecomposable summand of the basic 2-term silting complex $P_{B_Z}$, $[P_Z]$ is part of a $\mathbb{Z}$-basis of $K_0(\mathrm{proj} A)$ ([AI, Thm. 2.27], [AIR, Thm. 5.1]), hence primitive; $K_0(G)([P_Z]) = r \cdot [P_C]$ forces $r = 1$, and Step 4 of Section 3 preserves $r_i = 1$ verbatim through the induction. Airtight.
2. **Lemma 2.1 (L57–73):**
   - (a) Degree-overlap lifting + null-homotopy sign $\tilde{f} = h^0 d - d h^{-1}$ (exact for $d_{T[1]} = -d_T$) proves $G(T)$ is 2-term presilting.
   - (b) $J \subseteq \mathrm{rad} A \implies \mathrm{rad}(A/J) = (\mathrm{rad} A)/J$, so $\mathrm{Im}(G(d_X)) \subseteq \mathrm{rad} G(Q_0)$ makes $G(Q_0) \twoheadrightarrow G(X)$ a projective cover; splitting off a projective cover $Q'_1 \twoheadrightarrow \mathrm{Im}(G(d_X))$ from $G(Q_1)$ gives $G(P_X) \cong P_{G(X)} \oplus R[1]$.
   - (c) Combining (a), (b), [BHM, Prop. 4.8(a)], and [AIR, Thm. 3.2, Prop. 2.2(b)] forces $|\mathrm{basic}(R)| \le \mathrm{rk}(A/J) - |B_C| = 0$, hence $G(P_{B_Z}) \cong P_{G(B_Z)}$, $\mathrm{add} G(P_{B_Z}) = \mathrm{add} P_{B_C}$, and $G(P_Z) \cong P_C^r$ (by Krull–Schmidt + [BHM, Prop. 4.8(b)]). Airtight.
3. **Lemma 2.2 (L76–141):**
   - (a) Silting co-heart criterion: $\mathrm{smd}(\mathcal{S}) = \mathrm{thick}(B) = K^b(\mathrm{proj} A)$ via direct-sum triangle trick and octahedral associativity; peeling off $b > 0$ and $a < 0$ leaves $a = b = 0$, hence $K \in \mathrm{add}(B)$ *(minor note: if $K = 0$, $K \in \mathrm{add}(B)$ is trivial, and for $K \ne 0$ the $a = b > 0$ / $a = b < 0$ empty-product cases immediately give $\mathrm{id}_K = 0$, impossible, so $a < b$ holds whenever peeling is invoked)*.
   - (b) Every 2-term complex $T$ decomposes in $K^b(\mathrm{proj} A)$ as $P_{H^0(T)} \oplus R[1]$; $\mathrm{Hom}(B, T[m]) = 0$ ($m \ge 1$) follows from degree bounds ($m \ge 2$), $R[2]$ in degree $-2$, and Eq. (1) + $Y \in {}^\perp \tau_A Z = \mathrm{Gen}(B_Z)$ ($m = 1$). Approximation triangle $B_1 \to B_0 \to T \to B_1[1]$ has $B_1 \in \mathrm{add}(B)$ by (a). Uniqueness in $K^b(\mathrm{add} B)$ verified cleanly (noting $g(rs) = g \implies g((rs)^{-1} r) = g'$ so $g' = (g, 0)$ on $B_0 \oplus S$, and TR3 yields the contractible summand $(S \xrightarrow{\mathrm{id}} S)$).
   - (c) Null-homotopy lifting for $\mathrm{Hom}_{K^b(\mathrm{add} B)}(X_T^\bullet, X_{T'}^\bullet[1]) = 0$, minimal radical splitting, cone isomorphism, and idempotent lifting modulo the nilpotent ideal of null-homotopic endomorphisms in the finite-dimensional $k$-algebra $\mathrm{End}_{C^b(\mathrm{add} B)}(X_T^{\min})$ (valid over any field $k$) all hold strictly.
   - (d) Right exactness of $H^0$ on (3) + lifting $u \colon Z \to Y$ to $P_Z \to P_Y \hookrightarrow T$ via $\mathrm{add}(B)$-approximation gives $H^0(g)(t_Z(Q_0)) = t_Z(Y)$, whence exactness of (5) in $\mathrm{mod} A$ and in the wide subcategory $\mathsf{J}(Z)$ yields $H^0(K^b(\Phi_Z)(X_T^\bullet)) \cong f_Z(H^0(T))$. Airtight.
4. **Proposition 2.3 (L144–180):**
   - (a) $\widetilde{A} = \mathrm{End}_{K^b(\mathrm{proj} A)}(B)^{\mathrm{op}}$ gives $K^b(\mathrm{add} B) \simeq K^b(\mathrm{proj}\widetilde{A})$ (matching left-module convention); fullness and density of $\Phi_Z = f_Z \circ H^0$ ([BHM, Lem. 5.7]) preserve presilting and thick generation; combining Lemma 2.2(d) with Jasso's $\tau$-tilting reduction [J, Thm. 3.16, Thm. 3.23] shows $\Psi_Z \colon 2\text{-}\mathrm{silt}_{P_Z}(A) \xrightarrow{\sim} 2\text{-}\mathrm{silt}(\mathsf{J}(Z))$ is a bijection.
   - (b) Direct mutation-pigeonhole argument (mutating a 2-term silting completion $S = P_Z \oplus T_1 \oplus \cdots \oplus T_{n-1}$ at each $T_k$ via [AIR, Thm. 2.18, 3.2], comparing against $\mathrm{rk}\mathsf{J}(Z) = n - 1$ [J, Thm. 3.8]) proves cleanly that for every indecomposable $T \not\cong P_Z$ compatible with $P_Z$—**including** shifted projectives $Q[1]$—$K^b(\Phi_Z)(X_T^\bullet) \cong W_T^{c_T}$ with a unique indecomposable $W_T$ and $c_T \ge 1$. Airtight.
5. **Lemmas 2.4–2.5 (L183–216):**
   - Lemma 2.4: Jasso's torsion-class lattice bijection [J, Thm. 3.23] gives $\mathcal{T}_Y = \mathcal{T}_M =: \mathcal{T}$, and split-projective characterization $P_s(\mathcal{T})$ ([BHM, §2.2]) forces $Y \cong M$ (since $f_C(Y) \ne 0 \implies f_C(M) \ne 0$ and $Y, M$ are each the unique indecomposable class in $\mathrm{add}(P_s(\mathcal{T})) \setminus \mathrm{add}(C)$).
   - Lemma 2.5: Right-to-left peeling of $\omega$ ([BHM, Thm. 7.1]) satisfies $f_{\overline{U}_{i+1} \amalg \cdots \amalg \overline{U}_{t-1}}^{\mathsf{J}(U)}(\overline{U}_i) \cong f_{U_{i+1} \amalg \cdots \amalg U_t}(U_i)$ by uniqueness of the canonical torsion sequence, giving $(H(\overline{N}_1), \dots, H(\overline{N}_{t-1})) = L_{I_Z}(H'(\overline{M}_1), \dots, H'(\overline{M}_{t-1}))$ under [BHM, Thm. 5.10]. Airtight.
6. **Section 3 — Proof of Theorem 1 (L219–314):**
   - Step 1: Naturality of $\alpha_X \colon F(H^0(X)) \xrightarrow{\sim} H^0(F(X))$ descends cleanly from $C^b$ to $K^b$, and composing with $\rho_{H^0(X)}$ ([BHM, Prop. 5.6]) yields a natural isomorphism of triangle functors $K^b(\Phi_C) \circ K^b(F) \simeq K^b(F_Z) \circ K^b(\Phi_Z)$ on $K^b(\mathrm{add} B)$.
   - Step 2: Evaluates right-then-down on $X_{P_{N_i}}^\bullet$ via Proposition 2.3(b), Lemma 2.2(d), and the induction hypothesis on $(\Gamma, I_Z)$ ([BHM, Thm. 5.10]).
   - Step 3: Applies the triangle functor $F$ to triangle (10), uses Lemma 2.2(b) uniqueness over $(\Lambda/I, C)$ to identify $K^b(F)(X^\bullet) \cong \bigoplus_\alpha X_{T_\alpha}^\bullet$, and evaluates $K^b(\Phi_C)$ via Proposition 2.3(b).
   - Step 4: Krull–Schmidt matching in (14) shows EVERY summand $T_\alpha \not\cong P_C$ has $f_C(H^0(T_\alpha)) \cong \overline{M}_j^{c_\alpha} \ne 0$, simultaneously ruling out any shifted projective $T_\alpha \cong Q[1]$, identifying $T_\alpha \cong P_{M_j}$ via Lemma 2.4, forcing $c_\alpha = 1$, and preserving the exact multiplicities $r_i \ge 1$ ($= 1$ by Corollary 3) and $s_{ij} \ge 0$ (with $s_{it}$ counting copies of $P_C = P_{M_t}$). Zero gaps.

---

## 3. Independent Exact Verification — PASS

- Command: `.venv/bin/python -u targets/buan-2610.34398-conj6.2/notes/check-check-2.py`
- Exit code: `0`, raw output: `PASS (all 8 algebra-quotient pairs verified in 17.39s, zero floats)`
- AST zero-float check: `FLOATS: []` (pure exact Python `int` + `fractions.Fraction`).
- Independently verifies Eq. (1), Lemma 2.1(c), Corollary 3 ($r_i = 1$, $F(Z) \cong C$), recursive Jasso reduction $L_I$, Strong Theorem 1 ($R[1] = 0$ and exact $P_0, P_1$ / $g$-vector match), and Conjecture 7.2 across all **434** TF-ordered sequences in 8 diverse algebra-quotient pairs (Paper Examples 1–3, $C_3/J^4 \to C_3/J^3$, 2-cycle, $D_4 \to D_4/\langle ca\rangle$, and $\Pi(A_3) \to kA_3$, including 31 terms with $X \ne 0$ and 10 non-lifted modules exhibiting $R[1] \ne 0$).

---

## 4. Verdict & Handoff

**PASS.** The proof of Buan–Hanson–Marsh (`arXiv:2610.34398v1`) Conjecture 7.2—together with Strong Theorem 1 and sharp multiplicity Corollary 3 ($r_i = 1$, $F(Z) \cong C$)—is complete, self-contained, and rigorous over arbitrary fields. Ready for Gate 3 freshness verification (`<1h`) by `@watch-1`, `@watch-5`, `@watch-6` prior to `@coordinator` final verification.

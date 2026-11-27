# Adversarial Audit Report (`audit-1`): `targets/godard-2605.21866-prob3/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Jean Godard and Lucas Reis, *Graphs from quadratic forms and vector spaces over finite fields*, `arXiv:2605.21866v1` (`2026-05-21`), Section 5, **Problem 5.3** (3rd problem in Section 5, lines 363–365 of `godard-reis.tex`)
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after primary-source numbering fixes per `#375`), `notes/check-check-1.md`, `notes/check-check-1.py`, and primary source `tools/.arxiv_cache/eprint/2605.21866/godard-reis.tex`
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Re-Audit Summary (Primary-Source Numbering Fixes)

The initial audit confirmed zero mathematical gaps across all four sections of `PROOF.md` and flagged five environment-number mis-citations caused by `godard-reis.tex` sharing the `[theorem]` counter across all theorem-like environments (`lines 31–42`). `@attack-3` patched all five (`#375`):
- `TARGET.md` L15, L17, L21, L25 and `PROOF.md` L1, L3, L13 now cite **`Problem 5.3`** (3rd problem in Section 5) and **`Definition 1.1`**.
- `PROOF.md` L31 cites **`Remark 1.6`** (`rem:disc`); L45 cites **`Lemma 2.3`** (`lem:indicator`); L48 cites **`Lemma 2.4`** (`lem:boundaffine`); L54 cites **`Lemma 2.5`** (`lem:GS`).

All primary-source definitions, statements, and citations now match `godard-reis.tex` verbatim.

---

## 2. Full Mathematical Audit (Sections 1–4)

- **Preliminary reduction (L23):** For every $n \ge 4$, $d_0 = n/p_0(n) \le n/2$, so $2 \le s = d_0 + 1 < n$; passing to an $s$-dimensional $\mathbb{F}_q$-subspace yields a spanning subgraph. Exact.
- **Section 1 (Lower bound, L27–38):**
  - Case 1a ($n = 2k$ even): $\frac{q^{2k}-1}{2} = \frac{q^k+1}{2}(q^k-1)$ with $\frac{q^k+1}{2} \in \mathbb{Z}$, so $\mathbb{F}_{q^k} \subseteq (\mathbb{F}_{q^{2k}})^2$; $V = \alpha \mathbb{F}_{q^k}$ ($\alpha$ nonsquare) contains no nonzero squares, so $0$ is isolated in $\Gamma(Q_b, V)$ for every $b \in \mathbb{F}_{q^n}^*$. Exact.
  - Case 1b ($n$ odd, $p_0 \ge 3$): $V = \mathbb{F}_{q^{d_0}}$, $b \in \mathbb{F}_{q^{d_0}}^*$; completing the square gives $(y + \frac{b}{2}x)^2 \in \mathbb{F}_{q^{d_0}}$, so $[\mathbb{F}_{q^{d_0}}(w) : \mathbb{F}_{q^{d_0}}] \mid \gcd(2, p_0) = 1$, forcing $y \in \mathbb{F}_{q^{d_0}}$. Exact.
- **Section 2 (Even $n = 2k \ge 4$, $q \ge 5$, L41–82):**
  - Self-contained proofs of character orthogonality on $V_*$ ($\#V_* = q^j$), Lemma 2.1 (affine quadratic character sum bound $\frac{q^j-1}{q^j} q^{n/2}$ via Gauss sum modulus $q^{n/2}$), Lemma 2.2 (bilinear additive character sum bound $q^{n/2}(\#A)$ via Cauchy–Schwarz), and Proposition 2.3 (combining upper/lower bounds on $q^j P(A)$ gives $\#A \ge q^{2k}(1 - 2/q) + 2q^k > \frac{1}{2} q^{2k}$ for all odd $q \ge 5$, handling diagonal $(x,x)$ pairs cleanly). Exact.
- **Section 3 (Odd $n \ge 5$, $b = \pm 2$, L86–135):**
  - Lemma 3.1 ($b = -2$ Cayley graph; $b = +2$ closure of component $C_0$ of $0$ under negation and $x \mapsto \alpha - x$): exact.
  - Proposition 3.2: Step 1 subspace-avoidance count $1 + (\tau(n)-1)(q^{s-1}-1) < q^s$ ($s \ge 2$, $q > 2^{n-1} > n \ge \tau(n)$); Step 2 norm-quadratic character identity $\eta_{\mathbb{F}_{q^n}}(z) = \eta_{\mathbb{F}_q}(N(z))$ and Weil bound (Lidl–Niederreiter Thm. 5.41) for squarefree odd-degree $f(t)$; Step 3 invariance of $\widetilde{Q}$ under $Z_j \mapsto -Z_j$ ($2^{n-1}$ even), Kummer theory over $\overline{\mathbb{F}_q}(t)$ ($\mathrm{char} \neq 2$, $\mathrm{Gal} \cong \{\pm 1\}^n$) proving $P(t) \not\equiv 0$ of degree $\le 2^{n-2}$, hence $\le 2^{n-1}$ points in $C(\mathbb{F}_q)$ with $\alpha \in H$; Step 4 concludes $\mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$. Exact.
- **Section 4 (Odd $n \ge 5$, $b \notin \{0, \pm 2\}$, L138–334):**
  - **4.1 / Lemma 4.1:** Diagonalization $\iota$, $b_i \notin \{0, \pm 2\}$, $\Delta_i \neq 0$, and pairwise linear independence of $L_0, \dots, L_{n-1}$ via Frobenius $\gcd(j-i, n) \le d_0 < s$. Exact.
  - **4.2 / Lemma 4.2:** Inductive Kummer domain/flatness/separability argument (freeness of rank $2^n$ over $B[t]$, pairwise non-associate degree-$1$ primes $f_i(t)$ in $F[t]$, $\mathrm{char} \neq 2$); complete-intersection $S_2$ + Jacobian singular-locus codimension $\ge |I| + 2 \ge 5$ (even at $s = 2$) via finite projection $R \to \mathbb{A}^n_x \times \mathbb{A}^s_t$ giving $R_1$, hence normality of $R$. Exact.
  - **4.3 / Lemma 4.3:** (1) Derivation formula $U_j = D(c_j)^{-1}(V_{K_j} + D(a_j)(U_{j-1}\otimes K_j))$ with $c_{j,i}, a_{j,i} \neq 0$, and $\tau_i$-twist killing stagnation before dim $n$, reaching $\dim U_{k_0} = n$ at $k_0 = n - s + 1$; (2) char-$p$-safe algebraic independence over $\Omega$ (perfectness of $\Omega$), Matsumura Thm. 26.9 giving separable generation of $K_k/E_k$, finite separability of $L_k/E_k$, and regularity of $K_k/L_k$; (3) exact count of $d_{k_0}$ irreducible components of geometric generic fiber $F$ and Bézout bound (Hartshorne Thm. I.7.7) $d_{k_0} \le 2^{k_0(n-s)}$. Exact.
  - **4.4 / Lemmas 4.4–4.7 & Prop. 4.8:**
    - Lemma 4.4: Regularity of $H/E_k, H/E_{k+1}$, algebraic closedness of $M = L_k \cdot H \cong L_k \otimes_{E_k} H$ in $F_{k+1}$, and $d_{k+1} \mid d_k$. Exact.
    - Lemma 4.5: DVR base-change invariance of étaleness, handling wild and residue-inseparable ramification cleanly via regularity of $k_2 / k_1$ ($\ell_i \otimes_{k_1} k_2 \hookrightarrow \overline{k_1} \otimes_{k_1} k_2$ is a field). Exact.
    - Lemma 4.6: (1) Zariski–Nagata purity (SGA 1, Exp. X, Thm. 3.1) + flat dimension formula + normality of $R$ + Lemma 4.5 giving $B_Z^{(1)} = p_2^{-1}(B_{k+1}) = p_1^{-1}(B_k)$; $\tau_i$-invariance forcing $B_{k+1} = B_k = \emptyset$; (2) pulling back along $g(x) = \tau_i(x, y^*)$ gives triviality of $C_0 \times_{\mathbb{A}^1_T} N(y^*)$ over $N(y^*)$; $T, t_2, \dots, t_s$ algebraically independent over $\Omega$ (with $g_m \neq 0$ by Lemma 4.1 since $L_m \not\propto L_i = t_1$), Kummer abelian $(\mathbb{Z}/2\mathbb{Z})^r$ Galois group descending to $\mathrm{Gal}(K(C_0)/\Omega(T)) \cong (\mathbb{Z}/2\mathbb{Z})^m$, and ramification contradiction at any root $T_0 \in \Omega$ of squarefree non-constant $f(T)$ forcing $m = 0, e = 1$. Exact.
    - Lemma 4.7: EGA IV$_3$ Thm. 9.7.7(iv) spreading of idempotents over finite $S \to D(g)$ (identities hold in $B \otimes_{\Omega[Y']} A_S \hookrightarrow B \otimes_{\Omega[Y']} K_1$ by flatness of $B$), Nullstellensatz closed point $s \in \bigcap S_r(\Omega)$ forcing $c = d$, hence $L \otimes_{K_0} \overline{K_0} \cong \prod_{r=1}^d \overline{K_0}(Y_0)$, $L = M_0(Y_0)$, $B = B_0[Y_0]$, and induction on $n$ forcing $d = 1$. Exact.
    - Proposition 4.8: Strictly halving $d_k$ until $1$ yields $d_K = 1$ at $K = (n - s + 1)^2$ and geometric integrality of the generic fiber of $\varphi_K$ of dimension $Ks - n$. Exact.
  - **4.5 / Theorem 4.9 & Synthesis:** Constructibility over $\mathcal{S} \times \mathbb{A}^n_y$ over $\mathbb{Z}[1/2]$ (EGA IV$_3$, Thm. 9.7.7(iv) & Cor. 9.5.6), Chevalley (EGA IV$_1$, Thm. 1.8.4) + Noetherian induction giving uniform $D_0(n)$, Schwartz–Zippel giving $\ge q^n - D_0(n) q^{n-1}$ good endpoints, Lang–Weil (1954, Thm. 1 & Lemma 1, with $r = Ks - n \ge 3$ and unconditional boundary bound $\le D\pi_{r-1}(q) < 2Dq^{r-1}$) giving $\#X_y(\mathbb{F}_q) > 0$ for $q \ge q_1(n)$, and pigeonhole on $K$-balls giving connectedness with diameter $\le 2K$ for $q \ge \max(q_1(n), 2D_0(n)+1)$. Synthesis threshold inequality verified exact.

---

## 3. Independent Mechanical Verification & Gate 2 Status

- Executed `@check-1`'s independent exact-arithmetic verifier (zero floats):
  - Command: `.venv/bin/python targets/godard-2605.21866-prob3/notes/check-check-1.py`
  - Raw output (exit code `0`): `PASS` (all 4 suites passed: Section 1 disconnections, Section 2 even-$n$ bounds & BFS, Section 3 Kummer–Weil & BFS, Section 4 Lemma 4.1, $\tau_i$, Lemma 4.3 Jacobian rank growth to $n$ at $k_0$, and BFS).
- Gate 2 novelty receipts from all three watchers (`watch-1` `#247`, `watch-5` `#254`, `watch-6` `#251`) are clear.

---

## 4. Verdict

**PASS.** Ready for Gate 3 novelty verification (`<1h`).

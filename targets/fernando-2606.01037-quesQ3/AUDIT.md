# Blind Audit: `targets/fernando-2606.01037-quesQ3/` (`@audit-1`)

**Verdict:** **PASS (re-audit after `#1803` fixes)**
**Target:** Neranga Fernando & Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, `arXiv:2606.01037v1` (31 May 2026), Section 6 (`draftMay31.tex`, lines 911–915, `\label{Q3}`, **Question 6.3**).
**Answer Verified:** For even $q = 2^m > 2$ ($m \ge 2$), even $e > 0$, and $n = 1 + (q - 1)q^{e/2} + (q - 1)q^e$, the polynomial $g_{n,q} = S_{e/2 + 1}^{q^{e/2}} + S_e + S_e (S_{e/2}^{q^{e/2}})^{q-1}$ is a permutation polynomial (PP) of $\mathbb{F}_{q^e}$ **if and only if** $q = 4$ and $4 \mid e$.
**Audited artifacts (blind):** Primary source `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex` (confirmed `v1` is the sole latest live arXiv version at `https://arxiv.org/abs/2606.01037`), `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, and `notes/check-check-1.py`. (Author `verify.py` and author `notes/` were strictly unread.)

---

## 1. Primary-Source Statement Fidelity & Compiled Numbering

Verified verbatim against `tools/.arxiv_cache/eprint/2606.01037v1/draftMay31.tex`:
- **Question 6.3** (`\label{Q3}`, L911–915, third numbered environment in Section 6):
  *"Let $q>2$ be even, $n=1\cdot q^0+(q-1)\cdot q^{e/2}+(q-1)\cdot q^e$, and $e>0$ be even. Then $g_{1\cdot q^0+(q-1)\cdot q^{e/2}+(q-1)\cdot q^e}=S_{e/2+1}^{q^{e/2}}+S_e+S_e\,(S_{e/2}^{q^{e/2}})^{q-1}$. Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}.$"*
- Auxiliary references verified: Section 2 L119 ($S_k$, $S_0 = 0$, $\mathrm{Tr}_{q^e/q} = S_e$), Lemma 2.4 (`\label{L310}`, L148–151), Eq. `(1.1)` (`\label{AB1}`, L74–76), Eq. `(1.2)` (`\label{AB2}`, L78–80), Appendix Table 1 `(817, 4; 4)` (L1077).
- Both `TARGET.md` and `PROOF.md` match Question 6.3 verbatim.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

**Every step across Sections 1–5 (including all `#1803` patches) is SOUND and complete:**

- **Section 1 (Lemma 1.1, Prop. 1.2, Lemma 1.3):**
  - $\mathrm{im}(S_k) = \{z \in \mathbb{F}_{q^{2k}} : t(z) := z + z^{q^k} \in \mathbb{F}_q\}$ has size $q^{k+1}$; $x \mapsto z := S_k(x)^{q^k}$ with explicit inverse $x = b + z + t(z) + t(z)z^{q-1}$ establishes a fiber bijection between $g_{n,q}$ on $\mathbb{F}_{q^{2k}}$ and the $\mathbb{F}_q$-homogeneous map $\Phi_{\mathrm{Q3}}(z) = z + (k+1)t(z) + S_k(z) + t(z)S_k(z^{q-1})$ on $\mathrm{im}(S_k)$; when $k$ is even, $\Phi_{\mathrm{Q3}}|_{\mathbb{F}_{q^k}}(z) = z + \mathrm{Tr}_{q^k/q}(z)$ is an involution.
- **Section 2 ($e \equiv 2 \pmod 4$, $k$ odd $\implies$ never PP, Theorem 2.1):**
  - $S_{2k}(1) = S_{k+1}(1) = 0$ gives $g_{n,q}(1) = 0 = g_{n,q}(0)$ directly.
- **Section 3 ($q = 4$, $4 \mid e$, $k \ge 2$ even $\implies$ always PP, Theorem 3.1):**
  - Step 1: $s(z) \in t(z)\{\omega, \omega^2\}$ separates $\mathrm{im}(S_k) \setminus \mathbb{F}_{4^k}$ from $\mathbb{F}_{4^k}$.
  - Step 2: Quartic invariant $\Phi_{\mathrm{Q3}}(z)^4 + \Phi_{\mathrm{Q3}}(z) = (z^2 + tz)^2$ for all $t = t(z) \in \mathbb{F}_4^*$.
  - Step 3: Injectivity for $t_1 = t_2$ via $\Phi_{\mathrm{Q3}}(z_1^{4^k}) = \Phi_{\mathrm{Q3}}(z_1) + s \neq \Phi_{\mathrm{Q3}}(z_1)$, and for $t_1 \neq t_2$ via normalization $(1, \omega, \omega^2)$, $W = \omega^2 z_1 + \omega z_2 \in \mathbb{F}_{4^k}$, $W = \omega^2 Q(A)$, and the contradiction $Q(A)^2 + Q(A) + \omega^2 A = 0$ vs. $1$ (every algebraic coefficient checked by hand).
- **Section 4 ($q \ge 8$, $4 \mid e$, $e \ge 8$, $k \ge 4$ even $\implies$ never PP, Theorem 4.1):**
  - For $z = u + \alpha$ ($\alpha^{q^k} = \alpha + 1$), $f(u) = (u + \alpha)^{q-1} + (u + \alpha + 1)^{q-1} \in \mathbb{F}_{q^k}[u]$ has $u^{q-2}, u^{q-3}$ coefficients $1$; $h_\lambda(u) = \lambda f(u) + (\mu u^{q/2 - 1})^2 + \mu u^{q/2 - 1}$ ($\mu^2 = \lambda$) has exact odd degree $q - 3 \ge 5$ (since $q/2 - 1 < q - 3$ for $q \ge 8$) and identical $\mathrm{Tr}_{q^k/2}$. Lidl–Niederreiter Theorem 5.38 gives $N_0 \ge q(5q - 4) > 0$, colliding with $\Phi_{\mathrm{Q3}}|_{\mathbb{F}_{q^k}}$.
- **Section 5 ($e = 4$, $q = 2^m \ge 8 \implies$ never PP, Prop. 5.1, Lemmas 5.2–5.4, Theorem 5.5):**
  - **Prop. 5.1:** Bijection $\tilde{\Phi}(z) = \Phi(z)/s(z)$ on $A_1$ descends via $\pi(z) = z^2 + z$ to a bijection $\Psi(w) = N(w)/s(z)^2$ on $H_1$, where the 6-piece expansion confirms $\Phi(z)\Phi(z+1) = N(w) = w^q + S(w) + (w+1)/w^q$. Raising to $3(q - 1)$ cancels $s(z)$ and yields $\sum_{w \in H_1} N(w)^{3(q-1)} = \sum_{w \in H_1} w^{3(q-1)} = 0$ via the corrected exact bound $3q - 3 + q^2/2 = (q^2 - 1) - (q^2 - 6q + 4)/2 < q^2 - 1$ (L189–190, verified).
  - **Lemmas 5.2, 5.3, 5.4:** Support/weight/upper-triangular unique-matching criterion for $L(w)^A$, disjoint-subtraction popcount bounds, and exact solutions of $a + 2c = S$ ($a \& c = 0$, $4 \mid c$) all verified line by line.
  - **Theorem 5.5 (§5.3–5.5):**
    - Exact $M_{1,\mathrm{rem}}$ identity in $\mathcal{R} = \mathbb{F}_2[w]/(w^{q^2 - 1} - 1)$ and four-piece split verified.
    - Patched direct bounds for $\lambda \le -1$ ($N \le -2q < 0$), $\lambda \ge 2$ ($N \ge a q + (2q - 1)c + \frac{5q}{2} + a - 4 > A q/2$, L267–273), Type IV-A $\lambda = 1$ ($N \ge a q + (2q - 1)c + q/2 + a + 1 > a q/2$, L288–290), and Type III-A $\lambda = 1$ ($N \ge a q + (2q - 1)c + \frac{5q}{2} + a - 3 > a q/2$, L371–373) eliminate all borrow casework and are 100% exact.
    - Patched Piece I $\lambda = 0$ (L326) explicitly verifies $2^t - 1 = c - b \le q - 3 < q - 1 \implies 2 \le t \le m - 1$ before applying Lemma 5.4(3)–(4).
    - Every remaining branch across Pieces IV, I, II, III and final parity sum $(m - 1) + (1 + \binom{m-2}{2}) + \binom{m-3}{2} + 0 = m^2 - 5m + 9 \equiv m(m - 1) + 1 \equiv 1 \pmod 2$ verified line by line.

---

## 3. Exact Computational Verification

- **Independent checker (`notes/check-check-1.py`):**
  - AST audit confirmed zero floating-point literals, zero `float()` calls, and zero `/` operators (`FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: []`).
  - Executed `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py`: exited `0`, raw output `PASS` (verified Waring Eq. 2 & Eq. 1 against Q6.3, exhaustive PP tests up to $N = 16$, Section 1 & Theorem 3.1 identities for $(4, 4), (4, 8)$, Section 4 Carlitz–Uchiyama $N_0 = 576 \ge 288$ at $(8, 8)$, Lemmas 5.2–5.4, direct moment $m \in \{2, 3, 4, 5\}$, and exact 4-piece parities for $m \in \{3, 4, 5\}$).
- **Auditor's independent adversarial checks:**
  - Exhaustive per-subcase hit-set verifier across ALL subcases of Pieces IV, I, II, III for $m \in \{3, 4, 5, 6\}$: **100% exact tuple-for-tuple match** with `PROOF.md` §5.4 (`m=3: (I:2, II:3, III:2, IV:0)`, `m=4: (7, 8, 4, 0)`, `m=5: (14, 18, 9, 0)`, `m=6: (23, 35, 19, 0)`).
  - Direct exact finite-field evaluation of $\sum_{w \in H_1} N(w)^{3(q-1)} = 1$ in $\mathbb{F}_{2^{2m}}$ for $m \in \{6, 7, 8\}$ (up to $|H_1| = 32{,}768$): all confirmed $= 1$.

---

## 4. Handoff

- **Result Label:** `written proof, internally audited`
- **Verification Command:** `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py`
- **Files:** `targets/fernando-2606.01037-quesQ3/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`
- Handing off directly to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness (`< 1h`) and subsequent `@coordinator` reporting.

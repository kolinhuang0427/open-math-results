# Independent Adversarial Audit: `targets/saikia-2611.28840-conj8.1/`

- **Auditor:** `@audit-1`
- **Target:** Manjil P. Saikia, *Congruences modulo powers of 2 and 3 for Lin's function $\mathrm{PDO}_t(n)$*, `arXiv:2611.28840v1` (confirmed sole version live on `arxiv.org/abs/2611.28840` as of 2026-11-27), Section 8 Conjecture 8.1 (`\label{conj:sharp}`, `final.tex` L931–941) & `\eqref{eq:sharp}` best-possible sharpness.
- **Candidate Artifacts Inspected (blind):** Primary source `tools/.arxiv_cache/eprint/2611.28840v1/final.tex`, `TARGET.md`, `PROOF.md`, `notes/check-check-3.py`, `notes/check-check-3.md`.
- **Verdict:** **PASS** (verification label: `"written proof, internally audited"`).

---

## 1. Primary-Source Fidelity & Compiled Numbering — PASS

Verified verbatim against `tools/.arxiv_cache/eprint/2611.28840v1/final.tex`:
- **Conjecture 8.1 (`\label{conj:sharp}`, §8, L938–940):** For any $k \ge 3$, there exists an odd integer $\lambda_k$ such that for any $n \ge 0$,
  $$\mathrm{PDO}_{\mathrm{t}}(3 \times 2^{k+2} n) \equiv 8\lambda_k\,\mathrm{PDO}_{\mathrm{t}}(3 \times 2^k n) \pmod{2^{\lfloor 7(k+1)/2 \rfloor}} \qquad (\text{\texttt{eq:sharp}}, \text{ L932--934}).$$
- **Best-possible sharpness (L935):** `PROOF.md` additionally proves that for **every** $k \ge 3$, no integer $\lambda'_k$ satisfies `\eqref{eq:sharp}` modulo $2^{\lfloor 7(k+1)/2 \rfloor + 1}$ for all $n \ge 0$ (every integer fails at some $n \in \{1, 2, 3\}$).
- **All auxiliary references verified verbatim:** Section 1 eq. `(1.1)` (`eq:gf`, L79), Section 3 `(P1)`–`(P2)` / `eq:A1`–`eq:A3` (L441–450), Section 4 **Theorem 4.1** (`thm:gf`, `eq:gfm`, `eq:x1`, `eq:xrec`, L490–503), Section 5 **Lemma 5.1** (`lem:valPhi`, L558–580) and **Lemma 5.2** (`lem:refined`, `eq:odd`, `eq:even`, L590–641). Edge case $n = 0$ holds trivially since $\mathrm{PDO}_{\mathrm{t}}(0) = 0$.

---

## 2. Step-by-Step Mathematical Audit — PASS

1. **Step 1 — Lemma 1 (`PROOF.md` L38–60):** Support bounds $\lfloor (i+3)/4 \rfloor \le j \le 4i + 3$ and valuation bound $\nu_2(B_{i,j}) \ge 2j - \lfloor i/2 \rfloor$ follow cleanly from $\lfloor (i+1)/2 \rfloor + \lfloor i/2 \rfloor = i$ and Saikia's Lemma 5.1; all explicit entries/valuations in Lemma 1(3) verified exactly.
2. **Step 2 — Banach Algebra $\mathcal{B}_2(K), \mathcal{E}_2(K), \mathcal{R}_2(K)$, Lemma 2 & Theorem 3 (L64–161):**
   - Completeness and submultiplicativity of $\mathcal{B}_2(K) = K\langle X/2 \rangle$, $\mathcal{E}_2(K) = X\mathcal{B}_2(K)$, and $\mathcal{R}_2(K) = \mathcal{B}_2(K)[\zeta]/(\zeta^2 - 6X\zeta - X)$ ($\|X\| = 2, \|6X\| = 1, \|\zeta\| = \sqrt{2}, \|\xi\| = \sqrt{2} < 2$), boundedness $\|A\| \le 1/2$, unit $(1+6\zeta)^{-1} = 1 + 36X - 6\zeta$, and continuity of $\frac{1}{2}\mathrm{Tr}$ and $\tilde{A}$ all verified line-by-line.
   - **Lemma 2:** Density of $X K[X]$ in $\mathcal{E}_2(K)$, modular equation `(8)`, base cases $i = 1, 2$, and recurrence `(3)` establish $(1+8X)(1+9X)(\mathbf{u}A) = \tilde{A}((1+8t)(1+9t)\mathbf{u})$ on all of $\mathcal{E}_2(K)$.
   - **Theorem 3 ($W^2 = I$ and $W A = -A W$):** Checked $\|h\|_{\mathcal{B}_2} = 2$ (confirming the explicit power series `(9)`), Möbius identities `(12)`–`(16)`, exact minus sign in `(16)`, agreement of Banach-algebra evaluation $G(\xi) \in \mathcal{R}_2(K)$ with rational evaluation in $\mathrm{Frac}(\mathcal{R}_2(K))$ (via continuity of $\mathrm{ev}_\xi$ and invertibility of $1 + 8\xi = (1+4\zeta)^2$ in $\mathcal{R}_2(K)$), density of $K[X]$ in $\mathcal{B}_2(K)$, and conjugation `(17)` transferring $W_3 \tilde{A} = -\tilde{A} W_3$ to $W A = -A W$ on $\mathcal{E}_2(K)$ by integral-domain cancellation of $(1+8X)(1+9X)$. **Airtight.**
3. **Step 3 — Lemmas 4–6 & Theorem 7 (`(\mathbf{u}_2 B)_1 = 0`, L164–245):**
   - **Lemma 4:** Completeness of $S(K)$, $\nu_2(\Lambda(\mathbf{w})) = 3$, $\nu_2(\Lambda(\mathbf{w}') - \Lambda(\mathbf{w})) \ge 8 + \Delta$, bound `(18)` $\nu_2(w_k B_{k,j}) \ge 2j + \lceil 3k/2 \rceil - 3 \ge 2j + 2$, strict $2^2$-contraction on $S(K)$, and unique fixed point $\mathbf{u}_2 \in S(\mathbb{Q}_2) \subseteq S(K)$ with $\Lambda \in 8\mathbb{Z}_2^\times$ and $\nu_2(u_{2,j}) \ge 2j - 2$ ($j \ge 4$) all verified.
   - **Lemma 5:** $\|B_{YY}\| \le 2^{-5}$ on $Y(K)$, Schur-complement isomorphism $\ker_{\mathcal{E}_2(K)}(B - zI) \cong \ker_{K^2}(S(z))$ for $|z|_2 > 2^{-5}$, norm bounds $(\alpha_1, \alpha_2) = (4, 3)$ and $(\beta_1, \beta_2) = (4, 7)$, and every pair $(a, b)$ contributing to $c_n$ in $g(t) = \det M(t)$ checked directly (`c_0 = 1`, `c_1 = -45454`, `c_2` odd, `nu_2(c_n) >= 2n - 4 >= 2` for $n \ge 3$).
   - **Lemma 6:** Self-contained Euclidean division in $T = \mathbb{Z}_2\langle t \rangle$ and quadratically convergent Hensel–Weierstrass iteration ($g v_{k+1} = P_{k+1} + E_{k+1}$, $\|E_{k+1}\|_T \le \|E_k\|_T^2$) produce $g v = P$ with $|t_0|_2 = 1$, $v(t_0) \ne 0$, hence $z_0 = 8/t_0 \in \overline{\mathbb{Q}}_2$ ($[K:\mathbb{Q}_2] \le 2$) with $|z_0|_2 = 2^{-3}$ and $\det S(z_0) = 0$.
   - **Theorem 7:** Anti-commutation $W A = -A W$ splits $V = \ker_{\mathcal{E}_2(K)}(B - z_0 I) = V_+ \oplus V_-$ with $A \colon V_+ \xrightarrow{\sim} V_-$ ($z_0 \ne 0$), forcing $\dim_K V$ even; since $1 \le \dim_K V \le 2$, $\dim_K V = 2$ and $S(z_0) = 0$. Then $\mathbf{w}_2 = (0, 1, e_2 B_{0Y}(z_0 I - B_{YY})^{-1})$ lies in $S(K)$ (since $z_0^{-1} e_2 B_{0Y} \in S_0(K)$ and $z_0^{-1} B_{YY}(S_0(K)) \subseteq 2^2 S_0(K)$ with $S_0(K)$ closed in $Y(K)$), hence is a fixed point of $\Phi$ in $S(K)$, forcing $\mathbf{w}_2 = \mathbf{u}_2$, $z_0 = \Lambda \in 8\mathbb{Z}_2^\times$, and $(\mathbf{u}_2 B)_1 = 0$. **Airtight.**
4. **Step 4 — Lemma 8 (L247–276):**
   - $\mathbf{u}_1 = \mathbf{u}_2(A + 16I)$ satisfies $u_{1,1} = 1, u_{1,2} = 0$, $\mathbf{u}_1 B = \Lambda \mathbf{u}_1$; all valuations in Lemma 8(2) verified (including $\Phi_{3,7} = 72 \Phi_{2,5} = 2^{12} \cdot 3^8$ and $j = 5$ uniqueness of $\nu_2(\Phi_{2,5}) = 9 < 10$).
   - Contraction `(21)` $\nu_2(M(e_k)_j) \ge 7 + 2j - 2k$ ($k, j \ge 3$) checked analytically across all three infinite regimes ($k \ge 9$; $5 \le k \le 8$; $k \in \{3, 4\}, j \ge 20$) and rigorously on the 34-entry finite box ($k \in \{3, 4\}, 3 \le j \le 19$) + low entries ($5 \le k \le 8, j \in \{3, 4\}$) using the exact error bound $\nu_2(u_{2,j}^{(N)} - u_{2,j}) \ge 2j - 3 + 2N$ and $\nu_2(u_{1,j}^{(N)} - u_{1,j}) \ge 2j + 2N$.
5. **Step 5 — Propositions 9 & 10, Congruence & Sharpness (L279–366):**
   - Every term in both odd ($m = 2\mu + 1, k = 2\mu + 3$, target $7\mu + 14$) and even ($m = 2\mu + 2, k = 2\mu + 4$, target $7\mu + 17$) inductions verified by hand: exact cancellation $26(3\cdot 2^{7\mu+11}) + 2^{7\mu+12} = 40\cdot 2^{7\mu+12} \equiv 0 \pmod{2^{7\mu+14}}$ in odd $d_1$, exact valuation $\nu_2(\tilde{d}_3) = \lfloor 7(k+1)/2 \rfloor$ in both parities, and complete sharpness deduction at $n \in \{1, 2, 3\}$ for arbitrary integer $\lambda'_k$. **Airtight.**

---

## 3. Independent Mechanical Verification & Adversarial Stress Test — PASS

- **AST & exactness audit of `notes/check-check-3.py`:** `FLOATS: []`, `FLOAT_CALLS: []`, `DIVS: []` (pure integer / `Fraction` arithmetic, zero floats, zero `/` operators).
- **Execution:** `.venv/bin/python -u targets/saikia-2611.28840-conj8.1/notes/check-check-3.py` exited `0`, raw output:
  - `Part 1 (Lemma 5.1 & Lemma 1 support, bounds, low entries of B): OK`
  - `Part 2 (direct q-series PDO_t(n) up to q^4650, Thm 4.1 m=1..5, eq:sharp & sharpness k=3..7): OK`
  - `Part 3 (Lemma 2, Theorem 3 algebraic identities (8),(12)-(17) & 2-adic W A = -A W): OK`
  - `Part 4 (Lemma 5(3) exact Schur complement M(t) & det g(t) up to t^5): OK`
  - `Part 5 (Phi^28 contraction, Thm 7 (u_2 B)_1==0 mod 2^56, Lemma 8, Props 9-10, k=3..25 congruence & sharpness): OK`
  - `PASS`
- **Auditor's independent higher-precision check (`MAX_J = 42`, `N = 32`, mod $2^{150}$):** Independently confirmed `(u_2 B)_1 == 0 mod 2^64`, exact zero-margin set `[(3, 3), (3, 6), (3, 7), (3, 8), (4, 4), (4, 6)]` and `max_val_in_box == 49` matching `PROOF.md` L275 verbatim, plus exact base cases `pi1[3]/2^11 == 3 (mod 8)`, `pi1[4]/2^12 == 5 (mod 8)`, `v2(pi1[5]) == 16`, and `v2(pi2[3..9]) == [14, 16, 26, 25, 22, 24, 27]` (`[ADVERSARIAL PASS]`).

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (`"written proof, internally audited"`).
- Gate 2 novelty (`#1651`, `#1652`, `#1654`) and `#1658`/`#1659` competing-repo cross-checks are clear. Ready for Gate 3 freshness (`<1h`) and Coordinator reporting.

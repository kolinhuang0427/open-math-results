# Blind Audit: `targets/awan-2611.07303-q2/` (`@audit-1`)

**Verdict:** **PASS (re-audit after `#1861`/`#1863` fixes)**
**Target:** Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, *Gaps in the Most Frequent Sizes of Integer Sumsets*, `arXiv:2611.07303v2` (9 Nov 2026), Section 5 (*Additional Results and Future Work*), Subsection 5.2 (*Questions*), **Question 2** (`\label{q:rate}`, `sections/additional-results.tex` lines 556–578).
**Answer Verified:**
1. **Convergence for every $k \ge 4$ (and $k = 3$):** **YES** — $c_{h,k} = \lim_{q\to\infty} f_{h,k}(q)$ exists for all fixed $h \ge 2, k \ge 3$.
2. **Normalized $(k-1)$-dimensional volume formula:** **YES** — $c_{h,k} = k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2} = k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(\pi_m(P_{\mathbf{d}}))}{|d_m|}$ (recovering $c_{h,3} = 3\sum_{w=2}^h \varphi(w)/w$ and $c_{2,4} = 8$ term by term).
3. **Eventual monotonicity in $q$:** **NO** — disproved explicitly for $(3, 3)$ ($f_{3,3}(6m+1) > f_{3,3}(6m)$ and $f_{3,3}(6m+2) < f_{3,3}(6m+1)$ for all $m \ge 1$) and $(2, 4)$ (strict step-by-step alternation for all $q \ge 70$).

**Audited artifacts (blind):** Primary source `tools/.arxiv_cache/eprint/2611.07303.src` (confirmed `v2` is the sole latest live arXiv version via `arxiv_fetch.py query --id-list 2611.07303`), `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, and `notes/check-check-1.py`. (Author `verify.py` and author `notes/` were strictly unread.)

---

## 1. Primary-Source Statement Fidelity & Compiled Numbering

Verified verbatim against `tools/.arxiv_cache/eprint/2611.07303.src`:
- `preamble.tex` declares `\newtheorem{theorem}{Theorem}[section]` with `corollary`, `lemma`, `proposition`, `definition`, `example`, and `remark` sharing the `theorem` counter, and `\newtheorem{question}{Question}` un-sectioned.
- Compiled labels verified and matched across `TARGET.md`, `PROOF.md`, and `notes/check-check-1.{md,py}`:
  - **Definition 3.1** (`def:coefficient-vectors`), **Lemma 3.2** (`lem:equal-sum-criterion`), **Example 3.3** (`ex:E-relation`), **Lemma 3.4** (`lem:rank-lemma`), **Proposition 3.5** (`prop:coefficient-vectors-lemma`).
  - **Corollary 5.1** (`cor:proportion`), **Remark 5.2** (`rem:k3-limit`), **Question 2** (`q:rate`, `sections/additional-results.tex` L556–578 — quoted verbatim in `TARGET.md` L21–42).
- All `#1856` remediation items verified in place (`PROOF.md` L38, L67, L91 and `notes/check-check-1.{md,py}`).

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

- **Section 1 (Convergence & normalized volume formula, L30–98):**
  - Bonferroni inequalities with Lemma 3.2, Proposition 3.5 (pairwise linear independence), and Lemma 3.4 bound pairwise intersections by $\binom{|\mathcal{R}_{h,k}|}{2} q^{k-2}$.
  - Case 1 ($w(\mathbf{d}) = 1$): $E_{\mathbf{d}}(q) = P_{\mathbf{d}} = \varnothing$.
  - Case 2 ($w(\mathbf{d}) \ge 2$): Primitive $\mathbf{d}$ yields $\mathbf{u} \in \mathbb{Z}^k$ with $\mathbf{d}\cdot\mathbf{u} = 1$, giving unimodular matrix $M = [\mathbf{b}_1 \mid \dots \mid \mathbf{b}_{k-1} \mid \mathbf{u}]$ ($|\det M| = 1$) and exact lattice covolume $\operatorname{covol}(\Lambda_{\mathbf{d}}) = \|\mathbf{d}\|_2$.
  - Patched L67 cleanly notes that $(\Lambda_{\mathbf{d}} \cap q K_{\mathbf{d}}) \setminus E_{\mathbf{d}}(q)$ consists of points in $\Lambda_{\mathbf{d}} \cap [0, q]^k$ with $a_1 = 0$ or $a_i = a_{i+1}$ ($1 \le i \le k - 1$; $a_k = q$ is allowed in $E_{\mathbf{d}}(q)$), each bounded by $(q + 1)^{k-2}$ via the rank-$2$ argument of Lemma 3.4 on $[0, q]^k$.
  - Cube-tiling error bound $|\#(\mathbb{Z}^{k-1} \cap q Q_{\mathbf{d}}) - \operatorname{vol}_{k-1}(Q_{\mathbf{d}}) q^{k-1}| \le \#\{\mathbf{z} : C_{\mathbf{z}, q} \cap \partial Q_{\mathbf{d}} \neq \varnothing\} = O_{\mathbf{d}}(q^{k-2})$ via the $k + 1$ bounding hyperplane slices is completely rigorous.
  - Coordinate projection Gram determinant $\det(I_{k-1} + \frac{1}{d_m^2}\mathbf{d}'(\mathbf{d}')^T) = \|\mathbf{d}\|_2^2 / d_m^2$ yields $\operatorname{vol}_{k-1}(P_{\mathbf{d}})/\|\mathbf{d}\|_2 = \operatorname{vol}_{k-1}(\pi_m(P_{\mathbf{d}}))/|d_m|$, recovering $c_{h,3} = 3\sum_{w=2}^h \varphi(w)/w$ and $c_{2,4} = 8$ term by term.
- **Section 2 (Disproof of eventual monotonicity, L101–176):**
  - **§2.1 (`(3, 3)`):** Exact pairwise-disjoint count and rational simplifications at $q = 6m, 6m+1, 6m+2$ give $f_{3,3}(6m+1) - f_{3,3}(6m) = \frac{2}{(3m-1)(6m-1)} > 0$ and $f_{3,3}(6m+2) - f_{3,3}(6m+1) = -\frac{3}{(6m-1)(6m+1)} < 0$ for every $m \ge 1$.
  - **§2.2 (`(2, 4)`):** Exact enumeration of $R_1, \dots, R_5$ and all 10 pairwise intersections on $0 < x < y < D$ yields $\operatorname{cnt}(D)$, second-difference recurrence $B(q+1) - 2B(q) + B(q-1) = \operatorname{cnt}(q)$, exact period-$12$ quasipolynomial $P_{2,4}(q)$, and all $12$ residue-class quadratics $N_q$ proving $f_{2,4}(q+1) > f_{2,4}(q)$ for all even $q \ge 6$ and $f_{2,4}(q+1) < f_{2,4}(q)$ for all odd $q \ge 71$.

---

## 3. Exact Computational Verification

- **Independent checker (`notes/check-check-1.py`):**
  - AST audit confirmed zero floating-point literals or `float()` calls (`FLOATS: []`, `FLOAT_CALLS: []`; the two `/` operators at L57 and L110 are exact `Fraction` divisions).
  - Executed `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py`: exited `0`, raw output `PASS`.
- **Auditor's independent symbolic polynomial verification:**
  - Symbolically verified the exact polynomial recurrence $P_{2,4}(q+1) - 2P_{2,4}(q) + P_{2,4}(q-1) = \operatorname{cnt}(q)$ and all $12$ residue-class quadratics $N_q = 24((q-3)P_{2,4}(q+1) - q P_{2,4}(q))$ as exact polynomial identities over $\mathbb{Q}[q]$ in every residue class $q \bmod 12$ (proving the exact formula and sign alternation for **all** $q \ge 70$).

---

## 4. Handoff

- **Result Label:** `written proof, internally audited`
- **Verification Command:** `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py`
- **Files:** `targets/awan-2611.07303-q2/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`
- Handing off directly to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness (`< 1h`) and subsequent `@coordinator` reporting.

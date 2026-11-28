# Independent Check Report: `targets/awan-2611.07303-q2`

- **Verdict:** **PASS** (after owner remediation of `PROOF.md` L38, L67, and L91)
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/awan-2611.07303-q2/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source & Remediation Check
- **Source:** `tools/.arxiv_cache/eprint/2611.07303.src` (Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, *Gaps in the Most Frequent Sizes of Integer Sumsets*, `arXiv:2611.07303v2`, `sections/additional-results.tex`, Section 5, Subsection 5.2, Question 2 `\label{q:rate}`, lines 556–578; definitions from `sections/preliminary-lemmas.tex` lines 5–222 and `sections/additional-results.tex` lines 16–108).
- Confirmed `TARGET.md` reproduces Question 2 (`\label{q:rate}`), $\mathcal{B}_{h,k}(q)$, and $\mathcal{R}_{h,k}$ verbatim.
- Confirmed `@scout-10` patched all `#1856` items in `PROOF.md`:
  - L38 & L67: `Lemma 3.4` (`lem:rank-lemma`) and `Proposition 3.5` (`prop:coefficient-vectors-lemma`) match compiled numbering after `Example 3.3` (`ex:E-relation`).
  - L67: dropped redundant $a_k = q$ exclusion and cited the rank-2 argument of Lemma 3.4 on $[0, q]^k$ giving $(q+1)^{k-2}$.
  - L91: clarified "five vectors in $\mathcal{R}_{2,4}$ with $P_{\mathbf{d}} \neq \varnothing$".
- Verified the mathematical proofs in `PROOF.md`:
  - **Convergence & volume formula:** Bonferroni + pairwise linear independence (Lemma 3.4 + Prop 3.5), $\mathbb{Z}$-basis covolume $\operatorname{covol}(\Lambda_{\mathbf{d}}) = \|\mathbf{d}\|_2$, boundary hyperplane slicing ($O_{\mathbf{d}}(q^{k-2})$), and coordinate projection Jacobian $\sqrt{\det(I + \mathbf{d}'(\mathbf{d}')^T/d_m^2)} = \|\mathbf{d}\|_2/|d_m|$ yield $c_{h,k} = k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2} = k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(\pi_m(P_{\mathbf{d}}))}{|d_m|}$.
  - **Non-monotonicity:** Exact closed forms for $(h,k) = (3,3)$ at $q = 6m, 6m+1, 6m+2$ ($m \ge 1$) and exact period-$12$ quasipolynomial $P_{2,4}(q)$ for $(h,k) = (2,4)$ proving strict step-by-step alternation for all $q \ge 70$.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Section 1 & volumes:** Verified Lemma 3.2 directly against exhaustive $\binom{[q]}{k}$ $B_h$-checks for $(3,3,10)$, $(2,4,9)$, $(2,5,8)$, exact Gram determinant identity $\det(I + \mathbf{d}'(\mathbf{d}')^T/d_m^2) = \|\mathbf{d}\|_2^2/d_m^2$, exact $k=3$ sum recovering $3\sum_{w=2}^h \varphi(w)/w$ ($2 \le h \le 6$), and exact 5-vector $\mathcal{R}_{2,4}$ volume sum $24(\frac{1}{12} + \frac{1}{12} + \frac{1}{24} + \frac{1}{24} + \frac{1}{12}) = 8$.
2. **Section 2.1 (`(3, 3)`):** Verified exact non-$B_3$ counts against brute force for $3 \le q \le 26$ and exact closed forms/oscillations $f_{3,3}(6m+1) - f_{3,3}(6m) > 0 > f_{3,3}(6m+2) - f_{3,3}(6m+1)$ for $1 \le m \le 500$.
3. **Section 2.2 (`(2, 4)`):** Verified $\operatorname{cnt}(D)$ ($1 \le D \le 100$), brute-force $B(q) = P_{2,4}(q)$ ($4 \le q \le 26$), second-difference recurrence ($2 \le q < 200$), all $12$ residue-class quadratics $N_q$, and strict alternation for $6 \le q \le 500$ ($N_q > 0$ even $q \ge 6$; $N_q < 0$ odd $q \ge 71$).

## 3. Gate 2 Novelty Status
- Passed by `watch-5` (`#1849`), `watch-6` (`#1850`), and `watch-1` (`#1851`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).

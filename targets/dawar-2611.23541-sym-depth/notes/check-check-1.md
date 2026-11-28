# Independent Check Report: `targets/dawar-2611.23541-sym-depth`

- **Verdict:** **PASS** (after `#1972` / `#1974` remediation of `PROOF.md` Lemma 1, Lemma 2, and Theorems 2–4)
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/dawar-2611.23541-sym-depth/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source & Remediation Check
- **Source:** `tools/.arxiv_cache/eprint/2611.23541.src` (Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *Depth Hierarchies for Symmetric Algebraic Circuits*, `arXiv:2611.23541v1`, `introduction.tex` Section 1.2 "Future work", lines 269–271).
- Confirmed `TARGET.md` reproduces the open question verbatim, and verified all referenced lemmas/conventions in `prelims.tex` (notably unweighted `+`/`\times` gates at L7), `app-vsbr.tex`, `app-reduced-circuits-supports.tex`, and `app-circuits-from-patterns.tex`.
- Confirmed `@scout-9` cleanly patched every `#1972` item in `PROOF.md`:
  - **Lemma 1 & Theorem 2:** Fixed `(v\ w)(w\ w') = (v\ w\ w')` at L31; set $n \ge 28$, homogeneous degree $\le d$, and added explicit equivariant collapse of adjacent same-type gates ($\Sigma \to \Sigma, \Pi \to \Pi$).
  - **Lemma 2:** Fixed non-square ceiling bounds ($|\beta'(c_K)| \le 2(w+1)\lceil \sqrt{d} \rceil$, $1 \le |\mathrm{rep}^{-1}(c_K)| \le 2\lceil \sqrt{d} \rceil$), added $S = \emptyset$ depth-1 case ($W \le 2r$), deleted empty root $r_0$ before binarization, proved fixed-root disjoint-subtree bound $|S| \le 3\sqrt{d}$, and enforced `lem:normalised-decomposition` Items 2–3 pruning.
  - **Theorem 3:** Fixed $\kappa \le \min\{n^{1-\varepsilon}, \frac{\log\max\{s(n), n^2\}}{\varepsilon\log n}\} + 1$, restricted full homogeneity to homogeneous $p_n$, absorbed $\alpha_F$ into Layer-2 $\Pi$-gates for `prelims.tex` unweighted `+`-gates, and verified $2\kappa\lceil\sqrt{d}\rceil \le 4\kappa\sqrt{d} < 6\kappa\sqrt{d}$.
  - **Theorem 4:** Explicitly separated standard weighted $\Sigma\Pi\Sigma$ depth-3 (`[KKS16, Tavenas15]`) from unweighted `prelims.tex` L7 depth-4 (fan-in-2 scalar-multiplication bottom $\times$-gates), justified $\alpha_F \in \mathbb{Q}$ via $\mathbb{Q}$-linear projection $\tau : \mathbb{K} \to \mathbb{Q}$, handled $a = 0$, $1 \le b_j \le b$, $R_j \le n^{2(\kappa-1)\lceil\sqrt{d}\rceil}$, and synced Summary L10 with Theorem 4 L75–76.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/dawar-2611.23541-sym-depth/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Theorems 1–2 & Lemma 1:** Verified $\min\{d, n/2\} \ge 3^\Delta$ and Theorem 2 ($n \ge 28$) parameter bounds across ranges, and verified by exact finite-group closure that $\langle A_U, (v\ w_2\ w_1)\rangle = A_{U \cup \{v\}}$ and $\langle A_{U \cup \{v\}}, S_U \rangle = S_{U \cup \{v\}}$ ($|U| = 5$).
2. **Lemma 2 (incl. non-squares & normalised pruning):** Directly ran the greedy deepest-heavy-subtree 2-level tree decomposition + $S = \emptyset$ depth-1 handling + `lem:normalised-decomposition` Items 2–3 pruning across $d \in \{1, 2, 3, 5, 10, 16, 17, 35, 36, 64, 65, 100\}$, confirming all ceiling separator, bag-size, leaf-count, edge-count, and normalisation invariants.
3. **Theorem 3:** Evaluated the 4-layer ($\Sigma\Pi\Sigma\Pi$) depth-4 circuit for $P_4$ and $P_5$ ($n=4$) over $\mathbb{Q}$, confirming exact equality with $\hom_{F, n}$ and $\Gamma_n$-invariance.
4. **Theorem 4:** Verified Fischer's identity ($b \in \{2, 3, 4\}$), truncated-exponential $[z^a] H(z, X) \cdot a! = P(X)^a$ via Lagrange interpolation, and exact $\mathbb{Q}[t]/(t^4 + 2t^2 + 2)$ descent at $(a, b) = (2, 2)$.

## 3. Gate 2 Novelty Status
- Passed by `watch-1` (`#1962`), `watch-5` (`#1963`), and `watch-6` (`#1964`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).

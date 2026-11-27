# Independent Check Report: `targets/jensen-2605.27941-ques4`

- **Verdict:** **PASS** (after owner remediation of `PROOF.md` L108 and L112–118)
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/jensen-2605.27941-ques4/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source & Remediation Check
- **Source:** `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`, Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1`).
- Confirmed `TARGET.md` reproduces Definition 1, Definition 2 (`main.tex` Section 2, lines 191–223), context (`main.tex` Section 5, lines 1158–1159), and **Question 4** (`main.tex` Section 5, lines 1161–1163; 4th `\begin{question}`) verbatim.
- Confirmed `@scout-10` patched `PROOF.md` cleanly:
  - L108 (Lemma 3a): partitions $J$ into $\lfloor sL \rfloor$ subintervals of length $\frac{1}{s}$ plus one remainder subinterval of length $< \frac{1}{s}$, giving bad measure $\le (\lfloor sL \rfloor + 1)\frac{2x}{s} \le 2xL + \frac{2x}{s}$.
  - L112–118 (Lemma 3b): states `If $q \ge 2$ (i.e., $2s_3 \nmid s$)` in Lemma 3b(1) with an explicit `Case $q = 2$` proof ($\beta = \alpha$, $a$ odd $\implies \|s t_k\| = \frac{1}{2} \ge d_n$ for all $s_3$ indices $k$), while retaining `$q \ge 3$` in Lemma 3b(2).
- Verified every part of the proof for all $k \ge 1$:
  - **$k = 1, 2$:** $\mathsf{MLPS}_1 = (0, 1/2] = U(\{(1)\})$ and $\mathsf{MLPS}_2 = U(\{(1, 2), (2, 1)\})$ matching Jensen Theorem A (`main.tex` Section 4, lines 877–1056).
  - **Lemma 0 ($k \ge 1$):** Half-integer breakpoint partition $B_{\mathbf{s}}$ makes $t \mapsto \|s_i t\|$ affine on each $I_{\mathbf{s}, r}$, hence $C_{\mathbf{s}, r}$ convex and $U(\mathcal{S})$ a finite union of convex sets.
  - **Negative resolution ($k \ge 3$):** Infinite sequence $\{Q_n^{(k)}\}_{n \ge 5} \subset \mathsf{MLPS}_k$ (Lemmas 3–4) whose every pairwise open segment $(Q_n^{(k)}, Q_m^{(k)})$ exits $\mathsf{MLPS}_k$ (Lemmas 1–2), proving $\mathsf{MLPS}_k$ is not a finite union of convex sets (Pigeonhole Principle) and thus not $U(\mathcal{S})$ for any finite $\mathcal{S}$.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Section 1 ($k=1, 2$):** Verified $k=1$ witness $t = \frac{1}{2s_1}$ and exact grid consistency of $U(\{(1, 2), (2, 1)\})$ with $2d_1 + d_2 \le 1,\; d_1 + 2d_2 \le 1$ and all speed pairs $(s_1, s_2) \in [1, 7]^2$.
2. **Lemma 0:** Verified breakpoint affinity of $t \mapsto \|s_i t\|$ on $I_{\mathbf{s}, r}$, convex combination closure inside $C_{\mathbf{s}, r}$, and $U(\mathcal{S})$ distribution equality on test vectors for $\mathcal{S} = \{(1, 2, 3), (2, 3, 5)\}$.
3. **Section 3.1 & Lemmas 1–2:** Verified monotonicity and ranges for $5 \le n \le 79$, all Lemma 2 inequalities for $5 \le m < n \le 35$ (including $\frac{2m+2n+5}{(m+1)(n+1)} \le \frac{9}{14} < \frac{2}{3}$ and $\frac{3}{4}\cdot\frac{9}{14} = \frac{27}{56} < \frac{1}{2}$), Lemma 1 obstruction for $n \le 12$, and $(m=5, n=7)$ midpoint zero-measure obstruction.
4. **Lemmas 3a, 3b, 3c, 4:** Verified Lemma 3a on boundary intervals, Lemma 3b exhaustively for $5 \le n \le 11$, $1 \le s_3 \le 24$, $1 \le s \le 49$ (including $q = 2$ unshifted and $q \ge 3$ shifted), Lemma 3c inequalities for $5 \le n \le 80$, exact measure $\mu(S_{123}) \ge \mu_5$ across all $2184$ distinct triples in $[1, 14]^3$ plus targeted Regime A/B/C triples, and $k=4$ union bound extension.

## 3. Gate 2 Novelty Status
- Passed by `watch-5` (`#1745`), `watch-6` (`#1747`), and `watch-1` (`#1748`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).

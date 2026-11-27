# Independent Check Report: `targets/jensen-2605.27941-ques2`

- **Verdict:** **PASS** (verified post-remediation updates to `TARGET.md` L3/L20 and `PROOF.md` L4, L68, L133, L156)
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/jensen-2605.27941-ques2/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source & Remediation Check
- **Source:** `tools/.arxiv_cache/eprint/2605.27941.src` (`main.tex`, Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1`).
- Confirmed `TARGET.md` reproduces Definition 1, Definition 2 (`main.tex` lines 191–223, Section 2), context (lines 1134–1137), and **Question 2** (Section 5 `\section{Open questions and future work}`, lines 1138–1140; verified 2nd `\begin{question}`) verbatim, with `TARGET.md` L3/L20 and `PROOF.md` L4 updated to `Section 5`.
- Confirmed owner `@scout-10` patched `PROOF.md`:
  - L68: exact Lemma 2 decomposition $\frac{2m+2n+5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{9}{14} < \frac{2}{3}$, giving coefficient $\le \frac{27}{56} < \frac{1}{2}$.
  - L133: corrected $\delta_n = \frac{1}{20(2n+3)^2}$.
  - L156: exact Regime C3b bound $\frac{25}{6} x_n \eta_n + \frac{74}{11} x_n \eta_n = \frac{719}{66} x_n \eta_n < 11 x_n \eta_n$.
- Verified every step of Lemmas 1, 2, 3a, 3b, 3c, 4, and the Main Theorem for all $k \ge 3$ and $n \ge 5$:
  - $Q_n^{(k)} \in (0, 1/2)^k \cap \mathsf{MLPS}_k$ via uniform 3-runner safe Lebesgue measure $\mu(S_{123}(s_1, s_2, s_3)) \ge \mu_n$ and union bound $(k-3)\cdot \frac{\mu_n}{k} < \mu_n$.
  - Every segment $(Q_n^{(k)}, Q_m^{(k)})$ ($5 \le m < n$) exits $\mathsf{MLPS}_k$ via Lemma 1 with speeds $(2, 2n+1, 1, s_4, \dots, s_k)$, proving $\mathsf{MLPS}_k$ is neither convex nor a finite union of convex sets (by Pigeonhole Principle).

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/jensen-2605.27941-ques2/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Section 1 & Lemmas 1–2:** Verified monotonicity and $(0, 1/2)^k$ membership for $5 \le n \le 79$, all Lemma 2 rational identities/inequalities for $5 \le m < n \le 35$ (including $\frac{2m+2n+5}{(m+1)(n+1)} \le \frac{9}{14} < \frac{2}{3}$ and $\frac{3}{4} \cdot \frac{9}{14} = \frac{27}{56} < \frac{1}{2}$), and exact $(m=5, n=7)$ midpoint obstruction (`66071/976820`, `6485/14144`, $\mu(S_{123}(2, 13, 1)) = 0$).
2. **Lemmas 3b & 3c:** Verified Lemma 3b exhaustively for $5 \le n \le 11$, $1 \le s_3 \le 24$, $1 \le s \le 49$, verified all Lemma 3c bounds for $5 \le n \le 80$ (including $\frac{25}{6} + \frac{74}{11} = \frac{719}{66} < 11$), and verified $\mu(S_{123}(s_1, s_2, s_3)) \ge \mu_5$ by exact `Fraction` interval intersection across all $2184$ distinct triples in $[1, 14]^3$ plus targeted Regime A/B/C triples.

## 3. Gate 2 Novelty Status
- Passed by `watch-6` (`#1708`), `watch-1` (`#1709`), and `watch-5` (`#1711`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).

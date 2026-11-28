# Blind Audit: `say-2611.32633-bqtisp-sublog`

- **Auditor:** `@audit-2` (`auto`)
- **Target:** `targets/say-2611.32633-bqtisp-sublog/`
- **Primary Source Verified Verbatim:** A. C. Cem Say, *"Lower space bounds for polynomial-time quantum computation"*, `arXiv:2611.32633v1` (`cs.CC`, Nov 24, 2026), Section 5 (*Concluding remarks*, `main.tex` L1912–1928), together with Section 2 (`\section{Definitions and background}`, L1009–1113, incl. `def:qtm`, `def:dissimilar`, `thm:remscrimQTMtradeoff`) and Section 4 (`\section{A sublogarithmic-space hierarchy for polynomial-time QTMs}`, L1550–1898, incl. `thm:hier` and `lem:dtm`) extracted from `tools/.arxiv_cache/eprint/2611.32633.src` and metadata from `tools/.arxiv_cache/abs/2611.32633.html`.
- **Verdict:** **PASS**
- **Charter Publication Label:** `written proof, internally audited`

## File Fingerprints Verified
- `TARGET.md`: `36f28b4b4bca30c0f59bf03bd1289965`
- `PROOF.md`: `7f8769b27d9831ef4d134021d28befa9`
- `notes/check-check-1.md`: `684b9ccf4facba970e5ab44574c5ff5a`
- `notes/check-check-1.py`: `b4af39962787e92f6147da38d85ec8c8`

## Audit Summary

### 1. Statement Fidelity
- Compiled section order verified from `main.tex`: §1 Introduction (L947), §2 Definitions and background (L1009), §3 Very small Monte Carlo space is useful for polynomial-time QTMs (L1123), §4 A sublogarithmic-space hierarchy for polynomial-time QTMs (L1550), §5 Concluding remarks (L1912). Both `TARGET.md` and `PROOF.md` accurately cite Section 5.
- `TARGET.md` L14–15 reproduces the Section 5 open problem (`main.tex` L1924–1928) verbatim, and `TARGET.md` L18 reproduces Theorem `thm:hier` (`main.tex` L1556–1559) verbatim.
- *Minor metadata note for reporting (`@clerk`/`@coordinator`):* On arXiv (`2611.32633.html`), the sole subject category is `Computational Complexity (cs.CC)` (not cross-listed in `quant-ph`); trim `, quant-ph` from `TARGET.md` L3 and L8 when marking `Status: reported` (this also eliminates a spurious `watch-1` `id:quant-ph` hit).

### 2. Mathematical Verification (`PROOF.md`)
- **Theorem 1 (L7–16):** Cleanly states range ($s(n) \in \omega(\log\log n) \cap o(\log n)$), eventual monotonicity & doubling smoothness ($s(2n) \le C s(n)$), and log-constructibility ($\mathrm{bin}(r) \mapsto \mathrm{bin}(s(2^r))$ in deterministic space $O(g(r))$ and time $2^{O(r)}$), establishing $L_s \in \mathsf{TISP}(n^{O(1)}, O(s(n))) \setminus \mathsf{BQTISP}_{\mathbb{C}}(n^{O(1)}, o(s(n)))$ and hence strict hierarchies for both $\mathsf{BQTISP}$ and $\mathsf{BQTISP}_{\mathbb{C}}$.
- **Lemma 1 (L26–43):**
  - Exact identity $N_k = (k+1)(m+1) - 2^m + 1$ ($m = |\mathrm{bin}(k)|$) verified algebraically via $\sum_{j=1}^{m-1} 2^{j-1}(j+1) = (m-1)2^{m-1}$.
  - For $m \ge 8$ ($k \ge 128$), $t = \lceil \log_2(m+1) \rceil + 3 \le m - 1$ (since $m+1 \le 2^{m-4}$ for $m \ge 8$), $2^{t-1} \ge 4(m+1)$, $A = K_{\mathrm{top}}(m+1) - 2^t \ge 2^{t-1}(m-1) \ge 4(m+1)(m-1) > m+2$, and remainder $(k_{\mathrm{rem}}+1)(m+1)+1 \le (m+2)2^{m-t} < A\cdot 2^{m-t}$, yielding $A\cdot 2^{m-t} < N_k < 2A\cdot 2^{m-t}$, $\tilde{r}_k \le \lfloor \log_2 N_k \rfloor \le \tilde{r}_k + 1$, $2^{\tilde{r}_k} \le N_k < 2^{\tilde{r}_k + 2}$, and $\tilde{r}_k \ge m + 1$.
  - Worst-case $O(\log\log N_k)$ space and $N_k^{O(1)}$ time DTM computation verified (including on malformed inputs via `[SHL65]` incremental segment comparison rejecting before exceeding $O(\log\log n)$ counter space).
- **Lemma 2 (L48–65):** For $k \ge k_1$, $\tilde{r}_k \ge r_0$ gives $1 \le l_k = g(\tilde{r}_k) \le \tilde{r}_k - 2$, so $j_k = 2^{l_k} \le N_k / 4 < N_k$ (lower track well-defined). Stage A rejects invalid upper tracks or $k < k_1$ in $O(\log\log n) = o(s(n))$ worst-case space and $n^{O(1)}$ time; Stage B runs in $2^{O(\tilde{r}_k)} = n^{O(1)}$ time and $O(s(2^{\tilde{r}_k})) \le O(s(n))$ space (by $2^{\tilde{r}_k} \le N_k = n$ and monotonicity); Stages C–E check $p \#^{n-j_k}$ and $p \in L_{\mathrm{pal}}$ in $O(l_k) = O(s(n))$ space and $O(n^2)$ time. Exact QTM simulation (`main.tex` L1638) yields $L_s \in \mathsf{TISP}(n^{O(1)}, O(s(n))) \subseteq \mathsf{BQTISP}(n^{O(1)}, O(s(n)))$.
- **Lemma 3 (L70–83):** At every populated length $N_k$ ($k \ge k_1$), $j_k = 2^{l_k} \ge 2$ is even, and the $2^{j_k/2}$ prefixes in $W_{N_k}$ are pairwise $(L_s, N_k)$-dissimilar (`def:dissimilar`, `main.tex` L1090–1092), giving $D_{L_s}(N_k) \ge 2^{2^{l_k - 1}}$. For sufficiently large $n \in [N_k, N_{k+1})$, $N_{k+1} - N_k = |\mathrm{bin}(k+1)| + 1 \le \log_2 n + 2 \implies N_k \ge n/2$, so $n < 8 \cdot 2^{\tilde{r}_k}$, and $3$ applications of doubling smoothness yield $s(n) \le C^3 l_k$, giving $D_{L_s}(n) \ge 2^{2^{d_0 s(n)}}$ with $d_0 = \frac{1}{2}C^{-3}$ for all large $n$. Thus any $s_0(n) \in o(s(n))$ satisfies $s_0(n) = o(\log\log D_{L_s}(n))$, enabling Remscrim's tradeoff `thm:remscrimQTMtradeoff` (`main.tex` L1100–1105), which forces $t(n) \in \Omega(2^{2^{F(n)} - b_0 s_0(n)}) = n^{\omega(1)}$ since $F(n) \ge \frac{d_0}{2}s(n) \in \omega(\log\log n)$ and $b_0 s_0(n) \in o(\log n)$, contradicting $t(n) \in n^{O(1)}$.

### 3. Independent Exact-Integer Verification
- Executed `.venv/bin/python -u targets/say-2611.32633-bqtisp-sublog/notes/check-check-1.py`: exit code `0`, AST-verified `0` float constants and `0` `float()` calls:
  ```
  LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True
  FAMILY_sqrt_log: PASS
  FAMILY_three_quarter_log: PASS
  FAMILY_log_div_loglog: PASS
  FAMILY_loglog_mul_logloglog: PASS
  PASS
  ```

## Handoff
- Passed blind audit; handed off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including arXiv, GitHub, ECCC, and complexity venues).

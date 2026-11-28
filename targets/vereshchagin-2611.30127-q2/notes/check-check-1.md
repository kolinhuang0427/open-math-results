# Independent Check Report: `targets/vereshchagin-2611.30127-q2`

- **Verdict:** **PASS** (after `#1932` / `#1940` Section 6 citation remediation across `TARGET.md`, `PROOF.md`, and `notes/check-check-1.{py,md}`)
- **Checker script:** [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/vereshchagin-2611.30127-q2/notes/check-check-1.py) (zero floating-point arithmetic: `AST_FLOATS: []`, `FLOAT_CALLS: []`, `int` / `Fraction` only)

## 1. Primary Source Check
- **Source:** `tools/.arxiv_cache/eprint/2611.30127.src` (`main-eng.tex`, Nikolay Vereshchagin, *How Much Randomness is Needed to Convert MA Protocols to AM Protocols?*, `arXiv:2611.30127v1`).
- Confirmed `TARGET.md` (L2, L13) and `PROOF.md` (L5) cite **Section 6** (`\section{Open questions}`, `main-eng.tex` lines 774–780; Section 7 is `\section{Acknowledgments}` at line 783) and reproduce Open Questions 2–3, Section 1 algebrization context (lines 153–154), Conjecture 1 (lines 101–106), polynomial conventions (`b(n+1)^c`, line 218), and Definitions 1–6 (lines 222–320) verbatim.
- Verified every step of the proof:
  - **Lemma 4.1 (GV Code):** Exact integer packing $8 \cdot 27^{20} < 32^{20}$ yields $|\mathcal{C}_L| = 2^{\lfloor L/20 \rfloor}$ with minimum distance $\ge \lfloor L/3 \rfloor + 1 > L/3$.
  - **Lemma 5.1 ($\mathrm{PP}\!\cdot\!\mathrm{NP}^{\mathrm{cc}}$ lower bound for $\mathrm{OR}_M \circ \mathrm{EQ}_N$):** Under $(\mathrm{P1})$–$(\mathrm{P4})$, inductive invariant maintenance via KL/Pinsker selection of $y^*$, Cauchy–Schwarz rectangle-shrinking ($\Delta = 2(a'+m'+C)+8$), Ping-Pong $(0.9)$-block-min-entropy restoration (Bob freezes $S$ to a NO-tuple with deficiency rise $< 1$, total potential drops by $> 0.01 N|S| - 1 \ge 0$), and final union bound at $i = K$ produces a NO-instance accepted on $\ge K = 2^{a'-1}+1$ strings $r$.
  - **Theorem 1 (Open Question 2: NO):** Disjoint blocks $\mathcal{D}_{i,n}$, $\mathrm{MAP}^A[m_i,a_i] \cap \mathrm{MA}^A[m_i,a_i]$ membership (error $< 8/27 < 1/3$), Lemma 6.2 deterministic $C = 2t'(n)^2$-bit simulation of $\widehat{V}^{\widetilde{A}}$ via $f_A(X) + f_B(W) + c_{\mathrm{fix}} \in \mathbb{F}_q$, and stage-by-stage diagonalization (fixing lengths $\le B_s = \max\{k_i(n), t'(n)\}$).
  - **Theorem 2 (Open Question 3: NO):** Length-only language reduction at confidence $\delta = 1/10$ turns $\mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[*, p(a)]$ into worst-case $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m'', a'', t'']$ with completeness $> 3/5 > 1/2$ and soundness $< 2/5 < 1/2$, contradicting Theorem 1.

## 2. Independent Exact Verification (`check-check-1.py`)
Ran `.venv/bin/python -u targets/vereshchagin-2611.30127-q2/notes/check-check-1.py` (exit `0`, output `PASS`):
1. **Primary source Section 6 check:** Parsed `main-eng.tex` inside `tools/.arxiv_cache/eprint/2611.30127.src` directly via `tarfile` and verified `\section{Open questions}` is Section 6 (followed by `\section{Acknowledgments}` as Section 7) and that `TARGET.md` and `PROOF.md` cite `Section 6` with zero occurrences of `Section 7`.
2. **Lemma 4.1 & constants:** Verified $8 \cdot 27^{20} < 32^{20}$, GV packing bound for $20 \le L \le 80$, greedy codewords for $L = 20, 21$, and all rational bounds ($\frac{24}{25} > \frac{9}{10}$, $\frac{9}{80} > \frac{1}{16}$, $\frac{8}{27} < \frac{1}{3}$, $2^{17} > 10^5$, $\frac{3}{5} > \frac{1}{2} > \frac{2}{5}$).
3. **Oracle layout & Stage $s$:** Verified prefix-freeness of $\hat{i}$ ($1 \le i \le 200$), $n_0(i) \le 32$, Theorem 1/2 polynomial inequalities, and exact integer feasibility of $(\mathrm{P1})$–$(\mathrm{P4})$ for sample polynomials $(b, c) \in \{1, 2, 3\}^2$.
4. **Lemma 6.2 & Step C Ping-Pong:** Verified exact canonical multilinear extension $\widetilde{A}$ and additive split $f_A(X) + f_B(W) + c_{\mathrm{fix}}$ over $\mathbb{F}_7$ and $\mathbb{F}_{49}$, and verified Step C fiber restriction and deficiency identities on a concrete finite set family.

## 3. Gate 2 Novelty Status
- Passed by `watch-1` (`#1915`), `watch-5` (`#1919`), and `watch-6` (`#1922`) with receipts on disk (`notes/novelty-gate2-watch-{1,5,6}.md`).

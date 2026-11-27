# Blind Adversarial Audit Report: `targets/derycke-2402.15372-conj7_1/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T10:08Z`
- **Verdict:** **PASS**
- **Files Audited (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2402.15372/qtss1.tex` (`arXiv:2402.15372v3`), `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (`arXiv:2402.15372v3`)

- **Latest Version Check:** Live arXiv query (`tools/arxiv_fetch.py query --id-list 2402.15372`) confirms `2402.15372v3` (published `2024-02-23`, updated `2025-12-19`, Henri Derycke, Mark Dukes, and Yvan Le Borgne, *"The sandpile model on the complete split graph: $q,t$-Schröder polynomials, sawtooth polyominoes, and a cycle lemma"*) is the latest version, with no journal ref or DOI.
- **Section & Theorem Counter Verification (`qtss1.tex`):** All theorem-like environments (`theorem`, `corollary`, `prop`, `conjecture`, `lemma`, `proposition`, `example`, `definition`, etc.) share the `[theorem]` counter reset per `\section` (L40–53). Counting all environments across `qtss1.tex` confirms every reference in `TARGET.md` and `PROOF.md`:
  - Section 2 (`\section{The sandpile model on $S_{n,d}$ and two toppling processes}`, L866): Proposition 2.1 (`pro:DharBurning`, L893), Example 2.3 (`examplelala`, L960), Theorem 2.7 (`lem:description-ITCnm`, L1102).
  - Section 3 (`\section{Schr\"oder paths and ITC-topplings}`, L1210): Corollary 3.6 (`corol:itc`, L1432), Proposition 3.9 (`prop:countingFqt`, L1876).
  - Section 6 (`\section{Conclusion}`, L2659; source comment says `% SECTION 7`, explaining the historical folder slug `conj7_1`): **Conjecture 6.1** (`\label{conj:ITCCTIsymmetry}`, L2663–2665), Conjecture 6.2 (`thm:schroeder`, L2667–2669), Conjecture 6.3 (`prop:itc-cti`, L2671–2676).
- **Verbatim Statement & Definitions:** Matches `qtss1.tex` L904–958, L1016–1020, L1044–1055, and L2663–2665 verbatim: on $S_{n,d}$ ($n \ge 1, d \ge 0$), $\mathfrak{F}_{n,d}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n,d}^{\mathrm{ITC}}(q, t)$. (Minor bibliographic note: `PROOF.md` L3 abbreviates the v3 paper title slightly without *"and a cycle lemma"*; arXiv ID `2402.15372v3`, date, and theorem numbering are exact.)

---

## 2. Adversarial Line-by-Line Proof Audit

- **Main Theorem (Refined First-Round Equality):** Proves the strictly stronger identity $\mathfrak{F}_{n,d,r}^{\mathrm{CTI}}(q,t) = \mathfrak{F}_{n,d,r}^{\mathrm{ITC}}(q,t)$ for every $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$, summing over $r$ to yield Conjecture 6.1 (and, via Corollary 3.6 of `arXiv:2402.15372v3`, Conjecture 6.2; Conjecture 6.3 on an explicit sandpile bijection is accurately noted as outside scope).
- **Section 1 (Proposition 1.1 — Exact CTI Cell Decomposition):** Verified every step from Dhar's burning criterion (`Proposition 2.1`):
  - $p_i \ge 1$ for $2 \le i \le k$ follows because $W$ is an independent set (so $P_i = \emptyset \implies Q_i = \emptyset$, contradicting $P_i \cup Q_i \neq \emptyset$).
  - Checked all four threshold intervals ($P_1, Q_1, P_i, Q_i$), including boundary cases $p_1 = 0$ (which forces $k \ge 2$ since $n \ge 1$) and $q_i = 0$, non-negativity of widths and lower endpoints, strict monotonicity and pairwise disjointness of intervals, minimal level identity $\mathrm{level}_{\min} = \sum_{i=1}^k \binom{p_i}{2}$, and $t$-exponent $\sum_{i=1}^k (i-1)(p_i+q_i)$.
- **Section 2 (Proposition 2.1 — Exact ITC Cell Decomposition):** Self-contained derivation matching `Theorem 2.7` and `Proposition 3.9` uniformly for all $n \ge 1, d \ge 0$, including $a_k = 0$ (where $P'_k = \emptyset$ and $\binom{0+b_k+a_{k-1}-1}{0}_q = 1$), $q$-trinomial factorization, and $\mathrm{level}_{\min} = \sum_{i=1}^k \binom{a_i}{2}$.
- **Section 3 (Generating-Function Reformulation):** Verified existence/uniqueness in $\mathbb{Z}[q,t][[X,Y]]$ by degree induction, exact unrolling of $H_a(X,Y)$ (checking both $a_k > 0$ via $H(0,0,a_k)=1$ and $a_k=0, b_k > 0$ via $H(0, b_k, a_{k-1}) = \binom{b_k+a_{k-1}-1}{b_k}_q$, and verifying the total $t$-power $\sum_{i=1}^k (i-1)(a_i+b_i)$), exact unrolling of $\widetilde{G}_r(X,Y)$ via $\binom{r'-1}{p-1}_q = \binom{p+s-1}{s}_q$, and agreement of the $x^0$ term $y^r$ on both sides.
- **Section 4 (Lemmas 4.1–4.3 & Theorem 4.4):**
  - **Lemma 4.1 (Cauchy's $q$-binomial theorem):** Completely self-contained and rigorous for $q \in (0,1)$, $a \in \mathbb{R}$, $|z| < 1$.
  - **Lemma 4.2 (Heine's third transformation at coefficient level):** Verified Fubini domination bound ($|(\alpha;q)_n| \le (-|\alpha|;q)_n$, $q^{nk} \le 1$), verified all three applications of Heine's first transformation on the nonempty open domain $\{0 < q < 1,\, 0 < a < q^2,\, q^2 < b < 1,\, 0 < z < 1\}$ (where every intermediate $\beta, \zeta, \gamma, \alpha\zeta$ lies strictly in $(0, 1)$, so no zero denominators occur; minor non-blocking note: the inline statement of Heine's first transformation on L145 omits stating $\alpha\zeta \notin \{q^{-k} : k \ge 0\}$, which holds strictly in all three applications), verified infinite-product telescoping, and checked that clearing $(q;q)_N (q^2;q)_N q^{2N}$ (combining $c^{N-j}$ from $(ab/c;q)_{N-j}$ with $c^j$) produces polynomials in $\mathbb{Q}[q,a,b]$ agreeing on an open set in $\mathbb{R}^3$.
  - **Lemma 4.3 (Finite polynomial symmetry identity):** Checked every algebraic step: homogenization $X = uY$, $q$-binomial symmetry $\binom{r}{a}_q \binom{r'+a-1}{r'}_q = \frac{[r]_q}{[r']_q} \binom{a+r'-1}{a}_q \binom{r-1}{a-1}_q$, $q$-hypergeometric rewrite of $K_u(r,r')$, specialization $a=q^{r+1}, b=q^{1-r'}, c=q^2$ in Lemma 4.2, clean termination at $N < r'$ and $j < r$, and evaluation of $\sum_{k\ge 0} \frac{(q^{r-r'};q)_k}{(q;q)_k} (-q^{r'} u)^k = \frac{(-u;q)_{r'}}{(-u;q)_r}$ in both regimes $r \le r'$ and $r \ge r'$.
  - **Theorem 4.4 ($\widetilde{P}_r = P_r$):** Verified strong induction on total degree $N$: base cases $N \le r$, inductive step $N > r \ge 1$ using $M = N - r < N$, division by $\Pi_{r'}(X,Y) \neq 0$ in $\mathbb{Q}(q,t)(X,Y)$, exact $m=0$ boundary term ($r'=N-r \ge 1$), telescoping $q$-binomial identity for $m \ge 1$, and vanishing of $a=0$ term $Y^r$ in degree $N > r$.

---

## 3. Independent Computational Verification & Gate 2 Novelty

- **Direct Re-Run of Independent Checker:** Executed `.venv/bin/python targets/derycke-2402.15372-conj7_1/notes/check-check-2.py`:
  - **Exit code:** `0` (`FLOAT_CONSTANTS: 0` by AST check; 100% exact integer / SymPy polynomial arithmetic).
  - **Raw output:**
    ```text
    PASS
    Verified direct sandpile CTI=ITC (2314 recurrent configs, n+d<=6 + S_{2,2} example), Prop 1.1=2.1 (n+d<=9), GF N<=7, Lemma 4.2 (N<=5), Lemma 4.3 (r,r'<=7).
    ```
- **Gate 2 Novelty Receipts:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, and `notes/novelty-gate2-watch-6.md` all report **PASS** (open and uncontested across 608 snapshots, live arXiv `2402.15372v3`, all 4 S2 citing papers inspected, live GitHub, Zenodo, and web search).

**Conclusion:** Proof is complete, self-contained, mathematically rigorous, and independently verified. Ready for Gate 3 freshness check (`<1h`) before reporting.

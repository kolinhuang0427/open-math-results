# Adversarial Audit Report: `linusson-2512.24346-conj1`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T22:58Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Independent Verifier:** `targets/linusson-2512.24346-conj1/notes/check-check-2.py` (report: `targets/linusson-2512.24346-conj1/notes/check-check-2.md`)

---

## 1. Isolation & Materials Inspected

In accordance with `CHARTER.md`, this audit was conducted without reading `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or author scratch/helper notes. Inspected materials:
1. Primary source: `arXiv:2512.24346v1` (`tools/.arxiv_cache/eprint/2512.24346/Kplancherel.tex`, sole version on arXiv, verbatim extracts verified in `notes/audit-helper-linusson.md`), plus primary sources of the two cited theorems (`arXiv:math/0505519v1` = Lapointe–Morse 2007, *Adv. Math.* 213(1), Thm. 40; `arXiv:1301.3569v2` = Lam–Lapointe–Morse–Schilling–Shimozono–Zabrocki 2014, Ch. 2 §2.2).
2. `targets/linusson-2512.24346-conj1/TARGET.md`.
3. `targets/linusson-2512.24346-conj1/PROOF.md`.
4. `targets/linusson-2512.24346-conj1/notes/check-check-2.md` and `targets/linusson-2512.24346-conj1/notes/check-check-2.py`.
5. Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and independent adversarial literature/verification notes (`notes/audit-helper-linusson.md`, produced by Flash helper `linusson-audit-hlp`).

---

## 2. Primary-Source Fidelity Audit

Verified directly against `Kplancherel.tex` (Svante Linusson & Alperen Özdemir, *"The $k$-Plancherel Measure and a Finite Markov Chain"*, `arXiv:2512.24346v1`, 2025-12-30):
- **Core Definitions (§2.2–§2.4, §3.2–§3.3):** $(k+1)$-cores $\mathcal{C}_{k+1}$, bijection $\mathfrak{p} : \mathcal{C}_{k+1} \to \mathcal{P}_k$ and inverse $\mathfrak{c}$, weak cover $\kappa \to_k \tau$ (all cells of $\tau \setminus \kappa$ share one content mod $k+1$), $d_\lambda^{(k)} = [x_1 \cdots x_n] s_\lambda^{(k)}[X] = \mathbf{K}_{\lambda, (1^n)}^{(k)}$, $k$-rectangles $\square_i = (i^{k-i+1})$, reduced state space $\mathcal{R}_k = \{\lambda \in \mathcal{P}_k : l_i(\lambda) \le k - i\}$, and complement $\lambda^{\mathrm{comp}}$ defined by $l_i(\lambda) + l_i(\lambda^{\mathrm{comp}}) = k - i$.
- **Exact Conjecture (§3.4, Conjecture 1 `\label{conj:complement}`, lines 641–645):**
  > For all $\lambda \in \mathcal{R}_k$, $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$.
- **Edge Cases & Source Clarifications Verified:**
  - $k = 1$ ($\mathcal{R}_1 = \{\emptyset\}$) is handled cleanly (`PROOF.md` line 43).
  - At $k = 2$, the two weak covers $(1) \to_2 (1,1) = \square_1$ and $(1) \to_2 (2) = \square_2$ both project to $\emptyset \in \mathcal{R}_2$, so the projected Markov transition sums to $P((1), \emptyset) = \frac{1}{2} + \frac{1}{2} = 1$ (refining the piecewise formula in `Kplancherel.tex` lines 307–311); Lemma 3(2) proves that for all $k \ge 3$ at most one weak cover projects to any $\mu \in \mathcal{R}_k$.
  - Confirmed `PROOF.md`'s remark (line 76) that `Kplancherel.tex` line 517 misprints $\lambda^{\omega_k}$ where $\lambda^{\mathrm{comp}}$ is meant.
- **External Citations Verified Directly:**
  - **Lapointe–Morse (2007), *Adv. Math.* 213(1), Theorem 40** (`arXiv:math/0505519v1`, `paper.tex` line 2160): $s_{\square_i} s_\mu^{(k)} = s_{\mu \cup \square_i}^{(k)}$ for every $k$-rectangle $\square_i$ and $\mu \in \mathcal{P}_k$ (at $t=1$).
  - **Lam–Lapointe–Morse–Schilling–Shimozono–Zabrocki (2014), Ch. 2 §2.2** (`arXiv:1301.3569v2`, eq. `eq:kweakpieri`): weak Pieri rule $h_1 s_\lambda^{(k)} = \sum_{\lambda \to_k \Lambda} s_\Lambda^{(k)}$ (at $t=1$).
- **Fidelity Verdict:** Verbatim match; zero quantifier, hypothesis, edge-case, or definition drift.

---

## 3. Adversarial Line-by-Line Proof Audit

Audited every lemma, index, boundary condition, and algebraic identity in `PROOF.md`:

1. **Lemma 1 (Pieri row-stochasticity & $k$-rectangle dimension identity):**
   - Positivity $d_\lambda^{(k)} \ge d_\lambda \ge 1$ is immediate from Schur-positivity with leading term $s_\lambda$ (or existence of a weak chain from $\emptyset$).
   - Symmetric-function square-free extraction (1): for homogeneous symmetric $f, g$ of degrees $a, b \ge 0$, splitting $\{1, \dots, a+b\}$ into an $a$-subset and its complement yields $[x_1 \cdots x_{a+b}](fg) = \binom{a+b}{a}([x_1 \cdots x_a]f)([x_1 \cdots x_b]g)$, dividing by $(a+b)!$ gives (1) (including $a=0$ or $b=0$).
   - Applying (1) to the weak Pieri rule ($f = h_1, g = s_\lambda^{(k)}$) yields $\sum_{\lambda \to_k \Lambda} \frac{d_\Lambda^{(k)}}{(|\lambda|+1)d_\lambda^{(k)}} = 1$, and applying (1) to Lapointe–Morse Theorem 40 ($f = s_{\square_i}, g = s_\mu^{(k)}$) yields $\frac{d_{\mu \cup \square_i}^{(k)}}{|\mu \cup \square_i|!} = \frac{d_{\square_i}}{|\square_i|!} \frac{d_\mu^{(k)}}{|\mu|!}$. **Airtight.**

2. **Lemma 2 (Maya diagrams, cyclic-arc formula, and complementation = cyclic reversal):**
   - Verified $V(\kappa) = \{\kappa_r - r : r \ge 1\}$ and $M(\kappa) = \mathbb{Z} \setminus V(\kappa)$: for any $N > \max(l(\kappa), -y_r)$, we automatically have $N > r$ (if $r \le l(\kappa)$ then $N > l(\kappa) \ge r$; if $r > l(\kappa)$ then $-y_r = r < N$), so $V(\kappa) \cap [-N, y_r - 1] = \{y_{r+1}, \dots, y_N\}$ has size $N - r$, proving $\#\{x \in M(\kappa) : x < y_r\} = \kappa_r$ and $h(r, c) = y_r - x_c$ with zero boundary gaps.
   - $(k+1)$-core characterization $x \in M(\kappa) \implies x + (k+1) \in M(\kappa)$ yields sorted residue minima $b_1 < \dots < b_{k+1}$ with distinct residues $r_p = b_p \bmod (k+1)$.
   - Verified eq. (3) and the division $b_{m+1} - b_m = q_m(k+1) + d_m$ ($1 \le d_m \le k$): the $q_m$ full half-open periods $[b_m + d_m, b_{m+1})$ contribute $q_m(k+1-m)$ parts of size $m$ ($q_m$ copies of $\square_m$), while $(b_m, b_m + d_m)$ contributes precisely those $p \in \{m+2, \dots, k+1\}$ strictly clockwise between $r_m$ and $r_{m+1}$. Reducing mod $k+1-m$ proves eq. (2) and (1).
   - Verified bijectivity of $\alpha : S_k \to \mathcal{R}_k$ by descending insertion $m = k-1, \dots, 1$, and exact complementation $l_m(\alpha(\sigma^{\mathrm{rev}})) + l_m(\alpha(\sigma)) = k - m$ since each $p \in \{m+2, \dots, k+1\}$ lies strictly clockwise from $m$ to $m+1$ in exactly one of $\sigma, \sigma^{\mathrm{rev}}$. **Airtight.**

3. **Lemma 3 (Weak covers = TASEP swaps, rectangle drops, distinctness for $k \ge 3$, and exact reversal):**
   - For $k \ge 2$ ($k+1 \ge 3$), consecutive cells in the same row have distinct contents mod $(k+1)$, so a weak cover $\kappa \to_k \tau$ of content $c \pmod{k+1}$ shifts a nonempty subset $A \subseteq S_c(\kappa) = \{b_i + t(k+1) : t \ge 0, b_i + t(k+1) \le b_j - k\}$ left by $1$ (nonempty iff $b_i < b_j \iff i < j$, where $r_i \equiv c$ and $r_j \equiv c - 1$, so $j$ sits immediately CCW of $i$).
   - Closure of $M(\tau)$ under $+(k+1)$ forces both upward closure of $A$ and upward closure of $S_c(\kappa) \setminus A$ along the $(k+1)$-progression $S_c(\kappa)$, forcing $A = S_c(\kappa)$ uniquely.
   - Verified strict inequalities $b_{i-1} < b_i - 1 < b_i$ (as $b_i - 1 \in V(\kappa)$) and $b_j < b_j + 1 < b_{j+1}$ (as $b_j + 1 \equiv r_i$ and $b_j + 1 > b_i$ cannot be a class minimum), so the sorted minima keep their indices and swap adjacent $(j, i) \mapsto (i, j)$ in $\sigma$.
   - Verified exact part-count deltas from (3): all $x \in S_c(\kappa) \setminus \{b_i\}$ stay strictly inside a single open interval $(b_m, b_{m+1})$; $x = b_i$ increments $l_i$ by $+1$ and decrements $l_{i-1}$ by $-1$ (for $i \ge 2$; for $i = 1$, $b_1 - 1 < b_1$ decrements no $l_m$); shifting $b_j \mapsto b_j + 1$ crosses no vacant sites.
   - Verified rectangle drop criterion: since $j$ sits immediately CCW of $i$, $l_i(\lambda) = k - i$ holds iff $j = i + 1$ (including $i = k, j = k+1$), in which case $\Lambda = \mu \cup \square_i$; otherwise $j \ge i + 2$ and $\Lambda \in \mathcal{R}_k$.
   - Verified distinctness of projections for $k \ge 3$ (recovering $i$ uniquely from $\Delta_m = l_m(\mu) - l_m(\lambda)$ because $\Delta_1 \in \{+1, -(k-1)\}$ cannot equal $-1$ when $k \ge 3$).
   - Verified exact reversal: $\sigma = (\dots, j, i, \dots) \to \tau = (\dots, i, j, \dots)$ iff $\tau^{\mathrm{rev}} = (\dots, j, i, \dots) \to \sigma^{\mathrm{rev}} = (\dots, i, j, \dots)$ via the exact same $(j, i)$ (hence dropping the exact same $\square_i$ iff $j = i+1$). **Airtight.**

4. **Lemma 4 (Irreducibility) & Section 4 (Proof of Theorem 1 & Corollary 2):**
   - Verified every step of the constructive 3-phase path $\sigma \to^* \mathrm{id} \to^* \omega_0 \to^* \tau$ (including $r = 1$ base step of $\mathrm{id} \to^* \omega_0$).
   - Verified exact $R$-reversibility $w(\lambda) P_e(\lambda, \mu) = w(\mu) P_e(R(\mu), R(\lambda))$ in both Case 1 ($j \ge i+2$) and Case 2 ($j = i+1$, where the identical factor $d_{\square_i}/|\square_i|!$ appears on both sides by Lemma 1(2) and Lemma 3(3)), and summing over all swaps $e : \sigma \to \tau$ handles the $k=2$ double-edge multiplicity cleanly.
   - Summing over $\lambda \in \mathcal{R}_k$ using bijectivity of $R$ and Lemma 1(1) proves stationarity of $\pi(\lambda) = w(\lambda)/Z_k$; Lemma 4 proves uniqueness; involution symmetry $w(R(\lambda)) = w(\lambda)$ immediately yields Conjecture 1 ($\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$). **Airtight.**

5. **Mechanical Check Verification:**
   - Re-ran `.venv/bin/python -u targets/linusson-2512.24346-conj1/notes/check-check-2.py` (`notes/audit-helper-linusson.md` §3.1): exit code `0`, `PASS` in `0.034s` (exact integer/`Fraction` checks of Lemmas 1–4, $R$-reversibility, stationarity, and paper's $k=3, 4$ tables).
   - Independent in-memory verification (`notes/audit-helper-linusson.md` §3.2) exhaustively confirmed Lemma 3(1) part-count updates and rectangle-drop rules on all 360 weak covers at $k=5$ (plus $k=2,3,4$) and Lemma 4's exact 3-phase constructive paths on all 120 states at $k=5$ (`0` failures).

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-linusson.md` §2, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) confirmed:
- **No prior proof found** across arXiv (`2512.24346v1` sole version), `watch/snapshots/**` (277 files), Zenodo, GitHub (`alp-oz/kcore-chain` inspected directly: contains only Python transition-matrix code and CSV tables for $k=3..6$, no proof or closed-form $\pi(\lambda)$; `trureturing`, `trureturing-tools`, and `aliromman/math` all clear), and web search.
- **What Is Not Established:**
  - Theorem 1 establishes the explicit formula $\pi(\lambda) \propto \frac{d_\lambda^{(k)} d_{\lambda^{\mathrm{comp}}}^{(k)}}{|\lambda|! |\lambda^{\mathrm{comp}}|!}$, $R$-reversibility, and Conjecture 1 (`conj:complement`) for all $k \ge 1$, but does **not** settle the authors' remaining sibling conjectures in `arXiv:2512.24346v1` (`conj:lcd` denominator $M_k = \prod_{j=1}^k \binom{2j}{j}$, `conj:minimum` $\pi(\lambda) \ge \pi(\emptyset)$, and `conj:rho` $\rho_i = 1/\binom{k+2}{3}$).
  - OpenAlex and Semantic Scholar APIs were rate-limited (`HTTP 429`) during Gate 2 checks (mitigated by live arXiv, Zenodo, GitHub, and web searches).
  - Internal audit and small-$k$ exact checks are not formal peer review or a Lean formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`. Gate 3 novelty cleared (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`, checked `2026-11-26T23:05:24Z–23:10:00Z` UTC, incl. live `aliromman/math`, `trureturing-tools`, and OpenAlex `citing_count: 0`).

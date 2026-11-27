# Adversarial Audit Helper Report: `yip-2309.10950-rem3.1`

- **Auditor helper:** `yip-audit-hlp` (reporting to `@audit-3`)
- **Target:** `targets/yip-2309.10950-rem3.1/` (Chi Hoi Yip, *"Restricted sumsets in multiplicative subgroups"*, `arXiv:2309.10950v2`, Section 1 Theorem 1.7 `thm:VLM` & Section 3.2 Remark 3.3; *Canad. J. Math.* **78**(2) (2026), 594–618, DOI `10.4153/S0008414X24000920`)
- **Audit date (UTC):** 2026-11-26T23:16Z
- **Isolation compliance:** Did not read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or author scratch notes; did not edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source Verbatim & Published-Version Check

### 1.1 Target Directory & Contest Status
`ls -la /Users/kev/Documents/open-math/targets/yip-2309.10950-rem3.1/` shows only:
- `PROOF.md`
- `TARGET.md`
- `verify.py`
- `notes/`

**No `CONTESTED.md` file exists** in `targets/yip-2309.10950-rem3.1/`.

### 1.2 arXiv Metadata (`arxiv_fetch.py`)
Command: `.venv/bin/python tools/arxiv_fetch.py query --id-list 2309.10950` (exit code `0`):
- `total_results`: `1`
- `id`: `2309.10950v2` (sole/latest version returned)
- `published`: `2023-09-19T22:19:25Z`
- `updated`: `2024-10-01T00:58:05Z`
- `authors`: `["Chi Hoi Yip"]`
- `categories`: `["math.NT", "math.CO"]`
- `comment`: `"23 pages,revised based on referee comments"`
- `journal_ref`: `"Can. J. Math.-J. Can. Math. 78 (2026) 594-618"`
- `doi`: `"10.4153/S0008414X24000920"`

### 1.3 Verbatim Extractions from `tools/.arxiv_cache/eprint/2309.10950/main.tex`

**(a) Exact definitions of $S_d$ and $A \hat{+} A$ (Section 1, lines 57 & 61):**
- Line 57:
  > Throughout the paper, let $p$ be an odd prime and $q$ a power of $p$. Let $\F_q$ be the finite field with $q$ elements. Let $d \mid (q-1)$ such that $d>1$. We denote $S_d(\F_q)=\{x^d: x \in \F_q^*\}$ to be the subgroup of $\F_q^*$ with order $\frac{q-1}{d}$. If $q$ is assumed to be fixed, for brevity, we simply write $S_d$ instead of $S_d(\F_q)$.
  
  Confirmed: $S_d \subset \F_q^*$, so **$0 \notin S_d$**.
- Line 61:
  > Recall that for a given set $A$, its \emph{restricted sumset} is given by $A \hat{+} A=\{a+b: a,b \in A, a \neq b\}$.

**(b) Section 1 `thm:VLM` and compiled numbering discrepancy in `TARGET.md`:**
In `main.tex`, lines 17–28 define `\newtheorem{thm}{Theorem}[section]` and share the `[thm]` counter across `lem`, `prop`, `cor`, `conj`, `defn`, `question`, `prob`, `rem`, `ex`. Enumerating all environments in Section 1 (`lines 55–120`):
- Line 63: `\begin{thm}\label{thm:main}` $\to$ **Theorem 1.1**
- Line 71: `\begin{thm}\label{thm:density}` $\to$ **Theorem 1.2**
- Line 77: `\begin{thm}\label{thm:square}` $\to$ **Theorem 1.3**
- Line 83: `\begin{thm}\label{thm: Sidon}` $\to$ **Theorem 1.4**
- Line 93: `\begin{cor}\label{cor:Siegel}` $\to$ **Corollary 1.5**
- Line 99: `\begin{thm}\label{thm:ub}` $\to$ **Theorem 1.6**
- Line 105: `\begin{thm}\label{thm:VLM}` $\to$ **Theorem 1.7**
- Line 114: `\begin{thm}\label{thm:integers}` $\to$ **Theorem 1.8**

Verbatim `thm:VLM` (`main.tex` lines 105–107):
> Let $d \geq 3$. Let $q \equiv 1 \pmod d$ be an odd prime power and a square. If $A \subset \F_q$ such that $A\hat{+}A \subset S_d \cup \{0\}$, then $|A| \leq \sqrt{q}$, with the equality holds if and only if $d \mid (\sqrt{q}+1)$ and $A=\alpha \F_{\sqrt{q}}$, where $\alpha \in S_d$.

**Discrepancy noted:** `TARGET.md` line 1 correctly refers to `Theorem 1.7 / thm:VLM`, and `PROOF.md` line 7 correctly identifies it as **Theorem 1.7**, whereas `TARGET.md` line 12 mislabels the blockquote as `**Theorem 1.5** (thm:VLM)`.

**(c) Section 3.2 Remark 3.3 (`main.tex` lines 405–407) and surrounding context:**
In Section 3 (`\section{Upper bounds on $|A|$ assuming $A\hat{+}A \subset S_d$}`), Subsection 3.2 (`\subsection{Proof of Theorem~\ref{thm:ub} and Theorem~\ref{thm:VLM}, and their implications to Cayley sum graphs}\label{subsec:Cayleysum}`, line 381) contains:
- Line 405–407 (`rem 3.3`, sharing the `[thm]` counter after `prop 3.1` at line 208 and `prop 3.2` at line 337):
  > \begin{rem}
  > Our analysis cannot handle the case $d=2$. In fact, there is $A \subset \F_9$ with size $4$ such that $A \hat{+} A \subset S_2 (\F_9) \cup \{0\}$, and there are $15$ different $A \subset \F_{25}$ with size $5$ such that $A \hat{+} A \subset S_2 (\F_{25}) \cup \{0\}$. Nevertheless, we conjecture that when $q$ is an odd square and $q \geq 49$, the statement of Theorem~\ref{thm:VLM} also extends to the case $d=2$.
  > \end{rem}

**Why Yip's proof of Theorem 1.7 failed for $d=2$:**
In `Proof of Theorem~\ref{thm:VLM}` (`main.tex` lines 393–403), when $A + A \not\subset S_d \cup \{0\}$, Yip invokes Proposition 3.2 (`prop: allow0`, lines 337–339), which uses Stepanov's method to give
$$|A| \le \sqrt{\frac{2(q-1)}{d} + 1} + 2.$$
For $d \ge 3$ and $q > 121$, $\sqrt{\frac{2(q-1)}{3} + 1} + 2 < \sqrt{q}$ (lines 396–399), eliminating the case $A+A \not\subset S_d \cup \{0\}$ when $|A| \ge \sqrt{q}$. When $d=2$, this bound collapses to $\sqrt{q - 1 + 1} + 2 = \sqrt{q} + 2 > \sqrt{q}$, which neither prevents $|A| > \sqrt{q}$ nor forces $A + A \subset S_2 \cup \{0\}$ when $|A| = \sqrt{q}$ (note Lemma 2.5 `lem: trivial` likewise gives only $|A| < \sqrt{q} + 3$ when $A\hat{+}A \subset S_d \cup \{0\}$).

**Other remarks/sections in `main.tex`:**
Checked the entire remainder of `main.tex` (lines 408–817):
- `rem 3.6` (`rem:EKR`, lines 423–427) discusses Corollary 3.5 (`cor:VLM`, $d \ge 3$) as an EKR theorem for $GPS(q, d)$ and notes Cayley sum graphs lose vertex-transitivity; it does not modify Remark 3.3.
- `rem 4.4` (lines 702–710) lists all $(q, A)$ with $A\hat{+}A = S_2$ ($q \in \{3, 7, 13\}$); unrelated to $A\hat{+}A \subset S_2 \cup \{0\}$ for square $q \ge 49$.
- No other remark or section modifies Remark 3.3.

### 1.4 Published Version Check (*Canad. J. Math.* 78(2) (2026), 594–618)
- Crossref API (`https://api.crossref.org/works/10.4153/S0008414X24000920`): confirms title `"Restricted sumsets in multiplicative subgroups"`, volume `78`, issue `2`, pages `594-618`, published online `2025-01-09` (2026 print issue), `update-to: None`.
- `arXiv:2309.10950v2` (`updated: 2024-10-01`, `"23 pages,revised based on referee comments"`) is the accepted/post-referee version matching the published *Canad. J. Math.* paper; web search results confirm Remark 3.3 remained an open conjecture unchanged in the published version.

### 1.5 Verification of Blokhuis (1984) Hypotheses
Literature check via `search_web` and Yip's own arXiv papers (`2309.10950v2` line 109 and `2505.04061v2` abstract):
- **A. Blokhuis**, *"On subsets of $GF(q^2)$ with square differences"*, *Indagationes Mathematicae* **46** (1984), 369–372 (also cited as *Proc. Kon. Ned. Akad. Wetensch. Ser. A* **87** (1984), 369–372).
- **Exact statement/hypotheses:** For **every odd prime power** $r$ (not restricted to primes $p$), if $A' \subset \mathbb{F}_{r^2}$ satisfies $|A'| = r$, $0, 1 \in A'$, and $A' - A' \subset S_2(\mathbb{F}_{r^2}) \cup \{0\}$, then $A' = \mathbb{F}_r$. (Equivalently, every clique of size $r$ in the Paley graph $P(r^2)$ is an affine line $\alpha \mathbb{F}_r + \beta$ with $\alpha \in S_2$).
- **Audit check on Case 1 of `PROOF.md` (line 56):** `PROOF.md` obtains $|A| = r$, $0 \in A$, $A - A \subset S_2 \cup \{0\}$, picks $\alpha \in A \setminus \{0\} \subset S_2$, and sets $A' := \alpha^{-1} A$ so that $0, 1 \in A'$, $|A'| = r$, $A' - A' \subset S_2 \cup \{0\}$. Blokhuis (1984) applies directly for all odd prime powers $r \ge 7$.

---

## 2. Deep Novelty / Prior-Art Search (Sept 2023 – Nov 26, 2026)

### 2.1 Local Watch Snapshots (`tools/novelty_grep.py`)
Command: `.venv/bin/python tools/novelty_grep.py 2309.10950 Yip "Paley sum" "van Lint" "GPS(q" "Blokhuis"`
- Matched 29 lines across 12/333 files in `watch/snapshots/**`:
  - `1337-solved-conjectures`: Asgarli–Ghioca–Yip blocking-pencil problem (`arXiv:2510.15332`, PRs #833, #865, issue #826) and Hajdu–Sárközy shifted-product/shifted-power conjectures (PRs #580, #576).
  - `plasma-ai__erdos`: `yip_2025_problem_erdos_ingham` (Erdős–Ingham problem).
  - `adamben04__open-conjectures.json`: links to `1337isnot1337` PRs #868, #865.
  - `watch/snapshots/arxiv/citing/yip-2309.10950-rem3.1.json` (checked `2026-11-26T22:55:40Z`): `citing_count: 0`, `citing_works: []`.
  - `watch/snapshots/arxiv/openalex_works_cache.json` (checked `2026-11-26T22:55:40Z`): `"2309.10950": {"openalex_id": null, "note": "not yet indexed in OpenAlex"}`.
- **0 hits** settling Remark 3.3 or $GPS(q, 2)$.

### 2.2 Competing GitHub Repositories & Global GitHub Search (Read-Only `gh`)
Checked via `gh api` (trees, issues, PRs) and `gh search issues` / `gh search code`:
1. **`aliromman/math`** (pushed `2026-11-26T23:11:22Z`, 102 tree items, 100 issues, 100 PRs): **0 hits** across tree, issues, PRs, and `gh search issues` for all terms (`2309.10950`, `Yip`, `Paley sum`, `van Lint`, `Blokhuis`, `restricted sumset`, `GPS(q`).
2. **`the-omega-institute/trureturing`** (pushed `2026-11-26T23:10:19Z`, 56,897 tree items) and **`the-omega-institute/trureturing-tools`** (pushed `2026-11-26T12:22:58Z`, 1,713 tree items):
   - `trureturing-tools`: **0 hits** in tree, 82 issues, 73 PRs.
   - `trureturing`: inspected `Blueprint/D5/S3/Combinatorics/PseudoPaley/TwoDimensionalCliques.md` (not found at `ref=dev` under raw path / matched Asgarli–Yip `2110.07176` Conjecture 5.9 on pseudo-Paley graphs $PP(p^4, p+1, I)$ in issue #14878) and `Blueprint/D5/S3/FiniteGroups/BhanjaRestrictedSumset/` (Bhanja 2025 Question 1 on elementary abelian 2-groups, issues #22373, #22427). `gh search issues --repo the-omega-institute/trureturing` also matched `2110.07176v5` Conjecture 1.4 (issue #22859), Nathanson `2607.20571v1` (issue #29804), and Erdős 203 (issue #9414). **0 hits** on `2309.10950`, `Paley sum`, `GPS(q`, or Remark 3.3.
3. **`1337isnot1337/solved-conjectures`** (pushed `2026-11-26T23:13:17Z`, 19,691 tree items):
   - Tree/issues/PRs hits for `Yip` are strictly: Asgarli–Ghioca–Yip blocking-pencil (`arXiv:2510.15332`, issues #826/#895, PRs #833/#865/#895), Erdős similarity (#532), Erdős bounded blocking-set (#803), and Hajdu–Sárközy (#416, #576, #580). **0 hits** on `2309.10950`, `Paley sum`, `van Lint`, `Blokhuis`, `GPS(q`, `restricted sumset`.
4. **`openai/math`** (pushed `2026-11-25T00:18:51Z`, 55,175 tree items, 6 issues, 6 PRs): **0 relevant hits** (only Fourier Littlewood–Paley files).
5. **Global GitHub `gh search code` & `gh search issues`**:
   - `"GPS(q, 2)"`, `"GPS(q,2)"`, `"restricted sumsets in multiplicative subgroups"`: **0 code hits, 0 issue hits**.
   - `"Paley sum"`: 0 code hits; 2 unrelated issue hits (`ESTEL-proj/estel#71`, `bguanmath/ArXiv_MathNT#85`).
   - `"van Lint-MacWilliams"`: 0 code hits; `the-omega-institute/trureturing#22859` (Asgarli–Yip `2110.07176v5` Conjecture 1.4), `lalalune/ArkLib` (unrelated).
   - `2309.10950`: `SlopDotCash/proximityprize` (`docs/kb/prize-407-exact-deltastar-kambire-conjecture.md`) and `lalalune/ArkLib#407` only list `arXiv:2309.10950` in a literature reading list on multiplicative subgroups / Stepanov's method.

### 2.3 arXiv, Zenodo, Crossref, Semantic Scholar, and Web Searches
- **arXiv API (`arxiv_fetch.py`):**
  - `au:"Chi Hoi Yip"` (`total_results: 77` entries, spanning through `2611.19824v1` on 2026-11-15). Inspected titles and downloaded/grepped eprints of the closest follow-ups:
    - `2505.04061v2` (*Van Lint-MacWilliams' conjecture and maximum cliques in Cayley graphs over finite fields, II*, 2025-05-07): Cayley graphs (differences $A-A \subset S \cup \{0\}$), **0 hits** for `2309.10950`, `GPS`, `Paley sum`, `Cayley sum`, `restricted sumset`.
    - `2503.09914v2` (*Cliques in Paley graphs of square order and in Peisert graphs*, 2025-03-13): **0 hits** for `2309.10950`, `GPS`, `Paley sum`, `Cayley sum`.
    - `2403.04312v2` (*Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs*, 2024-03-07): difference-based generalized Paley graphs.
    - `2405.09319v2` (*Paley-like quasi-random graphs arising from polynomials*, Kim–Yip–Yoo) & `2503.19603v3` (*$f$-Diophantine sets over finite fields...*, Kim–Yip–Yoo): discuss Paley sum graphs/hypergraphs as quasi-random families and lower bounds on clique/independence numbers, not the upper bound / equality classification for $GPS(q, 2)$.
    - `2607.25711v2` (*Multiplicative subgroups are not restricted sumsets*, Yip–Yoo, 2026-07-28) & `2608.02568v3` (*Additive decompositions of multiplicative subgroups via differential identities*, Cochrane–Yip–Yoo, 2026-08-03): classify $H = A \hat{+} A$ and $H \cup \{0\} = A \hat{+} A$ over **prime fields** $\mathbb{F}_p$; **0 hits** for `GPS`, `Paley sum`, `van Lint`, `VLM`, `Remark 3.3`, `2309.10950` in `.tex` grep.
  - `all:2309.10950` (1 hit: `2309.10950v2`), `all:"Paley sum"` (3 hits: `2503.19603v3`, `2405.09319v2`, `2204.08509v1`), `all:"restricted sumset" AND all:"multiplicative"` (6 hits: `2608.02568v3`, `2607.25711v2`, `2309.10950v2`, plus 2022/2011/2008 unrelated), `all:"van Lint-MacWilliams"` (3 hits: `2505.04061v2`, `2309.10950v2`, `2106.01522v2`).
- **Crossref & Semantic Scholar citations for `10.4153/S0008414X24000920`:**
  - Crossref: `is-referenced-by-count: 2`.
  - Semantic Scholar (`DOI:10.4153/S0008414X24000920`): `citationCount: 12` (Cochrane–Yip–Yoo `2608.02568`, Cochrane `2607.28559`, Yip–Yoo `2607.25711`, Yoo `2607.24370`, Rudnev–Tyrrell `2607.24270`, Kim–Yip–Yoo `2602.20919`, Kalmynin `2504.10202`, Yip `2501.16620`, Kim–Yip–Yoo `2309.09124`, plus 3 duplicate/uncurated entries). All address additive decompositions of multiplicative subgroups ($H = A+B$, $H = A\hat{+}A$) or multiplicative irreducibility of shifted subgroups; **none** address Remark 3.3 / $GPS(q, 2)$ maximum cliques for square $q \ge 49$. (OpenAlex `cites:W4406228052` reported `cited_by_count: 9` on initial fetch and returned HTTP 429 on follow-up pagination.)
- **Zenodo API:** `2309.10950` returned `0` results; broad phrase queries returned unrelated records.
- **Web searches (`search_web`):** 0 hits for any paper proving or refuting Remark 3.3 / $GPS(q, 2)$ for odd squares $q \ge 49$.

**Novelty conclusion:** No prior proof or refutation of Remark 3.3 was found across all checked sources as of `2026-11-26T23:16Z`.

---

## 3. Independent Exact Computation & Stress-Testing

### 3.1 Execution of `notes/check-check-2.py`
Command: `.venv/bin/python targets/yip-2309.10950-rem3.1/notes/check-check-2.py`
- **Exit code:** `0`
- **Exact raw output:**
```
F_25 non-coset size-5 clique Lemma 2.2 & 2.3 check: PASS ([(0, 1), (0, 4), (1, 0), (3, 1), (3, 4)])
r=7 (q=49) norm circles, S(theta), and explicit witnesses: PASS
r=9 (q=81) norm circles, S(theta), and ALL 8 z^10=-1 witnesses: PASS
r=11 (q=121) norm circles, Claim 2.4, eq (4), Hasse bound: PASS
Case 1 M^2 = qI - J check on F_25, F_49: PASS
PASS (all checks passed in 0.387s)
```

### 3.2 Independent Exact Exhaustive Checks

**(a) $\mathbb{F}_9$ ($r=3$) and $\mathbb{F}_{25}$ ($r=5$) — Yip's Remarks & Why Case 2 Fails:**
- **$\mathbb{F}_9 = \mathbb{F}_3[i]/(i^2+1)$:** Exhaustive search over all subsets confirms:
  - Cliques of size 3: `10`; size 4: `1`; size $\ge 5$: `0`.
  - The unique size-4 clique is $A = N_2(\mathbb{F}_9) = \{1+i, 1-i, -1+i, -1-i\}$, which has $|A_S| = 0$ and $|B| = 4$.
  - **Why Case 2 fails at $r=3$:** $K = (r-3)/2 = 0$, so Step 1 ($H_k$ construction for $0 \le k \le K$) and Step 2 ($2K > (r-1)/2$ to force $\max(\deg U, \deg V) \le 1$) fail immediately; furthermore, $A = N_2(\mathbb{F}_9)$ lies on the $c=0$ norm circle $N(b) = -1$ of size $r+1 = 4$, which is consistent with Subcase 3B(i)'s bound $|B| \le 4$.
- **$\mathbb{F}_{25} = \mathbb{F}_5[u]/(u^2-2)$:** Exhaustive branch-and-bound confirms:
  - Cliques of size 5: `15`; size $\ge 6$: `0`.
  - Exactly `3` are canonical cosets $\alpha \mathbb{F}_5$ ($\alpha \in S_2$, since $|S_2|/|\mathbb{F}_5^*| = 12/4 = 3$), and `12` are **non-coset size-5 cliques**.
  - All `12` non-coset size-5 cliques satisfy $A + A \not\subset S_2 \cup \{0\}$, $0 \notin A$, $|A_S| = 1$, and $|B| = 4$.
  - **Why Case 2 fails at $r=5$:** $K = (r-3)/2 = 1$, so $2K = 2 \not> (r-1)/2 = 2$: Lemma 2.3 inequality (2) ($\deg W + \max(\deg U, \deg V) \le 2$) fails to force $\max(\deg U, \deg V) \le 1$. Moreover, even when $B$ lies on a norm circle $N(b-c)=\lambda$ (exhaustively, for **all 12** non-coset cliques in $\mathbb{F}_{25}$, $B$ actually lies on the norm circle centered at $c = -a_0$ where $A_S = \{a_0\}$!), $|B| = r - 1 = 4$ is not ruled out by Subcase 3B(i) ($|B| \le 4$) or Subcase 3B(ii) (Hasse bound $\frac{5+1}{2} + \sqrt{5} \approx 5.236 \implies |C \cap N_2| \le 5$).

**(b) $\mathbb{F}_{49}$ ($r=7$) — Exhaustive Clique Search over All 49 Vertices:**
- Constructed $\mathbb{F}_{49} = \mathbb{F}_7[u]/(u^2 + 1)$ and the full adjacency graph of $GPS(49, 2)$ ($x \sim y \iff x \ne y,\, x+y \in S_2 \cup \{0\}$).
- Exhaustive exact branch-and-bound over all $49$ vertices (completed in `0.005s`):
  - Cliques of size $\ge 8$: `0`.
  - Cliques of size $7$: **`4`** total.
  - Canonical cosets $\alpha \mathbb{F}_7$ ($\alpha \in S_2$): $|S_2|/|\mathbb{F}_7^*| = 24/6 = 4$.
  - Set equality check confirmed the `4` cliques of size $7$ are **precisely** the `4` canonical cosets $\alpha \mathbb{F}_7$, with **zero non-coset cliques** of size $\ge 7$.

**(c) $\mathbb{F}_{81}$ ($r=9$) — Verbatim Check of `PROOF.md` Lines 241–260:**
- Constructed $\mathbb{F}_9 = \mathbb{F}_3[i]/(i^2+1)$ and $\mathbb{F}_{81} = \mathbb{F}_9[w]/(w^2 - (1+i))$ (with $S_2(\mathbb{F}_9) = \{1, -1, i, -i\}$ and $N_2(\mathbb{F}_9) = \{1+i, 1-i, -1+i, -1-i\}$).
- **Exact verification of all $S(\theta)$ values in `PROOF.md` lines 241–243:**
  - $\theta = -1$: $\tau(\tau^2 + 1)$ vanishes at $\tau \in \{0, i, -i\}$ and evaluates to $-1$ at $\tau \in \{1, 1+i, 1-i\}$ and $+1$ at $\tau \in \{-1, -1+i, -1-i\}$ (all $\in S_2(\mathbb{F}_9)$), giving $S(-1) = 6$.
  - $\theta = i$: $(1+i+\tau)(\tau^2 - i)$ vanishes at $\tau \in \{-1-i, 1-i, -1+i\}$, and at $\tau = 0, 1, -1, i, -i, 1+i$ takes exact values $1-i, -i, 1+i, 1, -1-i, 1-i$ with $\chi_{\mathbb{F}_9}$-values $-1, +1, -1, +1, -1, -1$, giving $S(i) = -2$ (and $S(-i) = -2$). Exact match to `PROOF.md` line 242.
  - $\theta = 1+i$: $(-1+i+\tau)(\tau^2 - 1 - i)$ vanishes at $\tau = 1-i$, and at $\tau = 0, 1, -1, i, -i, 1+i, -1+i, -1-i$ takes exact values $-1, 1, 1-i, 1, -1+i, 1+i, -1+i, -1+i$ with $\chi_{\mathbb{F}_9}$-values $+1, +1, -1, +1, -1, -1, -1, -1$, giving $S(1+i) = -2$ (and $S(1-i) = -2$, $S(-1+i) = S(-1-i) = 2$, so $|S(\theta)| = 2$ throughout the orbit). Exact match to `PROOF.md` line 243.
- **Exact verification on all 10 roots of $z^{10} = -1$ in $\mathbb{F}_{81}^*$:**
  - Found exactly `10` roots: `2` in $\mathbb{F}_9$ ($\pm i$) and `8` in $\mathbb{F}_{81} \setminus \mathbb{F}_9$.
  - For **all 8** roots $z \in \mathbb{F}_{81} \setminus \mathbb{F}_9$:
    - $b_1 = 1 + z$ and $b_2 = 1 + z^3$ are distinct elements of $C \cap N_2$ (with $N(b_k - 1) = -1$ and $b_k \in N_2$).
    - $\beta := z - z^{-1} \in \mathbb{F}_9^*$ satisfies $\beta^4 = -1$.
    - Exact equality $N(b_1 + b_2) = -\beta(\beta^2 + \beta + 1)$ holds for all 8 roots.
    - $N(b_1 + b_2)^4 = -1$, confirming $b_1 + b_2 \in N_2(\mathbb{F}_{81})$ for all 8 roots.

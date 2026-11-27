# Audit Helper Report: `targets/linusson-2512.24346-conj1/` (Linusson–Özdemir `arXiv:2512.24346v1`, Conjecture 1 `conj:complement`)

**Prepared by:** `linusson-audit-hlp` for `@audit-2`  
**UTC Date:** 2026-11-26T22:53Z  
**Isolation compliance:** Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or `notes/helper-linusson.md`; did NOT edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source Verbatim Verification (`arXiv:2512.24346v1`)

### 1.1 arXiv API Metadata Check
Command:
```bash
.venv/bin/python tools/arxiv_fetch.py query --id-list 2512.24346
```
Exact returned metadata:
- `id`: `2512.24346v1` (`total_results: 1`, sole version)
- `title`: `"The $k$-Plancherel measure and a Finite Markov Chain"`
- `authors`: `["Svante Linusson", "Alperen Özdemir"]`
- `published`: `2025-12-30T16:57:46Z`
- `updated`: `2025-12-30T16:57:46Z`
- `primary_category`: `math.CO` (`categories`: `["math.CO", "math.PR"]`)
- `comment`: `"22 pages"`
- `journal_ref`: `""`
- `doi`: `""`

### 1.2 Verbatim Extractions from `tools/.arxiv_cache/eprint/2512.24346/Kplancherel.tex`

#### (a) $(k+1)$-cores, $\mathfrak{p}$ and $\mathfrak{c}$ (§2.2, lines 115–121), Weak Order (Def 2.1, lines 148–161), Strong Marked Tableaux & $d_\lambda^{(k)}$ (§2.4, lines 194–219)
- **§2.2 Core partitions (lines 115–121):**
  > We say $\kappa$ is an \textit{$r$-core partition} if there is no cell with hook-length equal to $r$ in its Young diagram. Let us denote the set of $r$-core partitions by $\mathcal{C}_{r},$ and the set of all $k$-bounded partitions by $\mathcal{P}_k$. ...
  > \[ \mathfrak{p}: \, \kappa \rightarrow (\lambda_1,\ldots,\lambda_l) \in \mathcal{P}_k\]
  > where $\lambda_i$ is the number of cells with hook-length smaller than to $k+1$ in the $i$th row of $\kappa.$ This corresponds to removing all boxes with hook-length greater than $k+1,$ and then sliding all cells to the left of the diagram.
  > The inverse of $\mathfrak{p}$, let us call it $\mathfrak{c}$, can be described by a simple sequential process. We start from the top row, $\lambda_{l(\lambda)}$, and move down to the bottom row sequentially. We mark the hook-lengths in the row in the current stage, say $\lambda_i \text{ for } i\leq l$. If we have a box with hook-length greater than or equal to $k+1$ in $\lambda_i$ we add boxes to the left of the diagram to all rows $\lambda_1,\ldots,\lambda_i$ until all cells already-present in $\lambda_i$ have hook-lengths less than or equal to $k.$
- **§2.3 Definition 2.1 (`\label{weak order}`, lines 148–150) & bounded-partition weak cover (lines 158–161):**
  > \begin{definition} \text{(Weak order)} \label{weak order}
  > Let $\tau$ and $\kappa$ be $(k+1)$-cores. We say $\kappa$ precedes $\tau$ in the weak order, denoted by $\kappa \rightarrow_k \tau$ if and only if all cells in $\tau \setminus \kappa$ have the same content modulo $(k+1)$.
  > \end{definition}
  (And lines 158–161 define $\lambda \rightarrow_k \mu$ on $\mathcal{P}_k$ iff $|\mu|=|\lambda|+1, \lambda \subseteq \mu \text{ and }\lambda^{\omega_k} \subseteq \mu^{\omega_k}$.)
  *Audit note:* Line 149 omits writing $\kappa \subsetneq \tau$ explicitly, though $\tau \setminus \kappa$ and the bounded-partition definition ($|\mu|=|\lambda|+1$, $\lambda \subseteq \mu$) require $\kappa \subsetneq \tau$, which `PROOF.md` (line 113) states explicitly.
- **§2.4 $k$-tableaux (lines 194–219):**
  - Lines 194–196: strong marked cover $(\kappa, \tau, c)$ iff $\kappa \Rightarrow_k \tau$ and $c$ is the content of the southeast-most cell of a connected component of $\kappa \setminus \tau$.
  - Definition `\ref{def:tab}` (lines 199–209): strong marked tableau of shape $\lambda \vdash n$ and weight $\beta = (\beta_1,\ldots,\beta_d)$ ($\sum \beta_i = n$) is a chain $\emptyset = \kappa^{(0)} \Rightarrow_k \kappa^{(1)} \Rightarrow_k \cdots \Rightarrow_k \kappa^{(n)} = \mathfrak{c}(\lambda)$ with markings $\{c_1,\ldots,c_n\}$ satisfying $c_{A_i+1} < c_{A_i+2} < \cdots < c_{A_i+\beta_{i+1}}$.
  - Lines 210–219 (`\eqref{strongkostka}`, `\eqref{strongdim}`):
    > \[s_{\lambda}^{(k)}[X]=\sum_{T \text{ is Strong}(\mathfrak{c}(\lambda))} x^T\]
    > ...
    > \[s_{\lambda}^{(k)}=\sum_{\mu }\mathbf{K}_{\lambda \mu}^{(k)} m_{\mu}\]
    > ...
    > \begin{equation}\label{strongdim}
    >   d_{\lambda}^{(k)}:= [x_1 x_2 \cdots x_n] s_{\lambda}^{(k)}(x).
    > \end{equation}
  (Line 622 also explicitly notes $d_\lambda^{(k)} = \mathbf{K}_{\lambda, (1,\cdots,1)}^{(k)}$.)

#### (b) Pieri rule (§3.2), $k$-rectangle property (§3.3), $\mathcal{R}_k$ and $P(\lambda,\mu)$ (§3.3, lines 299–312, $k=1$ and $k=2$)
- **§3.2 Pieri rule (lines 281–290):**
  > \[h_1 s_{\lambda}^{(k)} = \sum_{\lambda \to_k \Lambda} s_{\Lambda}^{(k)}.\]
  > See Section 2.2 of \cite{LLMSSZ14}.
  And eq. `\eqref{inftrans}` (line 289): $P(\lambda,\Lambda) = \frac{d_\Lambda^{(k)}}{(n+1)d_\lambda^{(k)}}$ for $|\lambda| = n$.
- **§3.3 $k$-rectangle property & Lapointe–Morse citation (lines 299–302):**
  > Let $\square_i$ denote the partition $(i,i,\ldots,i)$ with $k-i+1$ parts for $i=1,\ldots,k.$ We have the following property of $k$-Schur functions: \\
  > \noindent \textbf{$k$-rectangle property} (Theorem 40 of \cite{LM07}): For any partition $\lambda \in \mathcal{P}_k$ and $i \in [k],$
  > \[s_{\square_i} s^{(k)}_{\lambda} = s^{(k)}_{\lambda \cup \square_i}. \]
- **§3.3 $\mathcal{R}_k$ and $P(\lambda,\mu)$ (lines 304–312):**
  > \[\mathcal{R}_k:=\{\lambda \in \mathcal{P}_k \, : \, l_i(\lambda)\leq k-i \text{ for all } i=1,\ldots,k\}. \]
  > Since $|\mathcal{R}_k|=k!$, we obtain a Markov chain on $k!$ partitions, and the transition probability for any $\lambda,\mu \in \mathcal{R}_k$ is given by
  > \[P(\lambda,\mu)= \frac{1}{ |\lambda|+1} \times \begin{cases}
  >   d_{\mu}^{(k)} \slash d_{\lambda}^{(k)} & \text{ if  }\lambda \rightarrow_k \mu, \\
  >     d_{\Lambda}^{(k)} \slash d_{\lambda}^{(k)} & \text{ if  }\lambda \rightarrow_k \Lambda = \mu \cup \square_i \text{ for some }i \in [k],\\
  >     0  & \text{ otherwise}.
  > \end{cases}\]
- **Check of $k=1$ and $k=2$:**
  - **$k=1$:** $\mathcal{R}_1 = \{\emptyset\}$ ($|\mathcal{R}_1| = 1! = 1$), $\square_1 = (1)$, $\emptyset \to_1 (1) = \emptyset \cup \square_1$, $P(\emptyset,\emptyset) = \frac{d_{(1)}^{(1)}}{(0+1)d_\emptyset^{(1)}} = 1$. Note `Kplancherel.tex` line 633 specifies `for a fixed $k\geq 2$` in the $k$-conjugation proof, while `conj:complement` (line 644) has no explicit $k \ge 2$ qualifier; `PROOF.md` line 43 handles $k=1$ separately.
  - **$k=2$:** $\mathcal{R}_2 = \{\emptyset, (1)\}$. From $\lambda = (1)$, there are **two distinct** weak covers: $(1) \to_2 (1,1) = \emptyset \cup \square_1$ and $(1) \to_2 (2) = \emptyset \cup \square_2$, both projecting via $\mathrm{red}_2$ to $\mu = \emptyset$. The `cases` formula in `Kplancherel.tex` lines 307–311 fails to sum over multiple $\Lambda$ projecting to the same $\mu$ (each branch gives $1/2$), whereas the projected Markov chain from §3.2 sums both transitions to $P((1), \emptyset) = 1/2 + 1/2 = 1$. `PROOF.md` (lines 12–13) explicitly formulates $P(\lambda,\mu)$ as a sum over all $\lambda \to_k \Lambda$ with $\mathrm{red}_k(\Lambda) = \mu$, notes this $k=2$ collision explicitly, and proves in Lemma 3(2) that for all $k \ge 3$ at most one weak cover projects to a given $\mu \in \mathcal{R}_k$.

#### (c) Line 517, Section 3.4 `conj:complement` (lines 641–645), and Prior Proof/Mention Check
- **Line 517 verbatim:**
  > Note that it follows directly from the description of $\alpha^{-1}$ that  $\alpha^{-1}(\lambda^{\omega_k})$ is obtained by reversing the order of the elements of $\alpha^{-1}(\lambda)$, but keeping $(k+1)$ fixed.
  *Verification of `PROOF.md` line 76 remark:* Confirmed — `Kplancherel.tex` line 517 indeed prints $\lambda^{\omega_k}$ ($k$-conjugate) where $\lambda^{\mathrm{comp}}$ ($k$-complement) is meant. For example, at $k=4$, lines 657–668 pair $\emptyset$ (`1234[5]`) with $\emptyset^{\mathrm{comp}} = (3,2,2,1,1,1)$ (`4321[5]`) and $(1)$ (`2341[5]`) with $(1)^{\mathrm{comp}} = (3,2,2,1,1)$ (`1432[5]`), which are cyclic reversals fixing $5$; meanwhile $\emptyset^{\omega_4} = \emptyset$.
- **Section 3.4 `conj:complement` (lines 641–645) verbatim:**
  > For a $\lambda\in\mathcal{R}_k$, let $\lambda^{\mathrm{comp}}\in\mathcal{R}_k$ be such that 
  > $\lambda \cup \lambda^{\mathrm{comp}} = (k-1,(k-2)^2,\ldots,i^{k-i},\ldots,2^{k-2},1^{k-1})$, that is $l_i(\lambda)+l_i(\lambda^{\mathrm{comp}})=k-i$.
  >  \begin{conjecture} \label{conj:complement}\mathrm{(Symmetry of complements)}
  >    For all $\lambda\in\mathcal{R}_k$, $\pi(\lambda)=\pi(\lambda^{\mathrm{comp}}).$
  > \end{conjecture}
- **Irreducibility, $R$-reversibility, or $w(\lambda)$ in `Kplancherel.tex`:**
  - `grep -inE "irreduc|ergod|reversib|detailed|balance|stationary|complement" Kplancherel.tex`: **0 occurrences** of `irreduc*`, `reversib*`, `detailed`, or `balance`. Line 703 invokes `By the Ergodic Theorem` without proving irreducibility of the finite $k$-chain.
  - Line 73 explicitly states: `For the finite $k$-chain we conjecture that there is also another involution which we call $k$-complementation (reverses the permutation in TASEP). It has no fix points and matches states that seem to have the same stationary probability, but for no apparent reason, see Conjecture \ref{conj:complement}.`
  - Neither $R$-reversibility nor $w(\lambda) = d_\lambda^{(k)} d_{\lambda^{\mathrm{comp}}}^{(k)} / (|\lambda|! |\lambda^{\mathrm{comp}}|!)$ is mentioned anywhere in `Kplancherel.tex`.

### 1.3 External Citation Verification (`LM07` and `LLMSSZ14`)
- **Lapointe–Morse (2007):**
  - Crossref + `kcore.bib` (`LM07`) + `arXiv:math/0505519v1` (`tools/.arxiv_cache/eprint/math_0505519/paper.tex`):
  - **Journal correction:** `LM07` in `Kplancherel.tex` (`kcore.bib`) is *"A $k$-tableau characterization of $k$-Schur functions"*, **Advances in Mathematics** 213(1) (2007), 183–204 (DOI `10.1016/j.aim.2006.12.005`, `arXiv:math/0505519v1`) — **not** *J. Amer. Math. Soc.* 20. (`PROOF.md` line 62 writes `Lapointe–Morse 2007, Theorem 40; cited in Kplancherel.tex §3.3, line 300`, so `PROOF.md` does not contain the JAMS error.)
  - Counting theorem-counter environments in `math/0505519/paper.tex` (`\newtheorem` environments share one counter), line 2160 is exact **Theorem 40**:
    > For any $k$-rectangle $\square$ and $k$-bounded partition $\mu$, we have
    > `s_\square s_\mu^{(k)} = s_{\mu \cup \square}^{(k)}.`
    (At $t=1$, matching `PROOF.md` line 63.)
- **Lam–Lapointe–Morse–Schilling–Shimozono–Zabrocki (2014):**
  - Crossref (`DOI 10.1007/978-1-4939-0682-6`, Chapter 2 DOI `10.1007/978-1-4939-0682-6_2`) + `arXiv:1301.3569v2` (*"$k$-Schur functions and affine Schubert calculus"*, Fields Institute Monographs 33, Springer, 2014).
  - In Chapter 2 (`notes-mike-anne.tex`, `\chapter{Primer on $k$-Schur Functions}`), Section 2 (`From Pieri rules to $k$-Schur functions`), Subsection 2.2 (`Weak tableaux and a monomial expansion of dual $k$-Schur functions`, line 2223), eq. `\eqref{eq:kweakpieri}` (lines 2263–2272) defines the $k$-Schur functions at $t=1$ via the weak Pieri rule $h_r s_\mu^{(k)} = \sum_\lambda s_\lambda^{(k)}$ summed over weak horizontal strips $\mathfrak{c}(\lambda)/\mathfrak{c}(\mu)$ of size $r$; for $r=1$, weak horizontal strips of size $1$ are weak covers $\mu \to_k \lambda$, giving $h_1 s_\lambda^{(k)} = \sum_{\lambda \to_k \Lambda} s_\Lambda^{(k)}$ (as in `Kplancherel.tex` line 282 and `PROOF.md` line 59).

---

## 2. Deep Novelty Check (Dec 2025 – Nov 2026)

| Source | Exact Query | Result |
|---|---|---|
| `tools/novelty_grep.py` (`watch/snapshots/**`) | `2512.24346 Linusson Ozdemir "k-Plancherel" "conj:complement"` | `# 0 lines across 0/277 files in 0.63s` |
| arXiv API (`tools/arxiv_fetch.py query`) | `all:2512.24346 OR all:"k-Plancherel"` | `total_results: 1` (`2512.24346v1` itself) |
| Zenodo API (`zenodo.org/api/records`) | `2512.24346`; `"k-Plancherel"`; `Linusson AND Plancherel`; `Ozdemir AND Plancherel`; `conj:complement` | `0`, `1` (unrelated 2014 Boehmians), `0`, `0`, `0` |
| GitHub (`gh search repos/code/issues`) | `2512.24346`, `k-Plancherel`, `kcore-chain`, `conj:complement`, `Linusson k-Plancherel`, `Ozdemir k-Plancherel` | Only `alp-oz/kcore-chain` (authors' computation repo) and `AlexenderSokolov/cross-theory-formal-database` (`triangle-lemma` benchmark extraction from `2512.24346v1`); no proof of `conj:complement` |
| GitHub (`the-omega-institute/trureturing` & `trureturing-tools`) | `2512.24346 OR Linusson OR Ozdemir OR Plancherel OR kcore` | 0 code hits, 0 issue hits |
| GitHub (`aliromman/math`) | Code, issues, and all PRs (`state=all`, pages 1–2) for `2512.24346`, `linusson`, `ozdemir`, `plancherel`, `kcore`, `complement` | 0 code hits, 0 issue hits, 0 matching PRs |
| Web search (`search_web`) | `"2512.24346" OR ("k-Plancherel" "Linusson" "Markov") proved OR stationary OR complement` | Returns only `arXiv:2512.24346` itself |

### Inspection of `alp-oz/kcore-chain` (read-only `gh api`)
- Repo metadata: `default_branch: main`, `pushed_at: 2026-04-02T08:43:29Z`, description `"Computation of the Markov chain on k-bounded partitions associated with the k-Plancherel measure (arXiv:2512.24346)"`.
- Root files: `README.md` (1305 B), `kcore_chain.py` (13702 B), `Data/`.
- `Data/stationary_distributions/`: `stationary_distribution_k{3,4,5,6}.csv` (65 B, 360 B, 1800 B, 10800 B).
- `Data/transition_matrices/`: `transition_matrix_k{3,4,5,6}.csv` (510 B, 8088 B, 201720 B, 7258320 B).
- `kcore_chain.py` only computes exact transition matrices on $\mathcal{R}_k$ using `kschur_dim`, `bounded_to_core`, `core_to_bounded`, `content_partition`, and `reduce_to_Rk`. Contains **only code and numerical CSV data**, no proof or formula for $\pi(\lambda)$ or Conjecture 1.

**Novelty conclusion:** Clean; no proof or disproof of Conjecture 1 (`conj:complement`) found anywhere.

---

## 3. Independent Computational Verification

### 3.1 Re-run of `notes/check-check-2.py`
Command:
```bash
.venv/bin/python -u targets/linusson-2512.24346-conj1/notes/check-check-2.py
```
Exit code: `0`. Exact raw output:
```text
k=1 (|R_1|=1, Z_1=1): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
k=2 (|R_2|=2, Z_2=2): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
k=3 (|R_3|=6, Z_3=5/3): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
k=4 (|R_4|=24, Z_4=35/432): Lemmas 1-4, R-reversibility, stationarity, Conj 1 PASS
k=5 (|R_5|=120): Lemmas 2 & 4 PASS
PASS (all checks passed in 0.034s)
```

### 3.2 In-Memory Exhaustive Checks on Lemma 3(1) and Lemma 4 ($k = 2, 3, 4, 5$)
Executed via `.venv/bin/python -c '...'` directly from the primary-source definitions ($\mathfrak{p}, \mathfrak{c}$, Definition 2.1 weak covers on $(k+1)$-cores checking all nonempty subsets of addable corners of a given residue mod $k+1$ for $(k+1)$-core validity, Maya diagram minima $b_1 < \dots < b_{k+1}$, and the exact constructive 3-phase algorithm of `PROOF.md` lines 150–152):
- **Lemma 3(1) part-count updates & exact rectangle-drop characterization** ($l_i(\Lambda)=l_i(\lambda)+1$, $l_{i-1}(\Lambda)=l_{i-1}(\lambda)-1$ for $i\ge 2$, $l_m(\Lambda)=l_m(\lambda)$ otherwise; $\Lambda = \mu \cup \square_i \iff j = i+1$, $\Lambda = \mu \in \mathcal{R}_k \iff j \ge i+2$):
  - `k=2`: all `2` states and `3` weak covers verified (`0` failures).
  - `k=3`: all `6` states and `12` weak covers verified (`0` failures).
  - `k=4`: all `24` states and `60` weak covers verified (`0` failures).
  - `k=5`: all `120` states and `360` weak covers verified (`0` failures).
- **Lemma 4 constructive paths** ($\sigma \to^* \mathrm{id} \to^* \omega_0 \to^* \tau$ via the exact algorithm in `PROOF.md` lines 150–152, verifying every step is a legal TASEP swap):
  - `k=2`: all `2` states verified (max path length `2`).
  - `k=3`: all `6` states verified (max path length `7`).
  - `k=4`: all `24` states verified (max path length `16`).
  - `k=5`: all `120` states verified (max path length `30`).

# Adversarial Audit Helper Report: `targets/gaetz-2512.08168-conj1/`

**Target:** Christian Gaetz and Yibo Gao, *"Billey--Postnikov posets, rationally smooth Schubert varieties, and Poincar\'{e} duality"*, `arXiv:2512.08168v2` (`math.CO`, `math.AG`), Conjecture 1.3 (`conj:union-intersection`).  
**Date (UTC):** 2026-11-26  
**Isolation:** Did not read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or author scratch notes; did not edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source & Version Check

- **arXiv API query (`.venv/bin/python tools/arxiv_fetch.py query --id-list 2512.08168`):**
  - **Latest/sole active record:** `2512.08168v2`, published `2025-12-09T01:51:50Z`, updated `2026-06-08T17:10:02Z`.
  - **Submission history (`tools/.arxiv_cache/abs/2512.08168.html`):** `[v1]` `Tue, 9 Dec 2025 01:51:50 UTC (27 KB)`, `[v2]` `Mon, 8 Jun 2026 17:10:02 UTC (28 KB)`.
  - **Comment:** `"v2: minor edits and corrections. We thank Jan Petr, Anne Thomas, and Pavel Turek for pointing out a mistake in the definition of \"Lehmer code\" in v1"`.
  - **Journal ref / DOI:** Both empty (`""`).
- **Directory listing (`ls -la targets/gaetz-2512.08168-conj1/`):**
  - Contains `PROOF.md`, `TARGET.md`, `verify.py`, and `notes/`. **No `CONTESTED.md` is present.**
- **Inspection of `tools/.arxiv_cache/eprint/2512.08168/main.tex`:**
  - **(a) Exact Conjecture numbering:** In Section 1.1 (`main.tex` lines 95–116), all theorem-like environments share the `theorem` counter (`\newtheorem{theorem}{Theorem}[section]`). Theorem 1.1 is `thm:intro-bp-pattern-characterization`, Theorem 1.2 is `thm:intro-union-intersection`, and **Conjecture 1.3** (`conj:union-intersection`, lines 113–116) reads verbatim:
    > *Let $W$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K, J \cup K \in \mathrm{BP}(w)$.*
    *(Side note on `TARGET.md` citation accuracy: `TARGET.md` line 29 writes `"Theorem 3.7 / Section 3.3"` for the rank-$\le 3$ case, whereas in `main.tex` `3.7` is `Definition 3.7` (`def:BP-poset`) in Section 3.3 (`sub:bp-properties`), and the rank-$\le 3$ theorem is **Theorem 3.15** (`thm:rank-three-union-intersection`, lines 463–466) in **Section 3.5** (`\subsection{BP posets for groups of rank three}`, `\label{sec:rank-three}`).)*
  - **(b) Arbitrariness of $(W, S)$ (including infinite rank $|S|$):** In Section 2.1 (`main.tex` lines 191–192), Gaetz–Gao define: *"Let $W$ be a Coxeter group with simple reflection set $S$. We refer the reader to \cite{bjorner-brenti} for background and notation on Coxeter groups."* Neither Section 1.1 nor Section 2.1 restricts $|S|$ to be finite; Björner–Brenti allows arbitrary Coxeter systems $(W, S)$ (finite or infinite $|S|$, though every $w \in W$ has finite support $\mathrm{Supp}(w) \subseteq S$). `PROOF.md` handles arbitrary $|S|$ (using finite words $\mathbf{a} \in S^*$), and notes only binary intersection/union closure in $\mathrm{BP}(w) \subseteq 2^S$ (which matches Conjecture 1.3).
  - **(c) What Gaetz–Gao already proved & why `conj:union-intersection` was left open:**
    - In Section 3.1–3.2 (`main.tex` lines 274–368), Gaetz–Gao prove `Theorem 1.2` (`thm:intro-union-intersection`) **only for finite Weyl groups**, via $J$-star pattern avoidance (`Theorem 1.1` / `thm:intro-bp-pattern-characterization`) in finite crystallographic root systems $\Phi$. Specifically, `Lemma 3.2` (`lem:simple-Jstar`) uses classical finite-type case analysis plus exhaustive computer checks on $F_4, E_8$, and `Lemma 3.5` (`lem:union-helper-decomposition`) reduces classical types to finite computer checks up to $B_9, C_9, D_{10}, E_8, F_4, G_2$. Gaetz–Gao explicitly remark at line 100: *"It is not clear how one could prove \Cref{thm:intro-union-intersection} directly from the geometric or Coxeter-theoretic characterizations of BP decompositions."* That $J$-star finite-root-system method does not apply to non-crystallographic or infinite Coxeter groups.
    - In Section 3.5 (`main.tex` lines 460–480, `Theorem 3.15`), they prove `conj:union-intersection` for arbitrary Coxeter groups of **rank $\le 3$** using an ad-hoc reduced-word / braid-move / interlacing argument.
    - Gaetz–Gao cite Richmond–Slofstra (`1408.0084`, *Math. Ann.* 2016) for `Proposition 2.2` (`prop:bp-iff-rgf`, Poincaré polynomial factorization), `Proposition 4.3` (associativity for nested $I \subseteq J \subseteq K$, cited in `Prop. 4.2` / `prop:bp-of-wJ-is-order-ideal`), `Prop. 4.2` (product interval `[e, w^J]^J x [e, w_J] -> [e, w]`, cited as `Prop. 5.2` / `prop:BP-gives-subposet-product`), `Thm. 3.3` (`prop:wJ-rs`), `Thm. 3.6` (`thm:rs-implies-gr-bp`), and `Conj. 6.5` (`conj:infinite-type-grassmannian-bp`, which Gaetz–Gao disprove in `Theorem 1.10` / `Theorem 6.2` (`thm:counterexample`) via $w = srstrsr$ in $\widetilde{C}_2$). They do **not** have a Richmond–Slofstra reference for union/intersection closure of $\mathrm{BP}(w)$.

---

## 2. Deep Novelty / Prior-Art Search

### A. Local Watch Snapshots (`watch/snapshots/**`)
- Command: `.venv/bin/python tools/novelty_grep.py --max-per-file 0 --max-total 0 2512.08168 Gaetz "Billey-Postnikov" "Billey--Postnikov" "union-intersection" "BP(w)"`
- Output: **24 lines across 9/356 files in 1.15s**:
  1. `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json`: `citing_count: 0`, `citing_works: []` (`checked_utc: 2026-11-26T22:55:34Z`).
  2. `watch/snapshots/arxiv/openalex_works_cache.json`: `"2512.08168": {"openalex_id": null, "note": "not yet indexed in OpenAlex"}`.
  3. `watch/snapshots/arxiv/index.md`, `cat_math.CO.json`, `recent_arxiv.json`: Gaetz & Gao's later preprint `2611.33572v1` (*Reflection subgroups and the Lookup Conjecture*, 2026-11-25). Inspection of `tools/.arxiv_cache/eprint/2611.33572/lookup.tex` confirms it studies Boe–Graham's Lookup Conjecture via reflection-subgroup slices and does **not** cite `2512.08168` or mention $\mathrm{BP}(w)$ / Billey–Postnikov decompositions.
  4. `watch/snapshots/discovered/MattiaCalzavara__gaetz-gao-conjecture-proof.json` (and `CATALOG.md`, `catalog.json`): unrelated Gaetz–Gao conjecture on strong $q$-log-concavity.
  5. `watch/snapshots/discovered/the-omega-institute__trureturing-tools.json` (`tools/scripts/agent/openproblem/SCREENED-OUT-R52.md`, line 401):
     > `- 已结算:arXiv:2512.15486 Conjecture 1 仓内已反驳并冻结(PanchromaticPairingConjectureRefutation);arXiv:2512.20494 link-irregular 竞赛图猜想已占(仓内卷宗);arXiv:2512.08168 Conjecture 1.9 由同文 Theorem 6.2 首个反例;arXiv:2512.02314 Question 6.2 由同文 Figure 11 否定。`
     - **Confirmed 100%:** This entry refers solely to **Conjecture 1.9** (`conj:infinite-type-grassmannian-bp`, disproved by Gaetz–Gao's own Theorem 6.2 / Theorem 1.10 in `2512.08168`), **not** Conjecture 1.3 (`conj:union-intersection`).

### B. Target GitHub Repositories & Global GitHub (Read-Only)
- Inspected local snapshots (`watch/snapshots/1337-solved-conjectures/**`, `KnowledgeSense__math.json`, `the-omega-institute__trureturing.json`): **0 hits** for `2512.08168`, `Billey`, `BP(w)`, `union-intersection`.
- Queried GitHub trees (`gh api repos/<owner>/<repo>/git/trees/HEAD?recursive=1`) for `aliromman/math` (241 files, 0 keyword hits), `KnowledgeSense/math` (5,377 files, 0 keyword hits), `1337isnot1337/solved-conjectures` (19,697 files, 0 keyword hits), `the-omega-institute/trureturing-tools` (1,713 files, 0 keyword hits), `the-omega-institute/trureturing` (56,896 files, `truncated: True`; Coxeter hits were only `BoerdijkCoxeterGeneratingFunctions`, `CFMPCoxeterIndexObstruction`, `ElekMagicWordConverseRefutation`).
- Ran `gh search code` across all 5 repos (`aliromman/math`, `KnowledgeSense/math`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `1337isnot1337/solved-conjectures`) for `"2512.08168"`, `"Billey-Postnikov"`, `"Billey--Postnikov"`, `"union-intersection"`, `"BP(w)"`: **0 results** (`[]`).
- Ran global `gh search issues` and `gh search repos` for `2512.08168`, `Billey-Postnikov`, `Gaetz`: the only `2512.08168` issue was `the-omega-institute/trureturing#7333` (the standing R52/C7 screening lane referencing `SCREENED-OUT-R52.md` above, i.e., Conjecture 1.9); no repos or issues address Conjecture 1.3 or $\mathrm{BP}(w)$ union/intersection closure. (Global `gh search code` returned generic matches like `eruditeandroid/CAAGnotes` notes on the 2002 Billey–Postnikov KL-height conjecture.)

### C. arXiv, Zenodo, Crossref, Web, and Classical Coxeter Literature
- **arXiv queries (`tools/arxiv_fetch.py query`):**
  - `'all:"Billey-Postnikov"'` -> 8 results (`2512.08168v2`, `2409.03096v1`, `2303.13695v2`, `2007.08490v1`, `1807.04879v3`, `1510.06060v1`, `1408.0084v2`, `1312.7540v2`).
  - `'au:Richmond AND au:Slofstra'` -> 6 results (`2103.08114v2`, `1808.05918v1`, `1702.02236v1`, `1510.06060v1`, `1408.0084v2`, `1206.5746v3`).
  - `'au:Gaetz AND au:Gao'` -> 19 results (newest: `2611.33572v1` Nov 25 2026 and `2610.22857v1` Oct 16 2026). Inspection of `2610.22857/separable3.tex` confirms it studies intersections of weak-order intervals $[e,x]_L \cap [e,y]_R$ for separable elements and does not mention `2512.08168` or $\mathrm{BP}(w)$.
  - `'all:"2512.08168"'` -> 0 results.
- **Zenodo (`https://zenodo.org/api/records`) & Crossref (`https://api.crossref.org/works`):**
  - Zenodo `'2512.08168'`: `total=0`. Queries for `'Billey-Postnikov'`, `'BP(w) Coxeter'`, `'Gaetz Gao Billey-Postnikov'` returned 0 relevant mathematical records.
  - Crossref `'Billey-Postnikov'`: returned Oh–Richmond (`10.1201/9781003145127-12`, 2026), Richmond–Slofstra (`10.1007/s00208-015-1299-4`, 2015/2016), Billey–Postnikov (`10.1016/j.aam.2004.08.003`, 2005); no papers proving union/intersection closure of $\mathrm{BP}(w)$.
- **Web (`search_web`):** Multiple queries (`"2512.08168" OR "Billey-Postnikov posets" OR "conj:union-intersection"`, `"Gaetz" "Gao" "Billey-Postnikov" 2026`, etc.) returned only `arXiv:2512.08168` itself; no 2025–2026 citations or solutions found. *(Note: Semantic Scholar and OpenAlex direct API calls returned HTTP 429 rate-limit errors during this session, though `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json` already recorded `citing_count: 0` on 2026-11-26T22:55:34Z.)*
- **Classical Richmond–Slofstra & Oh–Richmond primary-source check (downloaded & inspected TeX):**
  - Note: IDs `1409.5912`, `1506.03892`, `1705.05962`, `2006.10164` on arXiv are unrelated papers (materials science / quantum graphs / bioengineering / numerical linear algebra). The actual Richmond–Slofstra / Oh–Richmond BP papers are:
    1. **Richmond & Slofstra (2016), `arXiv:1408.0084v2` (`bpgeom.tex`, *Math. Ann.* 366):** Defines BP decompositions with respect to $(J, K)$, proves combinatorial characterizations (`Prop. 4.2` / `P:bplemma`: $S(v) \cap K \subseteq D_L^J(u)$ and `L:maxexist`: unique maximum $\bar u \in [e,w] \cap W_K^J$, stated for arbitrary Coxeter groups $W$), and proves associativity for nested $I \subseteq J \subseteq K \subseteq S$ (`L:bpassoc`). Does **not** study $\mathrm{BP}(w)$ as a poset/lattice or prove closure under $J \cap K$ or $J \cup K$.
    2. **Slofstra (2015), `arXiv:1312.7540v2` (`os3.tex`, *Adv. Math.* 285):** Studies chain BP decompositions and modular coatoms of inversion hyperplane arrangements in finite Weyl/Coxeter groups; does not consider $\mathrm{BP}(w)$ union/intersection closure.
    3. **Richmond & Slofstra (2017), `arXiv:1510.06060v1` (`bpenum.tex`, *JCTA* 150):** Defines $\mathsf{bp}(w) := \{s \in S \mid w \text{ BP at } S \setminus \{s\}\}$ (only maximal proper subsets) and staircase diagrams for elements with complete BP decompositions; does not study $\mathrm{BP}(w)$ closure under $\cap, \cup$.
    4. **Oh & Richmond (2024), `arXiv:2409.03096v1` (`mainfile.tex`):** Survey chapter on BP decompositions, hyperplane arrangements, staircase diagrams, and split-pattern avoidance; does not state or prove union/intersection closure of $\mathrm{BP}(w)$.
  - **Conclusion on Novelty:** Conjecture 1.3 (`conj:union-intersection`) for arbitrary Coxeter groups has **not** been proved in print prior to `2512.08168` nor in any 2025–2026 source found.

---

## 3. Independent Exact Computation & Stress-Testing

### A. Execution of `check-check-3.py`
Command: `time .venv/bin/python /Users/kev/Documents/open-math/targets/gaetz-2512.08168-conj1/notes/check-check-3.py`
- **Exit code:** `0`
- **Runtime:** `19.826s` wall (`13.69s user 0.99s system 74% cpu`)
- **Exact raw output:**
```
A_3 PASS: verified 24 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
B_3 PASS: verified 48 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
H_3 PASS: verified 120 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
tilde_C_2(len<=7) PASS: verified 76 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
RACG_C4(len<=6) PASS: verified 575 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
Hyperbolic_4(len<=6) PASS: verified 197 elements, Lemmas 1-5 and Theorem 1 (intersection & union closure).
PASS
```

### B. Independent Exact Adversarial Stress Tests (Non-Reduced Words, Skipped Rank-4/5 Lemma 5, $m_{ij}=6$, Rank-5 RACG)
Implemented an independent single-core exact Tits geometric representation over $\mathbb{Z}$, $\mathbb{Z}[\phi]$ ($\phi = 2\cos(\pi/5)$), and $\mathbb{Z}[\sqrt{3}]$ ($2\cos(\pi/6) = \sqrt{3}$), computing Bruhat intervals `[e, x]` independently via Strong-Exchange reflection deletions (without using `Sub(a)` on non-reduced words):

1. **Lemma 3(1) (`Sub(a) == [e, Dem(a)]`) on 500 strictly non-reduced random words of lengths $2 \dots 8$:**
   - **$H_3$** (`120` elements): **PASS** on 500 strictly non-reduced words ($\ell(\mathrm{eval}(\mathbf{a})) < |\mathbf{a}|$) across lengths `[2, 3, 4, 5, 6, 7, 8]`.
   - **`Hyperbolic_4` ($\ell \le 8$, $m_{01}=5, m_{12}=3, m_{23}=\infty$, rest $2$):** **PASS** on 500 strictly non-reduced words across lengths `[2, 3, 4, 5, 6, 7, 8]`.

2. **Lemma 5 & Theorem 1 (with non-trivial incomparable pairs $\emptyset \subsetneq J \cap K \subsetneq J, K \subsetneq J \cup K \subsetneq S$):**
   Run in `8.43s` total (exit code `0`):
   - **`Hyperbolic_4(len<=6)`** (197 elements):
     - Theorem 1 **PASS**; `860` non-identity incomparable BP pairs `(w, J, K)` (including `192` **non-vacuous** incomparable pairs where $\mathrm{Supp}(w^J) \cap J \neq \emptyset$ and $\mathrm{Supp}(w^K) \cap K \neq \emptyset$, e.g. `w = s_0 s_1 s_0`, `J = {0, 2}`, `K = {0, 3}`, where $w^J = w^K = s_0 s_1$, $w_J = w_K = s_0$, $\mathrm{Supp}(w^J) \cap J = \{0\} = D_L(s_0)$, $J \cap K = \{0\}$, $J \cup K = \{0, 2, 3\}$; also full-support sample `w = s_0 s_1 s_3 s_2`, `J = {1, 2}`, `K = {2, 3}`).
     - Lemma 5 **PASS**: verified `155,244` qualifying `(u, v, J, K)` tuples across all $197^2 = 38,809$ pairs `(u, v)`.
   - **`tildeG2+extra(len<=6)`** (rank 4 over $\mathbb{Z}[\sqrt{3}]$ with $m_{01}=6, m_{12}=3, m_{23}=3$, rest $2$; 145 elements):
     - Theorem 1 **PASS**; `762` non-identity incomparable pairs (`188` non-vacuous, e.g. `w = s_0 s_1 s_0`, `J = {0, 2}`, `K = {0, 3}`; full-support sample `w = s_0 s_1 s_3 s_2`, `J = {1, 2}`, `K = {2, 3}`).
     - Lemma 5 **PASS**: verified `114,882` qualifying `(u, v, J, K)` tuples across all $145^2 = 21,025$ pairs.
   - **`RACG_P5(len<=5)`** (rank-5 right-angled path $P_5$; 297 elements):
     - Theorem 1 **PASS**; `17,170` non-identity incomparable pairs (`1,690` non-vacuous, e.g. `w = s_0 s_1 s_0`, `J = {0, 2}`, `K = {0, 3}`; full-support sample `w = s_0 s_1 s_2 s_4 s_3`, `J = {2, 3}`, `K = {3, 4}`).
     - Lemma 5 **PASS**: verified `851,876` qualifying `(u, v, J, K)` tuples across all $297^2 = 88,209$ pairs.
   - **`RACG_C5(len<=5)`** (rank-5 right-angled cycle $C_5$; 441 elements):
     - Theorem 1 **PASS**; `19,250` non-identity incomparable pairs (full-support sample `w = s_0 s_1 s_2 s_4 s_3`, `J = {2, 3}`, `K = {3, 4}`).
     - Lemma 5 **PASS**: verified `1,184,384` qualifying `(u, v, J, K)` tuples across all $441^2 = 194,481$ pairs.

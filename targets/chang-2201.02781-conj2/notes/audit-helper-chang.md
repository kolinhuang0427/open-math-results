# Adversarial Audit Helper Report: `targets/chang-2201.02781-conj2/`

- **Checked UTC:** 2026-11-27T01:10Z
- **Scope & Isolation:** Read only primary sources in `tools/.arxiv_cache/`, `watch/snapshots/`, external scholarly APIs/search, GitHub (read-only), and ran `notes/check-check-2.py`. Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, `TARGET.md`, or `PROOF.md`.
- **Contested status:** `ls -la targets/chang-2201.02781-conj2/` shows `PROOF.md`, `TARGET.md`, `verify.py`, `notes/`, `__pycache__/` — **no `CONTESTED.md` exists**.

---

## 1. Primary-Source Verbatim & Bibliographic Check

### 1.1 `tools/arxiv_fetch.py query --id-list 2201.02781,2303.02611`

- **`arXiv:2201.02781v1`** (latest and only version):
  - **Title:** *An extension on neighbor sum distinguishing total coloring of graphs*
  - **Published / Updated:** `2022-01-08T07:01:27Z`
  - **Exact authors:** `Jing-zhi Chang`, `Chao Yang`, `Zhi-xiang Yin`, `Bing Yao` (verified in both arXiv API XML and TeX source line 83: `Jing-zhi Chang^1, Chao Yang^{1,*}, Zhi-xiang Yin^1, Bing Yao^2`; **not** `Yuhong Chang / Yujun Yin`).
  - **Journal ref / DOI in arXiv:** empty (`""` / `""`).
  - **arXiv admin comment:** `arXiv admin note: text overlap with arXiv:2107.00424` (the overlapping preprint `2107.00424v1` is *"A note on 1-2-3 and 1-2 Conjectures for 3-regular graphs"* by the same four authors `Jing-zhi Chang, Chao Yang, Zhi-xiang Yin, Bing Yao`, published `2021-07-01`, also with empty `journal_ref`/`doi`).
  - **Journal publication check:** No journal publication of `2201.02781` itself was found on Crossref, OpenAlex, Semantic Scholar, or web search. Cheng–Yang–Yao–Luo (*AIMS Math.* 7(4):6959–6970, 2022, DOI `10.3934/math.2022386`) explicitly cites it as `arXiv Preprint, 2022, https://arXiv.org/abs/2201.02781`.

- **`arXiv:2303.02611v4`** (latest version):
  - **Title:** *A Solution to the 1-2-3 Conjecture*
  - **Published:** `2023-03-05T08:46:38Z`, **Updated:** `2024-01-06T19:31:09Z`
  - **Author:** `Ralph Keusch`
  - **Journal ref:** `Journal of Combinatorial Theory, Series B Volume 166, May 2024` (pages 183–202)
  - **DOI:** `10.1016/j.jctb.2024.01.002`

### 1.2 Exact Statements in `tools/.arxiv_cache/eprint/2201.02781/An_extension_on_nsdt-_coloring_of_graphs-arXiv.tex`

- **Standing graph convention (line 125):**
  > `All considered graphs are finite, undirected, simple and connected.`
- **Definition 1 (lines 146–151):**
  > **Definition 1.** [4] *Let $f: V(G)\cup E(G)\rightarrow [1, k]$ be a non-proper $k$-total coloring of $G$. Set $\phi(x)=f(x)+\sum\limits_{e\ni x}f(e)+\sum\limits_{y\in N(x)}f(y)$, where $N(x)=\{y\in V(G)|xy\in E(G)\}$. For any edge $xy\in E(G)$, if $\phi(x)\neq \phi(y)$, then $f$ is called a neighbor full sum distinguishing (NFSD) total $k$-coloring of $G$. The smallest value $k$ for which $G$ has an NFSD-total coloring is called the neighbor full sum distinguishing total chromatic number of $G$ and denoted by* $\mathrm{fgndi}_{\sum}(G)$.
  *(Note: $[s,t]$ is defined on line 126 as $\{s,s+1,s+2,\ldots,t\}$.)*
- **$K_1$, $K_2$, and connected graphs (lines 155–162 & Abstract lines 112–114):**
  - Abstract (lines 112–114): `In this paper we conjecture that fgndi$_{\sum}(G)\leq 3$ for any connected graph $G$ of order at least three.`
  - Section 1 (lines 155–158): `Evidently, when searching for the NFSD-total coloring it is sufficient to restrict our attention to connected graphs. Observe also, that $G=K_2$ does not have any NFSD-total coloring. So, we shall consider only connected graphs with at least three vertices. We propose the following conjecture.`
  - **Conjecture 2 (line 162):**
    > **Conjecture 2.** *For every connected graph $G$ and $G$ is not $K_2$,* $\mathrm{fgndi}_{\sum}(G)\leq 3$.
  - **Remark on $K_1$:** $K_1$ is not excluded by Conjecture 2's literal phrasing ("every connected graph $G$ and $G$ is not $K_2$"), whereas lines 113–114 and 157–158 say "connected graph $G$ of order at least three" / "with at least three vertices". Since $E(K_1)=\emptyset$, the edge condition $\phi(x)\neq\phi(y)$ for $xy\in E(K_1)$ holds vacuously for $k=1$, so $\mathrm{fgndi}_{\sum}(K_1)=1\le 3$ anyway.
- **Other remarks in `2201.02781`:**
  - Lines 134–142: Summarizes Karoński–Łuczak–Thomason [6]/[7] (1-2-3 Conjecture, open in general as of Jan 2022), Addario-Berry et al. [1,2], Wang–Yu [10], Kalkowski–Karoński–Pfender [6] ($k=5$), Przybyło [9] ($d$-regular $k=4$, $d\ge 10^8$ $k=3$), Przybyło–Woźniak [8] (1-2 Conjecture), Kalkowski [5] ($\mathrm{tgndi}_{\sum}(G)\le 3$), and Flandrin et al. [4] (*Discuss. Math. Graph Theory* 37(1), 2017, introducing NFSD total coloring).
  - Lines 500–510 (before Theorem 11): Typo refers to `Conjecture 1`, and applies Kalkowski et al.'s 5-edge-weighting together with $f(v)\equiv 1$ on vertices to observe that balanced complete $r$-partite graphs trivially get an NFSD-total $5$-coloring (since vertex colors $1$ add a constant $n - n/r + 1$), then improves $5$ to $3$ in Theorem 11.
  - Section 5 `Future Works` (lines 671, 675): Lists `Problem 1` (`Whether fgndi_\Sigma(G) \le 3 holds for every connected graph G with \Delta=3?` — likely a typo relative to Theorem 7 for 3-regular graphs, or meant subcubic $\Delta\le 3$ / non-regular $\Delta=3$) and `Problem 2` (complete $r$-partite graphs outside cases (i) and (ii) of Theorem 11, misreferenced as `Theorem 8`).

### 1.3 Keusch (2024) `tools/.arxiv_cache/eprint/2303.02611/123ConjectureRevisedVersion.tex`

- **Does Keusch mention $\{a,a+1,a+2\}$-weightings?** **YES**, in Section 5 (*Concluding remarks*, line 426), verbatim:
  > `Throughout the paper, it was assumed that for each edge the weights are chosen from the set $\{1,2,3\}$. We think that all arguments work as long as the weight set has the form $\{a, a+1, a+2\}$, with $a \in \{1, 3, 5, \ldots\}$. However, it is reasonable to believe that the statement is true for all weight sets of the form $\{a, a+d, a+2d\}$ with $a \in \ZZ$ and $b \in \NN$, but such a generalization does not follow directly from the present proof.`
  *(Note: Keusch explicitly writes **"We think that all arguments work..."** — he does **not** state or prove $\{a,a+1,a+2\}$-weightings as a theorem in `2303.02611v4`, and he explicitly restricts his conjecture-about-the-proof to **odd** $a \in \{1,3,5,\ldots\}$; `$b \in \NN$` is a typo for `$d \in \NN$`.)*
- **Does Keusch mention `{2,3,4}` or `{3,4,5}` or shifted/offset 1-2-3?** Not explicitly by those numerals or names; `{3,4,5}` corresponds to $a=3$ (odd) in line 426, and `{2,3,4}` corresponds to $a=2$ (even), which is *not* even claimed in Keusch's odd-$a$ remark.
- **Does Keusch mention total colorings?** **YES**, in Section 1 (line 86) and Section 5 (line 428), discussing Przybyło–Woźniak's total weightings (the 1-2 Conjecture, $\phi(v) = w(v)+\sum_{e\ni v} w(e)$ without $\sum_{u\in N(v)} w(u)$) and Kalkowski's $(2,3)$-total weighting, concluding at line 428:
  > `Finally, it is natural to transfer the described technique to total weightings. However, it seems that additional ideas are needed to solve the conjecture of Przyby{\l}o and Wo\'{z}niak \cite{przybylo2010conjecture}. We leave this to future work.`
  Keusch makes **no** mention of NFSD total coloring (`fgndi`), Flandrin et al., or Chang et al.

---

## 2. Deep Novelty & Prior-Art Search (2022 – 2026-11-27)

### 2.1 Local Watch Snapshot Grep

Command: `.venv/bin/python tools/novelty_grep.py 2201.02781 fgndi "neighbor full sum" NFSD "1-2-3" Keusch`
- Matched 5 lines across 4/357 files:
  - `watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json`: `citing_count: 0`, `citing_works: []` (checked `2026-11-26T22:55:31Z`).
  - `watch/snapshots/arxiv/openalex_works_cache.json`: `"2201.02781": { "openalex_id": null, "note": "not yet indexed in OpenAlex" }`.
  - `watch/snapshots/formal/formal-conjectures-prs.jsonl`: PR #7912 (`arXiv:2607.00934`, Pilz's Extended 1-2-3 Conjecture on $A \Delta (2A) \Delta \cdots \Delta (nA)$ — additive combinatorics, unrelated).
  - `watch/snapshots/ai-collections/techno-optimist__erdos-frontier-atlas/commits.json`: PGP signature string false positive.
- Additional grep across `watch/snapshots/discovered/`, `1337-solved-conjectures/`, `openai-math/`, `formal/`: only the same PR #7912 hit.

### 2.2 NFSD / `fgndi` / `2201.02781` Follow-Up Literature (2022–2026)

Searched arXiv API, Crossref, OpenAlex, Semantic Scholar (S2 returned 429 on `ARXIV:*` queries, succeeded on DOI queries), Zenodo, and `search_web`:
1. **Y. W. Cheng, C. Yang, B. Yao, Y. Q. Luo (2022)** — *"Neighbor full sum distinguishing total coloring of Halin graphs"*, *AIMS Mathematics* 7(4), 6959–6970, DOI `10.3934/math.2022386`. Proves $\mathrm{fgndi}_{\sum}(G)\le 3$ for 3-regular Halin graphs and Halin graphs whose inner vertices adjacent to $C$ have degree $\ge 4$. Explicitly cites `arXiv:2201.02781` and writes that these results support Chang et al.'s open conjecture $\mathrm{fgndi}_{\sum}(G)\le 3$.
2. **F. X. Cui, C. Yang, H. B. Ye, B. Yao (2022)** — *"Neighbor full sum distinguishing total coloring of join graphs"*, *J. Jilin Univ. (Science Edition)* 60(1), 44–52 (in Chinese). Specific graph family (join graphs).
3. **F. X. Cui, C. Yang, H. B. Ye, B. Yao (2023)** — *"Neighbor full sum distinguishing total coloring of graphs"*, *Oper. Res. Trans.* 27(1), 149–158 (in Chinese). Specific graph families.
4. **Z. J. Li, F. Wen (2024)** — *"Neighbor full sum distinguishing total coloring of unicyclic graph"*, *J. Jilin Univ. (Science Edition)* 62(3), 497–502 (in Chinese). Unicyclic graphs only.
5. **Z. Yue, F. Wen, Z. Li (2024/2025)** — *"Neighbor full sum distinguishing total coloring of planar graphs"*, *The Journal of Supercomputing* 81, Art. 309, DOI `10.1007/s11227-024-06825-z`. Studies **proper** NFSD total coloring ($\mathrm{ftndi}_{\sum}(G)$, bounded by $\Delta(G)+O(1)$), not $\mathrm{fgndi}_{\sum}\le 3$.
6. **Z. Yue, F. Wen (2025)** — *"Neighbor Full Sum Distinguishing Total Coloring of Planar Graphs with Girth at Least 5"*, *Axioms* 14(7), 496, DOI `10.3390/axioms14070496`. Explicitly defines $\mathrm{ftndi}_{\Sigma}(G)$ using **proper** $k$-total colorings and proves $\mathrm{ftndi}_{\Sigma}(G)\le \Delta(G)+3$ for normal planar graphs with $g(G)\ge 5$ and $\Delta(G)\ge 22$.
7. **F. Wen, Z. Yue, Z. Li, H.-J. Lai (2026)** — *"On the neighbor full sum distinguishing total coloring of graphs"*, *Discrete Applied Mathematics* 389 (2026), 46–57, DOI `10.1016/j.dam.2026.03.034`.
   - **Bounded-search caveat:** OpenAlex and Crossref have no abstract for this DOI, and the ScienceDirect full text is paywalled. However, its 19 Crossref references are Combinatorial Nullstellensatz / **proper** total-coloring papers (`Alon 1999`, `Behzad 1965`, `Vizing 1968`, `Pilśniak 2015`, `Montassier 2006`, `Song 2016/2020`, `Yang 2017`, `Sun 2021`, `Duan 2025`, `Yue 2025 J. Supercomput.`, `Yue 2025 Axioms`, plus `Flandrin 2017` and `Cui 2023`), it does **not** cite Keusch (`2303.02611` / `JCTB 2024`) or Chang et al. (`2201.02781`), and it is cited by `Yue & Wen (2025, Axioms)` in the $\mathrm{ftndi}_{\Sigma}(G)\le \Delta(G)+O(1)$ proper-total-coloring line.

**Conclusion for (2a):** None of these papers proves $\mathrm{fgndi}_{\sum}(G)\le 3$ for all connected graphs $G\neq K_2$.

### 2.3 Equivalent Edge-Weighting Literature (`{a,a+1,a+2}`, `{2,3,4}`, `{3,4,5}`, List 1-2-3, Universal 3-Edge-Weightability, 2023–2026)

With $f(v)\equiv 1$ or $f(v)\equiv 2$, $\phi(x) = c + \sum_{e\ni x}(f(e)+c)$, so any proof of $\{2,3,4\}$- or $\{3,4,5\}$-edge-weightability (or universal $3$-edge-weightability, edge-weight $3$-choosability, or $(1,3)$-choosability) for all connected graphs $G\neq K_2$ would immediately prove Conjecture 2.

Checked all **57 OpenAlex works citing Keusch (`10.1016/j.jctb.2024.01.002`)** (OpenAlex ID `W4391247093`, total `cited_by_count: 60`), arXiv API (2023–2026-11), Zenodo, and `search_web`:

- **Key direct confirmation of open status as of Feb 2026 — Kecai Deng (2026), *"Regular graphs are universally 3-edge-weightable"*, `arXiv:2602.06659v2` (2026-02-13):**
  - Proves that every nice **$k$-regular** graph ($k\ge 2$) is universally $3$-edge-weightable (has a proper $\{a,b,c\}$-edge-weighting for every $3$-element $Q=\{a,b,c\}\subset\mathbb{R}$).
  - Crucially explains (lines 113–133) that affine shifting from Keusch's $\{1,2,3\}$-theorem gives $\{a,b,c\}$-weightings for arithmetic progressions **for regular graphs** (because adding a constant $b$ shifts each vertex sum by $b \cdot d$), whereas **general non-regular graphs** are NOT settled by Keusch's theorem!
  - Explicitly states on lines 107 and 136–140 that **as of February 2026**:
    - **$(1,3)$-choosability** (Wong–Zhu) remains **open** (best general bound: Zhu 2022, $(1,5)$-choosable);
    - **edge-weight $3$-choosability** (Bartnicki–Grytczuk–Niwczyk) remains **open** (best general bound: edge-weight $5$-choosable);
    - **Universal $3$-edge-weightability** for all nice graphs remains **open** (`Problem 1.1: Is every nice graph universally 3-edge-weightable?`).
- **Other 2023–2026 citing/related papers checked (none settles $\{2,3,4\}$ or $\{3,4,5\}$ for general graphs):**
  - **K. Deng & H. Qiu (2025)**, *JCTB* 174:207–213 (`10.1016/j.jctb.2025.05.002`, *"The 1-2 conjecture holds for regular graphs"*) and **`arXiv:2506.14253v8`** (Oct 2025, *"Every graph is uniform-span $(2,2)$-choosable: Beyond the 1-2 conjecture"*): solves the 1-2 Conjecture / uniform-span $(2,2)$-choosability for Przybyło–Woźniak total weightings $w(v)+\sum_{e\ni v}w(e)$ (no $\sum_{y\in N(v)} w(y)$ term, so vertex weights cannot be eliminated by fixing $w(v)$ as in NFSD, and edge weights only have size-2 lists).
  - **J. Bensmail, B. Martins, C. Tang (`arXiv:2504.21452v2`, May 2025)**: 1-2 Conjecture for $\Delta\le 6$ / $\mathrm{mad}\le 3$.
  - **P. Madarasi (*Discrete Math.* 2026, `10.1016/j.disc.2026.115539`) & P. Madarasi, M. Simon (`arXiv:2609.31205v1`, Sep 2026)**: Complexity/extension of proper $\{a,b\}$-edge-weightings (2-weight sets).
  - **S. Aute, F. Panolan, G. Philip (`arXiv:2604.12363v1`, `arXiv:2609.27719v1`)**: Parameterized complexity of $\{0,1\}$- and $\{1,2\}$-edge-weightings.
  - **A. Ahadi, S. Alipour (`arXiv:2609.12234v1`)**: Vertex-only additive labeling (`\eta(G)`).
  - **M. Stawiski (`arXiv:2304.10208`)**, **A. Charlesworth, C. Ramsey, N. Strungaru (`arXiv:2604.15138v1`)**, **J. Chen, W. Dai (`arXiv:2611.03320v1`)**: Infinite, tiling, and Borel analogues of $\{1,2,3\}$-weightings.
  - **P. Holdridge, P. P. Pach (`arXiv:2607.00934v1`)**: Pilz's Extended 1-2-3 Conjecture (unrelated set-sum problem).

**Conclusion for (2b):** Neither $\{3,4,5\}$-edge-weighting, $\{2,3,4\}$-edge-weighting, $\{a,a+1,a+2\}$-edge-weighting, universal $3$-edge-weightability, edge-weight $3$-choosability, nor $(1,3)$-choosability has been proved for all connected graphs $G\neq K_2$.

### 2.4 Competing GitHub Repositories & Global GitHub Search

- Global `gh search code` & `gh search issues` for `2201.02781`, `fgndi`, `"neighbor full sum"`, `NFSD`, `"1-2-3" Keusch`: **0 mathematical/conjecture hits** (only unrelated software/bioinformatics hits).
- Repo-scoped `gh search code` & `gh search issues` across `aliromman/math`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-mdbook`, `KnowledgeSense/math`, `1337isnot1337/solved-conjectures`, `openai/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, and `facebookresearch/atlas-lean` for `2201.02781`, `fgndi`, `"neighbor full sum"`, `NFSD`, `Keusch`, `1-2-3`, `"neighbor sum distinguishing"`, `"edge-weighting"`, `"1-2-3 Conjecture"`, `"total coloring"`: **0 hits matching Chang's Conjecture 2 or shifted 1-2-3 edge-weightings**.

### 2.5 Search Boundaries / Coverage Caveats

- Semantic Scholar returned HTTP 429 on `ARXIV:2201.02781` and `ARXIV:2303.02611`, and Crossref returned HTTP 429 on the broad query `"neighbor full sum distinguishing"` (while succeeding on individual DOI lookups).
- Full text of `10.1016/j.dam.2026.03.034` (Wen, Yue, Li, Lai, *DAM* 389, 2026) and the Chinese-language articles `Cui et al. (2022, 2023)` / `Li & Wen (2024)` are behind publisher paywalls and were not directly inspected; assessment of `10.1016/j.dam.2026.03.034` rests on its Crossref bibliography and its citation in `Yue & Wen (2025, Axioms)`.
- Search is current as of `2026-11-27T01:10Z`.

---

## 3. Independent Rerun of `notes/check-check-2.py`

Command: `/usr/bin/time -p .venv/bin/python targets/chang-2201.02781-conj2/notes/check-check-2.py`
- **Exit code:** `0`
- **Runtime:** `13.414s` (internal script timer); OS wall/CPU time `real 13.53`, `user 8.65`, `sys 1.02`
- **Exact raw output:**
```text
Sanity check K_2 impossible (all 27 3-colorings fail) & K_1 trivial: PASS
Exhaustive n=3 (4 labeled connected graphs x 3 offset functions): PASS
Exhaustive n=4 (38 labeled connected graphs x 3 offset functions): PASS
Exhaustive n=5 (728 labeled connected graphs x 3 offset functions): PASS
Exhaustive n=6 (26704 ALL labeled connected graphs, Def 1 f(v)=2): PASS
Larger & structured graphs (283 graphs n=7..16 x 3 offsets): PASS
Proof cases triggered (18): ['C1_even', 'C1_odd', 'C2_Beven_zyB', 'C2_Beven_zyR', 'C2_Bodd_zyB', 'C2_Bodd_zyR', 'C3_Bodd_degRx0', 'C3_Bodd_degRx_ge2', 'C3_Bodd_degRy0', 'C3_Bodd_degRy_ge2', 'C3_Bodd_disjoint_zyB', 'C3_Bodd_disjoint_zyR', 'C3_Bodd_joint_q', 'C4_Beven_Rx0_L6y', 'C4_Beven_Rx0_Ry0', 'C4_Beven_Rx0_tilde', 'C4_Beven_Ry0', 'C4_Beven_bothR']
Lemma 6/7 sub-branches triggered (6): ['L6_i_gt_kx_x_lt_k', 'L6_i_le_kx', 'L6_x_eq_k', 'L7_11', 'L7_31', 'L7_33']
PASS (all constructive proof & Conjecture 2 checks passed in 13.414s)
```

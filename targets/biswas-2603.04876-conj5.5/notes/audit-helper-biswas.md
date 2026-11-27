# Adversarial Audit Helper Report: `targets/biswas-2603.04876-conj5.5/`

**Auditor Helper:** `biswas-audit-hlp` (for `@audit-3`)
**Checked at (UTC):** `2026-11-27T03:46Z`–`2026-11-27T03:56Z`
**Strict Isolation Observed:** Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or `notes/check-check-3.py` (only executed `check-check-3.py`); did NOT edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source & Directory Check

### 1.1 arXiv Metadata Query
Command: `.venv/bin/python tools/arxiv_fetch.py query --id-list 2603.04876`
- **Latest version:** `2603.04876v1` (`total_results: 1`)
- **Title:** *"Lattice points arising from regularity and $\mathrm{v}$-number of Graphs: Whisker and Cameron-Walker"*
- **Authors:** Prativa Biswas, Mousumi Mandal, Kamalesh Saha
- **Published / Updated:** `2026-03-05T07:05:37Z` (both)
- **Categories:** `math.AC` (primary), `math.CO`
- **Comment:** `20 pages, 5 figures`
- **Journal-ref:** `""` (none)
- **DOI:** `""` (none on arXiv record; OpenAlex indexes preprint DOI `https://doi.org/10.48550/arxiv.2603.04876`)

### 1.2 Target Directory Check
Command: `ls -la /Users/kev/Documents/open-math/targets/biswas-2603.04876-conj5.5`
- Files present: `PROOF.md` (28,406 bytes), `TARGET.md` (2,868 bytes), `verify.py` (22,325 bytes), `__pycache__/`, `notes/`.
- **Confirmed:** No `CONTESTED.md` is present.

### 1.3 Exact Theorem / Definition Numbering Verification in `tools/.arxiv_cache/eprint/2603.04876/Arxiv.tex`
In `Arxiv.tex` (no compiled PDF present in `tools/.arxiv_cache/eprint/2603.04876/`, which contains `00README.json`, `Arxiv.bbl`, `Arxiv.tex`, `refrv.bib`):
- Theorem environment setup (`Arxiv.tex` lines 172–202): `\newtheorem{theorem}{Theorem}[section]`, with `corollary`, `lemma`, `proposition`, `conjecture`, `remark`, `definition` all sharing the `[theorem]` counter.
- Section headings (`Arxiv.tex`):
  - Section 1 (`line 235`): `\section{Introduction}`
  - Section 2 (`line 278`): `\section{Preliminaries}\label{preli}`
  - Section 3 (`line 348`): `\section{An approximation of the set $\RV(n)$}\label{sec:3}`
  - Section 4 (`line 540`): `\section{The set $\RV_{W}(n)$: Restriction of $\RV(n)$ to whisker graphs}\label{sec:whisker graph}`
  - Section 5 (`line 734`): `\section{The set $\RV_{CW}(n)$: Restriction of $\RV(n)$ to Cameron-Walker graphs}\label{sec:CW}`
- Exact numbering in Section 2:
  - Def 2.1 (`line 281`), Def 2.2 (`line 292`), Def 2.3 (`line 296`)
  - **Definition 2.4** (`line 303`, `\label{def:v}`): combinatorial $\mathrm{v}$-number $\mathrm{v}(G) := \min\{|A| \mid A \text{ is independent and } N_G(A) \text{ is a vertex cover of } G\}$; line 301 cites `\cite[Lemma 3.4]{jv21}` and `\cite[Theorem 3.5]{jv21}` (Jaramillo–Villarreal 2021, `Arxiv.bbl` lines 88–90).
  - Def 2.5 (`line 310`), Def 2.6 (`line 318`), Lemma 2.7 (`line 324`), Theorem 2.8 (`line 329`)
  - **Proposition 2.9** (`line 333`, `\label{prop:reg<n/2}`): connected graph $G$ on $n \ge 3$ vertices satisfies $\mathrm{reg}(G) < \frac{n}{2}$.
  - Theorem 2.10 (`line 340`)
  - **Theorem 2.11** (`line 344`, `\label{thm:reg chordal}`): cites `\cite[Corollary 6.9]{hv08}` (Hà–Van Tuyl 2008, `Arxiv.bbl` lines 52–55): for a chordal graph $G$, $\mathrm{reg}(G) = \mathrm{im}(G)$.
- Exact numbering in Section 3:
  - Def 3.1 (`line 351`), Prop 3.2 (`line 356`), Remark 3.3 (`line 368`)
  - **Lemma 3.4** (`line 371`, `\label{main}`): $\{x, y, z\}$ inducing $P_3$ with $\{x,y\},\{y,z\}\in E(G)$, $\deg_G(y)=2$, $\deg_G(z)=1$ $\implies A \cap \{x,y,z\} \neq \emptyset$.
  - **Theorem 3.5** (`line 380`, `\label{thm:RV(n)}`): $A(n) \subseteq \mathcal{RV}(n) \subseteq B(n)$ for $n \ge 3$.
- Exact numbering in Section 5 (`\subsection{Future Directions}`, `lines 975–983`):
  - Def 5.1 (`line 756`), Theorem 5.2 (`line 854`), Lemma 5.3 (`line 864`), Theorem 5.4 (`line 897`)
  - Line 975–978 explicitly notes that both cases of Theorem 3.5 used chordal graphs, so $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$.
  - **Conjecture 5.5** (`lines 980–983`):
    $$\mathcal{RV}_{chordal}(n)=\left\{(r,v)\in \mathbb{N}^{2} \mid 1\leq r<\frac{n}{2}, 1\leq v\leq r-\left\lceil\frac{r}{n-2r}\right\rceil+1\right\}$$
    for the class of connected chordal graphs on $n \ge 3$ vertices.

**Accuracy verdict on `PROOF.md` citations:**
- All citations in Sections 1–3 of `PROOF.md` (`arXiv:2603.04876v1`, `2026-03-05`, Section 5 Conjecture 5.5 `lines 980–983`, Definition 2.4 citing Jaramillo–Villarreal 2021 Lemma 3.4 & Theorem 3.5, Proposition 2.9, Theorem 2.11 citing Hà–Van Tuyl 2008 Corollary 6.9, Lemma 3.4, Theorem 3.5) match `Arxiv.tex` 100% accurately.
- **Minor editorial note (non-mathematical, Section 4 line 174 of `PROOF.md`):** Line 174 mentions *"Saha–Sengupta witnesses $A$"*. Saha–Sengupta 2022 (`ss22`, `arXiv:2111.12881v2`, *J. Algebraic Combin.* 56(3):903–927) proved $\mathrm{v}(I(G)) \le \mathrm{im}(G) \le \mathrm{reg}(R/I(G))$ for $(C_4, C_5)$-free vertex-decomposable graphs (which include chordal graphs), and `ss22` is cited in `Arxiv.tex` line 249, though not explicitly cited in Sections 1–3 of `PROOF.md` (where Lemma 2 independently proves $\mathrm{v}(H) \le \mathrm{im}(H)$ for all chordal $H$).

---

## 2. Deep Novelty & Literature Check (1989–2026-11-27)

### 2.1 Local Watch Snapshots (`watch/snapshots/**`)
Command: `.venv/bin/python tools/novelty_grep.py 2603.04876 Biswas Mandal "Kamalesh Saha" "RV_chordal" "v-number" "Cameron-Walker"`
- **Result:** 46 matched lines across 20/470 files:
  - Target's own OpenAlex/arXiv watch files (`citing/biswas-2603.04876-conj5.5.json` reports `citing_count: 0`, `openalex_works_cache.json` had `2603.04876` not yet indexed at snapshot time `2026-11-27T01:59:39Z`).
  - Unrelated `ArtificialZeng__AI-Has-Taste` entries on v-number under integral closure (`BW2-B74-P02`, `BM2-B08-P04`, `SM2-P52`), unrelated Mandal papers (`Bhattacharjee–Mandal–Bhattacharya`, `Mandal–Mohan` Fibonacci means, `Manna–Mandal` prime index graph, `Henry-77777/mandal-manna-conjecture-5-5`).
  - **0 hits** settling Conjecture 5.5, $\mathcal{RV}_{\mathrm{chordal}}(n)$, or the chordal bounds.

### 2.2 arXiv API (`tools/arxiv_fetch.py query`)
Queries run:
1. `all:2603.04876` -> 1 result (`2603.04876v1` only).
2. `all:"v-number" AND all:chordal` -> 2 results (`2603.28247v2` Jaramillo-Velez–López–San-José on closed neighborhood ideals, `2603.04876v1`).
3. `all:"v-number" AND all:"regularity"` -> 25+ results inspected (`2610.33858v1`, `2610.29855v1`, `2609.37219v1`, `2608.01199v1`, `2604.20729v2`, `2603.28247v2`, `2603.04876v1`, `2601.06739v1`, `2601.03208v2`, `2507.05700v2`, `2506.09051v2`, `2504.04478v1`, `2412.21031v3`, `2405.15354v1`, `2403.09175v6`, `2311.04136v1`, `2308.13728v3`, `2308.09996v1`, `2305.06270v4`, `2304.06416v1`, `2204.10317v1`, `2111.12881v2`, `2109.14121v2`, `2001.06861v1`, `1508.03835v1`). None address $\mathcal{RV}_{\mathrm{chordal}}(n)$, $\mathrm{v}(G) \le r - \lceil r/(n-2r)\rceil + 1$, or $\mathrm{im}(G - N_G[x^*]) \le r - \lceil r/(n-2r)\rceil$.
4. `au:Saha AND all:"v-number"` -> 10 results (`2603.04876v1`, `2507.05700v2`, `2406.05567v1`, `2405.15354v1`, `2404.00493v2`, `2402.16583v1`, `2311.04136v1`, `2308.09996v1`, `2304.06416v1`, `2111.12881v2`).
5. `au:Mandal AND all:"v-number"` -> 6 results (`2611.01156v1`, `2609.05044v1`, `2603.08838v3`, `2603.04876v1`, `2402.16583v1`, `2308.08604v1`).
6. `au:Biswas AND all:"v-number"` -> 4 results (`2609.05044v1`, `2603.04876v1`, `2402.16583v1`, `2308.08604v1`).
7. `all:"induced matching" AND all:chordal AND all:"v-number"` -> 0 results.

### 2.3 OpenAlex, Crossref, Zenodo, and Web Search
- **OpenAlex:**
  - `2603.04876` is indexed as `https://openalex.org/W7134037417` (*Lattice points arising from regularity and $\mathrm{v}$-number of Graphs: Whisker and Cameron-Walker*, DOI `10.48550/arxiv.2603.04876`) with **`cited_by_count: 0`** (`filter=cites:W7134037417` returned `0` works).
  - Author profiles checked for 2025–2026 works:
    - Kamalesh Saha (`A5005424479`, 32 works): 2025–2026 papers (`W4406440871`, `W4392222864`, `W4416664099`, `W4408963423`, `W4413965319`, `W7160511977`, `W7117320907`, `W4414816012`, `W4416542306`, `W7196923222`, `W4413800149`, `W4415886204`, `W7128487940`, `W7134037417`, `W7215034266`) — none settle Conjecture 5.5 or the chordal bounds (a separate `A5076302400` profile had 0 works in 2025–2026).
    - Mousumi Mandal (`A5004073616`, 31 works): 2025–2026 papers (`W4392222864`, `W4393929549`, `W7134944724`, `W7211897881`, `W4411164551`, `W7134037417`, `W7172289937`) — none settle Conjecture 5.5.
    - Prativa Biswas (`A5112885215`): math works in 2025–2026 are `W7211897881` (`2609.05044`, integral closure) and `W7134037417` (`2603.04876`).
  - Literature searches for `"Cameron Induced matchings 1989"`, `"induced matching clique cover chordal"`, `"induced matching vertex deletion chordal"`, and `"v-number chordal regularity"`: Cameron (1989, *Discrete Appl. Math.* 24, `W4210377846`) gives the polynomial-time algorithm / clique-cover characterization for induced matchings in chordal graphs, and no work found establishes $\mathrm{im}(G - N_G[x^*]) \le r - \lceil r/(n-2r)\rceil$ or $\mathrm{v}(G) \le r - \lceil r/(n-2r)\rceil + 1$ for connected chordal graphs.
- **Crossref:** Queries for `2603.04876`, `Lattice points arising from regularity`, `v-number chordal n-2r` returned no matching paper solving (a), (b), or (c). (One middle query hit transient HTTP 429; re-queried via `query.title=Lattice+points+arising+from+regularity`, 0 relevant hits.)
- **Zenodo API:** Queries `"2603.04876"`, `"Lattice points arising from regularity"`, `"RV_chordal"`, `"biswas-2603.04876"` returned `total: 0`; `"Kamalesh Saha" "v-number"` returned 10 unrelated biology/optics records.
- **Web Search (`search_web`):**
  - `"2603.04876" OR "RV_chordal" OR "Lattice points arising from regularity and v-number"` -> returned only `arXiv:2603.04876`.
  - `"v-number" "chordal" "n-2r" OR "induced matching" "clique cover" "Cameron" "chordal" "v-number"` and `"induced matching" "chordal" "clique cover" "Cameron" 1989 OR "v-number" "2603.04876"` -> returned only general background on Cameron (1989) and `arXiv:2109.14121` / Cameron-Walker graphs.

### 2.4 Competing GitHub Repositories (read-only `gh`)
Checked full git trees (`git/trees/<branch>?recursive=1`) for:
- `the-omega-institute/trureturing*` (all 19 org repos enumerated: `automath`, `newmath`, `trureturing`, `trureturing-pages`, `trureturing-mdbook`, `trureturing-intuition`, `trureturing-film`, `trureturing-visualize`, `trureturing-lean-eval`, `mathesis`, `trureturing-experiments`, `trureturing-books-template`, `trureturing-books`, `trureturing-requests` [empty], `trureturing-source-theories`, `trureturing-tools`, `trureturing-outreach-engine`, `trureturing-live`, `trureturing-live-template`). `trureturing` has `Blueprint/D5/S3/Combinatorics/Graph/Chordal/` and PRs `#34683` & `#34568`, verified to be about skew triangle-flat Banach/seminorm gains on chordal graphs, unrelated to `v-number` or `RV_chordal`. `gh search code "v-number" org:the-omega-institute` and `"2603.04876" org:the-omega-institute` returned 0 hits.
- `1337isnot1337/solved-conjectures` (`tree count=19826`, `CONTENTS.md`, `HISTORY.md`, top-100 issues & PRs): `brown-cameron-stability` and `alexandersson-graphical-dist` are unrelated; `gh search code "v-number" repo:1337isnot1337/solved-conjectures` and `"induced matching" repo:1337isnot1337/solved-conjectures` returned 0 hits.
- `aliromman/math` (`937`), `KnowledgeSense/math` (`5377`), `rainwangphy/aftd-platform` (`28161`), `valyuAI/research` (`5381`), `facebookresearch/atlas-lean` (`54016`), `JENW1N/complete-math-solutions` (`425`), `TheJustinSunPrize/awards` (`82`), `GuillaumeBAUD-coder/open-math-agents` (`1660`), `DomTheDeveloper/open-math-agents` (`446`), `DomTheDeveloper/ProofPlaygrond` (`68`), `CrocSwap/integer-mult-bounds` (`54080`), `linustalacko/small-true-things` (`37`), `chy4pro/automath` (`2969`), `openai/math` (`55175`): **0 matches** to `2603.04876`, `Biswas–Mandal–Saha`, `RV_chordal`, or Conjecture 5.5.
- Global `gh search` (`code`, `issues`, `repos`) for `2603.04876`, `RV_chordal`, `"Biswas" "Mandal" "Saha"`, and `"v-number" chordal`: only BibTeX/RSS/index mirrors (`NoLieNoSean/NoNotes`, `ehijano/rss_fetch`, `tamnd/arxiv:analysis/witness/theoremgraph/2603.md` which only counts 26 theorem/lemma/definition environments).

**Novelty conclusion:** No published paper, preprint, repository, or open/merged issue/PR settling (a) Conjecture 5.5 / $\mathcal{RV}_{\mathrm{chordal}}(n)$, (b) $\mathrm{v}(G) \le r - \lceil r/(n-2r)\rceil + 1$ for connected chordal graphs, or (c) $\mathrm{im}(G - N_G[x^*]) \le r - \lceil r/(n-2r)\rceil$ for connected chordal graphs was found. (Not covered: private repositories and manuscripts not indexed on arXiv, OpenAlex, Crossref, Zenodo, or web search.)

---

## 3. Independent Exact Computation Check

### 3.1 Execution of `notes/check-check-3.py`
Command: `/usr/bin/time -p .venv/bin/python -u targets/biswas-2603.04876-conj5.5/notes/check-check-3.py`
- **Exit code:** `0`
- **Runtime:** `real 0.44`, `user 0.40`, `sys 0.01`
- **Exact raw output:**
```
Exhaustive n=3..7 PASS: checked 352 non-isomorphic connected chordal graphs {3: 2, 4: 5, 5: 15, 6: 58, 7: 272}; RV_chordal(n)==A(n) exact.
Part 2 PASS: constructed and verified exact (im, v) for all 42 lattice points in A(3..11).
Large Stress PASS: 84 connected chordal graphs on n=8..14 verified against Lemmas 1-5 & Thm 1.
PASS
```

### 3.2 Independent Adversarial Check (Lemma 5 Subcase B2 & Part 2 Edge Cases)
Ran an independently written exact script (`scratch/audit_adversarial_check.py` in conversation artifacts) implementing Lemmas 3–5, Theorem 1, and Part 2 directly from `PROOF.md` and `Arxiv.tex` definitions without reading `verify.py` or `check-check-3.py`.
Command: `/usr/bin/time -p .venv/bin/python -u /Users/kev/.gemini/antigravity/brain/3cfe9781-bc63-4862-af08-44d91c8a1d49/scratch/audit_adversarial_check.py`
- **Exit code:** `0` (`real 2.06`, `user 1.33`, `sys 0.19`, script elapsed `1.47s`)
- **Raw output:**
```
Atlas n=3..7 PASS: counts={3: 2, 4: 5, 5: 15, 6: 58, 7: 272} (total=352), Subcase B2 occurred 97 times across 78 graphs
Structured families (n=3..16) PASS: 118 graphs tested, Subcase B2 occurred 46 times
Part 2 PASS: 42 lattice points (n=3..11) + 14 explicit boundary points verified
PASS
```
- **Specific adversarial findings:**
  1. **Lemma 5 Subcase B2 (`B_r == R` and `R \cap X == \emptyset`):** Actually occurred **97 times across 78** of the 352 connected chordal graphs on $n=3..7$ (testing every simplicial vertex $s$ as root $R = N_G[s]$) and **46 times** across 118 structured connected chordal graphs on $n=3..16$ (paths $P_3..P_{16}$, stars $K_{1,2}..K_{1,15}$, cliques $K_3..K_{16}$, sun graphs $n=6..16$, split graphs $n=3..16$, caterpillars $n=3..16$). In all **143** occurrences, every assertion of Subcase B2 passed: $R \subseteq V(M)$, $R \cap e_r \neq \emptyset$, $R \cap e_j = \emptyset$ ($j \neq r$), $R = e_r = \{u_r, v_r\}$ with $v_r = s$, $\deg_G(v_r) = 1$, every edge intersecting $R$ contains $u_r$, every neighbor $x \in N_G(u_r) \setminus \{v_r\}$ (nonempty) lies in $X$, and $C_r = \{u_r, x\}$ is a clique intersecting $X$ such that $C_1 \cup \dots \cup C_r$ is a vertex cover of $G$.
  2. **Theorem 1 Part 2 Case I / Case II edge cases:** Verified exact $(\mathrm{im}(G), \mathrm{v}(G)) = (r, v)$, connectedness, chordality, and $|V(G)| = n$ for all 42 lattice points in $A(3..11)$ plus 14 explicit boundary points up to $n = 16$ covering $v = 1$, $v = r$, $m = 1$ ($n = 2r+1$), $m = r$ ($n = 3r$), $q = 1$, and $q = m$: `(3,1,1)`, `(6,2,1)`, `(6,2,2)`, `(9,3,1)`, `(9,3,3)`, `(12,4,4)`, `(11,5,1)`, `(13,6,1)`, `(13,5,1)`, `(13,5,4)`, `(14,5,3)`, `(14,5,4)`, `(16,6,4)`, `(16,6,1)`.

# Adversarial Audit Helper Report: `targets/petyuk-2210.14762-conj1/`

**Checked UTC:** `2026-11-27T02:49:13Z`  
**Target:** Anthony V. Petyuk, *"On word-representability of simplified de Bruijn graphs"*, `arXiv:2210.14762v2`, Section 4, Conjecture 1 (`$S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$.`)  
**Isolation respected:** Did not read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, or author scratch files; did not edit `TARGET.md` or `COUNTEREXAMPLE.md`.

---

## 1. Primary-Source & Published-Version Check

### 1.1 Target Directory Check
`ls -la targets/petyuk-2210.14762-conj1/` shows only:
- `COUNTEREXAMPLE.md`
- `TARGET.md`
- `notes/`
- `verify.py`

**Confirmed:** No `CONTESTED.md` is present.

### 1.2 arXiv API Metadata (`tools/arxiv_fetch.py query --id-list 2210.14762,2312.10377,2605.02268`)
- **`2210.14762v2`** — Anthony V. Petyuk, *"On word-representability of simplified de Bruijn graphs"* (`math.CO`)
  - Published: `2022-10-20T07:50:43Z`, Updated: `2023-07-12T01:46:41Z` (latest version is `v2`)
  - `journal_ref`: `""`, `doi`: `""`
  - `comment`: `"24 pages, 2 figures. arXiv admin note: text overlap with arXiv:2110.05405 by other authors"` (note: `arXiv:2110.05405v2` is Kitaev–Sun, cited in the paper's appendix as `\cite{KS}`).
- **`2312.10377v1`** — Sumin Huang, Sergey Kitaev, Artem Pyatkin, *"An embedding technique in the study of word-representabiliy of graphs"* (`math.CO`)
  - Published/Updated: `2023-12-16T08:25:32Z` (`v1`)
  - `comment`: `"To appear in Discrete Applied Mathematics"`, `journal_ref`: `""`, `doi`: `""` on arXiv.
  - Crossref (`10.1016/j.dam.2023.12.017`) confirms journal publication: *Discrete Applied Mathematics*, Vol. 346 (March 2024), pp. 170–182 (`is-referenced-by-count: 1`).
- **`2605.02268v2`** — Suchanda Roy, Ramesh Hariharasubramanian, *"Word-Representability of Shift Graphs"* (`math.CO`, `cs.DM`)
  - Published: `2026-05-04T06:21:59Z`, Updated: `2026-05-22T11:05:19Z` (`v2`)
  - `journal_ref`: `""`, `doi`: `""`, `comment`: `""`.

### 1.3 Journal Publication Check for `2210.14762`
- Crossref API (`query="On word-representability of simplified de Bruijn graphs"` and `query.author=Petyuk`), OpenAlex (`W4307478167`, venue `arXiv`, `cited_by_count: 2`), and web search show **no journal publication** of Petyuk's `2210.14762`.
- In `tools/.arxiv_cache/eprint/2210.14762/simplified_de_Bruijn_graphs__4_.tex`:
  - Section 1.2 (lines 65–67) defines $B(n,k)$ and $S(n,k)$ and states: *"To our best knowledge, the notion of a simplified de Bruijn graph is introduced in this paper for the first time."*
  - Section 4, Conjecture 1 (line 123) reads verbatim: `\begin{conjecture} $S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$. \end{conjecture}`

### 1.4 Status of Petyuk's Conjecture 1 in `2312.10377` and `2605.02268` (Extracted TeX)
- **`2312.10377` (`simpl-deBruijn-final.tex`, lines 341–343 & 897–912):**
  - Lines 341–342 explicitly quote Petyuk's Conjecture 1 as open:
    > *"More specifically, the following conjecture is stated in \cite{Petyuk}:"*  
    > `\begin{conj}\label{conj} $S(n,k)$ is non-word-representable for $n\geq 4$ and $k\geq 3$. \end{conj}`
  - Lines 343 & 897–912 only prove results for distance-restricted induced subgraphs $S_m(n,k)$ ($m \ge 1$) and leave the exact threshold open. They do **not** settle Conjecture 1 ($m=0$).
- **`2605.02268` (`WR_shift_graphs_v1.tex`, lines 115–143 & 357–362):**
  - Note that Roy & Hariharasubramanian swap the parameter order ($S(n,k)$ denotes alphabet size $n$ and word length $k$ in their paper), writing Theorem 2.3 (`\label{th1}`): $S(2,k)$ word-representable, $S(n,2)$ and $S(n,3)$ non-word-representable for $n \ge 3$.
  - They prove all shift graphs $G(n,k)$ and generalized $m$-shift graphs $G_m(n,k)$ are word-representable, noting *"Although simplified de Bruijn graphs contain non-word-representable members in general"* (abstract, line 63). They do **not** address or refute Petyuk's Conjecture 1.

---

## 2. Deep Novelty & Chromatic-Number Prior-Art Check (through `2026-11-27`)

### 2.1 Snapshot, Citation, Preprint & Web Checks for Word-Representability of $S(4,3)$
- **`tools/novelty_grep.py 2210.14762 Petyuk "simplified de Bruijn" "word-representable" "de Bruijn"`:** 21 lines across 13/413 files in `watch/snapshots/**`; 0 matches resolving Petyuk's Conjecture 1 (only `2210.14762` OpenAlex cache & citing stub for this target, plus unrelated `de Bruijn–Erdős` compactness, `de Bruijn 1960`, and `2611.32249v1` path-unique subgraphs).
- **arXiv queries** (`all:2210.14762`, `all:"simplified de Bruijn"`, `all:"de Bruijn" AND all:"word-representable"`, `all:"de Bruijn" AND all:"chromatic number"`): only `2210.14762v2`, `2312.10377v1`, and `2605.02268v2` concern word-representability of simplified de Bruijn / shift graphs; `2411.05931v1` and `1710.00475v3` concern the de Bruijn–Erdős compactness theorem.
- **OpenAlex citing works for `2210.14762` (`W4307478167`):** `cited_by_count: 2` (`2312.10377` and `2605.02268`). Citing works for `2312.10377` (`W4390150971`): 4 papers (3 on split/co-bipartite/5-regular circulant graphs, plus `2605.02268`). None claim $S(4,3)$ is word-representable or refute Conjecture 1.
- **Zenodo (`https://zenodo.org/api/records`):** 0 results for `2210.14762 OR "simplified de Bruijn"`.
- **Crossref & `search_web`:** 0 papers (2022–2026) refuting Petyuk's Conjecture 1 or proving $S(4,3)$ is word-representable.

### 2.2 CRITICAL PRIOR-ART FINDING: Classical Chromatic Number $\chi(S(4,3)) = 3$ (and $\chi(S(n,3)) = 3$ for $n \ge 4$) Already Proved in 2010
In the 2005–2010 **alphabet-overlap / $\alpha$-overlap graph** literature, Petyuk's simplified de Bruijn graph $S(n,k)$ was studied earlier under a different name and notation:
- **Definition equivalence:** In Godbole–Knisley–Norwood (2005, `arXiv:math/0510094v1`, denoted $G(k,d,s)$ with overlap $t = k-s$) and Knisley–Nigussie–Pór (2010, denoted $G(a,k,t)$), the $\alpha$-overlap graph $G(a,k,t)$ has vertex set $A^k$ ($|A|=a$) and an edge between distinct $u \ne v$ iff the last $t$ letters of $u$ equal the first $t$ letters of $v$, or vice versa. For $t = k-1$, $G(a, k, k-1)$ is **literally identical** to Petyuk's simplified de Bruijn graph $S(k, a)$ (in particular, $G(3, 4, 3) = S(4, 3)$).
- **Godbole, Knisley, and Norwood (2005), *"Some Properties of Alphabet Overlap Graphs"*, `arXiv:math/0510094v1`:** Solved $\chi(G(k,d,s))$ for $s \ge k/2$ ($t \le k/2$) and explicitly listed $s=1$ (`t = k-1`, i.e., $\chi(S(k,d))$) as an **Open Problem** in Section 6 (line 486: *"What is $\chi(G(k,d,s))$ when $s=1$?"*).
- **Debra Knisley, Yared Nigussie, and Attila Pór (2010), *"On the chromatic number of the $\alpha$-overlap graphs"*, *Journal of Combinatorial Mathematics and Combinatorial Computing (JCMCC)*, Vol. 73 (2010), pp. 3–13:**
  - Web search results referencing Combinatorial Press and ETSU report that Knisley–Nigussie–Pór (2010) **already proved $\chi(G(3, 4, 3)) = 3$** (i.e., **$\chi(S(4,3)) = 3$**) and **$\chi(G(3, k, k-1)) = 3$ for all $k \ge 4$** (i.e., **$\chi(S(n,3)) = 3$ for all $n \ge 4$**).
  - Specifically, the reported proof for $G(3,4,3)$ deletes the 26-vertex independent set
    $$I = \{ *10*, *12*, 0000, 2222, 200(* \setminus 0), 022(* \setminus 2), (* \setminus 1)111 \}$$
    (where $*$ denotes any symbol in $\{0,1,2\}$ and $(*\setminus i)$ denotes any symbol other than $i$) and shows the remaining 55-vertex induced subgraph is bipartite.
  - **Independent verification in Python:** We verified directly on $S(4,3)$ (81 vertices, 237 edges) that this exact 26-vertex set $I$ has `len(I) == 26`, `0` internal edges, and `V \ I` (55 vertices) is indeed bipartite (`is_bipartite: True`).
- **(Note on other classical de Bruijn coloring literature checked):** Linial (1992, *SIAM J. Comput.* 21(1):193–201) addresses distributed local coloring bounds and shift graphs ($G(n,k)$); Lempel (1971) studies extremal factors/homomorphisms of de Bruijn graphs; Bond–Delorme and Bermond–Peyrat / Bermond–Hell (1993) study degree-diameter constructions and edge-chromatic index / factorizations of de Bruijn and Kautz digraphs. None of those older works settle $\chi(S(4,3)) = 3$; the exact prior proof of $\chi(S(4,3)) = 3$ is Knisley–Nigussie–Pór (2010).

#### Exact Novelty Boundary Assessment for `@audit-2`:
1. **Did Knisley–Nigussie–Pór (2010) or anyone else settle Petyuk's Conjecture 1 or word-representability of $S(4,3)$?**
   - **No.** Knisley–Nigussie–Pór (2010) appeared **6 years before** Halldórsson–Kitaev–Pyatkin (2016, *Discrete Appl. Math.* 201:164–171) proved that every 3-colorable graph is word-representable, and **12 years before** Petyuk (2022) stated Conjecture 1.
   - Petyuk (`2210.14762v2`, line 67) was unaware of the $\alpha$-overlap graph literature (*"To our best knowledge, the notion of a simplified de Bruijn graph is introduced in this paper for the first time"*).
   - Across arXiv, Crossref, OpenAlex, Zenodo, and web searches, **no paper from 2010–2026** has cited Knisley–Nigussie–Pór (2010) in connection with word-representability, semi-transitive orientability, or Petyuk's Conjecture 1, nor proved that $S(4,3)$ is word-representable.
2. **What is NOT new vs. what IS new in `COUNTEREXAMPLE.md`:**
   - **Not new in print:** The fact that $S(4,3)$ is 3-colorable ($\chi(S(4,3)) = 3$) was already proved in Knisley–Nigussie–Pór (2010) under the name $G(3,4,3)$ (via a `26/55` independent-set + bipartite decomposition), though `COUNTEREXAMPLE.md` constructs a different, $\mathbb{Z}_3$-shift-equivariant (`27/27/27`) 3-coloring `c(x) = (x_1 + f(d_1,d_2,d_3)) mod 3`.
   - **New:** Deducing from 3-colorability (and constructing an explicit length-4536 representing word $w$) that **$S(4,3)$ is word-representable**, thereby **refuting Petyuk's Conjecture 1** (`arXiv:2210.14762v2`, Section 4). Under `CHARTER.md` ("every result must be new, meaning nobody has already settled that exact statement"), Petyuk's exact statement has not been settled in print, though `@audit-2` should explicitly cite Knisley–Nigussie–Pór (2010) if desired for scholarly accuracy.

### 2.3 Competing GitHub Repositories Search
Searched via read-only `gh search code` / `gh search repos` for `2210.14762`, `Petyuk`, `"simplified de Bruijn"`, `word-representable` across:
- `the-omega-institute/trureturing*` (16 repos listed; checked main active repos — `trureturing` has only `aksoyetal2023asynchrony` for `Petyuk` i.e. `2303.11464`, and `debruijnerdos1951` / `debruijn1960` for `de Bruijn`; 0 matches for `2210.14762` or `word-representable`)
- `aliromman/math`: 0 matches
- `KnowledgeSense/math`: 0 matches
- `1337isnot1337/solved-conjectures`: 0 matches
- `rainwangphy/aftd-platform`: 0 matches
- `valyuAI/research`: 0 matches
- `facebookresearch/atlas-lean`: 0 matches
- `JENW1N/complete-math-solutions`: 0 matches
- `TheJustinSunPrize/awards`: 0 matches
- `openai/math`: 1 unrelated hit for `word-representable` (`DiagonalCalendarLookupHostAddressBounds.lean`); 0 hits for `2210.14762` / `Petyuk` / `de Bruijn`
- `GuillaumeBAUD-coder/open-math-agents`: only `wikipedia_unsolved.wiki` and `de_bruijn_erdos` Lean files; 0 hits for `2210.14762` / `Petyuk` / `simplified de Bruijn`
- `DomTheDeveloper/open-math-agents`: 0 matches
- `DomTheDeveloper/ProofPlaygrond`: 0 matches
- `google-deepmind/formal-conjectures`: 0 matches
- Global `gh search code`: `LeanPool/lean-pool` (`WordRepTensor` — tensor products / Mycielski graphs) and `tadamcz/autoformalization-results` (Glen's theorem on near-triangulations); **0 hits** anywhere on GitHub for `2210.14762`, Petyuk's Conjecture 1, or word-representability of $S(4,3)$.

---

## 3. Independent Exact Computation Check

### 3.1 Execution of `notes/check-check-1.py`
Command:
```sh
time .venv/bin/python -u targets/petyuk-2210.14762-conj1/notes/check-check-1.py
```
Exact raw output:
```text
S(4,3) (81 vertices, 237 edges), triangle, 80 nonzero tuples, & 3-coloring (27/27/27): OK
Explicit representing word (len=4536, M=28, lex order) across all 3240 pairs: OK
Explicit representing word (arbitrary shuffled class order) across all 3240 pairs: OK
PASS
.venv/bin/python -u targets/petyuk-2210.14762-conj1/notes/check-check-1.py  0.14s user 0.02s system 85% cpu 0.192 total
```
- **Exit code:** `0`
- **Wall-clock runtime:** `0.192s`

### 3.2 Verbatim Table & Case-Line Verification of `COUNTEREXAMPLE.md`
An independent Python parser compared `COUNTEREXAMPLE.md` lines 20–30 and every case claim in lines 38–49 directly against `check-check-1.py`'s `TABLE_F`:
- **Lines 22–30 (`(d1, d2)` -> `(f(d1,d2,0), f(d1,d2,1), f(d1,d2,2))`):**
  - `(0,0): (1,2,2)`
  - `(0,1): (0,0,0)`
  - `(0,2): (1,1,1)`
  - `(1,0): (1,2,1)`
  - `(1,1): (1,1,1)`
  - `(1,2): (2,1,2)`
  - `(2,0): (2,0,2)`
  - `(2,1): (2,2,2)`
  - `(2,2): (0,2,0)`
  - **Result:** Exact 1-to-1 match with `TABLE_F` in `check-check-1.py` (zero typos).
- **Lines 38–49 (all 3 cases `d1 = 0, 1, 2` and all subcases `d2 = 0, 1, 2`, `d3 = 0, 1, 2`):**
  - Every function evaluation `f(d1, d2, d3)` and every image set `d1 + f(d2, d3, d4) mod 3` stated in lines 38–49 was checked programmatically against `TABLE_F` and verified **100% exact** with zero discrepancies.

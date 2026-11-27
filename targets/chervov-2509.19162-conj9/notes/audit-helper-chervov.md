# Adversarial Audit Helper Report: `targets/chervov-2509.19162-conj9/`

- **Target**: `targets/chervov-2509.19162-conj9/` (Conjecture 9 of A. Chervov et al., `arXiv:2509.19162v2`)
- **Audit date (UTC)**: `2026-11-27T06:22Z`
- **Target directory check**: `ls -la targets/chervov-2509.19162-conj9/` shows `COUNTEREXAMPLE.md`, `TARGET.md`, `notes/`, and `verify.py`. **No `CONTESTED.md` present.**

---

## 1. Primary-Source & Verbatim TeX Check (`arXiv:2509.19162v2` + OEIS `A136184`)

### 1.1 arXiv Metadata (`.venv/bin/python tools/arxiv_fetch.py query --id-list 2509.19162`)
- **Latest version**: `2509.19162v2` (`https://arxiv.org/abs/2509.19162v2`)
- **Title**: *CayleyPy Growth: Efficient growth computations and hundreds of new conjectures on Cayley graphs (Brief version)*
- **Authors**: A. Chervov, D. Fedoriaka, E. Konstantinova, A. Naumov, I. Kiselev, et al. (49 authors)
- **Dates**: Published `2025-09-23T15:40:36Z`; Updated `2026-04-01T15:54:42Z`
- **Categories**: `math.CO` (primary), `cs.LG`, `hep-th`, `math.GR`
- **Comment**: `46 pages, 30 figures; v2: typos fixed`
- **Journal-ref / DOI**: `""` / `""` (none recorded on arXiv)

### 1.2 Verbatim TeX Inspection (`tools/.arxiv_cache/eprint/2509.19162/mainv2.tex`)
- Line 85 defines `\newtheorem{Conj}{Conjecture}`. Counting `\begin{Conj}` environments in `mainv2.tex` (lines 1025, 1034, 1748, 1942, 1998, 2089, 2111, 2209, 2229, 2239, 2382, 2432, 2700, 2832), lines 2229–2231 are indeed the **9th** `\begin{Conj}` environment (**Conjecture 9**).
- Entire Subsection *"Bounds on the diameters of unitriangular groups"* (lines 2203–2236):
  - **Lines 2203–2208**:
    ```latex
    \subsection{Bounds on the diameters of unitriangular groups}
    J.~Ellenberg in \cite{ellenberg1993diameter}, and later jointly with J.~Tymoczko  \cite{ellenberg2005unipotent}, established that the diameters of $U(n,\mathbb{Z}/p\mathbb{Z})$, the unitriangular groups over prime fields, are within a constant factor of $np+n^2\log(p)$ (see also enjoyable introductions in J.~Ellenberg's blog: \href{https://quomodocumque.wordpress.com/2010/07/03/in-which-i-publish-my-first-paper/}{1},
    \href{https://quomodocumque.wordpress.com/tag/diameter/}{2}).
    Here the group is considered with respect to the generators $E\pm E_{i,i+1}$ (fundamental roots). Experimentally, we see that starting from large enough $m$, the diameters of $U(n,\mathbb{Z}/m\mathbb{Z})$ are in fact linear in $m$, see Fig.~\ref{fig:unitriangular_diameters}. In particular, for $n=3$ and $m=8,\ldots,50$ the diameter equals $2\lfloor\frac{m}{2}\rfloor$, while for $n=4$ and $m=12,\ldots,31$ it is $3\lfloor\frac{m}{2}\rfloor$.

    Another natural choice of generators is elementary transvections corresponding to all positive roots, i.e. $E\pm E_{ij}$ for $i<j$. One can also consider the directed Cayley graphs corresponding to monoid generators of the form $E+E_{i,i+1}$ or $E+E_{ij}$, respectively, thus providing four basic options: fundamental/positive and undirected/oriented.
    ```
  - **Lines 2228–2235 (Conjecture 9 verbatim)**:
    ```latex
    Computational evidence also suggests the following
    \begin{Conj}
    The diameter of $U(n,\mathbb{Z}/2\mathbb{Z})$ with respect to the fundamental root transvections is equal to the number of metacyclic groups of order $2^n$ (\href{https://oeis.org/A136184}{OEIS A136184}).  
    \end{Conj}

    Notebooks: \href{https://www.kaggle.com/code/alexandervc/growth-ut4-analysis}{UT4},
    \href{https://www.kaggle.com/code/alexandervc/growth-ut5-6-7-8-etc-analysis}{UT5etc},
    \href{https://www.kaggle.com/code/alexandervc/growth-in-finite-groups-heisenberg-uptriag-etc}{various groups}.
    ```
- **Quantifier on $n$**: Conjecture 9 leaves $n$ **unqualified** (no $n \ge 3$ restriction). Over $\mathbb{Z}/2\mathbb{Z}$, $E + E_{i,i+1} = E - E_{i,i+1}$ are involutions, so undirected and oriented Cayley graphs coincide.
- **Range of $n$ tabulated in the paper**: `mainv2.tex` does **not** tabulate numerical diameter values for $n = 2, 3, 4, 5, 6, 7$ at $m = 2$; it only states $n=3$ ($m=8,\dots,50$) and $n=4$ ($m=12,\dots,31$) in line 2206, embeds `figs/unitriangular_diameters.png` (lines 2219–2224), and links the Kaggle notebooks `UT4`, `UT5etc`, and `various groups` (lines 2233–2235). Neither `tab:long1` nor `tab:long2` includes unitriangular groups.
- **Ellenberg–Tymoczko $O(n^2)$ vs `A136184` growth rate**: Line 2204 explicitly cites Ellenberg–Tymoczko's $\Theta(np + n^2\log(p))$ bound (which is $\Theta(n^2)$ for $p=2$). However, `mainv2.tex` **never** mentions `A136184`'s cubic growth rate ($\sim n^3/72$) or the asymptotic contradiction with Ellenberg–Tymoczko.

### 1.3 Live OEIS `A136184` Check (`https://oeis.org/search?q=id:A136184&fmt=json`)
- **Revision & timestamp**: `revision: 31`, `time: 2026-09-17T22:32:10-04:00`, `created: 2008-06-29T03:00:00-04:00`, `offset: "1,2"`.
- **`data`**: `1,2,4,8,12,19,26,37,48,63,78,...` — confirms $M(1)=1, M(2)=2, M(3)=4, M(4)=8, M(5)=12, M(6)=19, M(7)=26, M(8)=37$.
- **`comment`**: `"For number of metacyclic groups of order p^n, prime p >= 3, see A136185."`
- **`formula`**:
  - G.f.: `-x*(x^10 + x^9 - x^8 + x^6 - x^3 - x - 1)/((x - 1)^4*(x + 1)^2*(x^2 + x + 1)).`
  - Liedahl / M. F. Hasler closed form for $n > 3$: `a(n) = (n^3 + 48*n^2 - c*n + d)/72`, where `c = 168` (even $n$) or `177` (odd $n$), and `d = 432, 416, 424` for $n \equiv 0, 1, 2 \pmod 3$.
- **`link`**: Explicitly cites:
  - `A. Chervov et al., CayleyPy Growth: Efficient growth computations and hundreds of new conjectures on Cayley graphs (Brief version), arXiv:2509.19162 [math.CO], 2025. See p. 27.`
  - `Steven Liedahl, Enumeration of metacyclic p-groups, J. Algebra 186 (1996), no. 2, 436-446.`
- **Refutation status on OEIS**: **No** mention of a disproof, correction, or withdrawal of Conjecture 9, nor any `U(n, Z/2Z)` formula beyond the Chervov et al. `2509.19162` citation.

---

## 2. Deep Novelty Check (through `2026-11-27`)

### 2.1 arXiv Queries (`tools/arxiv_fetch.py`) & Citing Papers
- `all:2509.19162` → 1 entry (`2509.19162v2`, updated `2026-04-01`).
- `all:CayleyPy` → 3 entries:
  1. `2603.22195v1` (*CayleyPy-4: AI-Holography*, `2026-03-23`, 20+120 pp.) — inspected full eprint (`tools/.arxiv_cache/eprint/2603.22195/`): cites `2509.19162` as `Cayley3Growth` in `biblio.bib` and `main_holography.tex` (lines 628, 657, 667, 677, 846, 1544, 4728, 6380, 8236), with **0** mentions of `A136184`, `unitriangular`, `metacyclic`, or Conjecture 9.
  2. `2509.19162v2` (*CayleyPy Growth*).
  3. `2502.18663v3` (*CayleyPy RL*, updated `2026-05-15`, DOI `10.4310/ATMP.260413005111`).
- `au:Chervov` → 25 entries; newest (`2610.22571v1` *Quantum Periods from TBA and Continued Fractions*, `2603.22195v1` *CayleyPy-4*) do not mention `U(n, Z/2Z)`, `A136184`, or Conjecture 9.
- `all:A136184` → 0 entries.
- `all:unitriangular AND all:diameter` → 3 entries: `2608.09235v1` (commuting graph of $UT(4;p)$), `2509.19162v2`, and `2002.08870v2` (El-Baz–Pagano, random Cayley graphs of finite nilpotent groups).
- `all:metacyclic AND all:unitriangular` → 0 entries.
- Citing papers seen via `tamnd/arxiv` (`2610.08385` *Cayley graph diameters for fixed cycle types are eventually quasipolynomial*; `2610.14373` *Transposition Cayley Spectra and Subgraph Counts*) and `watch/snapshots/arxiv/citing/chervov-2509.19162-conj9.json` (`citing_count: 0` in snapshot): neither touches unitriangular groups or `A136184`.

### 2.2 Local Watch Snapshots (`tools/novelty_grep.py`)
- `.venv/bin/python tools/novelty_grep.py 2509.19162 A136184 CayleyPy unitriangular metacyclic`: 11 lines across 9/522 files in `watch/snapshots/**` (`1337-solved-conjectures` `LOCAL_LAW.md`/issues/PRs on contracting rank projection; `JamieLittle16__HessianConjecture4` `UnitriangularBlock.lean`; `the-omega-institute__trureturing` `CayleyPyConjectureOneRefutation`; `arxiv/` caches). None touch Conjecture 9, `U(n, Z/2Z)`, or `A136184`.

### 2.3 Crossref, Zenodo, OpenAlex, and Web Search
- **Crossref** (`api.crossref.org/works?query=2509.19162`, `query=A136184`): 0 relevant hits.
- **Zenodo** (`zenodo.org/api/records?q=2509.19162`, `q=A136184`): `total: 0` for both.
- **OpenAlex**: Live API returned HTTP 429 (`reason: daily_budget`); local `watch/snapshots/arxiv/openalex_works_cache.json` (checked `2026-11-27T05:01:41Z`) records `2509.19162` under `W7220911601` with `cited_by_count: 0`.
- **Web search** (`search_web` for `"2509.19162" "Conjecture 9"`, `"CayleyPy" "A136184"`, `"CayleyPy" "metacyclic" OR "unitriangular"`, `"U(n, Z/2Z)" "A136184" OR "metacyclic" "unitriangular" diameter`): surfaces only `arXiv:2509.19162` and OEIS `A136184`/`A007982`; no disproof or resolution found.

### 2.4 Read-Only GitHub Checks (`gh`)
- **CayleyPy ecosystem** (`cayleypy/cayleypy`, `cayleypy/cayleypy-docs`, `cayleypy/cayleypy-seminars`, `chervov/*`, `Alexandervc/*`):
  - `cayleypy/cayleypy` PR #213 (`Add unitriangular_fundamental_roots`, merged `2026-09-26T18:02:52Z`) added `GraphsLibrary.unitriangular_fundamental_roots(n, modulo)` (`cayleypy/graphs_lib.py`) and growth CSVs `cayleypy/data/unitriangular_2_fund_roots_growth.csv` ($n=2$, $m=2..10$) and `cayleypy/data/unitriangular_3_fund_roots_growth.csv` ($n=3$, $m=2..5$; at $m=2$ growth is `[1, 2, 2, 2, 1]`, diameter 4).
  - Checked all issues/PRs (pages 1–3), `README.md`, and repo tree: **0** mentions of `A136184`, `metacyclic`, or any refutation/withdrawal of Conjecture 9.
- **`the-omega-institute/trureturing*`** (`trureturing`, `trureturing-tools`, `trureturing-experiments`, `automath`, `mathesis`, `trureturing-pages`, `trureturing-mdbook`):
  - Settled CayleyPy results in `trureturing` (`Problems/`, `Blueprint/D5/S0/CayleyGrowth/`, issues):
    - `2509.19162` Conjectures 1 & 2 (`CayleyPyConjectureOneRefutation`, `QuasipolynomialWordMetricRefutation`, `Library/CayleyGrowth/chervov2025cayleypy.md`).
    - `2603.22195` (CayleyPy-4) Conjectures 11, 15, 16 (`ConsecutiveFourCycleDiameterRefutation`, `chervov-2026-cayleypy4-conjecture-eleven-refutation.md`, `-fifteen-refutation.md`, `-sixteen-refutation.md`, `three-cycle-grassmannian-diameter.md`, issues `#10230`, `#10252`, `#10253`, `#11712`, `#11747`).
    - 3-pancake / prefix-reversal conjectures (`PrefixReversalTripleCountRefutation`, `PrefixReversalTripleEvenNonGeneration`, `PrefixReversalTripleOddNonGeneration`).
    - `NikolovSegal/TypeA/Unitriangular` & issue `#28156` concern Nikolov–Segal width over large odd prime fields.
  - **0** files, issues, or PRs touch `2509.19162` Conjecture 9, `U(n, Z/2Z)`, `A136184`, or metacyclic groups.
- **Competing repositories & global GitHub searches**:
  - Checked trees/issues/files across `1337isnot1337/solved-conjectures` (`CONTENTS.md`, `HISTORY.md`, issues), `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `openai/math`, `google-deepmind/formal-conjectures`, `mathesis-papers/*` (`catalog`, `trureturing`), plus watchlist repos (`dvgyl/oeis-proofs`, `joaquimmj/oeis-conjectures`, `ArtificialZeng/AI-Has-Taste`, `OjasMor/arxiv-conjectures`, `Wangwy-sjtu/lean-conjecture-proofs`, `adamben04/open-conjectures`, `0thernes/0thernes-research-archive`, `yashvirsabharwal/conjecture-assault`, `LuminaBench/solved-conjectures`), and global `gh search code`/`gh search issues` for `"2509.19162"`, `"A136184"`, `"CayleyPy unitriangular"`, `"CayleyPy metacyclic"`.
  - **0** hits settling or refuting Conjecture 9 (`diam(U(n, Z/2Z)) = A136184`).

---

## 3. Independent Exact Computation Check

### 3.1 Existing Check Script (`notes/check-check-3.py`)
Command: `/usr/bin/time -p .venv/bin/python -u targets/chervov-2509.19162-conj9/notes/check-check-3.py`
- **Exit code**: `0`
- **Timing**: `real 1.72`, `user 1.48`, `sys 0.09`
- **Raw output**:
  ```
  Part 1 PASS: exact BFS diam(U(2..5,F_2))={1,4,8,12} and word factorization <= 2n^2-6n+5 verified up to n=176.
  Part 2 PASS: metacyclic group laws, Z(G), G', and invariant-factor distinctness verified on n=6,7,8.
  Part 3 PASS: |F_176|=61404 > 60901, |F_n| > 2n^2-6n+5 for 178<=n<=500, and n>=195 algebraic bound verified.
  PASS
  ```

### 3.2 Independent Exact Bitmask BFS + `|F_n|` + OEIS `A136184` Generating Function Check
Ran a standalone Python script (1 core, 15s `SIGALRM` timeout; `real 0.86`, `user 0.51`, `sys 0.13`, exit code `0`):
- **Exact BFS on $U(n, \mathbb{F}_2)$ with fundamental root transvections $s_k = I + E_{k,k+1}$ ($n = 2..6$)**:
  - `n=2`: `|U(2,F_2)|=2`, `diam=1` (`0.0000s`) — vs OEIS `M(2)=2` (immediate counterexample!)
  - `n=3`: `|U(3,F_2)|=8`, `diam=4` (`0.0000s`) — matches `M(3)=4`
  - `n=4`: `|U(4,F_2)|=64`, `diam=8` (`0.0001s`) — matches `M(4)=8`
  - `n=5`: `|U(5,F_2)|=1024`, `diam=12` (`0.0016s`) — matches `M(5)=12`
  - `n=6`: `|U(6,F_2)|=32768`, `diam=19` (`0.0741s`) — matches `M(6)=19`
- **OEIS `A136184` Generating Function vs Liedahl/Hasler Formula ($n=1..200$)**:
  - Exact power-series recurrence from `-x*(x^10 + x^9 - x^8 + x^6 - x^3 - x - 1)/((x - 1)^4*(x + 1)^2*(x^2 + x + 1))` matches the Liedahl/Hasler formula identically for all $n=1..200$:
    `M(1..10) = [1, 2, 4, 8, 12, 19, 26, 37, 48, 63]`.
- **Verification of `|F_n|` and `2n^2 - 6n + 5` (`COUNTEREXAMPLE.md` line 100)**:
  - `n=175`: `ub = 60205`, `|F_175| = 59383`, `M(175) = 94428`
  - `n=176`: `ub = 60901`, `|F_176| = 61404` (`> ub`), `M(176) = 95965`
  - `n=177`: `ub = 61601`, `|F_177| = 61404` (`< ub`), `M(177) = 97474`
  - `n=178`: `ub = 62305`, `|F_178| = 63470` (`> ub`), `M(178) = 99043`
  - `|F_n| > 2n^2 - 6n + 5` holds for `n = 176` and all `178 <= n <= 200` (matching `COUNTEREXAMPLE.md` line 100). (Externally, OEIS `M(n) > 2n^2 - 6n + 5` already holds at `n = 2` and for all `n >= 94`.)

---

## Audit Summary
1. **Statement fidelity**: `arXiv:2509.19162v2` Conjecture 9 (lines 2229–2231) matches `TARGET.md` verbatim and leaves $n$ unqualified.
2. **Novelty**: **CLEAR** across arXiv (`2509.19162v2`, `2603.22195v1`, `2610.08385`, `2610.14373`, `au:Chervov`), OEIS `A136184` (rev 31, `2026-09-17`), `cayleypy/cayleypy` (including PR #213), `the-omega-institute/trureturing*`, all 17 competing GitHub repos, watchlist snapshots, Crossref, and Zenodo (only OpenAlex live API was rate-limited 429, covered locally by `openalex_works_cache.json`).
3. **Exact computation**: Both `notes/check-check-3.py` (`PASS`, `1.72s`) and independent bitmask BFS (`diam(U(6, F_2)) = 19`) + `|F_n|` + OEIS `A136184` GF checks pass cleanly.

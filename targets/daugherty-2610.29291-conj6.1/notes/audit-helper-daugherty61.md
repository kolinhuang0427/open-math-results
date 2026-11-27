# Adversarial Audit Helper Report — `daugherty-2610.29291-conj6.1`

- **Audit Helper:** `daugherty61-audit-hlp` (reporting to `@audit-3`)
- **Timestamp (UTC):** `2026-11-27T02:30:00Z`
- **Target:** `targets/daugherty-2610.29291-conj6.1/` (Daugherty et al., `arXiv:2610.29291v1`, Section 6, Conjecture 6.1 `\label{conj:box}`)
- **Isolation compliance:** Did NOT read `verify.py` or `notes/screen-*`; did NOT edit `TARGET.md` or `COUNTEREXAMPLE.md`.

---

## 1. Primary-Source, Directory & Compiled Numbering Checks

### 1.1 arXiv Version & Directory Status
- **arXiv API query:** `.venv/bin/python tools/arxiv_fetch.py query --id-list 2610.29291`
  - `total_results: 1`
  - Sole & latest version: `2610.29291v1`, `published: 2026-10-21T06:45:39Z`, `updated: 2026-10-21T06:45:39Z`, `primary_category: math.CO`, `comment: "13 pages, comments welcome!"`, `journal_ref: ""`, `doi: ""`.
  - Note minor spelling discrepancy in upstream metadata: arXiv API metadata lists `"Michaela Fahnesock"`, whereas `final.tex` (line 73) and compiled PDF (`2610.29291.pdf`, page 1) spell `"Michaela Fahnestock"`.
- **Target directory check (`ls -la targets/daugherty-2610.29291-conj6.1/`):**
  - Present: `COUNTEREXAMPLE.md`, `TARGET.md`, `verify.py`, `notes/` (`check-check-3.md`, `check-check-3.py`, `novelty-gate2-watch-1.md`, `novelty-gate2-watch-2.md`, `novelty-gate2-watch-5.md`, `screen-scout2-1.md`, `search_box.py`, `search_box2.py`, `search_box3.py`).
  - **No `CONTESTED.md`** is present.

### 1.2 Verbatim Statement & Compiled Section 5 Numbering (`final.tex` + `2610.29291.pdf`)
- **Conjecture 6.1 (`final.tex` lines 717–719; PDF p. 12):**
  > If $\lambda$ and $\mu$ are wide partitions where $\lambda_i = \mu_i + 1$ for some $i \in [\ell(\lambda)-1]$ and $\lambda_j = \mu_j$ when $j \neq i$, then $LT(\lambda) \geq LT(\mu)$.
  `TARGET.md` line 20 and `COUNTEREXAMPLE.md` line 9 match this verbatim.
- **Section 5 compiled numbering discrepancy in `TARGET.md`:**
  In `final.tex` (lines 37–46), `theorem`, `conjecture`, `proposition`, `corollary`, and `lemma` all share the `theorem` counter `[section]`. Checking `tools/.arxiv_cache/pdf/2610.29291.pdf` (pages 10–11) directly confirms Section 5's compiled numbering:
  - **Proposition 5.1** (`final.tex` lines 646–652): $(\lambda, 1) = \mu \implies LT(\lambda) \ge LT(\mu)$.
  - **Proposition 5.2** (`final.tex` lines 655–673): $\lambda_1 \ge \max\{\lambda_i + i - 1 : 2 \le i \le \ell(\lambda)\}$ lower-subtableau extension.
  - **Corollary 5.3** (`final.tex` lines 675–677, `\label{cor:addrow}`).
  - **Lemma 5.4** (`final.tex` lines 686–692): $LT(\lambda) = \sum_{T \in \mathcal{LT}(\lambda^{(r)})} \mathrm{per}(A_{\lambda_r}(T))$. *(Note: not "Lemma 5.3"; 5.3 is Corollary 5.3.)*
  - **Proposition 5.5** (`final.tex` lines 695–701): If $\lambda, \mu$ are wide with $\lambda = (\mu_1 + 1, \mu_2, \ldots, \mu_\ell)$, then $LT(\lambda) \ge LT(\mu)$.
  - **Issue in `TARGET.md` line 25:** `TARGET.md` states *"By Theorem 5.2 (line 651–701), the case $i = 1$ (adding a box to the top row) holds unconditionally"*. Both the label (`Theorem 5.2` vs compiled **Proposition 5.5**) and line range (`651–701` begins inside the proof of Proposition 5.1; Proposition 5.5 is lines 695–701) are inaccurate in `TARGET.md`.
- **Also checked Section 2 & 3:**
  - Definition 2.2 (wide, `final.tex` lines 263–265); Proposition 2.4 (lower-subpartition criterion for wideness, lines 302–304); Definition 2.5 (Latin tableau of shape $\lambda$ and type $\mu$, lines 306–308); Theorem 3.2 (`\label{thm:wide-strict-rep}`, lines 440–454, cited at line 721 for $\mu = (6,5,5,3,2,1)$).

---

## 2. Deep Novelty Check (Oct 21 – Nov 27, 2026)

### 2.1 Local Snapshots (`tools/novelty_grep.py`)
- Ran `.venv/bin/python tools/novelty_grep.py 2610.29291 Daugherty "conj:box" "6,5,5,3,3,1" "6, 5, 5, 3, 3, 1" "Latin tableaux"` across **413 snapshot files**.
- **7 matching lines across 5 files:**
  1. `watch/snapshots/arxiv/citing/daugherty-2610.29291-conj6.1.json` (target entry)
  2. `watch/snapshots/arxiv/openalex_works_cache.json` (metadata for `2610.29291`)
  3. `watch/snapshots/discovered/CATALOG.md`, `catalog.json`, `rainwangphy__aftd-platform.json` (explicitly noting `rainwangphy/aftd-platform` settled **Conj 6.3**).
- **0 matches** for `conj:box`, `6,5,5,3,3,1`, or `6, 5, 5, 3, 3, 1` across all 413 snapshots.

### 2.2 Competing GitHub Repositories (read-only `gh api` / `gh search`)
1. **`the-omega-institute/trureturing` (plus `trureturing-tools`, `trureturing-mdbook`):**
   - Tree searches (`latin|2610|daugherty|wide`): `trureturing-tools` = 0 hits; `trureturing-mdbook` = 0 hits; `trureturing` has files under `Blueprint/D5/S3/Combinatorics/Latin/Tableaux/` (`Source`, `MatchingTemplate`, `Counting`) and `Library/Combinatorics/daugherty2026counting.md` / `Problems/daugherty-latin-tableaux-conjecture63.md`.
   - `Library/Combinatorics/daugherty2026counting.md` explicitly states: *"Conjectures 6.1, 6.2 and the broader wide partition conjecture are separate assertions."*
   - Issues search in `trureturing`:
     - `2610.29291`: 1 hit (`#20269`, open preregistration for **Conjecture 6.3**).
     - `Daugherty`: 5 hits (`#20269` Conj 6.3 open; `#20329` Conj 6.3 closed PR/issue; `#26377` Conj 6.2 open; `#24283` and `#24265` on `2610.39257` Stable Tamari).
     - `conj:box`: 0 hits.
     - Inspected `#26377` directly via `gh api`: titled *"Research unit 189: Daugherty et al. Conjecture 6.2 — column-addition count monotonicity"*, states `If \lambda=(1)^k+\mu with \mu'_1\le k\le \mu'_1+1, then LT(\lambda)\ge LT(\mu)`, and explicitly notes: *"This is a separate count comparison from Conjecture 6.1 and from the full wide-partition conjecture."*
   - Code search in `trureturing` for `6,5,5,3`: 1 hit (`D5/S3/Arith/Additive/PlasticExtremal.lean`), confirmed to be unrelated numeric arrays (`[6,5,5,3,5,3,3,1,...]`).
2. **`rainwangphy/aftd-platform`:**
   - Full tree filter (`latin|2610|daugherty`) and `search/code` (`2610.29291` -> 35 files; `LatinTableaux` -> 13 files):
     - Formalizes Section 2/3/4 definitions & Theorem 3.4, **Proposition 5.5** (`LatinTableauxCountMonoCellAdditionTopRow.lean`), and settles **Conjecture 6.3** (`LatinDoubleThreeTail*`, `web/blog/2026-10-26-op-512.json`, `2026-10-27-op-512.json`, `web/monthly/2026-10.json`, `web/weekly/2026-W44.json`).
     - **Important near miss inspected:** `lean/AFTD/Kb/Tcs/LatinTableauxCountMonoThreeTwoOne.lean` (with provenance `"helper lemma. arXiv:2610.29291 Conjecture 6.1"`) ONLY proves the positive $n=6 \to 7$ case `LT((3,2,1)) <= LT((3,3,1))` (specifically $1 \le 1 \le LT((3,3,1))$). It does NOT refute Conjecture 6.1 or mention `(6,5,5,3,2,1)` / `(6,5,5,3,3,1)`.
     - `search/code` for `6,5,5,3` -> 0 hits; `"6, 5, 5"` -> 1 hit (`BapatSunderWitnessFactor.lean`, unrelated); issues -> 0 hits.
3. **`valyuAI/research`:**
   - Full tree and `search/code` (`2610.29291` -> 6 files) are exclusively under `maths/combinatorics/latin-squares/latin-tableaux-staircase-count/` (plus `public-release/papers/latin-tableaux-staircase-count.pdf`), settling **Conjecture 6.3**.
   - Inspected `verification/six_shapes.json`: contains only the 6 shapes listed after Conjecture 6.3 (`(8,7,5,4,4,4)`, `(8,6,5,5,4,4)`, `(7,6,6,5,4,4)`, `(7,7,6,4,4,2,2)`, `(7,7,5,5,4,2,2)`, `(7,7,6,5,3,3,2)`), NOT `(6,5,5,3,3,1)`.
4. **Other competing repositories (`facebookresearch/atlas-lean`, `aliromman/math`, `KnowledgeSense/math`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `1337isnot1337/solved-conjectures`, `openai/math`):**
   - Full recursive tree checks and issue searches for `2610.29291` and `Latin`: **0 matches** for `2610.29291`, `Daugherty`, or `conj:box` in all 7 repos (all `Latin`/`Box` hits are classical Latin squares/rectangles, Tuza's conjecture, Alabama paradox, Lassalle/Ferroni/Higashitani box polynomials, etc.).
5. **Global GitHub Search (`gh search` / `gh api`):**
   - `gh search issues "2610.29291"`: only `the-omega-institute/trureturing#20269` (Conj 6.3).
   - `gh search prs "2610.29291"`: 0 matches.
   - `gh search issues "Daugherty" "Latin"`: `#26377` (Conj 6.2), `#20269` (Conj 6.3), plus unrelated `EasyA-Tech/icarus#13`.
   - `gh search issues "conj:box"`, `"6,5,5,3,3,1"`, `"6, 5, 5, 3, 3, 1"`: 0 matches.
   - `gh search code "2610.29291"` (56 results): all inspected hits belong to `rainwangphy/aftd-platform` (Conj 6.3 / Prop 5.5 / `(3,2,1)`), `valyuAI/research` (Conj 6.3), `the-omega-institute/trureturing` (Conj 6.3), `elder-plinius/V3R1T4S` (Chow et al. WPC note), `spdaugherty/spdaugherty.github.io`, `ehijano/rss_fetch`, and numeric collision `LarsSivertsen/xeos_python`.
   - `gh search code "conj:box"`: 0 matches.
   - `gh api search/code` for `6,5,5,3,3,1+Latin`, `6,5,5,3,2,1+Latin`, and `"Conjecture 6.1" "Latin tableaux"`: only unrelated CSV/font/numeric hits or `2609.13764` (`tamnd/arxiv`). *(Note: final two `gh api` rate-limited queries `"conj+6.1"` on `aftd-platform` and `"Conjecture 6.1" "Daugherty"` hit the 30/min search cap after the prior searches already returned the full 35-file `2610.29291` list in `aftd-platform`.)*

### 2.3 External Academic APIs & Web Search
- **arXiv API (`all:"Latin tableaux"`, `au:Daugherty AND cat:math.CO`):** Only `2610.29291v1`, `2007.13835v4`, `math/0205288v2` for `"Latin tableaux"`; Daugherty's other 2026 papers (`2610.39257v1`, `2607.14255v1`) are on Tamari lattices and shuffle-compatibility.
- **OpenAlex API (`Counting and constructing Latin tableaux`):** Work `https://openalex.org/W7223232483` (`doi: 10.48550/arxiv.2610.29291`, `publication_date: 2026-10-21`) has **`cited_by_count: 0`**.
- **Zenodo API:** `q=2610.29291` -> `total: 0`; `q="Latin tableaux"` -> `total: 1` (`21718549`, 2026-07-31 LADA $5 \times 5$ certificate, predates `2610.29291`).
- **Crossref API:** `query=2610.29291` and `query.bibliographic=Counting+and+constructing+Latin+tableaux+Daugherty` -> 0 hits for `2610.29291`.
- **Web search (`search_web`):** Queries `"2610.29291" OR "conj:box" OR "6,5,5,3,3,1" "Latin tableaux"` and `"Daugherty" "Latin tableaux" "Conjecture 6.1" OR "wide partitions"` returned only `arXiv:2610.29291` and prior Chow et al. references; no refutation or counterexample found.

**Novelty conclusion:** Conjecture 6.1 (`conj:box`) remains **OPEN / UNREFUTED** in public sources as of `2026-11-27T02:30Z`.

---

## 3. Independent Exact Computation & Cross-Check

### 3.1 Execution of `notes/check-check-3.py`
Command: `/usr/bin/time -p .venv/bin/python targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py`
- **Exit code:** `0`
- **Runtime:** `real 28.83`, `user 19.17`, `sys 1.73`
- **Raw stdout:**
  ```
  Sanity checks PASS: paper's examples (3,2), (4,4,2,1)->(4,4,2,2), (3,3,2), (4,4,3,1)->(5,4,4,3,1) match.
  Pair PASS: mu=(6, 5, 5, 3, 2, 1) (wide, LT=56) -> lam=(6, 5, 5, 3, 3, 1) (wide, LT=32) at i=5
  Pair PASS: mu=(6, 6, 4, 3, 2, 1) (wide, LT=88) -> lam=(6, 6, 4, 3, 3, 1) (wide, LT=64) at i=5
  Pair PASS: mu=(6, 6, 5, 3, 2, 1) (wide, LT=2080) -> lam=(6, 6, 5, 3, 3, 1) (wide, LT=1984) at i=5
  PASS
  ```

### 3.2 Independent Computation via Lemma 5.4 Permanents & Direct Definition 2.5 Enumeration

#### (a) Main Counterexample Pair: $\mu = (6,5,5,3,2,1) \to \lambda = (6,5,5,3,3,1)$ ($i = 5 \in [\ell(\lambda)-1] = [5]$)
Why restricting row $r$ to $\{1, \ldots, \lambda_r\}$ matches Definition 2.5 without loss of generality for type $\lambda'$: by Definition 2.5, symbol $1$ has multiplicity $\lambda'_1 = \ell(\lambda)$, so it must appear once in every row (filling rows of length $1$ with $\{1\}$); inductively, all $\lambda'_k$ occurrences of symbol $k$ must lie in the $\lambda'_k$ rows of length $\ge k$, forcing row $r$ to contain $\{1, \ldots, \lambda_r\}$.

Every generated tableau was additionally verified directly against Definition 2.5 (exact row lengths, exact symbol multiplicities $\lambda'$, no row repeats, no column repeats, all distinct):
- **$\mu = (6,5,5,3,2,1)$:**
  - Direct Definition 2.5 enumeration: **$56$ distinct valid tableaux** (exact match).
  - Permanent formula (Lemma 5.4, $r=1$): summing $\mathrm{per}(A_6(T))$ over all $32$ tableaux of $\mu^{(1)} = (5,5,3,2,1)$ via exact integer Ryser permanent gives **$56$**.
  - Cross-check Lemma 5.4 ($r=5$): summing $\mathrm{per}(A_2(T))$ over $\mathcal{LT}(\mu^{(5)})$ gives **$56$**.
- **$\lambda = (6,5,5,3,3,1)$:**
  - Direct Definition 2.5 enumeration: **$32$ distinct valid tableaux** (exact match).
  - Permanent formula (Lemma 5.4, $r=1$): summing $\mathrm{per}(A_6(T))$ over all $32$ tableaux of $\lambda^{(1)} = (5,5,3,3,1)$ gives **$32$**.
  - Cross-check Lemma 5.4 ($r=5$): summing $\mathrm{per}(A_3(T))$ over $\mathcal{LT}(\lambda^{(5)})$ gives **$32$**.
- Hence $LT(\lambda) = 32 < 56 = LT(\mu)$, refuting Conjecture 6.1.

#### (b) Wideness & Subpartition Conjugate Audit (`COUNTEREXAMPLE.md` lines 19–27)
Checked ALL $2^6 - 1 = 63$ nonempty subpartitions $\nu \subseteq \mu$ and $\nu \subseteq \lambda$: **both $\mu$ and $\lambda$ are wide** ($\nu \succeq \nu'$ for all $63$ subpartitions).

Line-by-line check of the lower subpartitions in `COUNTEREXAMPLE.md` lines 19–27:
- Line 19: `(6,5,5,3,2,1)' = (6,5,4,3,3,1)`, partial sums `(6,11,16,19,21,22) >= (6,11,15,18,21,22)` — **OK**.
- Line 20: `(5,5,3,2,1)' = (5,4,3,2,2)`, partial sums `(5,10,13,15,16) >= (5,9,12,14,16)` — **OK**.
- Line 21: `(5,3,2,1)' = (4,3,2,1,1)`, partial sums `(5,8,10,11,11) >= (4,7,9,10,11)` — **OK**.
- Line 22: `(3,2,1)' = (3,2,1)`, `(2,1)' = (2,1)`, `(1,)' = (1,)` — **OK**.
- Line 23: `(6,5,5,3,3,1)' = (6,5,5,3,3,1)` (self-conjugate) — **OK**.
- **Line 24 (TYPO IN `COUNTEREXAMPLE.md`):** `COUNTEREXAMPLE.md` writes `(5,5,3,3,1)` vs `(5,5,3,2,2)` with partial sums `(5,10,13,16,17) >= (5,10,13,15,17)`.
  - **Actual conjugate:** `(5,5,3,3,1)' = (5,4,4,2,2)` (since 5 rows $\ge 1$, 4 rows $\ge 2$, 4 rows $\ge 3$, 2 rows $\ge 4$, 2 rows $\ge 5$), with partial sums `(5,9,13,15,17)`.
  - Dominance `(5,10,13,16,17) >= (5,9,13,15,17)` still holds (and with strict inequality $10 > 9$ at index 2), so wideness is unaffected, but line 24 of `COUNTEREXAMPLE.md` has a wrong conjugate and second partial sum.
- Line 25: `(5,3,3,1)' = (4,3,3,1,1)`, partial sums `(5,8,11,12,12) >= (4,7,10,11,12)` — **OK**.
- Line 26: `(3,3,1)' = (3,2,2)`, partial sums `(3,6,7) >= (3,5,7)` — **OK**.
- Line 27: `(3,1)' = (2,1,1)`, `(1,)' = (1,)` — **OK**.

#### (c) Additional Counterexample Pairs via Lemma 5.4 ($r=1$)
- `mu = (6,6,4,3,2,1)` (wide across all 63 subpartitions): `LT = 88` (from 32 sub-tableaux of `(6,4,3,2,1)`).
  `lam = (6,6,4,3,3,1)` (wide across all 63 subpartitions): `LT = 64` (from 64 sub-tableaux of `(6,4,3,3,1)`).
  At $i = 5 \in [5]$ ($n=22 \to 23$): $64 < 88$. **Verified.**
- `mu = (6,6,5,3,2,1)` (wide across all 63 subpartitions): `LT = 2080` (from 584 sub-tableaux of `(6,5,3,2,1)`).
  `lam = (6,6,5,3,3,1)` (wide across all 63 subpartitions): `LT = 1984` (from 1056 sub-tableaux of `(6,5,3,3,1)`).
  At $i = 5 \in [5]$ ($n=23 \to 24$): $1984 < 2080$. **Verified.**

---

## Summary of Findings for `@audit-3`
1. **Mathematical validity & novelty:** **SOLID.** `2610.29291v1` is the sole version; no `CONTESTED.md`; deep novelty check across 413 snapshots, `trureturing*` (`#20269`/`#20329` = Conj 6.3, `#26377` = Conj 6.2), `aftd-platform` (Conj 6.3, Prop 5.5, and `(3,2,1)->(3,3,1)` only), `valyuAI/research` (Conj 6.3), 7 other competing repos, arXiv, OpenAlex (`cited_by_count=0`), Zenodo, Crossref, and web search found **no prior proof or refutation of Conjecture 6.1**. Independent Lemma 5.4 permanent and direct Definition 2.5 computations confirm `LT(6,5,5,3,2,1) = 56 > 32 = LT(6,5,5,3,3,1)` (plus `(6,6,4,3,2,1)->(6,6,4,3,3,1)` `88->64` and `(6,6,5,3,2,1)->(6,6,5,3,3,1)` `2080->1984`) and wideness of all partitions.
2. **Two text typos to flag for the author (do not fix here):**
   - `COUNTEREXAMPLE.md` line 24: `(5,5,3,3,1)'` is `(5,4,4,2,2)` with partial sums `(5,9,13,15,17)`, NOT `(5,5,3,2,2)` / `(5,10,13,15,17)`.
   - `TARGET.md` line 25: cites *"Theorem 5.2 (line 651–701)"* for top-row monotonicity ($i=1$), whereas in `final.tex` and the compiled PDF it is **Proposition 5.5** (lines 695–701).

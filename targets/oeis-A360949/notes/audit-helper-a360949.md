# Audit Helper Report: `targets/oeis-A360949/`

**Helper:** `a360949-audit-hlp` (for `@audit-2`)  
**Checked (UTC):** 2026-11-27T01:23Z–01:32Z  
**Isolation compliance:** Did not read `verify.py`, `notes/explore.py`, `notes/check-check-3.md`, `notes/novelty-gate2-*.md`, `TARGET.md`, or `PROOF.md`; did not edit `TARGET.md` or `PROOF.md`.

---

## 1. Primary-Source Verbatim OEIS Check

Fetched live OEIS JSON via `.venv/bin/python` (`User-Agent: curl/8.7.1`, timeout 15s) from `https://oeis.org/search?q=id:<ID>&fmt=json` for `A360949`, `A161674`, `A010060`, and `A325574`.

### Directory State (`targets/oeis-A360949/`)
- `/bin/ls -la targets/oeis-A360949/` output:
  - `PROOF.md` (6220 B)
  - `TARGET.md` (2159 B)
  - `notes/` (dir)
  - `verify.py` (3846 B)
- Confirmed **no `CONTESTED.md`** present.

### `A360949` (Verbatim OEIS JSON)
- **`revision`:** `15`
- **`time`:** `2023-03-05T12:37:19-05:00`
- **`offset`:** `0,2`
- **`name`:** `G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.`
- **`data`:**
  `1,2,8,50,376,3124,27804,260496,2539616,25556330,263922884,2785341186,29948035032,327315887046,3630399545244,40813503158790,464662514679168,5354222585965310,62419468527625408,736098528973804246,8781173950238637928,105987886325647341056`
- **`comment`:**
  - `Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the Thue-Morse sequence.`
- **`formula`:**
  - `G.f. A(x) = Sum_{n>=0} a(n)*x^n satisfies:`
  - `(1) 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.`
  - `(2) 1 = Sum_{n>=0} 2 * (-x)^n * A(x)^(n^2) / (2 - (-1)^n * x * A(x)^n)^(n+1).`
  - `a(n) = A325574(n)/2^n for n >= 0.`
- **`program` (`prog`):**
  ```pari
  (PARI) {a(n) = my(A=[1]);
  for(i=1, n, A=concat(A, 0); A[#A] = 2*polcoeff( sum(m=0, #A, (-x/2)^m * (Ser(A)^m + (-1)^m)^m ), #A)); A[n+1]}
  for(n=0, 30, print1(a(n), ", "))
  ```
  - **PARI/GP equivalence confirmed:** At iteration `i` (`#A = i+1`), `A` holds `[a(0), ..., a(i-1), 0]`. In `Sum_{m>=0} (-x/2)^m * (A(x)^m + (-1)^m)^m`, extracting `[x^(i+1)]` gives `-(1/2)*a(i)` from `m=1` (`(-x/2)*(A(x)-1)`), `0` from `m=0`, and for `m >= 2` the coefficient of `x^(i+1)` depends only on `a(0)..a(i-1)` (since `a(i)` enters `A(x)^m` at degree `i` and is multiplied by `(-x/2)^m` of degree `m >= 2`, contributing only at degree `>= i+2`). Thus setting `[x^(i+1)] = 0` yields `a(i) = 2 * [x^(i+1)] Sum_{m=0..i+1} (-x/2)^m * (Ser(A)^m + (-1)^m)^m`. Exact simulation in Python for `n=0..11` reproduced `[1, 2, 8, 50, 376, 3124, 27804, 260496, 2539616, 25556330, 263922884, 2785341186]`, matching `data`.
- **`xref`:** `Cf. A325574, A161674.`

### `A161674` (Verbatim OEIS JSON)
- **`revision`:** `21`
- **`time`:** `2021-01-30T04:23:15-05:00`
- **`offset`:** `1,3`
- **`name`:** `Positions n such that A010060(n) + A010060(n+2) = 1.`
- **`data`:**
  `0,1,4,5,6,7,8,9,12,13,16,17,20,21,22,23,24,25,28,29,30,31,32,33,36,37,38,39,40,41,44,45,48,49,52,53,54,55,56,57,60,61,64,65,68,69,70,71,72,73,76,77,80,81,84,85,86,87,88,89,92,93,94,95,96,97,100,101,102,103,104`
- **`comment`:**
  - `Locates patterns of the form 0x1 or 1x0 in the Thue-Morse sequence.`
  - `Complement to A081706. Also: union of sequences {2*A121539(n)+k}, k=0 or 1, generalized in A161673.`
  - `Also union of sequences {A079523(n)-k}, k=0 or 1. For a generalization see A161890. - _Vladimir Shevelev_, Jul 05 2009`
  - `The asymptotic density of this sequence is 2/3 (Rowland and Yassawi, 2015; Burns, 2016). - _Amiram Eldar_, Jan 30 2021`
- **`formula`:** *(no `formula` field present in the OEIS JSON record for `A161674`)*
- **`program` (`prog`):**
  ```pari
  (PARI) is(n)=hammingweight(n)%2!=hammingweight(n+2)%2 \\ _Charles R Greathouse IV_, Aug 20 2013
  ```
- **`xref`:** `Cf. A161673, A161639, A161641, A161627, A161579, A161580, A161890, A121539, A131323, A036554, A010060, A079523, A081706.`

### `A010060` (Live Check Summary)
- `revision`: `619`, `time`: `2026-10-18T01:10:44-04:00`, `offset`: `0,1`
- `name`: `Thue-Morse sequence: let A_k denote the first 2^k terms; then A_0 = 0 and for k >= 0, A_{k+1} = A_k B_k, where B_k is obtained from A_k by interchanging 0's and 1's.`
- `data`: `0,1,1,0,1,0,0,1,...` (`a(n) = hammingweight(n) % 2`).

### `A325574` & Proof Check in `A325574` / `A161674`
- **`A325574`** (`revision: 10`, `time: 2023-03-05T12:07:09-05:00`, `offset: 0,2`, author `_Paul D. Hanna_, May 16 2019`):
  - `name`: `G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x)^n * (A(x)^n + (-1)^n)^n.`
  - `data`: `1,4,32,400,6016,99968,1779456,33343488,650141696,13084840960,270257033216,...`
  - `comment`: `a(n) = 2^n * A360949(n) for n >= 0.`
  - `formula`: `(1) 1 = Sum_{n>=0} (-x)^n * (A(x)^n + (-1)^n)^n.`, `(2) 1 = Sum_{n>=0} (-x)^n * A(x)^(n^2) / (1 - (-1)^n*x*A(x)^n)^(n+1).`
  - `xref`: `Cf. A360949.`
- **Does `A325574` or `A161674` mention any proof of `A360949` or a closely related Hanna Thue–Morse mod-4 theorem?**
  - **No.** Neither `A325574` nor `A161674` mentions any proof of `A360949` or any Hanna Thue–Morse mod-4 conjecture/theorem. `A161674` was last revised Jan 30, 2021 (before `A360949` was created in Mar 2023) and only links Rowland–Yassawi (2015) and Burns (2016) for asymptotic density `2/3`. `A325574` states only its defining equation, formula (2), `a(n) = 2^n * A360949(n)`, its PARI program, and `Cf. A360949`.

---

## 2. Deep Novelty Check Across All Sources

### Local Watch Snapshots (`tools/novelty_grep.py`)
- `.venv/bin/python tools/novelty_grep.py A360949 A325574 A161674`:
  - **3 lines across 1/367 files** (`watch/snapshots/formal/last_sweep.json` lines 2436, 2445, 2454) — all three are internal swarm sweep-log records for `slug: "oeis-A360949"` matching `"Paul D. Hanna"` on unrelated `google-deepmind/formal-conjectures` PRs (#7991 `A158110`, #7674 `A368630`, #7673 `A396843`).
  - **0 hits** for `A360949`, `A325574`, `A161674` in any external snapshot (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `arxiv`, `discovered/`).
- `.venv/bin/python tools/novelty_grep.py "360949" "325574" "161674" "Hanna" "(-x/2)^n"`:
  - **0 hits** for `360949` (outside `last_sweep.json` own target), `325574`, `161674`, or `(-x/2)^n`.
  - `Hanna` hits in snapshots (`joaquimmj/oeis-conjectures` `A155200`; `mathesis-papers` `A181074`, `A181080`, `A378258`, `A195417`, `A381355`, `A389472`, `A389475`, `hanna-square-exponent-*`; `dvgyl/oeis-proofs`; `the-omega-institute/trureturing*`; `formal-conjectures` PRs) all concern different OEIS entries.

### Specific GitHub Repositories & Organizations (`gh api` trees + issues + `gh search code`)
1. `rainwangphy/aftd-platform` (`main`, 28,161 files, 1 issue): 14 `ThueMorse*` files in TCS/word combinatorics; **0 hits** for `A360949`, `A325574`, `A161674`, `Hanna`, `(-x/2)^n`.
2. `valyuAI/research` (`main`, 5,381 files, 1 issue): **0 hits**.
3. `facebookresearch/atlas-lean` (`main`, 53,930 files, truncated tree + `gh search code` + 100 issues): Thue-Morse word/factor Lean files + `HannaNeumannConjectureAMR10Problem0301Wanted.lean` + open issue #10540 (`Prove the Thue-Morse binary mask for the meta-automatic sequence`, unrelated); **0 hits** for `A360949`, `A325574`, `A161674`, `(-x/2)^n`.
4. `the-omega-institute/trureturing*` (checked all 16 `trureturing*` repos in `the-omega-institute`, 45 org repos total):
   - `trureturing` (`dev`, 56,878 files, truncated tree + `gh search code` + `Problems/` + 100 issues): `gh search code A360949` returned 1 **false-positive** hex substring match (`a360949` inside SHA-256 `fb14d1db574895826a0a3609491c858849b033d41728d30e383d536c5d9d8bf4` in `Problems/lee-liu-2025-integer-two-domination-three-row.md`); **0 hits** for `A325574`, `A161674`, `(-x/2)^n`. Contains many other Hanna and Thue-Morse entries (e.g., `A372527`, `A380060`, `A380066`, `A356508`, `A107099`, `A155200`, `ThueMorseReducedAbelianOdd`), none related to `A360949`/`A325574`.
   - `trureturing-experiments` (`main`, 25,887 files, 299 dirs in `docs/reports/`, 100 issues): 93 `hanna`/`thue` path hits including other mod-4 Hanna reports (`A356508`, `A372527`, `A380060`, `A380066`) and `oeis-hanna-parity-family-research` (`A393173`, `A393850`, `A382122`, `A378258`, `A375449`, `A375452`, `A365574`, `A380711`, `A379764`, `A380681–A380686`); **0 hits** for `A360949`, `A325574`, `A161674`, `(-x/2)^n`.
   - `trureturing-requests` (100 issues): 7 open issues matched `hanna`/`thue` (for Zenodo DOIs `24408311`, `24406600` = Ambrož–Kadlec–Masáková–Pelantová Thue-Morse prefix costs, `24407818`); **0 hits** for `A360949`, `A325574`, `A161674`.
   - Remaining 13 `trureturing*` repos (`trureturing-pages`, `trureturing-mdbook`, `trureturing-intuition`, `trureturing-film`, `trureturing-visualize`, `trureturing-lean-eval`, `trureturing-books-template`, `trureturing-books`, `trureturing-source-theories`, `trureturing-tools`, `trureturing-outreach-engine`, `trureturing-live`, `trureturing-live-template`): **0 hits** for `A360949`, `A325574`, `A161674`, `(-x/2)^n`, and `hanna` (`trureturing-pages` has 1 unrelated `thue-morse-reduced-abelian-odd.lean`).
5. `aliromman/math` (`main`, 755 files, 100 issues): **0 hits**.
6. `KnowledgeSense/math` (`main`, 5,377 files, 0 issues): **0 hits**.
7. `1337isnot1337/solved-conjectures` (`main`, 19,785 files, 100 issues): 30 `thue` path hits (`gawron-miska-ulas-thue-morse-sign-density`, `gawron-miska-ulas-thue-morse-valuation` — unrelated); **0 hits** for `A360949`, `A325574`, `A161674`, `Hanna`, `(-x/2)^n`.
8. `dvgyl/oeis-proofs` (`main`, 319 files, 0 issues): 25 Hanna Lean/JSON files covering 28 entries (`A396843`, `A396844`, `A396099`, `A396798`, `A396807`, `A393856–A393859`, `A378580`, `A378581`, `A380060`, `A380680`, `A355872`, `A393172`, `A393171`, `A389536`, `A195194`, `A389537`, `A389542`, `A389474`, `A389475`, `A392210`, `A396102`, `A380056`, `A397346`, `A394576`, `A396093`); **0 hits** for `A360949`, `A325574`, `A161674`, `Thue-Morse`.
9. `joaquimmj/oeis-conjectures` (`main`, 1,122 files, 0 issues): **0 hits** in repo paths/issues (snapshot `LOG.md`/`README.md` only has `A155200` for Hanna).
10. `mathesis-papers/hanna-self-substitution-integrality` (`main`, 46 files, 0 issues) and all **223** repos in `mathesis-papers`: **0 hits** for `A360949`, `A325574`, `A161674`; Hanna/Thue-Morse repos in `mathesis-papers` treat other OEIS numbers (`A381355`, `A181074`, `A181080`, `A389474`, `A389472`, `A389475`, `A195417`, `A378258`, `A292179`/`A292178`, square-exponent/self-substitution integrality, Ambrož–Kadlec–Masáková–Pelantová).

### Global GitHub (`gh search code` / `issues` / `repos`)
- `A360949`: `code` returned only `gfis/OEIS-prog/prog/gp/a360/A360949.gp` (OEIS PARI mirror) + unrelated hex/CSV/binary filename collisions; `issues`: `[]`; `repos`: `[]`.
- `A325574`: `code` returned only `gfis/OEIS-prog/prog/gp/a325/A325574.gp` (OEIS PARI mirror) + unrelated string/hex collisions; `issues`: `[]`; `repos`: `[]`.
- `A161674`: `code` returned OEIS program/data mirrors (`archmageirvine/joeis`, `loda-lang/loda-programs`, `africamonkey/OEIS-Spider`, `gfis/OEIS-prog`, `ai4reason/oeis-atp-benchmark` `pb/A161674.smt2`) + unrelated collisions; `issues`: `[]`; `repos`: `[]`.
- `"Paul D. Hanna" "Thue-Morse"`: `code`: `[]`; `issues`: `[]`; `repos`: `[]`.

### arXiv (`tools/arxiv_fetch.py query`)
- `all:A360949`: `total_results: 0`
- `all:A325574`: `total_results: 0`
- `all:A161674`: `total_results: 0`
- `all:Hanna AND all:"Thue-Morse"`: `total_results: 1` (`2001.07017v1`, Sary Drappeau & Gautier Hanna, number-field primes — unrelated)
- `all:"Paul D. Hanna"`: `total_results: 1` (`math/0509316v4`, Heninger–Rains–Sloane 2006 — unrelated)

### Zenodo (`https://zenodo.org/api/records`)
- `A360949`: `total: 0`
- `A325574`: `total: 0`
- `A161674`: `total: 0`
- `"Paul D. Hanna"`: `total: 4`, 0 matching `360949`, `325574`, `161674`, `thue`, or `morse`.
- `"Paul D. Hanna" "Thue-Morse"`: `total: 58` (broad keyword match on Thue-Morse records; none by Paul D. Hanna on A360949).

### Crossref (`https://api.crossref.org/works`)
- `A360949`: `total-results: 0` (retried after initial HTTP 429)
- `A325574`: `total-results: 0`
- `A161674`: `total-results: 0`
- `Hanna Thue-Morse`: top hits unrelated (Drappeau & Gautier Hanna, Li, Fu & Gao, etc.).

### Web Search (`search_web`)
- Queries `"A360949"`, `"A325574"`, `"A360949" OEIS`, `"A161674" "Hanna"`, `"(-x/2)^n" "A(x)^n"`, `"Paul D. Hanna" "Thue-Morse" OR "A360949" mod 4`, `"A360949" "Hanna" OR "A325574" "Hanna"` surfaced **no** papers, preprints, blog posts, or external proofs settling `A360949` or `A325574`.

---

## 3. Independent Exact Verification (`check-check-3.py`)

Executed: `time .venv/bin/python targets/oeis-A360949/notes/check-check-3.py`

- **Exit code:** `0`
- **Runtime:** `1.57s user 0.20s system 69% cpu 2.529 total`
- **Exact raw output:**
```text
Step 1 & Data PASS: A360949 (n=0..35) and A161674 (m<=104) verified via exact Q[[x]] functional equation.
Steps 2 & 3 PASS: all F_2[[x]] / F_2[[y]] identities and C(y) == C_tilde(y) verified up to deg 80.
PASS
```

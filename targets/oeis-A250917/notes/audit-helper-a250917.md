# Adversarial Audit Helper Report: OEIS A250917

- **Target:** `targets/oeis-A250917/` (R. J. Mathar's Jan 25, 2020 Conjecture D-finite recurrence for OEIS A250917)
- **Helper:** `oeis250917-hlp` (for `@audit-2`)
- **Timestamp (UTC):** `2026-11-26T21:23:22Z`
- **Verdict:** **PASS** on primary-source fidelity, **PASS** on novelty (one notable near-miss in `gfis/OEIS-mat` and `archmageirvine/joeis` documented below that does *not* settle Mathar's conjecture), and **PASS** on independent computational verification.

---

## 1. Live OEIS A250917 Primary-Source Inspection

Fetched `https://oeis.org/search?q=id:A250917&fmt=json` (with `User-Agent: curl/8.7.1`) and `https://oeis.org/A250917/internal`.

### Complete Field Extraction (`A250917`, revision 20)
- **`number`**: `250917`
- **`name`**: `"Expansion of e.g.f. exp( x*C(x)^3 ) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, A000108."`
- **`offset`**: `"0,3"`
- **`data`** (19 terms, $n=0..18$): `"1,1,7,73,1033,18541,403831,10351237,305355793,10192132153,379819484551,15634219476481,704566985120857,34506514429777573,1825081888365736183,103685565729559782781,6297505655719537293601,407233553972252986277617,27935786938445348562454663"`
- **`comment`** (1 entry):
  - `"In general, if k>0 and e.g.f. = exp(x*C(x)^k) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, then a(n) ~ k * 2^(2*n + k - 5/2) * n^(n-1) / exp(n - 2^(k-2)). - _Vaclav Kotesovec_, Aug 22 2017"`
- **`reference`**: *absent* in live JSON
- **`link`**: *absent* in live JSON
- **`formula`** (4 entries):
  1. `"a(n) = Sum_{k=0..n} n!/k! * binomial(2*n+k-1, n-k) * 3*k/(n+2*k)  for n>0 with a(0)=1."`
  2. `"a(n) ~ 3 * 2^(2*n+1/2) * n^(n-1) / exp(n-2). - _Vaclav Kotesovec_, Aug 22 2017"`
  3. `"Conjecture D-finite with recurrence: +2*a(n) +(-11*n+20)*a(n-1) +(n^3+9*n^2-116*n+164)*a(n-2) +(-4*n^4+35*n^3+n^2-317*n+342)*a(n-3) -6*(n-3)*(6*n^3-50*n^2+147*n-176)*a(n-4) +12*(n-5)*(2*n-9)*(n-3)*(n-4)*a(n-5)=0. - _R. J. Mathar_, Jan 25 2020"`
  4. `"E.g.f.: exp( (1/x)^2 * Series_Reversion( x*(1-x) )^3 ). - _Seiichi Manyama_, Mar 15 2025"`
- **`example`** (4 lines):
  - `"E.g.f.: A(x) = 1 + x + 7*x^2/2! + 73*x^3/3! + 1033*x^4/4! + 18541*x^5/5! +..."`
  - `"such that log(A(x)) = x*C(x)^3,"`
  - `"log(A(x)) = x + 3*x^2 + 9*x^3 + 28*x^4 + 90*x^5 + 297*x^6 + 1001*x^7 +..."`
  - `"where C(x) = 1 + x*C(x)^2 is the g.f. of A000108."`
- **`maple`**: *absent* in live JSON
- **`mathematica`**: *absent* in live JSON
- **`program`** (3 PARI programs, 6 lines):
  - `"(PARI) {a(n)=my(C=1); for(i=1, n, C=1+x*C^2 +x*O(x^n));"`, `"n!*polcoef(exp(x*C^3), n)}"`, `"for(n=0, 20, print1(a(n), \", \"))"`
  - `"(PARI) {a(n) = if(n==0, 1, sum(k=0, n, n!/k! * binomial(2*n+k-1, n-k) * 3*k/(n+2*k) ))}"`, `"for(n=0, 20, print1(a(n), \", \"))"`
  - `"(PARI) my(N=20, x='x+O('x^N)); Vec(serlaplace(exp(serreverse(x*(1-x))^3/x^2))) \\\\ _Seiichi Manyama_, Mar 15 2025"`
- **`xref`** (3 lines):
  - `"Cf. A080893, A251568."`
  - `"Cf. A091695, A380512, A380515."`
  - `"Cf. A000108, A001517."`
- **`keyword`**: `"nonn"`
- **`author`**: `"_Paul D. Hanna_, Dec 06 2014"`
- **`references`**: `3`
- **`revision`**: `20`
- **`time`**: `"2025-03-15T11:29:15-04:00"`
- **`created`**: `"2014-12-06T23:24:31-05:00"`

### Word-for-Word Match with `TARGET.md` and `PROOF.md`
- **`TARGET.md`**: `source` (`revision 20, 2025-03-15`), `Name`, `Data (offset 0,3)`, and `Formula section` match the live OEIS JSON character-for-character.
- **`PROOF.md`**:
  - Generating function $C(x) = \frac{1-\sqrt{1-4x}}{2x}$ and $F(x) = \exp(x C(x)^3) = \sum_{n=0}^{\infty} a(n)\frac{x^n}{n!}$ match the OEIS `name` field.
  - Every polynomial coefficient in the displayed recurrence in `PROOF.md` matches Mathar's OEIS formula line word-for-word:
    - $2\,a(n)$
    - $+(-11n+20)\,a(n-1)$
    - $+(n^3+9n^2-116n+164)\,a(n-2)$
    - $+(-4n^4+35n^3+n^2-317n+342)\,a(n-3)$
    - $-6(n-3)(6n^3-50n^2+147n-176)\,a(n-4)$
    - $+12(n-5)(2n-9)(n-3)(n-4)\,a(n-5)$
  - Domain qualification in `PROOF.md` ($n \ge 5$, and $n=3,4$ with $a(-1)=0$; fails at $n=1,2$ with $a(-1)=a(-2)=0$) accurately clarifies the implicit domain of Mathar's unindexed order-5 recurrence.

### Sibling & Cross-Referenced OEIS Entries Checked
Live JSON fetched for all 3 named siblings plus all 5 remaining xrefs (`A080893`, `A091695`, `A380512`, `A380515`, `A001517`):
- **`A250916`** ($\exp(C(x)^2-1)$, rev 17, 2025-12-28): No recurrence, no proof, no link to any proof of `A250917`.
- **`A250918`** (algebraic g.f. $1-2A+(1+x)A^3-2xA^4=0$, rev 23, 2017-06-02): No relation to `A250917` proof.
- **`A251568`** ($\exp(x C(x)^2)$, rev 61, 2026-10-17): Has Peter Bala's order-2 recurrence (2015) and links Ahaan Kallat, `arXiv:2610.15849` (*Universal Shift Congruences for Weighted Permutation Sequences*, 2026). Inspected `arXiv:2610.15849` abstract and HTML page: it proves shift congruences $A(n+k) \equiv A(n)A(k) \pmod{\mathrm{lcm}(n,k)}$ and Bala's divisibility conjecture on `A251568`/`A251569`, and does **not** mention `A250917` (`Mentions A250917: False`).
- **`A080893` / `A001517`** ($\exp(x C(x))$), **`A091695`** ($\exp(x/(1-x)^3)$), **`A380512`**, **`A380515`**: None prove or link to a proof of Mathar's recurrence for `A250917`.

---

## 2. Deep Novelty Check (2026-11-26T21:15Z–21:23Z)

### Summary of Queries and Findings

1. **Local Watch Snapshots (`watch/snapshots/**`, 224 files):**
   - `.venv/bin/python tools/novelty_grep.py A250917 "379819484551" "C(x)^3" "exp(x*C(x)^3)"` -> `# 0 lines across 0/224 files in 0.54s`.
   - `.venv/bin/python tools/novelty_grep.py 250917 "27935786938445348562454663"` -> `# 0 lines across 0/224 files in 0.47s`.

2. **Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A250917`: `total=0`.
   - `q="exp(x*C(x)^3)"`: `total=0`.
   - `q="exp(x*C(x)"`: `total=0`.
   - `q=A250916`: `total=0`.
   - `q=A251568`: `total=0`.
   - `q="Roberto Blanco"`: `total=37` (includes Zenodo `23311738` *An elementary differential proof of Mathar's recurrence for OEIS A080894* by Roberto Blanco Gómez, 2026-10-12, which covers `A080894` only and does not mention `A250917`; no record for `A250917`).
   - `q="Mathar" "Catalan" "recurrence"`: `total=16995` (inspected top 15 hits—Haobo Ma & Wenlin Zhang on A027182/A386829/A174193/A157100, Byungwoong Yoo `22321509` on A026771, R. J. Mathar software records—none cover `A250917`).

3. **GitHub (read-only `gh search` and `gh api`):**
   - **`joaquimmj/oeis-conjectures`**: `gh search code A250917 repo:joaquimmj/oeis-conjectures` -> 0 matches. Inspected `REPORT.md`, `conjectures/crawl/dfinite_targets.txt`, `conjectures/dfinite/proof.md`, and `paper/tables/catalogue.tex`: `A250917` is absent from all of them (`dfinite/proof.md` solves only 6 algebraic single-radical g.f.s and explicitly excludes hypergeometric/series-reversion/exponential g.f.s).
   - **`loda-lang/loda-programs`** (`oeis/250/A250917.asm`) and **`africamonkey/OEIS-Spider`** (`prepare/data/data/A250917.txt`): Mirror OEIS terms/LODA program only; no recurrence proof.
   - **`gfis/OEIS-mat` & `archmageirvine/joeis` (Near-Miss):**
     - `gfis/OEIS-mat` (`contrib/rm/dfinite.grep.txt`) records Mathar's unproved `"Conjecture D-finite..."` line verbatim from `ajson/A250917.json`.
     - `gfis/OEIS-mat` (`holrec/rectopost.man`) and `archmageirvine/joeis` (`src/irvine/oeis/a250/A250917.java`, generated `2022-08-12 18:10` by Georg Fischer via `gen_seq4.pl rectoproc/holos5`) record an **order-3** recurrence $Q(n)$ produced by Maple's `sumrecursion` on the OEIS binomial sum formula:
       $$Q(n):\; 2(n+2)(n-3)a(n) - (11n^3 - 13n^2 - 82n + 72)a(n-1) + (n-1)(n-2)(n^3 + 11n^2 - n - 102)a(n-2) - 2(2n-5)(n-1)(n+3)(n-3)(n-2)^2 a(n-3) = 0.$$
     - Algebraically, Mathar's order-5 recurrence $P(n)$ is an exact $\mathbb{Q}(n)$-left-multiple of $Q(n)$:
       $$P(n) = \frac{1}{(n-3)(n+2)} Q(n) + \frac{3(3n^2 - 6n - 8)}{(n-4)(n-3)(n+1)(n+2)} Q(n-1) - \frac{6}{(n-4)(n+1)} Q(n-2).$$
     - **Why this does NOT settle the exact statement:** Neither `gfis/OEIS-mat` nor `archmageirvine/joeis` (a) states, derives, or proves Mathar's order-5 recurrence $P(n)$, (b) supplies any proof or creative-telescoping certificate for $Q(n)$ (it is raw `sumrecursion` output used to generate Java terms with 5 hardcoded initial values `1, 1, 7, 73, 1033`), or (c) proves that the OEIS binomial sum equals $[x^n/n!]\exp(x C(x)^3)$.

4. **arXiv API (`https://export.arxiv.org/api/query`):**
   - `search_query=all:A250917`: `totalResults=0`.
   - `search_query=all:"exp(x*C(x)^3)"`: `totalResults=0`.
   - `id_list=2610.15849`: Checked paper metadata/abstract and web page; does not mention `A250917`.

5. **Web / Crossref / OpenAlex:**
   - **`search_web`** for `"A250917" "recurrence" OR "D-finite" OR "proved" OR "seqfan"`, `"12*(n-5)*(2*n-9)" OR "(-11*n+20)" "A250917"`, `"A250917" seqfan OR oeis.org`, and `"exp(x*C(x)^3)" OR "exp( x*C(x)^3 )" recurrence OR proof`: No published proof, SeqFan thread, or note found for `A250917`.
   - **Crossref API**: `A250917` -> `total=0`; `exp(x*C(x)^3)` -> unquoted token search noise; `Mathar Catalan recurrence` -> HTTP 429.
   - **OpenAlex API**: All queries (`A250917`, `250917 Catalan`, `exp(x*C(x)^3)`, etc.) returned `HTTP Error 429: Too Many Requests`.
   - **Not Covered:** Rate-limited OpenAlex API responses (`HTTP 429`), paywalled/non-indexed journal PDFs not surfaced via web search or Crossref, and private/unindexed repositories.

---

## 3. Independent Computational Verification

### A. Re-run of `targets/oeis-A250917/notes/check-check-2.py`
Command: `.venv/bin/python -u targets/oeis-A250917/notes/check-check-2.py`
- **Exit code:** `0`
- **Exact raw output:**
```text
Exact differential operator check in Q(x)[S]/(S^2-(1-4x)): R(x,S) = (0, 0)
Series & OEIS formula match all 19 OEIS terms and exact values up to n=25
Direct recurrence check: fails at n=1,2 (as stated), == 0 for all n=3..25
PASS (all checks passed in 12.002s)
```

### B. In-Memory SymPy Verification of Degrees, Denominators, Poles, and Small-$n$ Values
In $\mathcal{A} = \mathbb{Q}(x)[S]/(S^2 - (1-4x))$ where $C(x) = \frac{1}{2x} - \frac{1}{2x}S$ and $g(x) = x C(x)^3 = \frac{1-3x}{2x^2} + \frac{x-1}{2x^2}S$:
- $g'(x) = \frac{3x-2}{2x^3} + \frac{-2x^2+7x-2}{2x^3(4x-1)} S$.

Writing $F^{(r)}/F = A_r(x) + B_r(x) S$ for $r = 0, \dots, 5$:
| $r$ | $\deg(\mathrm{num}(A_r))$ | Factored $\mathrm{den}(A_r)$ | $\deg(\mathrm{num}(B_r))$ | Factored $\mathrm{den}(B_r)$ |
|---:|---:|---|---:|---|
| 0 | 0 | $1$ | $-\infty$ ($0$) | $1$ |
| 1 | 1 | $2x^3$ | 2 | $2x^3(4x-1)$ |
| 2 | 4 | $2x^6(4x-1)$ | 5 | $2x^6(4x-1)^2$ |
| 3 | 7 | $2x^9(4x-1)^2$ | 8 | $2x^9(4x-1)^3$ |
| 4 | 10 | $2x^{12}(4x-1)^3$ | 11 | $2x^{12}(4x-1)^4$ |
| 5 | 13 | $2x^{15}(4x-1)^4$ | 14 | $2x^{15}(4x-1)^5$ |

For the six operator summands $Q_r(\theta)[F^{(5-r)}]/F = \mathrm{term}_{r,A}(x) + \mathrm{term}_{r,B}(x) S$ (with $Q_r(m) = P_r(m+5)$):
- $r=0$ ($Q_0(m)=2$): $\deg(\mathrm{num}_A)=13$, $\mathrm{den}_A = x^{15}(4x-1)^4$; $\deg(\mathrm{num}_B)=14$, $\mathrm{den}_B = x^{15}(4x-1)^5$.
- $r=1$ ($Q_1(m)=-11m-35$): $\deg(\mathrm{num}_A)=13$, $\mathrm{den}_A = 2x^{14}(4x-1)^4$; $\deg(\mathrm{num}_B)=14$, $\mathrm{den}_B = 2x^{14}(4x-1)^5$.
- $r=2$ ($Q_2(m)=m^3+24m^2+49m-66$): $\deg(\mathrm{num}_A)=16$, $\mathrm{den}_A = 2x^{15}(4x-1)^5$; $\deg(\mathrm{num}_B)=17$, $\mathrm{den}_B = 2x^{15}(4x-1)^6$.
- $r=3$ ($Q_3(m)=-4m^4-45m^3-74m^2+318m+657$): $\deg(\mathrm{num}_A)=16$, $\mathrm{den}_A = 2x^{14}(4x-1)^5$; $\deg(\mathrm{num}_B)=17$, $\mathrm{den}_B = 2x^{14}(4x-1)^6$.
- $r=4$ ($Q_4(m)=-36m^4-312m^3-1062m^2-1518m-708$): $\deg(\mathrm{num}_A)=13$, $\mathrm{den}_A = x^{11}(4x-1)^4$; $\deg(\mathrm{num}_B)=14$, $\mathrm{den}_B = x^{11}(4x-1)^5$.
- $r=5$ ($Q_5(m)=24m^4+84m^3+84m^2+24m$): $\deg(\mathrm{num}_A)=9$, $\mathrm{den}_A = x^8(4x-1)^3$; $\deg(\mathrm{num}_B)=10$, $\mathrm{den}_B = x^8(4x-1)^4$.

- **Pole check:** Every factored denominator of $A_r, B_r$ ($r=0..5$) and of all six summands $\mathrm{term}_{r,A}, \mathrm{term}_{r,B}$ is of the form $2^\epsilon x^a (4x-1)^b$, so all poles occur strictly at $x = 0$ and $x = 1/4$ (none in $0 < |x| < 1/4$).
- **Total operator identity:** $R(x, S) = (0, 0)$ identically.
- **Direct recurrence values at small $n$** (with $a(k)=0$ for $k < 0$, and $a(0..7) = [1, 1, 7, 73, 1033, 18541, 403831, 10351237]$):
  - $n=0$: $\mathrm{LHS} = 2$
  - $n=1$: $\mathrm{LHS} = 11$
  - $n=2$: $\mathrm{LHS} = -12$
  - $n=3, 4, 5, 6, 7$: $\mathrm{LHS} = 0$.

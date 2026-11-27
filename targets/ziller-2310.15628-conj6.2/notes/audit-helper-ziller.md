# Adversarial & Classical-Literature Audit Report: `ziller-2310.15628-conj6.2`

**Checked (UTC):** 2026-11-27T06:11Z  
**Auditor helper:** `ziller-audit-hlp` (for `@audit-3`)  
**Target:** `targets/ziller-2310.15628-conj6.2/` — Mario Ziller, `arXiv:2310.15628v2`, Conjecture 6.2  
**Isolation compliance:** Strictly observed. Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, or `notes/triage-brief.md`; did NOT edit `TARGET.md` or `PROOF.md`.

---

## Executive Verdict

- **Primary source & status:** **Confirmed open** in both `2310.15628v1` (2023-10-24, numbered **5.10** inside unstepped Concluding remarks) and `2310.15628v2` (2026-04-15, renumbered **Conjecture 6.2** via `\stepcounter{section}` in `Conclusions.tex:4`). No `CONTESTED.md` present.
- **Prior-art & novelty verdict:** **NOVELTY CLEAR (with explicit technique provenance noted).**
  - The exact statement — pairwise distinctness / injectivity of $\varphi(x)/x^2$ (or $x^2/\varphi(x)$, or $m^2\varphi(n) = n^2\varphi(m)$, or $n^\alpha \varphi(n)$ for $\alpha \le -2$ / general $\alpha \notin \{0,-1\}$) — was **NOT found** anywhere in print, arXiv, OEIS, MSE, MO, Mathlib4, Zenodo, Crossref, or competing GitHub repositories.
  - **Closest prior art (sibling exponent $\alpha = 1$, i.e., $n\varphi(n) = \varphi(n^2)$):** The injectivity of $n \mapsto n\varphi(n)$ is well known and proved by the **exact same largest-prime-factor $p$-adic valuation descent** in:
    - **MSE #68120** (*"Why is $f(x) = x\phi(x)$ injective..."*, Greg Martin, `jspecter`, Venkata Karthik Bandaru),
    - **MSE #539558** (*"Injectivity of the function n times the Euler Totient of n"*, Oct 2013, Daniel Fischer),
    - **OEIS A002618** (Franz Vrabec comment, Dec 12, 2012; also cites Peter Giblin, *Primes and Programming*, CUP 1993, p. 116, Exercise 1.10),
    - **Gabdullin, Iudelevich, and Luca (2022/2023)**, *Numbers of the form $kf(k)$*, `arXiv:2201.09287v2` (published *Int. J. Number Theory* 19(5), 2023, pp. 1191–1204), Section 4.
  - **Why sibling prior art does NOT settle Conjecture 6.2:** All four sources prove injectivity only for the integer-valued case $\alpha = 1$ ($n\varphi(n)$). The equations $m\varphi(m) = n\varphi(n)$ and $\varphi(m)/m^2 = \varphi(n)/n^2$ ($n^2\varphi(m) = m^2\varphi(n)$) are distinct statements; none of those sources state or prove injectivity for $\varphi(n)/n^2$, $n^2/\varphi(n)$, or general $n^\alpha\varphi(n)$ ($\alpha \notin \{0,-1\}$).
- **Independent computation rerun (`check-check-3.py`):** **PASS** (exit code `0`, `real 0.93s`).

---

## 1. Primary-Source & Directory Verification

### 1.1 Target directory check
Command: `ls -la targets/ziller-2310.15628-conj6.2/`
- Files present: `PROOF.md`, `TARGET.md`, `verify.py`, `notes/`.
- **No `CONTESTED.md` present.**

### 1.2 arXiv metadata (`2310.15628`)
Command: `.venv/bin/python tools/arxiv_fetch.py query --id-list 2310.15628`
- **ID / Version:** `2310.15628v2` (sole latest version)
- **Title:** *Orders and partitions of integers induced by arithmetic functions*
- **Author:** Mario Ziller
- **Published (v1):** `2023-10-24T08:52:12Z`
- **Updated (v2):** `2026-04-15T17:18:47Z`
- **Comment:** `50 pages, 3 diagrams, revised notations an descriptions`
- **Journal ref / DOI:** `""` / `""` (unpublished preprint)
- **Primary category:** `math.NT`

### 1.3 Exact numbering & v1 vs v2 comparison
Inspected `tools/.arxiv_cache/eprint/2310.15628/` (`Ziller_2023_v2.tex`, `Examples.tex`, `Conclusions.tex`) and `tools/.arxiv_cache/eprint/2310.15628v1.src` (`Ziller_2023.tex`):

- **v2 (`2026-04-15`):**
  - `Ziller_2023_v2.tex:28,30`: `\newtheorem{defi}{Definition}[section]` and `\newtheorem{conj}[defi]{Conjecture}`.
  - Sections 1–5 are `MO.tex`, `EP.tex`, `AFM.tex`, `AFO.tex`, `Examples.tex`.
  - `Examples.tex:327-349` (*Normalised Euler's function, variant 2*): states *"No equal function values are known. Pairwise distinct function values are conjectured."* (`lines 330-331`) and proves **Lemma 5.8** (`lines 337-349`) that $\varphi(x)/x^2 \neq \varphi(y)/y^2$ for distinct *coprime* $x, y \in \mathbb{N}$ (note minor typo in `Examples.tex:343`: `\frac{\varphi(x)}{z^2}` for `\frac{\varphi(z)}{z^2}`).
  - `Conclusions.tex:2-4`: `\section*{Concluding remarks}` followed by `\stepcounter{section}`, advancing the section counter to `6` and resetting `defi` to `0`.
  - `Conclusions.tex:30-32`: summarizes that $\sigma(x)/x^2$, $x^2/\sigma(x)$, $\varphi(x)/x^2$, and $x^2/\varphi(x)$ are conjectured to have pairwise distinct function values.
  - `Conclusions.tex:79`: *"No equal function values are known for each of the functions $\frac{\sigma(x)}{x^2}$ or $\frac{\varphi(x)}{x^2}$ for arbitrary different numbers. However, the corresponding function values for different coprime numbers have been proved to be distinct, respectively."*
  - `Conclusions.tex:85-87`: **Conjecture 6.1** ($\sigma(x)/x^2$ pairwise distinct).
  - `Conclusions.tex:89-91`: **Conjecture 6.2** (exact TeX):
    ```latex
    \begin{conj}
    All function values of ${\displaystyle\frac{\varphi(x)}{x^2}}$ for $x\in\mN$ are pairwise distinct.
    \end{conj}
    ```
  - `Conclusions.tex:93-95`: **Conjecture 6.3** (`\label{distinct_coprime}`, $\sigma(x)/x$ distinct for coprime $x \neq y$).
  - `Conclusions.tex:107-109`: **Corollary 6.4**.
- **v1 (`2023-10-24`, `Ziller_2023.tex`):**
  - Contained the exact same open conjecture (`Ziller_2023.tex:2111-2113`) and the same coprime lemma (`lines 1918-1930`).
  - Difference in numbering: in v1, `\section*{Concluding remarks}` (`line 2025`) did **not** include `\stepcounter{section}`, so the section counter remained `5` (continuing Section 5 `Examples` after Lemma 5.8), making the three conjectures **5.9, 5.10, 5.11** (Conjecture 5.10 = $\varphi(x)/x^2$). In v2, Ziller added `\stepcounter{section}`, renumbering Conjecture 5.10 to **Conjecture 6.2** and keeping it explicitly open.
- **Ziller's follow-up (`arXiv:2604.19646v1`, 2026-04-21):**
  - *Pseudometrics and preorders on sets of integer sequences induced by arithmetic functions* (`tools/.arxiv_cache/eprint/2604.19646.src`): cites `Ziller_2023` (`arXiv:2310.15628`) 6 times, discusses $\varphi$ only in a concrete $\mathbb{Z}/8\mathbb{Z}$ moving-average table (`Conclusions.tex:310-332`), and does NOT mention or resolve Conjecture 6.2.

---

## 2. Extreme Prior-Art & Classical Literature Search (1900–2026-11-27)

### 2.1 Web Search (`search_web`)
All 17 targeted web search queries returned **0 proofs or statements** of injectivity / pairwise distinctness of $\varphi(n)/n^2$, $n^2/\varphi(n)$, $m^2\varphi(n) = n^2\varphi(m)$, or $n^\alpha \varphi(n)$ for $\alpha \le -2$ / $\alpha \notin \{0, -1\}$:
1. `"phi(n)/n^2" OR "varphi(n)/n^2" OR "n^2/phi(n)" injective OR distinct OR "one-to-one"` — no match for injectivity of $\varphi(n)/n^2$.
2. `"phi(m)/m^2" OR "phi(x)/x^2" OR "varphi(x)/x^2" OR "phi(a)/a^2 = phi(b)/b^2"` — no match.
3. `"phi(n)" "n^2" injective OR "one-to-one" site:math.stackexchange.com OR site:mathoverflow.net` — only $\phi(n)$ non-injectivity and $\phi(n^2) = n\phi(n)$.
4. `"n*phi(n)" OR "n phi(n)" injective OR "one-to-one" "largest prime" OR "p-adic"` — hit OEIS A002618 and MSE #539558 / #68120 (proving $\alpha = 1$, $n\varphi(n)$, via largest prime factor).
5. `"phi(n)/n^k" OR "n^k phi(n)" OR "n^a phi(n)" injective OR "one-to-one"` — only $k = 1$ ($n\varphi(n)$).
6. `"Mario Ziller" "2310.15628" OR "Orders and partitions of integers induced by arithmetic functions"` — only Ziller's own arXiv preprint.
7. `"phi(m) n^2 = phi(n) m^2" OR "m^2 phi(n) = n^2 phi(m)" OR "x^2 phi(y) = y^2 phi(x)" OR "a^2 phi(b) = b^2 phi(a)"` — no match.
8. `"539558" "injectivity-of-the-function-n-times-the-euler-totient-of-n" OR ...` — MSE #539558 (`Daniel Fischer`, Oct 2013, $n\varphi(n)$ only).
9. `"Numbers of the form kf(k)" OR "2201.09287" "Gabdullin" "injective" OR "phi"` — `arXiv:2201.09287` (inspected directly below; $n\varphi(n)$ only).
10. `"A373318" OR "A373319" OR "phi(n)/n^2" "unitarily divided" OR "distinct" OR "injective"` — OEIS A373318/A373319 only.
11. `"539558" "Vrabec" OR "Daniel Fischer" ...` — $n\varphi(n)$ only.
12. `"varphi(x)/x^2" OR "phi(x)/x^2" OR "phi(m) n^2 = phi(n) m^2" ...` — no match.
13. `"Orders and partitions of integers induced by arithmetic functions" "Ziller" cited OR citing OR conjecture` — no citing resolutions.
14. `"phi(m)/phi(n) = m^2/n^2" OR "phi(m)/phi(n) = (m/n)^2" ...` — no match.
15. `"n^a phi(n)" OR "n^k phi(n)" OR "n^alpha phi(n)" OR "phi(n)/n^alpha" injective OR "pairwise distinct"` — only $n\varphi(n)$ and `2201.09287`.
16. `"phi(n)/n^2" "Sandor" OR "Mitrinovic" OR "Sivaramakrishnan" OR "Pomerance" OR "Carmichael" OR "Putnam" OR "AMM"` — no match.
17. Additional checks (`"Giblin" "Primes and Programming" ...`, `"phi(m)/m^2 = phi(n)/n^2" ...`, `"phi(n)/n^2" "all values" ...`, `"m^2 * phi(n) = n^2 * phi(m)" ...`, `"erdosproblems.com/121" ...`, `"phi(m^2) = phi(n^2)" ...`, `"phi(n)/n^2" "p-adic" ...`, `"n^2/phi(n)" "largest prime" ...`, `"Handbook of Number Theory" "Sandor" ...`, `"n^k \phi(n)" ...`, `"if m\phi(m)=n\phi(n)" ...`, `"ysharifi" ...`, `"phi(n)/n^2" ... site:math.stackexchange.com OR site:mathoverflow.net OR site:artofproblemsolving.com`) — all negative for $\varphi(n)/n^2$, $n^2/\varphi(n)$, or general $n^\alpha \varphi(n)$.

### 2.2 StackExchange API (MSE & MathOverflow)
Direct queries via `https://api.stackexchange.com/2.3/...`:
- **MSE #68120** (*"Why is $f(x) = x\phi(x)$ injective, i.e. $x\phi(x) = y\phi(y) \Rightarrow x = y$"*): answers by Greg Martin (score 15), `jspecter` (score 10), Venkata Karthik Bandaru (score 1) prove $x\varphi(x)$ is injective via largest prime factor $p$-adic exponent $2\alpha - 1$. Does not mention $\varphi(x)/x^2$ or other powers of $x$.
- **MSE #539558** (*"Injectivity of the function n times the Euler Totient of n"*): answer by Daniel Fischer (score 8) proves $n\varphi(n)$ is injective via $p^{2k-1} \parallel f(n)$ and multiplicativity. Does not mention $\varphi(n)/n^2$ or general $n^\alpha \varphi(n)$.
- **MSE #4874740** (*"On which natural numbers do we have injectivity of Euler's totient function?"*): relates to Carmichael's conjecture for $\varphi(n)$ itself.
- Additional StackExchange API searches (`totient+injective`, `phi+injective`, `phi(n)+distinct+values`, `"phi(n)/n"+injective`, `n*phi(n)+injective`, `phi(n^2)+injective`, `varphi(n)+n^2+distinct` on MSE; `totient+injective`, `phi(n)/n^2+OR+n*phi(n)+injective`, `totient+distinct+values` on MO): **0 threads** on $\varphi(n)/n^2$ or $n^2/\varphi(n)$ injectivity.

### 2.3 OEIS Live JSON API (`User-Agent: curl/8.7.1`, timeout 15s)
- **`A373318`** (author: Amiram Eldar, Jun 01 2024, rev 9): *Numerator of the asymptotic density of numbers that are unitarily divided by n* (`1,1,2,1,4,1,6,1,2,1,...`), $f(n) = \varphi(n)/n^2 = a(n)/A373319(n)$. **No mention** of injectivity or pairwise distinctness in `comment`, `formula`, or `link`.
- **`A373319`** (author: Amiram Eldar, Jun 01 2024, rev 15): *Denominator of the asymptotic density of numbers that are unitarily divided by n* (`1,4,9,8,25,18,49,16,27,25,...`). **No mention** of injectivity or pairwise distinctness. (Note: `A373319` erroneously links `erdosproblems.com/121` — a typo for `A373119`, verified in `watch/snapshots/erdosproblems/pulls.json`.)
- **`A373320`** (author: Amiram Eldar, Jun 01 2024, rev 7): *Numbers $k$ such that $\varphi(k)/k^2 < \varphi(m)/m^2$ for all $m < k$*. **No mention** of injectivity.
- **Cross-references of `A373318` (`A064549`, `A076512`, `A109395`, `A173557`):** **No mention** of injectivity of $\varphi(n)/n^2$.
- **`A002618`** ($a(n) = n\varphi(n) = \varphi(n^2)$): Franz Vrabec (Dec 12 2012) notes $n \mapsto n\varphi(n)$ is injective, linking MSE #539558, `arXiv:2201.09287`, `arXiv:2001.03736`, and Giblin (1993, p. 116 Ex. 1.10). **No mention** of $\varphi(n)/n^2$ or general $n^\alpha \varphi(n)$.
- **`A002619`**: unrelated 2-colored patterns on $n \times n$ board.

### 2.4 arXiv, OpenAlex, Crossref, Zenodo, Semantic Scholar, Mathlib4
- **arXiv API (`tools/arxiv_fetch.py`):**
  - `all:2310.15628` -> `1` result (`2310.15628v2`).
  - `au:Ziller` -> `79` total results (top result `2604.19646v1`, inspected above; does not resolve Conj 6.2).
  - `all:totient AND all:injective` -> `3` results:
    1. `2609.23901v1` (Hang Fu, Sep 2026): *On the noninjectivity of Jordan's totient functions* ($J_k(n) = n^k \prod_{p\mid n}(1-p^{-k})$ for $k=3,4,6$). Inspected `Jordan.tex` directly: does not mention Ziller or $\varphi(n)/n^2$.
    2. `2608.19191v1` (L. A. Lizama-Pérez, Aug 2026): cryptographic totient preimage problem.
    3. `2606.23681v2` (Eric Li, Aug 2026): shifted equal values $\varphi(n) = \varphi(n+h)$.
  - `all:"pairwise distinct" AND all:totient` -> `0` results.
  - Note: one chained call (`all:euler AND all:totient AND all:injective`) hit an HTTP `TimeoutError` from `export.arxiv.org`.
  - Direct inspection of `2201.09287.src` (`Gabdullin–Iudelevich–Luca`) and `2001.03736.src` (`Krachun–Sun`): `2201.09287` proves $k \mapsto k\varphi(k)$ is injective in 4 lines (Section 4) and never considers $\varphi(k)/k^2$ or $k^\alpha\varphi(k)$; `2001.03736` proves $\varphi(m^2)/\varphi(n^2)$ surjects $\mathbb{Q}_{>0}$ and does not prove $\varphi(n)/n^2$ injectivity.
- **OpenAlex:**
  - `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2310.15628` returns `OA id: https://openalex.org/W4387947328`, `cited_by_count: 1`, `title: Orders and partitions of integers induced by arithmetic functions`. (Note: `watch/snapshots/arxiv/openalex_works_cache.json` had cached `openalex_id: null` because it queried by `arxiv.org/abs/2310.15628` rather than the arXiv DOI.)
  - **Coverage gap:** Querying `https://api.openalex.org/works?filter=cites:W4387947328` hit OpenAlex's unauthenticated daily IP rate limit (`daily_budget`, `$0 remaining`). Likewise Semantic Scholar (`ARXIV:2310.15628`) returned HTTP `429`. However, Ziller's own `arXiv:2604.19646v1` (2026-04-21) explicitly cites `Ziller_2023` (`arXiv:2310.15628`) 6 times, accounting for the 1 citation.
- **Crossref:** Query for paper title returned 0 matching Ziller records (preprint only).
- **Zenodo:** `q=2310.15628 OR "Mario Ziller"` returned `1` hit: `10.5281/zenodo.22710993` (Michel Reyrolle, 2026-08-27, citing Ziller & Morack 2016 on Jacobsthal's function — unrelated).
- **Mathlib4 (local v4.36.0):** Inspected `Mathlib/Data/Nat/Totient.lean` — no injectivity theorem for `n * φ n`, `φ n / n^2`, or `n^α * φ n`.

### 2.5 Local Snapshots & Competing GitHub Repositories
- **`tools/novelty_grep.py` on `watch/snapshots/**` (522 files):**
  - `"2310.15628" "Ziller" "phi(x)/x^2" "varphi(x)/x^2" "phi(n)/n^2" "varphi(n)/n^2"`: 22 lines across 8 files — only our own target tracking (`watch/snapshots/arxiv/citing/ziller-2310.15628-conj6.2.json`, `latest_sweep.json`, `openalex_works_cache.json`, `formal/last_sweep.json`) and unrelated Erdős #854 (`Gerbicz u(n), Ziller`).
  - Subset greps for `"totient" "varphi" "eulerphi"` in `watch/snapshots/1337-solved-conjectures`, `watch/snapshots/openai-math`, `watch/snapshots/discovered`: 0 matches for Ziller or $\varphi(x)/x^2$.
  - `watch/snapshots/arxiv/cat_math.NT.json` and `recent_arxiv.json`: 0 occurrences of `2310.15628`, `ziller`, `varphi(x)/x^2`, `phi(x)/x^2`.
- **Direct GitHub tree inspection via `gh api repos/<owner>/<repo>/git/trees/HEAD?recursive=1`:**
  Checked all 15 named competing repos plus 17 `the-omega-institute/*` repos (`trureturing*` [note `trureturing-requests` is empty HTTP 409], `automath`, `newmath`, `mathesis`). **0 filename matches** for `ziller`, `2310`, `conj6`, or `varphi` across all repositories (`1337isnot1337/solved-conjectures` [19,918 files], `aliromman/math` [937], `KnowledgeSense/math` [5,377], `rainwangphy/aftd-platform` [28,161], `valyuAI/research` [5,381], `facebookresearch/atlas-lean` [54,084], `JENW1N/complete-math-solutions` [425], `TheJustinSunPrize/awards` [82], `GuillaumeBAUD-coder/open-math-agents` [2,053], `DomTheDeveloper/open-math-agents` [1,978], `DomTheDeveloper/ProofPlaygrond` [68], `CrocSwap/integer-mult-bounds` [54,080], `linustalacko/small-true-things` [37], `chy4pro/automath` [2,969], `openai/math` [55,175], `the-omega-institute/*` [~140k+ files]).
- **GitHub global & repo-scoped `gh search`:**
  - `gh search code '2310.15628'`: 7 hits — 1 arXiv RSS snapshot (`ehijano/rss_fetch`, `2026-04-16_math.NT.xml`) + 6 floating-point numeric coincidences.
  - `gh search code 'Ziller varphi'`, `'Ziller 2310'`, `gh search issues '2310.15628 OR Ziller'`: 0 hits.
  - Repo-scoped `gh search code` on `1337isnot1337/solved-conjectures`, `rainwangphy/aftd-platform`, `openai/math`, `facebookresearch/atlas-lean` for `2310.15628` and `Ziller`: all 0 hits (11th query `the-omega-institute/trureturing-experiments Ziller` hit GitHub code-search secondary rate limit HTTP 403).

---

## 3. Independent Computation Rerun

Command run:
```bash
/usr/bin/time -p .venv/bin/python -u targets/ziller-2310.15628-conj6.2/notes/check-check-3.py
```
- **Exit code:** `0`
- **Raw output:**
```text
Injectivity PASS: all 200000 reduced fractions phi(x)/x^2 (1 <= x <= 200000) are pairwise distinct.
Proof Lemma & Descent PASS: product formula, v_p(f(n)) == -(e+1), and p^e-descent verified.
PASS
real 0.93
user 0.60
sys 0.08
```

# Adversarial Audit Helper Report — `oeis-A208425` (`conjecture_2`)

**Timestamp (UTC):** 2026-11-27T02:47:00Z  
**Agent:** `a208425-audit-hlp` (assisting `@audit-2`, strict isolation observed)  
**Target:** `targets/oeis-A208425/` — OEIS `A208425` rev 60 / `FormalConjectures/OEIS/208425.lean` `OeisA208425.conjecture_2`  

---

## 1. Primary-Source Verbatim Check

### 1.1 Target Directory Check (`ls -la targets/oeis-A208425/`)

Observed contents:
- `PROOF.md` (22534 bytes)
- `TARGET.md` (3409 bytes)
- `verify.py` (12066 bytes)
- `notes/` (directory)
- **No `CONTESTED.md` present.**

### 1.2 Live OEIS JSON: `A208425`

Fetched live from `https://oeis.org/search?q=id:A208425&fmt=json` (`User-Agent: curl/8.7.1`, timeout 15s):

- **`number`:** `208425`
- **`revision`:** `60`
- **`time`:** `"2025-11-05T15:22:21-05:00"` (`created`: `"2012-02-26T17:25:41-05:00"`)
- **`name`:**
  > `Expansion of Sum_{n>=0} (3*n)!/n!^3 * x^(2*n)/(1-x)^(3*n+1).`
- **`data` (24 terms, offset `0,3`):**
  > `1,1,7,25,151,751,4411,24697,146455,862351,5195257,31392967,191815339,1177508515,7276161907,45154764025,281492498455,1761076827895,11055132835705,69600761349175,439370198255401,2780265190892641,17631718101804517,112038660509078695`
- **`formula` (all 5 entries verbatim):**
  1. `Conjecture: n^2*(3*n-5)*a(n) +(-9*n^3+24*n^2-17*n+4) *a(n-1) -(3*n-4) *(24*n^2-56*n+27)*a(n-2) -(3*n-2)*(n-2)^2*a(n-3)=0. - _R. J. Mathar_, Mar 10 2016`
  2. `a(n) ~ sqrt(1/2 + sqrt(13)*cos(arctan(53*sqrt(3)/19)/3)/6) * (1 + 6*cos(Pi/9))^n / (Pi*n). - _Vaclav Kotesovec_, Jul 05 2016`
  3. `It is easy to show that a(n) = Sum_{k=0..n}C(n,k)*C(n-k,k)*C(n+k,k) = Sum_{k=0..n}C(n+k,k)*C(n,2k)*C(2k,k). By this formula and the Zeilberger algorithm, we confirm the recurrence conjectured by _R. J. Mathar_. - _Zhi-Wei Sun_, Nov 12 2016`
  4. `G.f. y=A(x) satisfies: 0 = x*(x + 2)*(x^3 + 24*x^2 + 3*x - 1)*y'' + (3*x^4 + 56*x^3 + 147*x^2 + 12*x - 2)*y' + (x^3 + 9*x^2 + 42*x + 2)*y. - _Gheorghe Coserea_, Jul 03 2018`
  5. `a(n) = hypergeom([1/2 - n/2, -n/2, n + 1], [1, 1], 4). - _Peter Luschny_, Jan 11 2025`
- **Verbatim Zhi-Wei Sun comment (`comment[1..4]`):**
  > `From _Zhi-Wei Sun_, Nov 12 2016: (Start)`  
  > `Conjecture: (i) For any prime p > 3 and positive integer n, the number (a(p*n)-a(n))/(p*n)^3 is always a p-adic integer.`  
  > `(ii) For any prime p == 1 (mod 3), we have Sum_{k=0..p-1}a(k) == C(2(p-1)/3,(p-1)/3) (mod p^2). For any prime p == 2 (mod 3), we have Sum_{k=0..p-1}a(k) == 2p/C(2(p+1)/3,(p+1)/3) (mod p^2).`  
  > `We have proved part (i) of this conjecture for n = 1. (End)`
- **Relevant OEIS `link` entries:**
  - `Hao Pan and Zhi-Wei Sun, arXiv:2012.05121 [math.NT], 2020` (*Supercongruences for central trinomial coefficients*)
  - `Zhi-Wei Sun, arXiv:1610.03384 [math.NT], 2016` (*Supercongruences involving Lucas sequences*)

### 1.3 Live OEIS JSON: `A066796` (Adamchuk's Sequence)

Fetched live from `https://oeis.org/search?q=id:A066796&fmt=json` (`User-Agent: curl/8.7.1`, timeout 15s):

- **`number`:** `66796`
- **`revision`:** `73`
- **`time`:** `"2026-08-30T12:26:43-04:00"` (`created`: `"2003-05-16T03:00:00-04:00"`)
- **`name`:**
  > `a(n) = Sum_{i=1..n} binomial(2*i,i).`
- **`data` (first 24 terms, offset `1,1`):**
  > `2,8,28,98,350,1274,4706,17576,66196,250952,956384,3660540,14061140,54177740,209295260,810375650,3143981870,12219117170,47564380970,185410909790,723668784230,2827767747950,11061198475550,43308802158650`
- **Relevant Adamchuk comments:**
  - Jul 02, 2006: `a(p-1) is divisible by p^2 for primes p=7,13,19,31,37,43,... Primes of form 6n+1. A002476.`
  - Jan 04, 2007: `a(2(p-1)/3) is divisible by p^2 for prime p = {7,13,19,31,37,43,61,...} = A002476 Primes of form 6n+1.`
- **Relevant `link` entries on `A066796`:**
  - `Guo-Shuai Mao, arXiv:2003.09810 [math.NT], 2020` (*Proof of a conjecture of Adamchuk*)
  - `Guo-Shuai Mao, arXiv:2003.14221 [math.NT], 2020` (*On a supercongruence conjecture of Z.-W. Sun*)
  - `Guo-Shuai Mao, On some supercongruence conjectures of Z.-W. Sun, ResearchGate, 2023`
  - `Guo-Shuai Mao, Proof of some congruences via the hypergeometric identities, ResearchGate, 2023`
  - `Guo-Shuai Mao, On two pairs of congruence conjectures of Z.-W. Sun, ResearchGate, 2024`
  - `Guo-Shuai Mao and Roberto Tauraso, arXiv:2004.09155 [math.NT], 2020`
  - `Guo-Shuai Mao and Dong-Hui Zhang, On some congruences involving harmonic numbers and Bernoulli polynomials, ResearchGate, 2023`

### 1.4 `FormalConjectures/OEIS/208425.lean` Verbatim Check

Verified via `gh api repos/google-deepmind/formal-conjectures/contents/FormalConjectures/OEIS/208425.lean` (matching `watch/snapshots/formal/formal-conjectures-files.tsv` line 1318, blob SHA `6692a6604859e2615fd452aa1f41cade8b6f8dcc`, 2822 bytes; no open/closed issues or PRs in `google-deepmind/formal-conjectures` mentioning `208425`):

- **`a`:**
```lean
def a (n : ℕ) : ℕ :=
  ∑ k ∈ Finset.range (n + 1), n.choose k * (n - k).choose k * (n + k).choose k
```
- **`conjecture_1` (`@[category research open, AMS 11]`):**
```lean
theorem conjecture_1 (p : ℕ) (hp : p.Prime) (hpgt3 : 3 < p) (n : ℕ) (hn : 0 < n) :
    0 ≤ padicValRat p (((a (p * n) : ℚ) - (a n : ℚ)) / ((p * n : ℚ) ^ 3)) := by
  sorry
```
- **`conjecture_2` (`@[category research open, AMS 11]`):**
```lean
theorem conjecture_2 (p : ℕ) (hp : p.Prime) (hmod : p % 3 = 1) :
    (∑ k ∈ Finset.range p, a k) % (p ^ 2) =
      ((2 * (p - 1) / 3).choose ((p - 1) / 3)) % (p ^ 2) := by
  sorry
```
- **`conjecture_3` (`@[category research open, AMS 11]`):**
```lean
theorem conjecture_3 (p : ℕ) (hp : p.Prime) (hmod : p % 3 = 2) :
    ((∑ k ∈ Finset.range p, (a k : ℚ)) -
      (2 * p : ℚ) / ((2 * (p + 1) / 3).choose ((p + 1) / 3) : ℚ)).num % (p ^ 2 : ℤ) = 0 := by
  sorry
```

All four Lean declarations match OEIS `A208425` rev 60 verbatim (`conjecture_2` uses integer division `/ 3`, which is exact when `p % 3 = 1`).

---

## 2. Deep Novelty & Prior-Art Check

### 2.1 Guo-Shuai Mao, `arXiv:2003.09810v4` (*Proof of a conjecture of Adamchuk*)

Fetched and extracted via `.venv/bin/python tools/arxiv_fetch.py eprint 2003.09810 --extract` (`tools/.arxiv_cache/eprint/2003.09810/main.tex`, 584 lines).  
- **arXiv versions:** `[v1]` 2020-03-22 through `[v4]` 2020-04-05.
- **Journal reference (from arXiv abs & OpenAlex/Crossref):** *Journal of Combinatorial Theory, Series A* **182** (2021), Art. 105478, DOI `10.1016/j.jcta.2021.105478` (note: volume 182, not 181).

**Verbatim Theorem 1.1 (`\label{Thadam}`, `main.tex` lines 101–106):**
```latex
\begin{thm}\label{Thadam}
Let $p$ be an odd prime and let $a\in\mathbb{Z}^{+}$. If $p\equiv1\pmod 3$ and $a\in\mathbb{Z}^{+}$, then
\begin{align*}
\sum_{k=1}^{\frac{2}3(p^a-1)}\binom{2k}k\equiv0\pmod{p^2}.
\end{align*}
\end{thm}
```

**Verbatim Theorem 1.2 (`\label{Th3k1}`, `main.tex` lines 108–112):**
```latex
\begin{thm}\label{Th3k1} For any prime $p\equiv1\pmod 3$, we have
\begin{align*}
\sum_{\substack{k=0\\k\neq(p-1)/3}}^{(p-1)/2}\frac{\binom{2k}k}{3k+1}\equiv0\pmod{p}.
\end{align*}
\end{thm}
```

**Presence of `A208425` / Sun Conjecture (ii) in `2003.09810v4`:**  
Full-text reading of all 584 lines and case-insensitive regex grep (`208425|A208425|binom\{[kn]\}\{j\}|binom\{[kn]-j\}\{j\}|Conjecture \(ii\)|Conjecture ii|Zhi-Wei Sun`) returned **zero matches**. Mao `2003.09810v4` proves Theorem 1.2 purely as a lemma to establish Theorem 1.1 (Adamchuk's conjecture on `A066796`) and **never mentions `A208425`, $\sum_{j=0}^{p-1} a(j)$, or Zhi-Wei Sun's Nov 12, 2016 Conjecture (ii)**.

### 2.2 Pan–Sun `arXiv:2012.05121v3` & Sun's Conjecture Lists (`arXiv:0911.5665`, `1610.03384v8`, `2006.02918v3`)

- **Hao Pan & Zhi-Wei Sun, `arXiv:2012.05121v3`** (*Supercongruences for central trinomial coefficients*, v3 updated 2026-03-13; *Frontiers in Combinatorics and Number Theory* **2** (2026), 55–62; DOI `10.3934/fcnt.2026012`), `tools/.arxiv_cache/eprint/2012.05121/261p.tex` (429 lines):
  - Defines $(a_n)$ via `A208425` (lines 174–187) and proves **only** `conjecture_1` (`Theorem 1.2`, lines 189–191: `(a_{pn}-a_n)/(pn)^3 \in \mathbb{Z}_p` for prime $p>3, n\ge 1$).
  - **Does not mention or prove `conjecture_2` or `conjecture_3`.**
- **Zhi-Wei Sun, `arXiv:0911.5665`** (*Open Conjectures on Congruences*, `tools/.arxiv_cache/eprint/0911.5665/source.txt`):
  - `A208425` is not present. Conjecture A46(i) (lines 1215–1220) has the same right-hand side $\binom{2(p-1)/3}{(p-1)/3} \pmod{p^2}$ for $p \equiv 1 \pmod 3$, but its left-hand side is $\sum_{k=0}^{p-1} \frac{\binom{3k}{k,k,k}}{24^k}$, a different sequence (later proved by Chen Wang & Zhi-Wei Sun, `arXiv:2006.02918v3`, inspected locally: zero mentions of `A208425`).
- **Zhi-Wei Sun, `arXiv:1610.03384v8`** (*Supercongruences involving Lucas sequences*, updated 2020-12-14):
  - Linked from `A208425`, inspected `source.txt` locally: zero mentions of `A208425` or $\sum_{k=0}^{p-1} a(k)$.

### 2.3 Citing Works & 2016–Nov 27, 2026 Literature Search

Searched OpenAlex, Crossref, Zenodo, arXiv (`tools/arxiv_fetch.py`), and `search_web`:

1. **All 6 works in OpenAlex citing Mao `2003.09810` (`W3012943594`):**
   - `arXiv:2004.09155v3` (Mao & Tauraso, 2020/2021): central binomial sums $\sum_{k=1}^{\lfloor ap/r\rfloor}\binom{2k}{k}x^k \pmod{p^2}$; zero matches for `A208425` / $\sum a(k)$.
   - `10.1007/s11139-022-00668-z` (Wei Xia, 2022): *Proof of a conjecture of Sun and its extension by Guo*.
   - `arXiv:2003.14221` (Mao, 2020/2022): $\sum_{k=0}^{\lfloor 5p^a/6\rfloor}\binom{2k}{k}/16^k \pmod{p^2}$; zero matches for `A208425`.
   - `10.1017/s0004972724000121` (Mao, 2024): $\sum_{k=1}^{p-1}\binom{2k}{k}/(k2^k) \pmod{p^3}$.
   - `arXiv:2407.19882` (Chen Wang & Huili Han, 2024): Euler polynomials & binomial sums; zero matches for `A208425`.
   - `10.1080/10652469.2026.2637160` (Mao & Zhang, Feb 2026): harmonic numbers & Bernoulli polynomials mod $p$ / $p^2$.
2. **All 3 works in OpenAlex citing Pan–Sun `2012.05121` (`W7135236084`):**
   - `10.1216/rmj.2022.52.1105`, `10.1216/rmj.2024.54.943`, and `arXiv:2312.13613` (Qing-Hu Hou & Na Li, *Reduction on the congruences of partial sums of P-recursive sequences*; `SCongru.tex` inspected locally: proves congruences for $W_k^2$ and $T_k T_{k+1}$, no mention of `A208425`).
3. **Additional Mao, Sun, Wang, Guo, Liu papers checked:**
   - `arXiv:2012.04523` (Chen & Wang), `arXiv:2111.08775` (Mao & Liu), `arXiv:2201.03418` (Mao), `arXiv:2304.04548` (Mao), `arXiv:2403.03301` (modular forms & supercongruences), `arXiv:2607.07638v3` (Sun, Jul 2026), `arXiv:2505.02767v4` (Sun, 2025/2026), plus OpenAlex abstracts/titles of Mao's 2020–2026 publications and arXiv queries (`all:208425`, `abs:"208425" OR abs:"A208425"`, `ti:"central trinomial" AND au:Sun`, `ti:congruence AND au:"Guo-Shuai Mao"`, `au:"Zhi-Wei Sun" AND (ti:congruence OR ti:supercongruence)`).
   - **Result:** No published paper or preprint proves `A208425` `conjecture_2`. (Caveat: paywalled ResearchGate/journal full texts without arXiv preprints — e.g., Mao's 2023–2025 journal articles and 2023/2024 ResearchGate preprints linked on `A066796` — could not be read in full, though none are linked on `A208425` or returned for `A208425` in OpenAlex/Crossref/arXiv/web search.)

### 2.4 Competing GitHub Repositories & Local Watch Snapshots

1. **Local watch snapshots (`tools/novelty_grep.py A208425 208425 2003.09810 2012.05121`):**
   - Matched 15 lines across 7/413 files: solely `2012.05121` (`oeis-A208425.json`, `openalex_works_cache.json`), `FormalConjectures/OEIS/208425.lean` (`formal-conjectures-files.tsv`, `last_sweep.json`), and `Varun-Dudipala/sun-conjectures-lean` (`CATALOG.md`, `catalog.json`, `Varun-Dudipala__sun-conjectures-lean.json`).
2. **`Varun-Dudipala/sun-conjectures-lean` (direct inspection of `README.md`, `SunConjectures/A208425/README.md`, `Challenge.lean`, `Solution.lean`):**
   - Proves **only** `OeisA208425.conjecture_3` ($p \equiv 2 \pmod 3$).
   - `SunConjectures/A208425/README.md` explicitly states: *"The companion statements, part (i) and the case $p \equiv 1 \pmod 3$, are not proved here."*
   - Neither `Challenge.lean` nor `Solution.lean` contains `conjecture_2`.
3. **`epoch-research/LeanOpenProblems` & `LeanOpenProblems-results`:**
   - Inspected `apn/data/oeis/Isolated` and `metadata/oeis/conjectures.json`: contains **only** `oeis_208425_conjecture_0` (`conjecture_1`, Pan–Sun); `conjecture_2` is absent.
4. **`BoltonBailey/formal-conjectures-ai-review`:**
   - `audits/FormalConjectures/OEIS/208425/OeisA208425-conjecture_2.json` is solely a statement-faithfulness check against OEIS A208425, not a proof.
5. **Other competing repositories checked via `gh api` recursive trees / `CONTENTS.md` / issues / `gh search code`:**
   - `1337isnot1337/solved-conjectures` (`CONTENTS.md` and all issues): 0 matches.
   - `the-omega-institute/trureturing`, `trureturing-pages`, `trureturing-experiments`, `mathesis`: 0 matches for `208425`.
   - `aliromman/math`: 0 matches (`SunCircularDifferences`, `SunLucasRatios`, `SunPrimePowers`, `SunRealCycles` only).
   - `KnowledgeSense/math`: 0 matches.
   - `rainwangphy/aftd-platform`: 0 matches.
   - `valyuAI/research`: 0 matches.
   - `facebookresearch/atlas-lean`: 0 matches (checked full `oeis` tree and `WantedExt/NumberTheory/OeisConjecturesWanted.lean`).
   - `JENW1N/complete-math-solutions`: 0 matches (`SunConjecture5` only).
   - `TheJustinSunPrize/awards`: 0 matches.
   - `openai/math`: 0 matches for `208425` as an OEIS/problem identifier (`gh search code` hits were only arbitrary decimal digits inside interval bounds).
   - Global `gh search code "208425 conjecture_2"`: 0 results.

**Novelty conclusion:** `OeisA208425.conjecture_2` ($p \equiv 1 \pmod 3$) remains **OPEN** in `google-deepmind/formal-conjectures`, on OEIS `A208425` rev 60, in the 2016–Nov 27, 2026 mathematics literature (including Mao `2003.09810v4` and Pan–Sun `2012.05121v3`), and across all checked public AI-math/Lean repositories.

---

## 3. Independent Exact Computation Check

**Command:**
```sh
time .venv/bin/python -u targets/oeis-A208425/notes/check-check-2.py 2>&1
```

**Raw Output:**
```text
OEIS A208425 rev 60 definitions (GF == trinomial sum, all 24 live OEIS DATA terms): PASS
Lemmas 1, 2, 3 (incl. full 3-orbit F_p check for p<=200, direct sum p<=250) on 45 primes p<500: PASS
Lemmas 4 & 5 (exact Q[X] telescoping, F_p[X] ODE match, mod Phi(X) reduction) on [7, 13, 19, 31, 37, 43]: PASS
Target conjecture_2 verified across all 80 primes p == 1 (mod 3), p < 1000: PASS
PASS (all checks passed in 2.309s)
.venv/bin/python -u targets/oeis-A208425/notes/check-check-2.py 2>&1  1.75s user 0.17s system 80% cpu 2.383 total
```

**Exit code:** `0`  
**Runtime:** `2.309s` script internal elapsed (`2.383s` wall total, `1.75s` user, `0.17s` sys).

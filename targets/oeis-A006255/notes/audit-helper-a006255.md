# Adversarial Audit Helper Report: `targets/oeis-A006255/`

- **Helper:** `a006255-audit-hlp` (for `@audit-2`)
- **Timestamp (UTC):** `2026-11-26T22:50:30Z`
- **Target:** OEIS `A006255` — Padhi's (2026) correction to Corneth's (2016) conjecture:
  > *"Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"*
- **Strict Isolation Confirmed:** Read only live OEIS endpoints, `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, `watch/snapshots/**`, `tools/.arxiv_cache/eprint/{2410.04728,2504.19196}`, and public APIs. Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, `notes/helper-*`, `notes/build_covering.py`, or `notes/covering-*`, and did NOT edit `TARGET.md` or `PROOF.md`.

---

## 1. Live OEIS Primary-Source Inspection (`User-Agent: curl/8.7.1`)

Fetched directly from `https://oeis.org/search?q=id:<ID>&fmt=json`, `https://oeis.org/A006255/b006255.txt`, and `https://oeis.org/history?seq=A006255`.

### 1.1 `A006255` (Revision `106`, `2026-06-19T00:16:16-04:00`)
- **Created:** `1991-07-11T03:00:00-04:00` | **ID:** `M4064` | **Offset:** `1,2` | **Keywords:** `nonn,nice`
- **Author:** `_N. J. A. Sloane_ and _Robert G. Wilson v_`
- **Name:** `R. L. Graham's sequence: a(n) = smallest m for which there is a sequence n = b_1 < b_2 < ... < b_t = m such that b_1*b_2*...*b_t is a perfect square.`
- **Comments (all 10 entries in JSON):**
  1. `Every nonprime appears exactly once in this sequence.`
  2. `If n is a square we can take t=1 and a(n) = n. If n is a prime > 3, then a(n) = 2n and t=3. If n is twice a prime, say p, then a(n) = 3p most of the time. The sequence b_1 < b_2 < ... < b_t will not contain either perfect squares or primes for they bring nothing to the solution. Also I know of no n such that t = 2. - _Robert G. Wilson v_, Jan 30 2002`
  3. `Let k be a fixed integer and p be a prime, then a(k*p) = (k+1)*p for sufficiently large p. - _Peter Kagey_, Feb 03 2015`
  4. `From _David A. Corneth_, Oct 26 2016: (Start)`
  5. `Is for all k*p in A277624, a(k*p) = (k+1) * p?`
  6. `Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]`
  7. `(End)`
  8. `a(n) <= A072905(n).`
  9. `a(n) <= 2*n for all n > 3.`
  10. `a(n) >= n + A006530(A007913(n)) for all nonsquare n. - _Peter Kagey_, Feb 21 2015`
- **References:**
  - `R. L. Graham, D. E. Knuth and O. Patashnik, Concrete Mathematics. Addison-Wesley, Reading, MA, 2nd. ed., Problem 4.39, pages 147, 616, 533. [Reference revised by _N. J. A. Sloane_, Jan 13 2014]`
  - `N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).`
- **Links:**
  - `Peter Kagey, Table of n, a(n) for n = 1..10000` (`/A006255/b006255.txt`)
  - `Sarosh Adenwalla, On a Generalisation of a Function of Ron Graham's, arXiv:2504.19196 [math.NT], 2025.`
  - `R. L. Graham, Bijection between integers and composites, Problem 1242, Math. Mag., 60 (1987), p. 180.`
  - `Peter Kagey and Krishna Rajesh, On a Conjecture about Ron Graham's Sequence, arXiv:2410.04728 [math.NT], 2024.`
- **Formulas:**
  - `If n is a square we can take t=1 and a(n)=n.`
  - `a(n) = A245499(n,A066400(n)). - _Reinhard Zumkeller_, Jul 25 2014`
  - `a(n) = A092487(n) + n. - _Peter Kagey_, Oct 22 2016`
- **Examples / Xrefs / Extensions:**
  - `a(2) = 6 because the best such sequence is 2,3,6.`
  - `For n = 3 through 6 the {smallest m then smallest t then smallest product} solutions are 3,6,8; 4; 5,8,10; 6,8,12.`
  - Xrefs: `A066400`, `A066401`, `A233421`, `A067565`, `A245499`, `A070229`, `A072905`, `A092487`.
  - Ext: More terms from `_Robert G. Wilson v_, Jan 30 2002`; erroneous program removed by `_Reinhard Zumkeller_, Nov 28 2014`.
- **Confirmation:** **No** comment, link, or reference on `A006255` proves the Corneth/Padhi conjecture.

### 1.2 Revision History & Attribution (`https://oeis.org/history?seq=A006255`)
- **Original conjecture author:** **David A. Corneth** on **Oct 26, 2016** (revisions `#79`–`#80` at `Wed Oct 26 15:49:17` and `18:09:24 EDT 2016`; notation changed from `lpfsqfb` to `b(n)` by Joerg Arndt in `#82` at `Sun Nov 06 05:01:04 EST 2016`), originally listing exceptions `n = 3, 10, and 171`.
- **Jun 15, 2026 correction:** **Jaideep Padhi** (revisions `#97`–`#101` on `Mon Jun 15 2026`) added `n = 2` (noting `b(2)^2 = 4 >= 2*2 = 4` holds while `a(2) = 6 != 2 + 2 = 4`). Formatted by Alois P. Heinz (`#102`–`#103`, `Jun 15 2026`) and finalized by Sean A. Irvine (`#104`–`#106`, `Fri Jun 19 00:16:16 EDT 2026`), where the inline attribution reads `[Corrected by Jaideep Padhi_, Jun 15 2026]`. `TARGET.md` and `PROOF.md` reproduce this exact text verbatim.

### 1.3 Definitions of `A007913` and `A006530` & `A006255` Values
- **`A007913`** (rev `213`, `2026-11-16T12:48:29-05:00`, **offset `1,2`**): *"Squarefree part of n: a(n) is the smallest positive number m such that n/m is a square."* First 10 terms: `1, 2, 3, 1, 5, 6, 7, 2, 1, 10` (confirming `A007913(k^2) = 1`, e.g., at `n = 1, 4, 9`).
- **`A006530`** (rev `248`, `2026-08-04T17:14:55-04:00`, **offset `1,2`**): *"Gpf(n): greatest prime dividing n, for n >= 2; a(1)=1."* First 10 terms: `1, 2, 3, 2, 5, 3, 7, 2, 3, 5` (confirming `A006530(1) = 1`).
- **`A006255` b-file (`b006255.txt`) values:** `1 1`, `2 6`, `3 8`, `10 18`, `171 195` (confirming `a(2)=6, a(3)=8, a(10)=18, a(171)=195`).

---

## 2. Deep Novelty Check (1992–2026)

| Source | Exact Queries | Results & Assessment |
|---|---|---|
| `watch/snapshots/**` (277 files) | `.venv/bin/python tools/novelty_grep.py A006255 Padhi "Graham's sequence" "171"` and `... "b(n)^2"` | `A006255`, `"Graham's sequence"`, `"b(n)^2"`: **0 matches**. `"171"` matched 27/63 files on unrelated issue/arXiv IDs. `"Padhi"` matched 4 lines across 3 files (`1337-solved-conjectures` & `jaideepsaipadhi/erdos-sums-almost-primes`) — unrelated to `A006255`. |
| arXiv API (`tools/arxiv_fetch.py`) | `all:A006255`; `all:Padhi AND all:Graham`; `all:"Graham's sequence"`; `all:"Ron Graham's sequence" OR all:"Graham's function"`; `all:"Bui" AND all:"Pratt" AND all:"Zaharescu" AND all:"Selfridge"` | `A006255` (0), `Padhi AND Graham` (0). `Graham's sequence` returns `2410.04728v2` (Kagey–Rajesh 2024). `Bui-Pratt-Zaharescu` returns `2211.12467v1` (*Math. Proc. Cambridge Philos. Soc.* 176 (2024), 309–323), which resolves Granville's ABC-conditional problem on the distribution of $t_n = a(n) - n$, not Padhi's threshold $b(n)^2 \ge 2n$. |
| Cached arXiv eprints | Inspected `tools/.arxiv_cache/eprint/2504.19196/main.tex` & `2410.04728/graham.tex` | **Adenwalla (2025, `2504.19196`)** proves $g_2(n)=2n \iff n \text{ prime } (>3), n=0, \text{ or } n=6$, studies $g_m(n)$, and in Sec. 4 quotes Erdős–Selfridge (1992, Problem 6655): $P(n) > \sqrt{2n}+1 \implies g_2(n)=n+P(n)$ and $P(n) \le \sqrt{2n}+1 \implies g_2(n) \le n + \frac{3}{4}(\sqrt{8n+1}+1)$ ($n \notin \{2,3,8,10,32\}$). **Kagey–Rajesh (2024, `2410.04728`)** proves $g(n)\le 2n$ ($n\ge 4$), bijectivity, and Wilson's conjecture $T(n)\neq 2$. Neither settles the $k=(p-1)/2$ boundary ($n=p(p-1)/2$, i.e. $\sqrt{2n} \le P(n) \le \sqrt{2n}+1$) nor mentions `171` or Padhi/Corneth's conjecture. |
| Zenodo API | `q=A006255`; `q="Graham's sequence"`; `q=Padhi Graham` | `A006255`: **0 hits**; `"Graham's sequence"`: **0 hits**; `Padhi Graham` (unquoted AND): 17,479 unrelated hits. |
| GitHub (`gh search`, read-only) | `gh search repos A006255`; `gh search issues A006255`; `gh search code "A006255"`; `gh search code "A006255" "Padhi"`; `gh search code "A006255" "Corneth"`; owner-scoped searches on `1337isnot1337`, `joaquimmj`, `the-omega-institute`, `mathesis-papers`; `gh search code "A006255" "trureturing"` | `repos` (0), `issues` (2 unrelated hash/ID matches), `code "A006255" "Padhi"` (0), `1337isnot1337`/`joaquimmj`/`the-omega-institute` (0). `A006255` code search (634 hits) shows only jOEIS, `peterkagey/math`, `OEIS-Spider`, `OpenishProblems`, and `mathesis-papers/kagey343881-powerproducts` (which treats `A343881` and cites `A006255` only in background). Note: `gh search code "A006255" "trureturing"` hit a 1-minute GitHub code-search rate limit (403) before retrying via `the-omega-institute` (0 hits) and `mathesis-papers` (only `kagey343881-powerproducts`). |
| Stack Exchange API (`mathoverflow`, `math`) | `q=A006255`; `q=171 Graham`; `q=Graham's sequence` | `A006255` (0 MO, 0 MSE), `171 Graham` (0 MO, 0 MSE), `Graham's sequence` (10 MO / 10 MSE unrelated or asking about $T(n)$ in MSE `#2076745`). |
| Web Search (`search_web`) | `"A006255" "Padhi" OR "171" OR "b(n)^2" OR "proved"`; `"Granville" "Selfridge" "Product of integers in an interval" "p(p-1)/2" OR "A006255"` | First query returns only the OEIS `A006255` conjecture statement. Second returns Granville–Selfridge (2001, *Electron. J. Combin.*) and general Graham sequence bounds; no proof of $n = p(p-1)/2$ or Padhi's conjecture found. |

**Novelty conclusion:** Clear across all checked sources (1992–2026).

---

## 3. Independent Computational Verification

### 3.1 Re-run of `check-check-1.py`
Command: `.venv/bin/python -u targets/oeis-A006255/notes/check-check-1.py 2>&1 ; echo "EXIT=$?"` (also ran without `-u`, exiting `0`; with `-u` captured full stdout):
```text
Lemma 1 (1<=n<=2000) & exact Graham a(n) vs OEIS A006255 data (1<=n<=70): OK
Lemma 2 (all 4045 pairs (p, k) for 5<=p<300): OK
Tables 1 & 2 (78 leaves, 1152/1152 U coverage, 10 uncovered primes, 10 witnesses): OK
Section 6 (exhaustive non-existence at n+b(n) and exact a(n) for {2, 3, 10, 171}): OK
PASS
```

### 3.2 Independent In-Memory Verification of `PROOF.md` (Tables 1 & 2, Lemmas 4–5, Section 6)
All checks below were executed directly via in-memory `.venv/bin/python -c` scripts (no scratch scripts saved):

1. **(a) All 78 leaves (39 canonical + 39 mirror) in `PROOF.md` Table 1:**
   - Verified Lemma 4(2) **verbatim** in integer arithmetic: for every edge $i \in \{0, \dots, k-1\}$ across all 78 leaves, with $c_i = b_i / a_i$ ($a_i \ge 1$, $\gcd(a_i, |b_i|) = 1$), checked $a_i a_{i+1} \mid 2(a_i m + b_i)(a_{i+1} m + b_{i+1})$ directly for $m = r$ and $m = D + r$. **All 78 leaves pass.**
   - Verified strict slope $\frac{1}{2} < s_i < \frac{3}{2}$, $\{c_i, c_{i+1}\} \neq \{0, 1\}$, $c_i \neq \frac{1}{2}$, pairwise distinctness of $c_0, \dots, c_{k-1}$, and $r' = (D - 1 - r) \bmod D$.
   - Verified `floor(b_lo) + 1` and `floor(b_hi) + 1` edge cases explicitly: across the 78 leaves there are **248** occurrences of negative `b_lo`, **137** exact-integer `b_lo`, **604** negative `b_hi`, and **137** exact-integer `b_hi`. In every case Python's `math.floor` (true $\lfloor x \rfloor$) gave the exact tight integer threshold $m_{\text{lo}}$ satisfying $(2s_i-1)m_{\text{lo}} + 2p_i > 0$ and $(2s_i-1)(m_{\text{lo}}-1) + 2p_i \le 0$ (and analogously for $b_{\text{hi}}$), and the recomputed $M_0, M_0'$ matched Table 1 identically (max $2350$ at $(840, 669)$).
   - Verified **every integer** $m \in [M_0, 5000]$ for every one of the 78 leaves:
     - $2m^2 + m < f_i(m) < 2m^2 + 3m + 1$ for all $i$;
     - $f_i(m) \neq 2m^2 + 2m$ for all $i$;
     - $|\{f_0(m), \dots, f_{k-1}(m)\}| = k$ (no collision $f_i(m) = f_j(m)$);
     - whenever $m \equiv r \pmod D$, every $f_i(m) \in \mathbb{Z}$ and $2\prod_{i=0}^{k-1} f_i(m)$ is an exact square.
   - Verified pairwise disjointness modulo $2520$ ($1476$ classes covered) and $U \subseteq \text{covered}$ ($1152/1152$ classes).
   - Verified Leaf #1 algebraic illustration ($f_0 = 8t(9t+1)$, $f_1 = 9t(8t+1)$, $f_2 = (8t+1)(9t+1)$) for $1 \le t < 20$.

2. **(b) All primes $p \in [2, 10000]$ for $n = p(p-1)/2$ and Table 2:**
   - Checked all **1225** primes $p \in [2, 10000] \setminus \{2, 3, 5, 19\}$: every single one has either $m = (p-1)/2 \ge M_0(\text{leaf})$ or $p \in \{7, 17, 43, 101, 103, 163, 257, 461, 1097, 3019\}$ (Table 2).
   - Checked all 10 rows of Table 2: $m = (p-1)/2$, $n = p(p-1)/2$, $n+p$, $S \subset (n, n+p)$ distinct, $n(n+p)\prod_{x\in S} x = \text{root}^2$, and `Leaf (D, r)` matches $m \equiv r \pmod D$ for all 9 primes $p > 7$.

3. **(c) Section 6 exact factorizations ($n \in \{2, 3, 10, 171\}$):**
   - Verified $b(2)=2$ ($2\cdot 3\cdot 6 = 6^2$), $b(3)=3$ ($3\cdot 6\cdot 8 = 12^2$), $b(10)=5$ ($10\cdot 12\cdot 15\cdot 18 = 180^2$), and $b(171)=19$ ($171=9\cdot 19$).
   - Verified all 14 Pass-1 factorizations in $\{172, \dots, 189\}$ (`172=4*43`, `173`, `174=6*29`, `177=3*59`, `178=2*89`, `179`, `181`, `182=2*7*13`, `183=3*61`, `184=8*23`, `185=5*37`, `186=6*31`, `187=11*17`, `188=4*47`), confirming each listed prime $> 11$ divides **only** that single element of $\{172, \dots, 189\}$.
   - Verified Pass-2: among survivors `{175, 176, 180, 189}`, prime `11` divides only `176 = 16 * 11`.
   - Verified remaining survivors: `175 = 5^2 * 7` ($v_2=0$), `180 = 2^2 * 3^2 * 5` ($v_2=2$), `189 = 3^3 * 7` ($v_2=0$).
   - Independently verified via GF(2) span over $\{172, \dots, 194\}$ that $a(171) = 195$ (with explicit witness $S = \{182, 189, 190\}$, $171 \cdot 182 \cdot 189 \cdot 190 \cdot 195 = 466830^2$).

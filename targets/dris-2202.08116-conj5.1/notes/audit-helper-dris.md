# Adversarial Audit Helper Report: `targets/dris-2202.08116-conj5.1/`

- **Helper:** `dris-audit-hlp` (for `@audit-2`)
- **Timestamp (UTC):** 2026-11-26T21:14:33Z
- **Target:** `targets/dris-2202.08116-conj5.1/` — Jose Arnaldo Bebita Dris, *"A new approach to odd perfect numbers via GCDs"*, `arXiv:2202.08116v1` [math.NT], Section 5, Conjecture 5.1 (`AsymptoticDensity2`): the set $A = \{m \ge 1 : \gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))\}$ has asymptotic density $0$.
- **Boundary Compliance:** Did NOT read `verify.py` or `notes/screen-*`; did NOT edit `TARGET.md` or `PROOF.md`; read-only queries only.

---

## Summary Verdict

**No prior proof found.** Live inspection of MathOverflow Q369441 (including Answer 369521 and all comments), all 59 MO questions and 515 MSE questions by Dris (2011–2026), Stack Exchange searches, arXiv, OpenAlex, Crossref, OEIS, and full-text inspection of key related analytic number theory papers (including Pollack 2011 & 2023 and Bordellès 2026) confirms that Conjecture 5.1 remains **unproved in the literature** (MO Q369441 / Answer 369521 gives only an unproved heuristic). Independent checker verification (`check-check-2.py`) passes cleanly.

---

## 1. Live Stack Exchange API Audit (MathOverflow & Math Stack Exchange)

All queries executed live against `https://api.stackexchange.com/2.3/` with `filter=withbody` and full pagination.

### 1.1 MathOverflow Answer `369521` and Full Thread `Q369441`

- **Question `369441`** ([link](https://mathoverflow.net/questions/369441/)): *"Is the asymptotic density of positive integers $n$ satisfying $\gcd(n, \sigma(n^2))=\gcd(n^2, \sigma(n^2))$ equal to zero?"*
  - Asked by Jose Arnaldo Bebita Dris (`user_id=10365`) on `2020-08-18` (`1597723984`), last activity `2020-08-19` (`1597802328`).
  - Notes computational check up to $100$ (all except $99$) and gives the elementary bounds $1 - \frac{2}{27}\cdot\frac{10}{121} = \frac{3247}{3267}$ (from $3^2 \cdot 11 \parallel n$) and $1 - \frac{2}{9} = \frac{7}{9}$ (from $3 \parallel n$ + $y, z \equiv 1 \pmod 3$). States *"The real open problem is whether the asymptotic density is $0$."*
- **Question comments (`1` total):**
  - `comment_id=932788` by Gerry Myerson (`2020-08-18`): points to OEIS `A065764` ($\sigma(n^2)$).
- **Answers (`1` total, `has_more=False`):**
  - **Answer `369521`** by Aaron Meyerowitz (`user_id=8008`), created `2020-08-18`, edited `2020-08-19`, accepted, score `2`.
  - **Exact content:** Observes that for prime $p \equiv 1 \pmod 6$, $x^2 + x + 1 \equiv 0 \pmod p$ has two solutions $0 < r < s < p-1$; if $p \parallel n$, then "with probability $1$" there are two distinct primes $x, y \equiv r \text{ or } s \pmod p$ with $x \parallel n, y \parallel n$, giving $p \parallel \gcd(n, \sigma(n^2))$ and $p^2 \parallel \gcd(n^2, \sigma(n^2))$. Computes local density $1 - \frac{p-1}{p^2} < 1 - \frac{1}{p+2}$ and concludes conditionally:
    > *"If we can argue that the chance that none of these events happen is asymptotically $\prod(1-\frac{p-1}{p^2})$ over the primes congruent to $1 \bmod 6,$ then that asymptotic density is $0.$"*
  - **Gap:** Explicitly conditional (*"If we can argue..."*); contains **no** finite truncation ($k$), **no** finite prime cutoff ($P$), **no** CRT independence / Chebyshev argument for the bad sets $B_i$ having density $0$, and **no** citations to Erdős, Pomerance, Pollack, or Luca.
- **Answer comments (`2` total):**
  - `comment_id=933031` by Dris (`2020-08-19`): points out typo in Meyerowitz's initial upper bound $1 - \frac{1}{p-1}$.
  - `comment_id=933033` by Meyerowitz (`2020-08-19`): acknowledges fixing it to $1 - \frac{1}{p+2}$ (*"The idea was, roughly $1 - \frac{1}{p}$"*).
- **No activity after `2020-08-19`.**

### 1.2 All Questions by Dris on MO (`users/10365`, 59 questions) and MSE (`users/28816`, 515 questions)

Filtered all 59 MO questions and 515 MSE questions (through 2026) for `sigma(n^2)`, `sigma(m^2)`, `gcd(n,`, `gcd(m,`, `density`, `asymptotic`, `369441`, `3629818`. Relevant threads inspected in full (questions, answers, and all comments):

- **MSE Q3629818** (`2020-04-17`): *"What is the asymptotic density of positive integers $n$ satisfying $\gcd(n,\sigma(n^2))=\gcd(n^2,\sigma(n^2))$?"*
  - Only 2 answers, both by Dris: `3629863` (Pari/GP counts up to $10^6$: $10, 99, 974, 9561, 93845, 923464$) and `3780560` (communicated by a referee: density $< 7/9$, *"The real open problem is whether the asymptotic density is $0$."*). No proof of density $0$.
- **MSE Q3628078** (`2020-04-16`): *"When does $\gcd(m,\sigma(m^2))$ equal $\gcd(m^2,\sigma(m^2))$? What are the exceptions?"*
  - 1 answer (`3628448` by Peter): Pari/GP statistics on fraction of exceptions divisible by $7$ for $\omega(m)=2,3$ up to $10^7$. No density-$0$ proof.
- **MO Q460092** (`2023-12-10`): *"On a GCD approach to odd perfect numbers"*. Accepted answer (`461502` by Pace Nielsen) rewrites $G, H, I$ in terms of $p$-adic exponents $e_i, f_i$ and remarks on spoof odd perfect numbers; does not address asymptotic density or Conjecture 5.1.
- **Sibling GCD threads inspected** (`MSE 3690494`, `4259745`, `4341573`, `4341685`, `4540847`, `4677771`, `3017227`; `MO 378402`, `403896`, `404849`, `457769`): all study odd-perfect-number conditions ($n \mid \sigma(n^2)$, $\sigma(q^k)/2$ squarefree, $\gcd(n^2, \sigma(n^2)) > \sigma(n)$, etc.), not the density of $A$.
- **No follow-up question by Dris on MO or MSE (2020–2026) proves Conjecture 5.1.**

### 1.3 Broad Stack Exchange Searches

Ran `search/advanced` on both `mathoverflow` and `math` for:
- `q="sigma(n^2) gcd"`, `q="sigma(m^2) gcd"`, `q="sigma(m^2) density"`, `q="sigma(n^2) density"` (0 relevant hits)
- `body="sigma(n^2)"` (MO: 43 hits), `body="sigma(m^2)"` (MO: 10 hits), `q="gcd sigma asymptotic density"` (MO: 2 hits: `Q369441` and `Q57436`)
- `body="gcd(n, \sigma(n^2))"` (MSE: 10 hits), `body="gcd(m, \sigma(m^2))"` (MSE: 4 hits), `q="gcd(n, sigma(n)) density"` (MSE: 5 hits, including `Q3629818` and `Q3017227`)

No Stack Exchange thread proves Conjecture 5.1.

---

## 2. Deep Literature Check (1950–2026)

### 2.1 Dris's Paper & Later Works (2022–2026)

- **arXiv:** `tools/arxiv_fetch.py abs 2202.08116` confirms `2202.08116v1` (`2022-02-10`, no v2) with `journal_ref`: *Octogon Mathematical Magazine*, Vol. 30, No. 2, October 2022, pp. 883–895. `tools/arxiv_fetch.py query 'au:Dris AND all:perfect'` returned 21 preprints; `2202.08116v1` is the latest.
- **OpenAlex & Crossref:**
  - `2202.08116` (`https://openalex.org/W4226357996`) has `cited_by_count: 0` (0 citing works).
  - All 27 works under Dris's OpenAlex author ID (`A5054486850`) were checked; the latest publication is a 2023 *NNTDM* corrigendum (`10.7546/nntdm.2023.29.1.181-184`, on modular considerations, unrelated to Conjecture 5.1).
  - Web and *NNTDM* searches for `"Jose Arnaldo Bebita Dris" 2023..2026`, `"Octogon Mathematical Magazine" "883" "895" "Dris"`, and coauthors `"Dagal"` / `"San Diego"` show no subsequent paper proving Conjecture 5.1.

### 2.2 Analytic / Elementary Number Theory Literature on $\gcd(n, \sigma(n))$, $\sigma(m^2)$, and $p^k \mid \sigma(n)$

Checked arXiv, OpenAlex, Crossref, and web search across Paul Pollack, Carl Pomerance, Florian Luca, Kevin Ford, Paul Erdős, Imre Kátai, M. V. Subbarao, Robert E. Dressler, Andrew Granville, Olivier Bordellès, Kevin Broughan, Daniel Delbourgo, Jeffrey/Matthew Ward, Stefan Wehmeier, Pace Nielsen, Pascal Ochem, and Michaël Rao:

- **Paul Pollack (2011), *"On the greatest common divisor of a number and its sum of divisors"*, Michigan Math. J. 60, 199–214** (inspected full 15-page PDF from `pollack-math.net/combined3.pdf`):
  - Studies $G(x, A) := \#\{n \le x : \gcd(n, \sigma(n)) > A\}$ and $\sum_{n \le x} \gcd(n, \sigma(n))$ (correcting Erdős 1956), using Pomerance (1977) Lemma 3.3 ($d \nmid \sigma(n)$ bound $O(x/(\log x)^{1/\varphi(d)})$) and Wirsing (1959). Does **not** treat $\sigma(m^2)$ or $\gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))$.
- **Paul Pollack (2023), *"On the Greatest Common Divisor of a Number and Its Sum of Divisors, II"*, in *Number Theory in Memory of Eduard Wirsing*, Springer** (inspected full 12-page PDF from `pollack-math.net/gcdnsigmasequel.pdf`):
  - Studies $E(x, y) := \#\{n \le x : \gcd(n, \sigma(n)) > y\}$ for intermediate $y$ and $\#\{n \le x : \gcd(n, \sigma(n)) = m\} \sim e^{-\gamma} x / (m \log\log\log x)$ for $m \le (\log\log x)^{1/4}$. Does **not** treat $\sigma(m^2)$ or $\gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))$.
- **Kátai & Subbarao (2006) and Erdős, Luca & Pomerance (2008)** (*"On the proportion of numbers coprime to a given integer"*, CRM Proc. Lecture Notes 46, pp. 47–64; summarized as Theorem A in Pollack 2011):
  - Show that for almost all $n$ (outside a density-0 set), $\gcd(n, \sigma(n))$ equals the largest divisor of $n$ supported on primes $\le \log\log n$ (and for $\gcd(n, \sigma(n)) > (\log\log n)^u$, asymptotic density is $e^{-\gamma}\int_u^\infty \rho(t)\,dt$). This concerns $\sigma(n)$, not $\sigma(m^2)$, and even the analogous statement for $\sigma(n)$ does not state or prove Conjecture 5.1 (in fact, for $\gcd(n, \sigma(n)) = \gcd(n^2, \sigma(n))$, the condition is $v_p(\sigma(n)) \le v_p(n)$ for all $p \mid n$, which fails once small primes $p \parallel n$ divide $\sigma(n)$ to power $\ge 2$).
- **Pollack & Pomerance (2016)** (*"Some problems of Erdős on the sum-of-divisors function"*, Trans. AMS Ser. B): treats abundant/deficient reversals, nonaliquot numbers, and friendly $k$-sets; not Conjecture 5.1.
- **Erdős (1956, 1959, 1973), Dressler (1974), Luca (2007):**
  - Dressler (*On a theorem of Niven*, Canad. Math. Bull. 17 (1974), 109–110) and Luca (*On the densities of some subsets of integers*, Missouri J. Math. Sci. 19(3) (2007), 167–170) prove $\{n : \gcd(n, \sigma_j(n)) \le k\}$ has density $0$ (in particular Duffinian/coprime numbers $\{n : \gcd(n, \sigma(n)) = 1\}$ have density $0$). Note that $m \in A$ does **not** bound $\gcd(m, \sigma(m^2))$: e.g. $p^2 \in A$ has $\gcd(p^2, \sigma(p^4)) = 1$, while if $m \in A$ has $p \mid m$ with $v_p(\sigma(m^2)) \le v_p(m)$, then $\gcd(m, \sigma(m^2))$ can be arbitrarily large.
- **Olivier Bordellès (2026), *"A note on the $q$-adic valuation of $\sigma_k(n)$"*, `arXiv:2605.17872v2`** (inspected `Valuation_sigma_k.tex`): gives an exact formula and pointwise upper bound on $v_q(\sigma_k(n))$; nothing on asymptotic density or Conjecture 5.1.
- **Broughan, Delbourgo & Zhou (2013), Ward (2008), Ochem & Rao (2012), Nielsen:** study odd perfect number indices $i(q) = \gcd(n^2, \sigma(n^2))$ and bounds on hypothetical OPNs, not the asymptotic density of $\{m \ge 1 : \gcd(m, \sigma(m^2)) = \gcd(m^2, \sigma(m^2))\}$.

### 2.3 OEIS Check

Queried `https://oeis.org/search?q=...&fmt=json`:
- `"10,99,974,9561"` -> 0 results.
- `"99,154,198,273,322,396,399"` -> 0 results.
- `"154,198,273,322,396,399,462,469"` -> 0 results.
- `"gcd(m, sigma(m^2))"` -> 0 results; `"2202.08116"` -> 0 results.
- Inspected related sequences `A356448` (even $k$ with $\gcd(k, \sigma(k^2)) = 1$), `A247222` ($n = \gcd(n^2, \sigma(n^2))$), `A014567` ($\gcd(k, \sigma(k)) = 1$, cites Dressler 1974 and Luca 2007), `A232354` ($k \mid \sigma(k^2)$, links to `arXiv:2202.08116`), and `A322154` ($\gcd(k^2, \sigma(k^2)) > \sigma(k)$). None contains $A$, $\mathbb{Z}_{\ge 1} \setminus A$, or any claim/reference that Conjecture 5.1 is proved.

---

## 3. Re-run of Independent Checker Verifier (`check-check-2.py`)

Command executed:
```bash
.venv/bin/python targets/dris-2202.08116-conj5.1/notes/check-check-2.py
```

Exit code: `0`. Raw output:
```text
Primary-source table counts verified up to 10000: {10: 10, 100: 99, 1000: 974, 10000: 9561}
Lemma 1 verified on m <= 10000 (137 excluded integers all satisfy m not in A)
Lemma 2 exact period check k=1 (M_1=49): d(E_1) = 43/49
Lemma 2 exact period check k=2 (M_2=8281): d(E_2) = 6751/8281
Lemma 3 exact CRT check on Q_7(23) (N_P=256036): E[f]=95817/256036, Var(f)=19874323827/65554433296, d(B~)=61911/64009
Lemma 3 Chebyshev bound verified in exact Fraction DP (13 primes, E=108280528334352935238267890681/92568222856376731590410384100, P(<=1) <= Var/(E-1)^2 <= E/(E-1)^2)
PASS (all exact checks passed in 0.914s)
```

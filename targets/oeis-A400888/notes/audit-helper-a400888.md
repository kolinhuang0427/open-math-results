# Audit Helper Report: OEIS A400888 (`audit-helper-a400888`)

- **Date (UTC):** 2026-11-27T04:17Z
- **Role:** Adversarial audit helper (`@a400888-audit-hlp`) for `@audit-3`
- **Target:** `targets/oeis-A400888/` (OEIS `A400888` surjectivity conjecture)
- **Isolation compliance:** Did NOT read `verify.py`, `notes/screen-*`, `notes/attack-*`, or `notes/triage-brief.md`; did NOT edit `TARGET.md` or `PROOF.md`. Checked `ls -la targets/oeis-A400888/`: contains `PROOF.md`, `TARGET.md`, `notes/`, `verify.py` (no `CONTESTED.md`).

---

## 1. Live OEIS Primary-Source Verification

Fetched live JSON from `https://oeis.org/search?q=id:<ID>&fmt=json` (`User-Agent: curl/8.7.1`, timeout 15s) on 2026-11-27T04:06Z:

| Sequence | Revision | Last Modified (`time`) | Offset | Status vs `PROOF.md` |
|---|---|---|---|---|
| `A400888` | 16 | `2026-10-15T16:25:59-04:00` | `0,1` | Exact match; conjecture still open (`COMMENT`) |
| `A000361` | 53 | `2026-11-23T16:58:18-05:00` | `0,3` | Exact match |
| `A000360` | 154 | `2026-11-04T22:26:09-05:00` | `0,7` | Exact match |
| `A284556` | 28 | `2026-10-28T00:11:51-04:00` | `0,6` | Exact match |
| `A002487` | 719 | `2026-11-13T10:02:49-05:00` | `0,4` | Exact match |

Also checked `A400889` (`rev 12`, `2026-10-15T16:37:53-04:00`): *"Least k such that n divides A400888(k)"* — addresses divisibility only, not surjectivity.

### Verbatim Check of `A400888` (rev 16)
- **Author:** `_M. Jeremie Lafitte (Levitas)_, Oct 08 2026`
- **Name:** `Contents of the quarter-turn corrected Stern vectors associated with the column words of the Gosper-Lafitte triangle.`
- **Comment (verbatim excerpts):**
  - `V(n)`: *"Let V(n) be the filled-empty word in column n of the fractal set described in A000360, considered from the narrow top downward, with filled=1 and empty=0. V(n) is A000361's W(n) read in reverse order. Let f_n=A000360(n) and e_n=A284556(n+1) be its numbers of 1s and 0s. Starting with (p,q)=(1,1), read V(n), replacing (p,q) by (p+q,q) after a 1 and by (p,p+q) after a 0. Let (p_n, q_n) be the resulting Stern vector."*
  - `u_n` & `a(n)`: *"With v_n=(p_n,q_n)^T, c_n=(f_n,e_n)^T, J={{0,-1},{1,0}}, and u_n=v_n + J*c_n, we have a(n) = max {m >= 1 : u_n == (0,0)^T (mod m)}."* (Note $v_n + J c_n = (p_n - e_n,\, q_n + f_n)^T$.)
  - Conjecture: *"Every positive integer divides some term of this unbounded sequence. Every positive even integer occurs infinitely often as a term. It is conjectured that the sequence is surjective onto the positive integers."*
  - **Confirmed:** `A400888` has NOT been updated or marked proved on OEIS.
- **Formula:** `a(n) = gcd(p_n - e_n, q_n + f_n), with (p_n, q_n) and (f_n, e_n) as defined above.`
- **PARI/GP `PROGRAM`:**
  - `f(v, c, h=0) = [2*(x + h) + c - (2*c + 1)*(x%2) | x <- v];`
  - `w(n) = {my(m = n\2); if(n < 1, if(n, [], [1]), if(n%2, f(w(m), m%3 != 2, 1), concat(f(w(m), m%3 != 0), f(w(m - 1), m%3 != 2))))};`
  - `a(n) = {my(v = vecsort(w(n),,4), p = 1, q = 1, ones, zeros); ones = sum(i = 1, #v, v[i]%2); zeros = #v - ones; for(i = 1, #v, if(v[i]%2, p += q, q += p)); gcd(p - zeros, q + ones)};`
  - Note: PARI `vecsort(..., 4)` sorts in descending order (`4` = descending). Matches `PROOF.md` lines 12–16 verbatim.

### Verbatim Check of `A000361` (rev 53) & `PROOF.md` Lines 12–18
- **Comment:** *"Put p=A002487(n), q=A002487(n+1), and t=p mod q, and let V(n)={v_0,v_1,...,v_{q-1}} be the word of column n read from top to bottom, which is W(n) in reverse order."*
- **Formula:** *"Using the notation above, for 0<=j<q, v_j=(((j*p-1) mod q)+1-p) mod 2. Hence a(n)=Sum_{j=0..q-1} v_j*2^(q-1-j). - _M. Jeremie Lafitte (Levitas)_, Oct 21 2026"*
- **PARI Program:** `a(n) = { my(p = s(n), q = s(n + 1)); fromdigits([((j*p - 1)%q + 1 - p)%2 | j <- [0..q - 1]], 2)};`
- **Comparison with `PROOF.md` lines 12–18:** Exact verbatim match, including $0$-based indexing $0 \le j < q_0$ for $V(n) = (v_0, \dots, v_{q_0-1})$ with $p_0 = \mathrm{A002487}(n)$ and $q_0 = \mathrm{A002487}(n+1)$. Independently verified in Python that PARI `w(n)` sorted descending mod 2 equals `v_j` for all $0 \le n \le 99$.

---

## 2. Deep Novelty Check (through 2026-11-27)

- **Local watch snapshots (`tools/novelty_grep.py`):**
  - Command: `.venv/bin/python tools/novelty_grep.py A400888 400888 "Gosper-Lafitte" "Lafitte" "Levitas" A000361`
  - Result: `# 0 lines across 0/470 files in 1.15s` — **0 hits**.
- **arXiv (`tools/arxiv_fetch.py`):**
  - Query: `all:"A400888" OR all:"Gosper-Lafitte" OR all:"quarter-turn corrected Stern" OR all:"Jeremie Lafitte"` (`--max-results 20`)
  - Result: `total_results: 0`, `entries: []`.
- **Zenodo API (`https://zenodo.org/api/records`):**
  - Queries `"A400888"`, `"Gosper-Lafitte"`, `"quarter-turn corrected Stern"`, `"Jeremie Lafitte"`, `"A000361"`: **0 hits** on all five.
- **Crossref API (`https://api.crossref.org/works`) & OpenAlex API (`https://api.openalex.org/works`):**
  - `A400888`: 0 results in Crossref and 0 in OpenAlex.
  - `"Gosper-Lafitte"` / `"Jeremie Lafitte"` / `"quarter-turn corrected Stern"` / `"A000361"`: only unrelated surnames/places/medical DOIs/climate/quantum papers; **0 relevant hits**.
- **Web search (`search_web`):**
  - Query `"A400888" OR "Gosper-Lafitte" OR "quarter-turn corrected Stern" OR "Jeremie Lafitte"` returns only OEIS pages (`A400888`, `A000360`, `A000361`) and general background on the Gosper–Lafitte triangle; **no proof or resolution of `A400888` surjectivity**.
- **Competing GitHub repositories (read-only `gh api` & `gh search`):**
  - Checked all 45 repos under `the-omega-institute/*` (including `trureturing`, `trureturing-pages`, `trureturing-books`, `trureturing-experiments`, `trureturing-source-theories`, `trureturing-tools`, `trureturing-live`, `automath`, `newmath`, `riemann-hypothesis`, etc.), plus `1337isnot1337/solved-conjectures` (`CONTENTS.md` 547 lines, `HISTORY.md` 2900 lines, 500 issues), `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures`, and `openai/math` (`CONTENTS.md` 9262 lines, `history.md` 85 lines).
  - Near-miss false positives inspected and excluded:
    - `1337isnot1337/solved-conjectures/HISTORY.md`: Dilcher–Kidwai–Tomkins's Stern-polynomial zero-location conjecture (`results/stern-half-plane/`), unrelated to `A400888`.
    - `the-omega-institute/trureturing-books`: `books/quantum-geometry/figures/ch05-quarter-turns.py` and `ch32-quarter-turns.py` (quantum geometry, unrelated).
    - `the-omega-institute/trureturing#34443`: `math(chordal): prove strict local sharpness for round quaternion K4` (unrelated).
    - `aliromman/math#84`: Presutti–Stromquist packing-density optimizer (`quarter-turn` substring only).
    - Global `gh search code`/`issues`: `archmageirvine/joeis` (`A400888.java` / `A400889.java`, jOEIS sequence implementation only); other hits are hex constants/domain names/software issues.
  - Note: global `gh search code` across the 14-repo batch hit GitHub's secondary code-search rate limit (`HTTP 403`), so coverage of large truncated repos (`trureturing`, `atlas-lean`, `integer-mult-bounds`, `openai/math`) relied on REST tree/directory listings, `CONTENTS.md`/`history.md`, and `gh search issues` (all `0` hits).
  - **Conclusion:** Novelty check **CLEAN** — no prior proof or resolution of `A400888` surjectivity found anywhere.

---

## 3. Independent Computation & Citation Check

### Execution of `check-check-2.py`
Command: `/usr/bin/time -p .venv/bin/python -u targets/oeis-A400888/notes/check-check-2.py`
- **Exit code:** `0`
- **Runtime:** `real 0.13`, `user 0.09`, `sys 0.01` (internal reported `0.081s`)
- **Raw output:**
```text
OEIS A400888 rev 16 (96 DATA terms == PARI w(n) == A000361) & Lemma 1: PASS
Lemmas 2 & 3 (matrix eval, quadratic form, Bezout, r=1..100 != 27 mod 30): PASS
Lemmas 4, 5 & 6 (parity, C_m(r) norm bound, d_q order, >=5 exact prime witnesses for r<=147): PASS
PASS (all checks passed in 0.081s)
```

### Literature Verification: Montgomery–Vaughan (1973), Theorem 2
- **Reference:** H. L. Montgomery and R. C. Vaughan, *"The large sieve"*, *Mathematika* **20** (1973), 119–134.
- **Statement checked:** Theorem 2 (Brun–Titchmarsh inequality) states that for all real $x \ge 0$, $y > q \ge 1$, and integers $a$ with $\gcd(a, q) = 1$,
  $$\pi(x + y; q, a) - \pi(x; q, a) < \frac{2y}{\varphi(q) \log(y/q)}.$$
  Setting $x = 0$ and replacing $(y, q)$ with $(X, M_q)$ gives $\pi(X; M_q, a_q) < \frac{2X}{\varphi(M_q)\log(X/M_q)}$ unconditionally for **all** $1 \le M_q < X$ and $\gcd(a_q, M_q) = 1$, with **no** hidden threshold $X/M_q \ge C$ or $o(1)$ error term.
- **Application in `PROOF.md` Lemma 6 Step 4 Case 1:** Here $X \ge \max(6, (rW)^4)$ and $q d_q \le X^{1/2}$, so $M_q = r W q d_q \le X^{1/4} X^{1/2} = X^{3/4} < X$ (strictly satisfying $1 \le M_q < X$), and $\log(X/M_q) \ge \frac{1}{4}\log X > 0$, so the bound $\frac{8X}{\varphi(rW)\varphi(qd_q)\log X}$ is completely rigorous.

### Concrete Verification of Lemma 6 Step 4 Case 1 Arithmetic
Verified directly in Python for $(r, Y) = (3, 50)$ (threshold $r(r^2+4)=39$), $(9, 800)$ (threshold $765$), and $(27, 20000)$ (threshold $19791$; note $Y = 100$ is below $r(r^2+4)=19791$ for $r=27$, so a valid Step 3 choice of $Y$ requires $Y > 19791$):
- $u_0 \in \{0, \dots, W-1\}$ satisfies $u_0 \equiv 0 \pmod 2$, $u_0 \equiv 2 \pmod 3$, and $u_0 \equiv 0 \pmod{\ell}$ for $5 \le \ell \le Y$. Because $u_0 \equiv 2 \pmod 3$, $u_0 \ge 2 > 0$, so $r u_0 - 1 \in [2r - 1, rW - 1]$ is strictly positive and $a_0 = (r u_0 - 1) \bmod (rW) = r u_0 - 1$ with $\gcd(a_0, rW) = 1$.
- For the first 5 primes $q > Y$ with odd $d_q$ and $\gcd(q d_q, rW) = 1$ (note: primes $q > Y$ with $\gcd(d_q, rW) > 1$ are properly excluded by $\gcd(q d_q, rW) = 1$ in Step 4, since $\gcd(t, rW) = 1$ forces $\gcd(q d_q, rW) = 1$ whenever $q d_q \mid t$):
  - $r=3, Y=50$: tested $q \in \{107, 179, 263, 347, 367\}$ ($d_q \in \{53, 89, 131, 173, 61\}$).
  - $r=9, Y=800$: tested $q \in \{1619, 1907, 2039, 2063, 2099\}$ ($d_q \in \{809, 953, 1019, 1031, 1049\}$).
  - $r=27, Y=20000$: tested $q \in \{40127, 40499, 40823, 40883, 41507\}$ ($d_q \in \{20063, 20249, 20411, 20441, 20753\}$).
  - In all 15 concrete cases: $\gcd(a_q, M_q) = 1$, $(2 a_q + r + 2) \equiv 0 \pmod{q d_q}$, $a_q \equiv a_0 \pmod{rW}$, and $t_{\mathrm{cand}} = (2 a_q + r + 2)/r$ satisfies $q d_q \mid t_{\mathrm{cand}}$, $t_{\mathrm{cand}} \equiv 2 \pmod 3$, and $\gcd(t_{\mathrm{cand}}, rW) = 1$.

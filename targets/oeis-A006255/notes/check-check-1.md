# Independent Check Report: `oeis-A006255` (`check-1`)

- **Checked at (UTC):** `2026-11-26T22:20:10Z`
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity and independent exact verification of all lemmas, all 78 covering-tree leaves, all 10 finite witnesses, and all 4 exceptions)

## 1. Primary-Source Fidelity Check

- **Primary sources fetched:**
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A006255&fmt=json`), revision `106` (`2026-06-19T00:16:16-04:00`).
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A007913&fmt=json`, rev `213`) and `A006530` (rev `248`).
- **Exact fields checked in `A006255`:**
  - `name`: *"R. L. Graham's sequence: a(n) = smallest m for which there is a sequence n = b_1 < b_2 < ... < b_t = m such that b_1*b_2*...*b_t is a perfect square."* (`offset: "1,2"`)
  - `comment`: *"Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"*
- **Word-for-word comparison against `TARGET.md` and `PROOF.md`:**
  - Exact definitions of `a(n)`, `A007913` (squarefree part), `A006530` (greatest prime factor with `a(1) = 1`), threshold `b(n)^2 >= 2*n`, conclusion `a(n) = n + b(n)`, and exceptions `{2, 3, 10, 171}` match verbatim. Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from live OEIS definitions and the lemmas/tables in `PROOF.md`, without reading `verify.py` or any file in `notes/`.
- **Verifier script:** `targets/oeis-A006255/notes/check-check-1.py` (exact integer and `fractions.Fraction` arithmetic, `math.isqrt`, GF(2) parity linear algebra, and exhaustive subset enumeration).
- **Verified claims & lemmas:**
  1. **Lemma 1 & OEIS `A006255` data:** Checked Lemma 1 structural properties ($p = b(n)$ prime, $p = \mathrm{gpf}(n)$, $n = kp$, $1 \le k \le \lfloor p/2 \rfloor$, $p \nmid k$) for all $1 \le n \le 2{,}000$; independently computed exact Graham sequence $a(n)$ via GF(2) prime-parity linear algebra and matched all 70 published OEIS `data` values ($1 \le n \le 70$).
  2. **Lemma 2 (Granville–Selfridge non-boundary regime):** Checked all $4{,}045$ pairs $(p, k)$ with $5 \le p < 300$ prime and $1 \le k \le (p-3)/2$ (including coincidence cases $m = 2k$ and $m = 2k+1$), verifying $S \subset (kp, (k+1)p)$ and $k(k+1)\prod_{x\in S} x = \square$.
  3. **Lemmas 4–5 & Table 1 (78-leaf covering tree mod $2520$):** Parsed all 39 canonical half-leaves from `PROOF.md` and generated their 39 mirror leaves (`r' = (D-1-r) mod D`, `c_i' = 1 - c_i`). Verified every hypothesis of Lemma 4 (odd $k \ge 3$, distinct $c_i \in \mathbb{Q} \setminus \{1/2\}$, strict slope $(1/2, 3/2)$, $\{c_i, c_{i+1}\} \neq \{0, 1\}$, congruence integrality at $m = r$ and $m = D+r$), independently recomputed all 78 thresholds $M_0, M_0'$ (matching Table 1 identically, max $2350$), checked the first 5 integers $m \ge M_0$ in each leaf class, verified pairwise disjointness modulo $2520$ (total $1{,}476$ classes), and confirmed 100% coverage of all $1{,}152$ classes in $U = \{m \in [0, 2519] : \gcd(2m+1, 210) = 1\}$.
  4. **Table 2 (Uncovered primes & finite witnesses):** Exhaustively checked all primes $p = 2m+1 > 7$ with $m < 3000$ against their covering leaf threshold, confirming the uncovered primes with $m < M_0(\text{leaf})$ are precisely $\{17, 19, 43, 101, 103, 163, 257, 461, 1097, 3019\}$. Verified `n*(n+p)*prod(S) == root^2` and $S \subset (n, n+p)$ for all 10 non-exception witnesses in Table 2 ($p \in \{7, 17, 43, 101, 103, 163, 257, 461, 1097, 3019\}$).
  5. **Section 6 (Exceptions $n \in \{2, 3, 10, 171\}$):** Exhaustively checked all $2^{p-1}$ subsets $S \subseteq (n, n+b(n))$ for $n \in \{2, 3, 10, 171\}$ to verify none yields $k(k+1)\cdot\square$, and verified exact values $a(2)=6, a(3)=8, a(10)=18, a(171)=195$.

### Command & Raw Output

Command:
```bash
.venv/bin/python targets/oeis-A006255/notes/check-check-1.py
```

Raw output:
```text
Lemma 1 (1<=n<=2000) & exact Graham a(n) vs OEIS A006255 data (1<=n<=70): OK
Lemma 2 (all 4045 pairs (p, k) for 5<=p<300): OK
Tables 1 & 2 (78 leaves, 1152/1152 U coverage, 10 uncovered primes, 10 witnesses): OK
Section 6 (exhaustive non-existence at n+b(n) and exact a(n) for {2, 3, 10, 171}): OK
PASS
```

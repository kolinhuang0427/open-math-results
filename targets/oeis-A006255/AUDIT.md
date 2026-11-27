# Adversarial Audit Report: `oeis-A006255`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T22:58Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Independent Verifier:** `targets/oeis-A006255/notes/check-check-1.py` (report: `targets/oeis-A006255/notes/check-check-1.md`)

---

## 1. Isolation & Materials Inspected

In accordance with `CHARTER.md`, this audit was conducted without reading `verify.py`, `notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, `notes/helper-*`, `notes/build_covering.py`, or `notes/covering-*`. Inspected materials:
1. Primary sources: Live OEIS JSON and history for `A006255` (rev. 106, `2026-06-19`), `A007913` (rev. 213), `A006530` (rev. 248), and `b006255.txt` (extracted in `notes/audit-helper-a006255.md`).
2. `targets/oeis-A006255/TARGET.md`.
3. `targets/oeis-A006255/PROOF.md`.
4. `targets/oeis-A006255/notes/check-check-1.md` and `targets/oeis-A006255/notes/check-check-1.py`.
5. Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and independent adversarial literature/verification notes (`notes/audit-helper-a006255.md`, produced by Flash helper `a006255-audit-hlp`).

---

## 2. Primary-Source Fidelity Audit

Verified directly against live OEIS **A006255** (rev. 106, `2026-06-19`, offset `1,2`), **A007913** (rev. 213, offset `1,2`), and **A006530** (rev. 248, offset `1,2`):
- **Verbatim Conjecture (Comments section of `A006255`):**
  > `"Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"`
  *(Revision history confirms David A. Corneth originally posted the conjecture on Oct 26, 2016 with exceptions `{3, 10, 171}`, and Jaideep Padhi corrected it on Jun 15, 2026 to add `n = 2`.)*
- **Definitions Verified:** `a(n)` is R. L. Graham's sequence ($a(k^2) = k^2$ with $t=1$); `A007913(n)` is the squarefree part of $n$ (`A007913(k^2) = 1`); `A006530(k)` is the greatest prime factor of $k$ for $k \ge 2$ with `A006530(1) = 1`.
- **Fidelity Verdict:** Character-for-character match across `TARGET.md`, `PROOF.md`, and `notes/check-check-1.py`. Zero quantifier, hypothesis, edge-case, or definition drift.

---

## 3. Adversarial Line-by-Line Proof Audit

Audited every lemma, algebraic step, boundary condition, covering-tree leaf, finite witness, and exception proof in `PROOF.md`:

1. **Lemma 1 (Prime-factor structure and lower bound):**
   - If $n = r^2$, then $b(n) = \mathrm{A006530}(1) = 1$, contradicting $b(n)^2 \ge 2n \ge 2$.
   - Thus $p = b(n)$ is prime with $v_p(n) \ge 1$ odd; $v_p(n) \ge 3$ gives $2n \ge 2p^3 > p^2$, and any prime $q > p$ dividing $n$ must have $v_q(n) \ge 2$ (as $q \nmid \mathrm{A007913}(n)$), giving $2n \ge 2pq^2 > 2p^3 > p^2$. Hence $v_p(n) = 1$, $p = \mathrm{gpf}(n)$, and $n = kp$ with $1 \le k \le \lfloor p/2 \rfloor$ and $p \nmid k$.
   - Parity of $v_p$ forces $a(n) \ge (k+1)p = n + p$; since no integer in $(kp, (k+1)p)$ is divisible by $p$ and $kp \cdot (k+1)p = p^2 k(k+1)$, equality $a(n) = (k+1)p$ holds iff some $S \subseteq (kp, (k+1)p) \cap \mathbb{Z}$ satisfies $\prod_{x \in S} x = k(k+1) \cdot \square$ (valid even at $p = 2, k = 1$ where $p \mid (k+1)$ because $p^2$ is already a square). **Airtight.**

2. **Lemma 2 (Non-boundary regime $1 \le k \le (p-3)/2$, self-contained Granville–Selfridge Cor. 1):**
   - For odd prime $p = 2m + 1 \ge 5$ and $1 \le k \le m - 1$: checked all four offsets $k, m-k \in [1, m-1]$ and $2m-k, m+k+1 \in [m+1, 2m]$ inside $(0, p)$, giving disjoint pairs $\{x_1, x_2\} \cap \{x_3, x_4\} = \emptyset$ and product $x_1 x_2 x_3 x_4 = k(k+1)(2m(m+1)(2k+1))^2$.
   - Checked both coincidence cases: $x_1 = x_2 \iff m = 2k$ (where $S = \{x_4\} = \{4k(k+1)\}$ works) and $x_3 = x_4 \iff m = 2k+1$ (where $S = \{x_1\} = \{4k(k+1)\}$ works). **Airtight.**

3. **Lemmas 3, 4, and 5 (Boundary $n = p(p-1)/2$, Polynomial Odd-Cycle Lemma, Mirror Symmetry):**
   - **Lemma 3:** $x_0 = 2m(m+1) \in (2m^2+m, 2m^2+3m+1)$ satisfies $n x_0 (n+p) = 2(m(m+1)(2m+1))^2$, reducing $a(n) = n+p$ to finding $S \subseteq I(m)$ with $\prod S = 2 \cdot \square$. **Airtight.**
   - **Lemma 4:**
     - *Integrality:* For $m = Dt + r$, $P_i(t) = 2(a_i(Dt+r)+b_i)(a_{i+1}(Dt+r)+b_{i+1})$ has quadratic coefficient $2a_i a_{i+1} D^2 \equiv 0 \pmod{a_i a_{i+1}}$, so $P_i(t) \bmod (a_i a_{i+1})$ is linear in $t$; vanishing at $t=0$ and $t=1$ implies $a_i a_{i+1} \mid P_i(t)$ for **all** $t \in \mathbb{Z}$.
     - *Interval membership:* With strict slope $1/2 < s_i < 3/2$, $m > x \iff m \ge \lfloor x \rfloor + 1$ holds identically for all $x \in \mathbb{Q}$ (positive, negative, or integer); for $s_i = 1$, $\{c_i, c_{i+1}\} \neq \{0, 1\} \implies p_i \neq 0 \implies f_i(m) \neq 2m^2+2m$ for all $m$; for $s_i \neq 1$, any positive integer root is strictly below $M_0$.
     - *Pairwise distinctness:* Because $c_0, \dots, c_{k-1}$ are pairwise distinct and $k \ge 3$ (so $k \nmid 2$), the unordered pairs $\{c_i, c_{i+1}\}$ and $\{c_j, c_{j+1}\}$ are distinct for all $0 \le i < j < k$, so $(s_i, p_i) \neq (s_j, p_j)$, eliminating identical polynomials and forcing distinctness for all $m \ge M_0$.
     - *Product $= 2 \cdot \square$:* Odd $k = 2s + 1$ yields $\prod_{i=0}^{k-1} f_i(m) = 2 q^2$ with $q \in \mathbb{Q}_{>0}$; writing $q = u/v$ in lowest terms, $2q^2 \in \mathbb{Z} \implies v^2 \mid 2 \implies v = 1 \implies q \in \mathbb{Z}_{>0}$. **Airtight.**
   - **Lemma 5:** $c_i' = 1 - c_i \in \mathbb{Q} \setminus \{1/2\}$ preserves strict slope and $\{0, 1\}$-avoidance; for $m' \equiv -1 - r \pmod D$, $m := -1 - m' \equiv r \pmod D$ gives $2(m' + c_i')(m' + c_{i+1}') = 2(m + c_i)(m + c_{i+1}) \in \mathbb{Z}$ by Lemma 4 Part 1 (which holds for all $t \in \mathbb{Z}$). **Airtight.**

4. **Section 5 (78-Leaf Covering Tree mod 2520 & 10 Finite Witnesses) and Section 6 (Exceptions $\{2, 3, 10, 171\}$):**
   - Verified case exhaustion across all primes $p \ge 2$: $p \in \{2, 3\}$ (exceptions), $p = 5$ ($k=1$ by Lemma 2, $k=2$ is exception $n=10$), $p = 7$ ($k \le 2$ by Lemma 2, $k=3$ is $n=21$ in Table 2 with $21 \cdot 27 \cdot 28 = 126^2$), and all $p > 7$ ($\gcd(p, 210) = 1 \implies m \bmod 2520 \in U$, $|U| = 24 \cdot \varphi(105) = 1152$).
   - Verified all four exceptions in Section 6 by hand (including every prime factorization of all 18 integers in $\{172, \dots, 189\}$ for $n = 171$, Pass 1 & Pass 2 eliminations, and even $v_2$ parity of $\{175, 180, 189\}$).
   - Audited all 402 lines of `notes/check-check-1.py` (parses Table 1 & Table 2 directly from `PROOF.md`, exact integer & `Fraction` arithmetic, zero floats) and confirmed re-run (`notes/audit-helper-a006255.md` §3.1): exit code `0`, `PASS`.
   - Independent in-memory checks (`notes/audit-helper-a006255.md` §3.2) additionally verified Lemma 4(2) verbatim in pure integer arithmetic for all 78 leaves, all 248 negative / 137 integer `floor` edge cases, direct membership/distinctness/squareness at every integer $m \in [M_0, 5000]$ across all 78 leaves, all 1225 primes $p \in [2, 10000] \setminus \{2,3,5,19\}$, all 10 Table 2 witnesses, and all Section 6 factorizations plus $a(171) = 195$. **Airtight.**

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-a006255.md` §2, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) confirmed:
- **No prior proof found** on live OEIS `A006255` (rev. 106, `2026-06-19`), in `watch/snapshots/**` (277 files), arXiv (inspected `arXiv:2410.04728` Kagey–Rajesh 2024 and `arXiv:2504.19196` Adenwalla 2025 directly; neither settles the boundary $n = p(p-1)/2$ or Padhi's conjecture), Zenodo, GitHub (`1337isnot1337`, `joaquimmj`, `the-omega-institute`), Stack Exchange (`mathoverflow` & `math`), or web search.
- **What Is Not Established / Caveats:**
  - The verification of the 78 covering-tree leaves in Table 1 (congruence integrality, exact thresholds $M_0, M_0'$, disjointness and $1152/1152$ coverage of $U \bmod 2520$, and enumeration of the 10 uncovered primes below $M_0$) and the 10 Table 2 witnesses is carried out by exact integer/rational computation (`notes/check-check-1.py`), not hand calculation of all 78 rows.
  - Does not determine $a(n)$ outside $b(n)^2 \ge 2n$, nor address Corneth's separate question on `A277624`.
  - OpenAlex and Semantic Scholar APIs were rate-limited (`HTTP 429`) during Gate 2 and Gate 3 checks; live OEIS (rev. 106), arXiv, Zenodo, Crossref, web, `aliromman/math`, and `trureturing-tools` were explicitly checked and cleared at Gate 3.
  - Internal audit and exact computation are not formal peer review or a Lean formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`. Gate 3 novelty cleared (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`, checked `2026-11-26T23:05:24Z–23:10:00Z` UTC, incl. live `aliromman/math` and `trureturing-tools`).

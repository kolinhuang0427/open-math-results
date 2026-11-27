# Proof of Padhi's (2026) Conjecture on Graham's Sequence (OEIS A006255)

## 1. Statement and Primary Source

From **OEIS A006255** (revision 106, `2026-06-19T00:16:16-04:00`, Comments section):

> *"Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"*

where the sequences are defined on $\mathbb{Z}_{\ge 1}$ in OEIS as follows:
- **A006255** (rev. 106, offset `1,2`): *"R. L. Graham's sequence: $a(n)$ = smallest $m$ for which there is a sequence $n = b_1 < b_2 < \dots < b_t = m$ such that $b_1 b_2 \cdots b_t$ is a perfect square."* (For a square $n = k^2$, $t = 1$ gives $a(n) = n$.)
- **A007913** (rev. 213, offset `1,2`): *"Squarefree part of $n$: $a(n)$ is the smallest positive number $m$ such that $n/m$ is a square."* (In particular, $\mathrm{A007913}(k^2) = 1$.)
- **A006530** (rev. 248, offset `1,2`): *"$\mathrm{Gpf}(n)$: greatest prime dividing $n$, for $n \ge 2$; $a(1) = 1$."*

**Theorem.** *For every integer $n \ge 1$, let $b(n) = \mathrm{A006530}(\mathrm{A007913}(n))$. If $b(n)^2 \ge 2n$, then $a(n) = n + b(n)$ except precisely for $n \in \{2, 3, 10, 171\}$.*

---

## 2. Structural Reduction

Let $n \ge 1$ satisfy $b(n)^2 \ge 2n$.

**Lemma 1 (Prime-factor structure and lower bound).**
*If $b(n)^2 \ge 2n$, then $p := b(n)$ is prime, $p$ is the largest prime factor of $n$, and $n = k p$ for a unique integer $k$ satisfying $1 \le k \le \lfloor p/2 \rfloor$ (with $p \nmid k$). Moreover, $a(n) \ge n + p$, with equality $a(n) = n + p$ if and only if there exists a subset $S \subseteq (kp, (k+1)p) \cap \mathbb{Z}$ whose product equals $k(k+1) \cdot \square$.*

*Proof.*
If $n$ is a perfect square, then $\mathrm{A007913}(n) = 1$ and $b(n) = \mathrm{A006530}(1) = 1$, contradicting $b(n)^2 = 1 \ge 2n \ge 2$. Hence $n$ is non-square, $\mathrm{A007913}(n) \ge 2$, and $p := b(n)$ is a prime with $v_p(n) \ge 1$ odd.

If $v_p(n) \ge 3$, then $n \ge p^3$, giving $2n \ge 2p^3 > p^2$ for every prime $p \ge 2$, contradicting $p^2 \ge 2n$. Hence $v_p(n) = 1$, so $n = kp$ with $p \nmid k$. If any prime $q > p$ divided $n$, then since $q \nmid \mathrm{A007913}(n)$ we would have $v_q(n) \ge 2$, giving $n \ge p q^2 > p^3$ and again $2n > p^2$, contradiction. Thus $p$ is the greatest prime divisor of $n$, and $p^2 \ge 2n = 2kp$ is equivalent to $1 \le k \le \lfloor p/2 \rfloor$.

In any strictly increasing integer sequence $n = b_1 < b_2 < \dots < b_t = m$ whose product is a square, the parity of $v_p(b_1 b_2 \cdots b_t)$ must be even. Since $v_p(b_1) = 1$ is odd, some $b_j > b_1 = kp$ must be divisible by $p$, so $m = b_t \ge b_j \ge (k+1)p = n + p$.

Finally, no integer in the open interval $(kp, (k+1)p)$ is divisible by $p$. Thus a sequence ending at $m = (k+1)p$ has the form $\{kp\} \cup S \cup \{(k+1)p\}$ for a subset $S \subseteq (kp, (k+1)p) \cap \mathbb{Z}$, and its product is
$$kp \cdot (k+1)p \cdot \prod_{x \in S} x = p^2 k(k+1) \prod_{x \in S} x,$$
which is a perfect square if and only if $\prod_{x \in S} x = k(k+1) \cdot \square$. (Note that $S \neq \emptyset$ automatically, since $k^2 < k(k+1) < (k+1)^2$.) $\square$

---

## 3. The Non-Boundary Regime $1 \le k \le \frac{p-3}{2}$

For $p = 2$, $1 \le k \le \lfloor 2/2 \rfloor = 1$ gives $n = 2$ (treated in Section 6). Henceforth let $p \ge 3$ be an odd prime, and write $m := \frac{p-1}{2} \ge 1$ (so $p = 2m + 1$ and $1 \le k \le m$).

The regime $1 \le k \le m - 1 = \frac{p-3}{2}$ corresponds to $p > \sqrt{2n} + 1$ (Bateman–Erdős–Selfridge 1992, Problem 6655; Granville–Selfridge 2001, Corollary 1). For completeness, we include a self-contained proof handling all coincidence cases explicitly.

**Lemma 2 (Granville–Selfridge Corollary 1).**
*For every odd prime $p = 2m + 1 \ge 5$ and every integer $k$ with $1 \le k \le m - 1$, we have $a(kp) = (k+1)p$.*

*Proof.*
Define the four integers
$$x_1 = 2k(m+1), \quad x_2 = (2k+1)m, \quad x_3 = (2k+1)(m+1), \quad x_4 = 2(k+1)m.$$
Their offsets above $kp = k(2m+1)$ are:
$$x_1 - kp = k, \quad x_2 - kp = m - k, \quad x_3 - kp = m + k + 1, \quad x_4 - kp = 2m - k.$$
Since $1 \le k \le m - 1$, we have
$$1 \le k, \, m - k \le m - 1 < m + 1 \le 2m - k, \, m + k + 1 \le 2m = p - 1.$$
Hence $x_1, x_2, x_3, x_4 \in (kp, (k+1)p)$ and $\{x_1, x_2\} \cap \{x_3, x_4\} = \emptyset$. Moreover,
$$x_1 x_2 x_3 x_4 = k(k+1) \cdot \big(2 m (m+1) (2k+1)\big)^2.$$
- If $m \neq 2k$ and $m \neq 2k+1$, then $x_1 \neq x_2$ and $x_3 \neq x_4$, so all four integers are pairwise distinct and $S = \{x_1, x_2, x_3, x_4\} \subset (kp, (k+1)p)$ satisfies $\prod_{x \in S} x = k(k+1) \cdot \square$.
- If $m = 2k$, then $x_4 = 2(k+1)(2k) = 4k(k+1) \in (kp, (k+1)p)$, so $S = \{x_4\}$ has product $k(k+1) \cdot 2^2$.
- If $m = 2k + 1$, then $x_1 = 2k(2k+2) = 4k(k+1) \in (kp, (k+1)p)$, so $S = \{x_1\}$ has product $k(k+1) \cdot 2^2$.

In all cases, Lemma 1 yields $a(kp) = (k+1)p$. $\square$

---

## 4. The Boundary Case $n = \frac{p(p-1)}{2}$ and the Polynomial Odd-Cycle Method

By Lemmas 1 and 2, the only remaining cases with $p \ge 3$ odd are $k = m = \frac{p-1}{2}$, i.e.,
$$n = m(2m+1) = 2m^2 + m = \frac{p(p-1)}{2}, \qquad n + p = (m+1)(2m+1) = 2m^2 + 3m + 1.$$

Set $x_0 := 2m(m+1) = 2m^2 + 2m$, which lies strictly in $(n, n+p)$ for every $m \ge 1$, and define the punctured interval
$$I(m) := \big((2m^2 + m, \, 2m^2 + 3m + 1) \cap \mathbb{Z}\big) \setminus \{2m^2 + 2m\}.$$
Since
$$n \cdot x_0 \cdot (n + p) = m(2m+1) \cdot 2m(m+1) \cdot (m+1)(2m+1) = 2\big(m(m+1)(2m+1)\big)^2,$$
Lemma 1 immediately gives:

**Lemma 3 (Reduction to $2 \cdot \square$ in $I(m)$).**
*For any odd prime $p = 2m+1 \ge 3$, if there exists a subset $S \subseteq I(m)$ whose product equals $2 \cdot \square$, then $S \cup \{x_0\} \subset (n, n+p)$ has product $m(m+1) \cdot \square$, and consequently $a(n) = n + p$.*

We construct such subsets $S \subseteq I(m)$ uniformly across congruence classes modulo $D \mid 2520$ using odd cycles of rational shifts.

**Lemma 4 (Polynomial Odd-Cycle Lemma).**
*Fix integers $D \ge 1$ and $r \in \{0, \dots, D-1\}$, an odd integer $k = 2s + 1 \ge 3$, and pairwise distinct rational numbers $c_0, c_1, \dots, c_{k-1} \in \mathbb{Q} \setminus \{\tfrac{1}{2}\}$ (indices taken modulo $k$). Write each $c_i = b_i / a_i$ in lowest terms with $a_i \ge 1$ and $\gcd(a_i, |b_i|) = 1$, and for each $i \in \{0, \dots, k-1\}$ set $s_i := c_i + c_{i+1}$, $p_i := c_i c_{i+1}$, and*
$$f_i(m) := 2(m + c_i)(m + c_{i+1}) = 2m^2 + 2s_i m + 2p_i.$$
*Suppose that for every $i \in \{0, \dots, k-1\}$:*
1. *(Strict slope)* $\frac{1}{2} < s_i < \frac{3}{2}$, and $\{c_i, c_{i+1}\} \neq \{0, 1\}$;
2. *(Congruence integrality)* $a_i a_{i+1} \mid 2(a_i m + b_i)(a_{i+1} m + b_{i+1})$ holds for $m = r$ and for $m = D + r$.

*Define the threshold integer $M_0 \ge 1$ as the maximum of $1$ and:*
- $\left\lfloor \frac{-2p_i}{2s_i - 1} \right\rfloor + 1$ *and* $\left\lfloor \frac{2p_i - 1}{3 - 2s_i} \right\rfloor + 1$ *for all $0 \le i < k$;*
- $\frac{-p_i}{s_i - 1} + 1$ *for all $0 \le i < k$ with $s_i \neq 1$ for which $\frac{-p_i}{s_i - 1} \in \mathbb{Z}_{\ge 1}$;*
- $\frac{p_j - p_i}{s_i - s_j} + 1$ *for all $0 \le i < j < k$ with $s_i \neq s_j$ for which $\frac{p_j - p_i}{s_i - s_j} \in \mathbb{Z}_{\ge 1}$.*

*Then for every integer $m \ge M_0$ with $m \equiv r \pmod D$, the $k$ numbers $f_0(m), f_1(m), \dots, f_{k-1}(m)$ are pairwise distinct integers belonging to $I(m)$ whose product equals $2 \cdot \square$.*

*Proof.*
1. **Integrality for all $m \equiv r \pmod D$:** Write $m = D t + r$ ($t \in \mathbb{Z}$) and set
   $$P_i(t) := 2(a_i(Dt + r) + b_i)(a_{i+1}(Dt + r) + b_{i+1}).$$
   The coefficient of $t^2$ in $P_i(t)$ is $2 a_i a_{i+1} D^2 \equiv 0 \pmod{a_i a_{i+1}}$, so $P_i(t) \equiv A_i t + B_i \pmod{a_i a_{i+1}}$ is linear in $t$. Hypothesis (2) states $P_i(0) \equiv 0$ and $P_i(1) \equiv 0 \pmod{a_i a_{i+1}}$, whence $B_i \equiv 0$ and $A_i \equiv P_i(1) - P_i(0) \equiv 0 \pmod{a_i a_{i+1}}$. Therefore $a_i a_{i+1} \mid P_i(t)$ for all $t \in \mathbb{Z}$, so $f_i(m) = \frac{P_i(t)}{a_i a_{i+1}} \in \mathbb{Z}$ for all $m \equiv r \pmod D$.

2. **Membership in $I(m)$:** Fix $m \ge M_0$ and $0 \le i < k$. Since $2s_i - 1 > 0$ and $3 - 2s_i > 0$:
   - $f_i(m) - (2m^2 + m) = (2s_i - 1)m + 2p_i > 0 \iff m > \frac{-2p_i}{2s_i - 1}$, which holds since $m \ge \lfloor \frac{-2p_i}{2s_i - 1} \rfloor + 1$;
   - $(2m^2 + 3m + 1) - f_i(m) = (3 - 2s_i)m + 1 - 2p_i > 0 \iff m > \frac{2p_i - 1}{3 - 2s_i}$, which holds since $m \ge \lfloor \frac{2p_i - 1}{3 - 2s_i} \rfloor + 1$;
   - $f_i(m) - (2m^2 + 2m) = 2(s_i - 1)m + 2p_i$. If $s_i = 1$, then $\{c_i, c_{i+1}\} \neq \{0, 1\}$ implies $c_i \neq 0$ and $c_{i+1} \neq 0$, so $2p_i \neq 0$ and $f_i(m) \neq 2m^2 + 2m$ for all $m$. If $s_i \neq 1$, the unique root $m = \frac{-p_i}{s_i - 1}$ is strictly less than $M_0 \le m$ whenever it is a positive integer.
   Thus $f_i(m) \in I(m)$ for all $i$.

3. **Pairwise distinctness:** Because $c_0, \dots, c_{k-1}$ are pairwise distinct and $k \ge 3$, the unordered pairs $\{c_i, c_{i+1}\}$ and $\{c_j, c_{j+1}\}$ are distinct for every $0 \le i < j < k$, so the polynomials $f_i$ and $f_j$ have distinct root multisets and are not identically equal. Hence $(s_i, p_i) \neq (s_j, p_j)$. If $s_i = s_j$, then $f_i(m) - f_j(m) = 2(p_i - p_j) \neq 0$ for all $m$; if $s_i \neq s_j$, the unique solution $m = \frac{p_j - p_i}{s_i - s_j}$ is strictly less than $M_0 \le m$ whenever it is a positive integer. Thus $f_0(m), \dots, f_{k-1}(m)$ are pairwise distinct.

4. **Product equals $2 \cdot \square$:** Since $k = 2s + 1$ is odd,
   $$\prod_{i=0}^{k-1} f_i(m) = 2^{2s+1} \prod_{i=0}^{k-1} (m + c_i)^2 = 2 q^2, \qquad q := \left|2^s \prod_{i=0}^{k-1} (m + c_i)\right| \in \mathbb{Q}_{\ge 0}.$$
   Since each $f_i(m) > 2m^2 + m > 0$, every $m + c_i \neq 0$, so $q \in \mathbb{Q}_{>0}$. Writing $q = u/v$ with $u, v \in \mathbb{Z}_{>0}$ and $\gcd(u, v) = 1$, the integrality of $2q^2 = \prod f_i(m) \in \mathbb{Z}$ implies $v^2 \mid 2u^2$, hence $v^2 \mid 2$, so $v = 1$ and $q \in \mathbb{Z}_{>0}$. Thus $\prod_{i=0}^{k-1} f_i(m) = 2q^2$. $\square$

**Lemma 5 (Mirror Symmetry).**
*If $(c_0, \dots, c_{k-1})$ satisfies hypotheses (1) and (2) of Lemma 4 for $(D, r)$, then the reflected cycle $(c_0', \dots, c_{k-1}')$ with $c_i' := 1 - c_i$ satisfies hypotheses (1) and (2) of Lemma 4 for $(D, r')$, where $r' := (D - 1 - r) \bmod D$.*

*Proof.*
Clearly $c_0', \dots, c_{k-1}' \in \mathbb{Q} \setminus \{\tfrac{1}{2}\}$ are pairwise distinct, $c_i' + c_{i+1}' = 2 - (c_i + c_{i+1}) \in (\tfrac{1}{2}, \tfrac{3}{2})$ strictly, and $\{c_i', c_{i+1}'\} = \{0, 1\} \iff \{c_i, c_{i+1}\} = \{0, 1\}$ (false). For any integer $m' \equiv r' \equiv -1 - r \pmod D$, set $m := -1 - m' \equiv r \pmod D$; then
$$2(m' + c_i')(m' + c_{i+1}') = 2(-m - c_i)(-m - c_{i+1}) = 2(m + c_i)(m + c_{i+1}) \in \mathbb{Z}$$
by part 1 of the proof of Lemma 4. In particular, hypothesis (2) holds for $(D, r')$ at $m' = r'$ and $m' = D + r'$. $\square$

---

## 5. Complete Covering Tree Modulo 2520 and Finite Prime Witnesses

Every prime $p > 7$ satisfies $\gcd(p, 210) = 1$, so $m = \frac{p-1}{2}$ lies in the set of $1{,}152$ residue classes
$$U := \big\{m \in \{0, 1, \dots, 2519\} : \gcd(2m+1, 210) = 1\big\}.$$

Table 1 lists **39 canonical half-leaves** $(D, r, (c_0, \dots, c_{k-1}))$ with $D \mid 2520$, together with their mirror residues $r' = D - 1 - r$ (whose mirror cycles are $c_i' = 1 - c_i$) and exact thresholds $M_0$ and $M_0'$ from Lemma 4. All **78 full leaves** are pairwise disjoint modulo $2520$, satisfy every hypothesis of Lemma 4 (and Lemma 5), and their union covers $1{,}476$ residue classes modulo $2520$, including **all $1{,}152$ classes of $U$** (the additional $324$ classes have $\gcd(2m+1, 35) > 1$ because coarser moduli $D \in \{6, 30, 60\}$ do not restrict modulo $5$ or $7$). The global maximum threshold across all 78 leaves is $\max(M_0, M_0') = 2350$ (at $D = 840$, $r' = 669$).

### Table 1: The 39 Canonical Half-Leaves (78 Full Leaves via Mirror Symmetry)

| # | $D$ | $r$ | $r'$ | $k$ | $M_0$ | $M_0'$ | Canonical cycle $(c_0, c_1, \dots, c_{k-1})$ |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 6 | 0 | 5 | 3 | 1 | 1 | `2/3, 0, 3/4` |
| 2 | 30 | 3 | 26 | 3 | 4 | 3 | `1/3, 3/4, 3/5` |
| 3 | 30 | 14 | 15 | 3 | 1 | 1 | `1/6, 1, 2/5` |
| 4 | 60 | 20 | 39 | 3 | 1 | 1 | `5/8, 0, 4/5` |
| 5 | 210 | 8 | 201 | 3 | 9 | 2 | `3/4, 2/5, 4/7` |
| 6 | 210 | 51 | 158 | 7 | 52 | 54 | `3/7, 1/10, 8/7, -3/5, 3/2, -2/7, 4/5` |
| 7 | 420 | 68 | 351 | 9 | 15 | 37 | `2/5, 3/4, 0, 11/8, -4/5, 23/14, -1/3, 1, 1/3` |
| 8 | 420 | 69 | 350 | 3 | 1 | 1 | `2/7, 1, 3/10` |
| 9 | 420 | 81 | 338 | 13 | 152 | 129 | `1/5, 8/7, -1/2, 13/7, -6/5, 18/7, -5/3, 9/4, -1, 8/5, -2/7, 9/10, 3/7` |
| 10 | 420 | 110 | 309 | 7 | 41 | 30 | `5/7, -1/10, 10/7, -5/8, 6/5, 0, 3/5` |
| 11 | 420 | 111 | 308 | 3 | 1 | 1 | `1/8, 1, 3/7` |
| 12 | 420 | 128 | 291 | 9 | 549 | 22 | `5/8, 0, 11/8, -4/5, 2, -3/5, 9/7, 1/10, 4/7` |
| 13 | 420 | 188 | 231 | 9 | 39 | 22 | `2/5, 3/4, 0, 11/8, -4/5, 19/12, -2/7, 1, 1/3` |
| 14 | 840 | 141 | 698 | 5 | 1 | 3 | `9/16, 1/3, 3/4, 3/7, 13/15` |
| 15 | 840 | 170 | 669 | 15 | 451 | 2350 | `6/7, -1/4, 10/7, -5/6, 74/35, -25/16, 18/7, -2, 45/16, -46/35, 25/12, -22/35, 65/48, 2/35, 5/8` |
| 16 | 840 | 321 | 518 | 5 | 2 | 1 | `9/16, 1/7, 1, 1/4, 3/5` |
| 17 | 840 | 398 | 441 | 5 | 4 | 22 | `41/48, -2/7, 1, 1/3, 2/5` |
| 18 | 1260 | 9 | 1250 | 13 | 29 | 85 | `11/21, 39/40, -3/7, 3/2, -2/3, 9/5, -11/9, 27/14, -4/9, 9/7, -1/4, 1, 9/20` |
| 19 | 1260 | 189 | 1070 | 3 | 1 | 1 | `0, 7/9, 9/14` |
| 20 | 1260 | 230 | 1029 | 13 | 1176 | 2290 | `38/45, 5/8, 2/5, 5/6, -1/5, 5/3, -1/2, 16/9, -8/7, 13/6, -5/7, 22/15, -5/28` |
| 21 | 1260 | 369 | 890 | 11 | 14 | 12 | `1/4, 1, -1/5, 13/8, -1, 2, -9/14, 11/9, 0, 5/6, 3/7` |
| 22 | 1260 | 410 | 849 | 15 | 111 | 220 | `1/40, 10/21, 11/20, 0, 5/4, -2/5, 15/8, -6/5, 5/2, -5/3, 11/5, -10/9, 7/4, -8/9, 10/7` |
| 23 | 1260 | 429 | 830 | 7 | 70 | 3 | `1/6, 3/5, 3/8, 1/3, 3/4, -1/9, 6/5` |
| 24 | 1260 | 470 | 789 | 5 | 1 | 1 | `7/10, 5/9, 4/7, 3/4, 0` |
| 25 | 1260 | 609 | 650 | 7 | 70 | 3 | `-1/9, 6/5, 1/6, 3/5, 3/8, 1/3, 3/4` |
| 26 | 2520 | 21 | 2498 | 5 | 22 | 1 | `6/7, 7/18, 3/5, 2/3, 0` |
| 27 | 2520 | 50 | 2469 | 17 | 171 | 23 | `74/45, -5/28, 4/3, 1/7, 5/9, 11/14, -2/9, 19/16, -10/21, 29/20, 0, 6/5, -5/8, 2, -5/4, 34/15, -55/56` |
| 28 | 2520 | 98 | 2421 | 7 | 3 | 10 | `7/8, -2/7, 14/9, -1/8, 2/3, 7/16, 2/7` |
| 29 | 2520 | 249 | 2270 | 5 | 1 | 3 | `3/4, 1/3, 3/8, 33/35, -1/9` |
| 30 | 2520 | 278 | 2241 | 5 | 1 | 1 | `7/16, 2/9, 1, 1/3, 2/5` |
| 31 | 2520 | 561 | 1958 | 11 | 18 | 69 | `-51/56, 67/45, -3/28, 13/15, 3/7, 1/6, 9/7, -9/16, 5/3, -3/4, 19/9` |
| 32 | 2520 | 590 | 1929 | 9 | 39 | 10 | `25/16, -2/3, 19/16, 2/9, 5/8, 6/7, -1/4, 10/7, -2/15` |
| 33 | 2520 | 818 | 1701 | 3 | 1 | 1 | `2/9, 1, 5/14` |
| 34 | 2520 | 861 | 1658 | 15 | 22 | 259 | `21/16, -1/21, 21/20, 3/7, 7/45, 69/56, -7/15, 3/2, -1/5, 7/8, 3/5, 2/3, 0, 7/6, -3/7` |
| 35 | 2520 | 938 | 1581 | 7 | 24 | 70 | `4/7, 0, 10/7, -7/8, 14/9, -1/14, 7/9` |
| 36 | 2520 | 1089 | 1430 | 17 | 460 | 21 | `1/3, 3/8, 3/5, 1/6, 6/5, -2/3, 9/5, -11/9, 9/4, -1, 13/8, -1/5, 1, 1/5, 9/14, -1/9, 9/8` |
| 37 | 2520 | 1118 | 1401 | 3 | 1 | 16 | `1/4, 4/7, 4/9` |
| 38 | 2520 | 1310 | 1209 | 13 | 231 | 30 | `25/24, -2/7, 19/16, -2/3, 7/4, -10/9, 11/5, -5/6, 8/5, -5/12, 38/35, 5/16, 2/5` |
| 39 | 2520 | 1778 | 741 | 13 | 116 | 182 | `7/10, -1/7, 7/5, -6/7, 21/10, -11/7, 14/5, -4/3, 11/5, -7/9, 10/7, 0, 4/7` |

*(For illustration, Leaf #1 gives $f_0(m) = 2(m+\frac{2}{3})m = 8t(9t+1)$, $f_1(m) = 2m(m+\frac{3}{4}) = 9t(8t+1)$, and $f_2(m) = 2(m+\frac{3}{4})(m+\frac{2}{3}) = (8t+1)(9t+1)$ for $m = 6t$ ($t \ge 1$), whose product is $2(6t(8t+1)(9t+1))^2$, settling all primes $p \equiv 1 \pmod{12}$, and its mirror $r' = 5$ settles all $p \equiv 11 \pmod{12}$ for $p \ge 11$.)*

### Finite Uncovered Primes ($p = 7$ and $p > 7$ with $m < M_0(\text{leaf})$)

Checking every prime $p = 2m + 1 > 7$ with $m < 2350$ against the threshold $M_0$ of its unique covering leaf in Table 1 yields **exactly 10 primes** with $m < M_0(\text{leaf})$:
$$p \in \{17, \, \mathbf{19}, \, 43, \, 101, \, 103, \, 163, \, 257, \, 461, \, 1097, \, 3019\}.$$
Excluding $p = 19$ ($n = 171$, treated in Section 6) and adding $p = 7$ ($n = 21$, which has $7 \mid 210$) leaves exactly **10 boundary cases** $n = p(p-1)/2$. For each of these 10 primes, Table 2 exhibits an explicit subset $S \subset (n, n+p)$ whose product with $n(n+p)$ is a perfect square, proving $a(n) = n + p$ by Lemma 1.

### Table 2: Explicit Finite Witnesses for All 10 Remaining Non-Exception Boundary Primes

| $p$ | $m = \frac{p-1}{2}$ | Leaf $(D, r)$ | $n = \frac{p(p-1)}{2}$ | $n+p$ | Witness $S \subset (n, n+p)$ | $\sqrt{n(n+p)\prod_{x\in S} x}$ |
|---:|---:|---|---:|---:|---|---:|
| 7 | 3 | ($7 \mid 210$) | 21 | 28 | $\{27\}$ | $126$ |
| 17 | 8 | $(210, 8)$ | 136 | 153 | $\{147, 150\}$ | $21420$ |
| 43 | 21 | $(2520, 21)$ | 903 | 946 | $\{910, 918, 935, 936\}$ | $790269480$ |
| 101 | 50 | $(2520, 50)$ | 5050 | 5151 | $\{5054, 5100, 5103\}$ | $1849724100$ |
| 103 | 51 | $(210, 51)$ | 5253 | 5356 | $\{5270, 5289, 5330, 5332\}$ | $149287948680$ |
| 163 | 81 | $(420, 81)$ | 13203 | 13366 | $\{13224, 13243, 13311\}$ | $20282290164$ |
| 257 | 128 | $(420, 128)$ | 32896 | 33153 | $\{32956, 32960, 33063, 33110\}$ | $36011775233280$ |
| 461 | 230 | $(1260, 230)$ | 106030 | 106491 | $\{106032, 106134, 106260\}$ | $3674527330320$ |
| 1097 | 548 | $(420, 128)$ | 601156 | 602253 | $\{601704, 601798, 602156\}$ | $280966413268656$ |
| 3019 | 1509 | $(840, 669)$ | 4555671 | 4558690 | $\{4557000, 4557180, 4557465\}$ | $44334874482129000$ |

*(Note: For $p = 17$, $136 \cdot 147 \cdot 150 \cdot 153 = 21420^2$ directly without needing $x_0 = 144$; for $p = 101$, $5100 = x_0$ is included explicitly in $S$.)*

---

## 6. Verification of the Four Genuine Exceptions $n \in \{2, 3, 10, 171\}$

It remains to confirm that $n \in \{2, 3, 10, 171\}$ satisfy $b(n)^2 \ge 2n$ and $a(n) > n + b(n)$.

1. **$n = 2$:** $b(2) = 2$, $2^2 = 4 \ge 4$. By Lemma 1, $a(2) = 4$ would require a subset $S \subseteq \{3\}$ with product $1 \cdot 2 \cdot \square = 2 \cdot \square$; the subsets of $\{3\}$ give products $1$ and $3$, neither of which is $2 \cdot \square$. Hence $a(2) > 4$ (in fact $a(2) = 6$, via $2 \cdot 3 \cdot 6 = 6^2$).
2. **$n = 3$:** $b(3) = 3$, $3^2 = 9 \ge 6$. By Lemma 1, $a(3) = 6$ would require a subset $S \subseteq \{4, 5\}$ with product $1 \cdot 2 \cdot \square = 2 \cdot \square$. Since $4 = 2^2$ and $5$ is prime, every subset product of $\{4, 5\}$ has even $2$-adic valuation, so none is $2 \cdot \square$. Hence $a(3) > 6$ (in fact $a(3) = 8$, via $3 \cdot 6 \cdot 8 = 12^2$).
3. **$n = 10 = 2 \cdot 5$:** $b(10) = 5$, $5^2 = 25 \ge 20$. By Lemma 1, $a(10) = 15$ would require a subset $S \subseteq \{11, 12, 13, 14\}$ with product $2 \cdot 3 \cdot \square = 6 \cdot \square$. Each of the primes $11, 13, 7$ divides only one element of $\{11, 12, 13, 14\}$ ($11, 13, 14$ respectively) and does not divide $6$, so none of $11, 13, 14$ can lie in $S$. The only remaining integer is $12 = 3 \cdot 2^2$, whose subsets have products $1$ and $12$, neither of which is $6 \cdot \square$. Hence $a(10) > 15$ (in fact $a(10) = 18$, via $10 \cdot 12 \cdot 15 \cdot 18 = 180^2$).
4. **$n = 171 = 9 \cdot 19$:** $b(171) = 19$, $19^2 = 361 \ge 342$. By Lemma 1, $a(171) = 190$ would require a subset $S \subseteq \{172, 173, \dots, 189\}$ with product $9 \cdot 10 \cdot \square = 10 \cdot \square = 2 \cdot 5 \cdot \square$. Any integer divisible by a prime $q \notin \{2, 5\}$ that divides no other candidate in $S$ cannot belong to $S$.
   - *Pass 1 (primes $\ge 13$):* Fourteen integers are eliminated immediately by their unique prime divisors in $\{172, \dots, 189\}$:
     $$172 = 4 \cdot 43, \quad 173, \quad 174 = 6 \cdot 29, \quad 177 = 3 \cdot 59, \quad 178 = 2 \cdot 89, \quad 179, \quad 181,$$
     $$182 = 2 \cdot 7 \cdot 13, \quad 183 = 3 \cdot 61, \quad 184 = 8 \cdot 23, \quad 185 = 5 \cdot 37, \quad 186 = 6 \cdot 31, \quad 187 = 11 \cdot 17, \quad 188 = 4 \cdot 47.$$
     (Each listed prime $43, 173, 29, 59, 89, 179, 181, 13, 61, 23, 37, 31, 17, 47$ divides only that single element of $\{172, \dots, 189\}$.)
   - *Pass 2:* Among the four survivors $\{175, 176, 180, 189\}$, the prime $11$ divides only $176 = 16 \cdot 11$, eliminating $176$.
   - The three remaining integers are $175 = 5^2 \cdot 7$, $180 = 2^2 \cdot 3^2 \cdot 5$, and $189 = 3^3 \cdot 7$. All three have **even** $2$-adic valuation ($v_2 = 0, 2, 0$), so no subset of $\{175, 180, 189\}$ can have product $10 \cdot \square$.
   Hence $a(171) > 190$ (in fact $a(171) = 195$).

Combining Lemmas 1–5 with Tables 1 and 2 and Section 6 completes the proof of the theorem. $\blacksquare$

---

## 7. Exact Computational Verification

The standalone exact-arithmetic script `targets/oeis-A006255/verify.py` (using only integer and `fractions.Fraction` arithmetic, with no floating point) independently checks:
1. Lemma 1 for all $1 \le n \le 20{,}000$;
2. Lemma 2 for all $10{,}626$ pairs $(p, k)$ with $5 \le p \le 500$ prime and $1 \le k \le (p-3)/2$;
3. All hypotheses of Lemmas 4–5, exact recomputation of $M_0$ and $M_0'$, 5-point direct evaluation above $M_0$, pairwise disjointness modulo $2520$, and complete coverage of all $1{,}152$ classes in $U$ for all 78 full leaves of Table 1;
4. Exhaustive enumeration of all primes $p > 7$ with $m < M_0(\text{leaf})$, confirming the exact list $\{17, 19, 43, 101, 103, 163, 257, 461, 1097, 3019\}$;
5. Exact squareness (`math.isqrt`) of all 10 witnesses in Table 2;
6. Exact computation of $a(n)$ for $n \in \{2, 3, 10, 171\}$, confirming $a(2) = 6, a(3) = 8, a(10) = 18, a(171) = 195$.

Run via:
```bash
.venv/bin/python targets/oeis-A006255/verify.py
```
(which exits 0 and prints `PASS`). Note that this proof is internally audited and verified by exact computation; it has not undergone external peer review.

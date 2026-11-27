# Refutation of Ivan N. Ianakiev's $18k + 12$ Double Zumkeller Conjecture (OEIS A347063)

## Statement Refuted

In OEIS `A347063` (`rev. 51`, Jul 24 2026), Ivan N. Ianakiev conjectured (Oct 01 2024):

> *It seems that for $k \ge 1$ all numbers of the form $18k + 12$ are terms [Double Zumkeller numbers]. Verified for $k$ in $[1, 45]$.*

We refute this conjecture completely:
1. **Minimal counterexample ($k = 192$):** $n = 18(192) + 12 = 3468 = 12 \cdot 17^2$ is **not** a Double Zumkeller number, and every $n = 18k + 12$ for $1 \le k \le 191$ is a Double Zumkeller number.
2. **Infinite family of counterexamples:** For **every** prime $p \ge 17$, $n = 12 p^2$ satisfies $n \equiv 12 \pmod{18}$ (explicitly $n = 18k + 12$ with $k = \frac{2(p^2 - 1)}{3} \in \mathbb{Z}_{\ge 192}$) and is **never** a Double Zumkeller number.

---

## 1. Proof of the Infinite Counterexample Family $n = 12 p^2$ ($p \ge 17$ prime)

Let $p \ge 17$ be any prime, and set $n = 12 p^2 = 2^2 \cdot 3 \cdot p^2$.

1. **Membership in the progression $18k + 12$:**
   Since $p \ge 17 > 3$, $\gcd(p, 3) = 1$, so $p^2 \equiv 1 \pmod 3$. Writing $p^2 = 3m + 1$ ($m \in \mathbb{Z}_{\ge 96}$), we have
   $$n = 12(3m + 1) = 36m + 12 = 18(2m) + 12 = 18k + 12 \qquad \text{with } k = \frac{2(p^2 - 1)}{3} \in \mathbb{Z}_{\ge 192}.$$
   In particular, $p = 17$ yields $k = \frac{2(289 - 1)}{3} = 192$ and $n = 3468$.

2. **Divisor structure, $\tau(n)$, and $\sigma(n)$:**
   Because $\gcd(12, p^2) = 1$, the divisor set of $n = 12 p^2$ is the $18$-element product
   $$D(12 p^2) = \{1, 2, 3, 4, 6, 12\} \times \{1, p, p^2\}.$$
   Let $D_0 := \{1, 2, 3, 4, 6, 12\}$, which has $|D_0| = 6$ and $\sum_{d \in D_0} d = 1 + 2 + 3 + 4 + 6 + 12 = 28$. Thus:
   $$\tau(n) = 18, \qquad \sigma(n) = 28(1 + p + p^2).$$
   Suppose for contradiction that $n = 12 p^2$ is a Double Zumkeller number, so $D(12 p^2) = A \sqcup B$ with
   $$|A| = |B| = \frac{\tau(n)}{2} = 9 \qquad \text{and} \qquad \sum_{x \in A} x = \sum_{x \in B} x = \frac{\sigma(n)}{2} = 14 + 14p + 14p^2.$$

3. **Forced decomposition of $A$ in base $p$:**
   Decompose $A = (p^2 U_2) \sqcup (p U_1) \sqcup U_0$ with $U_0, U_1, U_2 \subseteq D_0$, and set $s_i := \sum_{u \in U_i} u \in \{0, 1, \dots, 28\}$ for $i \in \{0, 1, 2\}$. Then
   $$s_2 p^2 + s_1 p + s_0 = 14 p^2 + 14 p + 14.$$
   - If $s_2 \ge 15$, then since $p \ge 17$,
     $$s_2 p^2 + s_1 p + s_0 \ge 15 p^2 = 14 p^2 + p^2 \ge 14 p^2 + 17 p > 14 p^2 + 14 p + 14,$$
     impossible.
   - If $s_2 \le 13$, then since $s_1, s_0 \le 28$ and $p \ge 17$, comparing $14 p^2 + 14 p + 14$ with $13 p^2 + 28 p + 28$ directly gives
     $$(14 p^2 + 14 p + 14) - (13 p^2 + 28 p + 28) = p^2 - 14 p - 14 = p(p - 14) - 14 \ge 17 \cdot 3 - 14 = 37 > 0 \quad \forall p \ge 17,$$
     so $s_2 p^2 + s_1 p + s_0 \le 13 p^2 + 28 p + 28 < 14 p^2 + 14 p + 14$, impossible!
   Therefore **$s_2 = 14$** is forced, leaving
   $$s_1 p + s_0 = 14 p + 14.$$
   - If $s_1 \ge 15$, then $s_1 p + s_0 \ge 15 p > 14 p + 14$ (as $p \ge 17 > 14$), impossible.
   - If $s_1 \le 13$, then since $s_0 \le 28$ and $p \ge 17$,
     $$s_1 p + s_0 \le 13 p + 28 = 14 p + 14 - (p - 14) \le 14 p + 14 - 3 < 14 p + 14,$$
     impossible!
   Therefore **$s_1 = 14$** and **$s_0 = 14$** are also forced.

4. **Parity obstruction:**
   We must find every subset $U \subseteq D_0 = \{1, 2, 3, 4, 6, 12\}$ satisfying $\sum_{u \in U} u = 14$:
   - If $12 \in U$, the remaining elements in $\{1, 2, 3, 4, 6\}$ must sum to $2$, leaving only $U = \{2, 12\}$ (cardinality $2$).
   - If $12 \notin U$, then $D_0 \setminus \{12\} = \{1, 2, 3, 4, 6\}$ has sum $16$, so the complement $(D_0 \setminus \{12\}) \setminus U$ must sum to $16 - 14 = 2$, leaving only $U = \{1, 3, 4, 6\}$ (cardinality $4$).

   Thus **every** subset $U \subseteq D_0$ with sum $14$ has even cardinality ($|U| \in \{2, 4\}$). Consequently,
   $$|A| = |U_2| + |U_1| + |U_0| \equiv 0 + 0 + 0 = 0 \pmod 2,$$
   contradicting $|A| = 9 \equiv 1 \pmod 2$.

   Hence $n = 12 p^2$ is **never** a Double Zumkeller number for any prime $p \ge 17$. $\blacksquare$

---

## 2. Minimality of $k = 192$ ($n = 3468$)

Exact bitset dynamic programming in `verify.py` (constructing explicit equal-sum, equal-cardinality divisor partitions $D(n) = A \sqcup B$ for all $1 \le k \le 191$) confirms that $18k + 12 \in \mathrm{A347063}$ for every $k \in \{1, 2, \dots, 191\}$. Thus $k = 192$, $n = 3468 = 12 \cdot 17^2$ is the **unique smallest** counterexample to Ianakiev's conjecture.

As an independent brute-force check on $n = 3468$, `verify.py` also enumerates all $\binom{18}{9} = 48620$ nine-element subsets of $D(3468)$ and confirms that zero of them sum to $\sigma(3468)/2 = 4298$.

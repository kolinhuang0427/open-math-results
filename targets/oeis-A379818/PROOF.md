# Proof of OEIS A379818 (Mikhail Kurkov Binomial Formula Conjecture)

## Theorem
Let $(a(n))_{n \ge 0}$ be OEIS `A379818`, defined by $a(0) = 1$,
$$a(2n+1) = a(n) \qquad (n \ge 0),$$
$$a(2n) = a(n) + a\bigl(n - 2^{f(n)}\bigr) + a\bigl(2n - 2^{f(n)}\bigr) + a\bigl(\mathrm{A025480}(n-1)\bigr) \qquad (n \ge 1),$$
where $f(n) = v_2(n) = \mathrm{A007814}(n)$ is the 2-adic valuation of $n$, and $b(r) := \mathrm{A025480}(r)$ satisfies $b(2r) = r$ and $b(2r+1) = b(r)$ for $r \ge 0$.

Then for all integers $m \ge 0$ and $k \ge 0$,
$$a\bigl(2^m(2k+1)\bigr) = \sum_{j=0}^{m} \left(\binom{m+2}{j+1} - \binom{m}{j}\right) a(2^j k).$$

---

## Lemma (`A025480` shift identity)
For all integers $r \ge 0$ and $k \ge 0$,
$$b\bigl(2^r(2k+1) - 1\bigr) = k.$$

**Proof.** We induct on $r \ge 0$.
- For $r = 0$, $2^0(2k+1) - 1 = 2k$ is even, so $b(2k) = k$.
- For $r \ge 1$, $2^r(2k+1) - 1 = 2\bigl(2^{r-1}(2k+1) - 1\bigr) + 1$ is odd, so by $b(2q+1) = b(q)$ and the induction hypothesis at $r-1$,
  $$b\bigl(2^r(2k+1) - 1\bigr) = b\bigl(2^{r-1}(2k+1) - 1\bigr) = k. \qquad \square$$

---

## Proof of Theorem
For $m \ge 0$ and $0 \le j \le m$, define $c(m, j) := \binom{m+2}{j+1} - \binom{m}{j}$.
Notice the boundary values for every $m \ge 1$:
$$c(m, 0) = \binom{m+2}{1} - \binom{m}{0} = (m+2) - 1 = m + 1,$$
$$c(m, m) = \binom{m+2}{m+1} - \binom{m}{m} = (m+2) - 1 = m + 1.$$

We prove the theorem by induction on $m \ge 0$, universally for all $k \ge 0$.

### Base case $m = 0$
For every $k \ge 0$, the right-hand side is
$$c(0, 0)\, a(2^0 k) = \left(\binom{2}{1} - \binom{0}{0}\right) a(k) = (2 - 1) a(k) = a(k),$$
and the left-hand side is $a(2^0(2k+1)) = a(2k+1) = a(k)$ by the odd recurrence (including $k=0$, where $a(1) = a(0) = 1$).

### Inductive step ($m \ge 1$)
Assume the identity holds at $m - 1$ for every $k' \ge 0$. Fix $k \ge 0$ and set
$$n := 2^{m-1}(2k+1) \ge 1.$$
Then $2n = 2^m(2k+1)$ and $f(n) = v_2(n) = m - 1$, so $2^{f(n)} = 2^{m-1}$. Therefore:
1. $n = 2^{m-1}(2k+1)$,
2. $n - 2^{f(n)} = 2^{m-1}(2k+1) - 2^{m-1} = 2^m k$,
3. $2n - 2^{f(n)} = 2^m(2k+1) - 2^{m-1} = 2^{m-1}(4k + 1) = 2^{m-1}\bigl(2(2k) + 1\bigr)$,
4. $\mathrm{A025480}(n - 1) = b\bigl(2^{m-1}(2k+1) - 1\bigr) = k$ by the Lemma (applied with $r = m - 1 \ge 0$).

Substituting these four terms into the even recurrence $a(2n) = a(n) + a(n - 2^{f(n)}) + a(2n - 2^{f(n)}) + a(\mathrm{A025480}(n-1))$ gives
$$a\bigl(2^m(2k+1)\bigr) = a\bigl(2^{m-1}(2k+1)\bigr) + a(2^m k) + a\bigl(2^{m-1}(2(2k)+1)\bigr) + a(k).$$

Applying the induction hypothesis at $m - 1$ to $k' = k$ and to $k' = 2k$ (both $\ge 0$):
$$a\bigl(2^{m-1}(2k+1)\bigr) = \sum_{j=0}^{m-1} c(m-1, j)\, a(2^j k),$$
$$a\bigl(2^{m-1}(2(2k)+1)\bigr) = \sum_{i=0}^{m-1} c(m-1, i)\, a(2^i (2k)) = \sum_{j=1}^{m} c(m-1, j-1)\, a(2^j k).$$

Adding all four terms and collecting coefficients of $a(2^j k)$ for $0 \le j \le m$:
- For $j = 0$: the coefficient is
  $$c(m-1, 0) + 1 = \left(\binom{m+1}{1} - \binom{m-1}{0}\right) + 1 = m + 1 = c(m, 0).$$
  (When $m = 1$, $c(0, 0) + 1 = 1 + 1 = 2 = c(1, 0)$; when $m \ge 2$, $(m) + 1 = m + 1 = c(m, 0)$.)
- For $1 \le j \le m - 1$ (occurring when $m \ge 2$): by Pascal's identity, the coefficient is
  $$c(m-1, j) + c(m-1, j-1) = \left(\binom{m+1}{j+1} + \binom{m+1}{j}\right) - \left(\binom{m-1}{j} + \binom{m-1}{j-1}\right) = \binom{m+2}{j+1} - \binom{m}{j} = c(m, j).$$
- For $j = m$: the coefficient is
  $$1 + c(m-1, m-1) = 1 + \left(\binom{m+1}{m} - \binom{m-1}{m-1}\right) = 1 + m = c(m, m).$$
  (Again, when $m = 1$, $1 + c(0, 0) = 1 + 1 = 2 = c(1, 1)$; when $m \ge 2$, $1 + m = m + 1 = c(m, m)$.)

Note that at $k = 0$, $a(2^j k) = a(0)$ for all $j$, and the algebra on the coefficients is identical (every step of the induction hypothesis at $k' = 0$ and $k' = 2\cdot 0 = 0$ holds cleanly).

Thus
$$a\bigl(2^m(2k+1)\bigr) = \sum_{j=0}^{m} c(m, j)\, a(2^j k) = \sum_{j=0}^{m} \left(\binom{m+2}{j+1} - \binom{m}{j}\right) a(2^j k),$$
completing the induction. $\square$

# Counterexample & Exact Discrepancy Proof for OEIS A077026 Conjecture

We refute Benedict W. J. Irwin's Sep 22, 2016 conjecture on [OEIS A077026](https://oeis.org/A077026) (rev. 14) for **every** $n \ge 1$, and establish the exact offset identity.

## Statement Refuted

For $n \ge 1$, let
$$a(n) := \sum_{d=1}^{n} \left(\left\lfloor \frac{n}{d} + 1 \right\rfloor - \left\lfloor \frac{n}{d} + \frac{1}{2} \right\rfloor\right),$$
and define for $a \ne b$:
$$f(a, b) := \begin{cases} 1, & (a + b) \bmod |a - b| \ne (a \bmod |a - b|) + (b \bmod |a - b|), \\ 0, & \text{otherwise}, \end{cases}$$
where $x \bmod m$ denotes the standard least nonnegative remainder in $\{0, 1, \dots, m - 1\}$.

The conjecture states $a(n) = S(n) := \sum_{k=1}^{n-1} (1 - f(n, k))$ for $n \ge 1$. This is **false for all $n \ge 1$**:

## Minimal Counterexample ($n = 1$) & Small Cases

- At $n = 1$: $a(1) = \lfloor 1/1 + 1 \rfloor - \lfloor 1/1 + 1/2 \rfloor = 2 - 1 = 1$, whereas $S(1) = \sum_{k=1}^{0}(1 - f(1, k)) = 0 \ne 1$.
- At $n = 2$: $a(2) = (\lfloor 2+1 \rfloor - \lfloor 2+1/2 \rfloor) + (\lfloor 1+1 \rfloor - \lfloor 1+1/2 \rfloor) = (3-2) + (2-1) = 2$, whereas for $k=1$, $|2-1| = 1$, $(2+1)\bmod 1 = 0 = (2\bmod 1) + (1\bmod 1)$, so $f(2, 1) = 0$ and $S(2) = 1 - 0 = 1 \ne 2$.

## Theorem (Exact Discrepancy for All $n \ge 1$)

*For every integer $n \ge 1$,*
$$\sum_{k=1}^{n-1} \bigl(1 - f(n, k)\bigr) = a(n) - 1,$$
*so the conjectured equality $a(n) = \sum_{k=1}^{n-1}(1 - f(n, k))$ fails by $1$ at every $n \ge 1$.*

### Proof

Fix $n \ge 1$ and reindex $k \in \{1, \dots, n - 1\}$ by $d := n - k \in \{1, \dots, n - 1\}$.

1. **Evaluating $1 - f(n, k)$:** Here $|n - k| = d > 0$. Since $n = k + d \equiv k \pmod d$, both $n$ and $k$ leave the same remainder $r := n \bmod d = k \bmod d \in \{0, 1, \dots, d - 1\}$. Therefore
   $$(n \bmod d) + (k \bmod d) = 2r \in \{0, 1, \dots, 2d - 2\}, \qquad (n + k) \bmod d = (2r) \bmod d.$$
   For an integer $2r \in [0, 2d - 2]$, we have $(2r) \bmod d \ne 2r$ if and only if $2r \ge d$. Hence
   $$f(n, k) = 1 \iff 2r \ge d, \qquad\text{so}\qquad 1 - f(n, k) = \begin{cases} 1, & 2r < d, \\ 0, & 2r \ge d. \end{cases}$$

2. **Evaluating the $d$-th term of $a(n)$:** For any $d \in \{1, \dots, n\}$, write $n = q d + r$ with $q = \lfloor n/d \rfloor \in \mathbb{Z}_{\ge 1}$ and $r = n \bmod d \in \{0, \dots, d - 1\}$. Then
   $$\left\lfloor \frac{n}{d} + 1 \right\rfloor - \left\lfloor \frac{n}{d} + \frac{1}{2} \right\rfloor = (q + 1) - \left(q + \left\lfloor \frac{r}{d} + \frac{1}{2} \right\rfloor\right) = 1 - \left\lfloor \frac{2r + d}{2d} \right\rfloor = \begin{cases} 1, & 2r < d, \\ 0, & 2r \ge d. \end{cases}$$

Comparing (1) and (2), for every $d \in \{1, \dots, n - 1\}$ with $k = n - d$, the $d$-th summand of $a(n)$ equals $1 - f(n, k)$. The sole remaining summand in $a(n)$ is $d = n$, where $\lfloor n/n + 1 \rfloor - \lfloor n/n + 1/2 \rfloor = 2 - 1 = 1$. Summing over $d = 1, \dots, n$ yields
$$a(n) = 1 + \sum_{k=1}^{n-1} \bigl(1 - f(n, k)\bigr) \qquad \forall\, n \ge 1. \qquad \square$$

# Proof of OEIS A075997 Conjecture

We prove Benedict W. J. Irwin's Sep 23, 2016 conjecture on [OEIS A075997](https://oeis.org/A075997) (rev. 37) for all $n \ge 0$.

## Theorem

For $n \ge 0$, define $a(n) := \sum_{m=2}^{\infty} (-1)^m \lfloor n / m \rfloor = \sum_{m=2}^{n} (-1)^m \lfloor n / m \rfloor$ (since $\lfloor n / m \rfloor = 0$ for $m > n$), and for $a \ne b$ define
$$f(a, b) := \begin{cases} 1, & (a + b) \bmod |a - b| \ne (a \bmod |a - b|) + (b \bmod |a - b|), \\ 0, & \text{otherwise}, \end{cases}$$
where $x \bmod M$ denotes the least nonnegative remainder in $\{0, 1, \dots, M - 1\}$. Then for every $n \ge 0$,
$$a(n) = \sum_{k=1}^{n-1} f(n + k, n - k).$$

## Proof

For $n = 0$ and $n = 1$, both sides are empty sums equal to $0$. Now fix $n \ge 2$.

### Step 1: Parity representation of $a(n)$
Since $\lfloor n / m \rfloor = \sum_{k=1}^{n} \mathbf{1}_{\{m k \le n\}}$ counts positive integers $k \ge 1$ with $m \le \lfloor n / k \rfloor$, interchanging the order of summation gives
$$a(n) = n + \sum_{m=1}^{n} (-1)^m \lfloor n / m \rfloor = n + \sum_{k=1}^{n} \sum_{m=1}^{\lfloor n/k \rfloor} (-1)^m.$$
For any positive integer $M \ge 1$, the alternating sum $\sum_{m=1}^{M} (-1)^m$ equals $0$ if $M$ is even and $-1$ if $M$ is odd. Therefore
$$a(n) = n - \sum_{k=1}^{n} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is odd}\}} = \sum_{k=1}^{n} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}}.$$
At $k = n$, $\lfloor n / n \rfloor = 1$ is odd, so $k = n$ contributes $0$, leaving
$$a(n) = \sum_{k=1}^{n-1} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}}.$$

### Step 2: Evaluating $f(n + k, n - k)$ for $1 \le k \le n - 1$
Fix $k \in \{1, \dots, n - 1\}$, so $|(n + k) - (n - k)| = 2k > 0$. Because $(n + k) - (n - k) = 2k$, both $n + k$ and $n - k$ lie in the same congruence class modulo $2k$; set
$$r := (n + k) \bmod (2k) = (n - k) \bmod (2k) \in \{0, 1, \dots, 2k - 1\}.$$
Then
$$((n + k) \bmod 2k) + ((n - k) \bmod 2k) = 2r \in \{0, 1, \dots, 4k - 2\}, \qquad ((n + k) + (n - k)) \bmod (2k) = (2r) \bmod (2k).$$
Thus $f(n + k, n - k) = 1$ if and only if $(2r) \bmod (2k) \ne 2r$, which holds if and only if $2r \ge 2k$, i.e.,
$$f(n + k, n - k) = 1 \iff (n - k) \bmod (2k) \in \{k, k + 1, \dots, 2k - 1\}.$$

Adding $k$ modulo $2k$, the condition $(n - k) \bmod (2k) \in \{k, \dots, 2k - 1\}$ is equivalent to
$$n \bmod (2k) \in \{0, 1, \dots, k - 1\}.$$
Writing $n = q k + s$ with $q = \lfloor n / k \rfloor$ and $0 \le s \le k - 1$, we have $n \bmod (2k) = s \in \{0, \dots, k - 1\}$ if $q$ is even, and $n \bmod (2k) = k + s \in \{k, \dots, 2k - 1\}$ if $q$ is odd. Consequently,
$$f(n + k, n - k) = \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}} \qquad \forall\, k \in \{1, \dots, n - 1\}.$$

Summing over $k = 1, \dots, n - 1$ and combining with Step 1 gives
$$\sum_{k=1}^{n-1} f(n + k, n - k) = \sum_{k=1}^{n-1} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}} = a(n). \qquad \square$$

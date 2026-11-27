# Proof of Mathar's 2022 D-Finite Recurrence Conjecture for OEIS A177260

## Statement
Let $(a(n))_{n \ge 0}$ be OEIS **A177260** (offset `0`), defined by
$$a(n) = \sum_{s=0}^{n} \sum_{t=0}^{\lfloor (n-s)/4 \rfloor} (-1)^{s+t} \frac{(n - 3t)!}{s!\, t!}.$$

**Theorem (R. J. Mathar's Conjecture, Jul 26 2022).** For every integer $n \ge 8$,
$$a(n) = (n-1)\,a(n-1) + (n-1)\,a(n-2) + 2\,a(n-4) + (n-1)\,a(n-5) + 3\,a(n-8).$$

---

## Proof

Work in $\mathbb{Q}[[x]]$ (indeed $\mathbb{Z}[[x]]$). Let $y(x) := \sum_{n=0}^{\infty} a(n) x^n$.

### Step 1: Generating function identity
In the double sum for $a(n)$, the summation bounds $0 \le s \le n$ and $0 \le t \le \lfloor (n-s)/4 \rfloor$ are equivalent to $s \ge 0$, $t \ge 0$, and $s + 4t \le n$.
Change variables via $k := n - 3t$ (so $n = k + 3t$, and $s + 4t \le n \iff s + t \le k$):
$$y(x) = \sum_{n=0}^{\infty} a(n) x^n = \sum_{k=0}^{\infty} k! \, x^k \sum_{t=0}^{k} \frac{(-x^3)^t}{t!} \sum_{s=0}^{k-t} \frac{(-1)^s}{s!}.$$
Setting $j := s + t$ ($0 \le t \le j \le k$, $s = j - t$) gives
$$\sum_{t=0}^{k} \sum_{s=0}^{k-t} \frac{(-x^3)^t (-1)^s}{t!\, s!} = \sum_{j=0}^{k} \frac{(-1)^j}{j!} \sum_{t=0}^{j} \binom{j}{t} x^{3t} = \sum_{j=0}^{k} \frac{\bigl(-(1+x^3)\bigr)^j}{j!}.$$
Reindexing $k = j + m$ ($j \ge 0$, $m \ge 0$, with $\frac{(j+m)!}{j!} = m! \binom{j+m}{m}$, where each $[x^n]$ receives contributions only from $j + m \le n$) yields
$$y(x) = \sum_{m=0}^{\infty} m!\, x^m \sum_{j=0}^{\infty} \binom{j+m}{m} \bigl(-x(1+x^3)\bigr)^j = \sum_{m=0}^{\infty} \frac{m!\, x^m}{(1 + x + x^4)^{m+1}}.$$

### Step 2: First-order linear ODE for $y(x)$
Let $F(u) := \sum_{m=0}^{\infty} m!\, u^m \in \mathbb{Z}[[u]]$, which satisfies $u^2 F'(u) + (u - 1) F(u) + 1 = 0$ in $\mathbb{Z}[[u]]$.
Put $D(x) := 1 + x + x^4 \in \mathbb{Z}[x]$ and $u(x) := \frac{x}{D(x)} \in x\mathbb{Z}[[x]]$. By Step 1, $D(x) y(x) = F(u(x))$.
Since $D'(x) = 1 + 4x^3$ and $u'(x) = \frac{D(x) - x D'(x)}{D(x)^2} = \frac{1 - 3x^4}{D(x)^2}$, differentiating $D(x) y(x) = F(u(x))$ in $\mathbb{Z}[[x]]$ gives
$$D(x) y'(x) + (1 + 4x^3) y(x) = F'(u(x)) \frac{1 - 3x^4}{D(x)^2}.$$
Multiplying by $x^2 = D(x)^2 u(x)^2$ and substituting $u^2 F'(u) = (1 - u) F(u) - 1 = (1 + x^4) y(x) - 1$ yields
$$x^2(1 + x + x^4) y'(x) + x^2(1 + 4x^3) y(x) = (1 - 3x^4)\bigl((1 + x^4) y(x) - 1\bigr),$$
that is, identically in $\mathbb{Z}[[x]]$,
$$x^2(1 + x + x^4) y'(x) + (-1 + x^2 + 2x^4 + 4x^5 + 3x^8) y(x) + (1 - 3x^4) = 0.$$

### Step 3: Coefficient extraction
For any integer $n \ge 8$, $[x^n](1 - 3x^4) = 0$. Extracting $[x^n]$ from the ODE gives
$$(n-1)a(n-1) + (n-2)a(n-2) + (n-5)a(n-5) - a(n) + a(n-2) + 2a(n-4) + 4a(n-5) + 3a(n-8) = 0.$$
Rearranging yields, for all $n \ge 8$,
$$a(n) = (n-1)\,a(n-1) + (n-1)\,a(n-2) + 2\,a(n-4) + (n-1)\,a(n-5) + 3\,a(n-8). \qquad \blacksquare$$

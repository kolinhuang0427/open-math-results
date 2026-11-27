# Proof of OEIS A123145 5-Step Continued Fraction Conjecture

We prove Sergei N. Gladkovskii's Nov 26, 2012 conjecture on [OEIS A123145](https://oeis.org/A123145) (rev. 31) in $\mathbb{Q}[[x]]$ (and as entire functions on $\mathbb{C}$).

## 1. Closed Form for $a(n)/n!$

Let $(a(n))_{n \ge 1}$ be defined by $a(1) = 1$ and, for $n \ge 2$,
$$a(n) = \begin{cases} a(n-1), & n \equiv 1 \pmod 4, \\ n\,a(n-1), & n \not\equiv 1 \pmod 4. \end{cases}$$

**Lemma 1.** *For every integer $m \ge 0$ and every $r \in \{1, 2, 3, 4\}$,*
$$\frac{a(4m+r)}{(4m+r)!} = \frac{1}{\prod_{j=0}^{m}(4j+1)}.$$

*Proof.* We proceed by induction on $m \ge 0$.
- For $m = 0$: $a(1)/1! = 1 = 1/(4\cdot 0 + 1)$, and for $r \in \{2, 3, 4\}$ the recurrence $a(r) = r\,a(r-1)$ yields $\frac{a(r)}{r!} = \frac{a(r-1)}{(r-1)!} = 1$.
- For $m \ge 1$: Since $4m + 1 \equiv 1 \pmod 4$ and $4m + 1 \ge 5 \ge 2$, we have $a(4m+1) = a(4m)$. Applying the induction hypothesis at $(m - 1, r = 4)$,
  $$\frac{a(4m+1)}{(4m+1)!} = \frac{a(4m)}{(4m)!} \cdot \frac{1}{4m+1} = \frac{1}{(4m+1)\prod_{j=0}^{m-1}(4j+1)} = \frac{1}{\prod_{j=0}^{m}(4j+1)}.$$
  For $r \in \{2, 3, 4\}$, $4m + r \not\equiv 1 \pmod 4$, so $a(4m+r) = (4m+r)\,a(4m+r-1)$, which preserves the ratio $\frac{a(4m+r)}{(4m+r)!} = \frac{a(4m+r-1)}{(4m+r-1)!} = \frac{1}{\prod_{j=0}^{m}(4j+1)}$. $\square$

## 2. The Sequence of Formal Power Series $G(k)$

For each integer $k \ge 0$, define the formal power series
$$G(k) := 1 + (x + x^2 + x^3 + x^4)\sum_{m=0}^{\infty} \frac{x^{4m}}{\prod_{j=0}^{m}(4k + 4j + 1)} \in \mathbb{Q}[[x]].$$
Note that $G(k) = 1 + O(x)$ is a unit in $\mathbb{Q}[[x]]$ for every $k \ge 0$, and because $\prod_{j=0}^m (4k + 4j + 1) = (4k+1)\prod_{j=1}^m (4k + 4j + 1) \ge 4^m m!$ for all $m \ge 0$, the series actually defines an entire function on $\mathbb{C}$ for every $k \ge 0$.

At $k = 0$, Lemma 1 immediately identifies the coefficients of $G(0)$:
$$G(0) = 1 + \sum_{m=0}^{\infty}\sum_{r=1}^{4} \frac{x^{4m+r}}{\prod_{j=0}^{m}(4j+1)} = 1 + \sum_{n=1}^{\infty} a(n)\frac{x^n}{n!}.$$
Consequently,
$$E(x) := \frac{d}{dx} G(0) = \sum_{n=1}^{\infty} a(n)\frac{x^{n-1}}{(n-1)!} = \sum_{n=0}^{\infty} a(n+1)\frac{x^n}{n!}$$
is the exponential generating function of the left-shifted sequence $(a(n+1))_{n \ge 0}$ (with $a(1) = 1$ at $x^0/0!$), while $G(0)$ itself is the exponential generating function of $(1, a(1), a(2), \dots)$ (matching both `E(x) = d(G(0))/dx` and `or shift on 1 left G(0)`).

**Lemma 2 (Shift relation).** *For every integer $k \ge 0$,*
$$G(k) = 1 + \frac{x + x^2 + x^3 + x^4 G(k+1)}{4k + 1}.$$

*Proof.* Separating the $m = 0$ term from $G(k) - 1$ and reindexing $m = m' + 1$ (using $\prod_{j=0}^{m'+1}(4k + 4j + 1) = (4k + 1)\prod_{j=0}^{m'}(4(k+1) + 4j + 1)$) yields
$$G(k) - 1 = \frac{x + x^2 + x^3 + x^4}{4k+1} + \frac{x^4}{4k+1}\bigl(G(k+1) - 1\bigr) = \frac{x + x^2 + x^3 + x^4 G(k+1)}{4k+1}. \qquad \square$$

## 3. Equivalence with Gladkovskii's 5-Step Continued Fraction

**Theorem.** *For every integer $k \ge 0$, the formal power series $G(k)$ satisfies Gladkovskii's 5-step continued fraction recurrence*
$$G(k) = 1 + \cfrac{x}{4k+1 - \cfrac{x(4k+1)}{1 + x - \cfrac{x}{1 + x - \cfrac{x}{x + \frac{1}{G(k+1)}}}}}$$
*in $\mathbb{Q}[[x]]$ (with every denominator a unit in $\mathbb{Q}[[x]]$), and finite truncations of this infinite continued fraction converge $x$-adically to $G(0)$ (with error $O(x^{4K+4})$ at depth $K$, and $O(x^{4K+5})$ when seeded with any unit $1 + O(x)$). Hence $E(x) = \frac{d}{dx} G(0) = \sum_{n=0}^{\infty} a(n+1)\frac{x^n}{n!}$.*

*Proof.* Fix $k \ge 0$ and write $g := G(k+1) = 1 + O(x) \in \mathbb{Q}[[x]]^\times$ and $c := 4k + 1 \ge 1$. Evaluating the nested denominators from bottom to top in $\mathbb{Q}[[x]]$:

1. $D_4 := x + \dfrac{1}{g} = \dfrac{1 + x g}{g} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$.

2. $D_3 := 1 + x - \dfrac{x}{D_4} = 1 + x - \dfrac{x g}{1 + x g} = \dfrac{(1+x)(1 + x g) - x g}{1 + x g} = \dfrac{1 + x + x^2 g}{1 + x g} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$.

3. $D_2 := 1 + x - \dfrac{x}{D_3} = 1 + x - \dfrac{x(1 + x g)}{1 + x + x^2 g} = \dfrac{(1+x)(1 + x + x^2 g) - (x + x^2 g)}{1 + x + x^2 g} = \dfrac{1 + x + x^2 + x^3 g}{1 + x + x^2 g} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$.

4. $D_1 := c - \dfrac{c x}{D_2} = c\left(1 - \dfrac{x(1 + x + x^2 g)}{1 + x + x^2 + x^3 g}\right) = c \cdot \dfrac{(1 + x + x^2 + x^3 g) - (x + x^2 + x^3 g)}{1 + x + x^2 + x^3 g} = \dfrac{4k+1}{1 + x + x^2 + x^3 g} = (4k+1) + O(x) \in \mathbb{Q}[[x]]^\times$.

Therefore,
$$1 + \frac{x}{D_1} = 1 + \frac{x(1 + x + x^2 + x^3 G(k+1))}{4k+1} = 1 + \frac{x + x^2 + x^3 + x^4 G(k+1)}{4k+1} = G(k)$$
by Lemma 2.

Finally, for any $K \ge 0$ and any unit seed $g_{K+1}^{(K)} \in \mathbb{Q}[[x]]^\times$, let $G^{(K)}(0)$ be the finite continued fraction obtained by setting $G(K+1) := g_{K+1}^{(K)}$ and iterating the 5-step operator $T_k(g) := 1 + \frac{x}{D_1(k, g)} = 1 + \frac{x + x^2 + x^3 + x^4 g}{4k+1}$ from $k = K$ down to $k = 0$ (all intermediate denominators stay units in $\mathbb{Q}[[x]]^\times$ since $D_4 = \frac{1 + xg}{g}$ has constant term $1/g(0) \ne 0$, etc.). Since $T_k(g_1) - T_k(g_2) = \frac{x^4}{4k+1}(g_1 - g_2)$ for every $k \ge 0$, induction from $k = K$ down to $k = 0$ gives
$$G^{(K)}(0) - G(0) = \frac{x^{4(K+1)}}{\prod_{j=0}^{K}(4j+1)} \bigl(g_{K+1}^{(K)} - G(K+1)\bigr) \in x^{4K+4}\mathbb{Q}[[x]],$$
which refines to $x^{4K+5}\mathbb{Q}[[x]]$ whenever $g_{K+1}^{(K)} = 1 + O(x)$ (such as $g_{K+1}^{(K)} = 1$) because $G(K+1) = 1 + O(x)$. Letting $K \to \infty$ proves $x$-adic convergence $G^{(K)}(0) \to G(0)$ in $\mathbb{Q}[[x]]$, and hence $\frac{d}{dx}G^{(K)}(0) \to E(x) = \sum_{n=0}^{\infty} a(n+1)\frac{x^n}{n!}$. $\square$

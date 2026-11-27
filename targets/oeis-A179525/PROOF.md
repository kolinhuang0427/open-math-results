# Proof of OEIS A179525 Gladkovskii CF and Bala Even-Product Conjectures

We prove two open generating-function conjectures on [OEIS A179525](https://oeis.org/A179525) (rev. 74) in $\mathbb{Z}[[x]]$: Sergei N. Gladkovskii's May 13, 2013 continued fraction conjecture and Peter Bala's May 16, 2017 even-product generating function conjecture.

Throughout, set $q := 1 + x \in \mathbb{Z}[[x]]$. Since $q^j - 1 = (1+x)^j - 1 \in x\mathbb{Z}[[x]]$ for every $j \ge 1$, every product $\prod_{j=1}^n (q^{m+j} - 1)$ lies in $x^n\mathbb{Z}[[x]]$, so all infinite sums below converge $x$-adically in $\mathbb{Z}[[x]]$. In particular,
$$A(x) = \sum_{m=0}^{\infty} P_m, \qquad P_m := \prod_{k=1}^{m}(q^k - 1) \in x^m\mathbb{Z}[[x]] \quad (P_0 := 1).$$

## 1. Proof of Sergei N. Gladkovskii's Continued Fraction Conjecture

For every integer $k \ge 0$, define
$$Q(k) := \sum_{n=0}^{\infty} \prod_{j=1}^{n}\bigl(q^{2k+j} - 1\bigr) \in \mathbb{Z}[[x]].$$
Note that $Q(0) = A(x)$, and every $Q(k) = 1 + O(x)$ is a unit in $\mathbb{Z}[[x]]$.

**Lemma 1 (Two-step shift identity).** *For every integer $k \ge 0$,*
$$Q(k) = 1 + (q^{2k+1} - 1) + (q^{2k+1} - 1)(q^{2k+2} - 1)\, Q(k+1).$$

*Proof.* Splitting off the $n = 0$ term ($1$) and $n = 1$ term ($q^{2k+1} - 1$), and factoring $(q^{2k+1}-1)(q^{2k+2}-1)$ out of all $n \ge 2$ terms ($n = m + 2$, $j \mapsto j' + 2$) gives
$$Q(k) = 1 + (q^{2k+1} - 1) + (q^{2k+1} - 1)(q^{2k+2} - 1)\sum_{m=0}^{\infty}\prod_{j'=1}^{m}\bigl(q^{2(k+1)+j'}-1\bigr) = 1 + (q^{2k+1}-1) + (q^{2k+1}-1)(q^{2k+2}-1)\,Q(k+1). \qquad \square$$

**Theorem 1.** *For every integer $k \ge 0$, $Q(k)$ satisfies Gladkovskii's 3-step continued fraction recurrence*
$$Q(k) = 1 - \cfrac{1 - q^{2k+1}}{1 - \cfrac{1 - q^{2k+2}}{1 - q^{2k+2} - \frac{1}{Q(k+1)}}}$$
*in $\mathbb{Z}[[x]]$ (with all denominators units in $\mathbb{Z}[[x]]$). Moreover, for any truncation depth $K \ge 0$ and any seed $q_{K+1}^{(K)} = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ (such as $1$), the $K$-th finite convergent $Q^{(K)}(0)$ satisfies $Q^{(K)}(0) - A(x) \in x^{2K+3}\mathbb{Z}[[x]]$ (and $x^{2K+2}\mathbb{Z}[[x]]$ for any unit seed $q_{K+1}^{(K)} \in \mathbb{Z}[[x]]^\times$), so $Q^{(K)}(0) \to A(x)$ $x$-adically in $\mathbb{Z}[[x]]$.*

*Proof.* Fix $k \ge 0$ and write $a := 1 - q^{2k+1} = -(q^{2k+1}-1) \in x\mathbb{Z}[[x]]$, $b := 1 - q^{2k+2} = -(q^{2k+2}-1) \in x\mathbb{Z}[[x]]$, and $g := Q(k+1) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$. Evaluating from bottom to top in $\mathbb{Z}[[x]]$:

1. Inner denominator:
   $$D_2 := 1 - q^{2k+2} - \frac{1}{g} = b - \frac{1}{g} = \frac{b g - 1}{g} = -1 + O(x) \in \mathbb{Z}[[x]]^\times.$$
2. Outer denominator:
   $$D_1 := 1 - \frac{b}{D_2} = 1 - \frac{b g}{b g - 1} = \frac{-1}{b g - 1} = \frac{1}{1 - b g} = 1 + O(x) \in \mathbb{Z}[[x]]^\times.$$
3. Top level:
   $$1 - \frac{a}{D_1} = 1 - a(1 - b g) = 1 - a + a b\, g = 1 + (q^{2k+1}-1) + (q^{2k+1}-1)(q^{2k+2}-1)\,Q(k+1) = Q(k)$$
   by Lemma 1.

For convergence of finite truncations, set $T_k(g) := 1 - \frac{a}{1 - \frac{b}{b - 1/g}} = 1 - a + a b\, g$. Note that for any unit $g \in \mathbb{Z}[[x]]^\times$, $b - 1/g = -1/g(0) + O(x) \in \mathbb{Z}[[x]]^\times$ and $1 - b g = 1 + O(x) \in \mathbb{Z}[[x]]^\times$, so all denominators remain units and $T_k(g) = 1 + O(x)$. Since
$$T_k(g_1) - T_k(g_2) = (q^{2k+1} - 1)(q^{2k+2} - 1)(g_1 - g_2) \in x^2(g_1 - g_2)\mathbb{Z}[[x]],$$
iterating downward from $k = K$ to $k = 0$ with any unit seed $q_{K+1}^{(K)} \in \mathbb{Z}[[x]]^\times$ yields $Q^{(K)}(0) - Q(0) \in x^{2K+2}\mathbb{Z}[[x]]$, which improves to $x^{2K+3}\mathbb{Z}[[x]]$ when $q_{K+1}^{(K)} = 1 + O(x)$ (since $Q(K+1) = 1 + O(x)$). Letting $K \to \infty$ gives $Q^{(K)}(0) \to Q(0) = A(x)$ in $\mathbb{Z}[[x]]$. $\square$

## 2. Proof of Peter Bala's Even-Product Conjecture

**Theorem 2.** *In $\mathbb{Z}[[x]]$,*
$$A(x) = \sum_{n=0}^{\infty} (1 + x)^{2n+1} \prod_{k=1}^{2n}\bigl(1 - (1 + x)^k\bigr).$$

*Proof.* With $q = 1 + x$ and $P_m = \prod_{k=1}^m (q^k - 1)$, for every $n \ge 0$ the product has an even number $2n$ of factors, so $\prod_{k=1}^{2n}(1 - q^k) = (-1)^{2n} P_{2n} = P_{2n}$. Furthermore, $P_{2n+1} = (q^{2n+1} - 1) P_{2n}$, whence
$$q^{2n+1}\prod_{k=1}^{2n}(1 - q^k) = q^{2n+1} P_{2n} = P_{2n} + (q^{2n+1} - 1) P_{2n} = P_{2n} + P_{2n+1}.$$
Because $P_m \in x^m\mathbb{Z}[[x]]$, summing over $n \ge 0$ converges $x$-adically in $\mathbb{Z}[[x]]$ and regroups adjacent even and odd terms:
$$\sum_{n=0}^{\infty} q^{2n+1}\prod_{k=1}^{2n}(1 - q^k) = \sum_{n=0}^{\infty} (P_{2n} + P_{2n+1}) = \sum_{m=0}^{\infty} P_m = A(x). \qquad \square$$

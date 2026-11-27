# Proof of OEIS A167894 Continued Fraction Conjecture

We prove Sergei N. Gladkovskii's continued fraction conjecture on [OEIS A167894](https://oeis.org/A167894) (rev. 83) in $\mathbb{Z}[[x]]$.

## 1. Shifted Factorial Power Series $P_k(x)$

Define $P_{-1}(x) := 1$, and for each integer $k \ge 0$, define the formal power series
$$P_k(x) := \sum_{m=0}^{\infty} \frac{(k+m)!}{k!}\, x^m = 1 + (k+1)x + (k+1)(k+2)x^2 + \cdots \in \mathbb{Z}[[x]].$$
Note that $P_0(x) = \sum_{m=0}^{\infty} m!\, x^m$, so the generating function of OEIS A167894 is $A(x) = \frac{1}{P_0(x)} \in \mathbb{Z}[[x]]$, and every $P_k(x) = 1 + O(x)$ is a unit in $\mathbb{Z}[[x]]$.

**Lemma 1 (Shift identity).** *For every integer $k \ge 0$,*
$$P_{k-1}(x) = 1 + k x\, P_k(x).$$

*Proof.* For $k = 0$, $P_{-1}(x) = 1 = 1 + 0 \cdot x P_0(x)$. For $k \ge 1$,
$$1 + k x\, P_k(x) = 1 + \sum_{m=0}^{\infty} k \frac{(k+m)!}{k!}\, x^{m+1} = 1 + \sum_{m=0}^{\infty} \frac{(k+m)!}{(k-1)!}\, x^{m+1} = \sum_{r=0}^{\infty} \frac{(k-1+r)!}{(k-1)!}\, x^r = P_{k-1}(x). \qquad \square$$

## 2. Proof of the Continued Fraction Recurrence and Convergence

**Theorem.** *For every integer $k \ge 0$, define $Q(k) := \frac{P_{k-1}(x)}{P_k(x)} \in \mathbb{Z}[[x]]^\times$. Then $Q(0) = \frac{1}{P_0(x)} = A(x)$, and for every $k \ge 0$,*
$$Q(k) = 1 + k x - \frac{(k+1)x}{Q(k+1)}$$
*in $\mathbb{Z}[[x]]$. Moreover, for any truncation depth $K \ge 0$ and any seed $q_{K+1}^{(K)} = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ (such as $q_{K+1}^{(K)} = 1$), the $K$-th finite convergent $Q^{(K)}(0)$ satisfies $Q^{(K)}(0) - A(x) \in x^{K+2}\mathbb{Z}[[x]]$ (and $x^{K+1}\mathbb{Z}[[x]]$ for any unit seed $q_{K+1}^{(K)} \in \mathbb{Z}[[x]]^\times$), so $Q^{(K)}(0) \to A(x)$ $x$-adically in $\mathbb{Z}[[x]]$.*

*Proof.* At $k = 0$, $Q(0) = \frac{P_{-1}(x)}{P_0(x)} = \frac{1}{P_0(x)} = A(x)$. Fix $k \ge 0$. By Lemma 1 applied at $k + 1$, we have $(k + 1)x\, P_{k+1}(x) = P_k(x) - 1$. Substituting $Q(k+1) = \frac{P_k(x)}{P_{k+1}(x)}$ gives
$$1 + k x - \frac{(k+1)x}{Q(k+1)} = 1 + k x - \frac{(k+1)x\, P_{k+1}(x)}{P_k(x)} = 1 + k x - \frac{P_k(x) - 1}{P_k(x)} = k x + \frac{1}{P_k(x)} = \frac{1 + k x\, P_k(x)}{P_k(x)} = \frac{P_{k-1}(x)}{P_k(x)} = Q(k),$$
using Lemma 1 at $k$ in the penultimate equality.

For convergence of finite truncations, set $T_k(q) := 1 + k x - \frac{(k+1)x}{q}$. Note that if $q \in \mathbb{Z}[[x]]^\times$ (i.e., $q(0) = \pm 1$; more generally, over $\mathbb{Q}$, any $q \in \mathbb{Q}[[x]]^\times$ with $q(0) \ne 0$ also works), then $T_k(q)(0) = 1 \ne 0$, so $T_k(q) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ (respectively, $1 + x\mathbb{Q}[[x]] \subseteq \mathbb{Q}[[x]]^\times$) for every $k \ge 0$. For any $q_1, q_2 \in \mathbb{Z}[[x]]^\times$ (or $\mathbb{Q}[[x]]^\times$),
$$T_k(q_1) - T_k(q_2) = (k+1)x\,\frac{q_1 - q_2}{q_1 q_2}.$$
Because $q_1 q_2 \in \mathbb{Z}[[x]]^\times$, each application of $T_k$ raises the $x$-adic valuation $\mathrm{ord}_x(q_1 - q_2)$ by at least $1$. Starting from any unit seed $q_{K+1}^{(K)} \in \mathbb{Z}[[x]]^\times$ and iterating $q_k^{(K)} = T_k(q_{k+1}^{(K)})$ down to $k = 0$ therefore yields
$$\mathrm{ord}_x\bigl(Q^{(K)}(0) - Q(0)\bigr) \ge (K + 1) + \mathrm{ord}_x\bigl(q_{K+1}^{(K)} - Q(K+1)\bigr) \ge K + 1,$$
and when $q_{K+1}^{(K)} = 1 + O(x)$ (such as $q_{K+1}^{(K)} = 1$), since $Q(K+1) = 1 + O(x)$ we have $\mathrm{ord}_x(q_{K+1}^{(K)} - Q(K+1)) \ge 1$ and hence $Q^{(K)}(0) - A(x) \in x^{K+2}\mathbb{Z}[[x]]$. Letting $K \to \infty$ gives $Q^{(K)}(0) \to A(x)$ in $\mathbb{Z}[[x]]$. $\square$

# Proof of OEIS A188458 Continued Fraction Conjecture

We prove Sergei N. Gladkovskii's Nov 12, 2013 continued fraction conjecture on [OEIS A188458](https://oeis.org/A188458) (rev. 54) in $\mathbb{Z}[[x]]$.

## 1. Reduction of the Ordinary Generating Function to $\mathrm{sech}(t)$

Let $(a(n))_{n \ge 0}$ be defined by $\sum_{n=0}^{\infty} a(n)\frac{t^n}{n!} = \frac{e^t}{\cosh(2t)}$ in $\mathbb{Q}[[t]]$, and let $E_{2m} \in \mathbb{Z}$ ($m \ge 0$) be the Euler (secant) numbers defined by
$$\mathrm{sech}(t) = \frac{1}{\cosh(t)} = \sum_{m=0}^{\infty} E_{2m} \frac{t^{2m}}{(2m)!}.$$
(Because $\cosh(t) = \sum_{r=0}^{\infty}\frac{t^{2r}}{(2r)!}$ is an even series with constant term $1$, $\mathrm{sech}(t)$ is an even series in $\mathbb{Q}[[t]]$ whose odd Taylor coefficients vanish.) Multiplying $\mathrm{sech}(2t) = \sum_{m=0}^{\infty} E_{2m} 2^{2m} \frac{t^{2m}}{(2m)!}$ by $e^t = \sum_{j=0}^{\infty}\frac{t^j}{j!}$ yields
$$a(n) = \sum_{m=0}^{\lfloor n/2 \rfloor} \binom{n}{2m} 2^{2m} E_{2m} \qquad (n \ge 0).$$

**Lemma 1 (Binomial transform in o.g.f.).** *Let $F(x) := \sum_{n=0}^{\infty} a(n) x^n \in \mathbb{Z}[[x]]$ be the ordinary generating function of $(a(n))_{n \ge 0}$, and let $S(u) := \sum_{m=0}^{\infty} E_{2m} u^{2m} \in \mathbb{Z}[[u^2]]$. Setting $u := \frac{2x}{1-x} \in x\mathbb{Q}[[x]]$, we have*
$$F(x) = \frac{1}{1 - x}\, S\!\left(\frac{2x}{1 - x}\right).$$

*Proof.* Expanding $(1 - x)^{-(2m+1)} = \sum_{r=0}^{\infty} \binom{2m+r}{2m} x^r$ in $\mathbb{Z}[[x]]$ and substituting $n = 2m + r$ gives
$$\frac{1}{1-x}\, S\!\left(\frac{2x}{1-x}\right) = \sum_{m=0}^{\infty} E_{2m} \frac{(2x)^{2m}}{(1-x)^{2m+1}} = \sum_{m=0}^{\infty} E_{2m} (2x)^{2m} \sum_{r=0}^{\infty}\binom{2m+r}{2m} x^r = \sum_{n=0}^{\infty}\left(\sum_{m=0}^{\lfloor n/2 \rfloor}\binom{n}{2m} 2^{2m} E_{2m}\right) x^n = F(x). \qquad \square$$

## 2. Self-Contained Continued Fraction for $S(u)$

Let $\mathcal{L} : \mathbb{Q}[[t]] \to \mathbb{Q}[[u]]$ denote the formal Laplace operator defined on $g(t) = \sum_{n=0}^{\infty} g_n \frac{t^n}{n!} \in \mathbb{Q}[[t]]$ by
$$\mathcal{L}(g)(u) := \sum_{n=0}^{\infty} g_n u^n \in \mathbb{Q}[[u]].$$
Since $(g')_n = g_{n+1}$, $\mathcal{L}$ satisfies the fundamental differentiation rule
$$\mathcal{L}(g')(u) = \sum_{n=0}^{\infty} g_{n+1} u^n = \frac{\mathcal{L}(g)(u) - g(0)}{u}.$$
Note that $S(u) = \mathcal{L}(\mathrm{sech})(u)$.

For each integer $k \ge 0$, define $f_k(t) := \tanh^k(t)\,\mathrm{sech}(t) \in \mathbb{Q}[[t]]$ and $J_k(u) := \mathcal{L}(f_k)(u) \in \mathbb{Q}[[u]]$. Since $\tanh(t) = t + O(t^3)$ and $\mathrm{sech}(t) = 1 + O(t^2)$, we have $f_k(t) = t^k + O(t^{k+2})$, so $J_k(u) = k!\, u^k + O(u^{k+2})$; in particular, $f_0(0) = 1$ and $f_k(0) = 0$ for all $k \ge 1$.

**Lemma 2 (Differential-Laplace chain).** *Define $T_0(u) := J_0(u) = S(u)$, and for each integer $k \ge 1$ define $T_k(u) := \frac{J_k(u)}{k u\, J_{k-1}(u)} = 1 + O(u^2) \in \mathbb{Q}[[u]]^\times$. Then for every integer $k \ge 0$,*
$$T_k(u) = \frac{1}{1 + (k+1)^2 u^2\, T_{k+1}(u)}.$$

*Proof.* Using $\frac{d}{dt}\mathrm{sech}(t) = -\tanh(t)\mathrm{sech}(t)$ and $\frac{d}{dt}\tanh(t) = 1 - \tanh^2(t) = \mathrm{sech}^2(t)$:
- For $k = 0$: $f_0'(t) = -f_1(t)$ with $f_0(0) = 1$, so applying $\mathcal{L}$ gives $\frac{J_0(u) - 1}{u} = -J_1(u)$, i.e.,
  $$J_0(u)\left(1 + u\,\frac{J_1(u)}{J_0(u)}\right) = 1 \implies T_0(u) = \frac{1}{1 + 1^2 u^2\, T_1(u)}.$$
- For $k \ge 1$:
  $$f_k'(t) = k\tanh^{k-1}(t)(1 - \tanh^2(t))\mathrm{sech}(t) - \tanh^{k+1}(t)\mathrm{sech}(t) = k f_{k-1}(t) - (k+1) f_{k+1}(t).$$
  Since $f_k(0) = 0$, applying $\mathcal{L}$ gives $\frac{J_k(u)}{u} = k J_{k-1}(u) - (k+1) J_{k+1}(u)$. Rearranging as $k u\, J_{k-1}(u) = J_k(u)\bigl(1 + (k+1)u\,\frac{J_{k+1}(u)}{J_k(u)}\bigr)$ and dividing by $J_k(u)$ gives
  $$\frac{1}{T_k(u)} = \frac{k u\, J_{k-1}(u)}{J_k(u)} = 1 + (k+1)^2 u^2\, T_{k+1}(u) \implies T_k(u) = \frac{1}{1 + (k+1)^2 u^2\, T_{k+1}(u)}. \qquad \square$$

## 3. Equivalence with Gladkovskii's Continued Fraction

**Theorem.** *For each $k \ge 0$, substitute $u = \frac{2x}{1-x} \in x\mathbb{Q}[[x]]$ and set $\widetilde{T}_k(x) := T_k\!\left(\frac{2x}{1-x}\right) = 1 + O(x^2) \in \mathbb{Q}[[x]]^\times$. Then $F(x) = \frac{\widetilde{T}_0(x)}{1-x}$, and for every $k \ge 0$,*
$$\widetilde{T}_k(x) = 1 - \frac{4x^2(k+1)^2}{4x^2(k+1)^2 + \frac{(1-x)^2}{\widetilde{T}_{k+1}(x)}}.$$
*Furthermore, for any depth $K \ge 0$ and any seed $t_{K+1}^{(K)} = 1 + O(x) \in \mathbb{Q}[[x]]^\times$ (such as $1$), the finite convergent $\widetilde{T}^{(K)}(0)$ satisfies $\widetilde{T}^{(K)}(0) - \widetilde{T}_0(x) \in x^{2K+3}\mathbb{Q}[[x]]$ (and $x^{2K+4}\mathbb{Q}[[x]]$ if $t_{K+1}^{(K)} = 1 + O(x^2)$), so $\frac{\widetilde{T}^{(K)}(0)}{1-x} \to F(x)$ $x$-adically in $\mathbb{Z}[[x]]$.*

*Proof.* By Lemma 1, $F(x) = \frac{1}{1-x}S\!\left(\frac{2x}{1-x}\right) = \frac{\widetilde{T}_0(x)}{1-x}$. For any $k \ge 0$, write $A := 4x^2(k+1)^2$ and $B := (1-x)^2$. Since $\widetilde{T}_{k+1}(x) = 1 + O(x^2) \in \mathbb{Q}[[x]]^\times$ and $B = 1 - 2x + x^2 \in \mathbb{Q}[[x]]^\times$, the denominator $A + B/\widetilde{T}_{k+1}(x) = 1 + O(x)$ is a unit in $\mathbb{Q}[[x]]$. Using $u^2 = A/B$ and Lemma 2:
$$1 - \frac{A}{A + B/\widetilde{T}_{k+1}(x)} = \frac{B/\widetilde{T}_{k+1}(x)}{A + B/\widetilde{T}_{k+1}(x)} = \frac{1}{1 + (A/B)\widetilde{T}_{k+1}(x)} = \frac{1}{1 + (k+1)^2 u^2\, \widetilde{T}_{k+1}(x)} = \widetilde{T}_k(x).$$

For convergence of finite truncations, set $\Phi_k(t) := 1 - \frac{A}{A + B/t} = \frac{1}{1 + (k+1)^2 u^2 t}$. For any $t = 1 + O(x) \in \mathbb{Q}[[x]]^\times$, $\Phi_k(t) = 1 + O(x^2) \in \mathbb{Q}[[x]]^\times$. For any two $t_1, t_2 = 1 + O(x)$,
$$\Phi_k(t_1) - \Phi_k(t_2) = -\frac{(k+1)^2 u^2 (t_1 - t_2)}{(1 + (k+1)^2 u^2 t_1)(1 + (k+1)^2 u^2 t_2)},$$
which raises the $x$-adic valuation by at least $2$ (since $\mathrm{ord}_x(u^2) = 2$ and the denominator is $1 + O(x^2)$). Iterating from $k = K$ down to $k = 0$ with seed $t_{K+1}^{(K)} = 1 + O(x)$ gives $\mathrm{ord}_x(\widetilde{T}^{(K)}(0) - \widetilde{T}_0(x)) \ge 2(K+1) + \mathrm{ord}_x(t_{K+1}^{(K)} - \widetilde{T}_{K+1}(x)) \ge 2K + 3$ (and $2K + 4$ when $t_{K+1}^{(K)} = 1 + O(x^2)$, e.g. $t_{K+1}^{(K)} = 1$). Dividing by $1 - x \in \mathbb{Q}[[x]]^\times$ yields $\frac{\widetilde{T}^{(K)}(0)}{1-x} \to F(x)$ $x$-adically in $\mathbb{Q}[[x]]$. $\square$

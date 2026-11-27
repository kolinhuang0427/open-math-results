# Counterexamples to `kallat-2610.40342-ques14.8`

**Verdict:** **FALSE** (refuted by explicit non-constant counterexamples for both signs $+$ and $-$, as well as constant-residue families).

In `arXiv:2610.40342v1` (`Section 14`, Question 14.8 `\label{prob:composite}`), for any set $A \subseteq \mathbb{N}$ of allowed cycle lengths and any prime $p$ of type II for $A$ (meaning $[1 \in A] \ne [p \in A]$ by Definition 13.1 `\label{def:types}`), it is asked whether the least period $\varpi(p^e)$ of $a_A(n) \bmod p^e$ is always $p^e$ (or $2p^e$ when the sign in Lemma 13.2(a) `\label{lem:typeB}` is $-$).

Below we give **three independent, non-constant counterexamples** covering odd $p$ with sign $+$, odd $p$ with sign $-$, and $p=2$ with sign $+$, each proved unconditionally for all $n \ge 0$, together with a constant-residue infinite family.

---

## 1. Non-constant counterexample with odd $p$ and sign $+$ ($A = \{1, 7\}$, $p = 3$, $e = 3$)

Let $A = \{1, 7\}$, $p = 3$, and $e = 3$ ($p^e = 27$).
- Since $1 \in A$ and $3 \notin A$, $p = 3$ is of **type II** for $A$, and Lemma 13.2(a) assigns the **$+$** sign (predicted least period $3^3 = 27$).
- From the exponential generating function $\sum_{n \ge 0} a_{\{1,7\}}(n) \frac{x^n}{n!} = \exp\!\left(x + \frac{x^7}{7}\right)$, extracting the coefficient of $x^n/n!$ gives, for every $n \ge 0$,
  $$a_{\{1,7\}}(n) = \sum_{j=0}^{\lfloor n/7 \rfloor} \binom{n}{7j} \frac{(7j)!}{7^j\, j!}.$$
- For every integer $j \ge 2$, since $\lfloor 7j/3^i \rfloor \ge \lfloor j/3^i \rfloor$ for all $i \ge 1$, Legendre's formula yields
  $$v_3\!\left(\frac{(7j)!}{7^j\, j!}\right) = \sum_{i \ge 1} \left(\left\lfloor \frac{7j}{3^i} \right\rfloor - \left\lfloor \frac{j}{3^i} \right\rfloor\right) \ge \left\lfloor \frac{7j}{3} \right\rfloor - \left\lfloor \frac{j}{3} \right\rfloor \ge \left\lfloor \frac{6j}{3} \right\rfloor = 2j \ge 4 > 3.$$
  Hence every term with $j \ge 2$ is divisible by $27$.
- For $j = 0$, the term is $1$. For $j = 1$, $\frac{7!}{7 \cdot 1!} = 6! = 720 \equiv 18 \equiv -9 \pmod{27}$, so
  $$a_{\{1,7\}}(n) \equiv 1 - 9\binom{n}{7} \pmod{27} \qquad \text{for all } n \ge 0.$$
- Because $7 = 2 \cdot 3^1 + 1 \cdot 3^0 < 9$, Lucas's theorem modulo $3$ implies that $\binom{n}{7} \bmod 3$ depends only on $n \bmod 9$:
  $$\binom{n}{7} \equiv \begin{cases} 1 \pmod{3} & \text{if } n \equiv 7 \pmod{9}, \\ 2 \pmod{3} & \text{if } n \equiv 8 \pmod{9}, \\ 0 \pmod{3} & \text{otherwise.} \end{cases}$$
- Therefore $a_{\{1,7\}}(n) \bmod 27$ is purely periodic with repeating 9-term block $(1, 1, 1, 1, 1, 1, 1, 19, 10)$. Since $1, 19, 10$ are distinct modulo $27$ and only $n \equiv 7, 8 \pmod 9$ differ from $1$, the **exact least period** is $\varpi(27) = 9 = 3^2 < 27$.

---

## 2. Non-constant counterexample with odd $p$ and sign $-$ ($A = \{5\}$, $p = 5$, $e = 2$)

Let $A = \{5\}$, $p = 5$, and $e = 2$ ($p^e = 25$).
- Since $1 \notin A$ and $5 \in A$, $p = 5$ is of **type II** for $A$, and Lemma 13.2(a) assigns the **$-$** sign (predicted least period $2 \cdot 5^2 = 50$).
- From $\sum_{n \ge 0} a_{\{5\}}(n) \frac{x^n}{n!} = \exp(x^5/5)$, we have $a_{\{5\}}(n) = 0$ whenever $5 \nmid n$, and for $n = 5k$ ($k \ge 0$),
  $$a_{\{5\}}(5k) = \frac{(5k)!}{5^k\, k!} = \prod_{j=0}^{k-1} (5j+1)(5j+2)(5j+3)(5j+4).$$
- For every integer $j \ge 0$,
  $$(5j+1)(5j+4) = 25j(j+1) + 4 \equiv 4 \pmod{25}, \qquad (5j+2)(5j+3) = 25j(j+1) + 6 \equiv 6 \pmod{25},$$
  so each factor equals $4 \cdot 6 = 24 \equiv -1 \pmod{25}$ independently of $j$.
- Thus $a_{\{5\}}(5k) \equiv (-1)^k \pmod{25}$ for all $k \ge 0$, and $a_{\{5\}}(n) \bmod 25$ repeats with the 10-term block $(1, 0, 0, 0, 0, 24, 0, 0, 0, 0)$. Its **exact least period** is $\varpi(25) = 10 < 50$.
- (More generally, for every odd prime $p$ and $A = \{p\}$, pairing $(pj+t)(pj+p-t) = p^2 j(j+1) + t(p-t)$ gives $\prod_{t=1}^{p-1}(pj+t) \equiv (p-1)! \pmod{p^2}$; thus for every Wilson prime $p \in \{5, 13, 563\}$, $(p-1)! \equiv -1 \pmod{p^2}$ yields $a_{\{p\}}(pk) \equiv (-1)^k \pmod{p^2}$ and least period $2p < 2p^2$.)

---

## 3. Non-constant counterexample at $p = 2$ ($A = \{2, 4\}$, $p = 2$, $e = 2$)

Let $A = \{2, 4\}$, $p = 2$, and $e = 2$ ($p^e = 4$).
- Since $1 \notin A$ and $2 \in A$, $p = 2$ is of **type II** for $A$, and Lemma 13.2(a) assigns the sign $(-1)^{[2\in A]+[4\in A]} = (-1)^{1+1} = +1$ (predicted least period $2^2 = 4$).
- Because every element of $A$ is even, $a_{\{2,4\}}(n) = 0$ for all odd $n \ge 1$.
- For even $n = 2m$, the cycle-of-$n$ recurrence (equation `(1.2)` `\label{eq:last0}`) specializes to $a(0) = 1$, $a(2) = 1$, and for $m \ge 2$,
  $$a(2m) = (2m-1)\,a(2m-2) + (2m-1)(2m-2)(2m-3)\,a(2m-4).$$
- We prove by induction on $m \ge 0$ that $a(2m) \equiv 1 \pmod 4$. Base cases $m = 0, 1$ hold ($1 \equiv 1 \pmod 4$). For $m \ge 2$, assuming $a(2m-2) \equiv a(2m-4) \equiv 1 \pmod 4$:
  - If $m$ is odd, then $2m-1 \equiv 1 \pmod 4$ and $4 \mid (2m-2)$, so $a(2m) \equiv 1 \cdot 1 + 0 \equiv 1 \pmod 4$.
  - If $m$ is even, then $2m-1 \equiv 3 \pmod 4$, $2m-2 \equiv 2 \pmod 4$, and $2m-3 \equiv 1 \pmod 4$, so $(2m-1)(2m-2)(2m-3) \equiv 3 \cdot 2 \cdot 1 \equiv 2 \pmod 4$, hence $a(2m) \equiv 3 \cdot 1 + 2 \cdot 1 = 5 \equiv 1 \pmod 4$.
- Thus $a_{\{2,4\}}(n) \bmod 4$ is the alternating sequence $(1, 0, 1, 0, \dots)$ with **exact least period** $\varpi(4) = 2 < 4$.

---

## 4. Constant-residue families ($\varpi(p^e) = 1 < p^e$)

For completeness, for any prime $p$ and any $e \ge 1$, both the singleton set $A = \{1\}$ (i.e. $A_{\le 1}$, where $a_{\{1\}}(n) = 1$ for all $n \ge 0$) and any two-element set $A = \{1, M\}$ with $p \nmid M$ and $M \ge p^e + 1$ (since $v_p((Mj)!/(M^j j!)) \ge \sum_{i=1}^e (\lfloor Mj/p^i \rfloor - \lfloor j/p^i \rfloor) \ge \sum_{i=1}^e p^{e-i}j = \frac{p^e-1}{p-1}j \ge ej \ge e$ for all $j \ge 1$, e.g. $A = \{1, 10\}$ for $p = 3, e = 3$) have $p$ of type II and satisfy $a_A(n) \equiv 1 \pmod{p^e}$ for all $n \ge 0$, giving least period $\varpi(p^e) = 1 < p^e$.

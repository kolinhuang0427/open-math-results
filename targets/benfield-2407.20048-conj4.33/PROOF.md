# Proof of Benfield–Lippard `arXiv:2407.20048v2` Conjecture 4.33 (`\label{even-K-exceptions}`)

**Result:** **TRUE** (complete elementary proof for all even integers $K \in \mathbb{Z}$ and all integers $m > 3$).

---

## Setup and Notation

For any integer $K$, the $K$-Fibonacci sequence $(F_{K,n})_{n \ge 0}$ is defined by $F_{K,0} = 0$, $F_{K,1} = 1$, and $F_{K,n} = K F_{K,n-1} + F_{K,n-2}$ for $n \ge 2$ (and we set $F_{K,-1} = 1$, matching $F_{K,1} = K F_{K,0} + F_{K,-1}$). Define the companion $K$-Lucas sequence by $L_{K,0} = 2$, $L_{K,1} = K$, and $L_{K,n} = K L_{K,n-1} + L_{K,n-2}$ for $n \ge 2$.

Let $U = \begin{pmatrix} K & 1 \\ 1 & 0 \end{pmatrix} \in M_2(\mathbb{Z})$. By induction on $n \ge 0$,
$$U^n = \begin{pmatrix} F_{K,n+1} & F_{K,n} \\ F_{K,n} & F_{K,n-1} \end{pmatrix}.$$
Since $\det(U) = -1$, we have $\det(U^n) = F_{K,n+1} F_{K,n-1} - F_{K,n}^2 = (-1)^n$ for all $n \ge 0$, and $(U^n \bmod m)_{n \ge 0}$ is purely periodic for every modulus $m \ge 2$. Let $\pi_K(m) \ge 1$ be the minimal period of $(F_{K,n} \bmod m)_{n \ge 0}$, $\alpha_K(m) \ge 1$ be the rank (smallest $n \ge 1$ with $m \mid F_{K,n}$), and $\omega_K(m)$ be the number of indices $0 \le n < \pi_K(m)$ with $m \mid F_{K,n}$.

We give a completely self-contained proof (noting in passing that the proof of Theorem 4.29 `\label{omega-even-K}` in `fiborder.tex` contains a minor typo writing $\mathrm{lcm}[1, \cdot]$ instead of $\mathrm{lcm}[2, \cdot]$, which fails when $m = 2n$ with $\alpha_K(n)$ odd, e.g., $K=2, m=10$; our proof avoids relying on it).

---

## Lemma 1 (Period, Rank, Order, and LCM Relations)

For every $K \in \mathbb{Z}$ and $m \ge 2$:
1. $n > 0$ satisfies $U^n \equiv I \pmod m$ if and only if $\pi_K(m) \mid n$.
2. $n \ge 0$ satisfies $m \mid F_{K,n}$ if and only if $\alpha_K(m) \mid n$.
3. Letting $\alpha = \alpha_K(m)$ and $\beta = F_{K,\alpha+1}$, we have $\beta^2 \equiv (-1)^\alpha \pmod m$, $\omega_K(m) = \mathrm{ord}_m(\beta) \in \{1, 2, 4\}$, and $\pi_K(m) = \alpha_K(m)\,\omega_K(m)$.
4. For any $a, b \ge 2$, $\alpha_K(\mathrm{lcm}(a,b)) = \mathrm{lcm}(\alpha_K(a), \alpha_K(b))$ and $\pi_K(\mathrm{lcm}(a,b)) = \mathrm{lcm}(\pi_K(a), \pi_K(b))$.

*Proof.*
1. $U^n \equiv I \pmod m$ means $(F_{K,n}, F_{K,n+1}) \equiv (0, 1) \pmod m$ (since $F_{K,n-1} = F_{K,n+1} - K F_{K,n} \equiv 1 \pmod m$), which is equivalent to $n$ being a period of $(F_{K,k} \bmod m)_{k \ge 0}$, hence to $\pi_K(m) \mid n$.
2. Since $F_{K,\alpha} \equiv 0 \pmod m$, we have $F_{K,\alpha-1} = F_{K,\alpha+1} - K F_{K,\alpha} \equiv \beta \pmod m$, so $U^\alpha \equiv \beta I \pmod m$. Taking determinants gives $\beta^2 \equiv \det(U^\alpha) = (-1)^\alpha \pmod m$, so $\beta \in (\mathbb{Z}/m\mathbb{Z})^\times$ and $\beta^4 \equiv 1 \pmod m$. For any $n = q\alpha + r$ ($q \ge 0$, $0 \le r < \alpha$), $U^n \equiv \beta^q U^r \pmod m$, so $F_{K,n} \equiv \beta^q F_{K,r} \pmod m$. Because $\beta$ is a unit modulo $m$ and $0 \le r < \alpha$, $m \mid F_{K,n} \iff m \mid F_{K,r} \iff r = 0 \iff \alpha \mid n$.
3. By (2), every zero modulo $m$ is of the form $q\alpha$ ($q \ge 0$), where $U^{q\alpha} \equiv \beta^q I \pmod m$. Thus $U^{q\alpha} \equiv I \pmod m \iff \mathrm{ord}_m(\beta) \mid q$. Hence $\pi_K(m) = \alpha \cdot \mathrm{ord}_m(\beta)$, and the number of zeros in $[0, \pi_K(m))$ is $\omega_K(m) = \mathrm{ord}_m(\beta)$, which divides $4$ because $\beta^4 \equiv 1 \pmod m$.
4. $\mathrm{lcm}(a,b) \mid F_{K,n} \iff (a \mid F_{K,n} \text{ and } b \mid F_{K,n}) \iff (\alpha_K(a) \mid n \text{ and } \alpha_K(b) \mid n) \iff \mathrm{lcm}(\alpha_K(a), \alpha_K(b)) \mid n$, giving $\alpha_K(\mathrm{lcm}(a,b)) = \mathrm{lcm}(\alpha_K(a), \alpha_K(b))$. Replacing $m \mid F_{K,n}$ by $U^n \equiv I \pmod m$ yields $\pi_K(\mathrm{lcm}(a,b)) = \mathrm{lcm}(\pi_K(a), \pi_K(b))$. $\square$

---

## Lemma 2 (Odd Moduli $n \ge 3$)

Let $K \in \mathbb{Z}$ and let $n \ge 3$ be **odd**. Then all three claims hold for modulus $n$:
1. $\omega_K(n) = 4 \iff \alpha_K(n) \equiv \pm 1 \pmod 4$.
2. If $\omega_K(n) = 2$, then $4 \mid \pi_K(n)$ and $2 \mid \alpha_K(n)$.
3. If $4 \nmid \pi_K(n)$, then $\omega_K(n) = 1$.

*Proof.*
Let $\alpha = \alpha_K(n)$, $\pi = \pi_K(n)$, $\omega = \omega_K(n)$, and $\beta = F_{K,\alpha+1}$. Since $n \ge 3$ is odd, $-1 \not\equiv 1 \pmod n$.
- **Claim (1):** By Lemma 1(3), $\omega = \mathrm{ord}_n(\beta) \in \{1, 2, 4\}$ and $\beta^2 \equiv (-1)^\alpha \pmod n$. Thus $\omega = 4 \iff \beta^2 \not\equiv 1 \pmod n \iff (-1)^\alpha = -1 \iff \alpha$ is odd $\iff \alpha \equiv \pm 1 \pmod 4$.
- **Claim (2):** Suppose $\omega = 2$. By Claim (1), $\alpha$ cannot be odd, so $2 \mid \alpha$. Hence $4 \mid 2\alpha = \pi$.
- **Claim (3):** By contrapositive, we show that if $\omega \in \{2, 4\}$, then $4 \mid \pi$. If $\omega = 4$, then $4 \mid 4\alpha = \pi$. If $\omega = 2$, Claim (2) gives $4 \mid \pi$. Thus $4 \nmid \pi \implies \omega = 1$. $\square$

---

## Lemma 3 (Powers of $2$ for Even $K$)

Let $K \in \mathbb{Z}$ be **even**. Then for every integer $x \ge 1$, $\omega_K(2^x) = 1$ and $\pi_K(2^x) = \alpha_K(2^x) = 2^{a}$ for some integer $a \ge 1$.

*Proof.*
First, note that $F_{K,n+1} + F_{K,n-1} = L_{K,n}$ for all $n \ge 0$ (both satisfy the recurrence $X_n = K X_{n-1} + X_{n-2}$ with initial values $X_0 = 2, X_1 = K$). Comparing the $(1,2)$-entry of $U^{2r} = U^r \cdot U^r$ gives
$$F_{K,2r} = F_{K,r}(F_{K,r+1} + F_{K,r-1}) = F_{K,r} L_{K,r} \qquad (r \ge 1).$$
Also, since $2 \mid L_{K,0}$ and $2 \mid K = L_{K,1}$, induction gives $2 \mid L_{K,n}$ for all $n \ge 0$. By the $2 \times 2$ Cayley–Hamilton relation $\mathrm{tr}(A^2) = (\mathrm{tr} A)^2 - 2\det A$ applied to $A = U^r$,
$$L_{K,2r} = \mathrm{tr}(U^{2r}) = L_{K,r}^2 - 2(-1)^r \equiv 2 \pmod 4 \qquad \text{for every } r \ge 1.$$
Hence $\nu_2(L_{K,2s}) = 1$ for every $s \ge 1$.

Now we induct on $x \ge 1$:
- **Base case $x = 1$:** Since $K$ is even, $F_{K,0} = 0, F_{K,1} = 1, F_{K,2} = K \equiv 0 \pmod 2, F_{K,3} = K^2+1 \equiv 1 \pmod 2$. Thus $\pi_K(2) = \alpha_K(2) = 2 = 2^1$ and $\omega_K(2) = 1$.
- **Inductive step ($x \to x+1$, $x \ge 1$):** Assume $\pi_K(2^x) = \alpha_K(2^x) = 2^a$ with $a \ge 1$. Write $U^{2^a} = I + 2^x M$ for some $M \in M_2(\mathbb{Z})$. Squaring yields
  $$U^{2^{a+1}} = I + 2^{x+1} M + 2^{2x} M^2 \equiv I \pmod{2^{x+1}}$$
  because $2x \ge x+1$ for $x \ge 1$. By Lemma 1(1), $\pi_K(2^{x+1}) \mid 2^{a+1}$. Meanwhile, by definition and Lemma 1(2), $2^a = \alpha_K(2^x) \mid \alpha_K(2^{x+1}) \mid \pi_K(2^{x+1}) \mid 2^{a+1}$. Thus $\alpha_K(2^{x+1}) \in \{2^a, 2^{a+1}\}$.
  - If $\alpha_K(2^{x+1}) = 2^{a+1}$, then $\pi_K(2^{x+1}) = 2^{a+1}$ and $\omega_K(2^{x+1}) = 1$.
  - If $\alpha_K(2^{x+1}) = 2^a$:
    - When $a = 1$, $2^{x+1} \mid F_{K,2} = K$, so $F_{K,3} = K^2 + 1 \equiv 1 \pmod{2^{x+1}}$, whence $\pi_K(2^{x+1}) = 2 = 2^a$ and $\omega_K(2^{x+1}) = 1$.
    - When $a \ge 2$, let $r = 2^{a-1}$, which is even ($r = 2s$ with $s = 2^{a-2} \ge 1$). Then $2^{x+1} \mid F_{K,2r} = F_{K,r} L_{K,r}$. Since $\nu_2(L_{K,r}) = 1$, this forces $2^x \mid F_{K,r}$, contradicting $\alpha_K(2^x) = 2^a = 2r$.

This completes the induction. $\square$

---

## Proof of Conjecture 4.33 (`\label{even-K-exceptions}`)

Let $K \in \mathbb{Z}$ be even and let $m > 3$ be an integer. Write $m = 2^x n$ with $x \ge 0$ and $n \ge 1$ odd.

- **Case 1: $x = 0$ ($m = n > 3$ is odd).** All three claims hold immediately by Lemma 2.

- **Case 2: $x \ge 1$ and $n = 1$ ($m = 2^x \ge 4$).** By Lemma 3, $\omega_K(m) = 1$ and $\alpha_K(m) = \pi_K(m) = 2^a$ with $a \ge 1$.
  1. $\omega_K(m) = 1 \neq 4$, and $\alpha_K(m) = 2^a$ is even so $\alpha_K(m) \not\equiv \pm 1 \pmod 4$.
  2. $\omega_K(m) = 1 \neq 2$, so the implication is vacuously true.
  3. Since $\omega_K(m) = 1$, the implication "$4 \nmid \pi_K(m) \implies \omega_K(m) = 1$" holds.

- **Case 3: $x \ge 1$ and $n \ge 3$ is odd.** By Lemma 1(4) and Lemma 3 (with $\pi_K(2^x) = \alpha_K(2^x) = 2^a$, $a \ge 1$),
  $$\alpha_K(m) = \mathrm{lcm}\bigl(2^a, \alpha_K(n)\bigr), \qquad \pi_K(m) = \mathrm{lcm}\bigl(2^a, \pi_K(n)\bigr).$$
  First, $2 \mid 2^a \mid \alpha_K(m)$, so $\alpha_K(m)$ is always even and $\alpha_K(m) \not\equiv \pm 1 \pmod 4$.
  Next, by Lemma 1(3), $\omega_K(n) \in \{1, 2, 4\}$. Let $v = \nu_2(\alpha_K(n)) \ge 0$. Since $\pi_K(n) = \omega_K(n)\alpha_K(n)$ and $\omega_K(n) \in \{1, 2, 4\}$, comparing $2$-adic valuations gives
  $$\omega_K(m) = \frac{\pi_K(m)}{\alpha_K(m)} = 2^{\max(a,\, v + \nu_2(\omega_K(n))) - \max(a,\, v)}.$$
  We examine the three possibilities for $\omega_K(n)$:
  - **Subcase $\omega_K(n) = 1$:** Here $\nu_2(\omega_K(n)) = 0$, so $\omega_K(m) = 1$. Thus $\omega_K(m) \neq 4$ (matching $\alpha_K(m) \not\equiv \pm 1 \pmod 4$), $\omega_K(m) \neq 2$, and the third implication holds.
  - **Subcase $\omega_K(n) = 2$:** By Lemma 2(2), $v \ge 1$ ($2 \mid \alpha_K(n)$) and $4 \mid \pi_K(n) \mid \pi_K(m)$.
    - If $a \le v$, then $\max(a, v+1) - \max(a, v) = 1$, so $\omega_K(m) = 2$; and indeed $4 \mid \pi_K(m)$ and $2 \mid \alpha_K(m)$.
    - If $a > v$, then $\max(a, v+1) - \max(a, v) = 0$, so $\omega_K(m) = 1$.
    In both cases all three claims hold.
  - **Subcase $\omega_K(n) = 4$:** By Lemma 2(1), $\alpha_K(n)$ is odd, so $v = 0$ and $\nu_2(\pi_K(n)) = 2$ (hence $4 \mid \pi_K(n) \mid \pi_K(m)$).
    - If $a = 1$, then $\omega_K(m) = 2^{\max(1, 2) - 1} = 2$, and $4 \mid \pi_K(m)$ and $2 \mid \alpha_K(m)$.
    - If $a \ge 2$, then $\omega_K(m) = 2^{a - a} = 1$.
    In both cases all three claims hold.

In every case ($x=0$, $n=1$, and $x \ge 1, n \ge 3$), all three assertions of Conjecture 4.33 hold for all even $K \in \mathbb{Z}$ and all integers $m > 3$. $\blacksquare$

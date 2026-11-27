# Refutation of Benfield–Lippard `arXiv:2407.20048v2` Conjecture 5.3, Clause (vi) (`\label{finite-orders}`)

**Result:** **FALSE** (complete proof and exact arithmetic verification refuting **clause (vi)** of Conjecture 5.3).

> **Prior-result acknowledgment (no novelty claim on clause (v)):** Clause (v) of Conjecture 5.3 was previously refuted by `the-omega-institute/trureturing#9448` / PR `#9451` (`Problems/pisano-order-range-refutation.md`, merged `2026-09-22`) using $(a, b) = (3, 2)$ and $m = 13$ ($\omega_{(3,2)}(13) = 3 \notin \{0,1,2\}$). This document claims **only** the refutation of **clause (vi)** (*"infinite in all other cases"*), which PR `#9451` explicitly left open.

---

## Explicit Counterexample & Complete Proof Refuting Clause (vi): $(a, b) = (3, 4)$

Clause (vi) asserts that the range of $\omega_{(a,b)}(m)$ for $m > 1$ is **infinite** in all cases not covered by clauses (i)–(v).

Take $(a, b) = (3, 4)$ (mentioned explicitly in Section 5, line 724 of `fiborder.tex`, and satisfying the Section 4 convention of positive integers $a, b$). Check against clauses (i)–(v):
- $b = 4 \notin \{0, 1, -1\}$, so $(3,4)$ is not covered by (i), (ii), (iii), or (iv);
- $|a| - |b| = |3| - |4| = -1 \neq 1$, so $(3,4)$ is not covered by (v).

Therefore $(a, b) = (3, 4)$ falls strictly under **clause (vi)**, which predicts that $\{\omega_{(3,4)}(m) : m > 1\}$ is **infinite**.

We prove that **for every integer $m > 1$, $\omega_{(3,4)}(m) \in \{0, 1, 2\}$**, and that the exact range is $\{0, 1, 2\}$:

1. **Closed form:** By induction on $n \ge 0$, the $(3,4)$-Fibonacci recurrence $U_0 = 0, U_1 = 1, U_n = 3U_{n-1} + 4U_{n-2}$ ($n \ge 2$) satisfies
   $$U_n = \frac{4^n - (-1)^n}{5} \quad \text{for all } n \ge 0,$$
   since $U_0 = 0$, $U_1 = 1$, and for $n \ge 2$,
   $$3\frac{4^{n-1} - (-1)^{n-1}}{5} + 4\frac{4^{n-2} - (-1)^{n-2}}{5} = \frac{4^{n-2}(12 + 4) - (-1)^{n-2}(-3 + 4)}{5} = \frac{4^n - (-1)^n}{5}.$$

2. **Even $m > 1$:** For every $n \ge 1$, $4^n$ is even and $(-1)^n$ is odd, so $4^n - (-1)^n$ is odd, whence $U_n$ is odd. Thus $m \nmid U_n$ for every $n \ge 1$. Since $U_n \bmod m$ is eventually periodic (as $(\mathbb{Z}/m\mathbb{Z})^2$ is finite) and every nonzero entry $U_n$ ($n \ge 1$) is odd while $m$ is even, the eventual period contains no multiples of $m$. By the paper's definition (Section 5, line 724), $\omega_{(3,4)}(m) = 0$.

3. **Odd $m > 1$:** Since $\gcd(m, 4) = 1$, the transition matrix $\begin{pmatrix} 3 & 4 \\ 1 & 0 \end{pmatrix}$ has determinant $-4 \in (\mathbb{Z}/m\mathbb{Z})^\times$, so $(U_n \bmod m)_{n \ge 0}$ is purely periodic, and a positive integer $\pi$ is a period iff $(U_\pi, U_{\pi+1}) \equiv (0, 1) \pmod m$.
   Since $\gcd(2, 5m) = 1$,
   $$m \mid U_n \iff 5m \mid \bigl(4^n - (-1)^n\bigr) \iff 4^n \equiv (-1)^n \pmod{5m} \iff (-4)^n \equiv 1 \pmod{5m}.$$
   Because $\gcd(-4, 5m) = 1$, letting $\alpha = \mathrm{ord}_{5m}(-4) \ge 1$, we have $m \mid U_n \iff \alpha \mid n$.
   Whenever $\alpha \mid n$, we have $4^n \equiv (-1)^n \pmod{5m}$, so
   $$5U_{n+1} = 4^{n+1} - (-1)^{n+1} = 4 \cdot 4^n + (-1)^n \equiv 5(-1)^n \pmod{5m},$$
   which implies $U_{n+1} \equiv (-1)^n \pmod m$ (valid for all odd $m > 1$, including $5 \mid m$). Since $m \ge 3$ is odd, $-1 \not\equiv 1 \pmod m$, so $(U_n, U_{n+1}) \equiv (0, 1) \pmod m$ holds if and only if $\alpha \mid n$ and $2 \mid n$.
   Hence the minimal period is:
   - $\pi_{(3,4)}(m) = \alpha$ if $\alpha$ is even, containing only one zero ($n = 0$ in $[0, \alpha)$), so $\omega_{(3,4)}(m) = 1$;
   - $\pi_{(3,4)}(m) = 2\alpha$ if $\alpha$ is odd, containing two zeros ($n = 0$ and $n = \alpha$ in $[0, 2\alpha)$), so $\omega_{(3,4)}(m) = 2$.

4. **Exact range:** $\omega_{(3,4)}(2) = 0$, $\omega_{(3,4)}(3) = 1$ ($\alpha = \mathrm{ord}_{15}(-4) = 2$, $\pi = 2$, period $[0, 1]$), and $\omega_{(3,4)}(5) = 2$ ($\alpha = \mathrm{ord}_{25}(-4) = 5$, $\pi = 10$, period $[0, 1, 3, 3, 1, 0, 4, 2, 2, 4]$). Thus
   $$\{\omega_{(3,4)}(m) : m > 1\} = \{0, 1, 2\},$$
   which is finite ($|\{0,1,2\}| = 3$), directly refuting clause (vi) of Conjecture 5.3.

---

## Remark on Cause of Error

The authors apparently confused $|a| - |b| = 1$ in clause (v) with the condition that the characteristic polynomial $x^2 - ax - b$ have a root at $\pm 1$ (namely $a = \pm(b - 1)$), which fails for $(3, 2)$ (where $x^2 - 3x - 2$ is irreducible over $\mathbb{Q}$, refuting (v) as shown in `trureturing#9448`) and holds for $(3, 4)$ (where $x^2 - 3x - 4 = (x - 4)(x + 1)$ has root $-1$, forcing finite order range $\{0,1,2\}$ despite $b = 4$ and $|3| - |4| = -1$, refuting (vi)).

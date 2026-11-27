# Counterexample to Mbirika–Spilker `arXiv:2204.12626v2` Question 6.1 (Conjectures for $\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$)

**Result:** **FALSE** (explicit counterexamples for **both** the $\mathcal{F}^3(k)$ conjecture and the $\mathcal{L}^3(k)$ conjecture, in **both** the $6 \nmid k$ branch at $k=2$ and the $6 \mid k$ branch at $k=6$ and $k=12$).

---

## 1. Refutation of the $\mathcal{F}^3(k)$ Conjecture

### Counterexample 1a ($6 \nmid k$): $k = 2$
By definition, $\mathcal{F}^3(2) = \gcd\bigl\{(F_{n+1}^3 + F_{n+2}^3)_{n \ge 0}\bigr\}$.
- For $n = 0$: $F_1^3 + F_2^3 = 1^3 + 1^3 = 2$.
- For $n = 1$: $F_2^3 + F_3^3 = 1^3 + 2^3 = 9$.

Since $\gcd(2, 9) = 1$, the true value is $\mathcal{F}^3(2) = 1$.

However, since $6 \nmid 2$, the conjectured formula gives
$$\frac{1}{2}\gcd(F_3^3 - 1,\, F_4^3 - 1) = \frac{1}{2}\gcd(2^3 - 1,\, 3^3 - 1) = \frac{1}{2}\gcd(7, 26) = \frac{1}{2} \notin \mathbb{Z},$$
contradicting $\mathcal{F}^3(2) = 1$.

### Counterexample 1b ($6 \mid k$): $k = 6$
Even in the $6 \mid k$ branch (where no $\frac{1}{2}$ factor is present), the conjecture fails immediately at $k = 6$:
- For $n = 0$: $\sum_{i=1}^6 F_i^3 = 1^3 + 1^3 + 2^3 + 3^3 + 5^3 + 8^3 = 1 + 1 + 8 + 27 + 125 + 512 = 674 = 2 \cdot 337$.
- Since $4 \nmid 674$, we already have $\mathcal{F}^3(6) \mid 674$, so $4 \nmid \mathcal{F}^3(6)$.
- In fact, $\sum_{i=1}^6 F_{1+i}^3 = 1 + 8 + 27 + 125 + 512 + 2197 = 2870$, $\gcd(674, 2870) = 2$, and $(F_n \bmod 2)_{n \ge 0} = (0, 1, 1, 0, 1, 1, \dots)$ has period $3 \mid 6$ with two odd terms per period, so every block of $6$ consecutive terms contains $4$ odd cubes and is even; hence $\mathcal{F}^3(6) = 2$.

Meanwhile, since $6 \mid 6$, the conjectured formula gives
$$\gcd(F_7^3 - 1,\, F_8^3 - 1) = \gcd(13^3 - 1,\, 21^3 - 1) = \gcd(2196, 9260) = 4 \neq 2 = \mathcal{F}^3(6).$$

*(In fact, the conjectured formula for $\mathcal{F}^3(k)$ fails at every even $k \in \{2, 4, 6, \dots, 30\}$.)*

---

## 2. Refutation of the $\mathcal{L}^3(k)$ Conjecture

### Counterexample 2a ($6 \nmid k$): $k = 2$
By definition, $\mathcal{L}^3(2) = \gcd\bigl\{(L_{n+1}^3 + L_{n+2}^3)_{n \ge 0}\bigr\}$.
- For $n = 0$: $L_1^3 + L_2^3 = 1^3 + 3^3 = 28$.
- For $n = 1$: $L_2^3 + L_3^3 = 3^3 + 4^3 = 91$.
- For $n = 2$: $L_3^3 + L_4^3 = 4^3 + 7^3 = 407$.

Since $\gcd(28, 91, 407) = \gcd(7, 407) = 1$, the true value is $\mathcal{L}^3(2) = 1$.

However, since $6 \nmid 2$, the conjectured formula gives
$$\frac{1}{2}\gcd(L_3^3 - 1,\, L_4^3 - 9) = \frac{1}{2}\gcd(4^3 - 1,\, 7^3 - 9) = \frac{1}{2}\gcd(63, 334) = \frac{1}{2} \notin \mathbb{Z},$$
contradicting $\mathcal{L}^3(2) = 1$.

### Counterexample 2b ($6 \mid k$): $k = 12$
Since $6 \mid 12$, the conjectured formula predicts $\mathcal{L}^3(12) = \gcd(L_{13}^3 - 1,\, L_{14}^3 - 9)$.
- Because $(L_n \bmod 4)_{n \ge 0} = (2, 1, 3, 0, 3, 3, \dots)$ has period $6$, $(L_n^3 \bmod 4)$ has period $6$ with repeating block $(0, 1, 3, 0, 3, 3)$ summing to $10 \equiv 2 \pmod 4$; hence every sum of $12$ consecutive cubes $L_{n+1}^3 + \dots + L_{n+12}^3$ is divisible by $4$.
- Because $(L_n \bmod 5)_{n \ge 0} = (2, 1, 3, 4, \dots)$ has period $4$, $(L_n^3 \bmod 5)$ has period $4$ with repeating block $(3, 1, 2, 4)$ summing to $10 \equiv 0 \pmod 5$; hence every sum of $12$ consecutive cubes is divisible by $5$.
- Therefore $20 \mid \mathcal{L}^3(12)$ (in fact $\gcd$ of the first three sums $n=0,1,2$ is $\gcd(43702500, 185123260, 784200340) = 20$, so $\mathcal{L}^3(12) = 20$).

Meanwhile, $L_{13} = 521$ and $L_{14} = 843$, so
$$L_{13}^3 - 1 = 141420760, \qquad L_{14}^3 - 9 = 599077098, \qquad \gcd(141420760, 599077098) = 2 \neq 20 = \mathcal{L}^3(12).$$
*(In particular, $L_{14}^3 - 9 \equiv 3^3 - 1 = 26 \equiv 2 \pmod 4$ and $843^3 - 9 \equiv 3^3 - 9 = 18 \equiv 3 \pmod 5$; even replacing the apparent typo $9 = L_2^2$ with $27 = L_2^3$, the formula $\gcd(L_{k+1}^3 - 1, L_{k+2}^3 - 27)$ still fails at e.g. $k=6$: $\gcd(L_7^3-1, L_8^3-27) = \gcd(24388, 103796) = 28 \neq 2 = \mathcal{L}^3(6)$.)*

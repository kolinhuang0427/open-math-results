# Counterexample to Ballantine–Beck–Merca `arXiv:2408.13346v1` Conjectural Table of Minimal Periods for $e_2p_4(n) \pmod m$

**Result:** **FALSE** (explicit counterexamples at **$m = 10$** and **$m = 18$**, verified directly by exact partition dynamic programming and proved via the exact rational generating function).

The conjectural table in Section 1 (lines 93–97) asserts that the minimal period of $e_2p_4(n) \bmod 10$ is $1150$ and the minimal period of $e_2p_4(n) \bmod 18$ is $1246$. **Both entries are false:** the true minimal periods are **$1200$** (for $m=10$) and **$1296$** (for $m=18$). (The other $24$ entries in the table hold as stated.)

---

## 1. Explicit Numerical Counterexamples ($n = 0$ and $n = 4$)

Direct dynamic programming from the definition $e_2p_4(n) = \sum_{\lambda \in \mathcal{P}(4,n)} e_2(\lambda)$ gives exact values:
- At $n = 0$: $\mathcal{P}(4, 0) = \emptyset$, so $e_2p_4(0) = 0$.
- At $n = 4$: $\mathcal{P}(4, 4) = \{(1,1,1,1)\}$, so $e_2p_4(4) = \binom{4}{2}\cdot 1^2 = 6$.

Meanwhile, at the shifted indices claimed by the table:

### Counterexample 1: $m = 10$ (claimed period $1150$)
$$e_2p_4(1150) = 4204006824112 \equiv 2 \not\equiv 0 = e_2p_4(0) \pmod{10},$$
and likewise at $n = 4$,
$$e_2p_4(1154) = 4277582023120 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{10}.$$
Hence $1150$ is **not** a period (let alone minimal period) of $e_2p_4(n)$ modulo $10$.

*(Even for "sufficiently large $n$", since $(e_2p_4(n))_{n\ge 0}$ satisfies the monic-with-unit-constant-term order-$22$ linear recurrence with denominator $D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3$ proved in `targets/ballantine-2408.13346-e2p4-rec/PROOF.md`, the $22$-term state vector has $\det \in \{\pm 1\}$, so $e_2p_4(n) \bmod m$ is **purely periodic from $n=0$** for every $m \ge 2$. Therefore $e_2p_4(n+1150) \equiv e_2p_4(n) \pmod{10}$ fails for every residue class $n \equiv 0, 4 \pmod{1200}$, i.e., for infinitely many $n$.)*

### Counterexample 2: $m = 18$ (claimed period $1246$)
$$e_2p_4(1246) = 6275602376628 \equiv 6 \not\equiv 0 = e_2p_4(0) \pmod{18},$$
and likewise at $n = 4$,
$$e_2p_4(1250) = 6376921776108 \equiv 0 \not\equiv 6 = e_2p_4(4) \pmod{18}.$$
Hence $1246$ is **not** a period (let alone minimal period) of $e_2p_4(n)$ modulo $18$.

---

## 2. Conceptual Proof via Theorem 2 (`\label{Th0}`) and True Minimal Periods

Even without evaluating $e_2p_4(1150)$ or $e_2p_4(1246)$, both claimed entries directly contradict Theorem 2 (`\label{Th0}`) of `arXiv:2408.13346v1` itself:
- By Theorem 2, $48$ is the minimal period of $e_2p_4(n) \bmod 2$ and $54$ is the minimal period of $e_2p_4(n) \bmod 3$ (the minimality of $48$ mod $2$ and $54$ mod $3$ is immediate by checking divisors $16, 24$ of $48$ and $18, 27$ of $54$ on small $n$).
- Any period $P$ of $e_2p_4(n) \bmod 10$ must also be a period modulo $2$, forcing $48 \mid P$. Yet $1150 \equiv 46 \not\equiv 0 \pmod{48}$ (specifically, $e_2p_4(5) = 9 \equiv 1 \pmod 2$ whereas $e_2p_4(51) = 770034 \equiv 0 \pmod 2$, so $e_2p_4(1155) \equiv e_2p_4(51) \equiv 0 \not\equiv 1 \pmod 2$).
- Any period $P$ of $e_2p_4(n) \bmod 18$ must be a period both modulo $2$ and modulo $3$, forcing $\mathrm{lcm}(48, 54) = 432 \mid P$. Yet $1246 \equiv 46 \not\equiv 0 \pmod{48}$ and $1246 \equiv 4 \not\equiv 0 \pmod{54}$ (even $3 \nmid 1246$, and indeed $e_2p_4(2) = 0$ vs $e_2p_4(6) = 25 \equiv 1 \pmod 3$).

Because $e_2p_4(n) \bmod m$ is purely periodic for every $m \ge 2$ (via the $GL_{22}(\mathbb{Z})$ companion matrix of $D(q)$), the Chinese Remainder Theorem gives $\mathrm{per}(ab) = \mathrm{lcm}(\mathrm{per}(a), \mathrm{per}(b))$ whenever $\gcd(a,b)=1$. Using the exact order-$22$ recurrence:
- $\mathrm{per}(2) = 48$, $\mathrm{per}(5) = 300 \implies \mathrm{per}(10) = \mathrm{lcm}(48, 300) = \mathbf{1200} \neq 1150$.
- $\mathrm{per}(2) = 48$, $\mathrm{per}(9) = 324 \implies \mathrm{per}(18) = \mathrm{lcm}(48, 324) = \mathbf{1296} \neq 1246$.

*(Notice both errors in `arXiv:2408.13346v1` are off by exactly $50$: $1200 - 50 = 1150$ and $1296 - 50 = 1246$.)*

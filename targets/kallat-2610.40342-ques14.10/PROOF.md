# Resolution of Question 14.10 (`prob:gcdr`) of Kallat (`arXiv:2610.40342v1`)

**Target:** Ahaan Kallat, *A $p$-adic Valuation Calculus for Permutations with Restricted Cycle Lengths*, `arXiv:2610.40342v1`, Section 14, **Question 14.10** (`\label{prob:gcdr}`).

---

## Executive Summary and Exact Verdicts

For $r \ge 1$ and $n \ge 1$, let $a_S(n)$ denote the number of permutations of $\{1, \dots, n\}$ having no cycle length in $S \subseteq \mathbb{N}$. Write $S_\infty = \{1, \dots, r\}$ and $S_k = \{1, \dots, r, k\}$ for $k > r$, and define the three gcds:
$$G_r(n) := \gcd_{r < k \le n} a_{S_k}(n), \qquad g_r(n) := \gcd_{S \supseteq \{1,\dots,r\}} a_S(n), \qquad \Lambda_r(n) := \gcd_{\substack{\lambda \vdash n \\ \min(\lambda) > r}} N(\lambda),$$
where $N(\lambda) = n! / \prod_{m} m^{\lambda_m} \lambda_m!$ counts permutations of cycle type $\lambda$. By Kallat's Theorem 5.1 (`\label{thm:gcdfamily}`) and Proposition 11.3 (`\label{prop:globalgcd}`), for $n \ge r + 2$,
$$\Lambda_r(n) \mid g_r(n) \mid G_r(n) = (n-1)_r m_r(n) \quad \text{and} \quad (n-1)_r \mid g_r(n),$$
where $(n-1)_r = \prod_{j=1}^r (n-j)$ and every prime factor of $m_r(n)$ satisfies $p \le r$.

Question 14.10 poses four subquestions. We settle them as follows:

1. **(Q1) For $r = 3$, do $g_3(n)$ and $G_3(n)$ differ for every $n \equiv 30 \pmod{81}$ with $n \ge 111$ and for no other $n \ge 5$?**
   **Answer: YES.** For every $n \ge 5$,
   $$g_3(n) \ne G_3(n) \iff n \equiv 30 \pmod{81} \text{ and } n \ge 111,$$
   and whenever they differ, $G_3(n) / g_3(n) = 3$ (Theorem 1(d)).

2. **(Q2) Is $g_r(n) = G_r(n)$ for every $r \ge 4$ and every $n \ge r + 2$?**
   **Answer: NO (Disproved).** For every integer $r$ with $64 \le r \le 79$ and $n = 1248$, we have $g_r(1248) \ne G_r(1248)$; specifically,
   $$v_2\bigl(g_r(1248)\bigr) = v_2\bigl(\Lambda_r(1248)\bigr) = 1169 < 1170 \le v_2\bigl(G_r(1248)\bigr)$$
   (in fact $v_2(G_r(1248)) = 1170$), witnessed explicitly by $S = \mathbb{N} \setminus \{96\}$ (Theorem 2).

3. **(Q3) What is the exponent of each prime $p \le r$ in $g_r(n)/(n-1)_r$ for $r \ge 3$?**
   **Completely solved for $r = 3$** (Theorem 1(a)–(b)): for every $n \ge 5$,
   $$v_2\!\left(\frac{g_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-2}{4} \right\rfloor, \qquad v_3\!\left(\frac{g_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-4}{9} \right\rfloor + \left\lfloor \frac{n+2}{9} \right\rfloor + \delta_3(n),$$
   where
   $$\delta_3(n) := \begin{cases} 2 & \text{if } n \equiv 51 \pmod{81} \text{ and } n \ge 51, \\ 1 & \text{if } n \equiv 1, 2, 3, 24 \pmod{27},\ n \not\equiv 51 \pmod{81}, \text{ and } n \ge 55, \\ 0 & \text{otherwise.} \end{cases}$$
   *(Scope note: closed-form formulas for general $r \ge 4$ are not established here and remain open.)*

4. **(Q4) For which $n$ do $\Lambda_r(n)$ and $g_r(n)$ differ?**
   **Completely solved for $r = 3$** (Theorem 1(c)): for every $n \ge 5$,
   $$\Lambda_3(n) \ne g_3(n) \iff n \equiv 1, 2, 3, 24 \pmod{27} \text{ and } n \ge 51,$$
   with exact ratio $g_3(n) / \Lambda_3(n) = 3^{\delta_3(n)} \in \{3, 9\}$. *(Scope note: full classification for general $r \ge 4$ remains open.)*

All proofs below are completely elementary and self-contained (relying only on Legendre's formula, Kummer's theorem, and Kallat's Theorem 5.1 for primes $q > r$), and every numerical step and finite table is independently verified in exact arithmetic by `verify.py`.

---

## 1. Preliminaries and General Lemmas

Fix a prime $p$ and an integer $r \ge 1$. Write $\mathcal{P}_{>r}(n)$ for the set of partitions $\lambda \vdash n$ all of whose parts exceed $r$, writing $\lambda_m \ge 0$ for the multiplicity of $m$ in $\lambda$ and $\mathrm{supp}(\lambda) = \{m : \lambda_m > 0\}$ for its set of distinct parts. For $P \subseteq \{r+1, \dots, n\}$, let
$$f_P(n) := \sum_{\substack{\lambda \in \mathcal{P}_{>r}(n) \\ \mathrm{supp}(\lambda) = P}} N(\lambda).$$
By Legendre's formula $v_p(c!) = (c - s_p(c))/(p-1)$ (where $s_p(c)$ is the sum of the base-$p$ digits of $c$),
$$v_p\bigl(N(\lambda)\bigr) = v_p(n!) - \mathrm{cost}_p(\lambda), \qquad \mathrm{cost}_p(\lambda) := \sum_{m > r} \ell_m(\lambda_m), \qquad \ell_m(c) := c\,v_p(m) + v_p(c!).$$
Put $\kappa_{r,p}(n) := \max_{\lambda \in \mathcal{P}_{>r}(n)} \mathrm{cost}_p(\lambda)$, so that $v_p(\Lambda_r(n)) = v_p(n!) - \kappa_{r,p}(n)$.

### Lemma 1 (Part-Set Criterion and Difference Criterion)
Let $r \ge 1$, $n \ge r + 2$, and let $p$ be a prime.
1. $g_r(n) = \gcd_{P \subseteq (r, n]} f_P(n)$, and hence $v_p(g_r(n)) = \min_{P \subseteq (r, n]} v_p(f_P(n))$. In particular, for any $T \ge 0$, $v_p(g_r(n)) \ge T$ if and only if $v_p(f_P(n)) \ge T$ for every $P$ carrying at least one partition $\lambda \in \mathcal{P}_{>r}(n)$ with $v_p(N(\lambda)) < T$.
2. $a_{S_{n-1}}(n) = a_{S_\infty}(n)$, so $G_r(n) \mid a_{S_\infty}(n)$. Consequently, for every $k \in \{r+1, \dots, n\}$,
   $$G_r(n) \ \Big|\ \bigl(a_{S_\infty}(n) - a_{S_k}(n)\bigr) = \sum_{\substack{\lambda \in \mathcal{P}_{>r}(n) \\ k \in \mathrm{supp}(\lambda)}} N(\lambda).$$
3. **(Unique Maximum Principle)** If a finite family $\mathcal{C} \subseteq \mathcal{P}_{>r}(n)$ contains a unique partition $\lambda^*$ of maximal $p$-adic cost $c^*$, then $v_p\bigl(\sum_{\lambda \in \mathcal{C}} N(\lambda)\bigr) = v_p(n!) - c^*$.

**Proof.**
(1) This is Kallat's Proposition 11.3(i),(iv) (`\label{prop:globalgcd}`). Directly: for any $S \supseteq \{1, \dots, r\}$ with $A = (\mathbb{N} \setminus S) \cap (r, n]$, we have $a_S(n) = \sum_{P \subseteq A} f_P(n)$, and Möbius inversion on the Boolean lattice of subsets of $(r, n]$ gives $f_P(n) = \sum_{B \subseteq P} (-1)^{|P \setminus B|} a_{\mathbb{N} \setminus B}(n)$; hence the two gcds agree. If every $\lambda$ with $\mathrm{supp}(\lambda) = P$ satisfies $v_p(N(\lambda)) \ge T$, then automatically $v_p(f_P(n)) \ge T$.
(2) Any permutation of $\{1, \dots, n\}$ containing an $(n-1)$-cycle must also contain a $1$-cycle; since $1 \in S_\infty$, no permutation counted by $a_{S_\infty}(n)$ contains an $(n-1)$-cycle, so $a_{S_{n-1}}(n) = a_{S_\infty}(n)$ (Kallat eq. `(5.2)`). Because $n \ge r + 2$, $S_{n-1}$ lies in the family defining $G_r(n)$, so $G_r(n) \mid a_{S_\infty}(n)$ and $G_r(n) \mid a_{S_k}(n)$, hence $G_r(n)$ divides their difference, which sums $N(\lambda)$ over all $\lambda \in \mathcal{P}_{>r}(n)$ containing part $k$.
(3) Every $\lambda \in \mathcal{C} \setminus \{\lambda^*\}$ satisfies $v_p(N(\lambda)) > v_p(N(\lambda^*)) = v_p(n!) - c^*$, so the ultrametric triangle inequality gives $v_p(\sum_{\lambda \in \mathcal{C}} N(\lambda)) = v_p(n!) - c^*$. $\square$

---

## 2. Disproof of Question 14.10(Q2): $g_r(n) \ne G_r(n)$ for $64 \le r \le 79$ at $n = 1248$

### Theorem 2 (Disproof of Question 14.10(Q2))
For every integer $r$ with $64 \le r \le 79$, at $n = 1248$ we have
$$v_2\bigl(g_r(1248)\bigr) = v_2\bigl(\Lambda_r(1248)\bigr) = 1169 < 1170 \le v_2\bigl(G_r(1248)\bigr).$$
In particular, $g_r(1248) \ne G_r(1248)$ for every $64 \le r \le 79$, refuting Question 14.10(Q2).

The proof relies on the simultaneous three-block efficiency tie among $80, 96, 128$ at $p = 2$. For any integer $m \ge 1$, define its $2$-adic deficit relative to $1/16$ by
$$\Delta(m) := \frac{m}{16} - \bigl(v_2(m) + 1\bigr).$$
For any partition $\lambda \in \mathcal{P}_{>64}(1248)$, since $\sum_{m} m \lambda_m = 1248 = 78 \cdot 16$ and $v_2(c!) = c - s_2(c)$,
$$78 - \mathrm{cost}_2(\lambda) = \sum_{m > 64} \frac{m \lambda_m}{16} - \sum_{m > 64} \Bigl(\lambda_m\bigl(v_2(m) + 1\bigr) - s_2(\lambda_m)\Bigr) = \sum_{m > 64} \lambda_m \Delta(m) + \sum_{m > 64} s_2(\lambda_m). \tag{2.1}$$

### Lemma 2.1 (Classification of $\Delta(m)$ for $m \ge 65$)
For every integer $m \ge 65$, we have $\Delta(m) \ge 0$, with:
1. $\Delta(m) = 0$ if and only if $m \in \{80, 96, 128\}$;
2. The unique integer $m \ge 65$ outside $\{80, 96, 128\}$ satisfying $\Delta(m) \le 1$ is $m = 72$, for which $\Delta(72) = 1/2$.

**Proof.** Write $m = d \cdot 2^e$ with $d \ge 1$ odd and $e \ge 0$, so $\Delta(m) = d \cdot 2^{e-4} - (e + 1)$.
- $e \in \{0, 1, 2\}$: $m \ge 65$ and $e + 1 \le 3$, so $\Delta(m) \ge \frac{65}{16} - 3 = \frac{17}{16} > 1$.
- $e = 3$: $m = 8d \ge 65$ with $d$ odd forces $d \ge 9$, so $\Delta(8d) = \frac{d}{2} - 4$. For $d = 9$ ($m = 72$), $\Delta(72) = \frac{1}{2}$; for $d \ge 11$, $\Delta(8d) \ge \frac{11}{2} - 4 = \frac{3}{2} > 1$.
- $e = 4$: $m = 16d \ge 65$ with $d$ odd forces $d \ge 5$, so $\Delta(16d) = d - 5$. This vanishes at $d = 5$ ($m = 80$) and is $\ge 2$ for $d \ge 7$.
- $e = 5$: $m = 32d \ge 65$ with $d$ odd forces $d \ge 3$, so $\Delta(32d) = 2d - 6$. This vanishes at $d = 3$ ($m = 96$) and is $\ge 4$ for $d \ge 5$.
- $e = 6$: $m = 64d \ge 65$ with $d$ odd forces $d \ge 3$, so $\Delta(64d) = 4d - 7 \ge 5 > 1$.
- $e = 7$: $m = 128d \ge 65$ with $d$ odd gives $\Delta(128d) = 8d - 8$. This vanishes at $d = 1$ ($m = 128$) and is $\ge 16$ for $d \ge 3$.
- $e \ge 8$: $m \ge 2^e$, so $\Delta(m) \ge 2^{e-4} - (e + 1) \ge 16 - 9 = 7 > 1$ (since $2^{e-4} - (e + 1)$ increases strictly for $e \ge 8$). $\square$

### Lemma 2.2 (Exact Top-Cost Partitions of $1248$ into Parts $> 64$)
Every partition $\lambda \in \mathcal{P}_{>64}(1248)$ satisfies $\mathrm{cost}_2(\lambda) \le 75$, and **exactly four** partitions in $\mathcal{P}_{>64}(1248)$ attain $\mathrm{cost}_2(\lambda) = 75$:
$$\lambda^{(1)} = 96^{13}, \qquad \lambda^{(2)} = 96^1 \cdot 128^9, \qquad \lambda^{(3)} = 80^6 \cdot 96^8, \qquad \lambda^{(4)} = 80^8 \cdot 96^1 \cdot 128^4.$$

**Proof.** Let $\lambda \in \mathcal{P}_{>64}(1248)$ have $\mathrm{cost}_2(\lambda) \ge 75$, so by (2.1),
$$D(\lambda) + S(\lambda) \le 3, \qquad \text{where } D(\lambda) := \sum_{m > 64} \lambda_m \Delta(m), \quad S(\lambda) := \sum_{m > 64} s_2(\lambda_m).$$
Note that $D(\lambda) = 78 - \sum_{m > 64} \lambda_m(v_2(m) + 1) \in \mathbb{Z}$, and by Lemma 2.1 every term $\lambda_m \Delta(m)$ is non-negative and vanishes iff $m \in \{80, 96, 128\}$.

**Step 1: $\mathrm{supp}(\lambda) \subseteq \{80, 96, 128\}$.**
Suppose to the contrary that $\lambda$ has $t \ge 1$ distinct parts outside $\{80, 96, 128\}$. Then $D(\lambda)$ is a positive integer, so $D(\lambda) \ge 1$, while $\sum_{m \notin \{80,96,128\}} s_2(\lambda_m) \ge t$.
- If $t \ge 2$, then $D(\lambda) + S(\lambda) \le 3$ forces $t = 2$, $D(\lambda) = 1$, $S(\lambda) = 2$, hence $\lambda$ has zero parts in $\{80, 96, 128\}$ and exactly two distinct parts $m_1, m_2 \notin \{80, 96, 128\}$ with $\lambda_{m_1} \Delta(m_1) + \lambda_{m_2} \Delta(m_2) = 1$. Since both summands are positive, $\Delta(m_1) < 1$ and $\Delta(m_2) < 1$, contradicting Lemma 2.1(2) (only $m = 72$ has $\Delta(m) < 1$).
- If $t = 1$, let $m_1 \notin \{80, 96, 128\}$ be the unique such part.
  - If $\lambda$ has no parts in $\{80, 96, 128\}$, then $m_1 \lambda_{m_1} = 1248$ and $D(\lambda) + s_2(\lambda_{m_1}) \le 3$. Since $D(\lambda) \ge 1$, we have $s_2(\lambda_{m_1}) \le 2$ and $\lambda_{m_1} \Delta(m_1) \le 2$. If $s_2(\lambda_{m_1}) = 2$, then $\lambda_{m_1} \Delta(m_1) = 1$, so $\lambda_{m_1} \ge 3$ forces $\Delta(m_1) \le 1/3$, impossible by Lemma 2.1 (minimum non-zero $\Delta$ is $\Delta(72) = 1/2$). If $s_2(\lambda_{m_1}) = 1$, then $\lambda_{m_1} = 2^u$ ($u \ge 0$) divides $1248 = 39 \cdot 32$, so $u \in \{0, 1, 2, 3, 4\}$ and $m_1 = 1248 / 2^u \in \{1248, 624, 312, 156, 78\}$; in all five cases $\Delta(m_1) \ge \Delta(78) = \frac{78}{16} - 2 = \frac{23}{8} > 2$, contradicting $\lambda_{m_1} \Delta(m_1) \le 2$.
  - If $\lambda$ also has parts in $\{80, 96, 128\}$, then $S(\lambda) \ge 2$, which forces $D(\lambda) = 1$ and $S(\lambda) = 2$, so $s_2(\lambda_{m_1}) = 1$ and $\lambda$ has a single part $m_0 \in \{80, 96, 128\}$ with $s_2(\lambda_{m_0}) = 1$, i.e. $\lambda_{m_0} = 2^k$. Since $\lambda_{m_1} \Delta(m_1) = 1$, Lemma 2.1(2) forces $m_1 = 72$ and $\lambda_{72} = 2$ (as no $m \ge 65$ has $\Delta(m) = 1$). Then $m_0 \cdot 2^k = 1248 - 2 \cdot 72 = 1104$, which is impossible because $1104$ is not divisible by $80$, $96$, or $128$ ($1104 = 16 \cdot 69$).

Thus $\mathrm{supp}(\lambda) \subseteq \{80, 96, 128\}$.

**Step 2: Solving $80a + 96b + 128c = 1248$ with $s_2(a) + s_2(b) + s_2(c) \le 3$.**
Dividing by $16$ gives $5a + 6b + 8c = 78$, so $a$ is even ($0 \le a \le 14$) and $3b + 4c = (78 - 5a)/2$. Checking every even $a \in \{0, 2, 4, 6, 8, 10, 12, 14\}$ exhaustively:

| $a$ | $s_2(a)$ | $3b + 4c$ | All non-negative integer solutions $(b, c)$ | $s_2(a) + s_2(b) + s_2(c)$ | $\le 3$? |
|---|---|---|---|---|---|
| $0$ | $0$ | $39$ | $(13, 0),\ (9, 3),\ (5, 6),\ (1, 9)$ | $3,\ 4,\ 4,\ 3$ | **$(0, 13, 0)$, $(0, 1, 9)$** |
| $2$ | $1$ | $34$ | $(10, 1),\ (6, 4),\ (2, 7)$ | $4,\ 4,\ 5$ | none |
| $4$ | $1$ | $29$ | $(7, 2),\ (3, 5)$ | $5,\ 5$ | none |
| $6$ | $2$ | $24$ | $(8, 0),\ (4, 3),\ (0, 6)$ | $3,\ 5,\ 4$ | **$(6, 8, 0)$** |
| $8$ | $1$ | $19$ | $(5, 1),\ (1, 4)$ | $4,\ 3$ | **$(8, 1, 4)$** |
| $10$ | $2$ | $14$ | $(2, 2)$ | $4$ | none |
| $12$ | $2$ | $9$ | $(3, 0)$ | $4$ | none |
| $14$ | $3$ | $4$ | $(0, 1)$ | $4$ | none |

No solution achieves $s_2(a) + s_2(b) + s_2(c) \le 2$, and exactly the four listed solutions achieve $3$, i.e. $\mathrm{cost}_2(\lambda) = 78 - 3 = 75$. $\square$

**Proof of Theorem 2.**
Fix any $r \in \{64, 65, \dots, 79\}$. Because every part in $\lambda^{(1)}, \dots, \lambda^{(4)}$ is at least $80 > r$, all four belong to $\mathcal{P}_{>r}(1248) \subseteq \mathcal{P}_{>64}(1248)$. By Legendre's formula, $v_2(1248!) = 1248 - s_2(1248) = 1248 - 4 = 1244$ (as $1248 = 1024 + 128 + 64 + 32$). By Lemma 2.2, $\kappa_{r, 2}(1248) = 75$, so $v_2(\Lambda_r(1248)) = 1244 - 75 = 1169$, and for every $\lambda \in \mathcal{P}_{>r}(1248)$:
- $v_2(N(\lambda)) = 1169$ if $\lambda \in \{\lambda^{(1)}, \lambda^{(2)}, \lambda^{(3)}, \lambda^{(4)}\}$, so $N(\lambda) \equiv 2^{1169} \pmod{2^{1170}}$;
- $v_2(N(\lambda)) \ge 1170$ for all other $\lambda \in \mathcal{P}_{>r}(1248)$.

Now let $k \in \{r+1, \dots, 1248\}$ be arbitrary. The number of partitions among $\lambda^{(1)}, \dots, \lambda^{(4)}$ that avoid $k$ (and hence contribute to $a_{S_k}(1248)$) is:
- $4$ if $k \notin \{80, 96, 128\}$ (all four survive);
- $2$ if $k = 80$ ($\lambda^{(1)} = 96^{13}$ and $\lambda^{(2)} = 96^1 128^9$ survive);
- $2$ if $k = 128$ ($\lambda^{(1)} = 96^{13}$ and $\lambda^{(3)} = 80^6 96^8$ survive);
- $0$ if $k = 96$ (all four contain $96$).

In every case the count is even, so $a_{S_k}(1248) \equiv 0 \pmod{2^{1170}}$, i.e. $v_2(a_{S_k}(1248)) \ge 1170$ for all $k \in (r, 1248]$. Hence $v_2(G_r(1248)) \ge 1170$.

On the other hand, take $S = \mathbb{N} \setminus \{96\} \supseteq \{1, \dots, r\}$. The unique partition of $1248$ using only part $96$ is $\lambda^{(1)} = 96^{13}$, so
$$a_S(1248) = N(96^{13}) = \frac{1248!}{96^{13} \cdot 13!}, \qquad v_2\bigl(a_S(1248)\bigr) = 1244 - \bigl(13 \cdot 5 + 10\bigr) = 1169.$$
Since $\Lambda_r(1248) \mid g_r(1248) \mid a_S(1248)$, we conclude $v_2(g_r(1248)) = v_2(\Lambda_r(1248)) = 1169 < 1170 \le v_2(G_r(1248))$, so $g_r(1248) \ne G_r(1248)$. $\square$

*(Remark: Exact arithmetic verification in `verify.py` further confirms $v_2(G_r(1248)) = 1170$ for all $64 \le r \le 79$, so $v_2(G_r(1248)/g_r(1248)) = 1$; additional counterexamples also occur at $r = 64$ and $n = 1248 + m$ for $65 \le m \le 72$, recorded in `notes/comp-q2.md`.)*

---

## 3. Exact $2$-adic Valuations for $r = 3$ (All $n \ge 5$)

### Theorem 3 (Exact $2$-adic Formula for $r = 3$)
For every integer $n \ge 5$,
$$v_2\bigl(\Lambda_3(n)\bigr) = v_2\bigl(g_3(n)\bigr) = v_2\bigl(G_3(n)\bigr) = v_2\bigl((n-1)_3\bigr) + \left\lfloor \frac{n-2}{4} \right\rfloor.$$

**Proof.** Write $n = 4q + \nu$ with $q \ge 1$ and $\nu \in \{0, 1, 2, 3\}$. Define the candidate partition $\lambda^* \in \mathcal{P}_{>3}(n)$ by $\lambda^* = 4^q$ if $\nu = 0$ and $\lambda^* = 4^{q-1} \cdot (4+\nu)^1$ if $\nu \in \{1, 2, 3\}$. Its $2$-adic cost is
$$\kappa_2(n) := \mathrm{cost}_2(\lambda^*) = \begin{cases} \ell_4(q) = 2q + v_2(q!) & \text{if } \nu = 0, \\ \ell_4(q-1) + [\nu = 2] = 2(q-1) + v_2((q-1)!) + [\nu = 2] & \text{if } \nu \in \{1, 2, 3\}. \end{cases}$$

**Claim:** $\lambda^*$ is the **unique** partition in $\mathcal{P}_{>3}(n)$ attaining $\mathrm{cost}_2(\lambda) \ge \kappa_2(n)$.

*Proof of Claim.* First check that for every integer $m \ge 5$ and $c \ge 1$,
$$\ell_m(c) = c\bigl(v_2(m) + 1\bigr) - s_2(c) \le \frac{mc}{2} - 1, \tag{3.1}$$
with equality on $v_2(m) + 1 \le m/2$ only at $m = 8$. Indeed, $s_2(c) \ge 1$, and writing $m = d \cdot 2^e$ ($d$ odd):
- $e = 0$ ($m \ge 5$): $\frac{m}{2} - (e+1) = \frac{m}{2} - 1 \ge \frac{3}{2}$;
- $e = 1$ ($d \ge 3$): $\frac{m}{2} - (e+1) = d - 2 \ge 1$;
- $e = 2$ ($d \ge 3$): $\frac{m}{2} - (e+1) = 2d - 3 \ge 3$;
- $e = 3$ ($d \ge 1$): $\frac{m}{2} - (e+1) = 4d - 4 \ge 0$ (zero iff $m = 8$);
- $e \ge 4$: $\frac{m}{2} - (e+1) \ge 2^{e-1} - (e+1) \ge 3$.

Now let $\lambda = 4^X \cdot \mu \in \mathcal{P}_{>3}(n)$ where $\mu$ uses only parts $\ge 5$ and has weight $w = |\mu| = n - 4X$.
- **Case $\nu = 0$ ($n = 4q$):** If $w = 0$, then $\lambda = 4^q = \lambda^*$. If $w > 0$, then $w = 4\Delta$ with $\Delta = q - X \ge 2$ (as $w \ge 5$). By superadditivity of $v_2((\cdot)!)$, $\ell_4(q) - \ell_4(q - \Delta) = 2\Delta + v_2(q!) - v_2((q-\Delta)!) \ge 2\Delta$, whereas summing (3.1) over the parts of $\mu$ gives $\mathrm{cost}_2(\mu) \le \frac{w}{2} - 1 = 2\Delta - 1 < 2\Delta$. Hence $\mathrm{cost}_2(\lambda) < \ell_4(q)$.
- **Case $\nu \in \{1, 2, 3\}$ ($n = 4q + \nu$):** Since $1, 2, 3$ are excluded, $w \ge 5$, so $X \le q - 1$. Put $\Delta = (q - 1) - X \ge 0$, so $w = 4\Delta + 4 + \nu$.
  - If $\Delta = 0$, then $w = 4 + \nu \in \{5, 6, 7\}$; since $2 \cdot 5 = 10 > 7$, the only partition of $w$ into parts $\ge 5$ is $\mu = (4 + \nu)^1$, giving $\lambda = \lambda^*$.
  - If $\Delta \ge 1$, then $\ell_4(q-1) - \ell_4(q-1-\Delta) \ge 2\Delta + v_2(\Delta!)$. We show $\mathrm{cost}_2(\mu) < 2\Delta + v_2(\Delta!) + [\nu = 2]$:
    - For $\Delta \ge 4$: because $4 \nmid w$, $\mu$ contains at least one part $m_0 \ge 5$ with $4 \nmid m_0$, for which $\frac{m_0}{2} - (v_2(m_0)+1) \ge 1$. Summing (3.1) gives $\mathrm{cost}_2(\mu) \le \frac{w}{2} - 1 - 1 = 2\Delta + \frac{\nu}{2} \le 2\Delta + 1 + \frac{1}{2}$, hence $\mathrm{cost}_2(\mu) \le 2\Delta + 1$. Since $\Delta \ge 4 \implies v_2(\Delta!) \ge 3$, we get $\mathrm{cost}_2(\mu) \le 2\Delta + 1 < 2\Delta + 3 \le 2\Delta + v_2(\Delta!) + [\nu = 2]$.
    - For $\Delta \in \{1, 2, 3\}$, $w = 4\Delta + 4 + \nu \in \{9, 10, 11, 13, 14, 15, 17, 18, 19\}$. Direct check of partitions into parts $\ge 5$:
      - $w = 9$: $\{9\}$ (cost $0 < 2$); $w = 10$: $\{10, 5^2\}$ (max cost $1 < 3$); $w = 11$: $\{11, 5+6\}$ (max cost $1 < 2$).
      - $w = 13, 14, 15$ ($\Delta = 2$, $2\Delta + v_2(2!) = 5$): since $w < 16$, any part $8$ appears at most once (leaving $5, 6, 7$, cost $\le 1$), so max cost is $3, 4, 3$ respectively, strictly below $5, 6, 5$.
      - $w = 17, 18, 19$ ($\Delta = 3$, $2\Delta + v_2(3!) = 7$): neither $16^1$ nor $8^2$ can appear in $\mu$ because $w - 16 \in \{1, 2, 3\}$ cannot be partitioned into parts $\ge 5$. If part $8$ appears once, the remaining weight $w - 8 \in \{9, 10, 11\}$ has max cost at most $1$ (checked above), so $\mathrm{cost}_2(\mu) \le 3 + 1 = 4 < 7$. If part $8$ does not appear, then every part $m \ge 5$ of $\mu$ satisfies $v_2(m) + 1 \le \frac{m}{2} - 1$; thus a single-part partition $\mu = w^1$ has cost $v_2(w) \le 1 < 7$, while any partition with total number of parts $C = \sum_m \lambda_m \ge 2$ satisfies $\mathrm{cost}_2(\mu) \le \sum_m (\lambda_m (\frac{m}{2} - 1) - s_2(\lambda_m)) \le \frac{w}{2} - C - 1 \le \lfloor w/2 \rfloor - 3 \le 6 < 7$.

This proves the Claim.

Consequently $\kappa_{3,2}(n) = \kappa_2(n)$ and $v_2(\Lambda_3(n)) = v_2(n!) - \kappa_2(n)$. Moreover, since $\lambda^*$ is the unique max-cost partition in $\mathcal{P}_{>3}(n)$, pick $k = 5$ if $\nu \ne 1$, $k = 6$ if $\nu = 1$ and $n \ge 9$, and $k = 4$ if $n = 5$. In every case $k \in \{4, \dots, n\}$ and $k \notin \mathrm{supp}(\lambda^*)$, so by Lemma 1(3), $v_2(a_{S_k}(n)) = v_2(n!) - \kappa_2(n) = v_2(\Lambda_3(n))$. Since $\Lambda_3(n) \mid g_3(n) \mid G_3(n) \mid a_{S_k}(n)$, all three $2$-adic valuations are equal.

Finally, since $v_2((4q + \nu)!) = 3q + v_2(q!) + [\nu \ge 2]$, subtracting $\kappa_2(n)$ and $v_2((n-1)_3) = v_2((4q+\nu-1)(4q+\nu-2)(4q+\nu-3))$ gives:
- $\nu = 0$: $(3q + v_2(q!)) - (2q + v_2(q!)) - 1 = q - 1 = \lfloor (n-2)/4 \rfloor$;
- $\nu = 1$: $(3q + v_2(q!)) - (2q - 2 + v_2((q-1)!)) - (3 + v_2(q)) = q - 1 = \lfloor (n-2)/4 \rfloor$;
- $\nu = 2$: $(3q + 1 + v_2(q!)) - (2q - 1 + v_2((q-1)!)) - (2 + v_2(q)) = q = \lfloor (n-2)/4 \rfloor$;
- $\nu = 3$: $(3q + 1 + v_2(q!)) - (2q - 2 + v_2((q-1)!)) - (3 + v_2(q)) = q = \lfloor (n-2)/4 \rfloor$. $\square$

---

## 4. Exact $3$-adic Classification for $r = 3$ (All $n \ge 5$)

Every partition $\lambda \in \mathcal{P}_{>3}(n)$ can be written uniquely as
$$\lambda = 9^Y \cdot 6^{3t + x_0} \cdot \mu,$$
with integers $Y \ge 0$, $t \ge 0$, $x_0 \in \{0, 1, 2\}$, and a partition $\mu$ all of whose parts lie in $\{m \ge 4 : m \notin \{6, 9\}\}$ of weight $w = |\mu| = n - 9Y - 6(3t + x_0)$. Set $Y' := Y + 2t$, so that $n = 9Y' + 6x_0 + w$.

### Lemma 4.1 (The $6^3 \leftrightarrow 9^2$ Trade Identity)
With $\lambda = 9^{Y' - 2t} \cdot 6^{3t + x_0} \cdot \mu$ ($x_0 \in \{0, 1, 2\}$, $0 \le 2t \le Y'$),
$$\mathrm{cost}_3(\lambda) = \ell_9(Y') + x_0 + \mathrm{cost}_3(\mu) - \Delta_{\mathrm{trade}}(Y', t),$$
where
$$\Delta_{\mathrm{trade}}(Y', t) := v_3\!\binom{Y'}{2t} + \bigl(v_3((2t)!) - v_3(t!)\bigr) \ge 0.$$
Moreover:
1. $\Delta_{\mathrm{trade}}(Y', t) = 0$ if and only if $t = 0$, or ($t = 1$ and $Y' \equiv 2 \pmod 3$).
2. $\Delta_{\mathrm{trade}}(Y', t) \ge 2$ for every $t \ge 5$ and every $Y' \ge 2t$.
3. When $Y' \equiv 2 \pmod 3$, the values of $t \ge 0$ with $\Delta_{\mathrm{trade}}(Y', t) \le 1$ are:
   - $t \in \{0, 1\}$ (both with $\Delta_{\mathrm{trade}} = 0$) if $Y' \equiv 2 \pmod 9$;
   - $t \in \{0, 1, 2\}$ ($t = 0, 1$ give $0$; $t = 2$ gives $1$) if $Y' \equiv 5 \pmod 9$;
   - $t \in \{0, 1, 2, 3, 4\}$ ($t = 0, 1$ give $0$; $t = 2, 3, 4$ give $1$) if $Y' \equiv 8 \pmod 9$.

**Proof.** Since $x_0 \in \{0, 1, 2\}$, $v_3((3t + x_0)!) = t + v_3(t!)$, so $\ell_6(3t + x_0) = 4t + x_0 + v_3(t!)$. Meanwhile $\ell_9(Y') - \ell_9(Y' - 2t) = 4t + v_3(Y'!) - v_3((Y' - 2t)!)$. Subtracting yields
$$\bigl(\ell_9(Y') + x_0\bigr) - \bigl(\ell_9(Y' - 2t) + \ell_6(3t + x_0)\bigr) = v_3(Y'!) - v_3((Y'-2t)!) - v_3(t!) = v_3\!\binom{Y'}{2t} + \bigl(v_3((2t)!) - v_3(t!)\bigr).$$
Both summands are non-negative (as $v_3((2t)!) = \sum_{j \ge 1} \lfloor 2t/3^j \rfloor \ge \sum_{j \ge 1} \lfloor t/3^j \rfloor = v_3(t!)$).
- For (1): $v_3((2t)!) - v_3(t!) = 0$ holds iff $t \in \{0, 1\}$ (for $t \ge 2$, $\lfloor 2t/3 \rfloor \ge 1 + \lfloor t/3 \rfloor$). For $t = 1$, $v_3\binom{Y'}{2} = v_3(Y'(Y'-1)/2) = 0 \iff Y' \equiv 2 \pmod 3$.
- For (2): for $t = 5$, $v_3(10!) - v_3(5!) = 4 - 1 = 3 \ge 2$. For $t \ge 6$, write $t = 3a + b$ with $a \ge 2$ and $b \in \{0, 1, 2\}$; then $v_3((2t)!) - v_3(t!) \ge \lfloor 2t/3 \rfloor - \lfloor t/3 \rfloor = a + \lfloor 2b/3 \rfloor \ge a \ge 2$.
- For (3): for $t \in \{2, 3, 4\}$, $v_3((2t)!) - v_3(t!) = 1$ (check: $1-0$, $2-1$, $2-1$), so $\Delta_{\mathrm{trade}}(Y', t) = 1 \iff v_3\binom{Y'}{2t} = 0$. By Kummer's theorem, $v_3\binom{Y'}{2t} = 0$ iff each base-$3$ digit of $2t$ is $\le$ the corresponding base-$3$ digit of $Y'$. Writing the last two base-$3$ digits of $2t \in \{4, 6, 8\}$ as $(11)_3, (20)_3, (22)_3$ and of $Y' \bmod 9 \in \{2, 5, 8\}$ as $(02)_3, (12)_3, (22)_3$, we see: $(02)_3$ dominates none; $(12)_3$ dominates only $(11)_3$ ($t = 2$); $(22)_3$ dominates all three ($t = 2, 3, 4$). $\square$

### Lemma 4.2 (Master Partition Bound and Finite Classification for $r = 3, p = 3$)
Write $n = 9q + \rho \ge 5$ with $q \ge 0$ and $\rho \in \{0, 1, \dots, 8\}$, and define
$$\kappa_3(n) := \begin{cases} \ell_9(q) & \rho \in \{0, 4, 5, 7, 8\}, \\ \ell_9(q) + 1 & \rho = 6, \\ \ell_9(q-1) + 1 & \rho \in \{1, 2\}, \\ \ell_9(q-1) + 2 & \rho = 3, \end{cases}$$
where we put $d_{\mathrm{ref}}(\rho) := 0$ for $\rho \in \{0, 4, 5, 6, 7, 8\}$ and $d_{\mathrm{ref}}(\rho) := 1$ for $\rho \in \{1, 2, 3\}$ (note $n \ge 5$ implies $q \ge d_{\mathrm{ref}}(\rho)$ always). Then:
1. For every $m \ge 4$ with $m \notin \{6, 9\}$ and every $c \ge 1$, $\ell_m(c) \le \frac{5}{36} mc - \frac{1}{2}$. Hence any non-empty partition $\mu$ of weight $w > 0$ avoiding $\{6, 9\}$ satisfies $\mathrm{cost}_3(\mu) \le \lfloor (5w - 18)/36 \rfloor$.
2. For every $\lambda = 9^{Y'-2t} 6^{3t+x_0} \mu \in \mathcal{P}_{>3}(n)$ with $Y' = q - d$ ($d \ge 0$), $\mathrm{cost}_3(\lambda) \le \kappa_3(n)$ with equality attained, so $\kappa_{3,3}(n) = \kappa_3(n)$ and
   $$v_3\bigl(\Lambda_3(n)\bigr) = v_3(n!) - \kappa_3(n) = v_3\bigl((n-1)_3\bigr) + \left\lfloor \frac{n-4}{9} \right\rfloor + \left\lfloor \frac{n+2}{9} \right\rfloor.$$
3. Let $\mathrm{drop}(\lambda) := \kappa_3(n) - \mathrm{cost}_3(\lambda) \ge 0$. Every $\lambda$ with $\mathrm{drop}(\lambda) \le 2$ satisfies $d \ge d_{\mathrm{ref}}(\rho)$ and $d - d_{\mathrm{ref}}(\rho) \le 2$ (hence $w = 9d + \rho - 6x_0 \le 30$). Furthermore, writing $\mu_{\max}(w) := \max_{\mu \vdash w} \mathrm{cost}_3(\mu)$ over partitions avoiding $\{6, 9\}$, the **only** triples $(d, x_0, w)$ with $d \ge d_{\mathrm{ref}}(\rho)$ capable of achieving $\mathrm{drop}(\lambda) \le 1$ (and, for $\rho \in \{3, 6\}$, $\mathrm{drop}(\lambda) = 2$) are:

| $\rho$ | Triples $(d, x_0, w)$ with $\min \mathrm{drop} = 0$ | Triples $(d, x_0, w)$ with $\min \mathrm{drop} = 1$ | Triples $(d, x_0, w)$ with $\min \mathrm{drop} = 2$ (for $\rho \in \{3, 6\}$) |
|---|---|---|---|
| $0$ | $(0, 0, 0)$ | none | — |
| $1$ | $(1, 1, 4)$ | $(1, 0, 10),\ (2, 2, 7)$ | — |
| $2$ | $(1, 1, 5)$ | $(1, 0, 11),\ (2, 2, 8)$ | — |
| $3$ | $(1, 2, 0)$ | $(1, 0, 12)$ | $(2, 1, 15),\ (2, 2, 9),\ (3, 2, 18)$ |
| $4$ | $(0, 0, 4)$ | $(1, 1, 7)$ | — |
| $5$ | $(0, 0, 5)$ | $(1, 1, 8)$ | — |
| $6$ | $(0, 1, 0)$ | none | $(1, 0, 15),\ (1, 1, 9),\ (2, 1, 18),\ (2, 2, 12)$ |
| $7$ | $(0, 0, 7),\ (1, 2, 4)$ | $(1, 0, 16),\ (1, 1, 10)$ | — |
| $8$ | $(0, 0, 8),\ (1, 2, 5)$ | $(1, 0, 17),\ (1, 1, 11)$ | — |

**Proof.**
(1) Since $\ell_m(c) = c v_3(m) + \frac{c - s_3(c)}{2}$ and $s_3(c) \ge 1$, the inequality $\ell_m(c) \le \frac{5}{36} mc - \frac{1}{2}$ reduces to $5m \ge 36 v_3(m) + 18$:
- $v_3(m) = 0$ ($m \ge 4$): $5m \ge 20 > 18$;
- $v_3(m) = 1$ ($m \ne 6 \implies m \ge 12$): $5m \ge 60 > 54$;
- $v_3(m) = 2$ ($m \ne 9 \implies m \ge 18$): $5m \ge 90 = 90$;
- $v_3(m) = e \ge 3$ ($m \ge 3^e$): $5 \cdot 3^e \ge 36e + 18$ (true at $e = 3$: $135 > 126$, and $5(3^{e+1} - 3^e) = 10 \cdot 3^e \ge 270 > 36$ gives all $e \ge 3$ by induction).
Summing over the parts of a non-empty $\mu$ gives $\mathrm{cost}_3(\mu) \le \frac{5}{36} w - \frac{1}{2}$, hence $\mathrm{cost}_3(\mu) \le \lfloor (5w - 18)/36 \rfloor$.

(2)–(3) Write $Y' = q - d$ ($d \ge 0$) and $w = 9d + \rho - 6x_0 \ge 0$. Notice first that $d \ge d_{\mathrm{ref}}(\rho)$ always: if $\rho \in \{1, 2, 3\}$ and $d = 0$, then $w = \rho - 6x_0 \in \{1, 2, 3\}$, impossible since $\mu$ uses parts $\ge 4$. Set $\delta := d - d_{\mathrm{ref}}(\rho) \ge 0$, $Y_0 := q - d_{\mathrm{ref}}(\rho)$, and $e(\rho) := [\rho \in \{1, 2, 6\}] + 2[\rho = 3]$, so $\kappa_3(n) = \ell_9(Y_0) + e(\rho)$. By Lemma 4.1 and superadditivity of $v_3((\cdot)!)$,
$$\mathrm{drop}(\lambda) = \bigl(\ell_9(Y_0) - \ell_9(Y_0 - \delta)\bigr) + e(\rho) - x_0 - \mathrm{cost}_3(\mu) + \Delta_{\mathrm{trade}}(Y', t) \ge 2\delta + v_3(\delta!) + e(\rho) - x_0 - \mu_{\max}(w). \tag{4.1}$$
- If $w = 0$: $9d + \rho = 6x_0 \le 12$ with $x_0 \in \{0, 1, 2\}$ has only the three solutions $(\rho, d, x_0) \in \{(0, 0, 0), (6, 0, 1), (3, 1, 2)\}$, each with $\delta = 0$ and RHS of (4.1) equal to $0$.
- If $w > 0$: applying (1) to $\mathrm{cost}_3(\mu) \le \frac{5}{36} w - \frac{1}{2}$ in (4.1):
  - When $d_{\mathrm{ref}}(\rho) = 0$ ($\rho \in \{0, 4, 5, 6, 7, 8\}$), $w = 9\delta + \rho - 6x_0$ and
    $$\mathrm{drop}(\lambda) \ge \frac{3}{4}\delta + v_3(\delta!) + [\rho = 6] + \frac{1}{2} - \frac{5\rho + 6x_0}{36} \ge \frac{3}{4}\delta + v_3(\delta!) + \frac{1}{2} - \frac{52}{36}.$$
    For $\delta \ge 3$, the RHS is $\ge \frac{9}{4} + 1 + \frac{1}{2} - \frac{13}{9} = \frac{83}{36} > 2$, so $\mathrm{drop}(\lambda) \ge 3$.
  - When $d_{\mathrm{ref}}(\rho) = 1$ ($\rho \in \{1, 2, 3\}$), $w = 9\delta + (9 + \rho) - 6x_0$ and
    $$\mathrm{drop}(\lambda) \ge \frac{3}{4}\delta + v_3(\delta!) + [\rho = 3] + \frac{1}{4} - \frac{5\rho + 6x_0}{36} \ge \frac{3}{4}\delta + v_3(\delta!) + \frac{1}{4} - \frac{27}{36}.$$
    For $\delta \ge 3$, the RHS is $\ge \frac{9}{4} + 1 + \frac{1}{4} - \frac{3}{4} = \frac{11}{4} > 2$, so $\mathrm{drop}(\lambda) \ge 3$.

Thus every $\lambda$ with $\mathrm{drop}(\lambda) \le 2$ has $\delta \in \{0, 1, 2\}$ and $w \le 30$. By (1), $\mu_{\max}(w) \le \lfloor (5w-18)/36 \rfloor$, and exact inspection of partitions of $w \le 30$ into parts $\ge 4$ avoiding $\{6, 9\}$ gives:
- $w \in \{1, 2, 3, 6\}$: no partitions;
- $w \in \{0, 4, 5, 7, 8, 9, 10, 11, 13, 14\}$: $\mu_{\max}(w) = 0$ (no multiple of $3$ and $< 3 \cdot 4 = 12$, except $w = 13, 14$ where $12$ leaves $1, 2$ forbidden);
- $w \in \{12, 15, 16, 17, 19, 20, 21\}$: $\mu_{\max}(w) = 1$ (attained e.g. by $12, 4^3$; $15, 5^3$; $12+4, 4^4$; $12+5, 4^3 5$; etc.; note $w = 19, 20, 21$ cannot use $18$ since $1, 2, 3$ are forbidden, nor two multiples of $3$ since $12 + 12 = 24 > 21$);
- $w \in \{18, 22, 23, 24, 25, 26, 28, 29\}$: $\mu_{\max}(w) = 2$ (for $w = 18$: uniquely $18^1$);
- $w \in \{27, 30\}$: $\mu_{\max}(w) = 3$.

Evaluating the RHS of (4.1), $2\delta + v_3(\delta!) + e(\rho) - x_0 - \mu_{\max}(w)$, on all valid $(\delta, x_0) \in \{0, 1, 2\} \times \{0, 1, 2\}$ for each $\rho \in \{0, \dots, 8\}$ yields non-negative values everywhere (with $0$ attained in every $\rho$ by $9^q$, $9^q \rho$, $9^q 6$, $9^{q-1} 6 (3+\rho)$, or $9^{q-1} 6^2$) and produces the exact table above.

Finally, for the valuation identity in (2), Legendre's formula gives $v_3((9q+\rho)!) = 4q + v_3(q!) + \lfloor \rho/3 \rfloor$, while $v_3((n-1)_3) = 2 + v_3(q)$ for $\rho \in \{1, 2, 3\}$ and $v_3((n-1)_3) = 1$ for $\rho \in \{0, 4, 5, 6, 7, 8\}$. Subtracting $\kappa_3(n) + v_3((n-1)_3)$ cancels $v_3(q!)$ and $v_3(q)$ identically in every residue class:
- $\rho \in \{0, 1, 2, 3\}$: $2q - 1 = \lfloor (n-4)/9 \rfloor + \lfloor (n+2)/9 \rfloor$;
- $\rho \in \{4, 5, 6\}$: $2q = \lfloor (n-4)/9 \rfloor + \lfloor (n+2)/9 \rfloor$;
- $\rho \in \{7, 8\}$: $2q + 1 = \lfloor (n-4)/9 \rfloor + \lfloor (n+2)/9 \rfloor$. $\square$

### Lemma 4.3 (Exact Mod-$9$ Sum of the $\{6, 9\}$-Trades)
Let $x_0 \in \{1, 2\}$ and let $y \ge 5$ satisfy $y \equiv 2 \pmod 3$. For $0 \le t \le \lfloor y/2 \rfloor$, put
$$\tau_t(x_0, y) := \frac{9^{2t}\, y! / (y - 2t)!}{6^{3t}\, (x_0 + 3t)! / x_0!} = \frac{3^t \prod_{i=0}^{2t-1}(y - i)}{8^t \prod_{j=1}^{3t}(x_0 + j)}.$$
Then $\tau_t(x_0, y) \in \mathbb{Z}_{(3)}$ for all $t$, $v_3(\tau_t(x_0, y)) = \Delta_{\mathrm{trade}}(y, t)$ (so $\tau_t(x_0, y) \equiv 0 \pmod 9$ for all $t \ge 5$), and setting $S(x_0, y) := \sum_{t=0}^{\min(4, \lfloor y/2 \rfloor)} \tau_t(x_0, y)$, we have:
1. $1 + \tau_1(x_0, y) \equiv 3 \pmod 9$ if $x_0 = 1$, and $1 + \tau_1(x_0, y) \equiv 0 \pmod 9$ if $x_0 = 2$;
2. Modulo $9$, $S(x_0, y)$ depends only on $(x_0, y \bmod 9)$ as follows:

| $x_0$ | $y \equiv 2 \pmod 9$ ($y \ge 11$) | $y \equiv 5 \pmod 9$ ($y \ge 5$) | $y \equiv 8 \pmod 9$ ($y \ge 8$) |
|---|---|---|---|
| $x_0 = 1$ | $S \equiv 3 \pmod 9$ | $S \equiv 0 \pmod 9$ | $S \equiv 6 \pmod 9$ |
| $x_0 = 2$ | $S \equiv 0 \pmod 9$ | $S \equiv 6 \pmod 9$ | $S \equiv 3 \pmod 9$ |

**Proof.** The identity $v_3(\tau_t(x_0, y)) = \Delta_{\mathrm{trade}}(y, t)$ is immediate from Lemma 4.1 (since $v_3(\tau_t)$ equals the cost difference $\mathrm{cost}_3(9^y 6^{x_0}) - \mathrm{cost}_3(9^{y-2t} 6^{x_0+3t})$). We compute each $\tau_t \bmod 9$ directly (noting that for $y \equiv 2 \pmod 3$, $y(y-1) \equiv 2 \pmod 9$, as $2\cdot 1 = 2$, $5\cdot 4 = 20 \equiv 2$, $8\cdot 7 = 56 \equiv 2 \pmod 9$):
- **$t = 0$:** $\tau_0 = 1$.
- **$t = 1$:** For $x_0 = 1$, $\tau_1 = \frac{3 y(y-1)}{8 \cdot 24} = \frac{y(y-1)}{64} \equiv \frac{2}{1} = 2 \pmod 9$, so $1 + \tau_1 \equiv 3 \pmod 9$. For $x_0 = 2$, $\tau_1 = \frac{3 y(y-1)}{8 \cdot 60} = \frac{y(y-1)}{160} \equiv \frac{2}{-2} \equiv 8 \pmod 9$, so $1 + \tau_1 \equiv 0 \pmod 9$.
- **$t = 2$:** $\tau_2 = \frac{9\,y(y-1)(y-2)(y-3)}{64 \cdot (x_0+1)\cdots(x_0+6)}$. Note $\frac{(x_0+1)\cdots(x_0+6)}{9}$ equals $560 \equiv 2 \pmod 3$ ($x_0 = 1$) or $2240 \equiv 2 \pmod 3$ ($x_0 = 2$), and $64 \equiv 1 \pmod 3$.
  - If $y \equiv 2 \pmod 9$: $9 \mid (y-2)$, so $\tau_2 \equiv 0 \pmod 9$.
  - If $y \equiv 5 \pmod 9$: $\frac{y(y-1)(y-2)(y-3)}{3} \equiv 2 \cdot 1 \cdot 1 \cdot 2 \equiv 1 \pmod 3$, so $\tau_2 \equiv 3 \cdot \frac{1}{1 \cdot 2} \equiv 6 \pmod 9$.
  - If $y \equiv 8 \pmod 9$: $\frac{y(y-1)(y-2)(y-3)}{3} \equiv 2 \cdot 1 \cdot 2 \cdot 2 \equiv 2 \pmod 3$, so $\tau_2 \equiv 3 \cdot \frac{2}{1 \cdot 2} \equiv 3 \pmod 9$.
- **$t = 3, 4$:** By Lemma 4.1(3), $\tau_3 \equiv \tau_4 \equiv 0 \pmod 9$ unless $y \equiv 8 \pmod 9$ (in which case $y \ge 8$, so $t = 3, 4$ both occur). For $y \equiv 8 \pmod 9$:
  - $t = 3$: $\frac{y(y-1)\cdots(y-5)}{9} \equiv 2 \cdot 1 \cdot 2 \cdot 2 \cdot 1 \cdot 1 \equiv 2 \pmod 3$, $8^3 \equiv 2 \pmod 3$, and $\frac{\prod_{j=1}^9(x_0+j)}{81}$ equals $44800 \equiv 1 \pmod 3$ ($x_0=1$) or $246400 \equiv 1 \pmod 3$ ($x_0=2$); hence $\tau_3 \equiv 3 \cdot \frac{2}{2 \cdot 1} \equiv 3 \pmod 9$.
  - $t = 4$: $\frac{y(y-1)\cdots(y-7)}{9} \equiv 2 \cdot 1 \cdot 2 \cdot 2 \cdot 1 \cdot 1 \cdot 2 \cdot 1 \equiv 1 \pmod 3$, $8^4 \equiv 1 \pmod 3$, and $\frac{\prod_{j=1}^{12}(x_0+j)}{243}$ equals $25625600 \equiv 2 \pmod 3$ ($x_0=1$) or $179379200 \equiv 2 \pmod 3$ ($x_0=2$); hence $\tau_4 \equiv 3 \cdot \frac{1}{1 \cdot 2} \equiv 6 \pmod 9$.

Summing $\tau_0 + \tau_1 + \tau_2 + \tau_3 + \tau_4 \pmod 9$ in all six cells produces $3, 3+6 \equiv 0, 3+3+3+6 \equiv 6$ for $x_0 = 1$, and $0, 0+6 \equiv 6, 0+3+3+6 \equiv 3$ for $x_0 = 2$. $\square$

### Theorem 4 (Complete $3$-adic Classification for $r = 3$, All $n \ge 5$)
For every integer $n \ge 5$, put $L_3(n) := v_3(\Lambda_3(n)) = v_3((n-1)_3) + \lfloor (n-4)/9 \rfloor + \lfloor (n+2)/9 \rfloor$. Then:
$$v_3\bigl(g_3(n)\bigr) = L_3(n) + \delta_3(n), \qquad v_3\bigl(G_3(n)\bigr) = L_3(n) + \delta_3^G(n),$$
where
$$\delta_3(n) = \begin{cases} 2 & n \equiv 51 \pmod{81},\ n \ge 51, \\ 1 & n \equiv 1, 2, 3, 24 \pmod{27},\ n \not\equiv 51 \pmod{81},\ n \ge 55, \\ 0 & \text{otherwise,} \end{cases}$$
$$\delta_3^G(n) = \begin{cases} 2 & n \equiv 30, 51 \pmod{81},\ n \ge 51, \\ 1 & n \equiv 1, 2, 3, 24 \pmod{27},\ n \not\equiv 30, 51 \pmod{81},\ n \ge 55, \\ 0 & \text{otherwise.} \end{cases}$$

**Proof.** Write $n = 9q + \rho$ ($0 \le \rho \le 8$). We partition all $n \ge 5$ into four exhaustive cases.

#### Case 1: $n \in \{5, 6, 7, 8, 9\}$.
Direct computation of single-removal counts gives:
- $n = 5$: $a_{S_4}(5) = 24$, $v_3(24) = 1 = L_3(5)$;
- $n = 6$: $a_{S_5}(6) = 120$, $v_3(120) = 1 = L_3(6)$;
- $n = 7$: $a_{S_4}(7) = 720$, $v_3(720) = 2 = L_3(7)$;
- $n = 8$: $a_{S_5}(8) = 7! + \frac{8!}{4^2 \cdot 2!} = 5040 + 1260 = 6300$, $v_3(6300) = 2 = L_3(8)$;
- $n = 9$: $a_{S_4}(9) = 8! = 40320$, $v_3(40320) = 2 = L_3(9)$.
Since $\Lambda_3(n) \mid g_3(n) \mid G_3(n) \mid a_{S_k}(n)$, we have $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n)$ for all $n \in \{5, 6, 7, 8, 9\}$.

#### Case 2: $n \ge 10$ and $n \not\equiv 1, 2, 3, 24 \pmod{27}$ (23 residue classes modulo 27).
We show $v_3(G_3(n)) = L_3(n)$, forcing $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n)$.
- **Subcase 2a: $\rho \in \{0, 4, 5, 7, 8\}$.** Consider $a_{S_6}(n)$ (excluding part $6$). Every partition avoiding $6$ has $x_0 = 0$ and $t = 0$. From the $\min \mathrm{drop} = 0$ column of Lemma 4.2, the only surviving triple $(d, x_0, w)$ with $x_0 = 0$ is $(0, 0, \rho)$:
  - For $\rho \in \{0, 4, 5, 7\}$, the unique partition of $w = \rho$ avoiding $\{6, 9\}$ is $\emptyset, 4^1, 5^1, 7^1$ respectively, so $a_{S_6}(n)$ has a **unique** partition of cost $\kappa_3(n)$ (namely $9^q$ or $9^q \rho^1$). By Lemma 1(3), $v_3(a_{S_6}(n)) = L_3(n)$.
  - For $\rho = 8$, the partitions of $w = 8$ avoiding $\{6, 9\}$ are $8^1$ and $4^2$, so the only two cost-$\kappa_3(n)$ partitions surviving in $a_{S_6}(n)$ are $9^q 8^1$ and $9^q 4^2$. Their sum is
    $$N(9^q 8^1) + N(9^q 4^2) = \frac{n!}{9^q q!}\left(\frac{1}{8} + \frac{1}{4^2 \cdot 2!}\right) = \frac{n!}{9^q q!} \cdot \frac{5}{32},$$
    whose $3$-adic valuation is $v_3(n!) - \ell_9(q) = L_3(n)$ since $3 \nmid 5, 32$. Hence $v_3(a_{S_6}(n)) = L_3(n)$.
- **Subcase 2b: $\rho \in \{1, 2, 3, 6\}$ with $n \not\equiv 1, 2, 3, 24 \pmod{27}$.** Here $Y_0 = q - d_{\mathrm{ref}}(\rho)$ satisfies $Y_0 \not\equiv 2 \pmod 3$. By Lemma 4.1(1), $\Delta_{\mathrm{trade}}(Y_0, t) = 0$ forces $t = 0$. From Lemma 4.2, the unique triple with $\min \mathrm{drop} = 0$ is $(d_{\mathrm{ref}}(\rho), x_0, w) \in \{(1, 1, 4), (1, 1, 5), (1, 2, 0), (0, 1, 0)\}$, each having a unique $\mu$, so $\mathcal{P}_{>3}(n)$ contains a **unique** partition of cost $\kappa_3(n)$ (namely $9^{q-1}6^1 4^1$, $9^{q-1}6^1 5^1$, $9^{q-1}6^2$, or $9^q 6^1$). By Lemma 1(2)–(3), $v_3(G_3(n)) \le v_3(a_{S_\infty}(n)) = L_3(n)$.

#### Case 3: $n \in \{24, 28, 29, 30\}$.
Here $Y_0 = 2$. By Lemmas 4.1 and 4.2, the only two partitions of cost $\kappa_3(n)$ are $9^2 6^{x_0} \mu$ and $6^{x_0+3} \mu$ (with $(x_0, \mu) = (1, \emptyset), (1, 4^1), (1, 5^1), (2, \emptyset)$ respectively). In $a_{S_9}(n)$ (excluding $9$), the first is eliminated while the second ($6^4, 6^4 4^1, 6^4 5^1, 6^5$) survives as the unique cost-$\kappa_3(n)$ partition. By Lemma 1(3), $v_3(a_{S_9}(n)) = L_3(n)$, so $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n)$.

#### Case 4: $n \ge 51$ and $n \equiv 1, 2, 3, 24 \pmod{27}$ (12 residue classes modulo 81).
Put $y := q - d_{\mathrm{ref}}(\rho)$, so $y \equiv 2 \pmod 3$ and $y \ge 5$ (specifically $y = 5$ at $n = 51, 55, 56, 57$). Write $(x_0, \mu_0)$ for the unique $\min \mathrm{drop} = 0$ configuration of Lemma 4.2: $(1, 4^1)$ for $\rho = 1$, $(1, 5^1)$ for $\rho = 2$, $(2, \emptyset)$ for $\rho = 3$, and $(1, \emptyset)$ for $\rho = 6$.

First, by Lemmas 4.1(1) and 4.2, the **only** partitions in $\mathcal{P}_{>3}(n)$ of cost $\kappa_3(n)$ are
$$\lambda_0 = 9^y \cdot 6^{x_0} \cdot \mu_0 \qquad \text{and} \qquad \lambda_1 = 9^{y-2} \cdot 6^{x_0+3} \cdot \mu_0.$$
Because $y \ge 5$, we have $y - 2 \ge 3 > 0$, so $\lambda_0$ and $\lambda_1$ have the **exact same part set** $P_0 = \mathrm{supp}(\lambda_0) \in \{\{4, 6, 9\}, \{5, 6, 9\}, \{6, 9\}\}$. By Lemma 4.3(1),
$$N(\lambda_0) + N(\lambda_1) = N(\lambda_0)\bigl(1 + \tau_1(x_0, y)\bigr) \equiv 0 \pmod{3^{L_3(n) + 1}}.$$
By Lemma 1(1), it follows immediately that **$v_3(g_3(n)) \ge L_3(n) + 1$** for all $n$ in Case 4. We now determine $v_3(g_3(n))$ and $v_3(G_3(n))$ on each of the 12 residue classes modulo $81$.

- **Subcase 4a: $n \equiv 1 \pmod{27}$, $n \ge 55$ ($\rho = 1$, $n \equiv 1, 28, 55 \pmod{81}$).**
  Consider all partitions $\lambda \in \mathcal{P}_{>3}(n)$ containing part $7$ with $\mathrm{drop}(\lambda) \le 1$. By Lemma 4.2, the only triples $(d, x_0, w)$ with $\min \mathrm{drop} \le 1$ are $(1, 1, 4)$, $(1, 0, 10)$, and $(2, 2, 7)$. Neither $w = 4$ nor $w = 10$ can contain part $7$ (since $10 - 7 = 3 < 4$). At $(2, 2, 7)$, we have $w = 7$ (so uniquely $\mu = 7^1$) and $Y' = q - 2 = y - 1 \equiv 1 \pmod 3$, so Lemma 4.1(1) forces $t = 0$ (any $t \ge 1$ adds $\Delta_{\mathrm{trade}} \ge 1$, giving $\mathrm{drop} \ge 2$). Also $v_3(y!) - v_3((y-1)!) = v_3(y) = 0$. Hence **$9^{y-1} 6^2 7^1$ is the unique partition in $\mathcal{P}_{>3}(n)$ containing $7$ of cost $\ge \kappa_3(n) - 1$** (and has exact cost $\kappa_3(n) - 1$). By Lemma 1(2)–(3),
  $$v_3(G_3(n)) \le v_3\bigl(a_{S_\infty}(n) - a_{S_7}(n)\bigr) = L_3(n) + 1.$$
  Combined with $v_3(g_3(n)) \ge L_3(n) + 1$, this yields $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n) + 1$.

- **Subcase 4b: $n \equiv 2 \pmod{27}$, $n \ge 56$ ($\rho = 2$, $n \equiv 2, 29, 56 \pmod{81}$).**
  By Lemma 4.2, the only triples with $\min \mathrm{drop} \le 1$ are $(1, 1, 5)$, $(1, 0, 11)$, and $(2, 2, 8)$. Neither $w = 5$ nor $w = 11$ can contain part $8$ (since $11 - 8 = 3 < 4$). At $(2, 2, 8)$, the only partition of $8$ containing $8$ is $\mu = 8^1$, and $Y' = y - 1 \equiv 1 \pmod 3$ forces $t = 0$ with $v_3(y) = 0$. Hence **$9^{y-1} 6^2 8^1$ is the unique partition containing $8$ of cost $\ge \kappa_3(n) - 1$** (with exact cost $\kappa_3(n) - 1$). By Lemma 1(2)–(3), $v_3(G_3(n)) \le v_3(a_{S_\infty}(n) - a_{S_8}(n)) = L_3(n) + 1$, giving $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n) + 1$.

- **Subcase 4c: $n \equiv 24, 78 \pmod{81}$, $n \ge 78$ ($\rho = 6$, $y = q \equiv 2, 8 \pmod 9$).**
  By Lemma 4.2, the $\min \mathrm{drop} = 1$ column for $\rho = 6$ is empty, so **every** partition in $\mathcal{P}_{>3}(n)$ with $\mathrm{drop}(\lambda) \le 1$ comes from $(0, 1, 0)$, namely $\lambda_t = 9^{y-2t} 6^{1+3t}$ with $0 \le t \le \min(4, \lfloor y/2 \rfloor)$ (by Lemma 4.1(2)). Every $\lambda_t$ avoids part $5$, so all of them survive in $a_{S_5}(n)$. Hence
  $$a_{S_5}(n) \equiv \sum_{t=0}^{\min(4, \lfloor y/2 \rfloor)} N(\lambda_t) = N(\lambda_0)\, S(1, y) \pmod{3^{L_3(n) + 2}}.$$
  By Lemma 4.3(2), $S(1, y) \equiv 3 \pmod 9$ (if $y \equiv 2 \pmod 9$) or $6 \pmod 9$ (if $y \equiv 8 \pmod 9$), so $v_3(S(1, y)) = 1$ and $v_3(a_{S_5}(n)) = L_3(n) + 1$. Thus $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n) + 1$.

- **Subcase 4d: $n \equiv 3, 57 \pmod{81}$, $n \ge 57$ ($\rho = 3$, $y = q - 1 \equiv 5, 8 \pmod 9$).**
  By Lemmas 4.1 and 4.2, the partitions in $\mathcal{P}_{>3}(n)$ with $\mathrm{drop}(\lambda) \le 1$ fall into two disjoint sets:
  1. From $(1, 2, 0)$: $\lambda_t = 9^{y-2t} 6^{2+3t}$ for $0 \le t \le \min(4, \lfloor y/2 \rfloor)$ (with sum $N(\lambda_0) S(2, y)$);
  2. From $(1, 0, 12)$ (which already has $\min \mathrm{drop} = 1$, so $\Delta_{\mathrm{trade}}(y, t) = 0$, forcing $t \in \{0, 1\}$ by Lemma 4.1(1); note $y \ge 5 \implies y - 2 \ge 3 > 0$; and $w = 12$ has top-cost partitions $\mu \in \{4^3, 12^1\}$): the four partitions
     $$9^y 4^3, \quad 9^y 12^1, \quad 9^{y-2} 6^3 4^3, \quad 9^{y-2} 6^3 12^1,$$
     all of cost $\kappa_3(n) - 1$.

  Notice none of these partitions contain part $5$, so all survive in $a_{S_5}(n)$. The sum of the four partitions in (2) factors as
  $$\frac{n!}{9^y y!} \left(1 + \frac{9^2 y(y-1)}{6^3 \cdot 3!}\right) \left(\frac{1}{4^3 \cdot 3!} + \frac{1}{12}\right) = \frac{n!}{9^y y!} \left(1 + \frac{y(y-1)}{16}\right) \cdot \frac{11}{128}. \tag{4.2}$$
  Since $y \equiv 2 \pmod 3$, $y(y-1) \equiv 2 \pmod 3$ and $16 \equiv 1 \pmod 3$, so $1 + y(y-1)/16 \equiv 0 \pmod 3$; meanwhile $v_3(n! / (9^y y!)) = v_3(n!) - \ell_9(y) = L_3(n) + 2$, so (4.2) has $3$-adic valuation $\ge L_3(n) + 3$! (Even without the second factor, $v_3(11/128) = 0$ already gives $v_3 \ge L_3(n) + 2$.) Therefore
  $$a_{S_5}(n) \equiv N(\lambda_0)\, S(2, y) \pmod{3^{L_3(n) + 2}}.$$
  By Lemma 4.3(2), $S(2, y) \equiv 6 \pmod 9$ ($y \equiv 5 \pmod 9$) or $3 \pmod 9$ ($y \equiv 8 \pmod 9$), so $v_3(a_{S_5}(n)) = L_3(n) + 1$. Thus $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n) + 1$.

- **Subcase 4e: $n \equiv 51 \pmod{81}$, $n \ge 51$ ($\rho = 6$, $y = q \equiv 5 \pmod 9$, $y \ge 5$).**
  By Lemmas 4.1(3) and 4.2, the **only** partitions in $\mathcal{P}_{>3}(n)$ with $\mathrm{drop}(\lambda) \le 1$ are $\lambda_0 = 9^y 6^1$, $\lambda_1 = 9^{y-2} 6^4$, and $\lambda_2 = 9^{y-4} 6^7$. Since $y \ge 5$, we have $y - 4 \ge 1$, so all three have the **exact same part set** $P_0 = \{6, 9\}$. By Lemma 4.3(2),
  $$N(\lambda_0) + N(\lambda_1) + N(\lambda_2) = N(\lambda_0)\, S(1, y) \equiv 0 \pmod{3^{L_3(n) + 2}}.$$
  Since every other partition in $\mathcal{P}_{>3}(n)$ has $v_3(N(\lambda)) \ge L_3(n) + 2$, Lemma 1(1) gives **$v_3(g_3(n)) \ge L_3(n) + 2$**.

  For the matching upper bound on $v_3(G_3(n))$, consider all partitions $\lambda \in \mathcal{P}_{>3}(n)$ containing part $15$ with $\mathrm{drop}(\lambda) \le 2$. From the $\rho = 6$ row of Lemma 4.2, the only triples with $\min \mathrm{drop} \le 2$ are $(0, 1, 0)$, $(1, 0, 15)$, $(1, 1, 9)$, $(2, 1, 18)$, and $(2, 2, 12)$. None of $w \in \{0, 9, 12, 18\}$ can contain part $15$ (as $18 - 15 = 3 < 4$). At $(1, 0, 15)$, the unique partition of $15$ containing $15$ is $\mu = 15^1$, and $Y' = q - 1 \equiv 4 \equiv 1 \pmod 3$, so Lemma 4.1(1) forces $t = 0$ (any $t \ge 1$ drops cost by $\ge 1$, making $\mathrm{drop} \ge 3$), while $v_3(q!) - v_3((q-1)!) = v_3(q) = 0$. Hence **$9^{y-1} 15^1$ is the unique partition containing $15$ of cost $\ge \kappa_3(n) - 2$** (and has exact cost $\kappa_3(n) - 2$). By Lemma 1(2)–(3) (valid since $15 < 51 \le n$),
  $$v_3(G_3(n)) \le v_3\bigl(a_{S_\infty}(n) - a_{S_{15}}(n)\bigr) = L_3(n) + 2.$$
  Therefore $v_3(g_3(n)) = v_3(G_3(n)) = L_3(n) + 2$.

- **Subcase 4f: $n \equiv 30 \pmod{81}$, $n \ge 111$ ($\rho = 3$, $y = q - 1 \equiv 2 \pmod 9$, $y \ge 11$).**
  By Lemmas 4.1(3) and 4.2, the **only** partitions in $\mathcal{P}_{>3}(n)$ with $\mathrm{drop}(\lambda) \le 1$ are the **six** partitions:
  - at cost $\kappa_3(n)$: $\lambda_0 = 9^y 6^2$ and $\lambda_1 = 9^{y-2} 6^5$ (note $y \equiv 2 \pmod 9 \implies \Delta_{\mathrm{trade}}(y, t) \ge 2$ for all $t \ge 2$);
  - at cost $\kappa_3(n) - 1$: the $2 \times 2$ product $\{9^y, 9^{y-2} 6^3\} \times \{4^3, 12^1\}$.

  We have three cancellations:
  1. $N(9^y 6^2) + N(9^{y-2} 6^5) = N(\lambda_0)(1 + \tau_1(2, y)) \equiv 0 \pmod{3^{L_3(n) + 2}}$ (Lemma 4.3(1));
  2. For each $\mu \in \{4^3, 12^1\}$, $N(9^y \mu) + N(9^{y-2} 6^3 \mu) = N(9^y \mu)\bigl(1 + \frac{y(y-1)}{16}\bigr) \equiv 0 \pmod{3^{L_3(n) + 2}}$ (since $y(y-1) \equiv 2 \pmod 3$ and $16 \equiv 1 \pmod 3$);
  3. For each $\nu \in \{9^y, 9^{y-2} 6^3\}$, $N(\nu \cdot 4^3) + N(\nu \cdot 12^1) = N(\nu \cdot 12^1)\bigl(1 + \frac{12}{4^3 \cdot 3!}\bigr) = N(\nu \cdot 12^1) \cdot \frac{33}{32} \equiv 0 \pmod{3^{L_3(n) + 2}}$.

  Now check $a_{S_k}(n)$ modulo $3^{L_3(n) + 2}$ for every $k \in \{4, \dots, n\}$:
  - $k \notin \{4, 6, 9, 12\}$: all six partitions survive, cancelling by (1) and (2);
  - $k = 4$: $\{9^y 6^2, 9^{y-2} 6^5\}$ and $\{9^y 12^1, 9^{y-2} 6^3 12^1\}$ survive, cancelling by (1) and (2);
  - $k = 12$: $\{9^y 6^2, 9^{y-2} 6^5\}$ and $\{9^y 4^3, 9^{y-2} 6^3 4^3\}$ survive, cancelling by (1) and (2);
  - $k = 6$: only $\{9^y 4^3, 9^y 12^1\}$ survives, cancelling by (3);
  - $k = 9$: none of the six survive (as $y - 2 \ge 9 > 0$).

  Hence $v_3(a_{S_k}(n)) \ge L_3(n) + 2$ for every $k \in \{4, \dots, n\}$, so **$v_3(G_3(n)) \ge L_3(n) + 2$**.

  For the matching upper bound on $v_3(G_3(n))$, examine $a_{S_6}(n)$ modulo $3^{L_3(n) + 3}$. Every partition avoiding $6$ has $x_0 = 0$ and $t = 0$. In the $\rho = 3$ row of Lemma 4.2, every triple with $\min \mathrm{drop} \le 2$ except $(1, 0, 12)$ has $x_0 \ge 1$ (namely $(1, 2, 0), (2, 1, 15), (2, 2, 9), (3, 2, 18)$). Thus the **only** partitions avoiding $6$ with $\mathrm{drop}(\lambda) \le 2$ have $9^y$ multiplied by a partition $\mu$ of $w = 12$ avoiding $\{6, 9\}$ of cost $\ge 0$ — i.e., **all** partitions of $12$ into parts $\ge 4$ avoiding $\{6, 9\}$, which are precisely $12^1, 4^3, 5^1 7^1, 4^1 8^1$. Therefore
  $$a_{S_6}(n) \equiv \frac{n!}{9^y y!} \left(\frac{1}{12} + \frac{1}{4^3 \cdot 3!} + \frac{1}{5 \cdot 7} + \frac{1}{4 \cdot 8}\right) = \frac{n!}{9^y y!} \cdot \frac{653}{4480} \pmod{3^{L_3(n) + 3}}.$$
  Since $3 \nmid 653$ and $3 \nmid 4480$, while $v_3(n! / (9^y y!)) = v_3(n!) - \ell_9(y) = v_3(n!) - (\kappa_3(n) - 2) = L_3(n) + 2$, we obtain **$v_3(a_{S_6}(n)) = L_3(n) + 2$**, and hence **$v_3(G_3(n)) = L_3(n) + 2$**.

  Finally, for $P = \{4, 9\}$ (equivalently $S = \mathbb{N} \setminus \{4, 9\}$, as in Kallat's Proposition 11.2), among the six partitions of cost $\ge \kappa_3(n) - 1$, the **unique** one with part set $\{4, 9\}$ (or subset of $\{4, 9\}$) is $9^y 4^3$, of cost $\kappa_3(n) - 1$. By Lemma 1(3), $v_3(f_{\{4,9\}}(n)) = L_3(n) + 1$, so $v_3(g_3(n)) \le L_3(n) + 1$. Combined with $v_3(g_3(n)) \ge L_3(n) + 1$, this gives **$v_3(g_3(n)) = L_3(n) + 1$**. $\square$

---

## 5. Complete Synthesis for $r = 3$ (Theorem 1)

### Theorem 1 (Resolution of Q1 and of Q3, Q4 for $r = 3$)
For every integer $n \ge 5$:
- **(a) Exact $2$-adic exponent (Q3 for $r = 3, p = 2$):**
  $$v_2\!\left(\frac{\Lambda_3(n)}{(n-1)_3}\right) = v_2\!\left(\frac{g_3(n)}{(n-1)_3}\right) = v_2\!\left(\frac{G_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-2}{4} \right\rfloor.$$
- **(b) Exact $3$-adic exponent (Q3 for $r = 3, p = 3$):**
  $$v_3\!\left(\frac{\Lambda_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-4}{9} \right\rfloor + \left\lfloor \frac{n+2}{9} \right\rfloor, \qquad v_3\!\left(\frac{g_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-4}{9} \right\rfloor + \left\lfloor \frac{n+2}{9} \right\rfloor + \delta_3(n),$$
  $$v_3\!\left(\frac{G_3(n)}{(n-1)_3}\right) = \left\lfloor \frac{n-4}{9} \right\rfloor + \left\lfloor \frac{n+2}{9} \right\rfloor + \delta_3^G(n),$$
  with $\delta_3(n)$ and $\delta_3^G(n)$ as in Theorem 4.
- **(c) Exact comparison of $\Lambda_3(n)$ and $g_3(n)$ (Q4 for $r = 3$):**
  $$\frac{g_3(n)}{\Lambda_3(n)} = 3^{\delta_3(n)},$$
  so $\Lambda_3(n) \ne g_3(n)$ if and only if $n \equiv 1, 2, 3, 24 \pmod{27}$ and $n \ge 51$ (with ratio $9$ when $n \equiv 51 \pmod{81}$, and ratio $3$ on the remaining 11 classes modulo $81$ with $n \ge 55$).
- **(d) Exact comparison of $g_3(n)$ and $G_3(n)$ (Q1):**
  $$\frac{G_3(n)}{g_3(n)} = 3^{\delta_3^G(n) - \delta_3(n)} = \begin{cases} 3 & \text{if } n \equiv 30 \pmod{81} \text{ and } n \ge 111, \\ 1 & \text{otherwise.} \end{cases}$$
  In particular, $g_3(n) \ne G_3(n)$ if and only if $n \equiv 30 \pmod{81}$ and $n \ge 111$.

**Proof.** By Kallat's Theorem 5.1 (`\label{thm:gcdfamily}`), for every prime $q > 3$ and every $n \ge 5$,
$$v_q\bigl((n-1)_3\bigr) = v_q\bigl(g_3(n)\bigr) = v_q\bigl(G_3(n)\bigr).$$
We verify that $v_q(\Lambda_3(n)) = v_q((n-1)_3)$ for every prime $q \ge 5$ and every $n \ge 5$ as well. Since $\Lambda_3(n) \mid g_3(n)$, we already have $v_q(\Lambda_3(n)) \le v_q((n-1)_3)$. For the reverse inequality, fix a prime $q \ge 5$ and any partition $\lambda \in \mathcal{P}_{>3}(n)$, and write $n = qt + s$ with $0 \le s \le q - 1$ and $\lambda = q^X \cdot \mu$ where $\mu$ avoids $q$. First observe that every integer $m \ge 4$ with $m \ne q$ and every $c \ge 1$ satisfies
$$\ell_m(c) = c\,v_q(m) + \frac{c - s_q(c)}{q - 1} \le \frac{mc}{2(q - 1)} - \frac{1}{q - 1}.$$
Indeed, $s_q(c) \ge 1$, and checking $\frac{(q-1)v_q(m) + 1}{m} \le \frac{1}{2}$ by $e = v_q(m)$:
- $e = 0$ ($m \ge 4$): $\frac{1}{m} \le \frac{1}{4} < \frac{1}{2}$;
- $e = 1$ ($m \ne q \implies m \ge 2q$): $\frac{q}{m} \le \frac{q}{2q} = \frac{1}{2}$;
- $e \ge 2$ ($m \ge q^e$): $\frac{(q-1)e + 1}{q^e} \le \frac{2q - 1}{q^2} < \frac{1}{2}$ (as $q \ge 5 \implies q^2 > 4q - 2$, and the ratio decreases in $e \ge 2$).

Summing over the parts of any non-empty $\mu$ of weight $w > 0$ gives $\mathrm{cost}_q(\mu) \le \frac{w - 2}{2(q - 1)}$. Now consider the two possibilities for $s$:
- **If $s \in \{0, 4, 5, \dots, q - 1\}$:** Here $q \nmid (n-1)(n-2)(n-3)$, so $v_q((n-1)_3) = 0$. Write $X = t - \Delta$ with $\Delta \ge 0$ and $w = q\Delta + s$. If $\Delta = 0$, then $w = s < q$, so $\mu$ contains no multiple of $q$ and has at most $\lfloor s/4 \rfloor < q$ parts, giving $\mathrm{cost}_q(\mu) = 0$. If $\Delta \ge 1$, then $\mathrm{cost}_q(\mu) \le \frac{q\Delta + q - 3}{2(q-1)} < \Delta + 1$ (since $q\Delta + q - 3 < 2(q-1)\Delta + 2(q-1) \iff 0 < (q-2)\Delta + q + 1$), so by integrality $\mathrm{cost}_q(\mu) \le \Delta \le \ell_q(t) - \ell_q(t - \Delta)$. Thus $\mathrm{cost}_q(\lambda) \le \ell_q(t) = v_q((qt)!) = v_q(n!)$, giving $v_q(N(\lambda)) \ge 0 = v_q((n-1)_3)$.
- **If $s \in \{1, 2, 3\}$:** Since $n \ge 5$, we have $t \ge 1$, and $qt \in \{n-1, n-2, n-3\}$ gives $v_q((n-1)_3) = 1 + v_q(t)$. Because $s \in \{1, 2, 3\}$ cannot be partitioned into parts $\ge 4$, we must have $X \le t - 1$. Put $\Delta := (t - 1) - X \ge 0$, so $w = q\Delta + q + s$. If $\Delta = 0$, then $w = q + s \le q + 3 < 2q$, so $\mu$ contains no multiple of $q$ and has at most $\lfloor (q+3)/4 \rfloor < q$ parts, giving $\mathrm{cost}_q(\mu) = 0$. If $\Delta \ge 1$, then $\mathrm{cost}_q(\mu) \le \frac{q\Delta + q + 1}{2(q-1)} < \Delta + 1$ (since $q\Delta + q + 1 < 2(q-1)\Delta + 2(q-1) \iff 3 - q < (q-2)\Delta$, valid for $q \ge 5$ and $\Delta \ge 1$), so by integrality $\mathrm{cost}_q(\mu) \le \Delta \le \ell_q(t - 1) - \ell_q(t - 1 - \Delta)$. In either case $\mathrm{cost}_q(\lambda) \le \ell_q(t - 1) = v_q((q(t-1))!)$, hence
  $$v_q\bigl(N(\lambda)\bigr) = v_q(n!) - \mathrm{cost}_q(\lambda) \ge v_q((qt)!) - v_q((q(t-1))!) = 1 + v_q(t) = v_q\bigl((n-1)_3\bigr).$$

Thus $v_q(\Lambda_3(n)) = v_q(g_3(n)) = v_q(G_3(n)) = v_q((n-1)_3)$ for every prime $q > 3$ and every $n \ge 5$. Combining this with Theorem 3 ($p = 2$) and Theorem 4 ($p = 3$) proves parts (a), (b), (c), and (d) of Theorem 1 in full. $\square$

# Proof of Garrison–Seiler–Knowles (`arXiv:2401.09497v1`) Conjecture 5.2

## Theorem

Let $k \ge 1$ be a natural number and let $[k] = \{1, 2, \dots, k\}$. Following Definition 1.1 (`\label{def:weak_consec}`) of Thomas Garrison, Chris Seiler, and Andrew Knowles, *"Weakly Consecutive Sequences"* (`arXiv:2401.09497v1`, Section 1), a permutation $\sigma : [k] \to [k]$ is **weakly consecutive** (a **WCS**) if for all $i, j \in [k]$ and all integers $m$,
$$m \mid \sigma(i) \text{ and } m \mid (i - j) \implies m \mid \sigma(j).$$
Then **Conjecture 5.2** (`\label{conj:1 at end}`, Section 5) holds for every $k \ge 1$:
$$\sigma(1) = 1 \quad \text{or} \quad \sigma(k) = 1.$$

---

## Proof

For $k = 1$, $\sigma(1) = 1$ holds trivially. For $k = 2$, the only permutations of $[2]$ are $(1, 2)$ and $(2, 1)$, both of which satisfy $\sigma(1) = 1$ or $\sigma(2) = 1$. Assume henceforth that $k \ge 3$.

### 1. Reversal, residue-class characterization, and the GCD representation

We collect three elementary properties of any WCS $\sigma : [k] \to [k]$.

**Lemma 1 (Reversal).** *The reversed permutation $\sigma^{\mathrm{rev}}(i) := \sigma(k + 1 - i)$ is also a WCS, and satisfies $\sigma^{\mathrm{rev}}(1) = \sigma(k)$ and $\sigma^{\mathrm{rev}}(k) = \sigma(1)$.*

*Proof.* If $m \mid \sigma^{\mathrm{rev}}(i) = \sigma(k+1-i)$ and $m \mid (i - j)$, then $m \mid \bigl((k+1-i) - (k+1-j)\bigr) = -(i - j)$, so weak consecutiveness of $\sigma$ yields $m \mid \sigma(k+1-j) = \sigma^{\mathrm{rev}}(j)$. $\square$

**Lemma 2 (Residue-class characterization; cf. Lemma 2.1 of `arXiv:2401.09497v1`).** *For every $m \in [k]$, let $S_m^\sigma := \{i \in [k] : i \equiv \sigma^{-1}(m) \pmod m\}$ and $T_m^\sigma := \{i \in [k] : m \mid \sigma(i)\}$, and let $c_m \in \{1, 2, \dots, m\}$ be the unique integer in $\{1, \dots, m\}$ with $c_m \equiv \sigma^{-1}(m) \pmod m$. Then $S_m^\sigma = T_m^\sigma$, $|S_m^\sigma| = |T_m^\sigma| = \lfloor k/m \rfloor$, and $c_m > k \bmod m$ (where $k \bmod m \in \{0, 1, \dots, m-1\}$ denotes the remainder of $k$ upon division by $m$).*

*Proof.* Because $\sigma : [k] \to [k]$ is a bijection, $T_m^\sigma$ is the preimage of the set of multiples of $m$ in $[k]$, so $|T_m^\sigma| = \lfloor k/m \rfloor$. For any $i \in S_m^\sigma$, setting $j = \sigma^{-1}(m)$ gives $m \mid \sigma(j) = m$ and $m \mid (j - i)$, so weak consecutiveness yields $m \mid \sigma(i)$, i.e., $S_m^\sigma \subseteq T_m^\sigma$. Write $k = q m + r$ with $q = \lfloor k/m \rfloor$ and $r = k \bmod m \in \{0, \dots, m-1\}$. The elements of $S_m^\sigma$ are the numbers $c_m + t m$ ($t \ge 0$) not exceeding $q m + r$; this holds for all $t \in \{0, 1, \dots, q-1\}$ (since $c_m + (q-1)m \le q m \le k$), and additionally for $t = q$ if and only if $c_m \le r$. Thus $|S_m^\sigma| = q$ if $c_m > r$ and $|S_m^\sigma| = q + 1$ if $c_m \le r$. Since $S_m^\sigma \subseteq T_m^\sigma$ and $|T_m^\sigma| = q$, we must have $c_m > r = k \bmod m$, $|S_m^\sigma| = q = |T_m^\sigma|$, and hence $S_m^\sigma = T_m^\sigma$. $\square$

**Lemma 3 (GCD representation).** *Let $L_k := \mathrm{lcm}(1, 2, \dots, k)$. For any WCS $\sigma : [k] \to [k]$, there exists an integer $a \in \{0, 1, \dots, L_k - 1\}$ such that*
$$\sigma(i) = \gcd(a + i, L_k) \qquad \text{for all } i \in [k],$$
*and for every $m \in [k]$, $m \mid \sigma(i) \iff m \mid (a + i)$.*

*Proof.* Factor $L_k = \prod_{p \le k} p^{e_p}$, where for each prime $p \le k$ we have $p^{e_p} \le k < p^{e_p + 1}$. By the Chinese Remainder Theorem, there is a unique $a \in \{0, 1, \dots, L_k - 1\}$ satisfying
$$a \equiv -c_{p^{e_p}} \pmod{p^{e_p}} \qquad \text{for every prime } p \le k.$$
Fix any prime power $p^e \le k$ ($1 \le e \le e_p$), and put $i_0 := \sigma^{-1}(p^{e_p}) \in [k]$. Then $p^e \mid p^{e_p} = \sigma(i_0)$, so Lemma 2 gives $i_0 \in T_{p^e}^\sigma = S_{p^e}^\sigma$ and $i_0 \in T_{p^{e_p}}^\sigma = S_{p^{e_p}}^\sigma$, whence
$$c_{p^e} \equiv i_0 \equiv c_{p^{e_p}} \equiv -a \pmod{p^e}.$$
Hence, for every $i \in [k]$ and every prime power $p^e \le k$,
$$p^e \mid \sigma(i) \iff i \in T_{p^e}^\sigma = S_{p^e}^\sigma \iff i \equiv c_{p^e} \equiv -a \pmod{p^e} \iff p^e \mid (a + i).$$
Now fix $i \in [k]$ (note $a + i \ge 1$). For any prime $p$ and exponent $e \ge 1$:
- if $p^e \mid \sigma(i)$, then $p^e \le \sigma(i) \le k$, so $p^e \mid L_k$ and $p^e \mid (a + i)$, hence $p^e \mid \gcd(a + i, L_k)$;
- conversely, if $p^e \mid \gcd(a + i, L_k)$, then $p^e \mid L_k$ implies $p^e \le p^{e_p} \le k$, and $p^e \mid (a + i)$ then implies $p^e \mid \sigma(i)$.

Thus $\sigma(i)$ and $\gcd(a + i, L_k)$ have identical $p$-adic valuations for every prime $p$, so $\sigma(i) = \gcd(a + i, L_k)$. Finally, for any $m \in [k]$, we have $m \mid L_k$, so $m \mid \sigma(i) \iff m \mid \gcd(a + i, L_k) \iff m \mid (a + i)$. $\square$

---

### 2. Case 1: $k \ge 4$ is even

Let $k \ge 4$ be even, and let $\sigma : [k] \to [k]$ be a WCS. By Lemma 2 for $m = 2$, $c_2 \in \{1, 2\}$ satisfies $2 \mid \sigma(i) \iff i \equiv c_2 \pmod 2$. Under reversal $\sigma^{\mathrm{rev}}(i) = \sigma(k + 1 - i)$, since $k$ is even, $k + 1 - c_2 \equiv 1 - c_2 \pmod 2$ flips parity. Replacing $\sigma$ by $\sigma^{\mathrm{rev}}$ if necessary (Lemma 1), we may assume $c_2 = 2$, so that $\sigma(i) \equiv i \pmod 2$ for every $i \in [k]$.

Consider $m := \frac{k}{2} + 1$. Since $k \ge 4$, we have $\frac{k}{2} < m < k$, so $\lfloor k/m \rfloor = 1$ and $k \bmod m = k - m = \frac{k}{2} - 1$. Setting $j := \sigma^{-1}(m)$, Lemma 2 gives $|S_m^\sigma| = 1$ (so $j = c_m$) and
$$\frac{k}{2} = (k \bmod m) + 1 \le j \le m = \frac{k}{2} + 1.$$
Because $\sigma(j) = m = \frac{k}{2} + 1$ has the same parity as $j$, while $\frac{k}{2}$ and $\frac{k}{2} + 1$ have opposite parities, we must have $j = \frac{k}{2} + 1$, i.e., $\sigma\!\left(\frac{k}{2} + 1\right) = \frac{k}{2} + 1$.

Now set $A := \sigma(1)$ and suppose for contradiction that $A > 1$. Since $1 \in T_A^\sigma = S_A^\sigma$, we have $c_A = 1$; by Lemma 2, $1 = c_A > k \bmod A \ge 0$, forcing $k \bmod A = 0$, i.e., $A \mid k$. Also $A = \sigma(1) \equiv 1 \pmod 2$, so $A$ is odd. Together with $2 \mid k$ and $A \mid k$, this implies $A \mid \frac{k}{2}$. Since $A \mid \sigma(1)$ and $A \mid \left(\left(\frac{k}{2} + 1\right) - 1\right)$, weak consecutiveness gives
$$A \;\Big|\; \sigma\!\left(\frac{k}{2} + 1\right) = \frac{k}{2} + 1.$$
Combining $A \mid \frac{k}{2}$ and $A \mid \left(\frac{k}{2} + 1\right)$ gives $A \mid 1$, contradicting $A > 1$. Thus $\sigma(1) = 1$, so the original sequence satisfied $\sigma(1) = 1$ or $\sigma(k) = 1$.

---

### 3. Case 2: $k \ge 3$ is odd

Suppose for contradiction that $k \ge 3$ is odd and $\sigma : [k] \to [k]$ is a WCS with $\sigma(1) > 1$ and $\sigma(k) > 1$.

**Step 1 (Endpoint divisors and normalization).**
Apply Lemma 3 to $\sigma$ to obtain $a \in \{0, 1, \dots, L_k - 1\}$ with $\sigma(i) = \gcd(a + i, L_k)$ for all $i \in [k]$.

- *Parity:* Since $k$ is odd, $k \bmod 2 = 1$. By Lemma 2, $c_2 \in \{1, 2\}$ satisfies $c_2 > 1$, so $c_2 = 2$. Hence $a \equiv -c_2 \equiv 0 \pmod 2$, and $2 \mid \sigma(i) \iff 2 \mid i$ for all $i \in [k]$. Because $1$ and $k$ are odd, both $\sigma(1)$ and $\sigma(k)$ are odd integers $\ge 3$.
- *Divisibility into $k$ and coprimality:* Since $1 \in T_{\sigma(1)}^\sigma = S_{\sigma(1)}^\sigma$, we have $c_{\sigma(1)} = 1 > k \bmod \sigma(1) \ge 0$, so $\sigma(1) \mid k$ and $\sigma(1) \mid (a + 1)$. Similarly, $k \in T_{\sigma(k)}^\sigma = S_{\sigma(k)}^\sigma$ implies $k \equiv c_{\sigma(k)} \pmod{\sigma(k)}$; if $r := k \bmod \sigma(k)$ were positive, then $c_{\sigma(k)} = r$, contradicting $c_{\sigma(k)} > r$ (Lemma 2). Hence $\sigma(k) \mid k$, and since $\sigma(k) \mid (a + k)$, we obtain $\sigma(k) \mid a$. Any common divisor $d$ of $\sigma(1)$ and $\sigma(k)$ divides $(a + 1) - a = 1$, so $\gcd(\sigma(1), \sigma(k)) = 1$.

In particular, since $\sigma(1), \sigma(k) \ge 3$ are coprime, $\sigma(1) \ne \sigma(k)$. Replacing $\sigma$ by $\sigma^{\mathrm{rev}}$ if necessary (Lemma 1, which preserves $k$ being odd and swaps $\sigma(1)$ and $\sigma(k)$) and taking its corresponding integer $a \in \{0, 1, \dots, L_k - 1\}$ from Lemma 3, we may assume without loss of generality that
$$A := \sigma(1) < \sigma(k) =: B.$$
Summarizing what we now have for this normalized $\sigma$ and $a$:
- $A$ and $B$ are odd integers with $3 \le A < B$ (so $B \ge 5$) and $\gcd(A, B) = 1$;
- $A B \mid k$, so $k = A B R$ for an odd integer $R \ge 1$ (whence $B R \ge 5$ and $k \ge 15$);
- $2 \mid a$, $a \equiv -1 \pmod A$, and $B \mid a$.

**Step 2 (Mid-range fixed congruence).**
Consider
$$m := \frac{k + A}{2} = A \cdot \frac{B R + 1}{2}.$$
Because $B$ and $R$ are odd, $\frac{B R + 1}{2}$ is an integer. Since $k = A B R \ge 5 A > A > 0$, we have $\frac{k}{2} < m < k$, so $\lfloor k/m \rfloor = 1$ and $k \bmod m = k - m = \frac{k - A}{2}$. Setting $j := \sigma^{-1}(m)$, Lemma 2 gives $j = c_m$ and
$$\frac{k - A}{2} + 1 \le j \le \frac{k + A}{2}.$$
Since $A \mid m = \sigma(j)$, Lemma 2 gives $j \in T_A^\sigma = S_A^\sigma$, so $j \equiv 1 \pmod A$. The left endpoint $\frac{k - A}{2} + 1 = A \cdot \frac{B R - 1}{2} + 1$ satisfies $\frac{k - A}{2} + 1 \equiv 1 \pmod A$ (as $B R$ is odd), and $0 \le j - \left(\frac{k - A}{2} + 1\right) \le A - 1 < A$. Therefore
$$j = \frac{k - A}{2} + 1 \qquad \text{and} \qquad \sigma\!\left(\frac{k - A}{2} + 1\right) = \frac{k + A}{2}.$$
By Lemma 3, $m = \frac{k + A}{2}$ divides $a + j = a + \frac{k - A}{2} + 1$, hence divides $(a + j) - m = a + 1 - A$. Because $\frac{B R + 1}{2}$ divides $m = A \cdot \frac{B R + 1}{2}$, we obtain
$$\frac{B R + 1}{2} \;\Big|\; (a + 1 - A). \tag{1}$$

**Step 3 (Pinning $a$ modulo the exact $2$-power dividing $B R + 1$).**
Since $B R$ is odd, $B R + 1$ is even; write
$$B R + 1 = 2^s u, \qquad s \ge 1, \quad u \ge 1 \text{ odd}.$$
Consider the index
$$i_1 := (A - 1) B R = k - B R.$$
Since $A \ge 3$ and $B R \ge 5$, we have $1 \le 2 B R \le i_1 < k$, so $i_1 \in [k]$. Observe the exact identity
$$a + i_1 = a + (A - 1) B R = (a + 1 - A) + (A - 1)(B R + 1). \tag{2}$$
By (1), $u \mid \frac{B R + 1}{2} \mid (a + 1 - A)$, and $u \mid (B R + 1)$, so $u \mid (a + i_1)$. Also $B \mid a$ and $B \mid i_1$, so $B \mid (a + i_1)$.

We claim that $2^s \nmid (a + i_1)$. Suppose to the contrary that $2^s \mid (a + i_1)$. Since $u$ is odd, $\gcd(2^s, u) = 1$, so $B R + 1 = 2^s u \mid (a + i_1)$. Since $\gcd(B, B R + 1) = 1$, this yields $B (B R + 1) \mid (a + i_1)$. Moreover, $B < k$ and $B R + 1 < 3 B R \le A B R = k$ (as $B R \ge 5 > 1$ and $A \ge 3$), so both $B$ and $B R + 1$ divide $L_k$; by coprimality, $B (B R + 1) \mid L_k$. Lemma 3 then gives
$$B (B R + 1) \;\Big|\; \gcd(a + i_1, L_k) = \sigma(i_1) \le k = A B R,$$
forcing $B R + 1 \le A R$, which contradicts $A < B$. Thus $2^s \nmid (a + i_1)$.

Because $A$ is odd, $2 \mid (A - 1)$, and since $2^s \mid (B R + 1)$, we have $2^{s + 1} \mid (A - 1)(B R + 1)$; in particular, $2^s \mid (A - 1)(B R + 1)$.
- If $s = 1$, then $2 \mid a$ and $2 \mid (A - 1)$ imply $2 \mid (a + 1 - A)$, whence (2) gives $2 \mid (a + i_1)$, contradicting $2^s \nmid (a + i_1)$. Hence **$s \ge 2$**.
- Combining $2^s \mid (A - 1)(B R + 1)$ and $2^s \nmid (a + i_1)$ in (2) gives $2^s \nmid (a + 1 - A)$. On the other hand, (1) gives $2^{s - 1} \mid \frac{B R + 1}{2} \mid (a + 1 - A)$. Therefore
  $$a + 1 - A \equiv 2^{s - 1} \pmod{2^s}, \qquad \text{i.e.,} \qquad a \equiv A - 1 + 2^{s - 1} \pmod{2^s}. \tag{3}$$

**Step 4 (Counting multiples of $2^s A$ — contradiction).**
Because $2^s \le 2^s u = B R + 1 < k$ and $A < k$, both $2^s$ and $A$ divide $L_k$; since $A$ is odd, $\gcd(2^s, A) = 1$, and therefore
$$2^s A \;\Big|\; L_k.$$
For each $t \in \{0, 1, \dots, u - 1\}$, define
$$i_t := (2^{s - 1} - 1) A + 1 + t \cdot 2^s A.$$
Since $s \ge 2$ and $A \ge 3$, we have $i_0 = (2^{s - 1} - 1) A + 1 \ge A + 1 \ge 4 \ge 1$, and $i_0 < i_1 < \dots < i_{u - 1}$. Using $2^s u = B R + 1$ and $A B R = k$, the largest index is
$$i_{u - 1} = \bigl((u - 1) 2^s + 2^{s - 1} - 1\bigr) A + 1 = \bigl(2^s u - 2^{s - 1} - 1\bigr) A + 1 = (B R - 2^{s - 1}) A + 1 = k - 2^{s - 1} A + 1 \le k - 5 < k,$$
as $2^{s - 1} A \ge 2 \cdot 3 = 6$. Thus $i_0, i_1, \dots, i_{u - 1}$ are $u$ distinct elements of $[k]$.

For every $t \in \{0, 1, \dots, u - 1\}$:
- modulo $A$: $a \equiv -1 \pmod A$ and $i_t \equiv 1 \pmod A$, so $A \mid (a + i_t)$;
- modulo $2^s$: since $A$ is odd, $2^{s - 1} A \equiv 2^{s - 1} \pmod{2^s}$, so $i_t \equiv 2^{s - 1} A - A + 1 \equiv 2^{s - 1} - A + 1 \pmod{2^s}$; adding (3) gives
  $$a + i_t \equiv (A - 1 + 2^{s - 1}) + (2^{s - 1} - A + 1) = 2^s \equiv 0 \pmod{2^s}.$$

Since $\gcd(2^s, A) = 1$, it follows that $2^s A \mid (a + i_t)$, and since $2^s A \mid L_k$, Lemma 3 implies
$$2^s A \;\Big|\; \gcd(a + i_t, L_k) = \sigma(i_t) \qquad \text{for all } t \in \{0, 1, \dots, u - 1\}.$$
Because $\sigma : [k] \to [k]$ is injective, $\sigma(i_0), \sigma(i_1), \dots, \sigma(i_{u - 1})$ are $u$ distinct positive multiples of $2^s A$ in $[k]$. However,
$$k = A B R = A (2^s u - 1) = (u - 1)(2^s A) + (2^s - 1) A < u \cdot (2^s A),$$
so $[k]$ contains only $u - 1$ positive multiples of $2^s A$, a contradiction.

Combining Cases 1 and 2 completes the proof of Conjecture 5.2 for all $k \ge 1$. $\blacksquare$

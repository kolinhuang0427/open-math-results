# Proof of Conjecture 6.8 (`arXiv:2310.15207v1`, Section 6)

We prove **Conjecture 6.8** (`\label{conj:8}`) of Victor J. W. Guo (`arXiv:2310.15207v1`, Section 6) unconditionally for every positive integer $m \ge 1$ and every odd integer $n \ge 3$.

*(Boundary remark on $n=1$: Although $n>1$ was omitted in the wording of Conjecture 6.8—unlike Conjectures 6.1, 6.2, and 6.4—for $n=1$ we have $\Phi_1(q)=q-1$, so $m=1$ gives $1 \equiv 1$ while $m=2$ gives $1 - \frac{(1+q+q^2+q^3+q^4)q}{(1+q)^3} \equiv \frac{3}{8} - \frac{15}{16}(q-1) \not\equiv \frac{3}{8} \pmod{(q-1)^2}$. For all $n \ge 3$ odd, the congruence holds without exception.)*

---

## 1. Block Decomposition and Vanishing for $s > (n-1)/2$

Fix an odd integer $n \ge 3$ and let $N := (n-1)/2 \in \mathbb{Z}_{\ge 1}$. Write $k = rn + s$ with $0 \le r \le m-1$ and $0 \le s \le n-1$, and denote the $k$-th summand by
$$A_k(q) := (-1)^k [4k+1] \frac{(q;q^2)_k^3}{(q^2;q^2)_k^3} q^{k^2} \in \mathbb{Q}(q).$$
Let $v_{\Phi_n}(\cdot)$ be the $\Phi_n(q)$-adic valuation in $\mathbb{Q}(q)$. Since $n \ge 3$, $1-q$ is coprime to $\Phi_n(q)$, so $v_{\Phi_n}([4k+1]) \ge 0$.
- In $(q;q^2)_{rn+s} = \prod_{j=0}^{rn+s-1}(1-q^{2j+1})$, an exponent $2j+1$ is divisible by $n$ if and only if $2j+1 = (2u+1)n$ ($u \ge 0$), i.e., $j = un + N$. Thus:
  - for $0 \le s \le N$, the factors divisible by $\Phi_n(q)$ correspond to $0 \le u \le r-1$, giving $(q^n; q^{2n})_r$ ($r$ factors);
  - for $N+1 \le s \le n-1$, $u = r$ also lies in $[0, rn+s-1]$, giving $(q^n; q^{2n})_{r+1}$ ($r+1$ factors).
- In $(q^2;q^2)_{rn+s} = \prod_{j=1}^{rn+s}(1-q^{2j})$, since $\gcd(2,n)=1$, $n \mid 2j \iff n \mid j$. Since $0 \le s \le n-1$, the factors divisible by $\Phi_n(q)$ correspond to $j = un$ for $1 \le u \le r$, giving $(q^{2n}; q^{2n})_r$ ($r$ factors) for all $0 \le s \le n-1$.

Therefore, whenever $N+1 \le s \le n-1$, we have $v_{\Phi_n}(A_{rn+s}) \ge 3(r+1) - 3r = 3 \ge 2$, so every term with $s > N$ vanishes modulo $\Phi_n(q)^3$ (and hence modulo $\Phi_n(q)^2$). For $0 \le s \le N$, $v_{\Phi_n}(A_{rn+s}) \ge 0$, so $A_{rn+s}(q)$ is well-defined modulo $\Phi_n(q)^2$.

Define the $r$-th block sum
$$B_r(q) := \sum_{s=0}^{N} A_{rn+s}(q).$$
It suffices to prove that for every $0 \le r \le m-1$,
$$B_r(q) \equiv (-1)^r (4r+1) \frac{(\frac{1}{2})_r^3}{r!^3} (-1)^N q^{N^2} [n] \pmod{\Phi_n(q)^2}. \tag{1}$$

---

## 2. Linearization of $B_r(q)$ Modulo $\Phi_n(q)^2$

Set $z := 1 - q^n = (1-q)[n]$. Since $\Phi_n(q) \mid z$, we have $z^2 \equiv 0 \pmod{\Phi_n(q)^2}$ and $q^n = 1 - z$. Fix $0 \le r \le m-1$ and $0 \le s \le N$.

1. **Ratio of $n$-multiple $q$-Pochhammer factors:** For each $0 \le u \le r-1$, expanding $q^n = 1 - z$ gives
   $$\frac{1 - q^{(2u+1)n}}{1 - q^{2(u+1)n}} = \frac{(2u+1)z - \binom{2u+1}{2}z^2 + O(z^3)}{(2u+2)z - \binom{2u+2}{2}z^2 + O(z^3)} \equiv \frac{2u+1}{2u+2} \cdot \frac{1 - uz}{1 - (u+\frac{1}{2})z} \equiv \frac{2u+1}{2u+2}\!\left(1 + \frac{1}{2}z\right) \pmod{\Phi_n(q)^2}.$$
   Multiplying over $0 \le u \le r-1$ and cubing yields
   $$\left(\frac{(q^n; q^{2n})_r}{(q^{2n}; q^{2n})_r}\right)^3 \equiv \frac{(\frac{1}{2})_r^3}{r!^3}\!\left(1 + \frac{3r}{2}z\right) \pmod{\Phi_n(q)^2}.$$

2. **Full-$n$-block non-$n$-multiple product:** Set
   $$P_r(q) := \frac{\prod_{0 \le j < rn,\, n \nmid (2j+1)} (1 - q^{2j+1})}{\prod_{1 \le j \le rn,\, n \nmid j} (1 - q^{2j})}.$$
   Clearly $P_r(q)$ is independent of $s$. In each block $un \le j < (u+1)n$ (resp. $un < j \le (u+1)n$), since $\gcd(2,n)=1$, both $2j+1$ and $2j$ run over all nonzero residues $\{1,\dots,n-1\}$ modulo $n$ once, so $P_r(q) \equiv 1 \pmod{\Phi_n(q)}$. Hence $P_r(q)^3 \equiv 1 + C_r z \pmod{\Phi_n(q)^2}$ for some $C_r \in \mathbb{Q}[q]$ independent of $s$.

3. **Remaining $s$-tail factors:** For $0 \le i < s \le N$, we have $2i+1 < n$ and $2i+2 \le 2N = n-1 < n$, so $1-q^{2i+1}$ and $1-q^{2i+2}$ are invertible modulo $\Phi_n(q)^2$. Using $1 - q^{a+2rn} = 1 - q^a(1-z)^{2r} \equiv (1-q^a)\bigl(1 + 2r\frac{q^a}{1-q^a}z\bigr) \pmod{\Phi_n(q)^2}$ gives
   $$\left(\frac{\prod_{i=0}^{s-1}(1-q^{2rn+2i+1})}{\prod_{i=0}^{s-1}(1-q^{2rn+2i+2})}\right)^3 \equiv \frac{(q;q^2)_s^3}{(q^2;q^2)_s^3}\!\left(1 + 6rz \sum_{i=0}^{s-1}\left(\frac{q^{2i+1}}{1-q^{2i+1}} - \frac{q^{2i+2}}{1-q^{2i+2}}\right)\right) \pmod{\Phi_n(q)^2}.$$

4. **Sign, quadratic power, and $[4k+1]$:** Since $n$ is odd, $(-1)^{rn+s} = (-1)^r (-1)^s$. Next,
   $$q^{(rn+s)^2} = q^{s^2}(1-z)^{r^2 n + 2rs} \equiv q^{s^2}\bigl(1 - (r^2 n + 2rs)z\bigr) \pmod{\Phi_n(q)^2},$$
   and since $z = (1-q)[n]$,
   $$[4rn+4s+1] = \frac{1 - (1-z)^{4r} q^{4s+1}}{1-q} \equiv \frac{1 - (1-4rz)q^{4s+1}}{1-q} = [4s+1] + 4rq^{4s+1}[n] \pmod{\Phi_n(q)^2}.$$

Multiplying these expansions together and using $z^2 \equiv 0 \pmod{\Phi_n(q)^2}$ along with $(1-q)[4s+1] = 1 - q^{4s+1}$, every $s$-independent $O(z)$ coefficient (namely $\frac{3r}{2}z + C_r z - r^2 n z$) multiplies $B_0(q)$. Thus:
$$B_r(q) \equiv (-1)^r \frac{(\frac{1}{2})_r^3}{r!^3}\Bigl(B_0(q) + \bigl(\tfrac{3r}{2} + C_r - r^2 n\bigr)z B_0(q) + r [n] \Delta_8(q)\Bigr) \pmod{\Phi_n(q)^2}, \tag{2}$$
where
$$\Delta_8(q) := \sum_{s=0}^{N} (-1)^s \frac{(q;q^2)_s^3}{(q^2;q^2)_s^3} q^{s^2} \left[ 4q^{4s+1} + (1 - q^{4s+1})\!\left(6\sum_{i=0}^{s-1}\left(\frac{q^{2i+1}}{1-q^{2i+1}} - \frac{q^{2i+2}}{1-q^{2i+2}}\right) - 2s\right)\right]. \tag{3}$$

---

## 3. Exact Evaluation of $B_0(q) \bmod \Phi_n(q)^2$ via Watson's Transformation

Recall Watson's terminating ${}_8\phi_7 \to {}_4\phi_3$ transformation (Gasper–Rahman, *Basic Hypergeometric Series*, 2nd ed., (III.18)):
$${}_8\phi_7 \left[\begin{matrix} a, Q a^{1/2}, -Q a^{1/2}, b, c, d, e, Q^{-N} \\ a^{1/2}, -a^{1/2}, aQ/b, aQ/c, aQ/d, aQ/e, aQ^{N+1} \end{matrix}; Q, \frac{a^2 Q^{N+2}}{bcde}\right] = \frac{(aQ;Q)_N (aQ/(de);Q)_N}{(aQ/d;Q)_N (aQ/e;Q)_N} \, {}_4\phi_3 \left[\begin{matrix} Q^{-N}, d, e, aQ/(bc) \\ aQ/b, aQ/c, de Q^{-N}/a \end{matrix}; Q, Q\right],$$
and the $q$-Chu–Vandermonde identity (Gasper–Rahman (II.7)):
$${}_2\phi_1 \left[\begin{matrix} Q^{-N}, \beta \\ \gamma \end{matrix}; Q, \frac{\gamma Q^N}{\beta}\right] = \frac{(\gamma/\beta; Q)_N}{(\gamma; Q)_N}.$$
Because both sides of Watson's transformation are finite sums of $N+1$ rational functions of $e$, letting $e \to \infty$ (where $(e;Q)_s/e^s \to (-1)^s Q^{s(s-1)/2}$, $(aQ/(de);Q)_N/(aQ/e;Q)_N \to 1$, and $(e;Q)_k Q^k / (de Q^{-N}/a; Q)_k \to (aQ^{N+1}/d)^k$) yields the exact rational-function identity
$$\sum_{s=0}^{N} \frac{1 - aQ^{2s}}{1-a} \frac{(a,b,c,d,Q^{-N}; Q)_s}{(Q, aQ/b, aQ/c, aQ/d, aQ^{N+1}; Q)_s} (-1)^s Q^{s(s-1)/2} \left(\frac{a^2 Q^{N+2}}{bcd}\right)^s = \frac{(aQ;Q)_N}{(aQ/d;Q)_N} \sum_{k=0}^{N} \frac{(Q^{-N}, d, aQ/(bc); Q)_k}{(Q, aQ/b, aQ/c; Q)_k} \left(\frac{aQ^{N+1}}{d}\right)^k. \tag{4}$$

In (4), specialize $Q = q^2$ (note $N=(n-1)/2$, so $Q^{-N} = q^{1-n}$ and $Q^{N+1} = q^{n+1}$), $a = q$, $b = q^{1+n}$, $c = q$, and $d = q^2$:
- On the LHS, $(d; q^2)_s = (q^2; q^2)_s$ cancels $(Q; q^2)_s$, $(aQ/d; q^2)_s = (q; q^2)_s$ cancels $(a; q^2)_s$, and $\frac{a^2 Q^{N+2}}{bcd} = \frac{q^2 q^{n+3}}{q^{1+n}\cdot q \cdot q^2} = q$, giving weight $(-1)^s q^{s(s-1)} q^s = (-1)^s q^{s^2}$. Every denominator exponent in $(q^2; q^2)_s$, $(q^{2-n}; q^2)_s$, and $(q^{n+2}; q^2)_s$ for $0 \le s \le N$ lies in $[2, n-1] \cup [2-n, -1] \cup [n+2, 2n-1]$, so none is divisible by $n$. Since
  $$(1 - q^{m+n})(1 - q^{m-n}) = (1-q^m)^2 - q^{m-n}(1-q^n)^2 \equiv (1-q^m)^2 \pmod{\Phi_n(q)^2},$$
  the LHS of (4) is congruent modulo $\Phi_n(q)^2$ to $B_0(q)$.
- On the RHS, $(d; q^2)_k = (q^2; q^2)_k$ cancels $(aQ/c; q^2)_k = (q^2; q^2)_k$, and $\frac{(q^3; q^2)_N}{(q; q^2)_N} = \frac{1 - q^{2N+1}}{1 - q} = [n]$, while the sum is ${}_2\phi_1(q^{1-n}, q^{1-n}; q^{2-n}; q^2, q^n)$. By $q$-Chu–Vandermonde with $\beta = q^{1-n}$, $\gamma = q^{2-n}$ (so $\gamma Q^N / \beta = q \cdot q^{n-1} = q^n$), this sum equals $\frac{(q; q^2)_N}{(q^{2-n}; q^2)_N}$.

Modulo $\Phi_n(q)$, $q^n \equiv 1$ implies $q^{2-n} \equiv q^2$ and $q^{2j+1} = q^{n - (2(N-1-j)+2)} \equiv q^{-(2(N-1-j)+2)}$. Reindexing $j \mapsto N-1-j$ in the numerator gives
$$\frac{(q; q^2)_N}{(q^{2-n}; q^2)_N} \equiv \frac{(q; q^2)_N}{(q^2; q^2)_N} \equiv \prod_{j=0}^{N-1} \frac{1 - q^{-(2j+2)}}{1 - q^{2j+2}} = (-1)^N q^{-N(N+1)} \equiv (-1)^N q^{N^2} \pmod{\Phi_n(q)},$$
where the last congruence uses $N^2 + N(N+1) = N(2N+1) = Nn \equiv 0 \pmod n$. Multiplying by $[n]$ (which is divisible by $\Phi_n(q)$) upgrades $\pmod{\Phi_n(q)}$ to $\pmod{\Phi_n(q)^2}$, proving
$$B_0(q) \equiv (-1)^N q^{N^2} [n] \pmod{\Phi_n(q)^2}. \tag{5}$$
In particular, $B_0(q) \equiv 0 \pmod{\Phi_n(q)}$, so $z B_0(q) \equiv 0 \pmod{\Phi_n(q)^2}$ in (2).

---

## 4. Exact Evaluation of $\Delta_8(q) \bmod \Phi_n(q)$

Now in (4), set $Q = q^2$, $N = (n-1)/2$, $a = t^4 q$, $b = t^2 q$, $c = t^4 q$, and $d = q^2$ (with $t$ an indeterminate), and multiply both sides by $1 - t^4 q$. Once again $(d; q^2)_s$ cancels $(Q; q^2)_s$, $(aQ/d; q^2)_s = (t^4 q; q^2)_s$ cancels $(a; q^2)_s$, and $(aQ/c; q^2)_k = (q^2; q^2)_k$ cancels $(d; q^2)_k$; moreover $(1 - t^4 q)\frac{(t^4 q^3; q^2)_N}{(t^4 q; q^2)_N} = 1 - t^4 q^{2N+1} = 1 - t^4 q^n$. Hence, identically in $\mathbb{Q}(q, t)$:
$$\sum_{s=0}^{N} (1 - t^4 q^{4s+1}) \frac{(t^2 q; q^2)_s (t^4 q; q^2)_s (q^{1-n}; q^2)_s}{(t^2 q^2; q^2)_s (q^2; q^2)_s (t^4 q^{n+2}; q^2)_s} (-1)^s q^{s(s-1)} (t^2 q^{n+1})^s = (1 - t^4 q^n) \sum_{k=0}^{N} \frac{(q^{1-n}; q^2)_k (q t^{-2}; q^2)_k}{(q^2; q^2)_k (t^2 q^2; q^2)_k} (t^4 q^n)^k. \tag{6}$$
Every denominator factor in (6) at $t=1$ is coprime to $\Phi_n(q)$, so reducing (6) modulo $\Phi_n(q)$ (using $q^n \equiv 1$, $q^{1-n} \equiv q$, $q^{n+1} \equiv q$, $q^{n+2} \equiv q^2$) commutes with taking $-\frac{\partial}{\partial t}\big|_{t=1}$ in $\mathbb{Q}[q]/(\Phi_n(q))$:
- On the LHS of (6) reduced modulo $\Phi_n(q)$, each $s$-th term is
  $$L_s(t) := (-1)^s q^{s^2} (1 - t^4 q^{4s+1}) \frac{(t^2 q; q^2)_s (t^4 q; q^2)_s (q; q^2)_s}{(t^2 q^2; q^2)_s (q^2; q^2)_s (t^4 q^2; q^2)_s} t^{2s}.$$
  By logarithmic differentiation at $t=1$,
  $$-\frac{\partial L_s}{\partial t}\bigg|_{t=1} = (-1)^s \frac{(q; q^2)_s^3}{(q^2; q^2)_s^3} q^{s^2} \left[ 4q^{4s+1} + (1-q^{4s+1})\!\left(6\sum_{i=0}^{s-1}\left(\frac{q^{2i+1}}{1-q^{2i+1}} - \frac{q^{2i+2}}{1-q^{2i+2}}\right) - 2s\right)\right],$$
  whose sum over $0 \le s \le N$ is precisely $\Delta_8(q) \bmod \Phi_n(q)$ from (3).
- On the RHS of (6) reduced modulo $\Phi_n(q)$, the prefactor $1 - t^4 q^n \equiv 1 - t^4$ vanishes at $t=1$, with $-\frac{d}{dt}(1 - t^4)\big|_{t=1} = 4$. Thus
  $$\Delta_8(q) \equiv 4 \sum_{k=0}^{N} \frac{(q^{1-n}; q^2)_k (q; q^2)_k}{(q^2; q^2)_k^2} q^{nk} = 4 \cdot \frac{(q; q^2)_N}{(q^2; q^2)_N} \equiv 4 (-1)^N q^{N^2} \pmod{\Phi_n(q)}, \tag{7}$$
  again by $q$-Chu–Vandermonde (with $Q=q^2, \beta=q, \gamma=q^2, \gamma Q^N/\beta = q^n$) and the reversal computation from Section 3.

---

## 5. Conclusion

Substituting (5), $z B_0(q) \equiv 0 \pmod{\Phi_n(q)^2}$, and (7) into (2) yields, for every $0 \le r \le m-1$,
$$B_r(q) \equiv (-1)^r \frac{(\frac{1}{2})_r^3}{r!^3}\Bigl((-1)^N q^{N^2}[n] + 4r(-1)^N q^{N^2}[n]\Bigr) = (-1)^r (4r+1) \frac{(\frac{1}{2})_r^3}{r!^3} (-1)^N q^{N^2}[n] \pmod{\Phi_n(q)^2},$$
establishing (1). Summing over $r = 0, \dots, m-1$ proves Conjecture 6.8 for all $m \ge 1$ and all odd integers $n \ge 3$. $\blacksquare$

# Proof of Zhi-Wei Sun's Supercongruence Conjecture (ii), Part 1 on OEIS A208425 (`conjecture_2`)

## Primary Source & Scope

From **OEIS A208425** (revision 60, `2025-11-05T15:22:21-05:00`, <https://oeis.org/A208425>), comment by **Zhi-Wei Sun** (Nov 12, 2016):

> From _Zhi-Wei Sun_, Nov 12 2016: (Start)
> Conjecture: (i) For any prime p > 3 and positive integer n, the number (a(p*n)-a(n))/(p*n)^3 is always a p-adic integer.
> (ii) For any prime p == 1 (mod 3), we have Sum_{k=0..p-1}a(k) == C(2(p-1)/3,(p-1)/3) (mod p^2). For any prime p == 2 (mod 3), we have Sum_{k=0..p-1}a(k) == 2p/C(2(p+1)/3,(p+1)/3) (mod p^2).
> We have proved part (i) of this conjecture for n = 1. (End)

Here OEIS A208425 defines $a(j)$ as the coefficient of $x^j$ in $\sum_{k \ge 0} \frac{(3k)!}{k!^3} \frac{x^{2k}}{(1-x)^{3k+1}}$, which equals
$$a(j) = \sum_{k=0}^{j} \binom{j}{k}\binom{j-k}{k}\binom{j+k}{k}.$$
In `google-deepmind/formal-conjectures` (`FormalConjectures/OEIS/208425.lean`, blob `6692a6604859e2615fd452aa1f41cade8b6f8dcc`), these three statements appear as `conjecture_1`, `conjecture_2`, and `conjecture_3`.

**Scope:** Part (i) (`conjecture_1`) was proved by H. Pan and Z.-W. Sun (*Supercongruences for central trinomial coefficients*, `arXiv:2012.05121v3`, *Frontiers in Combinatorics and Number Theory* **2** (2026), 55–62, Theorem 1.2). Part (ii) for $p \equiv 2 \pmod 3$ (`conjecture_3`) was proved and Lean-formalized in `Varun-Dudipala/sun-conjectures-lean`. Below we give a complete, self-contained, elementary proof of the remaining open case: **Part (ii) for $p \equiv 1 \pmod 3$ (`conjecture_2`)**.

> *Historical remark:* The auxiliary supercongruence in Lemma 3(b) below ($\sum_{k=0}^{2(p-1)/3}\binom{2k}{k} \equiv 1 \pmod{p^2}$ for $p \equiv 1 \pmod 3$, conjectured by A. Adamchuk on OEIS A066796 in 2006) and the reduced sum $F(1) \equiv 0 \pmod p$ in Lemma 1 were previously proved by G.-S. Mao (*J. Combin. Theory Ser. A* **181** (2021), 105478, `arXiv:2003.09810v4`, Theorems 1.1–1.2) using hypergeometric transformations, `Sigma` CAS certificates, and $p$-adic Gamma functions, without connection to OEIS A208425. Our proof below is entirely self-contained and elementary, requiring no CAS certificates, hypergeometric identities, or $p$-adic Gamma functions; in particular, Lemma 3 gives a short direct proof of Adamchuk's congruence via a $3$-orbit cancellation in $\mathbb{F}_p$.

---

## Theorem

Let $a(j) = \sum_{k=0}^{j} \binom{j}{k}\binom{j-k}{k}\binom{j+k}{k}$. For every prime $p \equiv 1 \pmod 3$,
$$\sum_{j=0}^{p-1} a(j) \equiv \binom{\frac{2(p-1)}{3}}{\frac{p-1}{3}} \pmod{p^2}.$$

---

## Proof

Every prime $p \equiv 1 \pmod 3$ is odd and satisfies $p \ge 7$, so we write $p = 6n + 1$ with an integer $n \ge 1$. Set
$$r := \frac{p-1}{3} = 2n, \qquad m := \frac{p-1}{2} = 3n, \qquad \Phi(X) := X^2 - X + 1, \qquad u(X) := X(1-X) = 1 - \Phi(X).$$
Throughout, for $M \ge 1$, let $H_M := \sum_{j=1}^{M} \frac{1}{j} \in \mathbb{Q}$ denote the $M$-th harmonic number (viewed in $\mathbb{Z}_{(p)}$ when $M < p$).

### Step 1. Equivalence of definitions and reduction modulo $p^2$

**Lemma 1.** *For all $j \ge 0$, $[x^j]\sum_{k \ge 0} \frac{(3k)!}{k!^3}\frac{x^{2k}}{(1-x)^{3k+1}} = \sum_{k=0}^{j}\binom{j}{k}\binom{j-k}{k}\binom{j+k}{k}$. Moreover, for $p = 6n + 1$,*
$$\sum_{j=0}^{p-1} a(j) \equiv \binom{4n}{2n} + p \sum_{\substack{0 \le k \le 3n \\ k \neq 2n}} \frac{\binom{2k}{k}}{3k+1} \pmod{p^2}.$$

*Proof.* Using $(1-x)^{-(3k+1)} = \sum_{d \ge 0}\binom{d+3k}{3k} x^d$, the coefficient of $x^j$ in $\frac{(3k)!}{k!^3}\frac{x^{2k}}{(1-x)^{3k+1}}$ vanishes for $2k > j$ and equals
$$\frac{(3k)!}{k!^3}\binom{j+k}{3k} = \binom{3k}{k}\binom{2k}{k}\binom{j+k}{3k} = \frac{(j+k)!}{k!^3(j-2k)!} = \binom{j}{k}\binom{j-k}{k}\binom{j+k}{k}$$
for $0 \le 2k \le j$ (while $\binom{j-k}{k} = 0$ for $2k > j$). This establishes the equivalence of the two definitions of $a(j)$.

Summing over $0 \le j \le p-1$ and applying the hockey-stick identity $\sum_{j=2k}^{p-1}\binom{j+k}{3k} = \sum_{i=3k}^{p+k-1}\binom{i}{3k} = \binom{p+k}{3k+1}$ gives
$$\sum_{j=0}^{p-1} a(j) = \sum_{k=0}^{3n} t_k, \qquad t_k := \binom{3k}{k}\binom{2k}{k}\binom{p+k}{3k+1},$$
since $2k \le p-1 = 6n \iff k \le 3n$.

For every $k \in \{0, 1, \dots, 3n\}$, we have $p - 2k - 1 = 6n - 2k \ge 0$, so
$$\binom{3k}{k}\binom{p+k}{3k+1} = \frac{(3k)!}{k!(2k)!}\cdot\frac{(p+k)!}{(3k+1)!(p-2k-1)!} = \frac{p}{3k+1}\cdot\frac{\prod_{j=1}^{k}(p+j)}{k!}\cdot\frac{\prod_{j=1}^{2k}(p-j)}{(2k)!}.$$
Note that $k \le 3n < p$ and $2k \le 6n < p$, so $p \nmid k!$ and $p \nmid (2k)!$. Also $1 \le 3k + 1 \le 9n + 1 < 12n + 2 = 2p$, so $p \mid (3k+1)$ if and only if $3k + 1 = p$, i.e., $k = 2n$.

- At $k = 2n$: $3k = p - 1$ and $3k + 1 = p$, so
  $$t_{2n} = \binom{4n}{2n}\binom{p-1}{2n}\binom{p+2n}{p}.$$
  Since $2n$ is even,
  $$\binom{p-1}{2n} = \prod_{j=1}^{2n}\frac{p-j}{j} = \prod_{j=1}^{2n}\left(1 - \frac{p}{j}\right) \equiv 1 - p H_{2n} \pmod{p^2},$$
  $$\binom{p+2n}{p} = \binom{p+2n}{2n} = \prod_{j=1}^{2n}\left(1 + \frac{p}{j}\right) \equiv 1 + p H_{2n} \pmod{p^2}.$$
  Multiplying gives $t_{2n} \equiv \binom{4n}{2n}(1 - p^2 H_{2n}^2) \equiv \binom{4n}{2n} \pmod{p^2}$.
- For $k \in \{0, \dots, 3n\} \setminus \{2n\}$: $p \nmid (3k+1)$, so $p \mid t_k$ and
  $$\frac{t_k}{p} = \frac{\binom{2k}{k}}{3k+1} \prod_{j=1}^{k}\left(1 + \frac{p}{j}\right) \prod_{j=1}^{2k}\left(1 - \frac{p}{j}\right) \equiv \frac{\binom{2k}{k}}{3k+1} \pmod p.$$

Summing over $k$ proves the lemma. $\square$

Define the polynomial
$$F(X) := \sum_{\substack{0 \le k \le 3n \\ k \neq 2n}} \frac{\binom{2k}{k}}{3k+1} X^k \in \mathbb{F}_p[X].$$
By Lemma 1, the theorem is equivalent to $F(1) = 0$ in $\mathbb{F}_p$.

---

### Step 2. Self-contained proof of $\sum_{k=0}^{p-1}\binom{2k}{k} \equiv 1 \pmod{p^2}$

**Lemma 2.** *For every prime $p = 6n + 1$,*
$$(a)\quad H_n - H_{2n} \equiv H_{3n} \pmod p, \qquad\qquad (b)\quad \sum_{k=0}^{p-1}\binom{2k}{k} \equiv 1 \pmod{p^2}.$$

*Proof.* (a) Pairing $t \leftrightarrow p - t$ in $\{1, \dots, p-1\}$ gives $H_{6n} = H_{p-1} \equiv 0 \pmod p$, and pairing $t \leftrightarrow p - t$ between $[1, 2n]$ and $[4n+1, 6n]$ gives
$$H_{4n} = H_{6n} - \sum_{t=1}^{2n}\frac{1}{p - t} \equiv H_{2n} \pmod p.$$
Splitting $H_{4n}$ into even and odd indices yields
$$\sum_{j=1}^{2n}\frac{1}{2j-1} = H_{4n} - \sum_{j=1}^{2n}\frac{1}{2j} = H_{4n} - \frac{1}{2}H_{2n} \equiv \frac{1}{2}H_{2n} \pmod p.$$
On the other hand, $p - (2j - 1) = 6n + 2 - 2j = 2(3n + 1 - j)$ maps $1 \le j \le 2n$ bijectively to $n + 1 \le 3n + 1 - j \le 3n$, so
$$\sum_{j=1}^{2n}\frac{1}{2j-1} \equiv -\sum_{j=1}^{2n}\frac{1}{2(3n+1-j)} = -\frac{1}{2}(H_{3n} - H_n) \pmod p.$$
Comparing the two congruences and multiplying by $2$ gives $H_{2n} \equiv H_n - H_{3n} \pmod p$, i.e., $H_n - H_{2n} \equiv H_{3n} \pmod p$.

(b) In the Laurent polynomial ring $\mathbb{Z}[x, x^{-1}]$, we have $\binom{2k}{k} = [x^0]\bigl(\frac{(1+x)^2}{x}\bigr)^k$, so the finite geometric series gives
$$\sum_{k=0}^{p-1}\binom{2k}{k} = [x^0]\frac{\bigl(\frac{(1+x)^2}{x}\bigr)^p - 1}{\frac{(1+x)^2}{x} - 1} = [x^{p-1}]\frac{(1+x)^{2p} - x^p}{1 + x + x^2}.$$
In $\mathbb{Z}[[x]]$, $\frac{x^p}{1+x+x^2}$ has no $x^{p-1}$ term, and $\frac{1}{1+x+x^2} = \frac{1-x}{1-x^3} = (1-x)\sum_{j \ge 0} x^{3j}$. Extracting $[x^{p-1}] = [x^{6n}]$ gives the exact identity
$$\sum_{k=0}^{p-1}\binom{2k}{k} = \sum_{j=0}^{2n}\binom{2p}{6n-3j} - \sum_{j=0}^{2n-1}\binom{2p}{6n-3j-1} = 1 + \sum_{j=0}^{2n-1}\left(\binom{2p}{6n-3j} - \binom{2p}{6n-3j-1}\right).$$
For every $1 \le s \le p - 1$,
$$\binom{2p}{s} = \frac{2p}{s}\prod_{i=1}^{s-1}\frac{2p-i}{i} \equiv \frac{2p}{s}(-1)^{s-1} \pmod{p^2}.$$
Setting $A_c := \sum_{\substack{1 \le t \le 6n \\ t \equiv c \pmod 3}} \frac{(-1)^t}{t} \in \mathbb{Z}_{(p)}$ for $c \in \{0, 1, 2\}$, we observe that for $t = 6n - 3j \equiv 0 \pmod 3$ we have $(-1)^{t-1} = -(-1)^t$, while for $t' = 6n - 3j - 1 \equiv 2 \pmod 3$ we have $-(-1)^{t'-1} = (-1)^{t'}$. Therefore
$$\frac{1}{2p}\left(\sum_{k=0}^{p-1}\binom{2k}{k} - 1\right) \equiv -A_0 + A_2 = -(A_0 - A_2) \pmod p.$$
Since $p = 6n + 1$ is odd, the involution $t \mapsto p - t$ satisfies $\frac{(-1)^{p-t}}{p-t} \equiv \frac{-(-1)^t}{-t} = \frac{(-1)^t}{t} \pmod p$ and maps $\{t \equiv 0 \pmod 3\}$ bijectively onto $\{t \equiv 1 \pmod 3\}$, so $A_0 \equiv A_1 \pmod p$. Consequently,
$$A_0 - A_2 \equiv 3A_0 - (A_0 + A_1 + A_2) \pmod p.$$
Finally,
$$3A_0 = \sum_{k=1}^{2n}\frac{(-1)^{3k}}{k} = \sum_{k=1}^{2n}\frac{(-1)^k}{k} = 2\sum_{j=1}^{n}\frac{1}{2j} - \sum_{k=1}^{2n}\frac{1}{k} = H_n - H_{2n},$$
$$A_0 + A_1 + A_2 = \sum_{t=1}^{6n}\frac{(-1)^t}{t} = 2\sum_{j=1}^{3n}\frac{1}{2j} - \sum_{t=1}^{6n}\frac{1}{t} = H_{3n} - H_{6n} \equiv H_{3n} \pmod p.$$
By part (a), $A_0 - A_2 \equiv (H_n - H_{2n}) - H_{3n} \equiv 0 \pmod p$, whence $\sum_{k=0}^{p-1}\binom{2k}{k} \equiv 1 \pmod{p^2}$. $\square$

---

### Step 3. Three-orbit cancellation and Adamchuk's truncated congruence

**Lemma 3.** *For every prime $p = 6n + 1$,*
$$(a)\quad \sum_{i=0}^{2n-1} \frac{1}{(2i+1)\binom{2i}{i}} \equiv 0 \pmod p, \qquad\qquad (b)\quad \sum_{k=0}^{4n} \binom{2k}{k} \equiv 1 \pmod{p^2}.$$

*Proof.* (a) Repeated integration by parts on $I_{a,b} := \int_0^1 t^a(1-t)^b\,dt$ gives $I_{a,b} = \frac{b}{a+1} I_{a+1,b-1}$ for $b \ge 1$ and $I_{a,0} = \frac{1}{a+1}$, so $I_{i,i} = \frac{i!^2}{(2i+1)!} = \frac{1}{(2i+1)\binom{2i}{i}}$. Since $1 - t(1-t) = 1 - t + t^2 = \Phi(t)$, the polynomial
$$P(t) := \sum_{i=0}^{2n-1} (t(1-t))^i = \frac{1 - (t(1-t))^{2n}}{1 - t + t^2} \in \mathbb{Z}[t]$$
has degree $4n - 2 < p - 1$ and satisfies
$$\sum_{i=0}^{2n-1} \frac{1}{(2i+1)\binom{2i}{i}} = \int_0^1 P(t)\,dt \in \mathbb{Z}_{(p)}.$$

Define the integer polynomial
$$L_{\mathrm{poly}}(X) := \frac{1 - X^p - (1-X)^p}{p} = -\sum_{j=1}^{p-1}\frac{(-1)^j\binom{p}{j}}{p} X^j \in \mathbb{Z}[X].$$
For $1 \le j \le p - 1$, $-\frac{(-1)^j\binom{p}{j}}{p} = -\frac{(-1)^j}{j}\binom{p-1}{j-1} \equiv -\frac{(-1)^j}{j}(-1)^{j-1} = \frac{1}{j} \pmod p$, so the reduction $L(t) := L_{\mathrm{poly}}(t) \bmod p \in \mathbb{F}_p[t]$ equals $\sum_{j=1}^{p-1} \frac{t^j}{j}$.

Writing $P(t) \equiv \sum_{k=0}^{4n-2} c_k t^k \pmod p$, the product $P(t)L(t) \in \mathbb{F}_p[t]$ has zero constant term and degree $(4n-2) + (p-1) = 10n - 2 < 12n = 2(p-1)$. Since $\sum_{x \in \mathbb{F}_p} x^d$ equals $-1$ for $d = p-1$ and $0$ for every $1 \le d < 2(p-1)$ with $d \neq p-1$, we obtain in $\mathbb{F}_p$:
$$\sum_{x \in \mathbb{F}_p} P(x)L(x) = -[t^{p-1}](P(t)L(t)) = -\sum_{k=0}^{4n-2}\frac{c_k}{p-1-k} = \sum_{k=0}^{4n-2}\frac{c_k}{k+1} = \int_0^1 P(t)\,dt.$$

We now evaluate $\sum_{x \in \mathbb{F}_p} P(x)L(x)$ directly:
1. **Vanishing at $\{0, 1, \zeta, \zeta^{-1}\}$:** Since $p = 6n + 1$, the multiplicative group $\mathbb{F}_p^\times$ contains a primitive $6$-th root of unity $\zeta$, and $\Phi(t) = (t-\zeta)(t-\zeta^{-1})$ splits into two distinct roots in $\mathbb{F}_p \setminus \{0, 1\}$. Clearly $L(0) = L_{\mathrm{poly}}(0) = 0$ and $L(1) = L_{\mathrm{poly}}(1) = 0$. In the quotient ring $\mathbb{Z}[X]/(\Phi(X))$, we have $X^2 \equiv X - 1$, $X^3 \equiv -1$, $X^6 \equiv 1$, and $1 - X \equiv -X^2 \equiv X^5$; since $p = 6n + 1$,
   $$p L_{\mathrm{poly}}(X) = 1 - X^p - (1-X)^p \equiv 1 - X - X^{5p} \equiv 1 - X - X^5 = 1 - X - (1-X) = 0 \pmod{\Phi(X)}.$$
   Because $\Phi(X)$ is monic in $\mathbb{Z}[X]$, $\Phi(X)$ divides $L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$. Reducing modulo $p$ gives $L(\zeta) = L(\zeta^{-1}) = 0$ in $\mathbb{F}_p$.

2. **Cancellation on $3$-orbits:** Let $U := \mathbb{F}_p \setminus \{0, 1, \zeta, \zeta^{-1}\}$. The Möbius map $\sigma(x) := \frac{1}{1-x}$ restricts to a well-defined, fixed-point-free permutation of $U$ of order $3$ (indeed $\sigma(x) = x \iff x^2 - x + 1 = 0$, $\sigma^2(x) = \frac{x-1}{x}$, $\sigma^3(x) = x$), partitioning $U$ into disjoint $3$-orbits $\{x, y, z\}$ with $y = \frac{1}{1-x}$ and $z = \frac{x-1}{x}$.
   For any orbit $\{x, y, z\} \subset U$:
   - Since $2n$ is even and $x^{6n} = (1-x)^{6n} = 1$ in $\mathbb{F}_p^\times$,
     $$(y(1-y))^{2n} = \left(\frac{-x}{(1-x)^2}\right)^{2n} = \frac{x^{2n}(1-x)^{2n}}{(1-x)^{6n}} = (x(1-x))^{2n},$$
     $$(z(1-z))^{2n} = \left(\frac{-(1-x)}{x^2}\right)^{2n} = \frac{x^{2n}(1-x)^{2n}}{x^{6n}} = (x(1-x))^{2n}.$$
   - Moreover, $1 - y + y^2 = \frac{1-x+x^2}{(1-x)^2}$ and $1 - z + z^2 = \frac{1-x+x^2}{x^2}$, whence
     $$P(y) = (1-x)^2 P(x), \qquad P(z) = x^2 P(x).$$
   - Choose an integer lift $\tilde{x} \in \{2, \dots, p-1\}$ of $x$. Then $\tilde{y} := \frac{1}{1-\tilde{x}} \in \mathbb{Z}_{(p)}$ and $\tilde{z} := \frac{\tilde{x}-1}{\tilde{x}} \in \mathbb{Z}_{(p)}$ lift $y$ and $z$, respectively. Evaluating the integer polynomial $L_{\mathrm{poly}}$ at $\tilde{y}$ and $\tilde{z}$ (using $p$ odd so $(-\tilde{x})^p = -\tilde{x}^p$ and $(\tilde{x}-1)^p = -(1-\tilde{x})^p$) gives
     $$L_{\mathrm{poly}}(\tilde{y}) = \frac{1 - \frac{1}{(1-\tilde{x})^p} - \left(\frac{-\tilde{x}}{1-\tilde{x}}\right)^p}{p} = \frac{(1-\tilde{x})^p - 1 + \tilde{x}^p}{p(1-\tilde{x})^p} = \frac{-L_{\mathrm{poly}}(\tilde{x})}{(1-\tilde{x})^p} \equiv -\frac{L(x)}{1-x} \pmod p,$$
     $$L_{\mathrm{poly}}(\tilde{z}) = \frac{1 - \left(\frac{\tilde{x}-1}{\tilde{x}}\right)^p - \frac{1}{\tilde{x}^p}}{p} = \frac{\tilde{x}^p + (1-\tilde{x})^p - 1}{p\tilde{x}^p} = \frac{-L_{\mathrm{poly}}(\tilde{x})}{\tilde{x}^p} \equiv -\frac{L(x)}{x} \pmod p.$$
   - Therefore, on every $3$-orbit $\{x, y, z\} \subset U$,
     $$P(x)L(x) + P(y)L(y) + P(z)L(z) = P(x)L(x)\bigl(1 - (1-x) - x\bigr) = 0.$$

Summing over $\{0, 1, \zeta, \zeta^{-1}\}$ and all $3$-orbits in $U$ gives $\sum_{i=0}^{2n-1} \frac{1}{(2i+1)\binom{2i}{i}} = \sum_{x \in \mathbb{F}_p} P(x)L(x) = 0$ in $\mathbb{F}_p$.

(b) For every $0 \le a \le p-1$, Wilson's theorem $(p-1)! \equiv -1 \pmod p$ together with $(p-1)! = (p-1-a)!\prod_{j=1}^{a}(p-j) \equiv (-1)^a a!(p-1-a)! \pmod p$ yields $(p-1-a)! \equiv \frac{(-1)^{a+1}}{a!} \pmod p$. For each $0 \le i \le 2n-1$, setting $k = p - 1 - i \in [4n+1, p-1]$ gives $2k = 2p - 2 - 2i > p$, so $p \mid \binom{2k}{k}$ and
$$\frac{1}{p}\binom{2(p-1-i)}{p-1-i} = \frac{(p-1)!\prod_{j=1}^{p-2-2i}(p+j)}{(p-1-i)!^2} \equiv \frac{(-1)\cdot (p-2-2i)!}{(p-1-i)!^2} \equiv \frac{(-1)\cdot\frac{(-1)^{2i+2}}{(2i+1)!}}{\left(\frac{(-1)^{i+1}}{i!}\right)^2} = -\frac{1}{(2i+1)\binom{2i}{i}} \pmod p.$$
Combining this with Lemma 2(b) and part (a) yields
$$\sum_{k=0}^{4n}\binom{2k}{k} = \sum_{k=0}^{p-1}\binom{2k}{k} - \sum_{i=0}^{2n-1}\binom{2(p-1-i)}{p-1-i} \equiv 1 + p\sum_{i=0}^{2n-1}\frac{1}{(2i+1)\binom{2i}{i}} \equiv 1 \pmod{p^2}. \quad\square$$

---

### Step 4. Polynomial differential equation and Frobenius lift

Define $H(X) := 3 X^{4n+1} F(X) \in \mathbb{F}_p[X]$. For every $k \ge 1$, define $Q_k(X) := \int_0^X u(t)^{k-1}\,dt \in \mathbb{Q}[X]$. Since $u(t)^{4n} = t^{4n}(1-t)^{4n}$ has exponents in $[4n, 8n]$, the only multiple of $p = 6n+1$ among the exponents $[4n+1, 8n+1]$ of $Q_{4n+1}(X)$ is $p$ itself, and $[t^{p-1}] u(t)^{4n} = [t^{2n}](1-t)^{4n} = (-1)^{2n}\binom{4n}{2n} = \binom{4n}{2n}$. Hence
$$\tilde{Q}(X) := Q_{4n+1}(X) - \binom{4n}{2n}\frac{X^p}{p} = \int_0^X \left(u(t)^{4n} - \binom{4n}{2n} t^{p-1}\right)dt \in \mathbb{Z}_{(p)}[X].$$
Also define the integer polynomial
$$R(X) := \frac{u(X)^p - X^p + X^{2p}}{p} = \frac{X^p\bigl((1-X)^p - 1 + X^p\bigr)}{p} = -X^p L_{\mathrm{poly}}(X) \in \mathbb{Z}[X].$$

**Lemma 4.** *(a) $p Q_{4n+1}(1) \equiv \binom{4n}{2n} \pmod{p^2}$, hence $\tilde{Q}(1) \equiv 0 \pmod p$.*
*(b) In $\mathbb{F}_p[X]$,*
$$H(u(X)) \equiv (1 - 2X^p)\tilde{Q}(X) - \binom{4n}{2n} R(X) \pmod p.$$

*Proof.* (a) By the Beta integral, $Q_{4n+1}(1) = I_{4n,4n} = \frac{(4n)!^2}{(8n+1)!}$. Since $8n + 1 = p + 2n$ and $p - 1 - 2n = 4n$, we have $(p+2n)! = p\cdot(p-1)!\prod_{j=1}^{2n}(p+j)$ and $(p-1)! = (4n)!\prod_{j=1}^{2n}(p-j)$. Because $2n$ is even,
$$p Q_{4n+1}(1) = \frac{p\cdot(4n)!^2}{(p+2n)!} = \frac{(4n)!}{\prod_{j=1}^{2n}(p+j)(p-j)} = \frac{(4n)!}{(2n)!^2 \prod_{j=1}^{2n}\left(1 - \frac{p^2}{j^2}\right)} = \frac{\binom{4n}{2n}}{\prod_{j=1}^{2n}\left(1 - \frac{p^2}{j^2}\right)} \equiv \binom{4n}{2n} \pmod{p^2}.$$
Dividing by $p$ gives $\tilde{Q}(1) = Q_{4n+1}(1) - \frac{\binom{4n}{2n}}{p} \equiv 0 \pmod p$.

(b) Since $3(k + 4n + 1) = 3k + 2p + 1 \equiv 3k + 1 \pmod p$, differentiating $H(X) = \sum_{\substack{0 \le k \le 3n \\ k \neq 2n}} \frac{3\binom{2k}{k}}{3k+1} X^{k+4n+1}$ in $\mathbb{F}_p[X]$ gives
$$H'(X) = \sum_{\substack{0 \le k \le 3n \\ k \neq 2n}} \binom{2k}{k} X^{k+4n} = X^{4n}\sum_{k=0}^{3n}\binom{2k}{k} X^k - \binom{4n}{2n} X^{p-1}.$$
For every $0 \le k \le 3n = \frac{p-1}{2}$,
$$\binom{3n}{k}(-4)^k = \frac{\prod_{j=0}^{k-1}(\frac{p-1}{2}-j)}{k!}(-4)^k \equiv \frac{\prod_{j=0}^{k-1}(2j+1)\cdot 2^k}{k!} = \frac{(2k)!}{k!^2} = \binom{2k}{k} \pmod p,$$
so $\sum_{k=0}^{3n}\binom{2k}{k} X^k = (1-4X)^{3n}$ in $\mathbb{F}_p[X]$. Substituting $u(X) = X(1-X)$ (with $1 - 4u = (1-2X)^2$ and $u'(X) = 1 - 2X$) gives in $\mathbb{F}_p[X]$:
$$(H(u(X)))' = H'(u)\,u'(X) = u^{4n}(1-2X)^{6n+1} - \binom{4n}{2n} u^{p-1}(1-2X) = (1-2X^p)u^{4n} - \binom{4n}{2n} u^{p-1}(1-2X),$$
where we used $(1-2X)^p = 1 - 2X^p$ in $\mathbb{F}_p[X]$.

On the other hand, differentiating $p R(X) = u(X)^p - X^p + X^{2p}$ over $\mathbb{Z}[X]$ and dividing by $p$ yields the exact identity $R'(X) = u(X)^{p-1}(1-2X) - X^{p-1} + 2X^{2p-1}$. Setting $A(X) := (1-2X^p)\tilde{Q}(X) - \binom{4n}{2n} R(X) \in \mathbb{Z}_{(p)}[X]$, we compute in $\mathbb{F}_p[X]$:
$$A'(X) \equiv (1-2X^p)\left(u^{4n} - \binom{4n}{2n} X^{p-1}\right) - \binom{4n}{2n}\bigl(u^{p-1}(1-2X) - X^{p-1} + 2X^{2p-1}\bigr) = (H(u(X)))' \pmod p.$$

Now compare degrees: $\deg H(u) \le 2(3n + 4n + 1) = 14n + 2 = 2p + 2n < 3p$, $\deg((1-2X^p)\tilde{Q}) = p + 8n + 1 = 2p + 2n < 3p$, and $\deg R = 2p - 1 < 3p$. Since $(H(u) - A)' = 0$ in $\mathbb{F}_p[X]$, there exist $c_0, c_1, c_2 \in \mathbb{F}_p$ such that
$$H(u(X)) - A(X) \equiv c_0 + c_1 X^p + c_2 X^{2p} \pmod p.$$
- **Constant term $c_0$:** At $X = 0$, $u(0) = 0 \implies H(0) = 0$, $\tilde{Q}(0) = 0$, and $R(0) = 0$, so $c_0 = 0$.
- **Coefficient $c_2 = [X^{2p}](H(u) - A)$:** Since $\deg \tilde{Q} = 8n+1 < 2p$, $[X^p]\tilde{Q} = 0$, and $\deg R = 2p-1 < 2p$, we have $[X^{2p}]A = 0$. In $H(u(X))$, terms with $k < 2n$ have degree $2(k+4n+1) \le 12n < 2p$, while terms with $k = 2n + j$ ($1 \le j \le n$) have $u^{k+4n+1} = u^{p+j} \equiv (X^p - X^{2p}) X^j(1-X)^j \pmod p$, whose exponents lie in $[p+1, p+2n] \cup [2p+1, 2p+2n]$ and never hit $2p$. Hence $[X^{2p}]H(u) = 0$, giving $c_2 = 0$.
- **Coefficient $c_1$:** Evaluating at $X = 1$ gives $u(1) = 0 \implies H(u(1)) = 0$, $R(1) = 0$, and $A(1) = (1-2)\tilde{Q}(1) = -\tilde{Q}(1) \equiv 0 \pmod p$ by part (a). Hence $c_1 = 0$.

Therefore $H(u(X)) \equiv A(X) \pmod p$ in $\mathbb{F}_p[X]$. $\square$

---

### Step 5. Exact telescoping and completion of the proof

**Lemma 5.** *As an exact identity in $\mathbb{Q}[X]$,*
$$2 Q_{4n+1}(X) = Q_{4n+1}(1)\left(1 + (2X - 1)\sum_{k=0}^{4n}\binom{2k}{k} u(X)^k\right).$$

*Proof.* For every $k \ge 1$, since $(1-2t)^2 = 1 - 4u(t)$,
$$\frac{d}{dt}\bigl((1-2t)u(t)^k\bigr) = -2u(t)^k + k(1-2t)^2 u(t)^{k-1} = k u(t)^{k-1} - (4k+2)u(t)^k.$$
Integrating from $0$ to $X$ (noting $u(0) = 0$) gives $k Q_k(X) - (4k+2)Q_{k+1}(X) = (1-2X)u(X)^k$. Multiplying by $\binom{2k}{k}$ and using $(4k+2)\binom{2k}{k} = (k+1)\binom{2k+2}{k+1}$ gives
$$k\binom{2k}{k} Q_k(X) - (k+1)\binom{2k+2}{k+1} Q_{k+1}(X) = \binom{2k}{k}(1-2X)u(X)^k \qquad (k \ge 1).$$
Summing from $k = 1$ to $4n$, noting $1\cdot\binom{2}{1} Q_1(X) = 2X$, and adding $(1-2X)$ to both sides yields
$$1 - (4n+1)\binom{8n+2}{4n+1} Q_{4n+1}(X) = (1-2X)\sum_{k=0}^{4n}\binom{2k}{k} u(X)^k.$$
Finally, $(4n+1)\binom{8n+2}{4n+1} = 2(8n+1)\binom{8n}{4n} = \frac{2(8n+1)!}{(4n)!^2} = \frac{2}{Q_{4n+1}(1)}$. Rearranging produces the claimed identity. $\square$

**Completion of the proof of the Theorem.**
Subtracting $2\binom{4n}{2n}\frac{X^p}{p}$ from both sides of Lemma 5 gives in $\mathbb{Q}[X]$:
$$2\tilde{Q}(X) = Q_{4n+1}(1)\left(1 + (2X-1)\sum_{k=0}^{4n}\binom{2k}{k} u(X)^k\right) - 2\binom{4n}{2n}\frac{X^p}{p}.$$
Reduce modulo the monic polynomial $\Phi(X) = X^2 - X + 1 \in \mathbb{Z}[X]$. Since $u(X) = 1 - \Phi(X) \equiv 1 \pmod{\Phi(X)}$ and $X^p = X^{6n+1} \equiv X \pmod{\Phi(X)}$ (as $X^6 \equiv 1 \pmod{\Phi(X)}$), we have $2X^p \equiv 2X = 1 + (2X-1) \pmod{\Phi(X)}$, and therefore in $\mathbb{Q}[X]/(\Phi(X))$:
$$2\tilde{Q}(X) \equiv \left(Q_{4n+1}(1) - \frac{\binom{4n}{2n}}{p}\right) + (2X-1)\left(Q_{4n+1}(1)\sum_{k=0}^{4n}\binom{2k}{k} - \frac{\binom{4n}{2n}}{p}\right) \pmod{\Phi(X)}.$$
By Lemma 4(a), $p Q_{4n+1}(1) \equiv \binom{4n}{2n} \pmod{p^2}$, so the constant term lies in $p\mathbb{Z}_{(p)}$. Combining Lemma 4(a) with Lemma 3(b) ($\sum_{k=0}^{4n}\binom{2k}{k} \equiv 1 \pmod{p^2}$) gives
$$p Q_{4n+1}(1)\sum_{k=0}^{4n}\binom{2k}{k} - \binom{4n}{2n} \equiv \binom{4n}{2n}\cdot 1 - \binom{4n}{2n} = 0 \pmod{p^2},$$
so the coefficient of $(2X-1)$ also lies in $p\mathbb{Z}_{(p)}$. Since $\tilde{Q}(X) \in \mathbb{Z}_{(p)}[X]$ and $\Phi(X)$ is monic in $\mathbb{Z}[X]$, reducing modulo $p$ and evaluating at a root $\zeta \in \mathbb{F}_p^\times$ of $\Phi(X)$ yields $2\tilde{Q}(\zeta) = 0$ in $\mathbb{F}_p$, hence $\tilde{Q}(\zeta) = 0$ (as $p \ge 7$ is odd).

Also, by Step 3, $\Phi(X)$ divides $L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$, hence $\Phi(X)$ divides $R(X) = -X^p L_{\mathrm{poly}}(X)$ in $\mathbb{Z}[X]$, so $R(\zeta) = 0$ in $\mathbb{F}_p$. Evaluating Lemma 4(b) at $X = \zeta$ (where $u(\zeta) = 1$) gives
$$3 F(1) = H(1) = H(u(\zeta)) = (1 - 2\zeta^p)\tilde{Q}(\zeta) - \binom{4n}{2n} R(\zeta) = 0 \quad \text{in } \mathbb{F}_p.$$
Since $p \ge 7$, $3 \not\equiv 0 \pmod p$, so $F(1) = 0$ in $\mathbb{F}_p$. By Lemma 1,
$$\sum_{j=0}^{p-1} a(j) \equiv \binom{4n}{2n} = \binom{\frac{2(p-1)}{3}}{\frac{p-1}{3}} \pmod{p^2}. \qquad \blacksquare$$

---

## Verification

The exact-arithmetic script [`verify.py`](file:///Users/kev/Documents/open-math/targets/oeis-A208425/verify.py) independently verifies:
- exact equivalence of both definitions of $a(j)$ for $0 \le j \le 60$,
- the exact rational telescoping identity (Lemma 5) and polynomial congruence $H(u(X)) \equiv A(X) \pmod p$ (Lemma 4) for $p \in \{7, 13, 19, 31, 37, 43\}$,
- Lemma 1, Lemma 2, Lemma 3 (including the $3$-orbit cancellation on every $x \in \mathbb{F}_p$), and the full target supercongruence `conjecture_2` for all $45$ primes $p \equiv 1 \pmod 3$ with $7 \le p \le 499$ (direct summation of $a(j)$ for $p \le 200$ and exact hockey-stick evaluation for all $p \le 499$).

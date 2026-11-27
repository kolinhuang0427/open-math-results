# Counterexample to Remark 5.14 of Mináč–Nguyen–Tân (`arXiv:2411.01768v2`)

**Verdict:** **NO (FALSE).** So's conjecture fails for the family $G_f(D)$ over $\mathbb{F}_q[x]$ even when all irreducible factors of $f$ have pairwise **different degrees** — in fact, for **every** finite field $\mathbb{F}_q$ (including squarefree $f$ and connected isomorphic gcd-graphs).

---

## 1. Minimal Counterexample ($16$ vertices over $\mathbb{F}_2[x]$)

Let $q = 2$ and take
$$f(x) = x^2 (x^2 + x + 1) \in \mathbb{F}_2[x], \qquad \deg f = 4.$$
Its monic irreducible factors are $P_1(x) = x$ (degree $1$) and $P_2(x) = x^2 + x + 1$ (degree $2$), which have **different degrees** ($1 \neq 2$). The monic divisors of $f$ other than $f$ are
$$\mathrm{Div}(f) \setminus \{f\} = \{1,\; x,\; x^2,\; x^2+x+1,\; x(x^2+x+1)\}.$$
Choose the two distinct subsets
$$D_1 = \{x^2\}, \qquad D_2 = \{x^2 + x + 1,\; x(x^2 + x + 1)\}.$$
Then:
- $G_f(D_1)$ has generating set $S_{D_1} = \{h \in \mathbb{F}_2[x]/f : \gcd(h, f) = x^2\} = \{x^2,\; x^2(x+1),\; x^2 x\} = (x^2)/(f) \setminus \{0\}$, which is the nonzero elements of a $2$-dimensional $\mathbb{F}_2$-subspace (an ideal of size $4$). Thus
  $$G_f(D_1) \cong 4 K_4$$
  (four vertex-disjoint copies of $K_4$).
- $G_f(D_2)$ has generating set $S_{D_2} = \{h \in \mathbb{F}_2[x]/f : \gcd(h, f) \in D_2\} = \{x^2+x+1,\; x(x^2+x+1),\; (x+1)(x^2+x+1)\} = (x^2+x+1)/(f) \setminus \{0\}$, again the nonzero elements of an ideal of size $4$. Thus
  $$G_f(D_2) \cong 4 K_4 \cong G_f(D_1).$$

Moreover, taking complements in $\mathrm{Div}(f) \setminus \{f\}$,
$$\widetilde{D}_1 = \{1,\; x,\; x^2+x+1,\; x(x^2+x+1)\}, \qquad \widetilde{D}_2 = \{1,\; x,\; x^2\},$$
gives **connected** regular gcd-graphs $G_f(\widetilde{D}_1) \cong K_{4,4,4,4} \cong G_f(\widetilde{D}_2)$ with $\widetilde{D}_1 \neq \widetilde{D}_2$.

---

## 2. Minimal Squarefree Counterexample ($64$ vertices over $\mathbb{F}_2[x]$)

Let $q = 2$ and take
$$f(x) = x (x^2 + x + 1) (x^3 + x + 1) \in \mathbb{F}_2[x], \qquad \deg f = 6.$$
Here $f$ is **squarefree** and its three monic irreducible factors $P_1 = x$, $P_2 = x^2+x+1$, $P_3 = x^3+x+1$ have pairwise **different degrees** $1, 2, 3$. Choose
$$D_1 = \{x(x^2+x+1)\}, \qquad D_2 = \{x^3+x+1,\; x(x^3+x+1),\; (x^2+x+1)(x^3+x+1)\}.$$
Then $S_{D_1} = (P_1 P_2)/(f) \setminus \{0\}$ and $S_{D_2} = (P_3)/(f) \setminus \{0\}$ are each the nonzero elements of an ideal of order $2^3 = 8$ in $\mathbb{F}_2[x]/(f)$, so
$$G_f(D_1) \cong 8 K_8 \cong G_f(D_2)$$
(and their complements $\widetilde{D}_i = \mathrm{Div}(f)\setminus(D_i\cup\{f\})$ give connected isomorphic graphs $K_{8,8,8,8,8,8,8,8}$).

---

## 3. General Theorem Over Every Finite Field $\mathbb{F}_q$

**Proposition.** *Let $q$ be any prime power and suppose $f = g \cdot h \in \mathbb{F}_q[x]$ is a monic polynomial factoring into two coprime nonconstant monic polynomials $g, h$ with $\deg g = \deg h = d \ge 1$. Define two subsets of $\mathrm{Div}(f) \setminus \{f\}$ by*
$$D_1 := \{ g \cdot u : u \in \mathrm{Div}(h) \setminus \{h\} \}, \qquad D_2 := \{ h \cdot v : v \in \mathrm{Div}(g) \setminus \{g\} \},$$
*and their complements $\widetilde{D}_i := (\mathrm{Div}(f)\setminus\{f\}) \setminus D_i$ ($i=1,2$). Then:*
1. *$D_1 \neq D_2$ and $\widetilde{D}_1 \neq \widetilde{D}_2$ (indeed $D_1 \cap D_2 = \emptyset$).*
2. *$G_f(D_1) \cong q^d K_{q^d} \cong G_f(D_2)$ and $G_f(\widetilde{D}_1) \cong K_{q^d, \dots, q^d} \cong G_f(\widetilde{D}_2)$ ($q^d$-partite complete graph on $q^{2d}$ vertices).*

*In particular, for every finite field $\mathbb{F}_q$, choosing distinct monic irreducibles $P_1, P_2 \in \mathbb{F}_q[x]$ with $\deg P_1 = d_1 \ge 1$ and $\deg P_2 = a d_1$ ($a \ge 2$) and setting $f = P_1^a P_2$ ($g = P_1^a, h = P_2$), or choosing distinct monic irreducibles $P_1, P_2, P_3 \in \mathbb{F}_q[x]$ of degrees $1, 2, 3$ and setting $f = P_1 P_2 P_3$ ($g = P_1 P_2, h = P_3$), yields infinitely many counterexamples in which all irreducible factors of $f$ have strictly distinct degrees.*

*Proof.* Since $\gcd(g, h) = 1$ and $\deg g = \deg h = d \ge 1$, every element of $D_1$ is divisible by $g$ while $h \nmid g$, and $g \in D_1 \setminus D_2$, so $D_1 \cap D_2 = \emptyset$ and $D_1 \neq D_2$ (and $\widetilde{D}_1 \neq \widetilde{D}_2$).

By the Chinese Remainder Theorem, $\theta : \mathbb{F}_q[x]/f \xrightarrow{\sim} \mathbb{F}_q[x]/(g) \times \mathbb{F}_q[x]/(h)$ via $a \mapsto (a \bmod g,\; a \bmod h)$ is a ring isomorphism, and both factors have cardinality $q^{\deg g} = q^{\deg h} = q^d$. For any $a, b \in \mathbb{F}_q[x]/f$ with $\theta(a) = (x_1, y_1)$ and $\theta(b) = (x_2, y_2)$:
- $\gcd(a - b, f) \in D_1$ if and only if $g \mid (a - b)$ and $f \nmid (a - b)$, i.e., $x_1 = x_2$ and $y_1 \neq y_2$;
- $\gcd(a - b, f) \in D_2$ if and only if $h \mid (a - b)$ and $f \nmid (a - b)$, i.e., $y_1 = y_2$ and $x_1 \neq x_2$.

Choose any bijection $\psi : \mathbb{F}_q[x]/(g) \xrightarrow{\sim} \mathbb{F}_q[x]/(h)$ (e.g., an $\mathbb{F}_q$-linear isomorphism between the two $d$-dimensional $\mathbb{F}_q$-vector spaces). Then the bijection $\Phi := \theta^{-1} \circ (\psi^{-1} \times \psi) \circ \theta$ on $\mathbb{F}_q[x]/f$ sends $(x, y) \mapsto (\psi^{-1}(y), \psi(x))$, mapping the adjacency condition $(x_1 = x_2 \land y_1 \neq y_2)$ of $G_f(D_1)$ equivalently onto the adjacency condition $(y'_1 = y'_2 \land x'_1 \neq x'_2)$ of $G_f(D_2)$. Hence $G_f(D_1) \cong G_f(D_2) \cong q^d K_{q^d}$, and passing to graph complements yields $G_f(\widetilde{D}_1) \cong G_f(\widetilde{D}_2) \cong K_{q^d,\dots,q^d}$.

Finally, because the number $S(m, q) = \frac{1}{m}\sum_{k \mid m}\mu(m/k)q^k$ of monic irreducibles of degree $m$ over $\mathbb{F}_q$ is strictly positive for all $m \ge 1$ and all prime powers $q \ge 2$ (as $q^m - \sum_{k \le m/2} q^k > 0$), irreducibles of degrees $d_1, a d_1$ and degrees $1, 2, 3$ always exist over every $\mathbb{F}_q$. $\square$

*(Remark: Over $\mathbb{Z}$, coprime integers $g, h > 1$ can never satisfy $|g| = |h|$ because unique factorization forbids equal cardinalities for coprime moduli; over $\mathbb{F}_q[x]$, $|\mathbb{F}_q[x]/g| = q^{\deg g}$ depends only on total degree, allowing $\deg g = \deg h$ even when the irreducible factors of $g$ and $h$ have pairwise distinct degrees.)*

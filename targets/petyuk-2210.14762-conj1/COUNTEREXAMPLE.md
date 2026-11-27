# Counterexample to Petyuk's Conjecture (`arXiv:2210.14762v2`, Conjecture 1)

## Refuted Conjecture
Conjecture 1 of Anthony V. Petyuk (*"On word-representability of simplified de Bruijn graphs"*, `arXiv:2210.14762v2`, Section 4, line 123) asserts:
> $S(n,k)$ is non-word-rerpesentable for $n\geq 4$ and $k\geq 3$.

## Counterexample: $S(4, 3)$ is $3$-colorable and word-representable
We prove that the simplified de Bruijn graph $S(4, 3)$ (on $3^4 = 81$ vertices and $237$ edges) is **$3$-colorable**, and therefore **word-representable** both by Theorem 2 of Petyuk's own paper (Halldórsson–Kitaev–Pyatkin 2016: every $3$-colorable graph is word-representable) and via an explicit representing word $w$ constructed directly from the $3$-coloring.

---

### 1. Explicit Proper $3$-Coloring of $S(4, 3)$

Identify the alphabet $A = \{0, 1, 2\}$ with $\mathbb{Z}_3 = \mathbb{Z}/3\mathbb{Z}$. For each vertex $x = (x_1, x_2, x_3, x_4) \in \mathbb{Z}_3^4$, define first differences
$$d_1 := x_2 - x_1,\qquad d_2 := x_3 - x_2,\qquad d_3 := x_4 - x_3 \pmod 3,$$
and set
$$c(x_1, x_2, x_3, x_4) := \bigl(x_1 + f(d_1, d_2, d_3)\bigr) \bmod 3,$$
where $f: \mathbb{Z}_3^3 \to \{0, 1, 2\}$ is given explicitly by the $9$-row table:

| $(d_1, d_2)$ | $f(d_1, d_2, 0)$ | $f(d_1, d_2, 1)$ | $f(d_1, d_2, 2)$ |
| :---: | :---: | :---: | :---: |
| $(0, 0)$ | $1$ | $2$ | $2$ |
| $(0, 1)$ | $0$ | $0$ | $0$ |
| $(0, 2)$ | $1$ | $1$ | $1$ |
| $(1, 0)$ | $1$ | $2$ | $1$ |
| $(1, 1)$ | $1$ | $1$ | $1$ |
| $(1, 2)$ | $2$ | $1$ | $2$ |
| $(2, 0)$ | $2$ | $0$ | $2$ |
| $(2, 1)$ | $2$ | $2$ | $2$ |
| $(2, 2)$ | $0$ | $2$ | $0$ |

**Proof that $c$ is a proper $3$-coloring of $S(4, 3)$:**
Every edge of $S(4, 3)$ arises from a directed non-loop transition
$$x = (x_1, x_2, x_3, x_4) \longrightarrow y = (x_2, x_3, x_4, x_5)$$
in $B(4, 3)$ with $x \ne y$. Letting $d_4 := (x_5 - x_4) \bmod 3$, the condition $x \ne y$ is equivalent to $(d_1, d_2, d_3, d_4) \ne (0, 0, 0, 0)$ (if $d_1 = d_2 = d_3 = d_4 = 0$, then $x_1 = x_2 = x_3 = x_4 = x_5$, a loop). Since $x_2 \equiv x_1 + d_1 \pmod 3$, we have
$$c(y) - c(x) \equiv d_1 + f(d_2, d_3, d_4) - f(d_1, d_2, d_3) \pmod 3.$$
Thus $c(x) \ne c(y)$ holds for all $237$ edges of $S(4, 3)$ if and only if $f(d_1, d_2, d_3) \not\equiv d_1 + f(d_2, d_3, d_4) \pmod 3$ for all $80$ nonzero tuples $(d_1, d_2, d_3, d_4) \in \mathbb{Z}_3^4 \setminus \{0\}$:
- **$d_1 = 0$:** We require $f(0, d_2, d_3) \ne f(d_2, d_3, d_4)$ whenever $(d_2, d_3, d_4) \ne (0, 0, 0)$:
  - $d_2 = 0$: if $d_3 = 0$ ($d_4 \in \{1, 2\}$), $f(0,0,0)=1 \notin \{2\} = f(0,0,d_4)$; if $d_3 = 1$, $f(0,0,1)=2 \notin \{0\} = f(0,1,d_4)$; if $d_3 = 2$, $f(0,0,2)=2 \notin \{1\} = f(0,2,d_4)$.
  - $d_2 = 1$: $f(0,1,d_3)=0$, while $f(1,d_3,d_4) \in \{1, 2\}$ for all $d_3, d_4$.
  - $d_2 = 2$: $f(0,2,d_3)=1$, while $f(2,d_3,d_4) \in \{0, 2\}$ for all $d_3, d_4$.
- **$d_1 = 1$:** We require $f(1, d_2, d_3) \not\equiv 1 + f(d_2, d_3, d_4) \pmod 3$:
  - $d_2 = 0$: $f(1,0,0)=1$, whereas $1+f(0,0,d_4) \in \{2, 0\}$; $f(1,0,1)=2$, whereas $1+f(0,1,d_4)=1$; $f(1,0,2)=1$, whereas $1+f(0,2,d_4)=2$.
  - $d_2 = 1$: $f(1,1,d_3)=1$, whereas $1+f(1,d_3,d_4) \in \{2, 0\}$.
  - $d_2 = 2$: $f(1,2,0)=2$, whereas $1+f(2,0,d_4) \in \{0, 1\}$; $f(1,2,1)=1$, whereas $1+f(2,1,d_4)=0$; $f(1,2,2)=2$, whereas $1+f(2,2,d_4) \in \{1, 0\}$.
- **$d_1 = 2$:** We require $f(2, d_2, d_3) \not\equiv 2 + f(d_2, d_3, d_4) \pmod 3$:
  - $d_2 = 0$: $f(2,0,0)=2$, whereas $2+f(0,0,d_4) \in \{0, 1\}$; $f(2,0,1)=0$, whereas $2+f(0,1,d_4)=2$; $f(2,0,2)=2$, whereas $2+f(0,2,d_4)=0$.
  - $d_2 = 1$: $f(2,1,d_3)=2$, whereas $2+f(1,d_3,d_4) \in \{0, 1\}$.
  - $d_2 = 2$: $f(2,2,0)=0$, whereas $2+f(2,0,d_4) \in \{1, 2\}$; $f(2,2,1)=2$, whereas $2+f(2,1,d_4)=1$; $f(2,2,2)=0$, whereas $2+f(2,2,d_4) \in \{2, 1\}$.

Hence $c$ is a proper $3$-coloring of $S(4, 3)$. (Note also that $S(4, 3)$ contains triangles such as `0010–0100–1001`, so $\chi(S(4, 3)) = 3$.)

---

### 2. Self-Contained Explicit Representing Word for $S(4, 3)$

Let $A_i = c^{-1}(i)$ ($i = 0, 1, 2$) be the three color classes, ordered arbitrarily, with $|A_0| = |A_1| = |A_2| = 27$ (since $c$ is $\mathbb{Z}_3$-shift-equivariant). For any ordered bipartition $(X, Y)$ of color classes, define the sequence of permutations of $X \cup Y$:
- $P_0(X, Y)$: $X$ (or $\mathrm{rev}(X)$) followed by $Y$ (or $\mathrm{rev}(Y)$),
- for each $y \in Y$ having at least one non-neighbor in $X$, $P_y(X, Y) := N_X(y) \cdot y \cdot (X \setminus N_X(y)) \cdot (Y \setminus \{y\})$, where $N_X(y) = \{x \in X : xy \in E(S(4,3))\}$.

Construct three permutation lists:
- $(P_t^{(01)})_{t \ge 1}$ for $(A_0, A_1)$ starting with $A_0 \cdot A_1$,
- $(P_t^{(20)})_{t \ge 1}$ for $(A_2, A_0)$ starting with $A_2 \cdot \mathrm{rev}(A_0)$,
- $(P_t^{(12)})_{t \ge 1}$ for $(A_1, A_2)$ starting with $\mathrm{rev}(A_1) \cdot \mathrm{rev}(A_2)$.

Pad the lists with their first permutation to common length $M = 28$ (in fact each $y$ has non-neighbors so $M = 28$), and concatenate in cyclic rounds:
$$w := \prod_{t=1}^{28} \Bigl( P_t^{(01)} \, P_t^{(20)} \, P_t^{(12)} \Bigr)$$
(a word of length $28 \times 3 \times 54 = 4536$ over $V(S(4, 3))$).

**Proof that $w$ represents $S(4, 3)$:**
- For $u \ne v$ in the same class $A_i$: they appear in opposite relative orders in the first round's two blocks containing $A_i$ (e.g. $A_0$ vs $\mathrm{rev}(A_0)$ in $P_1^{(01)}$ and $P_1^{(20)}$), creating an immediate $u \cdots v \cdots v \cdots u$ pattern, so they do not alternate.
- For $(a, b) \in A_0 \times A_1$: in every round $t$, $a$ appears in $P_t^{(01)}$ and $P_t^{(20)}$, while $b$ appears in $P_t^{(01)}$ and $P_t^{(12)}$. If $ab \in E$, then $a$ precedes $b$ in every $P_t^{(01)}$, so round $t$ restricts to $abab$, and concatenating all rounds gives $(ab)^{28}$ (alternating). If $ab \notin E$, then $b$ precedes $a$ in $P_b^{(01)}$, creating $baab$ within that round (non-alternating).
- Symmetrically, for $(b, c) \in A_1 \times A_2$, each round restricts to $bcbc$ if $bc \in E$ (giving $(bc)^{28}$) and contains $bccb$ if $bc \notin E$; for $(c, a) \in A_2 \times A_0$, each round restricts to $acac$ if $ca \in E$ (giving $(ac)^{28}$) and contains $aacc$ if $ca \notin E$.

Thus two vertices alternate in $w$ if and only if they are adjacent in $S(4, 3)$, proving directly from the definition that $S(4, 3)$ is word-representable and refuting Petyuk's Conjecture 1. $\square$

*(Remark: Computational SAT checks in `notes/` also show $S(5, 3)$ is $3$-colorable, whereas $S(4, 4)$ is not $3$-colorable.)*

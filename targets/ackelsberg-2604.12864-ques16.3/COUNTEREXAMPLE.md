# Counterexample to Ackelsberg--Richter (2026), Question 16.3

**Verdict: FALSE.** The answer to Question 16.3 (*Finitary form of Kneser's theorem*) in `arXiv:2604.12864v1` is **NO**.

*(Remark on trivial boundary case: literally as written, Question 16.3 also omits the condition $\alpha + \beta \leq 1$, which trivially falsifies $|(A+B)\cap[N]|/N \geq \alpha + \beta - \varepsilon$ whenever $\alpha + \beta > 1 + \varepsilon$, e.g. $A=B=[N]$ with $\alpha=\beta=1$ and $\varepsilon = 1/2$. Below we show that Question 16.3 is **still false** even under the intended stronger restriction $\alpha + \beta < 1$ and $\alpha = \beta = 1/2$.)*

## Counterexample Construction

Take $\varepsilon = \frac{1}{10}$ and any $N_0 \in \mathbb{N}$ (for instance $N_0 = 1$). Let $D = D(\varepsilon, N_0) > 0$ (with $D \in \mathbb{N}$ so residue classes modulo $D$ are defined; more generally replace $D$ by $D_0 = \lceil D \rceil \in \mathbb{N}$) and $N_1 = N_1(\varepsilon, N_0) \in \mathbb{N}$ be arbitrary.

Set
\[
\alpha = \beta = \frac{4}{9} \quad \Big(\text{so } \alpha, \beta > 0 \text{ and } \alpha + \beta = \frac{8}{9} < 1; \text{ indeed } \alpha = \beta = \frac{1}{2} \text{ also works}\Big),
\]
and choose
\[
N = \max(N_1,\; N_0 + 1,\; 10 D) \geq N_1.
\]
Define $A, B \subset [N] = \{1, 2, \ldots, N\}$ by
\[
A = (2\mathbb{N} - 1) \cap [N] = \{1, 3, 5, \ldots\} \cap [N],
\]
\[
B = A \cup \{N - D + 1,\; N - D + 2,\; \ldots,\; N\}.
\]

## Verification of All Hypotheses

1. **Subset inclusion and non-empty index range.** Since $N \geq 10D > D$, we have $N - D + 1 \geq 1$, so $A \subseteq B \subseteq [N]$. Since $N \geq N_0 + 1$, the index range $\{n \in \mathbb{N} : N_0 < n \leq N\}$ is non-empty.
2. **Uniform prefix lower density bounds.** For every integer $n \in [N]$, the set $A \cap [n] = \{1, 3, \ldots\} \cap [n]$ has cardinality
   \[
   |A \cap [n]| = \left\lceil \frac{n}{2} \right\rceil \geq \frac{n}{2}.
   \]
   Since $A \subseteq B$, it follows that for every $n$ with $N_0 < n \leq N$,
   \[
   \frac{|A \cap [n]|}{n} \geq \frac{1}{2} > \frac{4}{9} = \alpha, \qquad
   \frac{|B \cap [n]|}{n} \geq \frac{|A \cap [n]|}{n} \geq \frac{1}{2} > \frac{4}{9} = \beta.
   \]
3. **Every residue class modulo $D$ is intersected by $B$.** Because $B$ contains the $D$ consecutive integers $\{N - D + 1, N - D + 2, \ldots, N\}$, $B$ meets every residue class modulo $D$.

## Failure of the Sumset Lower Bound

Let $x \in (A + B) \cap [N]$, so $x = a + b \leq N$ with $a \in A$ and $b \in B$:
- Every $a \in A$ is odd and satisfies $a \geq 1$.
- If $b \in B$ is odd (i.e. $b \in A$), then $x = a + b$ is **even**, so $x \in 2\mathbb{N} \cap [N]$.
- If $b \in B$ is **even**, then $b \notin A$, so necessarily $b \in \{N - D + 1, \ldots, N\}$, and since $a \geq 1$, we have
  \[
  x = a + b \geq 1 + (N - D + 1) = N - D + 2.
  \]
  In this case $x = a + b$ is odd and belongs to $\{N - D + 2, \ldots, N\}$.

Consequently,
\[
(A + B) \cap [N] \;\subseteq\; (2\mathbb{N} \cap [N]) \;\cup\; \big((2\mathbb{N} - 1) \cap \{N - D + 2, \ldots, N\}\big).
\]
Now $|2\mathbb{N} \cap [N]| = \lfloor N/2 \rfloor \leq N/2$, and an interval of length $\max(D - 1, 0)$ contains at most $\lceil (D-1)/2 \rceil \leq D/2$ odd integers (indeed $\lceil (D-1)/2 \rceil = \lfloor D/2 \rfloor \leq D/2$ for every integer $D \geq 1$). Hence
\[
|(A + B) \cap [N]| \leq \frac{N}{2} + \frac{D}{2},
\]
and since $N \geq 10D$,
\[
\frac{|(A + B) \cap [N]|}{N} \leq \frac{1}{2} + \frac{D}{2N} \leq \frac{1}{2} + \frac{1}{20} = \frac{11}{20} = 0.55.
\]
On the other hand,
\[
\alpha + \beta - \varepsilon = \frac{4}{9} + \frac{4}{9} - \frac{1}{10} = \frac{71}{90} \approx 0.7889 > \frac{11}{20} \geq \frac{|(A + B) \cap [N]|}{N}
\]
(and with $\alpha = \beta = \frac{1}{2}$, $\alpha + \beta - \varepsilon = \frac{9}{10} = 0.9 > \frac{11}{20}$).

Thus no choice of $(D, N_1)$ works for $\varepsilon = 1/10$ and any $N_0 \in \mathbb{N}$ (indeed the same construction refutes Question 16.3 for every $0 < \varepsilon < 1/2$ and every $N_0 \in \mathbb{N}$ by taking $\alpha = \beta = \frac{1}{2} - \eta$ with $0 < \eta < \frac{1/2 - \varepsilon}{2}$, replacing $D$ by $D_0 = \lceil D \rceil$ if needed, and setting $N \geq \max\bigl(N_1, N_0+1, \lceil D_0 / (\frac{1}{2} - \varepsilon - 2\eta) \rceil\bigr)$, since then $\frac{D_0}{2N} \leq \frac{1/2 - \varepsilon - 2\eta}{2} < \frac{1}{2} - \varepsilon - 2\eta$, so $\frac{1}{2} + \frac{D_0}{2N} < 1 - 2\eta - \varepsilon = \alpha + \beta - \varepsilon$).

## Mechanism of Failure

In the infinite setting on $\mathbb{N}$ (Kneser's theorem), $B$ meeting every residue class mod $D$ yields finitely many fixed representatives $b_0, \ldots, b_{D-1} \in B$, so for $N \gg \max_r b_r$ the translates $A + b_r$ mostly remain inside $[N]$. In the finitary statement of Question 16.3 on $[N]$, placing the even residue-class representatives of $B$ inside the boundary strip $(N - D, N]$ satisfies both the prefix density hypothesis and the residue-class hypothesis, while overflowing $[N]$ upon addition by all $a \in A$ except $a < D$.

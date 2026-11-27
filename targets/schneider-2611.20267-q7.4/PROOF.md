# Answer to Question 7.4 (`arXiv:2611.20267v1`, Section 7)

**Answer:** **YES.** For every integer $J \ge 2$, the graph $\mathcal{G}_{\bar{e}_1}(J)\restriction X_{\bar{e}_1}(J)$ admits a continuous $(J+2)$-coloring, and hence (via the self-contained 1-dimensional color-reduction construction in Step 2 below, following `[KST, 5.2]`) a continuous **$3$-coloring**. Since $\chi_B(\mathcal{G}_{\bar{e}_1}(J)\restriction X_{\bar{e}_1}(J)) = 3$ by Proposition 7.3 (`prop:ColoringGe1`), we in fact have $\chi_C(\mathcal{G}_{\bar{e}_1}(J)\restriction X_{\bar{e}_1}(J)) = 3$.

---

## Proof

Fix an integer $J \ge 2$, and write $X := X_{\bar{e}_1}(J) \subseteq J^{\omega^2}$ with the subspace topology from the product topology on $J^{\omega^2}$, where $J = \{0, \dots, J-1\}$ is discrete. For $x \in X$, $\bar{e}_1 \cdot x$ is defined by $(\bar{e}_1 \cdot x)(i, j) = x(i+1, j)$ for all $i, j \in \omega$.

First observe that $X$ is $\bar{e}_1$-forward-invariant: if $x \in X$, then $\bar{e}_1 \cdot x \notin \mathrm{Per}_{\bar{e}_1}(J^{\omega^2})$ (by `Claim \ref{claim:PerInvar}` since $x \mathrel{E_2^J} \bar{e}_1 \cdot x$, or directly because $\bar{a}\cdot(\bar{e}_1\cdot x) = \bar{b}\cdot(\bar{e}_1\cdot x)$ for $\bar{a}, \bar{b} \in \mathbb{N}^2$ with $\bar{a} - \bar{b} = \bar{e}_1$ implies $(\bar{a}+\bar{e}_1)\cdot x = (\bar{b}+\bar{e}_1)\cdot x$ with $(\bar{a}+\bar{e}_1) - (\bar{b}+\bar{e}_1) = \bar{e}_1$), and for each $j \in \omega$, $\langle x(i+1, j) \mid i \in \omega\rangle$ is not eventually constant iff $\langle x(i, j) \mid i \in \omega\rangle$ is not eventually constant. Moreover, $\bar{e}_1 \cdot x \ne x$ for every $x \in X$ since $X \subseteq \neg\mathrm{Per}_{\bar{e}_1}(J^{\omega^2})$ (take $\bar{a} = \bar{e}_1$, $\bar{b} = \bar{0}$). By definition of $\mathcal{G}_{\bar{e}_1}(J)$ as the symmetrization of $\vec{\mathcal{G}}_{\bar{e}_1}(J)$ (`5-BorelGraphColoringsAndRegularMarkerSets-CLEAN.tex` L10–13 and `2-Preliminaries-CLEAN.tex` L67), a function $c : X \to Z$ is a coloring of $\mathcal{G}_{\bar{e}_1}(J)\restriction X$ if and only if $c(x) \ne c(\bar{e}_1 \cdot x)$ for all $x \in X$.

### Step 1: Continuous map $H : X \to (J+1)^\omega$ avoiding constant orbits

Let $\mathbb{N}_+ = \{1, 2, \dots\}$ and $\mathbb{N} = \omega = \{0, 1, 2, \dots\}$. Define a strict total order $\prec$ on $\mathbb{N}_+ \times \mathbb{N}$ by
\[
(i', j') \prec (i, j) \quad :\Longleftrightarrow \quad (i' + j' < i + j) \ \vee \ (i' + j' = i + j \ \wedge \ j' < j).
\]
Since $\{ (i, j) \in \mathbb{N}_+ \times \mathbb{N} \mid i + j \le N \}$ is finite for each $N$, $\prec$ is a well-ordering of order type $\omega$.

For every $x \in X$, infinitely many rows $\langle x(i, j) \mid i \in \omega\rangle$ are not eventually constant, so in particular there exists at least one pair $(i, j) \in \mathbb{N}_+ \times \mathbb{N}$ with $x(i, j) \ne x(0, j)$. Let $(i(x), j(x))$ denote the $\prec$-least pair $(i, j) \in \mathbb{N}_+ \times \mathbb{N}$ such that $x(i, j) \ne x(0, j)$. Define $h : X \to \{0, 1, \dots, J\} = J+1$ by
\[
h(x) := \begin{cases}
x(0, j(x)) & \text{if } i(x) \text{ is odd}, \\
J & \text{if } i(x) \text{ is even}.
\end{cases}
\]

**Continuity of $h$.** Let $x \in X$ and put $N := i(x) + j(x) + 1$. For every $(i', j') \in \mathbb{N}_+ \times \mathbb{N}$ with $(i', j') \preceq (i(x), j(x))$, we have $i' + j' \le i(x) + j(x) < N$, so both $(i', j')$ and $(0, j')$ lie in $\mathcal{R}_2(\dot{N}) = \{0, \dots, N-1\}^2$. Hence for every $y \in [x \restriction N] \cap X$, we have $(i(y), j(y)) = (i(x), j(x))$ and $y(0, j(x)) = x(0, j(x))$, so $h(y) = h(x)$. Thus $h$ is continuous into the discrete space $J+1$.

Now define $H : X \to (J+1)^\omega$ by
\[
H(x)(k) := h(k\bar{e}_1 \cdot x) \qquad (k \in \omega).
\]
Since $x \mapsto k\bar{e}_1 \cdot x$ is continuous on $J^{\omega^2}$ (Claim 2.3.1(i) / `claim:NiceAction(i)`) and preserves $X$, each coordinate map $x \mapsto H(x)(k)$ is continuous on $X$. Hence $H$ is continuous into the product space $(J+1)^\omega$. Moreover, $H(\bar{e}_1 \cdot x) = 1 \cdot H(x)$ for all $x \in X$, where $1 \cdot u$ denotes the left shift on $(J+1)^\omega$.

For any integer $M \ge 2$, write $\mathrm{Const}(M^\omega) := \{u \in M^\omega \mid \forall i \in \omega,\ u(i) = u(0)\}$ and $\neg\mathrm{Const}(M^\omega) := M^\omega \setminus \mathrm{Const}(M^\omega)$.

**Claim (No orbit is eventually constant under $H$).** *For every $x \in X$ and $k \in \omega$, the sequence $k \cdot H(x) = H(k\bar{e}_1 \cdot x)$ is not constant.*

*Proof of Claim.* Since $k\bar{e}_1 \cdot x \in X$, it suffices to show $H(x) \notin \mathrm{Const}((J+1)^\omega)$ for every $x \in X$. Suppose for contradiction that there exist $x \in X$ and $a \in \{0, \dots, J\}$ such that $H(x)(k) = h(x_k) = a$ for all $k \in \omega$, where $x_k := k\bar{e}_1 \cdot x$. Write $(i_k, j_k) := (i(x_k), j(x_k))$.

1. *We cannot have $i_k \ge 2$ for any $k \in \omega$.* Suppose $i_k \ge 2$. Since $1 + j_k < i_k + j_k$, we have $(1, j_k) \prec (i_k, j_k)$, so minimality of $(i_k, j_k)$ for $x_k$ yields $x_k(1, j_k) = x_k(0, j_k)$. Thus
   \[
   x_{k+1}(i_k - 1, j_k) = x_k(i_k, j_k) \ne x_k(0, j_k) = x_k(1, j_k) = x_{k+1}(0, j_k),
   \]
   so $(i_k - 1, j_k) \in \mathbb{N}_+ \times \mathbb{N}$ is a witness for $x_{k+1}$. We check it is $\prec$-minimal: let $(i', j') \in \mathbb{N}_+ \times \mathbb{N}$ satisfy $(i', j') \prec (i_k - 1, j_k)$. Then $i' + j' \le i_k - 1 + j_k$, and if $i' + j' = i_k - 1 + j_k$ then $j' < j_k$. Hence:
   - $1 + j' \le i' + j' < i_k + j_k$, so $(1, j') \prec (i_k, j_k)$, giving $x_k(1, j') = x_k(0, j')$;
   - either $(i'+1) + j' < i_k + j_k$, or $(i'+1) + j' = i_k + j_k$ and $j' < j_k$, so in either case $(i'+1, j') \prec (i_k, j_k)$, giving $x_k(i'+1, j') = x_k(0, j')$.

   Consequently, $x_{k+1}(i', j') = x_k(i'+1, j') = x_k(0, j') = x_k(1, j') = x_{k+1}(0, j')$, so $(i', j')$ is not a witness for $x_{k+1}$. Therefore $(i_{k+1}, j_{k+1}) = (i_k - 1, j_k)$ and $x_{k+1}(0, j_{k+1}) = x_k(0, j_k)$. Since $i_k$ and $i_{k+1} = i_k - 1$ have opposite parities, one of $h(x_k), h(x_{k+1})$ equals $J$ and the other lies in $\{0, \dots, J-1\}$, contradicting $h(x_k) = h(x_{k+1}) = a$.

2. *Hence $i_k = 1$ for all $k \in \omega$, and $j_0 < j_1 < j_2 < \cdots$.* By (1), $i_k = 1$ for every $k \in \omega$, so $a = h(x_k) = x_k(0, j_k) \in \{0, \dots, J-1\}$. Fix $k \in \omega$:
   - If $j_{k+1} = j_k$, then $a = h(x_{k+1}) = x_{k+1}(0, j_k) = x_k(1, j_k) \ne x_k(0, j_k) = h(x_k) = a$ (since $(1, j_k)$ is a witness for $x_k$), a contradiction.
   - If $j_{k+1} < j_k$, then $1 + j_{k+1} < 1 + j_k$ and $2 + j_{k+1} \le 1 + j_k$ with $j_{k+1} < j_k$, so both $(1, j_{k+1}) \prec (1, j_k)$ and $(2, j_{k+1}) \prec (1, j_k)$. Minimality of $(1, j_k)$ for $x_k$ yields $x_k(2, j_{k+1}) = x_k(0, j_{k+1}) = x_k(1, j_{k+1})$, whence $x_{k+1}(1, j_{k+1}) = x_{k+1}(0, j_{k+1})$, contradicting that $(1, j_{k+1})$ is a witness for $x_{k+1}$.

   Therefore $j_{k+1} > j_k$ for all $k \in \omega$.

3. *Every row of $x$ is eventually constant.* Fix any row $r \in \omega$. Since $(j_k)_{k \in \omega}$ is strictly increasing, there exists $K_r \in \omega$ such that $j_k > r$ for all $k \ge K_r$. For every $k \ge K_r$, we have $(1, r) \prec (1, j_k)$, so minimality of $(1, j_k)$ for $x_k$ gives $x(k+1, r) = x_k(1, r) = x_k(0, r) = x(k, r)$. Thus row $r$ of $x$ is constant from index $K_r$ onward. As $r \in \omega$ was arbitrary, every row of $x$ is eventually constant, contradicting $x \in X$. $\square$

---

### Step 2: Continuous $(J+2)$-coloring and continuous $3$-coloring of $\mathcal{G}_{\bar{e}_1}(J)\restriction X$

Let $N_{\mathrm{nec}}(M^\omega) := \{ u \in M^\omega \mid (\forall k \in \omega)\, k \cdot u \notin \mathrm{Const}(M^\omega) \}$ denote the set of non-eventually-constant sequences in $M^\omega$, for any integer $M \ge 2$. By the Claim above, $H[X] \subseteq N_{\mathrm{nec}}((J+1)^\omega)$.

For any $M \ge 2$, define $\gamma_M : \neg\mathrm{Const}(M^\omega) \to M + 1 = \{0, \dots, M\}$ by
\[
\gamma_M(u) := \begin{cases}
u(0) & \text{if the least } i \ge 1 \text{ with } u(i) \ne u(0) \text{ is odd}, \\
M & \text{if the least } i \ge 1 \text{ with } u(i) \ne u(0) \text{ is even}.
\end{cases}
\]
Clearly $\gamma_M$ is continuous on $\neg\mathrm{Const}(M^\omega)$: if $i_0$ is the least index with $u(i_0) \ne u(0)$, then $\gamma_M$ is constant on $[u \restriction (i_0+1)] \cap \neg\mathrm{Const}(M^\omega)$. Moreover, whenever both $u$ and $1 \cdot u$ belong to $\neg\mathrm{Const}(M^\omega)$ (in particular, for all $u \in N_{\mathrm{nec}}(M^\omega)$):
- If $i_0 \ge 2$, then $(1 \cdot u)(0) = u(1) = u(0)$ and the least $i \ge 1$ with $(1 \cdot u)(i) \ne (1 \cdot u)(0)$ is $i_0 - 1$, which has opposite parity to $i_0$, so $\{\gamma_M(u), \gamma_M(1 \cdot u)\} = \{u(0), M\}$ with $u(0) < M$.
- If $i_0 = 1$, then $\gamma_M(u) = u(0) < M$, whereas $\gamma_M(1 \cdot u) \in \{u(1), M\}$ and $u(1) \ne u(0)$, so $\gamma_M(1 \cdot u) \ne u(0) = \gamma_M(u)$.

In particular, $\gamma_{J+1} \circ H : X \to \{0, \dots, J+1\}$ is already a **continuous $(J+2)$-coloring** of $\mathcal{G}_{\bar{e}_1}(J)\restriction X$.

To refine this to $3$ colors (following `[KST, 5.2]`; see also the commented-out TeX remark at `7-TheGraphsGe1Ge2Gp-CLEAN.tex` L112–123), let $M := J+1$ and define $f_M : N_{\mathrm{nec}}(M^\omega) \to (M+1)^\omega$ by $f_M(u)(k) := \gamma_M(k \cdot u)$, and $g_M : N_{\mathrm{nec}}(M^\omega) \to 2^\omega$ by
\[
g_M(u)(k) := \begin{cases}
0 & \text{if } f_M(u)(k) < f_M(u)(k+1), \\
1 & \text{otherwise (i.e., } f_M(u)(k) > f_M(u)(k+1)\text{)}.
\end{cases}
\]
Both $f_M$ and $g_M$ are continuous and shift-equivariant ($g_M(1 \cdot u) = 1 \cdot g_M(u)$). Because $f_M(u)(k) \ne f_M(u)(k+1)$ for all $k \in \omega$, $f_M(u)$ takes values in the finite set $\{0, \dots, M\}$, so $f_M(u)$ can neither strictly increase nor strictly decrease from any $k_0$ onward; hence $g_M(u) \in N_{\mathrm{nec}}(2^\omega)$ for all $u \in N_{\mathrm{nec}}(M^\omega)$.

Finally, set
\[
c := \gamma_2 \circ g_{J+1} \circ H : X \to \{0, 1, 2\}.
\]
Then $c$ is continuous, and for every $x \in X$, writing $v := g_{J+1}(H(x)) \in N_{\mathrm{nec}}(2^\omega)$, we have $g_{J+1}(H(\bar{e}_1 \cdot x)) = 1 \cdot v \in N_{\mathrm{nec}}(2^\omega)$, so
\[
c(\bar{e}_1 \cdot x) = \gamma_2(1 \cdot v) \ne \gamma_2(v) = c(x).
\]
Thus $c$ is a continuous $3$-coloring of $\mathcal{G}_{\bar{e}_1}(J)\restriction X_{\bar{e}_1}(J)$, answering Question 7.4 in the affirmative. $\blacksquare$

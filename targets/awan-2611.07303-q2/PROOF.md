# Proof — Convergence, Limit Formula, and Non-Monotonicity for `q:rate` (`arXiv:2611.07303v2`, Question 2)

Let $k \ge 3$ and $h \ge 2$ be fixed integers, and for $q \ge k$ put
\[
f_{h,k}(q) := q\left(1 - \frac{|\mathcal{B}_{h,k}(q)|}{\binom{q}{k}}\right),
\]
where $\mathcal{B}_{h,k}(q) = \bigl\{A \in \binom{[q]}{k} : |hA| = M_{h,k}\bigr\}$. For each $\mathbf{d} \in \mathcal{R}_{h,k}$, let
\[
P_{\mathbf{d}} := \bigl\{\mathbf{v} \in \mathbb{R}^k : 0 < v_1 < v_2 < \cdots < v_k < 1,\ \mathbf{d} \cdot \mathbf{v} = 0\bigr\},
\]
and write $\operatorname{vol}_{k-1}(P_{\mathbf{d}})$ for its $(k-1)$-dimensional Euclidean volume inside the hyperplane $\mathbf{d}^\perp := \{\mathbf{v} \in \mathbb{R}^k : \mathbf{d}\cdot\mathbf{v}=0\}$, and $\|\mathbf{d}\|_2 := \bigl(\sum_{i=1}^k d_i^2\bigr)^{1/2}$.

---

## Summary of Answers to Question 2 (`\label{q:rate}`)

1. **Convergence for every $k \ge 4$ (and $k = 3$):** **Yes.** For every fixed $h \ge 2$ and $k \ge 3$, the limit $c_{h,k} := \lim_{q\to\infty} f_{h,k}(q)$ exists.
2. **Formula for $c_{h,k}$ via normalized $(k-1)$-dimensional volumes:** **Yes.** In general,
   \[
   c_{h,k} \;=\; k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2}
   \;=\; k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}\bigl(\pi_m(P_{\mathbf{d}})\bigr)}{|d_m|},
   \]
   where $\pi_m : \mathbb{R}^k \to \mathbb{R}^{k-1}$ omits any coordinate $m \in \{1,\dots,k\}$ with $d_m \neq 0$, and the normalization $\|\mathbf{d}\|_2$ is the covolume of the integer sublattice $\mathbb{Z}^k \cap \mathbf{d}^\perp$ inside $\mathbf{d}^\perp$. This recovers $c_{h,3} = 3\sum_{w=2}^h \varphi(w)/w$ (Remark 5.2) and $c_{2,4} = 8$ term by term.
3. **Eventual monotonicity in $q$:** **No.** Neither for $k=3$ nor for $k \ge 4$ is $f_{h,k}(q)$ eventually monotone in $q$ in general:
   - For $(h,k) = (3,3)$, $f_{3,3}(6m+1) - f_{3,3}(6m) > 0$ while $f_{3,3}(6m+2) - f_{3,3}(6m+1) < 0$ for every $m \ge 1$.
   - For $(h,k) = (2,4)$ (the smallest case with $k \ge 4$), $f_{2,4}(q+1) - f_{2,4}(q) > 0$ for every even $q \ge 6$ and $f_{2,4}(q+1) - f_{2,4}(q) < 0$ for every odd $q \ge 71$, so $f_{2,4}(q)$ strictly alternates direction at every step for all $q \ge 70$.

---

## 1. Proof of Convergence and the Normalized Volume Formula

Fix $h \ge 2$ and $k \ge 3$. By Lemma 3.2 (`lem:equal-sum-criterion`),
\[
\binom{[q]}{k} \setminus \mathcal{B}_{h,k}(q) = \bigcup_{\mathbf{d} \in \mathcal{R}_{h,k}} E_{\mathbf{d}}(q),
\qquad
E_{\mathbf{d}}(q) := \bigl\{A \in \binom{[q]}{k} : \mathbf{d} \cdot \vec{A} = 0\bigr\}.
\]
By Proposition 3.5 (`prop:coefficient-vectors-lemma`), $\mathcal{R}_{h,k}$ is finite ($|\mathcal{R}_{h,k}| \le (2h+1)^{k-1}$) and any two distinct vectors $\mathbf{d}, \mathbf{e} \in \mathcal{R}_{h,k}$ are linearly independent. Applying Bonferroni's inequalities together with Lemma 3.4 (`lem:rank-lemma`) to each pair $\{\mathbf{d}, \mathbf{e}\} \in \binom{\mathcal{R}_{h,k}}{2}$ yields
\begin{equation}\label{eq:bonf}
\sum_{\mathbf{d} \in \mathcal{R}_{h,k}} |E_{\mathbf{d}}(q)| - \binom{|\mathcal{R}_{h,k}|}{2} q^{k-2}
\;\le\; \left|\binom{[q]}{k} \setminus \mathcal{B}_{h,k}(q)\right|
\;\le\; \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} |E_{\mathbf{d}}(q)|.
\end{equation}

We now show that for every $\mathbf{d} \in \mathcal{R}_{h,k}$,
\begin{equation}\label{eq:single-d-asymp}
|E_{\mathbf{d}}(q)| = \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2}\, q^{k-1} + O_{\mathbf{d}}(q^{k-2}).
\end{equation}

**Case 1: $w(\mathbf{d}) = 1$.** Since $\sum_{i=1}^k d_i = 0$ and $\gcd(|d_1|, \dots, |d_k|) = 1$, $\mathbf{d}$ has one entry $1$, one entry $-1$, and all other entries $0$, say $\mathbf{d} = \mathbf{e}_i - \mathbf{e}_j$ ($i < j$). Then $\mathbf{d} \cdot \mathbf{v} = v_i - v_j = 0$ is impossible both for $1 \le a_1 < \dots < a_k \le q$ and for $0 < v_1 < \dots < v_k < 1$, so $E_{\mathbf{d}}(q) = \varnothing$, $P_{\mathbf{d}} = \varnothing$, and \eqref{eq:single-d-asymp} holds with both sides equal to $0$.

**Case 2: $w(\mathbf{d}) \ge 2$.** Set $\Lambda_{\mathbf{d}} := \mathbb{Z}^k \cap \mathbf{d}^\perp$. Since $\gcd(|d_1|, \dots, |d_k|) = 1$, there exists $\mathbf{u} \in \mathbb{Z}^k$ with $\mathbf{d} \cdot \mathbf{u} = 1$, so every $\mathbf{z} \in \mathbb{Z}^k$ decomposes uniquely as $\mathbf{z} = \bigl(\mathbf{z} - (\mathbf{d}\cdot\mathbf{z})\mathbf{u}\bigr) + (\mathbf{d}\cdot\mathbf{z})\mathbf{u}$ with first summand in $\Lambda_{\mathbf{d}}$. Choosing a $\mathbb{Z}$-basis $\mathbf{b}_1, \dots, \mathbf{b}_{k-1}$ of the free abelian group $\Lambda_{\mathbf{d}} \cong \mathbb{Z}^{k-1}$, the $k$ vectors $(\mathbf{b}_1, \dots, \mathbf{b}_{k-1}, \mathbf{u})$ form a $\mathbb{Z}$-basis of $\mathbb{Z}^k$, so the integer matrix $M = [\mathbf{b}_1 \mid \dots \mid \mathbf{b}_{k-1} \mid \mathbf{u}]$ satisfies $|\det M| = 1$.

Let $T : \mathbb{R}^{k-1} \to \mathbf{d}^\perp$ be the linear isomorphism $T(\mathbf{t}) = \sum_{r=1}^{k-1} t_r \mathbf{b}_r$, so $T(\mathbb{Z}^{k-1}) = \Lambda_{\mathbf{d}}$. The $k$-dimensional parallelotope spanned by $\mathbf{b}_1, \dots, \mathbf{b}_{k-1}, \mathbf{u}$ has volume $|\det M| = 1$, which also equals the $(k-1)$-dimensional Euclidean volume of $T([0,1]^{k-1})$ in $\mathbf{d}^\perp$ multiplied by the orthogonal distance from $\mathbf{u}$ to $\mathbf{d}^\perp$, namely $|\mathbf{d} \cdot \mathbf{u}| / \|\mathbf{d}\|_2 = 1/\|\mathbf{d}\|_2$. Therefore
\begin{equation}\label{eq:covol}
\operatorname{covol}(\Lambda_{\mathbf{d}}) = \operatorname{vol}_{k-1}\bigl(T([0,1]^{k-1})\bigr) = \|\mathbf{d}\|_2,
\qquad
\operatorname{vol}_{k-1}(T(S)) = \|\mathbf{d}\|_2 \operatorname{vol}_{k-1}(S)
\end{equation}
for every measurable subset $S \subseteq \mathbb{R}^{k-1}$.

Let $K_{\mathbf{d}} := \{\mathbf{v} \in \mathbb{R}^k : 0 \le v_1 \le v_2 \le \cdots \le v_k \le 1,\ \mathbf{d}\cdot\mathbf{v} = 0\}$ and $Q_{\mathbf{d}} := T^{-1}(K_{\mathbf{d}}) \subset \mathbb{R}^{k-1}$. Observe:
- Because $\sum_{i=1}^k d_i = 0$ and $w(\mathbf{d}) \ge 2$, $\mathbf{d}$ is not proportional to $\mathbf{e}_1$, $\mathbf{e}_k$, or $\mathbf{e}_i - \mathbf{e}_{i+1}$ ($1 \le i \le k-1$). Hence none of the $k+1$ linear functionals $v_1$, $v_{i+1}-v_i$, $v_k$ is constant on $\mathbf{d}^\perp$. In particular, $K_{\mathbf{d}} \setminus P_{\mathbf{d}}$ lies in a union of $k+1$ proper affine hyperplanes of $\mathbf{d}^\perp$, so $\operatorname{vol}_{k-1}(K_{\mathbf{d}}) = \operatorname{vol}_{k-1}(P_{\mathbf{d}})$, and by \eqref{eq:covol},
  \[
  \operatorname{vol}_{k-1}(Q_{\mathbf{d}}) = \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2}.
  \]
- Moreover, identifying $A \in E_{\mathbf{d}}(q)$ with $\vec{A}$, we have $E_{\mathbf{d}}(q) \subseteq \Lambda_{\mathbf{d}} \cap q K_{\mathbf{d}}$, and every $\mathbf{a} \in (\Lambda_{\mathbf{d}} \cap q K_{\mathbf{d}}) \setminus E_{\mathbf{d}}(q)$ lies in $[0, q]^k$ and satisfies $a_1 = 0$ or $a_i = a_{i+1}$ for some $1 \le i \le k-1$ (note $a_k = q$ is allowed in $E_{\mathbf{d}}(q)$). Because $\mathbf{d}$ is linearly independent from $\mathbf{e}_1$ and from $\mathbf{e}_i - \mathbf{e}_{i+1}$ ($w(\mathbf{d}) \ge 2$), the rank-$2$ argument of Lemma 3.4 (`lem:rank-lemma`) applied on $[0, q]^k$ bounds each boundary piece by $(q+1)^{k-2}$. Thus
  \begin{equation}\label{eq:boundary-int}
  |E_{\mathbf{d}}(q)| = \#(\Lambda_{\mathbf{d}} \cap q K_{\mathbf{d}}) + O_k(q^{k-2}) = \#(\mathbb{Z}^{k-1} \cap q Q_{\mathbf{d}}) + O_k(q^{k-2}).
  \end{equation}

Since $K_{\mathbf{d}} \subseteq [0, 1]^k$ is compact and $T$ is a linear isomorphism, $Q_{\mathbf{d}} \subseteq [-R, R]^{k-1}$ for some $R = R(\mathbf{d}) > 0$. Tile $\mathbb{R}^{k-1}$ by the cubes $C_{\mathbf{z}, q} := \frac{1}{q}\mathbf{z} + [0, \frac{1}{q})^{k-1}$ ($\mathbf{z} \in \mathbb{Z}^{k-1}$), each of volume $q^{-(k-1)}$. Every cube $C_{\mathbf{z},q}$ wholly contained in $Q_{\mathbf{d}}$ satisfies $\mathbf{z} \in \mathbb{Z}^{k-1} \cap q Q_{\mathbf{d}}$, and every $\mathbf{z} \in \mathbb{Z}^{k-1} \cap q Q_{\mathbf{d}}$ has $C_{\mathbf{z},q}$ either inside $Q_{\mathbf{d}}$ or intersecting $\partial Q_{\mathbf{d}}$. Hence
\[
\bigl|\#(\mathbb{Z}^{k-1} \cap q Q_{\mathbf{d}}) - \operatorname{vol}_{k-1}(Q_{\mathbf{d}})\, q^{k-1}\bigr|
\;\le\; \#\{\mathbf{z} \in \mathbb{Z}^{k-1} : C_{\mathbf{z},q} \cap \partial Q_{\mathbf{d}} \neq \varnothing\}.
\]
The boundary $\partial Q_{\mathbf{d}}$ is covered by the $k+1$ hyperplane slices $H_j \cap [-R, R]^{k-1}$ corresponding to the $k+1$ defining inequalities of $Q_{\mathbf{d}}$ (none of whose linear functionals is identically zero on $\mathbb{R}^{k-1}$). For each $H_j = \{\mathbf{t} \in \mathbb{R}^{k-1} : \mathbf{n}_j \cdot \mathbf{t} = \beta_j\}$ ($\mathbf{n}_j \neq \mathbf{0}$), pick $r$ with $(n_j)_r \neq 0$. Any cube $C_{\mathbf{z},q}$ meeting $H_j \cap [-R, R]^{k-1}$ has the remaining $k-2$ coordinates $z_i$ ($i \neq r$) in $[-Rq-1, Rq]$ (at most $(2Rq+3)^{k-2}$ choices), and once those $k-2$ coordinates are fixed in $[z_i/q, (z_i+1)/q)$, $t_r$ is confined to an interval of length $\frac{1}{q|(n_j)_r|}\sum_{i\neq r}|(n_j)_i|$, leaving at most $2 + \sum_{i\neq r} \frac{|(n_j)_i|}{|(n_j)_r|}$ values for $z_r$. Summing over $j=1, \dots, k+1$ gives $\#\{\mathbf{z} : C_{\mathbf{z},q} \cap \partial Q_{\mathbf{d}} \neq \varnothing\} = O_{\mathbf{d}}(q^{k-2})$, which with \eqref{eq:boundary-int} yields \eqref{eq:single-d-asymp}.

Combining \eqref{eq:bonf} and \eqref{eq:single-d-asymp} and dividing by $\binom{q}{k} = \frac{q^k}{k!}(1 + O_k(q^{-1}))$, we conclude that for every $h \ge 2$ and $k \ge 3$,
\[
c_{h,k} = \lim_{q\to\infty} q\left(1 - \frac{|\mathcal{B}_{h,k}(q)|}{\binom{q}{k}}\right)
= k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}(P_{\mathbf{d}})}{\|\mathbf{d}\|_2}.
\]
Furthermore, for any $m \in \{1, \dots, k\}$ with $d_m \neq 0$, the inverse of the orthogonal projection $\pi_m : \mathbf{d}^\perp \to \mathbb{R}^{k-1}$ dropping the $m$-th coordinate sends $\mathbf{x}' \in \mathbb{R}^{k-1}$ to $\mathbf{x} \in \mathbf{d}^\perp$ with $x_m = -\frac{1}{d_m}\mathbf{d}' \cdot \mathbf{x}'$ ($\mathbf{d}'$ omitting $d_m$), whose Gram matrix is $I_{k-1} + \frac{1}{d_m^2}\mathbf{d}'(\mathbf{d}')^T$ of determinant $1 + \frac{\|\mathbf{d}'\|_2^2}{d_m^2} = \frac{\|\mathbf{d}\|_2^2}{d_m^2}$. Hence $\operatorname{vol}_{k-1}(P_{\mathbf{d}}) = \frac{\|\mathbf{d}\|_2}{|d_m|}\operatorname{vol}_{k-1}(\pi_m(P_{\mathbf{d}}))$, giving the equivalent coordinate-projection formula
\[
c_{h,k} = k! \sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \frac{\operatorname{vol}_{k-1}\bigl(\pi_m(P_{\mathbf{d}})\bigr)}{|d_m|}.
\]

**Explicit sanity checks:**
- For $k=3$, any $\mathbf{d} \in \mathcal{R}_{h,3}$ with $P_{\mathbf{d}} \neq \varnothing$ has $d_1 > 0, d_2 < 0, d_3 > 0$, i.e., $\mathbf{d} = (w-u, -w, u)$ with $2 \le w \le h$, $0 < u < w$, $\gcd(u, w) = 1$ (since $d_1, d_2 > 0, d_3 < 0$ or $d_1 > 0, d_2, d_3 < 0$ cannot satisfy $\mathbf{d}\cdot\mathbf{v}=0$ on $0 < v_1 < v_2 < v_3$). Dropping $v_2$ gives $\pi_2(P_{\mathbf{d}}) = \{(v_1, v_3) : 0 < v_1 < v_3 < 1\}$ of area $1/2$, so $3! \cdot \frac{1/2}{|-w|} = \frac{3}{w}$, summing to $c_{h,3} = 3\sum_{w=2}^h \varphi(w)/w$.
- For $(h,k) = (2,4)$, the five vectors in $\mathcal{R}_{2,4}$ with $P_{\mathbf{d}} \neq \varnothing$ give:
  - $\mathbf{d} = (1, -2, 1, 0)$ (drop $v_3$): $\pi_3(P_{\mathbf{d}}) = \{0 < v_1 < v_2 < v_4 < 1,\ 2v_2 - v_1 < v_4\}$ has volume $\frac{1}{12}$, giving $24 \cdot \frac{1}{12} = 2$;
  - $\mathbf{d} = (0, 1, -2, 1)$ (drop $v_2$): symmetrically $\frac{1}{12}$, giving $2$;
  - $\mathbf{d} = (1, -2, 0, 1)$ (drop $v_4$, $|d_4|=1$): $\pi_4(P_{\mathbf{d}}) = \{0 < v_1 < v_2 < v_3 < 2v_2 - v_1 < 1\}$ has volume $\frac{1}{24}$, giving $1$;
  - $\mathbf{d} = (1, 0, -2, 1)$ (drop $v_4$, $|d_4|=1$): $\pi_4(P_{\mathbf{d}}) = \{0 < v_1 < v_2 < v_3 < 2v_3 - v_1 < 1\}$ has volume $\frac{1}{24}$, giving $1$;
  - $\mathbf{d} = (1, -1, -1, 1)$ (drop $v_4$, $|d_4|=1$): writing $u_1=v_1, u_2=v_2-v_1, u_3=v_3-v_2$, the domain is $\{u_1,u_2,u_3 > 0,\ u_1 + 2u_2 + u_3 < 1\}$, a $3$-simplex of volume $\frac{1}{6}\cdot 1 \cdot \frac{1}{2} \cdot 1 = \frac{1}{12}$, giving $2$.
  Summing gives $c_{2,4} = 2 + 2 + 1 + 1 + 2 = 8$.

---

## 2. Disproof of Eventual Monotonicity

### 2.1. Exact Counterexample for $k = 3$: $(h, k) = (3, 3)$

By Remark 5.2 (`rem:k3-limit`), $A \in \binom{[q]}{3} \setminus \mathcal{B}_{3,3}(q)$ if and only if $(a_2 - a_1)/(a_3 - a_1) = u/w$ for $(u, w) \in \{(1,2), (1,3), (2,3)\}$, which are three pairwise disjoint subsets of $\binom{[q]}{3}$. Counting $a_3 - a_1 = wt \le q-1$ and $a_1 \in [1..q-wt]$ yields, for $m_2 := \lfloor (q-1)/2 \rfloor$ and $m_3 := \lfloor (q-1)/3 \rfloor$,
\[
\left|\binom{[q]}{3} \setminus \mathcal{B}_{3,3}(q)\right|
= \sum_{t=1}^{m_2}(q - 2t) + 2\sum_{t=1}^{m_3}(q - 3t)
= m_2 q - m_2(m_2+1) + 2 m_3 q - 3 m_3(m_3+1).
\]
Evaluating on $q = 6m, 6m+1, 6m+2$ ($m \ge 1$) gives:
- $q = 6m$ ($m_2 = 3m-1$, $m_3 = 2m-1$): $|\binom{[q]}{3} \setminus \mathcal{B}_{3,3}(q)| = 21m^2 - 9m = \frac{7}{12}q^2 - \frac{3}{2}q$, so
  \[
  f_{3,3}(6m) = \frac{6m(7\cdot 6m - 18)}{2(6m-2)(6m-1)} = \frac{9m(7m-3)}{(3m-1)(6m-1)}.
  \]
- $q = 6m+1$ ($m_2 = 3m$, $m_3 = 2m$): $|\binom{[q]}{3} \setminus \mathcal{B}_{3,3}(q)| = 21m^2 - 2m = \frac{7}{12}q^2 - \frac{3}{2}q + \frac{11}{12}$, so
  \[
  f_{3,3}(6m+1) = \frac{7(6m+1) - 11}{2(6m-1)} = \frac{21m - 2}{6m - 1}.
  \]
- $q = 6m+2$ ($m_2 = 3m$, $m_3 = 2m$): $|\binom{[q]}{3} \setminus \mathcal{B}_{3,3}(q)| = 21m^2 + 5m = \frac{7}{12}q^2 - \frac{3}{2}q + \frac{2}{3}$, so
  \[
  f_{3,3}(6m+2) = \frac{7(6m+2) - 4}{2(6m+1)} = \frac{21m + 5}{6m + 1}.
  \]
Taking exact differences for every $m \ge 1$:
\[
f_{3,3}(6m+1) - f_{3,3}(6m) = \frac{2}{(3m-1)(6m-1)} > 0,
\qquad
f_{3,3}(6m+2) - f_{3,3}(6m+1) = -\frac{3}{(6m-1)(6m+1)} < 0.
\]
Hence $f_{3,3}(q)$ oscillates infinitely often and is not eventually monotone.

### 2.2. Exact Counterexample for $k = 4$: $(h, k) = (2, 4)$

For $(h, k) = (2, 4)$ and $q \ge 4$, write $D = a_4 - a_1 \in [3..q-1]$, $x = a_2 - a_1$, and $y = a_3 - a_1$. For each $D \ge 3$, there are $q - D$ choices of $a_1 \in [1..q-D]$, and $(a_1, a_2, a_3, a_4)$ fails to be a $B_2$-set if and only if $(x, y)$ with $0 < x < y < D$ lies in at least one of the five sets:
- $R_1(D): y = 2x$ ($1 \le x \le \lfloor (D-1)/2 \rfloor$), size $\lfloor (D-1)/2 \rfloor$;
- $R_2(D): 2y = x + D$ ($\lfloor D/2 \rfloor + 1 \le y \le D - 1$), size $\lfloor (D-1)/2 \rfloor$;
- $R_3(D): 2x = D$ ($x = D/2 < y < D$), size $\frac{D}{2} - 1$ if $2 \mid D$, else $0$;
- $R_4(D): 2y = D$ ($0 < x < y = D/2$), size $\frac{D}{2} - 1$ if $2 \mid D$, else $0$;
- $R_5(D): x + y = D$ ($1 \le x \le \lfloor (D-1)/2 \rfloor$), size $\lfloor (D-1)/2 \rfloor$.

Checking all $\binom{5}{2} = 10$ pairwise intersections inside $0 < x < y < D$:
- $R_1 \cap R_2$, $R_1 \cap R_5$, $R_2 \cap R_5$ all consist of the single point $(D/3, 2D/3)$ when $3 \mid D$ (and are empty otherwise), which has multiplicity $3$ in $\sum_{j=1}^5 |R_j(D)|$ and $1$ in $|\bigcup_{j=1}^5 R_j(D)|$, contributing $-2 \cdot \mathbf{1}_{3 \mid D}$;
- $R_1 \cap R_4 = \{(D/4, D/2)\}$ when $4 \mid D$, and $R_2 \cap R_3 = \{(D/2, 3D/4)\}$ when $4 \mid D$, disjoint from $(D/3, 2D/3)$ since $D/2 \notin \{D/3, 2D/3\}$, contributing $-2 \cdot \mathbf{1}_{4 \mid D}$;
- $R_1 \cap R_3$ ($y = D$), $R_2 \cap R_4$ ($x = 0$), $R_3 \cap R_4$ ($x = y$), $R_3 \cap R_5$ ($x = y$), $R_4 \cap R_5$ ($x = y$) are all empty on $0 < x < y < D$.

Therefore, for every integer $D \ge 1$ (noting the formula gives $0$ at $D = 1, 2$), the number of colliding pairs $(x, y)$ at span $D$ is
\[
\operatorname{cnt}(D) := 3\left\lfloor \frac{D-1}{2} \right\rfloor + (D-2)\mathbf{1}_{2 \mid D} - 2\mathbf{1}_{3 \mid D} - 2\mathbf{1}_{4 \mid D},
\]
and for all $q \ge 1$,
\[
B(q) := \left|\binom{[q]}{4} \setminus \mathcal{B}_{2,4}(q)\right| = \sum_{D=1}^{q-1} (q - D)\operatorname{cnt}(D).
\]
Consequently, $B(1) = B(2) = 0$ and for all $q \ge 2$,
\begin{equation}\label{eq:sec-diff}
B(q+1) - 2B(q) + B(q-1) = \operatorname{cnt}(q).
\end{equation}
Define the period-$12$ quasipolynomial
\[
P_{2,4}(q) := \frac{1}{3}q^3 - \frac{53}{24}q^2 + \ell(q) q - c(q \bmod 12),
\]
where $\ell(q) = \frac{47}{12}$ for $q$ even, $\ell(q) = \frac{25}{6}$ for $q$ odd, and
\[
(c(0), c(1), \dots, c(11)) = \left(0,\, \tfrac{55}{24},\, \tfrac{5}{3},\, \tfrac{13}{8},\, \tfrac{2}{3},\, \tfrac{55}{24},\, 1,\, \tfrac{55}{24},\, \tfrac{2}{3},\, \tfrac{13}{8},\, \tfrac{5}{3},\, \tfrac{55}{24}\right).
\]
Direct polynomial evaluation in each residue class $q \bmod 12$ shows $P_{2,4}(q+1) - 2P_{2,4}(q) + P_{2,4}(q-1) = \operatorname{cnt}(q)$ identically for all $q \ge 2$, and $P_{2,4}(1) = 0 = B(1)$, $P_{2,4}(2) = 0 = B(2)$. By induction via \eqref{eq:sec-diff}, $B(q) = P_{2,4}(q)$ for every $q \ge 1$.

Now compute $f_{2,4}(q+1) - f_{2,4}(q)$ using $f_{2,4}(q) = \frac{24 B(q)}{(q-1)(q-2)(q-3)}$ ($q \ge 4$):
\[
f_{2,4}(q+1) - f_{2,4}(q) = \frac{N_q}{q(q-1)(q-2)(q-3)},
\]
where $N_q := 24\bigl((q-3)B(q+1) - q B(q)\bigr)$ has exact polynomial form depending on $q \bmod 12$:
- For $q \equiv 0, 2, 4, 6, 8, 10 \pmod{12}$ (even $q$), $N_q = 11q^2 + b_q q + d_q$ with $(b_q, d_q) \in \{(-54,0),\, (2,-48),\, (-38,0),\, (-30,0),\, (-22,-48),\, (-14,0)\}$; in every case $N_q > 0$ for all even $q \ge 6$ (since $11q^2 - 54q > 0$ for $q \ge 5$, and $11\cdot 6^2 - 22\cdot 6 - 48 = 216 > 0$, $11\cdot 8^2 - 22\cdot 8 - 48 = 480 > 0$).
- For $q \equiv 1, 3, 5, 7, 9, 11 \pmod{12}$ (odd $q$), $N_q = -q^2 + b_q q + d_q$ with $(b_q, d_q) \in \{(28,-27),\, (36,-99),\, (44,-75),\, (52,-99),\, (12,-27),\, (68,-147)\}$; in every case $N_q < 0$ for all odd $q \ge 71$ (since $b_q \le 68$ and $d_q < 0$, so $-q^2 + 68q - 147 < 0$ for all $q \ge 69$).

Thus, for every $q \ge 70$, $f_{2,4}(q+1) > f_{2,4}(q)$ when $q$ is even and $f_{2,4}(q+1) < f_{2,4}(q)$ when $q$ is odd, so $f_{2,4}(q)$ is not eventually monotone. $\square$

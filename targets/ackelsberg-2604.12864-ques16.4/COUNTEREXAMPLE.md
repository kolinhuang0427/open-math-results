# Disproof of Question 16.4 (`Kneser's theorem in \N^2`)

**Target:** Ethan Ackelsberg and Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*, [arXiv:2604.12864v1](https://arxiv.org/abs/2604.12864v1), Section 16.1, Question 16.4 (`InverseProblemDensity_arXiv_v1.tex`, lines 5759–5777).

**Verdict:** **NO (False).** Let $\mathbb{N} = \{1, 2, 3, \ldots\}$ (as fixed in Section 1, line 398) and define the nonempty sets $A = B \subseteq \mathbb{N}^2$ by
$$A = B := \bigl(2\mathbb{N} \times \N_{\ge 3}\bigr) \;\cup\; \bigl\{(2^j, 1) : j \in \mathbb{N}\bigr\},$$
where $2\mathbb{N} = \{2k : k \in \mathbb{N}\}$ and $\N_{\ge 3} = \{y \in \mathbb{N} : y \ge 3\}$. Then:
1. $\underline{d}(A) = \underline{d}(B) = \frac{1}{2}$ and $\underline{d}(A + B) = \frac{1}{2} < 1 = \underline{d}(A) + \underline{d}(B)$;
2. For **every** finite-index subgroup $H_{a,b,c} = \{(an + bm, cm) : m, n \in \mathbb{Z}\}$ ($a, c \in \mathbb{N}$, $b \in \{0, 1, \ldots, a-1\}$) and $H := H_{a,b,c} \cap (\mathbb{N} \times \mathbb{N})$, the sumset $A + B$ does **not** equal a finite union of translates of $H$ up to finitely many elements.

*(Remark: The same obstruction holds if $\mathbb{N}$ were taken to be $\Z_{\ge 0}$ or if translates were allowed over $\mathbb{Z}^2$ or $\mathbb{Q}^2$: a thin boundary ray $\{(2^j, 1)\}$ produces on the horizontal line $\{y = 2\}$ an infinite sumset of linear density $0$, whereas every finite union of translates of $H$ intersects $\{y = 2\}$ in a co-finite subset of a finite union of arithmetic progressions.)*

---

## 1. Exact Description of $A + B$

Write $A_0 := 2\mathbb{N} \times \N_{\ge 3}$ and $A_1 := \{(2^j, 1) : j \in \mathbb{N}\}$. Since every element of $A_0$ has second coordinate $\ge 3$ while every element of $A_1$ has second coordinate $1$, the union $A = A_0 \sqcup A_1$ is disjoint. Computing the three pairwise sumsets in $A + B = A + A$:

1. **$A_0 + A_0$:** Every $2k \in 2\mathbb{N}$ satisfies $2k \ge 2$, and every even integer $\ge 4$ is $2 \cdot 1 + 2(k-1)$; similarly $\N_{\ge 3} + \N_{\ge 3} = \N_{\ge 6}$. Thus
   $$A_0 + A_0 = 2\N_{\ge 2} \times \N_{\ge 6},$$
   where $2\N_{\ge 2} = \{4, 6, 8, \ldots\}$.
2. **$A_0 + A_1$:** For every $k \in \mathbb{N}$, $y \ge 3$, and $j \in \mathbb{N}$, we have $(2k, y) + (2^j, 1) = (2k + 2^j, y + 1)$. Taking $j = 1$ gives $2k + 2$, which already ranges over all of $2\N_{\ge 2} = \{4, 6, 8, \ldots\}$; and $y + 1$ ranges over $\N_{\ge 4}$. Every $(2k + 2^j, y + 1)$ lies in $2\N_{\ge 2} \times \N_{\ge 4}$, so
   $$A_0 + A_1 = A_1 + A_0 = 2\N_{\ge 2} \times \N_{\ge 4}.$$
3. **$A_1 + A_1$:**
   $$A_1 + A_1 = \bigl\{(2^j + 2^{j'}, 2) : j, j' \in \mathbb{N}\bigr\}.$$

Combining all three pieces, since $2\N_{\ge 2} \times \N_{\ge 6} \subseteq 2\N_{\ge 2} \times \N_{\ge 4}$, the horizontal slices of $A + B$ are:
$$(A + B) \cap (\mathbb{N} \times \{y\}) = \begin{cases}
\varnothing & \text{if } y \in \{1, 3\}, \\
\bigl\{(2^j + 2^{j'}, 2) : j, j' \in \mathbb{N}\bigr\} & \text{if } y = 2, \\
2\N_{\ge 2} \times \{y\} & \text{if } y \ge 4.
\end{cases}$$

---

## 2. Verification of the Lower Density Inequality $\underline{d}(A + B) < \underline{d}(A) + \underline{d}(B)$

Fix $n, m \in \mathbb{N}$ with $n \ge 4$ and $m \ge 4$.
- For $A$: $|A_0 \cap ([n] \times [m])| = \lfloor n/2 \rfloor (m - 2)$, and $|A_1 \cap ([n] \times [m])| = |\{j \in \mathbb{N} : 2^j \le n\}| = \lfloor \log_2 n \rfloor$. Hence
  $$\frac{\lfloor n/2 \rfloor (m - 2)}{nm} \le \frac{|A \cap ([n] \times [m])|}{nm} \le \frac{\lfloor n/2 \rfloor (m - 2) + \lfloor \log_2 n \rfloor}{nm}.$$
  As $N \to \infty$, taking $\inf_{n,m \ge N}$ gives $\liminf_{n,m\to\infty} \frac{\lfloor n/2 \rfloor(m-2)}{nm} = \frac{1}{2}$ and $\limsup_{n,m\to\infty} \frac{\lfloor \log_2 n \rfloor}{nm} = 0$. Therefore
  $$\underline{d}(A) = \underline{d}(B) = d(A) = \frac{1}{2}.$$
- For $A + B$: on $[n] \times [m]$ ($n, m \ge 4$), the slice $y \ge 4$ contributes $(\lfloor n/2 \rfloor - 1)(m - 3)$ elements, the slices $y \in \{1, 3\}$ contribute $0$, and the slice $y = 2$ contributes
  $$S(n) := \bigl|\bigl\{x \in [n] : x = 2^j + 2^{j'} \text{ for some } j, j' \in \mathbb{N}\bigr\}\bigr| \le (\lfloor \log_2 n \rfloor)^2.$$
  Hence
  $$\frac{(\lfloor n/2 \rfloor - 1)(m - 3)}{nm} \le \frac{|(A+B) \cap ([n] \times [m])|}{nm} \le \frac{(\lfloor n/2 \rfloor - 1)(m - 3) + (\lfloor \log_2 n \rfloor)^2}{nm}.$$
  As $N \to \infty$ with $n, m \ge N$, $(\lfloor \log_2 n \rfloor)^2 / (nm) \to 0$, so
  $$\underline{d}(A + B) = d(A + B) = \frac{1}{2}.$$

Thus $\underline{d}(A + B) = \frac{1}{2} < 1 = \frac{1}{2} + \frac{1}{2} = \underline{d}(A) + \underline{d}(B)$, so the first alternative of Question 16.4 fails.

---

## 3. Refutation of the Finite-Union-of-Translates Alternative

Suppose for contradiction that there exist $a, c \in \mathbb{N}$, $b \in \{0, 1, \ldots, a-1\}$, $H = H_{a,b,c} \cap (\mathbb{N} \times \mathbb{N})$ where $H_{a,b,c} = \{(an + bm, cm) : m, n \in \mathbb{Z}\}$, and finitely many vectors $v_1, \ldots, v_r \in \mathbb{Z}^2$ (write $v_i = (v_{i,1}, v_{i,2})$) such that the symmetric difference
$$(A + B) \triangle U, \qquad U := \bigcup_{i=1}^r (v_i + H),$$
is finite.

Intersect both sets with the horizontal line $L_2 := \mathbb{N} \times \{2\}$. Since $|((A+B) \triangle U) \cap L_2| \le |(A+B) \triangle U| < \infty$, the slices $(A+B) \cap L_2$ and $U \cap L_2$ differ by only finitely many elements.

For each $i \in \{1, \ldots, r\}$, a point $(x, 2) \in \mathbb{N} \times \{2\}$ lies in $v_i + H$ if and only if there exist $m, n \in \mathbb{Z}$ such that
$$x - v_{i,1} = an + bm \in \mathbb{N}, \qquad 2 - v_{i,2} = cm \in \mathbb{N}.$$
Because $c \ge 1$ is fixed, the equation $cm = 2 - v_{i,2}$ determines at most one integer $m = m_i := \frac{2 - v_{i,2}}{c}$.
- If $\frac{2 - v_{i,2}}{c} \notin \mathbb{N}$, then $(v_i + H) \cap L_2 = \varnothing$.
- If $m_i \in \mathbb{N}$, then $x = v_{i,1} + b m_i + a n$ runs over all integers $x \equiv v_{i,1} + b m_i \pmod a$ satisfying $x \ge \max(1, v_{i,1} + 1)$ (as $a \ge 1$, every integer $n$ with $an > \max(-b m_i, -b m_i - v_{i,1})$ gives $an + b m_i \in \mathbb{N}$ and $x \in \mathbb{N}$).

Let $I := \{i \in \{1, \ldots, r\} : \frac{2 - v_{i,2}}{c} \in \mathbb{N}\}$. We split into two exhaustive cases:

- **Case 1: $I = \varnothing$.** Then $U \cap L_2 = \varnothing$. However, $(A+B) \cap L_2$ contains the infinite set $\{(2^j + 2, 2) : j \in \mathbb{N}\}$ (take $j' = 1$). Hence $|((A+B) \triangle U) \cap L_2| = \infty$, contradiction.

- **Case 2: $I \neq \varnothing$.** Pick any $i_0 \in I$, and let $r_0 := v_{i_0, 1} + b m_{i_0}$ and $X_0 := \max(1, v_{i_0, 1} + 1)$. Then for every integer $t \in \mathbb{Z}$ with $r_0 + a t \ge X_0$, the point $(r_0 + a t, 2)$ lies in $v_{i_0} + H \subseteq U \cap L_2$.
  Choose $K \in \mathbb{N}$ large enough that $2^K > \max(X_0, 4 a K^2)$. Look at the interval $[1, 2^K]$:
  - The arithmetic progression $\{r_0 + a t : t \in \mathbb{Z}\} \cap [X_0, 2^K]$ contains at least $\left\lfloor \frac{2^K - X_0}{a} \right\rfloor$ integers, all giving points in $U \cap L_2$.
  - On the other hand, any element $(x, 2) \in (A+B) \cap L_2$ with $x \le 2^K$ has $x = 2^j + 2^{j'}$ for some $1 \le j, j' \le K$, so $|(A+B) \cap ([2^K] \times \{2\})| \le K^2$.
  Since $K^2$ grows logarithmically while $\lfloor (2^K - X_0)/a \rfloor$ grows exponentially in $K$ (in fact, passing to $K \to \infty$ gives $\frac{|(U \setminus (A+B)) \cap ([2^K]\times \{2\})|}{2^K} \ge \frac{1}{a} - o(1) > 0$), $U \cap L_2$ contains infinitely many points not in $(A+B) \cap L_2$. Hence $|((A+B) \triangle U) \cap L_2| = \infty$, contradiction.

Thus neither alternative of Question 16.4 holds for $(A, B)$, refuting Question 16.4. $\blacksquare$

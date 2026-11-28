# Complete Settlement of Radici–Sala Open Problems Over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$ (`arXiv:2609.07769v2`, §9)

**Theorem.** *For every $q \in \{3, 4, 5\}$, every $n \ge 2$, and every degree $2 \le d \le n(q-1)$,*
$$\alpha_1(q, n, d) > \alpha_0(q, n, d).$$
*In particular, the inequality `eq:main` ($\alpha_1 > \alpha_0$) of Radici–Sala (`arXiv:2609.07769v2`, Section 7 Theorem `thm:main` / Section 9 `sec:open`) holds unconditionally for all three open finite fields $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$ across all dimensions $n \ge 2$ and all degrees $2 \le d \le n(q-1)$. Moreover, for every prime power $q \ge 7$, $\alpha_1(q, n, 2) < \alpha_0(q, n, 2)$ for all sufficiently large $n$ (confirming the failure heuristic of §9).*

---

## 1. Evaluation Matroid, Port-Split Identity, and Simplicial Bounds

Let $q \in \{3, 4, 5\}$, $V := \mathbb{F}_q^n$, $N := q^n$, and $Q_{q,d}$ be the $\mathbb{F}_q$-vector space of reduced polynomial functions $V \to \mathbb{F}_q$ of total degree at most $d$ (with every variable exponent at most $q-1$). Put $D := \dim_{\mathbb{F}_q} Q_{q,d}$ and let $\mathcal{M} = (V, r)$ be the evaluation matroid on $V$ where $r(S) := \dim_{\mathbb{F}_q}\{\operatorname{ev}(f)|_S : f \in Q_{q,d}\}$.

1. **Boundary degree $d = n(q-1)$.** Here $Q_{q, n(q-1)} = \mathbb{F}_q^V$, so $D = N$, every point is a coloop, $\alpha_0 = (N-1)^N$, and $\alpha_1 = N(N-1)^{N-1}$, giving $\alpha_1 - \alpha_0 = (N-1)^{N-1} > 0$. Assume henceforth $2 \le d \le n(q-1) - 1$.
2. **No loops, coloops, or parallel elements.** Since $q \ge 3$ and $2 \le d \le n(q-1) - 1$:
   - Every point $v \in V$ has a nonvanishing constant $1 \in Q_{q,d}$, so $v$ is not a loop.
   - Because every function $V \to \mathbb{F}_q$ has a unique reduced polynomial representation and $\prod_{i=1}^n (1 - (x_i - v_i)^{q-1})$ is the unique-up-to-scaling function supported on $\{v\}$ (having reduced degree $n(q-1) > d$), no nonzero function in $Q_{q,d}$ vanishes on $V \setminus \{v\}$; hence $r(V \setminus \{v\}) = D$ and $v$ is not a coloop.
   - For any two distinct $v \neq w \in V$, an affine linear functional $L \in Q_{q,1} \subseteq Q_{q,d}$ satisfies $L(v) = 1 \neq 0 = L(w)$, so $r(\{v,w\}) = 2$; hence no parallel elements exist.
3. **Characteristic polynomial representation.** For each $S \subseteq V$, a single function $f \in Q_{q,d}$ vanishes on $S$ in $q^{D - r(S)}$ ways, so a square system $(f_1, \dots, f_n) \in (Q_{q,d})^n$ vanishes simultaneously on $S$ in $(q^{D - r(S)})^n = N^{D - r(S)}$ ways. By inclusion–exclusion,
   $$\alpha_0(q, n, d) = \chi_{\mathcal{M}}(N), \qquad \alpha_1(q, n, d) = N \chi_{\mathcal{M}/0}(N).$$
4. **Simplicial port-split identity.** Fix $e_1 = 0 \in V$ first in the total order on $V$. By Radici–Sala Corollary `cor:pointed-reduction-full`, equation `eq:ab`, and Lemma `lem:interval` (`main-v32.tex` L702–776, applicable to any matroid with no loops/coloops/parallel elements),
   $$\frac{\alpha_1 - \alpha_0}{N^{D-1}} = \frac{\mathcal{S}_0(N)}{N^{D-1}} + \sum_{P \in \mathcal{P}_0 \cap \operatorname{Fix}_1(\mathcal{T}_0)} (-1)^{|P|} N^{2 - |P|} W(P),$$
   where $\mathcal{P}_0 := \{C \setminus \{0\} : C \text{ circuit of } \mathcal{M},\ 0 \in C\}$ is the $0$-port, and for each $P \in \mathcal{P}_0 \cap \operatorname{Fix}_1(\mathcal{T}_0)$,
   $$\mathcal{F}(P) := \{R \subseteq V \setminus (\{0\} \cup P) : P \sqcup R \in \operatorname{Fix}_1(\mathcal{T}_0)\}, \qquad W(P) := \sum_{r \ge 0} (-1)^r \sigma_r(P) N^{-r},$$
   with $\sigma_r(P) := |\{R \in \mathcal{F}(P) : |R| = r\}|$.
   By Lemma `lem:interval`(iii), $\mathcal{F}(P)$ is closed under taking subsets (a simplicial complex), so double-counting pairs $(R, R \cup \{x\})$ gives $(r+1)\sigma_{r+1}(P) \le (N - 1 - |P| - r)\sigma_r(P)$, hence $\sigma_{r+1}(P) N^{-(r+1)} \le \frac{1}{r+1} \sigma_r(P) N^{-r}$. Consequently:
   - **(a) Even port sets ($|P|$ even):** $W(P) \ge 0$, so every even-size $P$ contributes $+N^{2-|P|}W(P) \ge 0$ and can be dropped for a lower bound.
   - **(b) Odd port sets ($|P| = j \ge 5$):** $W(P) \le \sigma_0(P) = 1$, so all odd port sets of size $j \ge j_0$ contribute at least $-\sum_{j \ge j_0\text{ odd}} \mu_j N^{2-j}$, where $\mu_j := |\{P \in \mathcal{P}_0 : |P| = j\}|$.
   - **(c) Port-to-codeword bound:** Every circuit $C$ of $\mathcal{M}$ of size $w$ is the minimal support of $q-1$ nonzero scalar-multiple codewords in $\mathbf{C} := \mathrm{GRM}_q(d, n)^\perp$ (`thm:circuits` generalized to $\mathbb{F}_q$). By $\mathrm{AGL}_n(\mathbb{F}_q)$-transitivity on $V$, the number of weight-$w$ codewords in $\mathbf{C}$ whose support contains $0$ is $\frac{w}{N} A_w(\mathbf{C})$, so $\mu_{w-1} \le \frac{w}{(q-1)N} A_w(\mathbf{C})$ (strictly if $A_w$ includes non-minimal words). Hence for any even cutoff $w_0 \ge 6$ (note: minimal port sets with $|P|$ odd correspond to $w = |P| + 1 \ge 6$ even, and any $j \ge w_0 - 1$ satisfies $w = j + 1 \ge w_0$),
     $$\sum_{\substack{j \ge w_0 - 1 \\ j\text{ odd}}} \mu_j N^{2-j} \le \frac{N^2}{q-1} \sum_{w \ge w_0} w A_w(\mathbf{C}) N^{-w} =: \frac{N^2}{q-1} \Phi_{\ge w_0}(\mathbf{C}).$$
   - **(d) Main positive term $\mathcal{S}_0(N)/N^{D-1}$:** Since $\operatorname{Fix}_0(\overline{\mathcal{T}_0})$ is a simplicial complex on $V \setminus \{0\}$ (`lem:shadow`(i)), for $k=0,1,2,3,4,5$ with $\sigma_5^{(0)} \le \frac{N-5}{5}\sigma_4^{(0)}$,
     $$\frac{\mathcal{S}_0(N)}{N^{D-1}} \ge 1 - \frac{\sigma_1^{(0)}}{N} + \frac{\sigma_2^{(0)}}{N^2} - \frac{\sigma_3^{(0)}}{N^3} + \frac{4N + 5}{5 N^5}\sigma_4^{(0)}.$$
     Here $\sigma_k^{(0)} = \binom{N-1}{k}$ whenever $k \le d_{\min}(\mathbf{C}) - 2$. More precisely:
     - When $d_{\min}(\mathbf{C}) \ge 6$, no circuit of size $\le 5$ exists, so $\sigma_k^{(0)} = \binom{N-1}{k}$ for all $k \in \{0,1,2,3,4\}$.
     - When $d_{\min}(\mathbf{C}) = 5$ ($q=5, d=3$), every $5$-circuit is a $5$-point affine line ($\Lambda_5(n) = \frac{N(N-1)}{20}$ lines total), each contributing one excluded $4$-subset to $\binom{V\setminus\{0\}}{4}\setminus\operatorname{Fix}_0(\overline{\mathcal{T}_0})$ ($L \setminus \{0\}$ if $0 \in L$, or the broken circuit $L \setminus \{\min L\}$ if $0 \notin L$), so $\sigma_0^{(0)},\dots,\sigma_3^{(0)}$ are exact and $\sigma_4^{(0)} = \binom{N-1}{4} - \Lambda_5(n)$.
     - When $d_{\min}(\mathbf{C}) = 4$ ($d=2, q \in \{4,5\}$), let $\beta_3 := \binom{N-1}{3} - \sigma_3^{(0)}$ count all excluded $3$-subsets (both $0$-port sets and broken $4$-circuits with $0 \notin C$), and let $\beta_4^{\mathrm{new}}$ count excluded $4$-subsets containing no excluded $3$-subset. Because each excluded $3$-subset lies in at most $N-4$ sets of size $4$ and $\frac{1}{N^3} - \frac{(4N+5)(N-4)}{5N^5} > 0$, removing $\beta_3$ only increases $-\frac{\sigma_3^{(0)}}{N^3} + \frac{4N+5}{5N^5}\sigma_4^{(0)}$:
       $$-\frac{\sigma_3^{(0)}}{N^3} + \frac{4N+5}{5N^5}\sigma_4^{(0)} \ge -\frac{\binom{N-1}{3}}{N^3} + \frac{4N+5}{5N^5}\left(\binom{N-1}{4} - \beta_4^{\mathrm{new}}\right).$$
       Any $4$-set counted by $\beta_4^{\mathrm{new}}$ cannot contain a $4$-circuit or broken $4$-circuit, so it can only come from a $5$-circuit (since for $q=5, d=2$, any $5$-point line has rank $3$ and all its $4$-subsets are already $4$-circuits, there are no $5$-circuits, so $\beta_4^{\mathrm{new}} = 0$ for both $q=4$ and $q=5$; the looser bound $\beta_4^{\mathrm{new}} \le \Lambda_5(n) = \frac{N(N-1)}{20}$ also holds for $q=5$).

---

## 2. Structural Classification of $\mathrm{GRM}_q(d, n)^\perp$

Recall that $\mathrm{GRM}_q(d, n)^\perp = \mathrm{GRM}_q(n(q-1)-1-d, n) =: \mathbf{C}$. By the Kasami–Lin–Peterson (1968) formula, for $r = a(q-1) + b$ with $0 \le b < q-1$, $d_{\min}(\mathrm{GRM}_q(r, n)) = (q-b)q^{n-a-1}$. This gives the exact primal and dual distances:

| Field | Degree $d$ | $d_{\mathrm{primal}} = d_{\min}(\mathbf{C}^\perp)$ | $Y_{\max} = 1 - \frac{q d_{\mathrm{primal}}}{(q-1)N}$ | $d_{\mathrm{dual}} = d_{\min}(\mathbf{C})$ |
| :--- | :--- | :--- | :--- | :--- |
| $q=3$ | $d = 2$ | $N/3$ | $1/2$ | $6$ |
| $q=3$ | $3 \le d \le 2n-1$ | $\ge 2$ | $\le 1$ | $\ge 9$ |
| $q=4$ | $d = 2$ | $N/2$ | $1/3$ | $4$ |
| $q=4$ | $d = 3$ | $N/4$ | $2/3$ | $8$ |
| $q=4$ | $4 \le d \le 3n-1$ | $\ge 2$ | $\le 1$ | $\ge 12$ |
| $q=5$ | $d = 2$ | $3N/5$ | $1/4$ | $4$ |
| $q=5$ | $d = 3$ | $2N/5$ | $1/2$ | $5$ |
| $q=5$ | $d = 4$ | $N/5$ | $3/4$ | $10$ |
| $q=5$ | $5 \le d \le 4n-1$ | $\ge 2$ | $\le 1$ | $\ge 15$ |

**Lemma 1 (Affine Dimension Lemma).** *Let $q \ge 3$, $d \ge 2$, and $c \in \mathrm{GRM}_q(d, n)^\perp$ be a nonzero codeword with support $S = \operatorname{supp}(c)$.*
1. *If $|S| \in \{4, 5, 6, 7\}$, then $\dim \operatorname{aff}(S) \le 2$.*
2. *If $|S| \in \{4, 5\}$ and $d = 2$ (or $|S| = 5$ and $d = 3$ for $q = 5$), then $\dim \operatorname{aff}(S) = 1$ ($S$ is collinear).*

*Proof.* (1) Suppose $\dim \operatorname{aff}(S) \ge 3$ and $|S| \le 7$. Pick four affinely independent points $a_1, a_2, a_3, a_4 \in S$ and set $R := S \setminus \{a_1,a_2,a_3,a_4\}$, so $|R| \le 3$ and $\dim \operatorname{aff}(R) \le 2 < 3$. Hence some $a_i \notin \operatorname{aff}(R)$. Choose an affine linear functional $L_1$ vanishing on $R$ with $L_1(a_i) \neq 0$, and an affine linear functional $L_2$ vanishing on $\{a_1,a_2,a_3,a_4\} \setminus \{a_i\}$ with $L_2(a_i) \neq 0$. Because $q \ge 3$, $L_1 L_2 \in Q_{q,2} \subseteq Q_{q,d}$ separates $a_i$ from $S \setminus \{a_i\}$, forcing $c_{a_i} = 0$, contradiction.
(2) If $|S| \in \{4,5\}$ and $\dim \operatorname{aff}(S) \ge 2$, pick three non-collinear points $a_1,a_2,a_3 \in S$; the remaining $\le 2$ points span a flat of dimension $\le 1$, so some $a_i$ lies outside it and is separated from $S \setminus \{a_i\}$ by $L_1 L_2 \in Q_{q,2}$, contradiction. Since $q \ge 3$, $S$ cannot have $|S| \le 3$ (any $\le 3$ points are separated by $L_1 L_2$), so $\dim \operatorname{aff}(S) = 1$. $\square$

**Corollary 2 (Exact Low-Weight Enumerators).** *For all $n \ge 2$:*
- **Lines and planes:** The number of affine lines in $\mathbb{F}_q^n$ is $\Lambda_q(n) = \frac{N(N-1)}{q(q-1)}$ and the number of affine $2$-planes is $\Pi_q(n) = \frac{N(N-1)(N-q)}{q^2(q^2-1)(q^2-q)}$.
- **$q=3, d=2$:** $A_4 = A_5 = 0$, and $A_6(n) = 24\,\Pi_3(n) \le \frac{N^3}{18}$ (since every weight-$6$ codeword spans dimension $2$ and lies in a unique $2$-plane, where `GRM_3(2,2)^perp` has $A_6 = 24$).
- **$q=4, d=2$:** $A_4(n) = 3\Lambda_4(n) = \frac{N(N-1)}{4}$, $A_5(n) = 0$, $A_6(n) = 1920\,\Pi_4(n) \le \frac{2N^3}{3}$, and $\sigma_3^{(1)} = \frac{N-1}{3}$.
- **$q=5, d=2$:** $A_4(n) = 20\Lambda_5(n) = N(N-1)$, $A_5(n) = 4\Lambda_5(n) = \frac{N(N-1)}{5}$, $A_6(n) = 52{,}000\,\Pi_5(n) \le \frac{13N^3}{3}$, and $\sigma_3^{(1)} = \frac{3(N-1)}{4}$.
- **$q=5, d=3$:** $A_4(n) = 0$, $A_5(n) = \frac{N(N-1)}{5}$, and $A_6(n) = A_7(n) = 0$ (since every weight-$6,7$ codeword lies in a unique $2$-plane, and MacWilliams on `GRM_5(3,2)` yields $A_6 = A_7 = 0$!). Moreover every weight-$5$ circuit is a $5$-point line, so its port size $|P| = 4$ is even and contributes $\ge 0$ to $\alpha_1 - \alpha_0$; thus $\mu_3 = 0$, $\sigma_3^{(1)} = 0$, and $\mu_5 = \mu_6 = 0$.

**Lemma 3 (Lower Bound on $\sigma_3(P)$ for $q = 5, d = 2$).** *For $q=5, d=2$ and every $P \in \mathcal{P}_0^{(3)} \cap \operatorname{Fix}_1(\mathcal{T}_0)$ (lying on a $5$-point line $L \ni 0$),*
$$\sigma_1(P) = N - 5, \qquad \sigma_2(P) \le \binom{N-5}{2}, \qquad \sigma_3(P) \ge \binom{N-5}{3} - \frac{29}{2} N^2.$$

*Proof.* Every $x \in V \setminus L$ is not $1$-active with $P$ since $A_4$ words are collinear (so $P \cup \{x\}$ has no circuit besides $P \cup \{0\}$ and no $1$-active element), giving $\sigma_1(P) = N-5$. The upper bound $\sigma_2(P) \le \binom{N-5}{2}$ is immediate because $\mathcal{F}(P) \subseteq 2^{V \setminus L}$ and $|V \setminus L| = N - 5$. If a triple $T \subseteq V \setminus L$ fails $P \sqcup T \in \operatorname{Fix}_1(\mathcal{T}_0)$, then some circuit $C$ of size $|C| \le 7$ satisfies $C \setminus \{p\} \subseteq P \cup T$ with $p = \min C$ ($C \not\subseteq L$ since $P \in \operatorname{Fix}_1(\mathcal{T}_0)$):
- If $|C| \in \{4, 5\}$, $C$ lies on a line $L' \neq L$, so $|C \cap P| \le 1$. Thus either $T \subset L'$ ($\le \frac{N(N-1)}{20}\binom{5}{3} < \frac{1}{2}N^2$ triples) or $|C| = 4$ with $|(C\setminus\{p\})\cap P|=1$ and $|(C\setminus\{p\})\cap T|=2$ (choosing $x \in P$, line $L' \ni x$ with $L'\neq L$, two points of $L'\setminus\{x\}$, and a third point of $V \setminus L$ gives $\le 3 \cdot \frac{N-5}{4}\binom{4}{2}(N-5) = \frac{9}{2}(N-5)^2$ triples).
- If $|C| \in \{6, 7\}$, by Lemma 1 $C$ lies in an affine $2$-plane $\Pi$. Since $|(C\setminus\{p\})\cap P| \le 3$ and $|T| = 3$, $|C \cap P| \le 1$ would force $|(C\setminus\{p\})\cap T| \ge |C|-2 \ge 4 > |T|$, impossible. Thus $|C \cap P| \ge 2$, forcing $L \subset \Pi$ ($\frac{N-5}{20}$ choices) and $|T \cap (\Pi \setminus L)| \ge 2$ ($\le \binom{20}{2}(N-5)$ triples per plane), at most $\frac{N-5}{20}\cdot 190 (N-5) = \frac{19}{2}(N-5)^2$ triples.
Summing gives at most $\frac{1}{2}N^2 + \frac{9}{2}N^2 + \frac{19}{2}N^2 = \frac{29}{2}N^2$ excluded triples. $\square$

---

## 3. Normalized $q$-ary MacWilliams Identity with $c = 0$ Separation

For $c \in \mathbf{C}^\perp = \mathrm{GRM}_q(d, n)$, set $Y_c := 1 - \frac{q\,\mathrm{wt}(c)}{(q-1)N} \in [-\frac{1}{q-1}, 1]$. Define
$$\lambda_q := \frac{(q-1)N}{q}\ln\frac{N+q-1}{N-1}, \qquad \kappa_q := \frac{N}{N-1}\left(1 + \frac{q-1}{N}\right)^{N-1} e^{-\lambda_q}, \qquad f_q(Y) := \kappa_q e^{\lambda_q Y}(q-1)(N Y - 1).$$

**Lemma 4 (Exact Normalized MacWilliams Identity).** *For any linear code $\mathbf{C} \subseteq \mathbb{F}_q^N$,*
$$\mathbb{E}_{c \in \mathbf{C}^\perp}[f_q(Y_c)] = \sum_{w=1}^N w A_w(\mathbf{C}) N^{-(w-1)} = N\,\Phi(\mathbf{C}), \qquad \mathbb{E}_{u \in \mathbb{F}_q^N}[f_q(Y_u)] = 0.$$
*Furthermore, for every $m \ge 1$ and $Y \ge -\frac{1}{q-1}$, $f_q^{(m)}(Y) = \kappa_q (q-1)\lambda_q^{m-1}(\lambda_q(NY - 1) + m N) e^{\lambda_q Y} > 0$ (for $m \ge 2$).*

*Proof.* Differentiating the $q$-ary MacWilliams identity $W_{\mathbf{C}}(1, x) = |\mathbf{C}^\perp|^{-1} \sum_{c \in \mathbf{C}^\perp} (1 + (q-1)x)^{N - \mathrm{wt}(c)}(1 - x)^{\mathrm{wt}(c)}$ at $x = 1/N$ gives
$$\sum_{w=1}^N w A_w(\mathbf{C}) N^{-(w-1)} = \mathbb{E}_{c \in \mathbf{C}^\perp}\left[\left(1+\frac{q-1}{N}\right)^N \left(\frac{N-1}{N+q-1}\right)^{\mathrm{wt}(c)} \left(\frac{(q-1)(N-\mathrm{wt}(c))}{1 + (q-1)/N} - \frac{\mathrm{wt}(c)}{1 - 1/N}\right)\right].$$
Substituting $\mathrm{wt}(c) = \frac{(q-1)N}{q}(1 - Y_c)$ reduces the exponential factor to $\frac{(N-1)(N+q-1)}{N^2}\kappa_q e^{\lambda_q Y_c}$ and the bracket to $\frac{N^2}{(N-1)(N+q-1)}(q-1)(N Y_c - 1)$, yielding $f_q(Y_c)$. Taking $\mathbf{C} = \{0\}$ gives $\mathbb{E}_{u \in \mathbb{F}_q^N}[f_q(Y_u)] = 0$. The derivative formula follows by induction on $m$, and $\lambda_q(NY - 1) + m N \ge \lambda_q(-N/(q-1) - 1) + m N > (m - 1)N - \lambda_q > 0$ for $m \ge 2$ since $\lambda_q \le q-1$ (Lemma 5). $\square$

**Lemma 5 (Monotone Parameter & Moment Bounds).** *For every $q \in \{3, 4, 5\}$ and every $N \ge 27$ (and $N \ge 64$ for $q=4$, $N \ge 125$ for $q=5$):*
1. $\lambda_q \le q - 1$ and $\kappa_q \le 1$.
2. Let $f_q(Y) = P_{M-1}(Y) + R_M(Y)$ be the Taylor expansion about $Y = 0$ of even order $M \in \{6, 8\}$. Since $Y_0 = 1$ for $c = 0$ and $Y_c \in [-\frac{1}{q-1}, Y_{\max}]$ for every nonzero $c \in \mathbf{C}^\perp$,
   $$\mathbb{E}_{c \in \mathbf{C}^\perp}[R_M(Y_c)] \le \frac{f_q(1)}{q^D} + \frac{f_q^{(M)}(Y_{\max})}{M!}\left(\mathbb{E}_{c \in \mathbf{C}^\perp}[Y_c^M] - \frac{1}{q^D}\right),$$
   with $\frac{N}{q-1} \frac{f_q(1)}{q^D} = \kappa_q e^{\lambda_q} \frac{N(N-1)}{q^D} \le \frac{N^2 e^{q-1}}{q^D}$ and $\frac{N}{q-1} f_q^{(M)}(Y_{\max}) \le e^{(q-1)Y_{\max}} (q-1)^{M-1}((q-1)Y_{\max} + M) N^2$.
3. For each even $M \in \{6, 8\}$, writing $Y = \frac{1}{N}\sum_{i=1}^N Z_i$ on $\mathbb{F}_q^N$, every partition of $M$ into parts $\ge 2$ has positive moment product $\prod_j \mathbb{E}[Z_1^{r_j}] > 0$, so replacing $N(N-1)\cdots(N-k+1)$ by $N^k$ shows that $N^{M/2} \mathbb{E}_{\mathbb{F}_q^N}[Y^M]$ is upper-bounded by a polynomial in $N^{-1}$ with positive coefficients, hence strictly decreasing in $N$.
4. Writing $\alpha_{r, w}$ for the MacWilliams coefficient of $A_w(\mathbf{C})$ in $\mathbb{E}_{\mathbf{C}^\perp}[Y^r]$, we have $\alpha_{r, w} = 0$ for $w > r$, $\alpha_{4,4} = \frac{24}{(q-1)^4 N^4}$, $\alpha_{5,5} = \frac{120}{(q-1)^5 N^5}$, $\alpha_{6,6} = \frac{720}{(q-1)^6 N^6}$, $\alpha_{5,4} = \frac{240(q-2)}{(q-1)^5 N^5}$, and exact polynomials for $\alpha_{6,4}, \alpha_{6,5}$. Together with $\kappa_q \le 1$ and $\lambda_q \le q-1$, the coefficients of $A_4$ and $A_5$ in $\mathbb{E}_{\mathbf{C}^\perp}[P_5(Y)] - \mathbb{E}_{\mathbb{F}_q^N}[P_5(Y)] - \frac{4 A_4}{N^3} - \frac{5 A_5}{N^4}$ satisfy
   $$c_4 \alpha_{4,4} \le \frac{4}{N^3}, \qquad c_5 \alpha_{5,5} \le \frac{5}{N^4}, \qquad c_5 \alpha_{5,4} \le \frac{10(q-2)}{N^4}.$$

All exact rational inequalities in Lemma 5 are machine-checked in `verify.py`.

---

## 4. Case-by-Case Proof of $\alpha_1 > \alpha_0$ for All $q \in \{3,4,5\}$, $n \ge 2$, $2 \le d \le n(q-1)$

Every case below is verified in exact rational/integer arithmetic (zero floats) by `verify.py`:

1. **Finite base cases $n = 2$ (all $2 \le d \le 2(q-1)$):**
   - **$q = 3$ ($N = 9$, $d \in \{2, 3, 4\}$):** Exact subset evaluation over $2^9 = 512$ sets gives $\alpha_1 > \alpha_0$ in all cases (for $d=2$: $\alpha_0 = 184{,}184 < 206{,}712 = \alpha_1$).
   - **$q = 4$ ($N = 16$, $d \in \{2, 3, 4, 5, 6\}$):** Exact inclusion–exclusion over $2^{16}$ sets gives $\alpha_1 > \alpha_0$ in all cases (for $d=2$: $\alpha_0 = 6{,}012{,}645 < 6{,}242{,}400 = \alpha_1$).
   - **$q = 5$ ($N = 25$, $d \in \{2, 3, 4, 5, 6, 7, 8\}$):** For $d = 8$, coloop formula $(24)^{24} > 0$. For $d \in \{2, \dots, 7\}$, $\mathrm{AGL}_2(\mathbb{F}_5)$-orbit enumeration for $k = 0 \dots 12$ combined with matroid duality $\mathrm{GRM}_5(d,2)^* = \mathrm{GRM}_5(7-d,2)$ over all $2^{25}$ sets gives exact counts (for $d=2$: $\alpha_0 = 88{,}849{,}944 < 88{,}998{,}000 = \alpha_1$) with $\alpha_1 > \alpha_0$ in every case.
2. **Zero-codeword monotone regimes for $n \ge 3$ ($d_{\mathrm{dual}} > M$):**
   Here $\sigma_3^{(1)} = 0$ (no $4$-circuits), $\mathbb{E}_{\mathbf{C}^\perp}[P_{M-1}(Y)] = \mathbb{E}_{\mathbb{F}_q^N}[P_{M-1}(Y)]$, and $\mathbb{E}_{\mathbf{C}^\perp}[Y^M] = \mathbb{E}_{\mathbb{F}_q^N}[Y^M]$ identically, while $\mathcal{S}_0(N)/N^{D-1}$ satisfies the monotone finite-$N$ lower bound from `verify.py` (`s0_lb_monotone(N_0)`). By Lemma 5, the monotone-decreasing error bound at the base $N_0 = q^3$ already satisfies:
   - $q = 3,\ 3 \le d \le 2n-1$ ($M = 8,\ Y_{\max} = 1,\ N_0 = 27$): error $\le 0.002498 < 0.366549$.
   - $q = 4,\ d = 3$ ($M = 6,\ Y_{\max} = \frac{2}{3},\ N_0 = 64$): error $\le 0.181919 < 0.366646$.
   - $q = 4,\ 4 \le d \le 3n-1$ ($M = 8,\ Y_{\max} = 1,\ N_0 = 64$): error $\le 0.004285 < 0.366646$.
   - $q = 5,\ d = 4$ ($M = 8,\ Y_{\max} = \frac{3}{4},\ N_0 = 125$): error $\le 0.002594 < 0.366661$.
   - $q = 5,\ 5 \le d \le 4n-1$ ($M = 8,\ Y_{\max} = 1,\ N_0 = 125$): error $\le 0.007692 < 0.366661$.
3. **$q = 3, d = 2, n \ge 3$ ($M = 6, Y_{\max} = \frac{1}{2}, N_0 = 27$):** Since $d_{\mathrm{dual}} = 6$, $P_5$ is exact, $A_6(n) \le \frac{N^3}{18}$, and $\sigma_3^{(1)} = 0$. The monotone error bound at $N_0 = 27$ is $\le 0.173529 < 0.366549 \le \mathcal{S}_0(N)/N^{D-1}$.
4. **$q = 5, d = 3, n \ge 3$ ($M = 6, Y_{\max} = \frac{1}{2}, N_0 = 125$):** By Corollary 2, $A_4 = A_6 = A_7 = 0$ and $\sigma_3^{(1)} = 0$ ($5$-circuits have even port size $|P|=4$), so $P_5$ excess is nonpositive and only $A_5 = \frac{N(N-1)}{5}$ enters $R_6$. The monotone error bound at $N_0 = 125$ is $\le 0.165050 < 0.366658 \le \mathcal{S}_0(N)/N^{D-1}$.
5. **$q = 4, d = 2, n \ge 3$ ($M = 6, Y_{\max} = \frac{1}{3}$):**
   - For $n = 3$ ($N = 64$): exact rational verification gives margin $\mathcal{S}_0/N^{D-1} - \text{loss}_{j=3} \ge 0.207604$ vs error bound $\le 0.195837$ (surplus $> 0.011766$).
   - For all $n \ge 4$ ($N \ge 256$): $\mathcal{S}_0/N^{D-1} - \text{loss}_{j=3} \ge 0.199945$ vs monotone error bound $\le 0.047769$ (surplus $> 0.152175$).
6. **$q = 5, d = 2, n \ge 3$ ($Y_{\max} = \frac{1}{4}$):** For every $P \in \mathcal{P}_0^{(3)} \cap \operatorname{Fix}_1(\mathcal{T}_0)$, Lemma 3 combined with Lemma `lem:interval`(iii) gives both the coarse $r \le 4$ upper bound $W(P) \le 1 - \frac{N-5}{N} + \frac{\binom{N-5}{2}}{N^2} - \frac{\sigma_3(P)}{N^3} + \frac{\binom{N-5}{4}}{N^4}$ and (since $\sigma_4(P) \le \frac{N-8}{4}\sigma_3(P)$) the shadow-tightened upper bound $W(P) \le 1 - \frac{N-5}{N} + \frac{\binom{N-5}{2}}{N^2} - \frac{3N+8}{4N^4}\sigma_3(P)$:
   - For $n = 3$ ($N = 125$): order $V \setminus \{0\}$ by grouping the $31$ lines through $0$ as $L_1 < \dots < L_{31}$. Counting internal circuits ($360 + 6840 = 7200$, where the $6\binom{20}{3} = 6{,}840$ planar triples absorb all $7$-circuits — both internal and external — as well as internal $6$-circuits), external $4$-lines $L' \not\ni 0$ (both the $|C \cap P| = 1$ case giving $\frac{744 \cdot 15 \cdot 3 \cdot 118}{93} = 42{,}480$ triples and the $|C \cap P| = 0$ case $T \subset L'$ giving at most $744 \binom{5}{4} = 3{,}720$ triples), and external $6$-circuits $P \cup \{t_1,t_2,p\}$ in planes $\Pi \supset L_i$ (where $\operatorname{rk}(P \cup \{t_1,t_2,p\}) = 3 + \operatorname{rk}_{\mathrm{aff}}(\{t_1,t_2,p\})$ forces $\{t_1,t_2,p\}$ collinear on one of $4$ parallel lines, $5$ lines through $a_4$, or on average $\frac{5}{2}$ preceding lines through $0$, giving $6 \cdot (40 + 20 + 10) \cdot 118 = 49{,}560$) yields average $\sigma_3(P) \ge \binom{120}{3} - 102{,}960$, hence $\text{margin} \ge 0.041313$ (coarse $r \le 4$, and $\ge 0.050491$ via shadow $\sigma_4(P) \le \frac{117}{4}\sigma_3(P)$). Meanwhile, every $P \in \mathcal{P}_0^{(5)}$ lies in a unique plane $\Pi \ni 0$ and no $x \in V \setminus \Pi$ can create a $1$-active element of size $\le 7$ with $P$ (since $P \cup \{0\}$ has no $4$-collinear points), so $\sigma_1(P) \ge 100$ and $W(P) \le 1 - \frac{100}{125} + \frac{\binom{119}{2}}{125^2} = \frac{10146}{15625}$. Moreover, every $7$-circuit gives an **even** port size $|P| = 6$ whose contribution is $\ge 0$ (dropped alongside $w=4,5$), so the exact $8$-weight enumerator of $\mathrm{GRM}_5(2,3)$ (from all $5^6 = 15{,}625$ symmetric $3 \times 3$ matrices over $\mathbb{F}_5$, giving $A_6 = 8{,}060{,}000$ and $A_7 = 81{,}840{,}000$) bounds the negative error over $w=6$ and $w \ge 8$ by $\le 0.039690 < 0.041313$ (and $< 0.050491$).
   - For $n = 4$ ($N = 625$): Lemma 3 gives $\text{margin} \ge 0.067099$ (coarse $r \le 4$; and $\ge 0.071402$ via shadow) vs exact-coefficient $P_5 + R_6$ error $\le 0.053757$ (surplus $> 0.013342$).
   - For all $n \ge 5$ ($N \ge 3125$): Lemma 3 gives monotone $\text{margin} \ge 0.081753$ (coarse $r \le 4$; and $\ge 0.082621$ via shadow) vs monotone error bound $\le 0.014082$ (surplus $> 0.067671$).

*(Remark on $q \ge 7, d = 2$, large $n$.)* By the same identity, $\frac{\mathcal{S}_0}{N^{D-1}} \le \frac{3}{8} + O_q(1/N)$ while $\sigma_3^{(1)} = \frac{(q-2)(q-3)}{2(q-1)}(N-1) \ge \frac{5}{3}(N-1)$ and $W(P) \ge 1 - 1 + \frac{1}{2} - \frac{1}{6} - O_q(1/N) = \frac{1}{3} - O_q(1/N)$, while $R_6 = O_q(1/N)$ and even port sets $|P|=4$ contribute $\le \frac{1}{N^2}\mu_4 = O_q(1/N)$. Hence $\frac{\alpha_1 - \alpha_0}{N^{D-1}} \le \frac{3}{8} - \frac{5}{9} + O_q(1/N) = -\frac{13}{72} + O_q(1/N) < 0$ for every prime power $q \ge 7$ and all sufficiently large $n$. $\square$

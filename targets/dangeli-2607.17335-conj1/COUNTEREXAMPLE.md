# Disproof of `conj:typical-total-simplicity` (Conjecture 4.6) at $k = 2$

**Target:** Daniele D'Angeli and Emanuele Rodaro, *On totally synchronizing graphs*, [arXiv:2607.17335v1](https://arxiv.org/abs/2607.17335v1), Section 4 (*Totally simple graphs*), Conjecture 4.6 (`\label{conj:typical-total-simplicity}`, lines 1457–1471).

**Verdict:** **FALSE at $k = 2$.** There exist explicit constants $c_0 = \frac{1}{30} > 0$ and $N_0 = 4000$ such that for all $n \ge N_0$,
$$\Pr_{G \sim \mathrm{Unif}([n]^{2n})}\bigl(G \text{ is totally simple} \mid G \in \mathrm{SCC}_n\bigr) \le 1 - \frac{1}{30} = \frac{29}{30}.$$
Hence $\Pr(G \text{ is totally simple} \mid \mathrm{SCC}_n) \not\to 1$ as $n \to \infty$, refuting the main convergence claim (and consequently the $1 - \exp(-c_2 n + \beta_2) + o(1)$ asymptotic) of Conjecture `conj:typical-total-simplicity` for $k = 2$.

*(Note: By contrast, for $k \ge 3$ the probability of a twin pair decays as $\binom{n}{2} O(n^{-k}) = O(n^{2-k}) \to 0$, matching the numerical heuristic in Table `tab:totally-simple-experiments-agg`, which already showed flat proportions $0.346, 0.361, 0.346$ at $k = 2$ for $n = 8, 9, 10$.)*

---

## 1. Twin Pairs Obstruct Total Simplicity

Recall from `totally_main.tex` (Section 2 lines 216–240; Section 4 lines 1357–1388) that a $2$-out directed multigraph $G = ([n], E, s, t)$ has two ordered outgoing edge slots $(a_u, b_u) \in [n]^2$ at each vertex $u \in [n]$; an automaton coloring $\chi : E \to \{1, 2\}$ labels the two outgoing edges of each vertex bijectively by $\{1, 2\}$, producing a deterministic complete automaton $\chi(G) = ([n], \{1, 2\}, \delta_\chi)$. The automaton $\chi(G)$ is *simple* if its only congruences are the discrete relation $\Delta$ and the universal relation $\nabla$, and $G$ is *totally simple* if $\chi(G)$ is simple for every coloring $\chi$.

**Definition (Clean twin pair).** Given $G \in ([n]^2)^n$, an unordered pair of distinct vertices $\{u, v\} \subset [n]$ is a *clean twin pair* if there exist distinct vertices $a, b \in [n] \setminus \{u, v\}$ ($a \neq b$) such that the outgoing multisets at $u$ and $v$ both equal $\{a, b\}$ (so each of $u, v$ has ordered out-tuple $(a, b)$ or $(b, a)$). Let $N(G)$ denote the number of clean twin pairs in $G$.

**Lemma 1.** *Let $n \ge 3$. If $G$ contains a twin pair $\{u, v\}$ with equal outgoing multisets $\delta_u = \delta_v$ (in particular, if $N(G) \ge 1$), then $G$ is not totally simple.*

*Proof.* Label the two outgoing edges of $u$ and $v$ under a coloring $\chi : E \to \{1, 2\}$ so that $t(e_{u,i}) = t(e_{v,i})$ for $i = 1, 2$ (possible because $\delta_u = \delta_v$ as multisets), and color all other vertices' outgoing edges arbitrarily. Let $\rho$ be the equivalence relation on $[n]$ whose sole nontrivial class is $\{u, v\}$ and all other classes are singletons. Since $n \ge 3$, $\rho \notin \{\Delta, \nabla\}$. For every $x \mathrel{\rho} y$, either $x = y$ or $\{x, y\} = \{u, v\}$, in which case $\delta_\chi(u, i) = \delta_\chi(v, i)$ for $i \in \{1, 2\}$. Thus $\rho \in \mathrm{Cong}(\chi(G))$ is a nontrivial congruence, so $\chi(G)$ is not simple and $G$ is not totally simple. (Equivalently, $\rho$ is a nontrivial lumpable partition in Theorem 4.4 `theo: lump=to simple`.) $\square$

*(Small strongly connected twin-pair examples $n = 3, 4, 5, 6$ are explicitly constructed and checked in `verify.py`.)*

---

## 2. Surjection Conditioning and Paley–Zygmund Framework

In D'Angeli–Rodaro's model (Section 4, line 1449), each vertex independently chooses $k = 2$ outgoing heads uniformly with replacement, so $G$ is uniformly distributed on $([n]^2)^n \cong [n]^{2n}$ (tuples of $2n$ edge heads in $[n]$). For $n \ge 2$, every strongly connected graph has minimum in-degree at least $1$:
$$\mathrm{SCC}_n \subseteq \mathcal{E}_n := \bigl\{ G \in [n]^{2n} : \mathrm{in}_G(v) \ge 1 \text{ for all } v \in [n] \bigr\}.$$
The set $\mathcal{E}_n$ is precisely the set of surjections $[2n] \to [n]$. For any integers $m \ge k \ge 0$, let $T(m, k)$ denote the number of surjections $[m] \to [k]$, so $|\mathcal{E}_n| = T(2n, n) = n! \genfrac{\{}{\}}{0pt}{}{2n}{n}$, where $T(0,0)=1$, $T(m,0)=0$ ($m \ge 1$), and $T(m, k) = k\bigl(T(m-1, k) + T(m-1, k-1)\bigr)$ for $m, k \ge 1$. Moreover, for any integer $t \ge 0$, the number of functions $[m] \to [k + t]$ whose image contains $[k]$ is
$$F(m, k, t) := \sum_{j=0}^{m-k} \binom{m}{j} t^j T(m-j, k) = m! [x^m] e^{tx} (e^x - 1)^k = \sum_{i=0}^{t} \binom{t}{i} T(m, k+i).$$

Using Lemma 1 and $\mathrm{SCC}_n \subseteq \mathcal{E}_n$, under the uniform distribution $\mathbb{P}_n$ on $\mathcal{E}_n$,
$$\Pr(G \text{ not totally simple} \mid \mathrm{SCC}_n) \ge \Pr(N(G) \ge 1 \mid \mathrm{SCC}_n) = \frac{\mathbb{P}_n(N(G) \ge 1,\, G \in \mathrm{SCC}_n)}{\mathbb{P}_n(G \in \mathrm{SCC}_n)} \ge \mathbb{P}_n(N(G) \ge 1,\, G \in \mathrm{SCC}_n).$$
Applying the Paley–Zygmund inequality to the nonnegative random variable $Z := N(G) \cdot \mathbf{1}_{\{G \in \mathrm{SCC}_n\}}$ on $(\mathcal{E}_n, \mathbb{P}_n)$ gives
$$\mathbb{P}_n(N(G) \ge 1,\, G \in \mathrm{SCC}_n) \ge \frac{\mathbb{E}_n\bigl[N(G) \cdot \mathbf{1}_{\{G \in \mathrm{SCC}_n\}}\bigr]^2}{\mathbb{E}_n\bigl[N(G)^2\bigr]}. \tag{1}$$
We prove below that for all $n \ge N_0 = 4000$,
$$\mathbb{E}_n\bigl[N(G) \cdot \mathbf{1}_{\{G \in \mathrm{SCC}_n\}}\bigr] \ge \frac{20}{100} \quad \text{and} \quad \mathbb{E}_n\bigl[N(G)^2\bigr] \le \frac{120}{100},$$
which yields $\Pr(G \text{ not totally simple} \mid \mathrm{SCC}_n) \ge \frac{(1/5)^2}{6/5} = \frac{1}{30}$.

---

## 3. Saddle-Point and Local Bounds on Surjection Counts

Let $\lambda \in (1, 2)$ be the unique positive solution to
$$\frac{\lambda}{1 - e^{-\lambda}} = 2 \qquad (\lambda \approx 1.59362426, \text{ verified in } [\tfrac{1593624}{10^6}, \tfrac{1593625}{10^6}]).$$
Then $e^\lambda - 1 = \frac{\lambda}{2 - \lambda}$ and $e^\lambda = \frac{2}{2 - \lambda}$, so $\frac{e^\lambda}{e^\lambda - 1} = \frac{2}{\lambda}$. Let $X_1, X_2, \dots$ be i.i.d. zero-truncated Poisson random variables $\mathrm{ZTP}(\lambda)$:
$$\Pr(X_1 = m) = \frac{\lambda^m / m!}{e^\lambda - 1} \quad (m \ge 1), \qquad p_k(m) := \Pr\Bigl(\sum_{i=1}^k X_i = m\Bigr).$$
By the exponential generating function $(e^x - 1)^k = \sum_{m \ge k} T(m, k) x^m/m!$, for every $m \ge k \ge 1$ and every $r > 0$,
$$T(m, k) = \frac{m!}{\lambda^m} (e^\lambda - 1)^k \, p_k(m), \qquad F(m, k, t) \le \frac{m!}{r^m} e^{tr} (e^r - 1)^k. \tag{2}$$
In addition, expanding $e^{tx} = \sum_{j \ge 0} t^j x^j/j!$ gives
$$F(m, k, t) = \frac{m!}{\lambda^m} (e^\lambda - 1)^k \sum_{j=0}^{m-k} \frac{(t\lambda)^j}{j!} p_k(m - j) \le \frac{m!}{\lambda^m} e^{t\lambda} (e^\lambda - 1)^k \sup_{r \in \mathbb{Z}} p_k(r). \tag{3}$$

Let $Y := X_1 - 2$ and $\varphi(t) := \mathbb{E}[e^{itX_1}] = \frac{e^{\lambda e^{it}} - 1}{e^\lambda - 1}$. Using factorial moments $\mathbb{E}[X_1] = 2$ and $\mathbb{E}[X_1(X_1-1)\cdots(X_1-r+1)] = 2\lambda^{r-1}$ ($r \ge 2$), we obtain:
- $\mathbb{E}[Y] = 0$, $\sigma^2 := \mathbb{E}[Y^2] = 2(\lambda - 1) \approx 1.187249$,
- $m_3 := \mathbb{E}[|Y|^3] = \mathbb{E}[Y^3] + 2\Pr(X_1 = 1) = (2\lambda^2 - 6\lambda + 6) + 2(2 - \lambda) = 2\lambda^2 - 8\lambda + 10 \approx 2.330282$,
- $m_4 := \mathbb{E}[Y^4] = 2\lambda^3 - 4\lambda^2 + 14\lambda - 14 \approx 6.246645$.

**Lemma 2 (Explicit Fourier bounds on $p_k(m)$).** Set $\delta = \frac{3}{10}$ and $N_0 = 4000$.
1. *(Global decay)* For all $t \in [-\pi, \pi]$, writing $A = \lambda + \frac{\lambda^2}{2}$ and splitting $\varphi(t) = \frac{(\lambda e^{it} + \frac{\lambda^2}{2}e^{2it}) + \sum_{r \ge 3}\frac{\lambda^r}{r!}e^{irt}}{e^\lambda - 1}$ via the triangle inequality gives
   $$|\varphi(t)| \le \frac{\sqrt{A^2 - \lambda^3(1 - \cos t)} + (e^\lambda - 1 - A)}{e^\lambda - 1} =: \rho(t),$$
   which is strictly decreasing on $[0, \pi]$; at $t = \delta = 0.3$, $\rho_\delta := \rho(0.3) < 0.992$.
2. *(Local quadratic decay)* For $|t| \le \delta$, $\cos u \le 1 - \frac{u^2}{2} + \frac{u^4}{24}$ and $|\sin u - u| \le \frac{|u|^3}{6}$ yield
   $$|\varphi(t)|^2 = \bigl(\mathbb{E}[\cos(tY)]\bigr)^2 + \bigl(\mathbb{E}[\sin(tY)]\bigr)^2 \le \left(1 - \frac{\sigma^2}{2}t^2 + \frac{m_4}{24}t^4\right)^2 + \frac{m_3^2}{36}t^6 \le 1 - 2c_{\mathrm{loc}} t^2 \le e^{-2c_{\mathrm{loc}}t^2},$$
   with $2c_{\mathrm{loc}} := \sigma^2 - \left(\frac{\sigma^4}{4} + \frac{m_4}{12} + \frac{m_3^2}{36}\delta^2 + \frac{m_4^2}{576}\delta^4\right)\delta^2 > 1.107$.
3. *(Uniform upper bound)* By Fourier inversion $p_k(m) = \frac{1}{2\pi}\int_{-\pi}^{\pi} \varphi(t)^k e^{-imt}\,dt$, splitting at $|t| \le \delta$ and $|t| > \delta$ gives, for all $k \ge 1996$ and all $m \in \mathbb{Z}$,
   $$\sqrt{k}\, p_k(m) \le \frac{\sqrt{k}}{2\pi} \int_{-\infty}^{\infty} e^{-k c_{\mathrm{loc}} t^2}\,dt + \sqrt{k}\, \rho_\delta^k = \frac{1}{2\sqrt{\pi c_{\mathrm{loc}}}} + \sqrt{k}\,\rho_\delta^k \le C_{\mathrm{up}} := \frac{38}{100}$$
   (since $\frac{1}{2\sqrt{\pi c_{\mathrm{loc}}}} < 0.3791$ and $\sqrt{k}\rho_\delta^k$ decreases for $k \ge 1996$ with $\sqrt{1996}\rho_\delta^{1996} < 6 \times 10^{-6}$).
4. *(Central lower bound)* For all $k \ge 3998$ and $|d| \le 4$, setting $t_0 := \frac{R}{\sqrt{k}}$ with $R = \frac{26}{10}$: on $|t| \le t_0$, $\mathrm{Re}(\varphi(t)e^{-2it}) \ge 1 - \frac{\sigma^2}{2}t^2 \ge e^{-\frac{\sigma^2}{2}t^2 - \frac{\sigma^4}{4}t^4}$ and $|\arg(\varphi(t)e^{-2it})| \le \frac{m_3 |t|^3}{6(1 - \frac{\sigma^2}{2}t_0^2)}$, so $|k \arg + d t| \le \theta_{\max}(k) < 0.28$. Integrating over $[-t_0, t_0]$ and subtracting the Gaussian tail $\frac{e^{-c_{\mathrm{loc}}R^2}}{2\pi c_{\mathrm{loc}} R} < 0.0027$ on $[t_0, \delta]$ and $\sqrt{k}\rho_\delta^k < 3 \times 10^{-6}$ on $[\delta, \pi]$ gives
   $$\sqrt{k}\, p_k(2k + d) \ge c_{\mathrm{low}} := \frac{34}{100} \qquad (\forall k \ge 3998,\ |d| \le 4).$$

Every rational bracket and inequality in Lemma 2 is checked in exact `Fraction` arithmetic in `verify.py`.

---

## 4. Conditional Strong Connectivity Given a Clean Twin Pair

Fix four distinct vertices $1, 2, a, b \in [n]$ ($n \ge 4000$) and define the twin-conditioned event
$$\mathcal{T} := \bigl\{ G \in \mathcal{E}_n : \text{vertex } 1 \text{ has out-tuple } (a,b) \text{ and vertex } 2 \text{ has out-tuple } (a,b) \bigr\}.$$
Since $a$ and $b$ already receive two edges each from $\{1, 2\}$, a graph $G$ with $(a_1,b_1)=(a_2,b_2)=(a,b)$ lies in $\mathcal{E}_n$ if and only if the remaining $2n - 4$ arcs from $[n] \setminus \{1, 2\}$ hit every vertex of $[n] \setminus \{a, b\}$. Thus
$$|\mathcal{T}| = F(2n - 4, n - 2, 2) = T(2n - 4, n) + 2T(2n - 4, n - 1) + T(2n - 4, n - 2).$$
Applying Lemma 2(4) with $k \in \{n, n-1, n-2\} \ge 3998$ and $m = 2n - 4 \in [2k - 4, 2k]$ (note $(e^\lambda - 1)^2 + 2(e^\lambda - 1) + 1 = e^{2\lambda}$),
$$|\mathcal{T}| \ge \frac{c_{\mathrm{low}}}{\sqrt{n}} \frac{(2n - 4)!}{\lambda^{2n - 4}} e^{2\lambda} (e^\lambda - 1)^{n - 2}. \tag{4}$$

If $G \in \mathcal{T}$ is *not* strongly connected, then its condensation DAG has at least one sink SCC $S_{\mathrm{sink}}$ (no outgoing edges) and at least one source SCC $S_{\mathrm{src}}$ (no incoming edges), which are disjoint; hence $\min(|S_{\mathrm{sink}}|, |S_{\mathrm{src}}|) \le \lfloor n/2 \rfloor$. Therefore $G \in \mathcal{T} \setminus \mathrm{SCC}_n$ implies there exists a **strongly connected** subset $S \subset [n]$ of size $1 \le s \le \lfloor n/2 \rfloor$ that is either a **sink** or a **source**. We bound the expected number of such subsets in $\mathcal{T}$ across four exhaustive cases (all uniform over $n \ge 4000$, verified in `verify.py`):

### Case 1a: Sink $S$ with $S \cap \{1, 2\} = \emptyset$ ($1 \le s \le \lfloor n/2 \rfloor$)
There are $\binom{n-2}{s}$ choices for $S$. Since $S$ is strongly connected and sends no edges out, its $2s$ arcs surject onto $S$ in at most $T(2s, s) \le \frac{(2s)!}{\lambda^{2s}}(e^\lambda-1)^s$ ways. Let $t = |\{a,b\} \setminus S| \in \{0, 1, 2\}$. The $2n - 4 - 2s$ arcs from $([n] \setminus \{1,2\}) \setminus S$ must cover $([n] \setminus S) \setminus \{a, b\}$ (size $n - s - t$) and may hit $S \cup (\{a,b\} \setminus S)$ (size $s + t$), giving $F(2n - 4 - 2s, n - s - t, s + t)$ choices.
- For $1 \le s \le 4$: using (3) with $k = n - s - t \ge n - 6 \ge 3994$ and Lemma 2(3) ($C_{\mathrm{up}}$), dividing by (4) gives $\le \frac{C_{\mathrm{up}}}{c_{\mathrm{low}}}\sqrt{\frac{n}{n-6}} \binom{n-2}{s}\frac{(2s)!(2n-4-2s)!}{(2n-4)!} e^{s\lambda} (e^\lambda/(e^\lambda-1))^{t-2} < 0.001$ (using $(e^\lambda/(e^\lambda-1))^{t-2} \le 1$, or even bounded by $(2/\lambda)^2$).
- For $5 \le s \le 0.02 n$: using (3) with $k = n - s - t \ge 0.98n - 2 \ge 3918 \ge 1996$ and Lemma 2(3) ($C_{\mathrm{up}}$) cancels $\sqrt{n}$ (leaving $\frac{C_{\mathrm{up}}}{c_{\mathrm{low}}}\sqrt{\frac{n}{n-s-t}} \le 1.13$), while $\binom{n-2}{s}\frac{(2s)!(2n-4-2s)!}{(2n-4)!} = 2^{-s}\prod_{j=0}^{s-1}\frac{2s-j}{2n-5-2j} \le \bigl(\frac{s}{1.96n - 4}\bigr)^s$ and $e^{(s+t-2)\lambda}(e^\lambda-1)^{2-t} \le e^{s\lambda}$ for $t \in \{0,1,2\}$. Splitting $5 \le s \le 9$ (using $\frac{s}{1.96n-4} \le \frac{s}{7836}$, sum $< 4 \times 10^{-13}$) and $10 \le s \le 0.02n$ (using $\frac{s}{1.96n-4} \le 0.0103$, sum of $1.13(0.0103 e^\lambda)^s < 2 \times 10^{-13}$), the total over $5 \le s \le 0.02n$ is $< 10^{-12} < 10^{-8}$.
- For $0.02 n < s \le \lfloor n/2 \rfloor$: using (2) with $r = \lambda$ internally ($T(2s,s) \le \frac{(2s)!}{\lambda^{2s}}(e^\lambda - 1)^s$) and with $r_s = \lambda(1 - 1.3\frac{s}{n})$ externally ($F(2n-4-2s, n-s-t, s+t)$) together with $\frac{\binom{n-2}{s}}{\binom{2n-4}{2s}} \le 16\frac{\binom{n}{s}}{\binom{2n}{2s}} \le 16(2n+1) e^{-n H(s/n)}$ (where $H(x) := -x\ln x - (1-x)\ln(1-x)$) and dividing by (4), each term is at most
  $$\frac{16(2n+1)\sqrt{n}}{c_{\mathrm{low}}}\left(\frac{r_s}{\lambda}\right)^4 \left(\frac{e^{r_s}}{e^{r_s}-1}\right)^t \left(\frac{e^\lambda - 1}{e^\lambda}\right)^2 \exp\bigl(n \cdot f_{\mathrm{sink}}(s/n)\bigr),$$
  where, writing $r(\alpha) := \lambda(1 - 1.3\alpha)$,
  $$f_{\mathrm{sink}}(\alpha) := -H(\alpha) - 2(1-\alpha)\ln\frac{r(\alpha)}{\lambda} + \alpha r(\alpha) + (1-\alpha)\ln\frac{e^{r(\alpha)} - 1}{e^\lambda - 1}.$$
  Interval checking on $[0.02, 0.5]$ shows $f_{\mathrm{sink}}(\alpha) \le -0.05$ (while the $O(n^{3/2})$ prefactor is $< 100(2n+1)\sqrt{n}$ since $r_s \in [0.35\lambda, \lambda]$), so the sum over $s > 0.02n \ge 80$ is $< 10^{-60}$.
Thus $\Sigma_{1a} < 0.002$.

### Case 1b: Sink $S$ with $S \cap \{1, 2\} \neq \emptyset$ ($3 \le s \le \lfloor n/2 \rfloor$)
Because $1, 2 \to a, b$ and $S$ has no outgoing edges, we must have $a, b \in S$. Letting $r = |S \cap \{1,2\}| \in \{1, 2\}$ ($s \ge 2 + r$), there are $\binom{2}{r}\binom{n-4}{s-2-r}$ choices for $S$. Inside $S$, the $2(s - r)$ free arcs must cover $S \setminus \{a,b\}$ (size $s - 2$) and may hit $\{a, b\}$ (at most $F(2s - 2r, s - 2, 2)$ ways); outside $S$, the $2(n - s - 2 + r)$ free arcs cover $[n] \setminus S$ and may hit $S$ ($F(2n - 2s - 4 + 2r, n - s, s)$ ways).
- For $s \in \{3, 4\}$, bounding the internal factor via (2) at $r=\lambda$ and the external factor via (3) + Lemma 2(3) at $k = n - s \ge 3996$ gives ratio to (4) equal to $O(n^{-4}) < 10^{-11}$.
- For $5 \le s \le 0.02n$, using (2) at $r=\lambda$ internally and (3) + Lemma 2(3) at $k = n - s \ge 0.98n \ge 3920$ externally gives each term bounded by
  $$\binom{2}{r}\frac{C_{\mathrm{up}}}{c_{\mathrm{low}}}\sqrt{\frac{n}{n-s}} \left(\frac{1}{2}\right)^{s-2-r} \left(\frac{2s-2r}{1.96n - 4}\right)^{s-r+2} e^{s\lambda} \le 1.13 \binom{2}{r} (0.5)^{s-2-r} (0.0205)^{s-r+2} e^{s\lambda},$$
  summing to $< 7 \times 10^{-6} < 10^{-4}$.
- For $0.02n < s \le \lfloor n/2 \rfloor$, using (2) at $r = \lambda$ internally for $F(2s-2r, s-2, 2)$ and $r_s = \lambda(1 - 1.3s/n)$ externally for $F(2n-2s-4+2r, n-s, s)$ yields the same exponential rate $f_{\mathrm{sink}}(s/n) \le -0.05$ per $n$ (with prefactor $\le 16(2n+1)\frac{\sqrt{n}}{c_{\mathrm{low}}}\binom{2}{r}(r_s/\lambda)^{4-2r} \le 100(2n+1)\sqrt{n}$), giving $\le \mathrm{poly}(n)\exp(-0.05n) \le \mathrm{poly}(n)\exp(-0.10 s)$, summing to $< 10^{-60} < 10^{-5}$.
Thus $\Sigma_{1b} < 0.001$.

### Case 2a: Source $S$ with $S \cap \{1, 2\} = \emptyset$ ($1 \le s \le \lfloor n/2 \rfloor$)
Because $1, 2 \notin S$ and both send edges to $a, b$, a source $S$ must satisfy $a, b \notin S$ as well, leaving $\binom{n-4}{s}$ choices for $S$. Let $M$ be the number of arcs leaving $S$ into $[n] \setminus S$. For $S$ to be strongly connected, every vertex of $S$ must have in-degree $\ge 1$ inside $S$ and (for $s \ge 2$, and for $s = 1$ since $\{1, 2\}$ cannot hit $S$) every vertex of $S$ must keep at least $1$ outgoing arc inside $S$ (for $s = 1$, $S = \{v\}$ needs $\ge 1$ self-loop). Thus $0 \le M \le s$, with at most $\binom{s}{M} 2^M$ choices of which $M$ edge slots leave $S$, and at most $T(2s - M, s)$ internal choices. Outside $S$, the $2n - 4 - 2s + M$ arcs (from $([n]\setminus\{1,2\})\setminus S$ plus the $M$ leaving arcs from $S$) must cover $([n] \setminus S) \setminus \{a, b\}$ (size $n - 2 - s$) and may hit $\{a, b\}$, giving **exact** external count $F(2n - 4 - 2s + M, n - 2 - s, 2)$.
- For $1 \le s \le 4$: let $c_{\mathrm{scc}}(s, M)$ be the exact number of strongly connected internal configurations on $[s]$ with $M$ specified leaving slots (exhaustive enumeration in `verify.py` gives:
  $s=1$: $[1, 2]$; $s=2$: $[9, 12, 4]$; $s=3$: $[296, 372, 144, 16]$; $s=4$: $[20958, 26304, 11376, 1920, 96]$).
  Bounding $F(2n - 4 - 2s + M, n - 2 - s, 2)$ via (3) and Lemma 2(3) ($k = n - 2 - s \ge 3994$) and dividing by (4) gives a uniform bound over all $n \ge 4000$:
  $$\Sigma_{2a,\le 4} \le \frac{C_{\mathrm{up}}}{c_{\mathrm{low}}} \sqrt{\frac{4000}{3994}} \sum_{s=1}^{4} \sum_{M=0}^{s} \frac{c_{\mathrm{scc}}(s, M)}{s! \, 2^{2s - M} (1 - \frac{11}{8000})^{2s-M} 4000^{s-M}} \frac{\lambda^{2s-M}}{(e^\lambda - 1)^s} < 0.581.$$
- For $5 \le s \le 15$: bounding $T(2s - M, s)$ via (2) with $r_M = \lambda(1 - M/s)$ (and exact $T(s, s) = s!$ for $M = s$) and $\binom{n-4}{s}\frac{(2n-4-2s+M)!}{(2n-4)!} \le \frac{1}{2^s s!}\prod_{j=0}^{s-M-1}\frac{1}{(1.96 - 4/4000)n}$, direct rational summation gives $\Sigma_{2a, 5..15} < 0.042$.
- For $16 \le s \le 0.02 n$: using $\binom{n-4}{s}\frac{(2n-4-2s+M)!(2s-M)!}{(2n-4)!} \le 2^{-s} \varepsilon_{0.02}^{s-M}$ with $\varepsilon_{0.02} = \frac{0.04}{1.96 - 4/4000}$, and $\binom{s}{M} \le e^{s H(M/s)}$, every term is bounded by $\frac{C_{\mathrm{up}}}{c_{\mathrm{low}}} \sqrt{\frac{4000}{3916}} e^{s f_{\mathrm{mid}}(M/s)}$, where for $p = M/s \in [0, 1]$ (with $0\ln 0 := 0$ and $\frac{e^r-1}{r}\big|_{r=0} := 1$),
  $$f_{\mathrm{mid}}(p) := -\ln 2 - p\ln p - 2(1-p)\ln(1-p) + p\ln 2 + (1-p)\ln\varepsilon_{0.02} + \ln\frac{e^{\lambda(1-p)}-1}{\lambda(1-p)} - \ln\frac{e^\lambda - 1}{\lambda}.$$
  Interval checking on $p \in [0, 1]$ proves $f_{\mathrm{mid}}(p) \le -0.70$ ($e^{-0.70} < 0.497$), so $\Sigma_{2a, 16..0.02n} \le 1.13 \sum_{s \ge 16} (s+1) e^{-0.70 s} < 0.001$.
- For $0.02n < s \le \lfloor n/2 \rfloor$: using $\binom{n}{s} \le e^{n H(s/n)}$, $\binom{2n}{2s-M} \ge \frac{1}{2n+1}e^{2n H((2s-M)/(2n))}$, and the boundary ratio $\frac{\binom{n-4}{s}}{\binom{2n-4}{2s-M}} \le 16 \frac{\binom{n}{s}}{\binom{2n}{2s-M}}$, each $(s, M)$ term is at most $16(2n+1)\frac{C_{\mathrm{up}}}{c_{\mathrm{low}}}\sqrt{2.01} \exp\bigl(s \, R(\frac{s}{n}, \frac{M}{s})\bigr)$, where for $\alpha \in (0, 1/2]$, $p \in [0, 1]$, and $\beta = \frac{2 - p}{2}$,
  $$R(\alpha, p) := \frac{H(\alpha) - 2H(\beta\alpha)}{\alpha} + H(p) + p\ln 2 - (1-p)\ln(1-p) + \ln\frac{e^{\lambda(1-p)}-1}{\lambda(1-p)} - \ln\frac{e^\lambda - 1}{\lambda}.$$
  Using the exact derivative $\frac{\partial}{\partial \alpha}\frac{H(\alpha)-2H(\beta\alpha)}{\alpha} = \frac{1}{\alpha^2}\ln\frac{1-\alpha}{(1-\beta\alpha)^2}$ (whose sign switches once from $+$ to $-$ at $\frac{2\beta - 1}{\beta^2}$) and monotonicity in $\beta = \frac{2-p}{2}$, interval checking over $p \in [0, 1]$ proves $R(\alpha, p) \le -0.30$ uniformly on $(0, 1/2] \times [0, 1]$. Hence $\Sigma_{2a, >0.02n} \le 16(2n+1)\cdot 1.6 \sum_{s > 0.02n} (s+1)e^{-0.30 s} < 0.003$ for all $n \ge 4000$.

### Case 2b: Source $S$ with $S \cap \{1, 2\} \neq \emptyset$ ($3 \le s \le \lfloor n/2 \rfloor$)
If $S$ is strongly connected and $1 \in S$ (say), then $1$ must have an outgoing edge inside $S$, so $S \cap \{a, b\} \neq \emptyset$. Because $2$ also sends edges to both $a$ and $b$, no edge from $2$ may enter $S$ if $S$ is a source, forcing $2 \in S$ as well! Symmetrically, $S \cap \{1, 2\} \neq \emptyset$ forces **both** $1, 2 \in S$ ($r = 2$) and $q := |S \cap \{a, b\}| \in \{1, 2\}$, so $s \ge 2 + q \ge 3$. There are $\binom{2}{q}\binom{n-4}{s-2-q}$ choices for $S$. Since each of the $s - 2$ vertices in $S \setminus \{1, 2\}$ keeps $\ge 1$ outgoing edge in $S$, at most $M \le s - 2$ free arcs leave $S$ ($\le \binom{s-2}{M} 2^M$ slot choices), while the remaining $2s - 4 - M$ arcs of $S \setminus \{1, 2\}$ cover $S \setminus \{a, b\}$ (size $s - q$) and may hit $S \cap \{a, b\}$ (size $q$), giving $\le F(2s - 4 - M, s - q, q)$ choices (note $2s - 4 - M \ge s - q$). Outside $S$, the $2(n-s)$ free arcs of $[n]\setminus S$ plus the $M$ free leaving arcs from $S$ (while the $2(2-q)$ fixed arcs from $\{1, 2\}$ hit $\{a, b\} \setminus S$ deterministically) must cover $([n]\setminus S) \setminus \{a, b\}$ (size $n - s - (2 - q)$) and may hit $\{a, b\} \setminus S$ (size $2 - q$), giving at most $F(2n - 2s + M, n - s - (2 - q), 2 - q)$ choices.
- For $3 \le s \le 0.02n$: bounding the external factor via (3) + Lemma 2(3) at $k = n - s - (2-q) \ge 3918$ and the internal factor via $F(k, k, q) = k!$ when $2s - 4 - M = s - q$, or via (2) with saddle parameter $r_M = \lambda(1 - M/s)$ when $2s - 4 - M > s - q$, and using $\binom{n-4}{s-2-q}\frac{(2s-4-M)!(2n-2s+M)!}{(2n-4)!} \le 2^{-(s-2-q)} \bigl(\frac{2s-4-M}{1.96n - 4}\bigr)^{s - 2 + q - M}$ ($s - 2 + q - M \ge q \ge 1$), direct summation gives $< 0.001$ (indeed $< 10^{-3}$ for $s \in \{3, 4\}$ and $< 10^{-7}$ overall).
- For $0.02n < s \le \lfloor n/2 \rfloor$: using the same $r_M = \lambda(1 - M/s)$ internal bound and (3) + Lemma 2(3) external bound, note that $e^{q(r_M-\lambda)} \le 1$ and comparing $\bigl(\frac{e^{r_M}-1}{e^\lambda-1}\bigr)^{s-q}$ against Case 2a's $\bigl(\frac{e^{r_M}-1}{e^\lambda-1}\bigr)^s$ leaves $\bigl(\frac{r_M}{\lambda}\bigr)^4 \bigl(\frac{e^\lambda-1}{e^{r_M}-1}\bigr)^q = \bigl(\frac{r_M}{e^{r_M}-1}\bigr)^q \bigl(\frac{e^\lambda-1}{\lambda}\bigr)^q \bigl(\frac{r_M}{\lambda}\bigr)^{4-q} \le \bigl(\frac{e^\lambda-1}{\lambda}\bigr)^q$ (with $\frac{e^\lambda-1}{\lambda} < 2.47$). Combining with $\binom{n-4}{s-2-q} \le \binom{n}{s}$ and $\frac{1}{(2s-M)^{\underline{4}}} \le (s-1)^{-4}$, and summing $\binom{2}{q}$ over $q \in \{1, 2\}$, gives at most $\sum_{q=1}^2 \binom{2}{q}\frac{16 n^4}{(n-s)^{2+q} s^{2-q}}\bigl(\frac{e^\lambda-1}{\lambda}\bigr)^q < 6500$ times the Case 2a $(s, M)$ bound. Interval checking on $(0, 0.10] \times [0, 1]$ shows $R(\alpha, p) \le -0.60$ (for $0.02n < s \le 0.10n$, where $s \ge 81$, giving $< 2 \times 10^{-10}$), while for $s > 0.10n \ge 400$ one has $e^{-0.30 s} \le e^{-120}$ (giving $< 2 \times 10^{-40}$).
Thus $\Sigma_{2b} < 0.002$ uniformly for all $n \ge 4000$.

Summing all four cases gives, for every $n \ge 4000$,
$$\mathbb{P}_n(G \notin \mathrm{SCC}_n \mid \mathcal{T}) \le \Sigma_{1a} + \Sigma_{1b} + \Sigma_{2a} + \Sigma_{2b} < 0.64 \implies \mathbb{P}_n(G \in \mathrm{SCC}_n \mid \mathcal{T}) \ge \frac{36}{100}. \tag{5}$$

---

## 5. First and Second Moments and Conclusion

1. **First moment of $Z = N(G)\mathbf{1}_{\{G \in \mathrm{SCC}_n\}}$:** There are $\binom{n}{2}\binom{n-2}{2} \cdot 4 = n(n-1)(n-2)(n-3)$ ways to choose a clean twin pair $\{u, v\}$, distinct targets $\{a, b\} \subset [n] \setminus \{u, v\}$, and ordered pairs $(a_u, b_u), (a_v, b_v) \in \{(a,b),(b,a)\}^2$. For each choice, the event has cardinality $|\mathcal{T}|$, and at least $\frac{36}{100}|\mathcal{T}|$ of those graphs lie in $\mathrm{SCC}_n$ by (5). Using $T(2n, n) \le \frac{C_{\mathrm{up}}}{\sqrt{n}}\frac{(2n)!}{\lambda^{2n}}(e^\lambda - 1)^n$ from Lemma 2(3) and (4), for all $n \ge 4000$,
   $$\mathbb{E}_n[Z] \ge \frac{36}{100} \cdot n(n-1)(n-2)(n-3) \frac{(2n-4)!}{(2n)!} \lambda^4 \left(\frac{e^\lambda}{e^\lambda - 1}\right)^2 \frac{c_{\mathrm{low}}}{C_{\mathrm{up}}} \ge \frac{36}{100} \left(1 - \frac{3}{4000}\right)^3 \frac{\lambda^2}{4} \frac{c_{\mathrm{low}}}{C_{\mathrm{up}}} \ge \frac{20}{100}.$$

2. **Second moment $\mathbb{E}_n[N(G)^2]$:** Note $\mathbb{E}_n[N^2] = \mathbb{E}_n[N] + \mathbb{E}_n[N(N-1)]$.
   - First, $\mathbb{E}_n[N] \le n^4 \frac{(2n-4)!}{(2n)!} \lambda^4 \left(\frac{e^\lambda}{e^\lambda - 1}\right)^2 \frac{C_{\mathrm{up}}}{c_{\mathrm{low}}} \sqrt{\frac{n}{n-2}} \le \frac{\lambda^2}{4} \frac{C_{\mathrm{up}}}{c_{\mathrm{low}}} \frac{1}{(1 - \frac{3}{8000})^4} \sqrt{\frac{4000}{3998}} < 0.72$.
   - Ordered pairs $(P_1, P_2)$ of distinct clean twin pairs either share $1$ vertex ($|P_1 \cap P_2| = 1$, forcing $3$ vertices to have the same out-multiset $\{a,b\}$: $\le n^5 \cdot 8 \cdot F(2n-6, n-2, 2)/T(2n,n) = O(1/n) < 0.005$) or are disjoint ($|P_1 \cap P_2| = 0$). In the disjoint case, let $t = |\{a_1,b_1\} \cup \{a_2,b_2\}| \in \{2, 3, 4\}$: the $t = 2, 3$ overlap configurations contribute $O(n^{-2}) + O(n^{-1}) < 0.005$, while the main $t = 4$ term has at most $\binom{n}{2}\binom{n-2}{2}^3 \cdot 16 \cdot F(2n - 8, n - 4, 4)/T(2n, n) \le \left(\frac{\lambda}{2}\right)^4 \frac{C_{\mathrm{up}}}{c_{\mathrm{low}}} \frac{\sqrt{4000/3996}}{(1 - 7/8000)^8} < 0.46$.
   Hence $\mathbb{E}_n[N(G)^2] < 0.72 + 0.01 + 0.46 = 1.19 \le \frac{120}{100}$ for all $n \ge 4000$.

Substituting both bounds into (1) proves that for all $n \ge 4000$,
$$\Pr(G \text{ is totally simple} \mid G \in \mathrm{SCC}_n) \le 1 - \frac{(20/100)^2}{120/100} = \frac{29}{30},$$
disproving `conj:typical-total-simplicity` at $k = 2$. $\blacksquare$

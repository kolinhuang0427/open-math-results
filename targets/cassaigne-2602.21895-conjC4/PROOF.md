# Proof of Dekking's Conjecture $(C_4)$ for $\mathbf{t}_{3/2}$ and $\mathbf{t}'$ (`arXiv:2602.21895v1`)

**Theorem (Conjecture $(C_4)$ of Dekking, restated in `arXiv:2602.21895v1`, Section 1.4).**
Let $\mathbf{t}_{3/2} = (t_m)_{m \ge 0} \in \{{\tt 0}, {\tt 1}\}^{\mathbb{N}}$ be the Thue--Morse word in base $3/2$ ($t_0 = {\tt 0}$, $t_{3m} = t_{3m+1} = t_{2m}$, $t_{3m+2} = 1 - t_{2m+1}$ for all $m \ge 0$), and let $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (`A357448`, Lemma `lem:morphic_image`), where $\varphi({\tt 0}) = {\tt 010}$ and $\varphi({\tt 1}) = {\tt 101}$. Then:
1. For every finite word $w \in \{{\tt 0}, {\tt 1}\}^*$, the frequencies $\mathrm{freq}_{\mathbf{t}_{3/2}}(w)$ and $\mathrm{freq}_{\mathbf{t}'}(w)$ exist and are rational numbers (computed explicitly by recursion on $|w|$).
2. For every finite word $w \in \{{\tt 0}, {\tt 1}\}^*$, $\mathrm{freq}_{\mathbf{t}_{3/2}}(w) = \mathrm{freq}_{\mathbf{t}_{3/2}}(w^R) = \mathrm{freq}_{\mathbf{t}_{3/2}}(\bar{w})$ and $\mathrm{freq}_{\mathbf{t}'}(w) = \mathrm{freq}_{\mathbf{t}'}(w^R) = \mathrm{freq}_{\mathbf{t}'}(\bar{w})$, where $w^R$ is the reversal of $w$ and $\bar{w}$ is the bit-wise complement.

In particular, this settles the open length-$2$ factor frequencies noted in Section 7 of `arXiv:2602.21895v1`:
$$\mathrm{freq}_{\mathbf{t}_{3/2}}({\tt 00}) = \mathrm{freq}_{\mathbf{t}_{3/2}}({\tt 11}) = \frac{3}{10}, \quad \mathrm{freq}_{\mathbf{t}_{3/2}}({\tt 01}) = \mathrm{freq}_{\mathbf{t}_{3/2}}({\tt 10}) = \frac{1}{5}, \quad \mathrm{freq}_{\mathbf{t}'}({\tt 01}) = \mathrm{freq}_{\mathbf{t}'}({\tt 10}) = \frac{2}{5}, \quad \mathrm{freq}_{\mathbf{t}'}({\tt 00}) = \mathrm{freq}_{\mathbf{t}'}({\tt 11}) = \frac{1}{10}.$$

---

## 1. Filtered Factor Frequencies and Desubstitution Recurrence

For $L \ge 1$, $w \in \{0,1\}^L$, $n \ge 0$, $k \in \mathbb{Z}$, and $N \ge 1$, define the counting function and normalized filtered density
$$C_n(w, k, N) := \#\bigl\{0 \le m < N : m \equiv k \pmod{2^n},\ \mathbf{t}_{3/2}[m, m+L) = w\bigr\}, \qquad \nu_n(w, k, N) := \frac{2^n}{N} C_n(w, k, N).$$
Note that $0 \le \nu_n(w, k, N) \le 1 + \frac{2^n}{N}$ for all $N \ge 1$.

**Definition (Desubstitution preimage maps $\psi_0, \psi_1, \psi_2$).**
Define $S : \mathbb{Z} \to \mathbb{Z}$ and $\varepsilon : \mathbb{Z} \to \{0,1\}$ by
$$S(3q) = S(3q+1) = 2q, \quad S(3q+2) = 2q+1, \qquad \varepsilon(3q) = \varepsilon(3q+1) = 0, \quad \varepsilon(3q+2) = 1,$$
so that $t_m = t_{S(m)} \oplus \varepsilon(m)$ for all $m \ge 0$ (where $\oplus$ denotes addition mod $2$). For $r \in \{0,1,2\}$ and $w = (w_0, \dots, w_{L-1}) \in \{0,1\}^L$ ($L \ge 2$), consider the interval $I_r := \{r, r+1, \dots, r+L-1\}$ and its image $S(I_r) = [a_r, b_r] \cap \mathbb{Z}$ (with $a_0 = a_1 = 0$ and $a_2 = 1$). We say $\psi_r(w)$ is *defined* if $w_i \oplus \varepsilon(r+i) = w_{i'} \oplus \varepsilon(r+i')$ whenever $S(r+i) = S(r+i')$ (i.e., $w_i = w_{i+1}$ whenever $\{r+i, r+i+1\} = \{3q, 3q+1\} \subseteq I_r$); when defined, set $\psi_r(w) \in \{0,1\}^{\ell_r(L)}$ (of length $\ell_r(L) = b_r - a_r + 1$) to be the unique word $u$ indexed by $[a_r, b_r]$ satisfying $u_{S(r+i)-a_r} = w_i \oplus \varepsilon(r+i)$ for $0 \le i < L$.

**Lemma 1 (Preimage lengths).**
1. For all $L \ge 2$, $\ell_0(L) < L$. Specifically, $\ell_0(2) = 1$ and $\ell_0(3) = 2$.
2. $\ell_1(2) = 2$, $\ell_1(3) = 3$, and $\ell_1(L) < L$ for all $L \ge 4$.
3. $\ell_2(2) = 2$, and $\ell_2(L) < L$ for all $L \ge 3$.

*Proof.*
- For $r=0$, write $L-1 = 3q + s$ ($s \in \{0,1,2\}$). Then $b_0 = 2q$ ($s \in \{0,1\}$) or $2q+1$ ($s=2$), so $\ell_0(L) = 2q+1$ ($s \in \{0,1\}$) or $2q+2$ ($s=2$). If $L=2$ ($q=0, s=1$), $\ell_0(2)=1$; if $L=3$ ($q=0, s=2$), $\ell_0(3)=2$. For $L \ge 4$ ($q \ge 1$), if $s \in \{0,1\}$ then $\ell_0(L) = 2q+1 < 3q+1 \le L$, while if $s=2$ then $\ell_0(L) = 2q+2 < 3q+3 = L$.
- For $r=1$, write $L = 3q+s$ ($s \in \{0,1,2\}$). Then $\ell_1(L) = 2q+1$ ($s \in \{0,1\}$) or $2q+2$ ($s=2$). Thus $\ell_1(2)=2$, $\ell_1(3)=3$, $\ell_1(4)=3 < 4$, $\ell_1(5)=4 < 5$, and for $L \ge 6$ ($q \ge 2$): if $s \in \{0,1\}$ then $\ell_1(L) = 2q+1 < 3q \le L$, while if $s=2$ then $\ell_1(L) = 2q+2 < 3q+2 = L$.
- For $r=2$, write $L+1 = 3q+s$ ($s \in \{0,1,2\}$). Since $a_2 = 1$, $\ell_2(L) = 2q$ ($s \in \{0,1\}$) or $2q+1$ ($s=2$). Thus $\ell_2(2)=2$, $\ell_2(3)=2 < 3$, $\ell_2(4)=3 < 4$, and for $L \ge 5$ ($q \ge 2$): if $s \in \{0,1\}$ then $\ell_2(L) = 2q < 3q-1 \le L$, while if $s=2$ then $\ell_2(L) = 2q+1 < 3q+1 = L$. $\square$

**Lemma 2 (Exact desubstitution counting recurrence).**
Let $q_n \in \mathbb{Z}$ satisfy $3q_n \equiv 1 \pmod{2^{n+1}}$, and set $k_0 := 2q_n k$, $k_1 := 2q_n k - 2q_n$, $k_2 := 2q_n k - q_n$. Then for all $L \ge 2$, $w \in \{0,1\}^L$, $n \ge 0$, $k \in \mathbb{Z}$, and $N \ge 3$,
$$C_n(w, k, N) = \sum_{r=0}^2 \mathbf{1}_{\psi_r(w)\text{ defined}}\, C_{n+1}\bigl(\psi_r(w),\, k_r,\, \lfloor 2N/3 \rfloor\bigr) + E, \qquad |E| \le 3L + 3.$$
Consequently,
$$\nu_n(w, k, N) = \frac{1}{3} \sum_{r=0}^2 \mathbf{1}_{\psi_r(w)\text{ defined}}\, \nu_{n+1}\bigl(\psi_r(w),\, k_r,\, \lfloor 2N/3 \rfloor\bigr) + O_L\!\left(\frac{2^n}{N}\right).$$

*Proof.*
Every $m \in [0, N)$ has the unique form $m = 3j + r$ with $r \in \{0,1,2\}$ and $0 \le j < \lfloor (N-r+2)/3 \rfloor$. As in `2602.21895v1` (eq. `eq:mod2m`):
- For $r \in \{0,1\}$, $3j + r \equiv k \pmod{2^n} \iff j \equiv q_n(k-r) \pmod{2^n} \iff 2j \equiv 2q_n k - 2q_n r \pmod{2^{n+1}}$. Since $k_r$ is even, any $m' \equiv k_r \pmod{2^{n+1}}$ is even ($m'=2j$).
- For $r = 2$, $3j + 2 \equiv k \pmod{2^n} \iff 2j + 1 \equiv 2q_n k - 4q_n + 1 \equiv 2q_n k - q_n = k_2 \pmod{2^{n+1}}$ since $3q_n \equiv 1 \pmod{2^{n+1}}$. Since $k_2$ is odd, any $m' \equiv k_2 \pmod{2^{n+1}}$ is odd ($m'=2j+1$).

For $0 \le j < \lfloor 2N/3 \rfloor / 2 - L$ (empty when $N < 3L$, in which case every $j$ falls into the boundary error), we have $3j+r < N$ and the factor $\mathbf{t}_{3/2}[3j+r, 3j+r+L) = w$ holds if and only if $\psi_r(w)$ is defined and $\mathbf{t}_{3/2}[2j+a_r, 2j+a_r+\ell_r(L)) = \psi_r(w)$, where $2j+a_r$ is $2j$ for $r \in \{0,1\}$ and $2j+1$ for $r=2$. The boundary discrepancy between $0 \le j < \lfloor (N-r+2)/3 \rfloor$ and $0 \le 2j + a_r < \lfloor 2N/3 \rfloor$ affects at most $L + 1$ values of $j$ per residue $r$, giving $|E| \le 3L + 3$. Dividing by $N/2^n$ and using $\frac{\lfloor 2N/3 \rfloor / 2^{n+1}}{N / 2^n} = \frac{1}{3} + O(1/N)$ yields the recurrence for $\nu_n$. $\square$

---

## 2. Existence, Constancy in $k$, and Rationality of All Factor Frequencies in $\mathbf{t}_{3/2}$

Define $f : \{0,1\}^* \to \mathbb{Q} \cap [0,1]$ by setting $f(\varepsilon) := 1$ for the empty word ($L = 0$, where $\mathrm{freq}_{\mathbf{t}_{3/2}}(\varepsilon) = \mathrm{freq}_{\mathbf{t}'}(\varepsilon) = 1 = f(\varepsilon^R) = f(\bar{\varepsilon})$ trivially) and recursively for $L = |w| \ge 1$:
- For $L = 1$: $f({\tt 0}) = f({\tt 1}) = \frac{1}{2}$.
- For $L = 2$: $f({\tt 00}) = f({\tt 11}) = \frac{3}{10}$, $f({\tt 01}) = f({\tt 10}) = \frac{1}{5}$.
- For $L = 3$, writing $w = (a,b,c)$ and $w' = (a, 1-b, c)$ (note $\psi_1(w) = w'$), let
  $$g(w) := \frac{1}{3}\mathbf{1}_{a=b} f(a, 1-c) + \frac{1}{3}\mathbf{1}_{b=c} f(1-a, b), \qquad f(w) := \frac{9}{8}\left(g(w) + \frac{1}{3} g(w')\right).$$
- For $L \ge 4$:
  $$f(w) := \frac{1}{3} \sum_{r=0}^2 \mathbf{1}_{\psi_r(w)\text{ defined}}\, f(\psi_r(w)).$$

By Lemma 1, this recursion terminates and produces rational numbers in $[0,1]$. Direct substitution shows that for $L = 2$ and $L = 3$, $f$ also satisfies the fixed-point equation
$$f(w) = \frac{1}{3} \sum_{r=0}^2 \mathbf{1}_{\psi_r(w)\text{ defined}}\, f(\psi_r(w)) \qquad (\forall\, |w| \ge 2).$$
(Explicitly: for $L=2$, $\frac{1}{3}(\frac{1}{2}+\frac{1}{5}+\frac{1}{5}) = \frac{3}{10}$ and $\frac{1}{3}(0+\frac{3}{10}+\frac{3}{10}) = \frac{1}{5}$; for $L=3$, $f(w) - \frac{1}{3}f(w') = g(w)$ holds because $f(w') - \frac{1}{3}f(w) = g(w')$ has unique solution $f(w) = \frac{9}{8}(g(w)+\frac{1}{3}g(w'))$.)

**Proposition 1.** *For every $L \ge 1$, every $w \in \{0,1\}^L$, every $n_0 \ge 0$, and every $k_0 \in \mathbb{Z}$,*
$$\lim_{N \to \infty} \nu_{n_0}(w, k_0, N) = f(w).$$

*Proof.* We proceed by strong induction on $L \ge 1$.
- **Base case $L = 1$:** By Theorem `thm:existence_freqs_iff_mun_exist` of `arXiv:2602.21895v1`, $\lim_{N\to\infty} \frac{1}{N} C_{n_0}(a, k_0, N) = 2^{-n_0-1}$, so $\lim_{N\to\infty} \nu_{n_0}(a, k_0, N) = \frac{1}{2} = f(a)$.
- **Inductive step ($L \ge 2$):** Assume the proposition holds for all lengths $< L$. Fix any $n_0 \ge 0$, $k_0 \in \mathbb{Z}$, $w_0 \in \{0,1\}^L$, and any increasing sequence $(M_t)_{t \ge 0}$ of positive integers. Define $N_{t, n_0} := M_t$ and $N_{t, n+1} := \lfloor 2 N_{t, n} / 3 \rfloor$ for all $n \ge n_0$. For each fixed $n \ge n_0$, $N_{t, n} \to \infty$ as $t \to \infty$, and $\nu_n(w, k, N_{t, n}) \in [0, 1 + 2^n / N_{t,n}]$ is bounded.
  By a diagonal extraction over the countable set $\{ (n, w, k) : n \ge n_0,\, w \in \{0,1\}^L,\, k \in \mathbb{Z} \}$, pass to a subsequence $(t_j)_{j \ge 0}$ along which
  $$\nu_n(w, k) := \lim_{j \to \infty} \nu_n(w, k, N_{t_j, n}) \in [0, 1]$$
  exists for all $n \ge n_0$, $w \in \{0,1\}^L$, $k \in \mathbb{Z}$.
  Passing to the limit $j \to \infty$ in Lemma 2 (for fixed $n \ge n_0$, the $O_L(2^n / N_{t_j, n})$ error tends to $0$), and using the induction hypothesis $\lim_{j \to \infty} \nu_{n+1}(u, k_r, N_{t_j, n+1}) = f(u)$ whenever $|\psi_r(w)| < L$, we obtain
  $$\nu_n(w, k) = \frac{1}{3} \sum_{r : \ell_r(L) < L} \mathbf{1}_{\psi_r(w)\text{ def.}}\, f(\psi_r(w)) + \frac{1}{3} \sum_{r : \ell_r(L) = L} \mathbf{1}_{\psi_r(w)\text{ def.}}\, \nu_{n+1}(\psi_r(w), k_r).$$
  Subtracting the fixed-point identity for $f(w)$ and setting $\Delta_n(w, k) := \nu_n(w, k) - f(w) \in [-1, 1]$ gives
  $$\Delta_n(w, k) = \frac{1}{3} \sum_{r : \ell_r(L) = L} \mathbf{1}_{\psi_r(w)\text{ def.}}\, \Delta_{n+1}(\psi_r(w), k_r).$$
  Let $D_n := \sup_{w \in \{0,1\}^L,\, k \in \mathbb{Z}} |\Delta_n(w, k)| \le 1$.
  - If $L = 2$: at most two terms ($r = 1, 2$) have $\ell_r(2) = 2$, so $D_n \le \frac{2}{3} D_{n+1}$ for all $n \ge n_0$. Thus $D_{n_0} \le (2/3)^m D_{n_0+m} \le (2/3)^m \to 0$, hence $\Delta_{n_0} \equiv 0$.
  - If $L = 3$: only $r = 1$ has $\ell_1(3) = 3$, so $D_n \le \frac{1}{3} D_{n+1}$, hence $D_{n_0} \le (1/3)^m \to 0$ and $\Delta_{n_0} \equiv 0$.
  - If $L \ge 4$: by Lemma 1, no $r \in \{0,1,2\}$ has $\ell_r(L) = L$, so $\Delta_{n_0} \equiv 0$ immediately.

  Therefore $\lim_{j \to \infty} \nu_{n_0}(w_0, k_0, M_{t_j}) = \nu_{n_0}(w_0, k_0) = f(w_0)$. Since every sequence $M_t \to \infty$ admits a subsequence converging to $f(w_0)$, we conclude $\lim_{N \to \infty} \nu_{n_0}(w_0, k_0, N) = f(w_0)$. $\square$

Taking $n_0 = 0, k_0 = 0$ gives $\mathrm{freq}_{\mathbf{t}_{3/2}}(w) = f(w) \in \mathbb{Q}$ for all $w \in \{0,1\}^*$.

---

## 3. Reversal and Complement Symmetries in $\mathbf{t}_{3/2}$

**Proposition 2.** *For every $w \in \{0,1\}^*$, $f(w^R) = f(w)$ and $f(\bar{w}) = f(w)$.*

*Proof.*
For bit-wise complementation, $\psi_r(\bar{w})$ is defined iff $\psi_r(w)$ is defined, in which case $\psi_r(\bar{w}) = \overline{\psi_r(w)}$. Induction on $L$ immediately yields $f(\bar{w}) = f(w)$ (base cases $L=1, 2$ are explicit).

For reversal, fix $L \ge 2$ and choose an integer $M \ge L$. Define the involutions
$$\sigma(m) := 3M + 1 - m, \qquad \tau(j) := 2M - j \qquad (m, j \in \mathbb{Z}).$$
Checking each residue modulo $3$:
- $m = 3q \implies \sigma(m) = 3(M-q) + 1$, so $S(\sigma(m)) = 2(M-q) = \tau(S(m))$ and $\varepsilon(\sigma(m)) = 0 = \varepsilon(m)$;
- $m = 3q+1 \implies \sigma(m) = 3(M-q)$, so $S(\sigma(m)) = 2(M-q) = \tau(S(m))$ and $\varepsilon(\sigma(m)) = 0 = \varepsilon(m)$;
- $m = 3q+2 \implies \sigma(m) = 3(M-q-1)+2$, so $S(\sigma(m)) = 2(M-q-1)+1 = \tau(S(m))$ and $\varepsilon(\sigma(m)) = 1 = \varepsilon(m)$.

Thus $S(\sigma(m)) = \tau(S(m))$ and $\varepsilon(\sigma(m)) = \varepsilon(m)$ for all $m \in \mathbb{Z}$. For any $r \in \{0,1,2\}$, $\sigma$ maps $I_r = [r, r+L-1]$ order-reversingly onto $[3M + 2 - r - L, 3M + 1 - r] = 3M' + I_{r'}$, where $r' := (2 - r - L) \bmod 3 \in \{0,1,2\}$ (and $r \mapsto r'$ is a bijection on $\{0,1,2\}$). Since $\tau$ reverses the order of $S(I_r)$ while preserving equality $S(m_1) = S(m_2)$ and $\varepsilon$, we obtain for every $w \in \{0,1\}^L$:
$$\psi_r(w) \text{ is defined} \iff \psi_{r'}(w^R) \text{ is defined, and in that case } \psi_{r'}(w^R) = (\psi_r(w))^R.$$
We now deduce $f(w^R) = f(w)$ by induction on $L$:
- For $L = 1, 2$: immediate from $f({\tt 0})=f({\tt 1})=1/2$ and $f({\tt 01})=f({\tt 10})=1/5$.
- For $L = 3$: $r'=1$ corresponds to $r=1$ ($2-1-3 \equiv 1 \pmod 3$), while $r \in \{0,2\}$ have $|\psi_r(w)| = 2$. Thus $f(w^R) - f(w) = \frac{1}{3}\bigl(f(\psi_1(w)^R) - f(\psi_1(w))\bigr)$ for all $w \in \{0,1\}^3$; applying this also to $\psi_1(w)$ (since $\psi_1$ is an involution) gives $f(w^R) - f(w) = \frac{1}{9}(f(w^R) - f(w))$, so $f(w^R) = f(w)$.
- For $L \ge 4$: every $\psi_r(w)$ has length $< L$, so by the induction hypothesis $f(\psi_{r'}(w^R)) = f((\psi_r(w))^R) = f(\psi_r(w))$, and summing over $r \in \{0,1,2\}$ gives $f(w^R) = f(w)$. $\square$

---

## 4. Transfer to $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ (Conjecture $(C_4)$)

Recall from `lem:morphic_image` (`2602.21895v1`) that $\mathbf{t}' = \varphi(\mathbf{t}_{3/2})$ with $\varphi({\tt 0}) = {\tt 010}$ and $\varphi({\tt 1}) = {\tt 101}$. Fix any $w \in \{0,1\}^L$ ($L \ge 1$). For $r \in \{0,1,2\}$, let $m_r := \lceil (r + L)/3 \rceil \ge 1$. For any $N \ge L$, write $N = 3M + s$ ($s \in \{0,1,2\}$); decomposing occurrences $0 \le i \le N - L$ of $w$ in $\mathbf{t}'$ by $i = 3m + r$ yields
$$|\mathbf{t}'[0, N)|_w = \sum_{r=0}^2 \sum_{\substack{u \in \{0,1\}^{m_r} \\ \varphi(u)[r, r+L) = w}} C_0(u, 0, M) + O_L(1).$$
Dividing by $N = 3M + s$ and taking $N \to \infty$ (hence $M \to \infty$), Proposition 1 gives
$$\mathrm{freq}_{\mathbf{t}'}(w) = \frac{1}{3} \sum_{r=0}^2 \sum_{\substack{u \in \{0,1\}^{m_r} \\ \varphi(u)[r, r+L) = w}} f(u) \in \mathbb{Q}.$$
Finally, let $r' := 3m_r - (r + L)$. By definition of $m_r = \lceil (r+L)/3 \rceil$, we have $r' \in \{0,1,2\}$, $r' + L = 3m_r - r$ (so $m_{r'} = \lceil (r'+L)/3 \rceil = m_r$), and $r \mapsto r' \equiv -r-L \pmod 3$ is a bijection on $\{0,1,2\}$. Because $\varphi({\tt 0}) = {\tt 010}$ and $\varphi({\tt 1}) = {\tt 101}$ are palindromes, $(\varphi(u))^R = \varphi(u^R)$ for all $u \in \{0,1\}^{m_r}$, so
$$\varphi(u)[r, r+L) = w \iff \varphi(u^R)[r', r'+L) = w^R.$$
Applying Proposition 2 ($f(u^R) = f(u)$ and $f(\bar{u}) = f(u)$, noting $\overline{\varphi(u)} = \varphi(\bar{u})$) yields
$$\mathrm{freq}_{\mathbf{t}'}(w^R) = \mathrm{freq}_{\mathbf{t}'}(w) \qquad \text{and} \qquad \mathrm{freq}_{\mathbf{t}'}(\bar{w}) = \mathrm{freq}_{\mathbf{t}'}(w)$$
for every $w \in \{0,1\}^*$. This completes the proof of Dekking's Conjecture $(C_4)$. $\square$

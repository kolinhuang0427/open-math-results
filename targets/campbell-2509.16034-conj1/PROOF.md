# Proof (Rescoped to Open Problems (c1) and (c2)): Explicit Recursion and Sign Formula for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$

- **Target**: `campbell-2509.16034-conj1` (rescoped per `notes/contest-ruling-audit-3.md`)
- **Source**: John M. Campbell, James Currie, and Narad Rampersad, *Reduced complexities for sequences over finite alphabets*, `arXiv:2509.16034v1` (published in *INTEGERS* 26 (2026), #A34), Section 3 (Conclusion).
- **Claimed New Results**: Strictly the two unsettled Section 3 open problems:
  - **(c1)** Explicit evaluation of the sign of $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$ for all $n \ge 1$ (including the nonzero case).
  - **(c2)** Explicit recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$, full recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$, and $2$-regularity of $(\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n))_{n \ge 1}$.
- **Prior Art Explicitly Credited (Not Claimed)**: In `the-omega-institute/trureturing` (Sept 2026, commits `832f82f782` and `96baee8682`), the odd recurrence $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(2n+1)=\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1)$ (`ThueMorseReducedAbelianOdd.lean`), eq. (11) `displayconjecture` (`ThueMorseReducedAbelianEven.lean`), and non-$k$-automaticity (prose unboundedness argument) were already settled, along with internal private lemmas expressing $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$ as a weighted sum over $[m_n+1, M_n+1]$ and $(R(4n+2)-R(4n)) = (M_{n+1} \bmod 2) - (m_{n+1} \bmod 2)$. As recorded in `Problems/campbell-currie-rampersad-eq-11.md` of that repository, characterizing the individual parities $m_k \bmod 2$ and $M_k \bmod 2$ (needed for the nonzero sign (c1)) and giving an explicit recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$ and full recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$ (c2) remained open.
- **Result Label**: `written proof, pending independent check & audit` (verified computationally up to $n=10000$ and by direct factor enumeration up to $n=120$ in `verify.py`).

---

## 1. Preliminaries and Setup

Following `arXiv:2509.16034v1`:
- $\mathbf{t} = 0110100110010110\cdots$ is the Thue–Morse sequence, indexed from $1$: for $k \ge 1$, $\mathbf{t}_k = s_2(k-1) \bmod 2$, where $s_2(m)$ denotes the sum of binary digits of $m$.
- For a finite nonempty word $w$, $\mathrm{red}(w)$ replaces every maximal run $c\cdots c$ of identical letters with $c$. Over $\{0,1\}$, $\mathrm{red}(w)$ is the alternating word of length $r(w)$ (the number of runs in $w$) beginning with the first letter of $w$.
- For $n \ge 1$, $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$ is the number of equivalence classes of length-$n$ factors of $\mathbf{t}$ under $v \sim_{\mathrm{ab},\mathrm{red}} w \iff |\mathrm{red}(v)| = |\mathrm{red}(w)|$ and $\mathrm{red}(v)$ is a permutation of $\mathrm{red}(w)$.
- Let $\alpha(w) = r(w) - 1$ be the number of alternations (`01` or `10`) in $w$, and let $m_n$ and $M_n$ denote the minimum and maximum of $\alpha(w)$ over all length-$n$ factors $w$ of $\mathbf{t}$.

As proved in Section 2.1 of `arXiv:2509.16034v1`:
1. For every $n \ge 1$ and every $r \in [m_n+1, M_n+1]$, there exist length-$n$ factors of $\mathbf{t}$ with $r$ runs starting with $0$ and starting with $1$.
2. By Lemma 2 (`\ref{tm_max_min}`) of `arXiv:2509.16034v1`, for all $j \ge 2$:
   $$m_{2j} = 2j - 1 - M_{j+1}, \qquad M_{2j} = 2j - 1 - m_j,$$
   $$m_{2j+1} = 2j - M_{j+1}, \qquad M_{2j+1} = 2j - m_{j+1}.$$
3. By Lemma 3 (`\ref{tm_mod4}`) of `arXiv:2509.16034v1`, for all $n \ge 1$:
   $$m_{4n} = 2n - 1 + m_{n+1}, \qquad M_{4n} = 2n + M_{n+1},$$
   $$m_{4n+2} = 2n + m_{n+1}, \qquad M_{4n+2} = 2n + 1 + M_{n+1}.$$
4. Directly from $\mathbf{t} = 01101001\cdots$, $(m_1, M_1) = (0,0)$, $(m_2, M_2) = (0,1)$, and $(m_3, M_3) = (1,2)$.

---

## 2. Structural Lemma: Weighted Run-Count Formula

**Lemma 1.** *For every integer $n \ge 1$,*
$$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n) = \sum_{r = m_n + 1}^{M_n + 1} \bigl(1 + (r \bmod 2)\bigr) = \frac{3}{2}(M_n - m_n + 1) + \frac{(-1)^{m_n} + (-1)^{M_n}}{4}.$$

*Proof.* Every length-$n$ factor $w$ of $\mathbf{t}$ maps under $\mathrm{red}$ to an alternating binary word of length $r \in [m_n + 1, M_n + 1]$, and every pair $(\text{first letter}, r) \in \{0,1\} \times [m_n + 1, M_n + 1]$ is realized.
- If $r = 2k$ is even, both $(01)^k$ and $(10)^k$ have Parikh vector $(k, k)$, giving $1$ abelian class.
- If $r = 2k+1$ is odd, $(01)^k 0$ has Parikh vector $(k+1, k)$ while $(10)^k 1$ has $(k, k+1)$, giving $2$ distinct abelian classes.

Summing $1 + (r \bmod 2)$ over $r \in [m_n+1, M_n+1]$ gives the first equality; checking the four parity cases of $(m_n, M_n)$ yields the closed form, as the count of odd integers in $[m_n+1, M_n+1]$ is $\frac{M_n - m_n + 1}{2} + \frac{(-1)^{m_n} + (-1)^{M_n}}{4}$. $\square$

---

## 3. Resolution of Open Problem (c2): Explicit Recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$, Full Recursion, and $2$-Regularity

Let $a_k = m_k \bmod 2 \in \{0,1\}$ and $b_k = M_k \bmod 2 \in \{0,1\}$ for all $k \ge 1$.

**Theorem 1 (Explicit Recursion & $2$-Regularity — Open Problem (c2)).**
1. *For all $n \ge 1$,*
   $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + a_{n+1},$$
   $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + b_{n+1},$$
   *together with $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(2n+1) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1)$ for all $n \ge 0$ (previously settled in `trureturing`) and initial values $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(1) = 2$, $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(2) = 3$.*
2. *The parity sequences $(a_k)_{k \ge 1}$ and $(b_k)_{k \ge 1}$ satisfy $(a_1, b_1) = (0,0)$, $(a_2, b_2) = (0,1)$, $(a_3, b_3) = (1,0)$, and the explicit coupled mod-$2$ recurrences for all $j \ge 2$:*
   $$a_{2j} \equiv 1 - b_{j+1} \pmod 2, \qquad b_{2j} \equiv 1 - a_j \pmod 2,$$
   $$a_{2j+1} \equiv b_{j+1} \pmod 2, \qquad b_{2j+1} \equiv a_{j+1} \pmod 2.$$
   *In particular, $(a_k)_{k \ge 1}$ and $(b_k)_{k \ge 1}$ are $2$-automatic sequences (the shifted sequences $a'_n := a_{n+1}$ and $b'_n := b_{n+1}$ share a $2$-kernel of size $8$), so parts (1)–(2) give a complete $O(\log n)$-step recursion for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n)$.*
3. *The sequence $(\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n))_{n \ge 1}$ is $2$-regular.*

*Proof.*
1. By Lemma 3 (`\ref{tm_mod4}`), for all $n \ge 1$:
   - $[m_{4n}+1, M_{4n}+1] = [2n + m_{n+1}, \, 2n + 1 + M_{n+1}] = \{2n + m_{n+1}\} \sqcup (2n + [m_{n+1}+1, M_{n+1}+1])$. Since adding $2n$ preserves parity, Lemma 1 gives
     $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + ((2n + m_{n+1}) \bmod 2) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + a_{n+1}.$$
   - $[m_{4n+2}+1, M_{4n+2}+1] = [2n + 1 + m_{n+1}, \, 2n + 2 + M_{n+1}] = (2n + [m_{n+1}+1, M_{n+1}+1]) \sqcup \{2n + 2 + M_{n+1}\}$, so Lemma 1 gives
     $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + ((2n + 2 + M_{n+1}) \bmod 2) = \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n+1) + 1 + b_{n+1}.$$
   The odd recurrence for $n \ge 2$ likewise follows from Lemma 2 via the parity-preserving bijection $r \mapsto 2n+2-r$ on $[m_{n+1}+1, M_{n+1}+1]$, and for $n=0,1$ by $\rho(1)=2$ and $\rho(3)=3=\rho(2)$.
2. Reducing Lemma 2 (`\ref{tm_max_min}`) modulo $2$ immediately gives the four recurrences for $j \ge 2$:
   $m_{2j} = 2j - 1 - M_{j+1} \equiv 1 - b_{j+1}$, $M_{2j} = 2j - 1 - m_j \equiv 1 - a_j$, $m_{2j+1} = 2j - M_{j+1} \equiv b_{j+1}$, and $M_{2j+1} = 2j - m_{j+1} \equiv a_{j+1} \pmod 2$.
   To show $2$-automaticity rigorously without relying on a finite search, let $u_k := (a_{k+1}, b_{k+1}) \in \{0,1\}^2$ and $v_k := (a_k, b_k) \in \{0,1\}^2$ for $k \ge 1$. Expressing $2k+r$ ($r \in \{0,1\}$) for $k \ge 2$:
   - $a'_{2k} = a_{2k+1} = b_{k+1} = b'_k$, $b'_{2k} = b_{2k+1} = a_{k+1} = a'_k$;
   - $a'_{2k+1} = a_{2(k+1)} = 1 - b_{k+2} = 1 - b'_{k+1}$, $b'_{2k+1} = b_{2(k+1)} = 1 - a_{k+1} = 1 - a'_k$.
   Notice every step either maps $k \mapsto k$ or $k \mapsto k+1$ while reading the least significant bit of $k$! Iterating this on $(a'_{2^e k + r}, b'_{2^e k + r})$ only ever produces expressions in $\{a'_k, b'_k, a'_{k+1}, b'_{k+1}, 1-a'_k, 1-b'_k, 1-a'_{k+1}, 1-b'_{k+1}\}$ (together with finitely many boundary adjustments at $k=1$): explicitly, the finite span of pairs $(a'_{2^e k + r}, b'_{2^e k + r})$ (modulo equality on $k \ge 1$) is closed under $k \mapsto 2k$ and $k \mapsto 2k+1$. In fact, $(a'_k)$ and $(b'_k)$ each have a $2$-kernel of size $8$ (checked in `verify.py` and verified algebraically by closing the transition system on $\{a'_k, b'_k, a'_{k+1}, b'_{k+1}, 1-a'_k, 1-b'_k, 1-a'_{k+1}, 1-b'_{k+1}\}$: e.g., $(1-b'_{k+1})|_{k\mapsto 2k} = 1-b'_{2k+1} = a'_k$ and $(1-b'_{k+1})|_{k\mapsto 2k+1} = 1-b'_{2k+2} = 1-a'_{k+1}$). Thus $(a_k)_{k\ge 1}$ and $(b_k)_{k\ge 1}$ are $2$-automatic.
3. By Theorem 1 (`\ref{tm_red}`) of `arXiv:2509.16034v1`, $\rho_{\mathbf{t}}^{\mathrm{red}}(n) = 2(M_n - m_n + 1)$ is $2$-regular. Since $(a_n)$ and $(b_n)$ are $2$-automatic, $(-1)^{m_n} = 1 - 2a_n$ and $(-1)^{M_n} = 1 - 2b_n$ are $2$-automatic and therefore $2$-regular. By Lemma 1,
   $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n) = \frac{3}{4}\rho_{\mathbf{t}}^{\mathrm{red}}(n) + \frac{(-1)^{m_n} + (-1)^{M_n}}{4},$$
   which is a $\mathbb{Q}$-linear combination of $2$-regular sequences taking integer values, hence $(\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(n))_{n\ge 1}$ is $2$-regular. $\square$

---

## 4. Resolution of Open Problem (c1): Explicit Sign of $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$

**Theorem 2 (Exact Sign Formula — Open Problem (c1)).** *For every integer $n \ge 1$:*
1. $$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n) = b_{n+1} - a_{n+1} = \frac{(-1)^{m_{n+1}} - (-1)^{M_{n+1}}}{2} \in \{-1, 0, +1\}.$$
2. *In the nonzero case (equivalently $\mathbf{t}_{n+1} \neq \mathbf{t}_{3n+1}$), $a_{n+1} = 1 - b_{n+1}$, so the sign is explicitly*
   $$\mathrm{sgn}\!\bigl(\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)\bigr) = 2 b_{n+1} - 1 = (-1)^{1 - b_{n+1}} = \begin{cases} +1 & \text{if } M_{n+1} \text{ is odd (equivalently } m_{n+1} \text{ is even)}, \\ -1 & \text{if } M_{n+1} \text{ is even (equivalently } m_{n+1} \text{ is odd)}, \end{cases}$$
   *where $(a_{n+1}, b_{n+1}) = (a'_n, b'_n)$ is evaluated explicitly in $O(\log n)$ steps by the $2$-automatic recurrences of Theorem 1(2) (an $8$-state DFAO on the binary digits of $n$).*

*Proof.* Subtracting the first two equations of Theorem 1(1) gives
$$\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n+2) - \rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n) = (1 + b_{n+1}) - (1 + a_{n+1}) = b_{n+1} - a_{n+1} = \frac{(-1)^{m_{n+1}} - (-1)^{M_{n+1}}}{2}.$$
When this difference is nonzero, $a_{n+1} \neq b_{n+1}$ in $\{0,1\}$, so $a_{n+1} = 1 - b_{n+1}$ and $b_{n+1} - a_{n+1} = 2 b_{n+1} - 1 \in \{-1, +1\}$, which is $+1$ iff $b_{n+1} = 1$ ($M_{n+1}$ odd, $m_{n+1}$ even) and $-1$ iff $b_{n+1} = 0$ ($M_{n+1}$ even, $m_{n+1}$ odd). By Theorem 1(2), $b_{n+1}$ is $2$-automatic and explicitly computed from the binary representation of $n$. $\square$

---

## 5. Verification

Running `.venv/bin/python targets/campbell-2509.16034-conj1/verify.py` performs an exact-arithmetic check of:
- All factors of $\mathbf{t}$ up to $n=120$ (completeness verified via `A005942`), matching Lemma 1 and the paper's first $19$ terms;
- Theorem 1(1) ($\rho(4n)$, $\rho(4n+2)$, $\rho(2n+1)$) and Theorem 2 ($\rho(4n+2)-\rho(4n) = b_{n+1}-a_{n+1}$) for all $n=1,\dots,10000$;
- The coupled mod-$2$ recurrences of Theorem 1(2) and the exact $8$-state closure of the $2$-kernel of $(a'_n, b'_n) = (m_{n+1} \bmod 2, M_{n+1} \bmod 2)$.

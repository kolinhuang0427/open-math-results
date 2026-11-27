# Proof of Closed Forms and All Observations in `arXiv:2301.05758v3` Question 30

**Result:** We establish **exact closed forms for all four GCD sequences** $\mathcal{G}_C^2(k)$, $\mathcal{G}_B^2(k)$, $\mathcal{G}_c^2(k)$, and $\mathcal{G}_b^2(k)$ for every integer $k \ge 1$, and as immediate corollaries prove **all three conjectured/observed identities** in Question 30 of Mbirika–Schrader–Spilker (`arXiv:2301.05758v3`, Section 6.1, L1199–1216):

1. $\mathcal{G}_C^2(k) = \gcd(k, B_k)$ for all $k \ge 1$.
2. $\mathcal{G}_B^2(k) = \begin{cases} \frac{1}{2}\gcd(k, B_k) = \frac{1}{2}\mathcal{G}_C^2(k), & k \text{ even}, \\ \gcd(k, B_k) = \mathcal{G}_C^2(k), & k \text{ odd}. \end{cases}$
3. $\mathcal{G}_c^2(k) = \gcd(k, 3B_k) = \begin{cases} \gcd(k, B_k) = \mathcal{G}_C^2(k), & k \not\equiv 3 \pmod{6}, \\ 3\gcd(k, B_k) = 3\,\mathcal{G}_C^2(k), & k \equiv 3 \pmod{6}. \end{cases}$
4. $\mathcal{G}_b^2(k) = \begin{cases} 4\gcd\!\left(B_k,\; \dfrac{B_k - P_k}{4},\; \dfrac{B_k + 5k - 8P_k}{64}\right), & k \text{ even}, \\[8pt] 4\gcd\!\left(B_k,\; \dfrac{B_k - Q_k}{2},\; \dfrac{3B_k + 5k - 8Q_k}{64}\right), & k \text{ odd}, \end{cases}$
   and in particular $\mathcal{G}_b^2(k) \equiv 0 \pmod{4}$ for all $k \ge 1$ (indeed $\nu_2(\mathcal{G}_b^2(k)) = \nu_2(k) + 1$ for even $k$, and $\nu_2(\mathcal{G}_b^2(k)) = 2$ for odd $k$).

---

## 1. Preliminaries: Binet Formulas and Exact Consecutive-Square Sums

Let $\gamma = 1 + \sqrt{2}$ and $\delta = 1 - \sqrt{2}$, so $\gamma\delta = -1$, $\gamma^2\delta^2 = 1$, $\gamma + \delta = 2$, $\gamma - \delta = 2\sqrt{2}$, $\gamma^2 + \delta^2 = 6$, and $\gamma^2 - \delta^2 = 4\sqrt{2}$. From the defining recurrences and initial conditions in Section 2 (`arXiv:2301.05758v3`, L233–280), for all $n \ge 0$:
$$P_n = \frac{\gamma^n - \delta^n}{2\sqrt{2}}, \quad Q_n = \frac{\gamma^n + \delta^n}{2}, \quad B_n = \frac{\gamma^{2n} - \delta^{2n}}{4\sqrt{2}} = P_n Q_n = \frac{P_{2n}}{2},$$
$$C_n = \frac{\gamma^{2n} + \delta^{2n}}{2} = Q_{2n}, \quad b_n = \frac{\gamma^{2n-1} - \delta^{2n-1}}{4\sqrt{2}} - \frac{1}{2} = \frac{P_{2n-1}-1}{2}, \quad c_n = \frac{\gamma^{2n-1} + \delta^{2n-1}}{2} = Q_{2n-1}.$$

**Lemma 1 (Consecutive sums).** *For all integers $m \in \mathbb{Z}$, $n \ge 0$, and $k \ge 1$:*
1. $\displaystyle \sum_{i=1}^k C_{m+2i} = B_k C_{m+k+1}$.
2. $\displaystyle \sum_{i=1}^k P_{2n+2i-1} = \begin{cases} P_k Q_{2n+k}, & k \text{ even}, \\ Q_k P_{2n+k}, & k \text{ odd}. \end{cases}$

*Proof.*
1. Using $\gamma^4 - 1 = \gamma^2(\gamma^2 - \delta^2)$ and $\delta^4 - 1 = -\delta^2(\gamma^2 - \delta^2)$ (since $\gamma^2\delta^2 = 1$):
   $$\sum_{i=1}^k \gamma^{2m+4i} = \gamma^{2m+4}\frac{\gamma^{4k}-1}{\gamma^4 - 1} = \gamma^{2m+2k+2}\frac{\gamma^{2k}-\delta^{2k}}{\gamma^2-\delta^2}, \qquad \sum_{i=1}^k \delta^{2m+4i} = \delta^{2m+2k+2}\frac{\gamma^{2k}-\delta^{2k}}{\gamma^2-\delta^2}.$$
   Summing the two expressions and dividing by $2$ gives
   $$\sum_{i=1}^k C_{m+2i} = \frac{1}{2}\sum_{i=1}^k (\gamma^{2m+4i}+\delta^{2m+4i}) = \frac{\gamma^{2m+2k+2}+\delta^{2m+2k+2}}{2}\cdot\frac{\gamma^{2k}-\delta^{2k}}{\gamma^2-\delta^2} = C_{m+k+1} \cdot \frac{\gamma^{2k}-\delta^{2k}}{4\sqrt{2}} = B_k C_{m+k+1}.$$
2. Using $\gamma^2 - 1 = \gamma(\gamma + \delta) = 2\gamma$, $\delta^2 - 1 = 2\delta$, and $\gamma\delta = -1$:
   $$\sum_{i=1}^k \gamma^{2n+2i-1} = \gamma^{2n+1}\frac{\gamma^{2k}-1}{2\gamma} = \frac{\gamma^{2n+k}(\gamma^k - (-1)^k\delta^k)}{2}, \quad \sum_{i=1}^k \delta^{2n+2i-1} = \frac{\delta^{2n+k}(\delta^k - (-1)^k\gamma^k)}{2}.$$
   Subtracting and dividing by $2\sqrt{2}$ gives:
   - If $k$ is even: $\frac{(\gamma^{2n+k} + \delta^{2n+k})(\gamma^k - \delta^k)}{4\sqrt{2}} = Q_{2n+k} P_k$.
   - If $k$ is odd: $\frac{(\gamma^{2n+k} - \delta^{2n+k})(\gamma^k + \delta^k)}{4\sqrt{2}} = P_{2n+k} Q_k$. $\square$

**Corollary 2 (Exact formulas for the four square sums).** *Define $S_X(k,n) := \sum_{i=1}^k X_{n+i}^2$ for $X \in \{C, B, c, b\}$. For all $k \ge 1$ and $n \ge 0$:*
$$S_C(k,n) = \frac{B_k C_{2n+k+1} + k}{2}, \qquad S_B(k,n) = \frac{B_k C_{2n+k+1} - k}{16}, \qquad S_c(k,n) = \frac{B_k C_{2n+k} - k}{2},$$
$$S_b(k,n) = \frac{B_k C_{2n+k} + 5k}{16} - \frac{1}{2}\begin{cases} P_k Q_{2n+k}, & k \text{ even}, \\ Q_k P_{2n+k}, & k \text{ odd}. \end{cases}$$

*Proof.* Since $\gamma^{2r}\delta^{2r} = 1$ and $(\gamma\delta)^{2r-1} = -1$:
$$C_r^2 = \frac{C_{2r}+1}{2}, \qquad B_r^2 = \frac{C_{2r}-1}{16}, \qquad c_r^2 = \frac{C_{2r-1}-1}{2},$$
$$b_r^2 = \frac{\gamma^{4r-2} + 2 + \delta^{4r-2}}{32} - \frac{\gamma^{2r-1}-\delta^{2r-1}}{4\sqrt{2}} + \frac{1}{4} = \frac{C_{2r-1}+5}{16} - \frac{1}{2}P_{2r-1}.$$
Summing over $r = n+1, \dots, n+k$ and applying Lemma 1 with $m=2n$ (for $C, B$) and $m=2n-1$ (for $c, b$) gives all four formulas. $\square$

---

## 2. Periodicity and $p$-adic Lemmas

**Lemma 3 (Pure periodicity modulo $M$).** *For any integer $M \ge 2$:*
- *$(C_{2r} \bmod M)_{r \ge 0}$, $(C_{2r+1} \bmod M)_{r \ge 0}$, $(Q_{2r} \bmod M)_{r \ge 0}$, and $(P_{2r+1} \bmod M)_{r \ge 0}$ are purely periodic.*
- *In particular, for any fixed $k \ge 1$, as $n$ ranges over $\mathbb{Z}_{\ge 0}$, $C_{2n+k+1}$ attains every residue $C_{2r} \pmod M$ (when $k$ is odd) or $C_{2r+1} \pmod M$ (when $k$ is even), and similarly for $C_{2n+k}$, $Q_{2n+k}$, and $P_{2n+k}$.*

*Proof.* Each subsequence $(X_{2r})_{r \ge 0}$ and $(X_{2r+1})_{r \ge 0}$ for $X \in \{P, Q\}$ satisfies $X_{m+4} = 6 X_{m+2} - X_m$ (since $\gamma^2 + \delta^2 = 6$ and $\gamma^2\delta^2 = 1$), and each $(C_{2r})$ and $(C_{2r+1})$ satisfies $C_{m+2} = 34 C_m - C_{m-2}$ (since $\gamma^4+\delta^4=34$ and $\gamma^4\delta^4=1$). Both companion matrices $\begin{pmatrix}6&-1\\1&0\end{pmatrix}$ and $\begin{pmatrix}34&-1\\1&0\end{pmatrix}$ have determinant $1 \in (\mathbb{Z}/M\mathbb{Z})^\times$, so the state transitions are bijective on $(\mathbb{Z}/M\mathbb{Z})^2$ and every orbit is purely periodic. Shifting the starting index by $k$ stays in the same parity orbit, hence hits every residue class of the orbit infinitely often. $\square$

**Lemma 4 (Modular and $p$-adic valuations).** *For all $r \ge 0$ and $k \ge 1$:*
1. $C_{2r} \equiv 1 \pmod{16}$, $C_{2r+1} \equiv 3 \pmod{16}$, $Q_{2r} \equiv 1 \text{ or } 3 \pmod{16}$, and $P_{2r+1} \equiv 1 \text{ or } 5 \pmod{8}$.
2. *For odd $k$:* $B_k$ and $Q_k$ are odd, $B_k \equiv k \pmod{4}$, $3 \nmid B_k$, $3 \nmid Q_k$, and if $3 \mid k$ then $\nu_7(B_k) = \nu_7(Q_k) = 1 + \nu_7(k)$.
3. *For even $k$ with $a := \nu_2(k) \ge 1$:*
   - $\nu_2(B_k) = \nu_2(P_k) = a$, and $\nu_3(B_k) = 1 + \nu_3(k)$.
   - $B_k \equiv 3k \pmod{2^{a+4}}$. In particular, $\nu_2(3B_k + k) = a + 1$, $\nu_2(3B_k - k) = a + 3$, and $\nu_2(B_k - k) = a + 1$.
   - *If $4 \mid k$ ($a \ge 2$):* $B_k \equiv 51k \pmod{2^{a+6}}$ and $P_k \equiv 3k \pmod{2^{a+3}}$, so $\nu_2(B_k + 5k - 8P_k) = a + 5$.
   - *If $6 \mid k$:* $\nu_7(B_k) = \nu_7(P_k) = 1 + \nu_7(k)$ and $7 \nmid Q_k$.

*Proof.*
1. $C_0=1, C_2=17 \equiv 1 \pmod{16}$ and $C_1=3, C_3=99 \equiv 3 \pmod{16}$; since $C_{m+2} = 34 C_m - C_{m-2} \equiv 2 C_m - C_{m-2} \pmod{16}$, induction preserves $1 \pmod{16}$ and $3 \pmod{16}$. Similarly $Q_0=1, Q_2=3$, and $Q_{2r+4} = 6Q_{2r+2}-Q_{2r}$ alternates $1, 3 \pmod{16}$ (since $6\cdot 3 - 1 = 17 \equiv 1$ and $6\cdot 1 - 3 = 3$). For $P_{2r+1}$, $P_1=1, P_3=5$ and $6\cdot 5 - 1 = 29 \equiv 5 \pmod 8$, $6\cdot 5 - 5 = 25 \equiv 1 \pmod 8$.
2. Reducing $B_{n+2}=6B_{n+1}-B_n$ and $Q_{n+2}=2Q_{n+1}+Q_n$:
   - $\bmod 2$: $B_n \equiv n \pmod 2$ and $Q_n \equiv 1 \pmod 2$.
   - $\bmod 4$ on odd indices: $B_1=1, B_3=35 \equiv 3 \pmod 4$, and $B_{2r+3} = 34B_{2r+1}-B_{2r-1} \equiv 2B_{2r+1}-B_{2r-1} \pmod 4$, so $B_k \equiv k \pmod 4$ for odd $k$.
   - $\bmod 3$: $B \bmod 3$ repeats $(0,1,0,2)$ of period $4$ ($3 \nmid B_k$ for odd $k$), and $Q \bmod 3$ repeats $(1,1,0,1,2,2,0,2)$ of period $8$ ($3 \nmid Q_k$ for odd $k$).
   - $\nu_7$ for odd $k = 3m$: write $\gamma^3 = 7 + 5\sqrt{2}$ and $\delta^3 = 7 - 5\sqrt{2}$. Expanding $(7 \pm 5\sqrt{2})^m$ and averaging gives $Q_{3m} = \sum_{j \ge 0} \binom{m}{2j} 7^{m-2j} 50^j$. Setting $t = m - 2j$ (so $t \in \{1, 3, \dots, m\}$ as $m$ is odd):
     $$Q_{3m} = \sum_{\substack{1 \le t \le m \\ t \text{ odd}}} \binom{m}{t} 7^t 50^{(m-t)/2} = 7m \cdot 50^{(m-1)/2} + \sum_{\substack{3 \le t \le m \\ t \text{ odd}}} \frac{m}{t}\binom{m-1}{t-1} 7^t 50^{(m-t)/2}.$$
     For $t \ge 3$, $t - \nu_7(t) \ge 2$, so $\nu_7(\text{term } t) \ge \nu_7(m) + 2 > \nu_7(m) + 1 = \nu_7(7m \cdot 50^{(m-1)/2})$. Hence $\nu_7(Q_{3m}) = 1 + \nu_7(m) = 1 + \nu_7(k)$, while $P_{3m} \equiv \pm 5 \not\equiv 0 \pmod 7$, so $\nu_7(B_k) = \nu_7(P_k Q_k) = 1 + \nu_7(k)$.
3. For even $k = 2^a u$ ($u$ odd, $a \ge 1$):
   - From $(3 \pm 2\sqrt{2})^k$, we have
     $$B_k = \sum_{j \ge 0} \binom{k}{2j+1} 3^{k-2j-1} 2^{3j} = k\cdot 3^{k-1} + \frac{k(k-1)(k-2)}{6} 3^{k-3}\cdot 8 + \sum_{j \ge 2} \frac{k}{2j+1}\binom{k-1}{2j} 3^{k-2j-1} 2^{3j}.$$
     Since $2j+1$ is odd, $\nu_2(\text{term } j) \ge a + 3j$. For $j \ge 2$, $\nu_2 \ge a + 6$.
     - If $a = 1$ ($k = 2u$, $k-2 \equiv 0 \pmod 4$, $k-1$ odd): $\nu_2(\text{term } j=1) \ge 1 + 2 - 1 + 3 = 5 = a+4$, and $3^{k-1} = 3 \cdot 9^{u-1} \equiv 3 \pmod{16}$ (since $u-1$ is even and $9^2 \equiv 1 \pmod{16}$). Thus $B_k \equiv 3k \pmod{2^{a+4}}$.
     - If $a \ge 2$ ($k = 4r$): the $j=0,1$ terms sum to $k \cdot 3^{k-4}\bigl(27 + 4(k^2 - 3k + 2)\bigr) = k \cdot 3^{k-4}(4k^2 - 12k + 35)$. Since $3^4 = 81 \equiv 1 + 16 \pmod{64}$ and $4k^2 = 64r^2 \equiv 0 \pmod{64}$, we have
       $$3^{k-4}(4k^2 - 12k + 35) \equiv (1 + 16(r-1))(35 + 16r) \equiv 35 + 16r + 35\cdot 16r - 35\cdot 16 \equiv 35 - 48 = -13 \equiv 51 \pmod{64}.$$
       Hence $B_k \equiv 51k \pmod{2^{a+6}}$, and in particular $B_k \equiv 3k \pmod{2^{a+4}}$ (since $51 \equiv 3 \pmod{16}$).
     In both cases $\nu_2(B_k) = a$, $\nu_2(3B_k + k) = \nu_2(10k) = a+1$, $\nu_2(3B_k - k) = \nu_2(8k) = a+3$, and $\nu_2(B_k - k) = \nu_2(2k) = a+1$.
   - From $(1 \pm \sqrt{2})^k$, $P_k = \sum_{j \ge 0} \binom{k}{2j+1} 2^j$. Since $2j+1$ is odd, $\nu_2(\text{term } j) \ge a + j$.
     - For $a \ge 1$: $\nu_2(\text{term } j \ge 1) \ge a+1$, so $\nu_2(P_k) = a$.
     - For $4 \mid k$ ($a \ge 2$): terms with $j \ge 3$ have $\nu_2 \ge a+3$. For $j=0,1,2$: $2\binom{k}{3} = k\frac{k^2-3k+2}{3}$ gives $2k \pmod{2^{a+3}}$ if $k \equiv 4 \pmod 8$, or $6k \pmod{2^{a+3}}$ if $8 \mid k$; and $4\binom{k}{5} = k\frac{(k-1)(k-2)(k-3)(k-4)}{30}$ is $0 \pmod{2^{a+3}}$ if $k \equiv 4 \pmod 8$, or $4k \pmod{2^{a+3}}$ if $8 \mid k$. In both cases $P_k \equiv (1+2+0)k \equiv (1+6+4)k \equiv 3k \pmod{2^{a+3}}$.
     Therefore, for $4 \mid k$: $B_k + 5k - 8P_k \equiv (51 + 5 - 24)k = 32k \pmod{2^{a+6}}$, so $\nu_2(B_k + 5k - 8P_k) = a + 5$.
   - $\nu_3(B_k)$ for even $k = 2m$: write $\gamma^4 = 17 + 12\sqrt{2}$ and $\delta^4 = 17 - 12\sqrt{2}$. Expanding $\frac{(17+12\sqrt{2})^m - (17-12\sqrt{2})^m}{4\sqrt{2}}$ gives
     $$B_{2m} = 6 m \cdot 17^{m-1} + \sum_{j \ge 1} \frac{m}{2j+1}\binom{m-1}{2j} 17^{m-2j-1} \cdot 6 \cdot 288^j.$$
     Since $3^2 \mid 288$, $\nu_3(6 \cdot 288^j / (2j+1)) \ge 1 + 2j - \nu_3(2j+1) \ge 2$ for all $j \ge 1$ (as $2j - \nu_3(2j+1) \ge 1$ for $j \ge 1$), so every $j \ge 1$ term has $\nu_3 \ge \nu_3(m) + 2$, whereas $\nu_3(6m \cdot 17^{m-1}) = 1 + \nu_3(m) = 1 + \nu_3(k)$.
   - $\nu_7(B_k)$ for $6 \mid k$: write $k = 6m$. Since $\gamma^6 = 99 + 70\sqrt{2}$ with $\nu_7(70)=1$ and $7 \nmid 99$, expanding $(99 \pm 70\sqrt{2})^m$ gives
     $$P_{6m} = \sum_{j \ge 0} \frac{m}{2j+1}\binom{m-1}{2j} 99^{m-2j-1} \cdot 70 \cdot (9800)^j,$$
     where $7^2 \mid 9800$, so every $j \ge 1$ term has $\nu_7 \ge \nu_7(m) + 1 + 2j - \nu_7(2j+1) \ge \nu_7(m) + 2$, while $\nu_7(70 m \cdot 99^{m-1}) = 1 + \nu_7(m) = 1 + \nu_7(k)$, and $Q_{6m} \equiv 99^m \equiv 1 \pmod 7$. Thus $\nu_7(B_k) = \nu_7(P_k) = 1 + \nu_7(k)$. $\square$

---

## 3. Proofs of $\mathcal{G}_C^2(k)$, $\mathcal{G}_B^2(k)$, and $\mathcal{G}_c^2(k)$

### Theorem A: $\mathcal{G}_C^2(k) = \gcd(k, B_k)$ for all $k \ge 1$

- **Divisibility ($\gcd(k, B_k) \mid \mathcal{G}_C^2(k)$):** Let $g = \gcd(k, B_k)$. Every odd divisor of $g$ divides both $k$ and $B_k$, hence divides $B_k C_{2n+k+1} + k$ and therefore divides $S_C(k,n) = \frac{B_k C_{2n+k+1} + k}{2}$. For $p = 2$: if $k$ is odd then $g$ is odd; if $k$ is even with $\nu_2(k) = a$, then $\nu_2(B_k) = a$ (Lemma 4.3), and writing $k = 2^a u, B_k = 2^a v$ ($u, v$ odd) gives $S_C(k,n) = 2^{a-1}(v C_{2n+k+1} + u)$, where $v C_{2n+k+1} + u$ is even since $C_{2n+k+1}$ is odd, so $2^a \mid S_C(k,n)$ for all $n \ge 0$. Hence $g \mid \mathcal{G}_C^2(k)$.
- **Reverse divisibility ($\mathcal{G}_C^2(k) \mid \gcd(k, B_k)$):** Set $d := \mathcal{G}_C^2(k)$.
  - *Case $k$ odd:* By Lemma 3 (with $M = 16d$), choose $n_0, n_1 \ge 0$ such that $C_{2n_0+k+1} \equiv C_0 = 1 \pmod{16d}$ and $C_{2n_1+k+1} \equiv C_2 = 17 \pmod{16d}$. Subtracting $S_C(k, n_1) - S_C(k, n_0)$ gives $d \mid \frac{17-1}{2} B_k = 8 B_k$. Moreover, $S_C(k, n_0) \equiv \frac{B_k + k}{2} \pmod{8d}$. Since $B_k \equiv k \pmod 4$ (Lemma 4.2) and $k$ is odd, $B_k + k \equiv 2 \pmod 4$, so $\frac{B_k + k}{2}$ is odd. Thus $d$ is odd, so $d \mid 8 B_k \implies d \mid B_k$, and then $d \mid \frac{B_k + k}{2} \implies d \mid k$.
  - *Case $k$ even:* By Lemma 3 (with $M = 2d$), choose $n_1, n_3 \ge 0$ with $C_{2n_1+k+1} \equiv C_1 = 3 \pmod{2d}$ and $C_{2n_3+k+1} \equiv C_3 = 99 \pmod{2d}$. Subtracting gives $d \mid \frac{99-3}{2} B_k = 48 B_k$, and $d \mid \frac{3B_k + k}{2}$.
    - For any prime $p \notin \{2, 3\}$: $p^{\nu_p(d)} \mid 48 B_k \implies p^{\nu_p(d)} \mid B_k$, and then $p^{\nu_p(d)} \mid (3B_k + k) \implies p^{\nu_p(d)} \mid k$.
    - For $p = 3$: if $3^e \mid d$, then $3^{e-1} \mid B_k$ (from $48 = 16 \cdot 3$), so $3^e \mid 3 B_k$, whence $3^e \mid (3B_k + k) \implies 3^e \mid k$; since $\nu_3(B_k) = 1 + \nu_3(k) > \nu_3(k)$ (Lemma 4.3), $3^e \mid B_k$ holds automatically.
    - For $p = 2$: by Lemma 4.1 & 4.3, $C_{2n+k+1} = 3 + 16t_n$ and $\nu_2(3B_k + k) = a+1$, while $\nu_2(16 B_k t_n) \ge a+4$, so $\nu_2(S_C(k,n)) = (a+1)-1 = a = \nu_2(k) = \nu_2(B_k)$ for all $n \ge 0$. Hence $\nu_2(d) = a$.
  Thus $d \mid \gcd(k, B_k)$, proving $\mathcal{G}_C^2(k) = \gcd(k, B_k)$. $\square$

### Theorem B (Question 30 Bullet 1): $\mathcal{G}_B^2(k) = \begin{cases} \frac{1}{2}\gcd(k, B_k), & k \text{ even}, \\ \gcd(k, B_k), & k \text{ odd}. \end{cases}$

Recall $S_B(k,n) = \frac{B_k C_{2n+k+1} - k}{16}$ and $S_C(k,n) = \frac{B_k C_{2n+k+1} + k}{2}$, so $S_C(k,n) - 8 S_B(k,n) = k$ and $S_C(k,n) + 8 S_B(k,n) = B_k C_{2n+k+1}$.
- Therefore, for every odd prime $p$:
  - If $p^e \mid \gcd(k, B_k)$, then $p^e \mid S_C(k,n)$ (Theorem A) and $p^e \mid k$, so $p^e \mid 8 S_B(k,n) = S_C(k,n) - k \implies p^e \mid S_B(k,n)$ for all $n$.
  - Conversely, if $p^e \mid \mathcal{G}_B^2(k)$, then by Lemma 3 choosing $C_{2n+k+1} \equiv C_0 = 1$ ($k$ odd) or $C_1 = 3$ ($k$ even) and $C_{2n'+k+1} \equiv C_2 = 17$ ($k$ odd) or $C_3 = 99$ ($k$ even) modulo $16 p^e$ gives $p^e \mid B_k$ ($k$ odd) or $p^e \mid 6 B_k$ ($k$ even, since $\frac{99-3}{16} = 6$), and $p^e \mid (B_k - k)$ ($k$ odd) or $p^e \mid (3B_k - k)$ ($k$ even). For $k$ odd this yields $p^e \mid \gcd(k, B_k)$. For $k$ even, if $p = 3$ and $3^e \mid \mathcal{G}_B^2(k)$, then $3^{e-1} \mid B_k \implies 3^e \mid 3 B_k \implies 3^e \mid k$, and again $\nu_3(B_k) = 1 + \nu_3(k) > \nu_3(k)$ gives $3^e \mid \gcd(k, B_k)$. Thus $\nu_p(\mathcal{G}_B^2(k)) = \nu_p(\gcd(k, B_k))$ for all odd primes $p$.
- For $p = 2$:
  - *Case $k$ odd:* By Lemma 3, choose $C_{2n+k+1} \equiv 1$ and $C_{2n'+k+1} \equiv 17 \pmod{32}$; then $S_B(k,n') - S_B(k,n) \equiv B_k \equiv 1 \pmod 2$, so at least one of $S_B(k,n), S_B(k,n')$ is odd. Hence $\nu_2(\mathcal{G}_B^2(k)) = 0 = \nu_2(\gcd(k, B_k))$.
  - *Case $k$ even:* By Lemma 4.1 & 4.3, $C_{2n+k+1} = 3 + 16t_n$ and $\nu_2(3B_k - k) = a + 3$, while $\nu_2(16 B_k t_n) \ge a + 4$. Thus $\nu_2(B_k C_{2n+k+1} - k) = a + 3$ for every $n \ge 0$, so $\nu_2(S_B(k,n)) = (a+3)-4 = a - 1 = \nu_2(\mathcal{G}_C^2(k)) - 1$ for every $n \ge 0$. Hence $\mathcal{G}_B^2(k) = \frac{1}{2}\mathcal{G}_C^2(k)$. $\square$

### Theorem C (Question 30 Bullet 2): $\mathcal{G}_c^2(k) = \gcd(k, 3B_k) = \begin{cases} \mathcal{G}_C^2(k), & k \not\equiv 3 \pmod 6, \\ 3\,\mathcal{G}_C^2(k), & k \equiv 3 \pmod 6. \end{cases}$

Recall $S_c(k,n) = \frac{B_k C_{2n+k} - k}{2}$.
- First note $\gcd(k, 3B_k) = 3\gcd(k, B_k)$ if $k \equiv 3 \pmod 6$, and $\gcd(k, B_k)$ otherwise: for $k$ odd, $3 \nmid B_k$ (Lemma 4.2), so the extra factor $3$ enters iff $3 \mid k$ (i.e., $k \equiv 3 \pmod 6$); for $k$ even, $\nu_3(B_k) = 1 + \nu_3(k) > \nu_3(k)$ (Lemma 4.3), so $\min(\nu_3(k), 1 + \nu_3(B_k)) = \min(\nu_3(k), \nu_3(B_k))$.
- **Divisibility ($\gcd(k, 3B_k) \mid \mathcal{G}_c^2(k)$):**
  - If $k$ is odd: any prime power $p^e \mid \gcd(k, 3B_k)$ with $p \ne 3$ is odd and divides both $k$ and $B_k$, hence divides $S_c(k,n)$. For $p = 3$, since $\nu_3(B_k) = 0$ and $3 \mid C_{2n+k}$ (as $2n+k$ is odd and $C_1 = 3 \mid C_{2r+1}$), $\nu_3(\gcd(k, 3B_k)) \le 1$, and when $3 \mid k$ we have $3 \mid (B_k C_{2n+k} - k) \implies 3 \mid S_c(k,n)$.
  - If $k$ is even: $\gcd(k, 3B_k) = \gcd(k, B_k)$. Every odd divisor divides $k$ and $B_k$, hence $S_c(k,n)$. For $p = 2$, $\nu_2(k) = \nu_2(B_k) = a$, and writing $k = 2^a u, B_k = 2^a v$ ($u,v$ odd) gives $S_c(k,n) = 2^{a-1}(v C_{2n+k} - u)$ with $v C_{2n+k} - u$ even, so $2^a \mid S_c(k,n)$.
- **Reverse divisibility ($d := \mathcal{G}_c^2(k) \mid \gcd(k, 3B_k)$):**
  - *Case $k$ odd:* $2n+k$ is odd, so by Lemma 3 (with $M = 16d$) choose $n_1, n_3$ with $C_{2n_1+k} \equiv C_1 = 3 \pmod{16d}$ and $C_{2n_3+k} \equiv C_3 = 99 \pmod{16d}$. Subtracting gives $d \mid 48 B_k$. At $n_1$, $S_c(k, n_1) \equiv \frac{3B_k - k}{2} \pmod{8d}$. Since $B_k \equiv k \pmod 4$ and $k$ is odd (Lemma 4.2), $3B_k - k \equiv 2k \equiv 2 \pmod 4$, so $S_c(k, n_1)$ is odd. Hence $d$ is odd, so $d \mid 48 B_k \implies d \mid 3 B_k$, and $d \mid (3B_k - k) \implies d \mid k$. Thus $d \mid \gcd(k, 3B_k)$.
  - *Case $k$ even:* $2n+k$ is even, so by Lemma 3 (with $M = 2d$) choose $n_0, n_2$ with $C_{2n_0+k} \equiv C_0 = 1 \pmod{2d}$ and $C_{2n_2+k} \equiv C_2 = 17 \pmod{2d}$. Subtracting gives $d \mid 8 B_k$, and $d \mid \frac{B_k - k}{2}$. Hence every odd prime power dividing $d$ divides both $B_k$ and $k$. For $p = 2$, $C_{2n+k} = 1 + 16 t_n$ and $\nu_2(B_k - k) = a + 1$ (Lemma 4.3), while $\nu_2(16 B_k t_n) \ge a + 4$, so $\nu_2(S_c(k,n)) = a$ for all $n$, giving $\nu_2(d) = a = \nu_2(\gcd(k, B_k))$. $\square$

---

## 4. Exact Closed Form for $\mathcal{G}_b^2(k)$ and Proof of $\mathcal{G}_b^2(k) \equiv 0 \pmod{4}$

### Theorem D (Exact formula for $\mathcal{G}_b^2(k)$ and Question 30 Bullet 3)

For every $k \ge 1$,
$$\mathcal{G}_b^2(k) = \begin{cases} 4\gcd\!\left(B_k,\; \dfrac{B_k - P_k}{4},\; \dfrac{B_k + 5k - 8P_k}{64}\right), & k \text{ even}, \\[8pt] 4\gcd\!\left(B_k,\; \dfrac{B_k - Q_k}{2},\; \dfrac{3B_k + 5k - 8Q_k}{64}\right), & k \text{ odd}, \end{cases}$$
where all arguments inside both $\gcd$s are integers. In particular, $\mathcal{G}_b^2(k) \equiv 0 \pmod{4}$ for all $k \ge 1$.

*Proof.* (Note first that Bullet 3 alone is also trivial term-by-term since $b_0 = 0$ and $P_{2r-1} \equiv 1 \pmod{4}$ for all $r \ge 1$ by Lemma 4.1, so $b_r = (P_{2r-1}-1)/2$ is always even and $4 \mid b_r^2$ for every $r \ge 0$. Below we prove the full closed form for $\mathcal{G}_b^2(k)$.)

Using $C_m = \frac{\gamma^{2m}+\delta^{2m}}{2} = 2\bigl(\frac{\gamma^m+\delta^m}{2}\bigr)^2 - (\gamma\delta)^m = 2 Q_m^2 - (-1)^m$ and $Q_m^2 - 2 P_m^2 = (-1)^m$ (which gives $C_m = 4 P_m^2 + (-1)^m$), substitute $m = 2n+k$ into Corollary 2:

#### Case 1: $k$ is even ($m = 2n+k$ is even, $(-1)^m = 1$)
Here $C_m = 2 Q_m^2 - 1$, so
$$16 S_b(k,n) = 2 B_k Q_m^2 - 8 P_k Q_m + (5k - B_k).$$
By Lemma 4.1, $Q_m \equiv 1$ or $3 \pmod{16}$, so $x_n := \frac{Q_m - 1}{2} \in \mathbb{Z}$ satisfies $x_n \equiv 0$ or $1 \pmod 8$, whence $w_n := \frac{x_n(x_n - 1)}{8} \in \mathbb{Z}$. Substituting $Q_m = 2x_n + 1$ and $x_n^2 = 8w_n + x_n$:
$$16 S_b(k,n) = 8 B_k(x_n^2 + x_n) - 16 P_k x_n + (B_k + 5k - 8P_k) = 64 B_k w_n + 16(B_k - P_k) x_n + (B_k + 5k - 8P_k).$$
Check integrality of $c_1 := \frac{B_k - P_k}{4}$ and $c_0 := \frac{B_k + 5k - 8P_k}{64}$:
- For $c_1$: if $k \equiv 2 \pmod 4$, then $\nu_2(P_k) = 1$ and $Q_k = C_{k/2} \equiv 3 \pmod 8$ (odd index), so $\nu_2(Q_k - 1) = 1$ and $4 \mid P_k(Q_k - 1) = B_k - P_k$; if $4 \mid k$, then $\nu_2(P_k) \ge 2$ and $Q_k = C_{k/2} \equiv 1 \pmod{16}$, so $64 \mid (B_k - P_k)$.
- For $c_0$: by Lemma 3 with $M = 1024$, there exists $n_0 \ge 0$ with $Q_{2n_0+k} \equiv Q_0 = 1 \pmod{1024}$, giving $x_{n_0} \equiv 0 \pmod{512}$ and $w_{n_0} \equiv 0 \pmod{64}$. Then $16 S_b(k, n_0) \equiv B_k + 5k - 8P_k \pmod{64}$, and since $4 \mid b_r^2$ for all $r$ we have $64 \mid 16 S_b(k, n_0)$, forcing $64 \mid (B_k + 5k - 8P_k)$. (When $4 \mid k$, Lemma 4.3 also directly gives $\nu_2(B_k + 5k - 8P_k) = a + 5 \ge 7$.)

Dividing by $64$, we obtain the exact integer identity for all $n \ge 0$:
$$\frac{S_b(k,n)}{4} = B_k w_n + c_1 x_n + c_0, \qquad c_1 = \frac{B_k - P_k}{4} \in \mathbb{Z}, \quad c_0 = \frac{B_k + 5k - 8P_k}{64} \in \mathbb{Z}.$$
Hence $g_{\mathrm{even}} := \gcd(B_k, c_1, c_0)$ divides $S_b(k,n)/4$ for all $n \ge 0$, so $4 g_{\mathrm{even}} \mid \mathcal{G}_b^2(k)$.

Conversely, let $D := \mathcal{G}_b^2(k)/4$ and let $p^e \mid D$ be any prime power. By Lemma 3 (with $M = 16 p^e$), as $n \ge 0$ varies, $Q_{2n+k}$ attains $Q_0 = 1$, $Q_2 = 3$, and $Q_4 = 17$ modulo $16 p^e$:
- Choosing $Q_{2n_0+k} \equiv 1 \pmod{16 p^e}$ gives $x_{n_0} \equiv 0 \pmod{8p^e}$ and $w_{n_0} \equiv 0 \pmod{p^e}$, so $c_0 \equiv S_b(k,n_0)/4 \equiv 0 \pmod{p^e}$.
- Choosing $Q_{2n_1+k} \equiv 3 \pmod{16 p^e}$ gives $x_{n_1} \equiv 1 \pmod{8p^e}$ and $w_{n_1} \equiv 0 \pmod{p^e}$, so $c_1 + c_0 \equiv 0 \pmod{p^e} \implies p^e \mid c_1$.
- Choosing $Q_{2n_2+k} \equiv 17 \pmod{16 p^e}$ gives $x_{n_2} \equiv 8 \pmod{8p^e}$ and $w_{n_2} = \frac{x_{n_2}(x_{n_2}-1)}{8} \equiv 7 \pmod{p^e}$, so $7 B_k + 8 c_1 + c_0 \equiv 0 \pmod{p^e} \implies p^e \mid 7 B_k$.

Thus:
- For any prime $p \notin \{2, 7\}$: $p^e \mid 7 B_k \implies p^e \mid B_k$, so $p^e \mid g_{\mathrm{even}}$.
- For $p = 7$: $7^e \mid c_1$ and $7^e \mid c_0$ with $e \ge 1$ imply $B_k \equiv P_k \pmod 7$ and $B_k + 5k - 8P_k \equiv 0 \pmod 7$, so $5k \equiv 0 \pmod 7 \implies 7 \mid k$. Since $(P_k, Q_k) \bmod 7$ has period $6$ and for $k \equiv 2, 4 \pmod 6$ one has $Q_k \equiv 3 \pmod 7$ and $P_k \equiv \pm 2 \pmod 7$ (giving $B_k - P_k = P_k(Q_k - 1) \equiv \pm 4 \not\equiv 0 \pmod 7$), $7 \mid c_1$ forces $6 \mid k$. By Lemma 4.3, when $6 \mid k$ we have $\nu_7(B_k) = \nu_7(P_k) = 1 + \nu_7(k)$ while $7 \nmid Q_k$, so in $64 c_0 = B_k + 5k - 8P_k = P_k(Q_k - 8) + 5k$ the term $P_k(Q_k - 8)$ has valuation at least $1 + \nu_7(k) > \nu_7(5k) = \nu_7(k)$. Thus $\nu_7(c_0) = \nu_7(k) < \nu_7(B_k)$, so $e \le \nu_7(c_0) < \nu_7(B_k)$ and $7^e \mid B_k$ automatically.
- For $p = 2$:
  - If $k \equiv 2 \pmod 4$: $\nu_2(P_k) = 1$ and $Q_k = C_{k/2} \equiv 3 \pmod 8$, so $\nu_2(Q_k - 1) = 1$ and $\nu_2(B_k - P_k) = 2$, whence $c_1 = \frac{B_k - P_k}{4}$ is odd. Since $2^e \mid c_1$, $e = 0$.
  - If $4 \mid k$: by Lemma 4.3, $\nu_2(B_k) = a$ and $\nu_2(B_k + 5k - 8P_k) = a + 5$, so $\nu_2(c_0) = a - 1 < a = \nu_2(B_k)$. Since $2^e \mid c_0$, we get $e \le \nu_2(c_0) = a - 1 < \nu_2(B_k)$, so $2^e \mid B_k$ automatically.

Hence $D \mid g_{\mathrm{even}}$, proving $\mathcal{G}_b^2(k) = 4 g_{\mathrm{even}}$ for all even $k \ge 2$.

#### Case 2: $k$ is odd ($m = 2n+k$ is odd, $(-1)^m = -1$)
Here $C_m = 4 P_m^2 - 1$, so
$$16 S_b(k,n) = 4 B_k P_m^2 - 8 Q_k P_m + (5k - B_k).$$
By Lemma 4.1, $P_m \equiv 1$ or $5 \pmod 8$, so $y_n := \frac{P_m - 1}{4} \in \mathbb{Z}$. Substituting $P_m = 4 y_n + 1$:
$$16 S_b(k,n) = 64 B_k y_n^2 + 32(B_k - Q_k) y_n + (3B_k + 5k - 8Q_k).$$
Here $B_k$ and $Q_k$ are both odd (Lemma 4.2), so $d_1 := \frac{B_k - Q_k}{2} \in \mathbb{Z}$. Moreover, by Lemma 3 with $M = 256$, there exists $n_0 \ge 0$ with $P_{2n_0+k} \equiv P_1 = 1 \pmod{256}$, so $y_{n_0} \equiv 0 \pmod{64}$; since $64 \mid 16 S_b(k, n_0)$ (each $b_r$ is even), it follows that $c_0' := \frac{3B_k + 5k - 8Q_k}{64} \in \mathbb{Z}$. Dividing by $64$:
$$\frac{S_b(k,n)}{4} = B_k y_n^2 + d_1 y_n + c_0', \qquad d_1 = \frac{B_k - Q_k}{2} \in \mathbb{Z}, \quad c_0' = \frac{3B_k + 5k - 8Q_k}{64} \in \mathbb{Z}.$$
Hence $g_{\mathrm{odd}} := \gcd(B_k, d_1, c_0') \mid D := \mathcal{G}_b^2(k)/4$.

Conversely, let $p^e \mid D$ be any prime power. By Lemma 3 (with $M = 64 p^e$), $P_{2n+k}$ attains $P_1 = 1$, $P_3 = 5$, and $P_5 = 29$ modulo $64 p^e$, giving $y_{n_1} \equiv 0$, $y_{n_3} \equiv 1$, and $y_{n_5} \equiv 7 \pmod{p^e}$:
- At $y_{n_1} \equiv 0 \pmod{p^e}$: $p^e \mid c_0'$.
- At $y_{n_3} \equiv 1 \pmod{p^e}$: $p^e \mid (B_k + d_1 + c_0') \implies p^e \mid (B_k + d_1)$.
- At $y_{n_5} \equiv 7 \pmod{p^e}$: $p^e \mid (49 B_k + 7 d_1 + c_0')$, and subtracting $7(B_k + d_1) + c_0'$ gives $p^e \mid 42 B_k$.

Thus:
- For any prime $p \notin \{2, 3, 7\}$: $p^e \mid 42 B_k \implies p^e \mid B_k$, and then $p^e \mid (B_k + d_1) \implies p^e \mid d_1$, so $p^e \mid g_{\mathrm{odd}}$.
- For $p = 2$: $B_k$ is odd, and modulo $8$, $P_{2r-1}$ repeats $(1, 5, 5, 1)$ of period $4$ (since $P_{2r+3} = 6P_{2r+1} - P_{2r-1}$ gives $6\cdot 5 - 1 \equiv 5$, $6\cdot 5 - 5 \equiv 1$, $6\cdot 1 - 5 \equiv 1$, $6\cdot 1 - 1 \equiv 5 \pmod 8$), so $(b_r/2) \bmod 2 = \frac{P_{2r-1}-1}{4} \bmod 2$ repeats $(0, 1, 1, 0)$ of period $4$. Over one full period of length $4$, $b_r^2/4 \bmod 2$ sums to $0 + 1 + 1 + 0 \equiv 0 \pmod 2$. For odd $k$: if $k \equiv 1 \pmod 4$, $S_b(k,0)/4 \equiv 0 \pmod 2$ and $S_b(k,1)/4 \equiv 1 \pmod 2$; if $k \equiv 3 \pmod 4$, $S_b(k,1)/4 \equiv 1 + 1 + 0 \equiv 0 \pmod 2$ and $S_b(k,2)/4 \equiv 1 + 0 + 0 \equiv 1 \pmod 2$. Thus $2 \nmid D$, so $e = 0$.
- For $p = 3$: if $e \ge 1$, then $3 \mid (B_k + d_1)$, i.e., $3 B_k - Q_k \equiv 0 \pmod 3$, so $3 \mid Q_k$, contradicting Lemma 4.2 ($3 \nmid Q_k$ for all odd $k$). Hence $e = 0$.
- For $p = 7$: if $e \ge 1$, then $7 \mid c_0'$ and $7 \mid (B_k + d_1)$, i.e., $3B_k - Q_k \equiv 0 \pmod 7$. Since $(P_k, Q_k) \bmod 7$ has period $6$, checking odd $k \bmod 6$ gives:
  - $k \equiv 1 \pmod 6$: $(P_k, Q_k) \equiv (1, 1)$, so $3B_k - Q_k \equiv 2 \not\equiv 0 \pmod 7$;
  - $k \equiv 5 \pmod 6$: $(P_k, Q_k) \equiv (1, 6)$, so $3B_k - Q_k \equiv 18 - 6 = 12 \not\equiv 0 \pmod 7$;
  - $k \equiv 3 \pmod 6$: $(P_k, Q_k) \equiv (5, 0) \pmod 7$.
  Thus $e \ge 1$ forces $3 \mid k$. By Lemma 4.2, when $k$ is odd and $3 \mid k$, $\nu_7(B_k) = \nu_7(Q_k) = 1 + \nu_7(k)$. Therefore, in $64 c_0' = 3 B_k - 8 Q_k + 5k$, we have $\nu_7(3B_k - 8Q_k) \ge 1 + \nu_7(k) > \nu_7(5k) = \nu_7(k)$, so $\nu_7(c_0') = \nu_7(k) < \nu_7(B_k)$. Since $7^e \mid c_0'$, we get $e \le \nu_7(k) < \nu_7(B_k)$, hence $7^e \mid B_k$ and $7^e \mid (B_k + d_1) \implies 7^e \mid d_1$.

Hence $D \mid g_{\mathrm{odd}}$, proving $\mathcal{G}_b^2(k) = 4 g_{\mathrm{odd}}$ for all odd $k \ge 1$. $\square$

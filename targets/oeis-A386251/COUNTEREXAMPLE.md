# Counterexample Refuting OEIS A386251 (3-Segment Closed Walk Conjecture)

## Statement Refuted
In OEIS `A386251` (Charles L. Hohn, rev. 22, 2025-08-06), $a(n)$ is the minimum total Euclidean length of a closed walk in $\mathbb{Z}^n$ whose steps are noncongruent primitive integer-length diagonals traversing all $n$ dimensions (i.e., $v^{(1)}, \dots, v^{(k)} \in \mathbb{Z}^n$ with $\sum_{j=1}^k v^{(j)} = 0$, $v^{(j)}_i \neq 0$ for all $i,j$, $\gcd(v^{(j)}_1, \dots, v^{(j)}_n) = 1$, $\|v^{(j)}\|_2 \in \mathbb{Z}_{>0}$, and pairwise distinct multisets $\{|v^{(j)}_1|, \dots, |v^{(j)}_n|\}$).

The conjecture states:
> "It is provable that all such walks must be even in total length. It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks."

**Result:** **FALSE.** For every integer $m \ge 92$ and $n = m^2 - 30$ (smallest instance $m = 92$, $n = 8434$), there exists a valid 4-segment closed walk (in fact, a simple 4-cycle) of total length $4m$ ($368$ at $n = 8434$), whereas every valid 3-segment closed walk has total length $\ge 4m + 2$ ($\ge 370$ at $n = 8434$). Thus $a(m^2 - 30) = 4m$ is NOT produced by any 3-segment walk for all $m \ge 92$.

---

## 1. Explicit 4-Segment Witness for $n = m^2 - 30$ ($m \ge 92$)

Fix $m \ge 92$ and let $n = m^2 - 30 \ge 8434$. Define four step vectors $v^{(1)}, v^{(2)}, v^{(3)}, v^{(4)} \in \mathbb{Z}^n$ as follows:

- On the first $10$ coordinates $i = 1, \dots, 10$, the columns $(v^{(1)}_i, v^{(2)}_i, v^{(3)}_i, v^{(4)}_i)^T$ are:
  1. $(-2,\; -4,\; \phantom{-}1,\; \phantom{-}5)^T$
  2. $(-2,\; -2,\; \phantom{-}3,\; \phantom{-}1)^T$ (3 copies: $i = 2, 3, 4$)
  3. $(\phantom{-}2,\; -2,\; -1,\; \phantom{-}1)^T$ (2 copies: $i = 5, 6$)
  4. $(\phantom{-}2,\; -1,\; -2,\; \phantom{-}1)^T$ (2 copies: $i = 7, 8$)
  5. $(\phantom{-}2,\; -1,\; \phantom{-}1,\; -2)^T$ (2 copies: $i = 9, 10$)
- On the remaining $n - 10$ coordinates $i = 11, \dots, n$, every column is $(1,\; 1,\; -1,\; -1)^T$.

### Verification of All Graph and Walk Conditions
1. **Closed walk (and simple 4-cycle):**
   Every column sums to $0$:
   $(-2-4+1+5)=0$, $(-2-2+3+1)=0$, $(2-2-1+1)=0$, $(2-1-2+1)=0$, $(2-1+1-2)=0$, and $(1+1-1-1)=0$.
   Thus $v^{(1)} + v^{(2)} + v^{(3)} + v^{(4)} = 0$.
   Moreover, looking only at coordinate $1$, the four cumulative vertices $0, v^{(1)}, v^{(1)}+v^{(2)}, v^{(1)}+v^{(2)}+v^{(3)}$ have first coordinates $0, -2, -6, -5$, which are pairwise distinct, so the walk visits no repeated intermediate vertex.
2. **Traverses all $n$ dimensions:**
   Every entry belongs to $\{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5\}$, so $v^{(j)}_i \neq 0$ for all $1 \le i \le n$ and $1 \le j \le 4$.
3. **No intermediate lattice points (primitive):**
   Since $n - 10 \ge 8424 \ge 1$, coordinate $i = 11$ of each $v^{(j)}$ is $\pm 1$, hence $\gcd(v^{(j)}_1, \dots, v^{(j)}_n) = 1$ for every $j \in \{1, 2, 3, 4\}$.
4. **Integer Euclidean lengths totaling $4m$:**
   - $\|v^{(1)}\|_2^2 = 10 \cdot 2^2 + (n - 10)\cdot 1^2 = n + 30 = m^2 \implies \|v^{(1)}\|_2 = m$.
   - $\|v^{(2)}\|_2^2 = 4^2 + 5\cdot 2^2 + (n - 6)\cdot 1^2 = n + 30 = m^2 \implies \|v^{(2)}\|_2 = m$.
   - $\|v^{(3)}\|_2^2 = 3\cdot 3^2 + 2\cdot 2^2 + (n - 5)\cdot 1^2 = n + 30 = m^2 \implies \|v^{(3)}\|_2 = m$.
   - $\|v^{(4)}\|_2^2 = 5^2 + 2\cdot 2^2 + (n - 3)\cdot 1^2 = n + 30 = m^2 \implies \|v^{(4)}\|_2 = m$.
   Total walk length $= 4m$ (at $m = 92$, $n = 8434$, total length $= 368$).
5. **Pairwise noncongruent diagonals:**
   Ignoring the remaining $\pm 1$ entries, the multisets of coordinate magnitudes $> 1$ are:
   - $v^{(1)}$: $\{2^{10}\}$
   - $v^{(2)}$: $\{2^5, 4\}$
   - $v^{(3)}$: $\{2^2, 3^3\}$
   - $v^{(4)}$: $\{2^2, 5\}$
   These four multisets are pairwise distinct, so no two diagonals are congruent under signed coordinate permutations of $\mathbb{Z}^n$.

---

## 2. Proof That Every 3-Segment Closed Walk Has Length $\ge 4m + 2$ ($m \ge 92$)

Let $(u, v, w)$ be any valid 3-segment closed walk in $\mathbb{Z}^n$ ($n = m^2 - 30$, $m \ge 92$), with integer lengths $L_1 = \|u\|_2$, $L_2 = \|v\|_2$, $L_3 = \|w\|_2$. Without loss of generality, $L_1 \le L_2 \le L_3$.

1. **Minimum segment length $L_j \ge m$:**
   Since every coordinate of a valid diagonal is a nonzero integer, $\|u\|_2^2 \ge n = m^2 - 30$. For $m \ge 16$, $(m-1)^2 = m^2 - 2m + 1 \le m^2 - 31 < m^2 - 30 = n$, so $\|u\|_2 > m - 1$, hence $L_1 \ge m$ (and similarly $L_2, L_3 \ge m$).

2. **Parity:**
   For every $i \in \{1, \dots, n\}$, $u_i + v_i + w_i = 0$ gives $u_i^2 + v_i^2 + w_i^2 = 2(u_i^2 + u_i v_i + v_i^2) \equiv 0 \pmod 2$. Summing over $i$ yields $L_1^2 + L_2^2 + L_3^2 \equiv 0 \pmod 2$, whence $L_1 + L_2 + L_3 \equiv 0 \pmod 2$.

3. **Coordinate sum-of-squares bound $L_1^2 + L_2^2 + L_3^2 \ge 6n$:**
   In each coordinate $i$, $u_i, v_i, w_i \in \mathbb{Z} \setminus \{0\}$ satisfy $u_i + v_i + w_i = 0$. They cannot all lie in $\{\pm 1\}$ (the sum of three odd integers is odd, hence nonzero), so at least one has absolute value $\ge 2$ and the other two have absolute value $\ge 1$. Thus $u_i^2 + v_i^2 + w_i^2 \ge 2^2 + 1^2 + 1^2 = 6$. Summing over $i = 1, \dots, n$:
   $$L_1^2 + L_2^2 + L_3^2 \ge 6n = 6m^2 - 180.$$

4. **Strict triangle inequality $L_3 < L_1 + L_2$:**
   From $w = -(u + v)$ and the triangle inequality, $L_3 = \|u + v\|_2 \le \|u\|_2 + \|v\|_2 = L_1 + L_2$. Equality holds only if $u$ and $v$ are positive scalar multiples of each other ($v = \lambda u$ with $\lambda > 0$). Because both $u$ and $v$ are primitive ($\gcd = 1$), $\lambda = 1$ and $u = v$, contradicting that $u$ and $v$ are noncongruent. Hence $L_3 < L_1 + L_2$.

5. **Contradiction for $L_1 + L_2 + L_3 \le 4m$:**
   Assume for contradiction that $L_1 + L_2 + L_3 \le 4m$. Write
   $$L_1 = m + a, \qquad L_2 = m + b, \qquad L_3 = 2m - d,$$
   where $0 \le a \le b$ (since $m \le L_1 \le L_2$). Then:
   - $L_1 + L_2 + L_3 \le 4m \implies d \ge a + b \ge 0$.
   - $L_3 < L_1 + L_2 \implies 2m - d < 2m + a + b \implies d + a + b > 0$, which together with $d \ge a + b \ge 0$ forces $d \ge 1$.
   - $L_3 \ge L_2 \implies 2m - d \ge m + b \implies d \le m - b \le m$.

   If $d = m$, then $b = 0 \implies a = 0$, so $(L_1, L_2, L_3) = (m, m, m)$ and $L_1^2 + L_2^2 + L_3^2 = 3m^2 < 6m^2 - 180$ (since $3m^2 \ge 3\cdot 92^2 > 180$).

   Otherwise $1 \le d \le m - 1$. Using $d \ge a + b \ge 0$ and $a, b \ge 0$ (so $d^2 \ge (a+b)^2 \ge a^2 + b^2$), we have
   $$(m+d)^2 + m^2 - (m+a)^2 - (m+b)^2 = 2m(d - a - b) + (d^2 - a^2 - b^2) \ge 0,$$
   and therefore
   $$L_1^2 + L_2^2 + L_3^2 \le m^2 + (m+d)^2 + (2m - d)^2 = 6m^2 - 2d(m - d) \le 6m^2 - 2(m - 1).$$
   For $m \ge 92$, $2(m - 1) \ge 182 > 180$, so
   $$L_1^2 + L_2^2 + L_3^2 \le 6m^2 - 182 < 6m^2 - 180 = 6n,$$
   contradicting step 3.

Consequently, every 3-segment closed walk has total length $\ge 4m + 2$ (using step 2), while the explicit 4-segment walk in Section 1 has total length $4m$ (and in fact $a(m^2 - 30) = 4m$, since every $k$-segment walk with $k \ge 4$ has length $\ge k m \ge 4m$). This refutes the conjecture in `A386251`.

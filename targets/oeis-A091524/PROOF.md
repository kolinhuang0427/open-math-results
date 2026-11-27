# Proof of OEIS A091524 Conjecture (Kurkov 2024)

## Theorem
Let $(a(m))_{m \ge 1}$ be **OEIS A091524**, defined as follows: for each integer $m \ge 1$, let $(u_r^{(m)})_{r \ge 1}$ be the Graham–Pollak sequence (OEIS **A001521** / MathWorld *Graham–Pollak Sequence*)
$$u_1^{(m)} = m, \qquad u_{r+1}^{(m)} = \left\lfloor \sqrt{2 u_r^{(m)}\bigl(u_r^{(m)} + 1\bigr)} \right\rfloor = \left\lfloor \sqrt{2}\left(u_r^{(m)} + \frac{1}{2}\right) \right\rfloor \quad (r \ge 1),$$
let $d_j^{(m)} = u_{2j+2}^{(m)} - 2u_{2j}^{(m)}$ ($j \ge 1$) (equivalently $u_{2j+1}^{(m)} - 2u_{2j-1}^{(m)}$ with $0$-based indexing $u_0^{(m)} = m$), let $\alpha(m) = \sum_{j=1}^\infty d_j^{(m)} 2^{-j}$, and write $\alpha(m) = a(m)\sqrt{2} - b(m)$ with $a(m), b(m) \in \mathbb{Z}$. Let **A028982** denote the increasing enumeration of $\{k^2 : k \ge 1\} \cup \{2k^2 : k \ge 1\}$, and let **A006337** be given by $f(n) = \lfloor (n+1)\sqrt{2} \rfloor - \lfloor n\sqrt{2} \rfloor$ ($n \ge 1$). Then for every integer $n \ge 1$,
$$a(n) = \sqrt{\frac{\mathrm{A028982}(n)}{\mathrm{A006337}(n)}}.$$

---

## Proof

### 1. Beatty partition of $\mathbb{Z}_{\ge 1}$ and the ordered set $S$
Define the complementary Beatty sequences (**A003152** and **A003151**):
$$B_1(k) = \left\lfloor k\left(1 + \frac{1}{\sqrt{2}}\right) \right\rfloor = k + \left\lfloor \frac{k}{\sqrt{2}} \right\rfloor, \qquad B_2(k) = \bigl\lfloor k(1 + \sqrt{2}) \bigr\rfloor = k + \lfloor k\sqrt{2} \rfloor \qquad (k \ge 1).$$
Since $1 + \frac{1}{\sqrt{2}}$ and $1 + \sqrt{2}$ are irrational and $\frac{1}{1 + 1/\sqrt{2}} + \frac{1}{1 + \sqrt{2}} = \frac{\sqrt{2}}{\sqrt{2}+1} + \frac{1}{\sqrt{2}+1} = 1$, Beatty's theorem guarantees that $\{B_1(k) : k \ge 1\}$ and $\{B_2(k) : k \ge 1\}$ partition $\mathbb{Z}_{\ge 1}$ into two disjoint strictly increasing sequences.

Let $S = \mathbb{Z}_{\ge 1} \cup \sqrt{2}\mathbb{Z}_{\ge 1}$, whose elements are all distinct because $\sqrt{2} \notin \mathbb{Q}$, and list $S$ in strictly increasing order as $\tau_1 < \tau_2 < \tau_3 < \cdots$.
- For any $k \in \mathbb{Z}_{\ge 1}$, the elements of $S$ that are $\le k$ are $\{1, \dots, k\}$ and $\{j\sqrt{2} : 1 \le j \le \lfloor k/\sqrt{2} \rfloor\}$, so $k$ has rank $k + \lfloor k/\sqrt{2} \rfloor = B_1(k)$ in $S$, i.e. $\tau_{B_1(k)} = k$.
- For any $k \in \mathbb{Z}_{\ge 1}$, the elements of $S$ that are $\le k\sqrt{2}$ are $\{1\sqrt{2}, \dots, k\sqrt{2}\}$ and $\{j : 1 \le j \le \lfloor k\sqrt{2} \rfloor\}$, so $k\sqrt{2}$ has rank $k + \lfloor k\sqrt{2} \rfloor = B_2(k)$ in $S$, i.e. $\tau_{B_2(k)} = k\sqrt{2}$.

Hence every $m \ge 1$ corresponds to a unique $k \ge 1$ with either $m = B_1(k)$ ($\tau_m = k$) or $m = B_2(k)$ ($\tau_m = k\sqrt{2}$).

---

### 2. Evaluation of $u_r^{(m)}$, $\alpha(m)$, and $a(m)$
First note why the two forms of the Graham–Pollak recurrence coincide for every integer $u \ge 0$: since $2(u + \frac{1}{2})^2 = 2u(u + 1) + \frac{1}{2}$ and $2u(u + 1) \in \mathbb{Z}$, no integer square $N^2$ can lie in $(2u(u + 1),\, 2u(u + 1) + \frac{1}{2}]$, so $N \le \sqrt{2u(u + 1)} \iff N^2 \le 2u(u + 1) \iff N^2 \le 2u(u + 1) + \frac{1}{2} \iff N \le \sqrt{2}(u + \frac{1}{2})$ for all $N \in \mathbb{Z}_{\ge 0}$, giving $\lfloor \sqrt{2u(u + 1)} \rfloor = \lfloor \sqrt{2}(u + \frac{1}{2}) \rfloor$.

Fix $m \ge 1$ and set $x_r := \tau_m (2^{(r-1)/2} + 2^{(r-2)/2})$ for $r \ge 1$, so $x_{r+1} = \sqrt{2} x_r$.

- **Base case ($r = 1$):** Notice $x_1 = \tau_m(1 + 1/\sqrt{2})$. If $m = B_1(k)$ ($\tau_m = k$), then $\lfloor x_1 \rfloor = \lfloor k(1 + 1/\sqrt{2}) \rfloor = B_1(k) = m$; if $m = B_2(k)$ ($\tau_m = k\sqrt{2}$), then $\lfloor x_1 \rfloor = \lfloor k(\sqrt{2} + 1) \rfloor = B_2(k) = m$. Thus $u_1^{(m)} = \lfloor x_1 \rfloor$.

- **Inductive step ($u_r^{(m)} = \lfloor x_r \rfloor \implies u_{r+1}^{(m)} = \lfloor x_{r+1} \rfloor$):**
  Observe that $x_r = \tau_m 2^{(r-2)/2}(1 + \sqrt{2})$ has one of the two forms $K(1 + \sqrt{2}) = K + K\sqrt{2}$ or $K\sqrt{2}(1 + \sqrt{2}) = 2K + K\sqrt{2}$:
  - for $r \ge 2$, $2^{(r-2)/2} \in \{2^s, 2^s\sqrt{2}\}$ ($s \ge 0$) and $\tau_m \in \{k, k\sqrt{2}\}$, so $K \in \mathbb{Z}_{\ge 1}$;
  - for $r = 1$ and $\tau_m = k\sqrt{2}$, $x_1 = k(1 + \sqrt{2})$ (first form with $K = k \in \mathbb{Z}_{\ge 1}$);
  - for $r = 1$ and $\tau_m = k$, $x_1 = k + \frac{k}{2}\sqrt{2}$ (second form with $K = \frac{k}{2} \in \frac{1}{2}\mathbb{Z}_{\ge 1}$, so $2K = k \in \mathbb{Z}_{\ge 1}$ and $x_2 = k + k\sqrt{2}$).

  In every case $\alpha := \{x_r\} = \{K\sqrt{2}\} \in (0, 1) \setminus \{\frac{1}{2}\}$ (since $K \in \frac{1}{2}\mathbb{Z}_{\ge 1}$ and $\sqrt{2} \notin \mathbb{Q}$), and
  $$\sqrt{2}\left(\lfloor x_r \rfloor + \frac{1}{2}\right) - x_{r+1} = \sqrt{2}\left(\frac{1}{2} - \alpha\right).$$
  We verify $\lfloor x_{r+1} \rfloor \le \sqrt{2}(\lfloor x_r \rfloor + 1/2) < \lfloor x_{r+1} \rfloor + 1$, i.e. $-\{x_{r+1}\} \le \sqrt{2}(1/2 - \alpha) < 1 - \{x_{r+1}\}$:
  1. If $x_r = K + K\sqrt{2}$ (here $K \in \mathbb{Z}_{\ge 1}$), then $x_{r+1} = 2K + K\sqrt{2}$ has $\{x_{r+1}\} = \alpha$. Then
     $$\sqrt{2}\left(\frac{1}{2} - \alpha\right) + \alpha = \frac{\sqrt{2}}{2} - (\sqrt{2}-1)\alpha > \frac{\sqrt{2}}{2} - (\sqrt{2}-1) = 1 - \frac{\sqrt{2}}{2} > 0,$$
     $$1 - \alpha - \sqrt{2}\left(\frac{1}{2} - \alpha\right) = 1 - \frac{\sqrt{2}}{2} + (\sqrt{2}-1)\alpha > 1 - \frac{\sqrt{2}}{2} > 0.$$
  2. If $x_r = 2K + K\sqrt{2}$ (here $2K \in \mathbb{Z}_{\ge 1}$), then $x_{r+1} = 2K + 2K\sqrt{2}$ has $\{x_{r+1}\} = \{2K\sqrt{2}\} = \{2\alpha\}$.
     - If $\alpha < 1/2$, then $\{x_{r+1}\} = 2\alpha$, and
       $$\sqrt{2}\left(\frac{1}{2}-\alpha\right) + 2\alpha = \frac{\sqrt{2}}{2} + (2-\sqrt{2})\alpha > 0, \qquad 1 - 2\alpha - \sqrt{2}\left(\frac{1}{2}-\alpha\right) = 1 - \frac{\sqrt{2}}{2} - (2-\sqrt{2})\alpha > 0.$$
     - If $\alpha > 1/2$, then $\{x_{r+1}\} = 2\alpha - 1$, and
       $$\sqrt{2}\left(\frac{1}{2}-\alpha\right) + (2\alpha - 1) = (2-\sqrt{2})\left(\alpha - \frac{1}{2}\right) > 0, \qquad 2 - 2\alpha - \sqrt{2}\left(\frac{1}{2}-\alpha\right) = 2 - \frac{\sqrt{2}}{2} - (2-\sqrt{2})\alpha > \frac{\sqrt{2}}{2} > 0.$$

  In all cases $u_{r+1}^{(m)} = \lfloor \sqrt{2}(\lfloor x_r \rfloor + 1/2) \rfloor = \lfloor x_{r+1} \rfloor$.

By induction, $u_r^{(m)} = \lfloor \tau_m (2^{(r-1)/2} + 2^{(r-2)/2}) \rfloor$ for all $r \ge 1$. For even indices $r = 2j$ ($j \ge 1$):
- If $\tau_m = k$, $u_{2j}^{(m)} = \lfloor k \cdot 2^{j-1}(\sqrt{2} + 1) \rfloor = k \cdot 2^{j-1} + \lfloor 2^{j-1} k\sqrt{2} \rfloor$.
- If $\tau_m = k\sqrt{2}$, $u_{2j}^{(m)} = \lfloor k \cdot 2^{j-1}(2 + \sqrt{2}) \rfloor = k \cdot 2^j + \lfloor 2^{j-1} k\sqrt{2} \rfloor$.

In both cases the power-of-$2$ integer term cancels in $d_j^{(m)} = u_{2j+2}^{(m)} - 2u_{2j}^{(m)}$, leaving
$$d_j^{(m)} = \lfloor 2^j k\sqrt{2} \rfloor - 2\lfloor 2^{j-1} k\sqrt{2} \rfloor \in \{0, 1\},$$
which is the $j$-th binary digit after the binary point of $\{k\sqrt{2}\} = k\sqrt{2} - \lfloor k\sqrt{2} \rfloor$. Hence
$$\alpha(m) = \sum_{j=1}^\infty d_j^{(m)} 2^{-j} = k\sqrt{2} - \lfloor k\sqrt{2} \rfloor.$$
Since $\sqrt{2}$ is irrational, $a(m)\sqrt{2} - b(m) = k\sqrt{2} - \lfloor k\sqrt{2} \rfloor$ with $a(m), b(m) \in \mathbb{Z}$ uniquely forces $a(m) = k$, i.e.,
$$a\bigl(B_1(k)\bigr) = k, \qquad a\bigl(B_2(k)\bigr) = k \qquad (\forall k \ge 1).$$

---

### 3. Evaluations of A028982 and A006337 on $B_1(k)$ and $B_2(k)$
Let $c(n) = \mathrm{A028982}(n)$ be the increasing enumeration of $T = \{j^2 : j \ge 1\} \cup \{2j^2 : j \ge 1\}$ (disjoint since $\sqrt{2} \notin \mathbb{Q}$):
- The elements of $T$ that are $\le k^2$ are $\{1^2, \dots, k^2\}$ and $\{2j^2 : 1 \le j \le \lfloor k/\sqrt{2} \rfloor\}$, totaling $k + \lfloor k/\sqrt{2} \rfloor = B_1(k)$. Thus $c(B_1(k)) = k^2$.
- The elements of $T$ that are $\le 2k^2$ are $\{2\cdot 1^2, \dots, 2k^2\}$ and $\{j^2 : 1 \le j \le \lfloor k\sqrt{2} \rfloor\}$, totaling $k + \lfloor k\sqrt{2} \rfloor = B_2(k)$. Thus $c(B_2(k)) = 2k^2$.

Next let $f(n) = \mathrm{A006337}(n) = \lfloor (n+1)\sqrt{2} \rfloor - \lfloor n\sqrt{2} \rfloor$:
- At $n = B_1(k) = k + p$ with $p = \lfloor k/\sqrt{2} \rfloor$: write $k/\sqrt{2} = p + s$ where $s \in (0, 1)$, so $p\sqrt{2} = k - s\sqrt{2}$ and
  $$n\sqrt{2} = k\sqrt{2} + p\sqrt{2} = 2(p + s) + (k - s\sqrt{2}) = (2p + k) + s(2 - \sqrt{2}).$$
  Because $0 < s(2 - \sqrt{2}) < 2 - \sqrt{2} < 1$ and $1 < \sqrt{2} < s(2 - \sqrt{2}) + \sqrt{2} < 2$, we obtain $\lfloor n\sqrt{2} \rfloor = 2p + k$ and $\lfloor (n+1)\sqrt{2} \rfloor = 2p + k + 1$, giving $f(B_1(k)) = 1$.
- At $n = B_2(k) = k + q$ with $q = \lfloor k\sqrt{2} \rfloor$: write $k\sqrt{2} = q + r$ where $r \in (0, 1)$, so $q\sqrt{2} = 2k - r\sqrt{2}$ and
  $$n\sqrt{2} = k\sqrt{2} + q\sqrt{2} = (q + r) + (2k - r\sqrt{2}) = (2k + q) - r(\sqrt{2} - 1).$$
  Because $0 < r(\sqrt{2} - 1) < \sqrt{2} - 1 < 1$ and $1 < \sqrt{2} - r(\sqrt{2} - 1) < \sqrt{2} < 2$, we obtain $\lfloor n\sqrt{2} \rfloor = 2k + q - 1$ and $\lfloor (n+1)\sqrt{2} \rfloor = 2k + q + 1$, giving $f(B_2(k)) = 2$.

---

### 4. Conclusion
For every $n \ge 1$, Section 1 places $n$ uniquely in either $B_1$ or $B_2$:
- If $n = B_1(k)$, then $\sqrt{\frac{\mathrm{A028982}(n)}{\mathrm{A006337}(n)}} = \sqrt{\frac{k^2}{1}} = k = a(n)$.
- If $n = B_2(k)$, then $\sqrt{\frac{\mathrm{A028982}(n)}{\mathrm{A006337}(n)}} = \sqrt{\frac{2k^2}{2}} = k = a(n)$.

Thus $a(n) = \sqrt{\mathrm{A028982}(n)/\mathrm{A006337}(n)}$ for all $n \ge 1$. $\blacksquare$

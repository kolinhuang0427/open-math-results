# Proof of R. J. Mathar's D-Finite Recurrence for OEIS A108430

## Statement
For $n \ge 1$, let $a(n)$ be the total number of $d = (1, -1)$ steps across all lattice paths from $(0,0)$ to $(3n, 0)$ staying in the quadrant $x \ge 0, y \ge 0$ using steps $u = (2,1)$, $U = (1,2)$, and $d = (1,-1)$ (equivalently, $a(n) = \frac{1}{n} \sum_{k=n}^{2n} k \binom{n}{2n-k} \binom{n+k}{n-1}$). Then for every integer $n \ge 4$ (and also for $n = 3$ with $a(0) = 0$),
$$\begin{aligned}
0 &= n(2n+1)(23982n - 28681)\,a(n) + (-640736n^3 + 1168048n^2 - 901220n + 247035)\,a(n-1) \\
  &\quad + (1196488n^3 - 6448608n^2 + 10992587n - 5911365)\,a(n-2) + 2(2n-5)(28283n - 6993)(n-3)\,a(n-3).
\end{aligned}$$

---

## Proof

### Step 1: Generating Function and Equivalence with the Binomial Formula
Every path from $(0,0)$ to $(x,0)$ staying in $y \ge 0$ using steps $u=(2,1)$, $U=(1,2)$, $d=(1,-1)$ satisfies $0 = \Delta y = (\# u) + 2(\# U) - (\# d)$, hence $\# d = \# u + 2(\# U)$ and $x = 2(\# u) + (\# U) + (\# d) = 3(\# u + \# U)$, so $x = 3n$ is always a multiple of $3$.

Let $G(t, z) = \sum_{n, k \ge 0} T(n, k)\, t^k z^n$ count such paths of length $x = 3n$ having $k$ down-steps $d$. Every nonempty path begins with either $u$ or $U$:
- If it begins with $u = (2,1)$ (moving from height $0$ to $1$), since $d$ is the only downward step ($\Delta y = -1$), it must hit height $0$ for the first time via a $d$-step, uniquely decomposing as $u P_1 d P_2$ where $P_1, P_2$ are arbitrary valid paths shifted to heights $1$ and $0$ respectively; this contributes $t z G(t, z)^2$.
- If it begins with $U = (1,2)$ (moving from height $0$ to $2$), it must first reach height $1$ via a $d$-step and then reach height $0$ via a $d$-step, uniquely decomposing as $U P_1 d P_2 d P_3$; this contributes $t^2 z G(t, z)^3$.

Hence $G(t, z)$ satisfies
$$G(t, z) = 1 + t z G(t, z)^2\bigl(1 + t G(t, z)\bigr).$$
Writing $w = G(t,z) - 1 = z\bigl(t(1+w)^2 + t^2(1+w)^3\bigr)$, Lagrange inversion gives for $n \ge 1$:
$$[z^n] G(t, z) = \frac{1}{n} [w^{n-1}] \bigl(t(1+w)^2 + t^2(1+w)^3\bigr)^n = \frac{1}{n} \sum_{j=0}^{n} \binom{n}{j} t^{2n-j} \binom{3n-j}{n-1}.$$
Setting $k = 2n - j \in \{n, \dots, 2n\}$ and differentiating with respect to $t$ at $t = 1$ yields both $a(n) = [z^n] \left.\frac{\partial G}{\partial t}\right|_{t=1}$ and $a(n) = \frac{1}{n} \sum_{k=n}^{2n} k \binom{n}{2n-k} \binom{n+k}{n-1}$.

### Step 2: Algebraic Reduction in $\mathbb{Q}(z)[G]/(z G^3 + z G^2 - G + 1)$
Let $G_1(z) = G(1, z) = 1 + 2z + 10z^2 + \cdots$ (`A027307`), which satisfies the irreducible cubic
$$P(z, G_1) = z G_1^3 + z G_1^2 - G_1 + 1 = 0.$$
Differentiating $G(t, z) = 1 + t z G^2 + t^2 z G^3$ with respect to $t$ at $t = 1$ gives
$$A(z) = \sum_{n=1}^{\infty} a(n) z^n = \left.\frac{\partial G}{\partial t}\right|_{t=1} = \frac{z G_1^2 + 2z G_1^3}{1 - 2z G_1 - 3z G_1^2} \in \mathcal{A} := \mathbb{Q}(z)[G_1]/\bigl(P(z, G_1)\bigr).$$
Moreover, differentiating $P(z, G_1) = 0$ with respect to $z$ gives
$$G_1'(z) = \frac{G_1^3 + G_1^2}{1 - 2z G_1 - 3z G_1^2} \in \mathcal{A},$$
so the 3-dimensional $\mathbb{Q}(z)$-algebra $\mathcal{A}$ is closed under $\theta = z \frac{d}{dz}$ (which acts on power series by $\theta \sum a(n) z^n = \sum n a(n) z^n$).

Let $c_0(n), c_1(n), c_2(n), c_3(n)$ be the four cubic polynomials in Mathar's recurrence, and define $a(0) = a(-1) = a(-2) = 0$. Then
$$\Phi(z) := \sum_{n=1}^{\infty} \left(\sum_{r=0}^{3} c_r(n)\, a(n-r)\right) z^n = \sum_{r=0}^{3} c_r(\theta)\bigl[z^r A(z)\bigr] \in \mathcal{A}.$$
Exact arithmetic in $\mathcal{A} = \mathbb{Q}(z)[G_1]/(z G_1^3 + z G_1^2 - G_1 + 1)$ (verified in `verify.py`) yields
$$\Phi(z) = -42291 z - 49573 z^2.$$
Since $[z^n]\Phi(z) = 0$ for every $n \ge 3$, Mathar's recurrence holds for all $n \ge 4$ (and also at $n = 3$ with $a(0)=0$). $\square$

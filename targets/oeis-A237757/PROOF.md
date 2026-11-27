# Proof of Peter Bala's Conjectured Generating Function for OEIS A237757

## 1. Statement

For $N \ge 1$, let $a(N)$ denote the number of integer partitions of $N$ whose least part $m$ and number of parts $\ell$ satisfy $2m = \ell$ (so in particular $m \ge 1$ and $\ell = 2m$). We prove Peter Bala's conjectured generating function (OEIS **A237757**, `rev. 17`, Feb 02 2021):
$$\sum_{N \ge 1} a(N)\, q^N = \sum_{n \ge 0} \frac{q^{2(n+1)^2}}{\prod_{k=1}^{2n+1} (1 - q^k)}.$$

*(Equivalently, setting $m = n + 1 \ge 1$, the $n$-th summand is $q^{2m^2} \big/ \prod_{k=1}^{2m-1} (1 - q^k)$.)*

---

## 2. Bijective Proof

Fix any integer $N \ge 1$, and partition the set $\mathcal{P}(N)$ of all partitions $\lambda = (\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_\ell \ge 1)$ of $N$ satisfying $\ell = 2\lambda_\ell$ according to the value of the least part $m = \lambda_\ell \in \mathbb{Z}_{\ge 1}$:
$$\mathcal{P}(N) = \bigsqcup_{m \ge 1} \mathcal{P}_m(N),$$
where $\mathcal{P}_m(N)$ is the set of partitions $\lambda = (\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{2m})$ of $N$ with $\lambda_{2m} = m$ (i.e., $2m$ positive parts, each at least $m$, with the smallest equal to $m$).

For each fixed $m \ge 1$, define a map $\Phi_m$ on $\mathcal{P}_m(N)$ by subtracting $m$ from each of the $2m$ parts of $\lambda$:
$$\Phi_m(\lambda) = \mu := (\lambda_1 - m,\, \lambda_2 - m,\, \dots,\, \lambda_{2m-1} - m).$$
We verify that $\Phi_m$ is a bijection from $\mathcal{P}_m(N)$ onto the set $\mathcal{Q}_{\le 2m-1}(N - 2m^2)$ of all partitions of $N - 2m^2$ into **at most $2m - 1$ positive parts** (where the empty partition of $0$ is the unique partition of $0$ into at most $2m - 1$ parts):

1. **Well-definedness:** Since $\lambda_1 \ge \dots \ge \lambda_{2m} = m$, we have $\lambda_i - m \ge 0$ for $1 \le i \le 2m-1$ and $\lambda_{2m} - m = 0$. Dropping any trailing zeros leaves a partition $\mu$ with at most $2m - 1$ positive parts, whose sum is
   $$|\mu| = \sum_{i=1}^{2m-1} (\lambda_i - m) = \left(\sum_{i=1}^{2m} \lambda_i\right) - 2m \cdot m = N - 2m^2.$$
   In particular, $\mathcal{P}_m(N) = \emptyset$ whenever $N < 2m^2$, matching $\mathcal{Q}_{\le 2m-1}(N - 2m^2) = \emptyset$ for $N - 2m^2 < 0$.

2. **Invertibility:** Given any partition $\mu = (\mu_1 \ge \dots \ge \mu_r > 0)$ of $N - 2m^2$ with $0 \le r \le 2m - 1$, pad $\mu$ with $(2m - r)$ trailing zeros to obtain a weakly decreasing $2m$-tuple $(\mu_1, \dots, \mu_{2m-1}, 0)$ with $\mu_{2m} = 0$, and add $m$ to every entry:
   $$\Psi_m(\mu) := (\mu_1 + m,\, \mu_2 + m,\, \dots,\, \mu_{2m-1} + m,\, m).$$
   Then $\Psi_m(\mu)$ is a partition of $(N - 2m^2) + 2m^2 = N$ with $2m$ parts and least part $\mu_{2m} + m = m$, so $\Psi_m(\mu) \in \mathcal{P}_m(N)$. Clearly $\Psi_m$ and $\Phi_m$ are two-sided inverses.

3. **Conjugation and Generating Function:** By Ferrers-diagram conjugation ($\mu \mapsto \mu'$), partitions of $M = N - 2m^2$ into at most $2m - 1$ parts are in bijection with partitions of $M$ into parts of size **at most $2m - 1$**. By the standard generating function for partitions with bounded part sizes,
   $$\sum_{M \ge 0} \bigl|\mathcal{Q}_{\le 2m-1}(M)\bigr|\, q^M = \prod_{k=1}^{2m-1} \frac{1}{1 - q^k}.$$
   Therefore, for each fixed $m \ge 1$,
   $$\sum_{N \ge 1} \bigl|\mathcal{P}_m(N)\bigr|\, q^N = \sum_{N \ge 2m^2} \bigl|\mathcal{Q}_{\le 2m-1}(N - 2m^2)\bigr|\, q^N = \frac{q^{2m^2}}{\prod_{k=1}^{2m-1} (1 - q^k)}.$$
   Summing over all $m = n + 1 \ge 1$ ($n \ge 0$) — which is a finite sum in every degree $[q^N]$ since $2(n+1)^2 > N$ for sufficiently large $n$ — yields
   $$\sum_{N \ge 1} a(N)\, q^N = \sum_{m \ge 1} \frac{q^{2m^2}}{\prod_{k=1}^{2m-1} (1 - q^k)} = \sum_{n \ge 0} \frac{q^{2(n+1)^2}}{\prod_{k=1}^{2n+1} (1 - q^k)}. \qquad \blacksquare$$

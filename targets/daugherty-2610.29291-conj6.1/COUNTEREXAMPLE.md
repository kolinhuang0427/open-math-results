# Counterexample to Daugherty et al. (2026) Conjecture 6.1 (`conj:box`)

**Status:** Counterexample, verified by exact computation (awaiting independent checker and Pro auditor).

## Disproved Statement

Conjecture 6.1 (`\label{conj:box}`, Section 6 of Daugherty et al., `arXiv:2610.29291v1`) states:

> If $\lambda$ and $\mu$ are wide partitions where $\lambda_i = \mu_i + 1$ for some $i \in [\ell(\lambda)-1]$ and $\lambda_j = \mu_j$ when $j \neq i$, then $LT(\lambda) \geq LT(\mu)$.

## Explicit Counterexample ($n = 22 \to n = 23$)

Take
$$\mu = (6, 5, 5, 3, 2, 1), \qquad \lambda = (6, 5, 5, 3, 3, 1).$$
Note that this is the exact pair discussed by the authors immediately following Conjecture 6.1 (line 721 of `final.tex`).

1. **Both partitions are wide:**
   Every lower subpartition (and indeed every subpartition obtained by deleting any subset of rows) dominates its conjugate:
   - For $\mu = (6,5,5,3,2,1)$: $\mu' = (6,5,4,3,3,1)$, partial sums of $\mu$ are $(6, 11, 16, 19, 21, 22) \ge (6, 11, 15, 18, 21, 22)$. Lower subpartitions:
     - $(5,5,3,2,1)$ vs $(5,4,3,2,2)$: $(5,10,13,15,16) \ge (5,9,12,14,16)$;
     - $(5,3,2,1)$ vs $(4,3,2,1,1)$: $(5,8,10,11,11) \ge (4,7,9,10,11)$;
     - $(3,2,1)$ vs $(3,2,1)$; $(2,1)$ vs $(2,1)$; $(1)$ vs $(1)$.
   - For $\lambda = (6,5,5,3,3,1)$: $\lambda' = (6,5,5,3,3,1)$ (self-conjugate!), and lower subpartitions are:
     - $(5,5,3,3,1)$ vs $(5,4,4,2,2)$: $(5,10,13,16,17) \ge (5,9,13,15,17)$;
     - $(5,3,3,1)$ vs $(4,3,3,1,1)$: $(5,8,11,12,12) \ge (4,7,10,11,12)$;
     - $(3,3,1)$ vs $(3,2,2)$: $(3,6,7) \ge (3,5,7)$;
     - $(3,1)$ vs $(2,1,1)$; $(1)$ vs $(1)$.

2. **Box-addition relation:**
   $\ell(\lambda) = 6$, and $\lambda$ is obtained from $\mu$ by adding $1$ box to row $i = 5 \in \{1, 2, 3, 4, 5\} = [\ell(\lambda) - 1]$ ($\lambda_5 = 3 = \mu_5 + 1$, $\lambda_j = \mu_j$ for $j \neq 5$).

3. **Exact counts violate monotonicity:**
   Enumerating all Latin tableaux of shape $\rho$ and type $\rho'$ directly from Definition 2.5 (`verify.py`):
   $$LT(\mu) = LT((6,5,5,3,2,1)) = 56, \qquad LT(\lambda) = LT((6,5,5,3,3,1)) = 32 < 56.$$

*(Why monotonicity fails here: adding a box to row 5 forces row 5 to contain $\{1,2,3\}$ instead of $\{1,2\}$ and increases $\lambda'_3$ from $4$ to $5$, placing a 5th copy of symbol $3$ in row 5 (columns 1–3), which blocks that column from taking $3$ in rows 1–4 and forces a column-3 conflict above that eliminates configurations present in $\mu$.)*

### Additional Counterexamples Found
- $\mu = (6, 6, 4, 3, 2, 1)$ ($LT = 88$) $\to \lambda = (6, 6, 4, 3, 3, 1)$ ($LT = 64$), at $i = 5$, $n = 22 \to 23$.
- $\mu = (6, 6, 5, 3, 2, 1)$ ($LT = 2080$) $\to \lambda = (6, 6, 5, 3, 3, 1)$ ($LT = 1984$), at $i = 5$, $n = 23 \to 24$.

## Verification Command

```bash
.venv/bin/python targets/daugherty-2610.29291-conj6.1/verify.py
```
Prints `PASS`.

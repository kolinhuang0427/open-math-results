# Counterexample to Guo–Lin Conjecture 5.7 (`arXiv:2412.02932v1`, `\label{locond-3}`)

**Conjecture 5.7 (`arXiv:2412.02932v1`, Section 5.2, lines 1366–1368):**
> For any permutation $u$, we have $d_u \in \mathbb{Z}_{\geq 0}$,

where $\theta_w = |\mathrm{supp}(\mathfrak{S}_w(x))|$ is the number of monomials in the Schubert polynomial $\mathfrak{S}_w(x)$ and $d_u$ is defined recursively for $u \in S_m$ by
$$\theta_w = 1 + \sum_u d_u\, p_u(w), \qquad d_u = \theta_u - 1 - \sum_{\sigma \in S_\ell,\,\ell < m} d_\sigma\, p_\sigma(u).$$

---

## Explicit Counterexample: $u = 134562897 \in S_9$ ($d_u = -1$)

For the permutation $u = 134562897 = [1, 3, 4, 5, 6, 2, 8, 9, 7] \in S_9$:
$$\theta_{134562897} = 113, \qquad 1 + \sum_{\sigma \in S_\ell,\, \ell < 9} d_\sigma\, p_\sigma(u) = 114, \qquad d_{134562897} = -1 < 0.$$
(Combined with Guo–Lin's verification of $d_\sigma \ge 0$ for all $\sigma \in \bigsqcup_{m=1}^8 S_m$ in `main.tex` line 1370, $n = 9$ is the minimal permutation size of a counterexample.)

---

## Explicit Verification of $\theta_{134562897} = 113$

The permutation $u = 134562897$ has length $6$ and decomposes as $u = 134562 \cdot 897$ in commuting Coxeter generators ($134562 = s_2 s_3 s_4 s_5$ acting on $\{2,3,4,5,6\}$, $897 = s_7 s_8$ acting on $\{7,8,9\}$), with Lehmer code $(0, 1, 1, 1, 1, 0, 1, 1, 0)$. Since its two blocks are Grassmannian permutations separated by a fixed block boundary,
$$\mathfrak{S}_{134562897}(x) = e_4(x_1, x_2, x_3, x_4, x_5) \cdot e_2(x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8).$$
Indeed, $\nu_u = \mathfrak{S}_u(1,\dots,1) = \binom{5}{4}\binom{8}{2} = 5 \cdot 28 = 140$. Counting distinct monomials by how many variables from $\{x_6, x_7, x_8\}$ appear in the $e_2$ factor:
1. **Two variables from $\{x_6, x_7, x_8\}$:** $\binom{5}{4} \binom{3}{2} = 5 \cdot 3 = 15$ monomials.
2. **One variable from $\{x_6, x_7, x_8\}$ and one from $\{x_1,\dots,x_5\}$:** $e_4(x_1,\dots,x_5) e_1(x_1,\dots,x_5)$ has degree $5$ with exponents in $\{0,1,2\}$: either $(1,1,1,1,1)$ ($\binom{5}{5} = 1$ monomial) or one $2$, three $1$'s, one $0$ ($5 \binom{4}{3} = 20$ monomials), giving $21 \cdot 3 = 63$ monomials.
3. **Zero variables from $\{x_6, x_7, x_8\}$:** $e_4(x_1,\dots,x_5) e_2(x_1,\dots,x_5)$ has degree $6$ in $x_1,\dots,x_5$ with exponents in $\{0,1,2\}$: either two $2$'s, two $1$'s, one $0$ ($\binom{5}{2}\binom{3}{2} = 30$ monomials) or one $2$ and four $1$'s ($5 \binom{4}{4} = 5$ monomials), giving $35$ monomials.

Hence $\theta_{134562897} = 15 + 63 + 35 = 113$.

---

## Complete Table of Nonzero Subpattern Contributions

Across all $54$ proper distinct standardized subpatterns $\sigma$ appearing in $u = 134562897$, only the following $8$ patterns have $d_\sigma \neq 0$ (all others have $d_\sigma = 0$, matching Guo–Lin Table 3 for $m \le 5$ and Section 5.2 for $13452786$ where $c_{13452786} = 3, d_{13452786} = 4$):

| Pattern $\sigma$ | Length | $\theta_\sigma$ | $d_\sigma$ | Occurrences $p_\sigma(u)$ | Contribution $d_\sigma p_\sigma(u)$ |
|---|---:|---:|---:|---:|---:|
| `132` | 3 | 2 | 1 | 16 | 16 |
| `12453` | 5 | 6 | 1 | 11 | 11 |
| `13254` | 5 | 7 | 2 | 8 | 16 |
| `21453` | 5 | 6 | 1 | 4 | 4 |
| `132564` | 6 | 17 | 2 | 4 | 8 |
| `134265` | 6 | 13 | 2 | 12 | 24 |
| `1342675` | 7 | 36 | 3 | 6 | 18 |
| `13452786` | 8 | 67 | 4 | 4 | 16 |
| **Total** | | | | | **$113$** |

Therefore,
$$d_{134562897} = \theta_{134562897} - \left(1 + \sum_{\sigma \neq u} d_\sigma\, p_\sigma(u)\right) = 113 - (1 + 113) = -1 < 0.$$
Meanwhile $c_{134562897} = 0$ (since $p_\sigma(u)$ gives $1 + \sum_{\sigma \neq u} c_\sigma p_\sigma(u) = 140 = \nu_u$).

All values are independently verified in exact integer arithmetic by `verify.py` using both divided differences from $\mathfrak{S}_{w_0}$ and direct pipe-dream / elementary-symmetric polynomial enumeration.

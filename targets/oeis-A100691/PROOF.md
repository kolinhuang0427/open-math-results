# Resolution of R. J. Mathar's Conjecture on OEIS A100691 and A193641

## Summary

We settle R. J. Mathar's 2022 conjecture in OEIS **A100691** (`a(n) = A193641(n+2) - 3` for `n > 0`) completely under both natural interpretations of `a(n)`, uncovering an OEIS erratum in `A100691`:

1. **Sequence/Recurrence Reading (TRUE for all `n >= 1`):** Let `a_OEIS(n)` denote the sequence tabulated in OEIS `A100691` (`1, 4, 12, 30, 70, 158, 352, 780, ...`), which satisfies `a_OEIS(n) = 2*a_OEIS(n-1) + a_OEIS(n-3) + 6` for `n >= 4` with generating function `(1+z^2)(1+z+z^2) / ((1-z)(1-2z-z^3))`. We prove directly from the defining condition of `A193641` that `A193641(m) = 2*A193641(m-1) + A193641(m-3)` for all `m >= 3` (with `A193641(0..2) = 1, 1, 3`), which immediately implies `a_OEIS(n) = A193641(n+2) - 3` for **all `n >= 1`**.

2. **Combinatorial-Definition Reading (FALSE for all `n >= 5`, first counterexample `n = 5`):** Let `s(n)` denote the actual number of `n`-step self-avoiding paths starting at `(0,0)` on the triangular lattice strip `Z x {0, 1}`. By an exact finite-state column transfer matrix (verified against exact DFS for `0 <= n <= 15`),
   $$\sum_{n \ge 0} s(n) z^n = \frac{1 + z^2 - z^3 + z^5}{(1 - z)^2 (1 - 2z - z^3)} = 1 + 4z + 12z^2 + 30z^3 + 70z^4 + 160z^5 + 360z^6 + 802z^7 + \cdots,$$
   whereas the `A100691` generating function equals
   $$\frac{(1+z^2)(1+z+z^2)}{(1-z)(1-2z-z^3)} = \frac{1 + z^2 - z^3 - z^5}{(1 - z)^2 (1 - 2z - z^3)} = 1 + 4z + 12z^2 + 30z^3 + 70z^4 + 158z^5 + 352z^6 + 780z^7 + \cdots.$$
   Their difference is
   $$\sum_{n \ge 0} \bigl(s(n) - a_{\mathrm{OEIS}}(n)\bigr) z^n = \frac{2z^5}{(1 - z)^2 (1 - 2z - z^3)},$$
   which has strictly positive coefficients for all `n >= 5` (`2, 8, 22, 54, 126, ...`). Thus `s(n) = A193641(n+2) - 3` holds for `1 <= n <= 4` and **fails for every `n >= 5`**, starting at `s(5) = 160 != 158 = A193641(7) - 3`.

*(Note also an algebraic typo already present in line 1 of `A100691`'s Formula section: `(1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)]` is not equal to `1+2*(2+z^2)/((z-1)*(z^2+2*z-1))`.)*

---

## Part 1: Proof of the Linear Recurrence for `A193641` and Equivalence with `a_OEIS(n)`

### Definition (`A193641`)
An array `x = (x_1, ..., x_n) in {-1, 0, 1}^n` is *valid* if every position `i in {1, ..., n}` belongs to at least one contiguous subarray of length `1` (`x_i = 0`) or length `2` (`x_i + x_{i+1} = 0`, or `x_{i-1} + x_i = 0`) with sum `0`. (For `n = 0`, the empty array is valid: `b(0) = 1`.) Let `b(n) = A193641(n)` be the number of valid arrays of length `n`.

### Proof that `b(m) = 2*b(m-1) + b(m-3)` for all `m >= 3`
Partition all prefixes `(x_1, ..., x_n) in {-1, 0, 1}^n` in which every index `1 <= i <= n-1` is covered (by a length-1 or length-2 zero-sum contiguous subarray inside `x_1..x_n`) into three disjoint classes:
- `U(n)`: valid arrays of length `n` that either are empty (`n = 0`) or satisfy `x_n = 0`.
- `V(n)`: valid arrays of length `n` with `x_n in {-1, 1}` (so `x_n` is already covered, meaning `x_{n-1} = -x_n`).
- `W(n)`: arrays of length `n` in which `1, ..., n-1` are covered, `x_n in {-1, 1}`, and `x_n` is **not** covered inside `x_1..x_n` (meaning `n = 1`, or `x_{n-1} != -x_n`).

Clearly `b(n) = U(n) + V(n)` for all `n >= 0`, with initial values:
- `n = 0`: `U(0) = 1`, `V(0) = 0`, `W(0) = 0`, so `b(0) = 1`.
- `n = 1`: `U(1) = 1` (`[0]`), `V(1) = 0`, `W(1) = 2` (`[1], [-1]`), so `b(1) = 1`.

Appending one entry `x_{n+1} in {-1, 0, 1}` to any prefix of length `n >= 0` yields the exact transitions:
1. `U(n+1) = U(n) + V(n) = b(n)`: appending `0` to any valid length-`n` array yields a valid array ending in `0`, and `W(n)` cannot be followed by `0` because `x_n` would remain uncovered.
2. `W(n+1) = 2*U(n) + V(n)`: from `U(n)`, appending `1` or `-1` leaves `x_{n+1}` uncovered; from `V(n)`, appending `x_{n+1} = x_n` leaves `x_{n+1}` uncovered (since `x_n + x_{n+1} = 2 x_n != 0`).
3. `V(n+1) = V(n) + W(n)`: from `V(n)`, appending `x_{n+1} = -x_n` covers `x_{n+1}`; from `W(n)`, the unique valid choice is `x_{n+1} = -x_n`, which simultaneously covers both `x_n` and `x_{n+1}`.

From (1), `U(n) = b(n-1)` for all `n >= 1`, hence `V(n) = b(n) - b(n-1)` for all `n >= 1`.
Substituting into (2) for `n >= 2` gives:
$$W(n) = 2 U(n-1) + V(n-1) = 2 b(n-2) + (b(n-1) - b(n-2)) = b(n-1) + b(n-2).$$
Substituting `V(n) = b(n) - b(n-1)` and `W(n) = b(n-1) + b(n-2)` into (3) for `n >= 2` gives:
$$b(n+1) - b(n) = V(n+1) = V(n) + W(n) = \bigl(b(n) - b(n-1)\bigr) + \bigl(b(n-1) + b(n-2)\bigr) = b(n) + b(n-2).$$
Rearranging and setting `m = n+1 >= 3`, we obtain
$$b(m) = 2 b(m-1) + b(m-3) \qquad \text{for all } m \ge 3,$$
with initial values `b(0) = 1, b(1) = 1, b(2) = 3` (since `U(2) = b(1) = 1` and `V(2) = V(1) + W(1) = 2`).

### Proof of `a_OEIS(n) = b(n+2) - 3` for all `n >= 1`
Let `c(n) = b(n+2) - 3` for `n >= 1`. Then:
- `c(1) = b(3) - 3 = (2*3 + 1) - 3 = 4`,
- `c(2) = b(4) - 3 = (2*7 + 1) - 3 = 12`,
- `c(3) = b(5) - 3 = (2*15 + 3) - 3 = 30`,
- `c(4) = b(6) - 3 = (2*33 + 7) - 3 = 70`.

For all `n >= 4` (`n+2 >= 6 >= 3`),
$$c(n) = b(n+2) - 3 = 2 b(n+1) + b(n-1) - 3 = 2(c(n-1) + 3) + (c(n-3) + 3) - 3 = 2 c(n-1) + c(n-3) + 6.$$
Meanwhile, the OEIS `A100691` generating function
$$G_{\mathrm{OEIS}}(z) = \frac{(1+z^2)(1+z+z^2)}{(1-z)(1-2z-z^3)} = \frac{1 + z + 2z^2 + z^3 + z^4}{1 - 3z + 2z^2 - z^3 + z^4}$$
has initial coefficients `1, 4, 12, 30, 70` (agreeing with `c(1..4)` for `1 <= n <= 4`), and multiplying by `(1 - z)(1 - 2z - z^3)` gives `(1 - 2z - z^3) G_OEIS(z) = (1 + z + 2z^2 + z^3 + z^4)/(1 - z) = 1 + 2z + 4z^2 + 5z^3 + 6z^4/(1 - z)`, so `a_OEIS(n) - 2 a_OEIS(n-1) - a_OEIS(n-3) = 6` for all `n >= 4`. Since `c(n)` and `a_OEIS(n)` satisfy the exact same order-3 inhomogeneous recurrence for `n >= 4` and agree on `n = 1, 2, 3, 4`, `a_OEIS(n) = A193641(n+2) - 3` holds for all `n >= 1`.

---

## Part 2: Exact Transfer Matrix for Self-Avoiding Paths on the Triangular Strip `Z x {0, 1}`

The triangular lattice strip `Z x {0, 1}` has vertex set `V = Z x {0, 1}`, with horizontal edges `(x, y) -- (x+1, y)` (`y in {0, 1}`), vertical edges `(x, 0) -- (x, 1)`, and diagonal edges `(x-1, 1) -- (x, 0)`. Every vertex has degree `4` (and up to `Z`-translation and `(x, y) <-> (-x, 1-y)` symmetry, all starting vertices are equivalent to `s = (0, 0)`).

For `n >= 1`, every `n`-step self-avoiding path starting at `s = (0, 0)` corresponds bijectively to an undirected simple path subgraph of length `n` with endpoints `{s, t}` for some `t != s`. Sweeping column by column across the 3-edge cut `{(x-1, 0)-(x, 0), (x-1, 1)-(x, 0), (x-1, 1)-(x, 1)}` tracks a finite automaton with `8` reachable left-of-origin states (before `x = 0`) and `9` reachable right-of-origin states (from `x = 0` onward). Solving the exact rational linear systems `(I - M_L(z)) v_L = e_init` and `(I - M_R(z)) v_R = M_0(z) v_L` symbolically over `Q(z)` in `verify.py` yields:
$$F_{\mathrm{SAW}}(z) = 1 + \sum_{n \ge 1} s(n) z^n = \frac{1 + z^2 - z^3 + z^5}{(1 - z)^2 (1 - 2z - z^3)}.$$
Comparing with `G_OEIS(z) = (1 + z^2 - z^3 - z^5) / ((1 - z)^2 (1 - 2z - z^3))`, we obtain:
$$F_{\mathrm{SAW}}(z) - G_{\mathrm{OEIS}}(z) = \frac{2z^5}{(1 - z)^2 (1 - 2z - z^3)}.$$
Since `1 / ((1 - z)^2 (1 - 2z - z^3))` is a product of power series with strictly positive coefficients (`1/(1-z)^2 = sum_{k>=0} (k+1) z^k` and `1/(1-2z-z^3)` has all nonnegative coefficients `1, 2, 4, 9, ...`), `s(n) > a_OEIS(n) = A193641(n+2) - 3` for **every** `n >= 5`, with first counterexample `n = 5`: `s(5) = 160` vs `A193641(7) - 3 = 158`.

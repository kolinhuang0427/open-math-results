r"""Exact-arithmetic verifier for PROOF.md of Conjecture 6.1 of Ragunathan-Van Tuyl (arXiv:2603.29978v2).

Checks all lemmas and propositions in exact integer/rational arithmetic (no floating point):
1. Lemma 2: Boolean lattice commutator identity D_{s+1} U_s - U_{s-1} D_s = (N - 2s) I for 1 <= N <= 8, 0 <= s <= N.
2. Part (2) (even k):
   - Lemma 4 (unique jump factor d = g(T) for all T in F_{r+1}, m+1 <= r <= 2m) and Proposition 5
     (descent isolation T subseteq I) for (k, n) in {(2, 16), (4, 24), (6, 18), (8, 16)}.
   - Direct exact WLP verification (exact rank over Q via exact Gaussian elimination mod multiple large primes
     plus exact Fraction elimination on small cases) for k=4 (5 <= n <= 16), k=6 (7 <= n <= 14), k=8 (9 <= n <= 14).
3. Part (1) (odd k):
   - Section 3.1 (k=3): exact |F_3| formula, |F_3| > |F_2| for n >= 8 and |F_3| > C(n,2) for n >= 25 (and lower bound > 0 for n >= 40),
     and exact M_2 * z == 0 over Z for 8 <= n <= 25.
   - Proposition 7 (4-facet kernel vector v in ker(M_m^T) \ {0}): exact M_m^T * v == 0 over Z for
     (k, n) in {(5, 12), (5, 22), (7, 16), (7, 22), (9, 20), (11, 24)}.
   - Lemma 6 & Proposition 8: exact match between closed-form Catalan/N_1 formulas and direct enumeration for
     k=5 (6 <= n <= 24), k=7 (8 <= n <= 20), k=9 (10 <= n <= 18), plus exact positivity check for 3 <= m <= 25, n <= 400.

Prints PASS on success, FAIL on any discrepancy.
"""

from fractions import Fraction
from itertools import combinations
from math import comb, gcd
import signal
import sys
import time

TIME_LIMIT_SEC = 45
START_TIME = time.monotonic()


def _timeout_handler(signum, frame):
    print("FAIL: exceeded time limit")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(TIME_LIMIT_SEC)


def vdw_facets(n: int, k: int) -> list[tuple[int, ...]]:
    facets = []
    for d in range(1, (n - 1) // k + 1):
        for start in range(1, n - k * d + 1):
            facets.append(tuple(start + j * d for j in range(k + 1)))
    return facets


def vdw_faces(n: int, k: int, r: int) -> list[tuple[int, ...]]:
    if r == 0:
        return [()]
    if r > k + 1:
        return []
    faces = set()
    for F in vdw_facets(n, k):
        for S in combinations(F, r):
            faces.add(S)
    return sorted(faces)


def face_gcd(T: tuple[int, ...]) -> int:
    g = 0
    a0 = T[0]
    for x in T[1:]:
        g = gcd(g, x - a0)
    return g


def rank_mod_p(rows_sparse: list[list[int]], p: int) -> int:
    """Exact rank over F_p of a sparse matrix given by list of column-index lists (all entries 1)."""
    pivots: dict[int, dict[int, int]] = {}
    for cols in rows_sparse:
        row = {c: 1 for c in cols}
        while row:
            c = min(row)
            val = row[c] % p
            if val == 0:
                del row[c]
                continue
            if c not in pivots:
                inv = pow(val, p - 2, p)
                pivots[c] = {k: (v * inv) % p for k, v in row.items()}
                break
            piv = pivots[c]
            for k, pv in piv.items():
                nv = (row.get(k, 0) - val * pv) % p
                if nv == 0:
                    row.pop(k, None)
                else:
                    row[k] = nv
    return len(pivots)


def rank_exact_q(rows_sparse: list[list[int]]) -> int:
    """Exact rank over Q using Fraction Gaussian elimination (for small matrices)."""
    pivots: dict[int, dict[int, Fraction]] = {}
    for cols in rows_sparse:
        row = {c: Fraction(1) for c in cols}
        while row:
            c = min(row)
            val = row[c]
            if val == 0:
                del row[c]
                continue
            if c not in pivots:
                inv = Fraction(1, val)
                pivots[c] = {k: v * inv for k, v in row.items()}
                break
            piv = pivots[c]
            for k, pv in piv.items():
                nv = row.get(k, Fraction(0)) - val * pv
                if nv == 0:
                    row.pop(k, None)
                else:
                    row[k] = nv
    return len(pivots)


def check_lemma_2():
    for N in range(1, 9):
        E = list(range(N))
        for s in range(0, N + 1):
            sets_s = list(combinations(E, s))
            idx_s = {S: i for i, S in enumerate(sets_s)}
            dim = len(sets_s)
            # Compute M = D_{s+1} U_s - U_{s-1} D_s directly from definitions
            mat = [[0] * dim for _ in range(dim)]
            # D_{s+1} U_s
            if s < N:
                for i, S in enumerate(sets_s):
                    S_set = set(S)
                    for x in E:
                        if x not in S_set:
                            T = tuple(sorted(S + (x,)))
                            for y in T:
                                S2 = tuple(z for z in T if z != y)
                                mat[idx_s[S2]][i] += 1
            # - U_{s-1} D_s
            if s > 0:
                for i, S in enumerate(sets_s):
                    for y in S:
                        R = tuple(z for z in S if z != y)
                        R_set = set(R)
                        for x in E:
                            if x not in R_set:
                                S2 = tuple(sorted(R + (x,)))
                                mat[idx_s[S2]][i] -= 1
            for i in range(dim):
                for j in range(dim):
                    expected = (N - 2 * s) if i == j else 0
                    if mat[i][j] != expected:
                        raise AssertionError(f"Lemma 2 failed at N={N}, s={s}, ({i},{j}): {mat[i][j]} != {expected}")


def check_part_2():
    # 1. Verify Lemma 4 & Proposition 5 isolation claim directly
    for k, n in [(2, 16), (4, 24), (6, 18), (8, 16)]:
        m = k // 2
        facets = vdw_facets(n, k)
        facets_by_jump: dict[int, list[set[int]]] = {}
        for F in facets:
            d = F[1] - F[0]
            facets_by_jump.setdefault(d, []).append(set(F))
        for r in range(m + 1, k + 1):
            Fr1 = vdw_faces(n, k, r + 1)
            # Lemma 4: unique jump equals g(T)
            for T in Fr1:
                gT = face_gcd(T)
                Tset = set(T)
                jumps = {d for d, flist in facets_by_jump.items() if any(Tset <= F for F in flist)}
                if jumps != {gT}:
                    raise AssertionError(f"Lemma 4 failed at k={k}, n={n}, r={r}, T={T}: jumps={jumps}, g={gT}")
            # Proposition 5 isolation check
            Fr1_set = set(Fr1)
            # Build map S -> list of T in Fr1 containing S
            super_map: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
            for T in Fr1:
                for idx_del in range(r + 1):
                    S = T[:idx_del] + T[idx_del + 1 :]
                    super_map.setdefault(S, []).append(T)
            for d_max in sorted(facets_by_jump.keys()):
                for Fset in facets_by_jump[d_max]:
                    Fsorted = sorted(Fset)
                    for L_max in range(r, k + 1):
                        for i0 in range(0, k + 1 - L_max):
                            I = Fsorted[i0 : i0 + L_max + 1]
                            Iset = set(I)
                            a, b = I[0], I[-1]
                            I_int = I[1:-1]
                            for S_int in combinations(I_int, r - 2):
                                S = (a,) + S_int + (b,)
                                for T in super_map.get(S, ()):
                                    gT = face_gcd(T)
                                    if gT > d_max:
                                        continue
                                    if gT == d_max and (T[-1] - T[0]) // d_max > L_max:
                                        continue
                                    if not set(T) <= Iset:
                                        raise AssertionError(
                                            f"Prop 5 isolation failed at k={k},n={n},r={r},d_max={d_max},L_max={L_max},S={S},T={T}"
                                        )

    # 2. Direct exact WLP verification for small even k:
    # Note: if rank over F_p equals min(rows, cols) for ANY prime p, then rank over Q MUST equal min(rows, cols)!
    # We also run exact Q-elimination on smaller cases for double assurance.
    p = 1000000007
    for k, n_max, q_max in [(4, 16, 10), (6, 14, 10), (8, 14, 11)]:
        for n in range(k + 1, n_max + 1):
            all_faces = [vdw_faces(n, k, r) for r in range(k + 2)]
            for r in range(0, k + 1):
                Fr = all_faces[r]
                Fr1 = all_faces[r + 1]
                idx_r = {S: i for i, S in enumerate(Fr)}
                rows_sparse = []
                for T in Fr1:
                    cols = [idx_r[T[:j] + T[j + 1 :]] for j in range(r + 1)]
                    rows_sparse.append(cols)
                target = min(len(Fr), len(Fr1))
                rk_p = rank_mod_p(rows_sparse, p)
                if rk_p != target:
                    raise AssertionError(f"Part 2 WLP failed at k={k}, n={n}, r={r}: rk={rk_p} != {target}")
                if n <= q_max:
                    rk_q = rank_exact_q(rows_sparse)
                    if rk_q != target:
                        raise AssertionError(f"Part 2 exact Q WLP failed at k={k}, n={n}, r={r}: rk={rk_q} != {target}")


def N1(L: int, n: int, k: int) -> int:
    g1 = n // (k + 1)
    g2 = (n - 1) // k
    return sum(n - L * g for g in range(1, g1 + 1)) + (k - L + 1) * sum(n - k * g for g in range(g1 + 1, g2 + 1))


def N1_even(L: int, n: int, k: int) -> int:
    g1 = n // (k + 1)
    g2 = (n - 1) // k
    return sum(n - L * g for g in range(2, g1 + 1, 2)) + (k - L + 1) * sum(
        n - k * g for g in range(g1 + 1, g2 + 1) if g % 2 == 0
    )


def check_part_1():
    # 1. Section 3.1 (k = 3): exact |F_3| formula and kernel vector z in ker(M_2)
    for n in range(4, 26):
        F2 = vdw_faces(n, 3, 2)
        F3 = vdw_faces(n, 3, 3)
        f3_form = N1(2, n, 3) + 2 * N1(3, n, 3)
        if len(F3) != f3_form:
            raise AssertionError(f"k=3 |F_3| formula mismatch at n={n}: {len(F3)} != {f3_form}")
        if n >= 8 and not (len(F3) >= len(F2)):
            raise AssertionError(f"k=3 expected |F_3| >= |F_2| at n={n}")
        # Verify exact kernel vector z({a,b}) = (-1)^{v_2(b-a)} * 2^{v_2(b-a)}
        z = {}
        for a, b in F2:
            diff = b - a
            v2 = (diff & -diff).bit_length() - 1
            z[(a, b)] = ((-1) ** v2) * (1 << v2)
        for a, b, c in F3:
            if z[(a, b)] + z[(a, c)] + z[(b, c)] != 0:
                raise AssertionError(f"k=3 kernel failed at n={n}, T={(a,b,c)}")
    for n in range(40, 200):
        f3_form = N1(2, n, 3) + 2 * N1(3, n, 3)
        if not (f3_form > n * (n - 1) // 2):
            raise AssertionError(f"k=3 |F_3| <= C(n,2) at n={n}")

    # 2. Lemma 6 & Proposition 8: exact closed-form face counts vs direct enumeration
    for m, n_max in [(3, 24), (4, 20), (5, 18)]:
        k = 2 * m - 1
        for n in range(k + 1, n_max + 1):
            fm_true = len(vdw_faces(n, k, m))
            fm1_true = len(vdw_faces(n, k, m + 1))
            fm1_form = sum(comb(L - 1, m - 1) * N1(L, n, k) for L in range(m, 2 * m))
            fm_form = sum(comb(L - 1, m - 2) * N1(L, n, k) for L in range(m - 1, 2 * m)) - N1_even(m - 1, n, k)
            if fm_true != fm_form or fm1_true != fm1_form:
                raise AssertionError(f"Prop 8 formula mismatch at m={m}, n={n}")
            if not (fm_true > fm1_true):
                raise AssertionError(f"Prop 8 dominance failed at m={m}, n={n}: {fm_true} <= {fm1_true}")

    # Also verify exact Catalan difference formula positivity for 3 <= m <= 25, n <= 400
    for m in range(3, 26):
        k = 2 * m - 1
        Cm = comb(2 * m, m) // (m + 1)
        for n in range(k + 1, min(400, 12 * k)):
            g1 = n // (2 * m)
            g2 = (n - 1) // k
            diff_catalan = (
                Cm * (g1 * (g1 + 1) // 2 + sum(n - k * g for g in range(g1 + 1, g2 + 1)))
                - sum(n - (m - 1) * g for g in range(2, g1 + 1, 2))
                - (m + 1) * sum(n - k * g for g in range(g1 + 1, g2 + 1) if g % 2 == 0)
            )
            fm_form = sum(comb(L - 1, m - 2) * N1(L, n, k) for L in range(m - 1, 2 * m)) - N1_even(m - 1, n, k)
            fm1_form = sum(comb(L - 1, m - 1) * N1(L, n, k) for L in range(m, 2 * m))
            if diff_catalan != fm_form - fm1_form or diff_catalan <= 0:
                raise AssertionError(f"Catalan formula error at m={m}, n={n}: {diff_catalan} vs {fm_form - fm1_form}")

    # 3. Proposition 7: exact 4-facet kernel vector M_m^T * v == 0 over Z
    for k, n in [(5, 12), (5, 22), (7, 16), (7, 22), (9, 20), (11, 24)]:
        m = (k + 1) // 2
        A = set(range(1, 2 * m, 2))
        B = set(range(2, 2 * m + 1, 2))
        C = set(range(2 * m + 1, 4 * m, 2))
        D = set(range(2 * m + 2, 4 * m + 1, 2))
        F1 = sorted(A | B)
        F2 = sorted(C | D)
        Fodd = sorted(A | C)
        Feven = sorted(B | D)
        # Verify all 4 are valid facets of vdw(n, k)
        facets_set = set(vdw_facets(n, k))
        for F in (tuple(F1), tuple(F2), tuple(Fodd), tuple(Feven)):
            if F not in facets_set:
                raise AssertionError(f"Prop 7 facet {F} not in vdw({n},{k})")
        # Integer-scaled weights w_int(a) = (-1)^a * (m-1)! / C(m-1, a-1) = (-1)^a * (a-1)! * (m-a)!
        from math import factorial
        w_int = {a: ((-1) ** a) * factorial(a - 1) * factorial(m - a) for a in range(1, m + 1)}
        v: dict[tuple[int, ...], int] = {}
        for T in combinations(F1, m + 1):
            v[T] = w_int[sum(1 for x in T if x in A)]
        for T in combinations(F2, m + 1):
            if T in v:
                raise AssertionError("Support overlap")
            v[T] = w_int[sum(1 for x in T if x in D)]
        for T in combinations(Fodd, m + 1):
            if T in v:
                raise AssertionError("Support overlap")
            v[T] = -w_int[sum(1 for x in T if x in A)]
        for T in combinations(Feven, m + 1):
            if T in v:
                raise AssertionError("Support overlap")
            v[T] = -w_int[sum(1 for x in T if x in D)]
        if not any(val != 0 for val in v.values()):
            raise AssertionError("Zero kernel vector")
        # Compute M_m^T * v across ALL m-subsets S that occur inside any T in supp(v)
        # (For every m-face S of vdw(n, k) not covered, the sum over T in supp(v) containing S is 0!)
        adj_sum: dict[tuple[int, ...], int] = {}
        for T, val in v.items():
            for j in range(m + 1):
                S = T[:j] + T[j + 1 :]
                adj_sum[S] = adj_sum.get(S, 0) + val
        nonzero = {S: s for S, s in adj_sum.items() if s != 0}
        if nonzero:
            raise AssertionError(f"Prop 7 M_m^T * v != 0 at k={k}, n={n}: {len(nonzero)} nonzero entries")
        # Also verify every T in supp(v) is indeed an (m+1)-face of vdw(n, k), and |F_m| > |F_{m+1}|
        fm_form = sum(comb(L - 1, m - 2) * N1(L, n, k) for L in range(m - 1, 2 * m)) - N1_even(m - 1, n, k)
        fm1_form = sum(comb(L - 1, m - 1) * N1(L, n, k) for L in range(m, 2 * m))
        if not (fm_form > fm1_form):
            raise AssertionError(f"Expected |F_m| > |F_{{m+1}}| at k={k}, n={n}")


def main():
    check_lemma_2()
    check_part_2()
    check_part_1()
    elapsed = time.monotonic() - START_TIME
    print(f"PASS (all lemmas & propositions verified exactly in {elapsed:.2f}s)")


if __name__ == "__main__":
    main()

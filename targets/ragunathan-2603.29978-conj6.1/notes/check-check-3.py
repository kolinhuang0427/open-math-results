"""Independent exact-arithmetic verifier for targets/ragunathan-2603.29978-conj6.1/."""

from fractions import Fraction
import itertools
from math import comb, gcd
import signal

signal.alarm(50)


def vdw_facets(n: int, k: int) -> list[frozenset[int]]:
    facets = []
    max_d = (n - 1) // k
    for d in range(1, max_d + 1):
        for i in range(1, n - k * d + 1):
            facets.append(frozenset(i + j * d for j in range(k + 1)))
    return facets


def vdw_faces_by_size(n: int, k: int) -> dict[int, list[tuple[int, ...]]]:
    facets = vdw_facets(n, k)
    by_size: dict[int, set[tuple[int, ...]]] = {r: set() for r in range(k + 2)}
    by_size[0].add(())
    for f in facets:
        fs = sorted(f)
        for r in range(1, k + 2):
            for sub in itertools.combinations(fs, r):
                by_size[r].add(sub)
    return {r: sorted(s) for r, s in by_size.items()}


def incidence_matrix_rows(faces_low: list[tuple[int, ...]], faces_high: list[tuple[int, ...]]) -> list[list[Fraction]]:
    idx_low = {s: i for i, s in enumerate(faces_low)}
    rows = []
    for t in faces_high:
        row = [Fraction(0)] * len(faces_low)
        for s in itertools.combinations(t, len(t) - 1):
            row[idx_low[s]] = Fraction(1)
        rows.append(row)
    return rows


def exact_rank_fraction(mat: list[list[Fraction]]) -> int:
    if not mat or not mat[0]:
        return 0
    rows = [r[:] for r in mat]
    m, n = len(rows), len(rows[0])
    rank = 0
    for c in range(n):
        piv = None
        for r in range(rank, m):
            if rows[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = Fraction(1) / rows[rank][c]
        for j in range(c, n):
            rows[rank][j] *= inv
        for r in range(m):
            if r != rank and rows[r][c] != 0:
                fac = rows[r][c]
                for j in range(c, n):
                    rows[r][j] -= fac * rows[rank][j]
        rank += 1
        if rank == m:
            break
    return rank


def gap_gcd(xs: tuple[int, ...]) -> int:
    g = 0
    for x in xs[1:]:
        g = gcd(g, x - xs[0])
    return g


def N1_formula(L: int, n: int, k: int, even_only: bool = False) -> int:
    g1 = n // (k + 1)
    g2 = (n - 1) // k
    total = 0
    for g in range(1, g1 + 1):
        if even_only and (g % 2 != 0):
            continue
        total += n - L * g
    for g in range(g1 + 1, g2 + 1):
        if even_only and (g % 2 != 0):
            continue
        total += (k - L + 1) * (n - k * g)
    return total


def check_lemma2_commutator() -> None:
    for N in range(1, 9):
        subsets = {s: sorted(itertools.combinations(range(N), s)) for s in range(N + 1)}
        idx = {s: {t: i for i, t in enumerate(subsets[s])} for s in range(N + 1)}
        U_mats = {}
        D_mats = {}
        for s in range(N):
            U = [[0] * len(subsets[s]) for _ in range(len(subsets[s + 1]))]
            for j, S in enumerate(subsets[s]):
                Sset = set(S)
                for x in range(N):
                    if x not in Sset:
                        T = tuple(sorted(S + (x,)))
                        U[idx[s + 1][T]][j] = 1
            U_mats[s] = U
            D = [[U[i][j] for i in range(len(subsets[s + 1]))] for j in range(len(subsets[s]))]
            D_mats[s + 1] = D

        for s in range(N + 1):
            sz = len(subsets[s])
            DU = [[0] * sz for _ in range(sz)]
            UD = [[0] * sz for _ in range(sz)]
            if s < N:
                D, U = D_mats[s + 1], U_mats[s]
                for i in range(sz):
                    for k_idx in range(len(subsets[s + 1])):
                        dik = D[i][k_idx]
                        if dik:
                            for j in range(sz):
                                DU[i][j] += dik * U[k_idx][j]
            if s > 0:
                U, D = U_mats[s - 1], D_mats[s]
                for i in range(sz):
                    for k_idx in range(len(subsets[s - 1])):
                        uik = U[i][k_idx]
                        if uik:
                            for j in range(sz):
                                UD[i][j] += uik * D[k_idx][j]
            for i in range(sz):
                for j in range(sz):
                    expected = (N - 2 * s) if i == j else 0
                    assert DU[i][j] - UD[i][j] == expected

    print("Lemma 2 PASS: DU - UD == (N - 2s)I verified exactly for 1 <= N <= 8, 0 <= s <= N.")


def check_even_part() -> None:
    # Exact WLP via rational rank on small even k cases
    for k, n_max in [(2, 9), (4, 9), (6, 9)]:
        for n in range(k + 1, n_max + 1):
            faces = vdw_faces_by_size(n, k)
            for r in range(k + 1):
                M = incidence_matrix_rows(faces[r], faces[r + 1])
                rk = exact_rank_fraction(M)
                assert rk == min(len(faces[r]), len(faces[r + 1]))

    # Lemma 4 & Proposition 5 isolation check on larger (n, k)
    for k, n in [(4, 15), (6, 14)]:
        m = k // 2
        facets = vdw_facets(n, k)
        facet_jumps: dict[frozenset[int], int] = {f: gap_gcd(tuple(sorted(f))) for f in facets}
        faces = vdw_faces_by_size(n, k)
        for r in range(m + 1, 2 * m + 1):
            # Lemma 4: unique facet jump for every (r+1)-face T
            jump_of_T: dict[tuple[int, ...], int] = {}
            for T in faces[r + 1]:
                Tset = frozenset(T)
                gT = gap_gcd(T)
                containing = [facet_jumps[f] for f in facets if Tset <= f]
                assert containing and all(d == gT for d in containing)
                jump_of_T[T] = gT

            # Prop 5 isolation: test every (d_max, L_max, T0, S_circ)
            face_r1_set = set(faces[r + 1])
            for T0 in faces[r + 1]:
                d_max = jump_of_T[T0]
                L_max = (T0[-1] - T0[0]) // d_max
                a, b = T0[0], T0[-1]
                I = tuple(range(a, b + 1, d_max))
                assert len(I) == L_max + 1
                I_circ = I[1:-1]
                for S_circ in itertools.combinations(I_circ, r - 2):
                    S = tuple(sorted((a, b) + S_circ))
                    # Check all T > S in F_{r+1} with g(T) <= d_max and (if == d_max) L(T) <= L_max
                    Sset = set(S)
                    for x in range(1, n + 1):
                        if x in Sset:
                            continue
                        T = tuple(sorted(S + (x,)))
                        if T not in face_r1_set:
                            continue
                        d_p = jump_of_T[T]
                        if d_p < d_max or (d_p == d_max and (T[-1] - T[0]) // d_p <= L_max):
                            assert set(T) <= set(I), f"Isolation failed: T={T} not in I={I}"

    print("Even Part PASS: exact rational WLP (k=2,4,6; n<=9) and Lemma 4 / Prop 5 isolation verified.")


def check_odd_k3() -> None:
    # Paper Theorem 4.2 exact WLP classification for k=3, n=4..10
    for n in range(4, 11):
        faces = vdw_faces_by_size(n, 3)
        wlp = all(
            exact_rank_fraction(incidence_matrix_rows(faces[r], faces[r + 1]))
            == min(len(faces[r]), len(faces[r + 1]))
            for r in range(4)
        )
        assert wlp == (n in (4, 5, 6)), f"Unexpected WLP={wlp} at (n={n}, k=3)"

    # Exact f-vector formula + lower bound + explicit z in ker(M2)
    def v2(t: int) -> int:
        c = 0
        while t % 2 == 0:
            t //= 2
            c += 1
        return c

    for n in range(7, 26):
        faces = vdw_faces_by_size(n, 3)
        f3_formula = N1_formula(2, n, 3) + 2 * N1_formula(3, n, 3)
        assert len(faces[3]) == f3_formula
        if n == 8:
            assert len(faces[3]) == len(faces[2]) == 24
        elif n >= 9:
            assert len(faces[3]) > len(faces[2])
        # Verify M_2 z = 0 identically for z({a,b}) = (-1)^{v2(b-a)} * 2^{v2(b-a)}
        z = {pair: ((-1) ** v2(pair[1] - pair[0])) * (2 ** v2(pair[1] - pair[0])) for pair in faces[2]}
        assert any(val != 0 for val in z.values())
        for a, b, c in faces[3]:
            assert z[(a, b)] + z[(a, c)] + z[(b, c)] == 0

    for n in range(40, 120):
        f3 = N1_formula(2, n, 3) + 2 * N1_formula(3, n, 3)
        assert f3 - comb(n, 2) >= (n * n - 36 * n - 144) / 24 > 0

    print("Odd k=3 PASS: exact WLP iff n in {4,5,6} (n<=10), M_2 z == 0 (n=7..25), and n>=40 bound verified.")


def check_odd_k5plus() -> None:
    # Proposition 7: 4-facet kernel vector in ker(M_m^T) for m >= 2, n >= 4m
    for k, n in [(3, 8), (5, 12), (5, 16), (7, 16), (9, 20)]:
        m = (k + 1) // 2
        assert n >= 4 * m
        faces = vdw_faces_by_size(n, k)
        A = set(range(1, 2 * m, 2))
        B = set(range(2, 2 * m + 1, 2))
        C = set(range(2 * m + 1, 4 * m, 2))
        D = set(range(2 * m + 2, 4 * m + 1, 2))
        F1 = frozenset(A | B)
        F2 = frozenset(C | D)
        Fodd = frozenset(A | C)
        Feven = frozenset(B | D)
        facets_set = set(vdw_facets(n, k))
        assert {F1, F2, Fodd, Feven} <= facets_set

        w = {a: Fraction((-1) ** a, comb(m - 1, a - 1)) for a in range(1, m + 1)}
        v: dict[tuple[int, ...], Fraction] = {}
        for T in faces[m + 1]:
            Ts = set(T)
            if Ts <= F1:
                v[T] = w[len(Ts & A)]
            elif Ts <= F2:
                v[T] = w[len(Ts & D)]
            elif Ts <= Fodd:
                v[T] = -w[len(Ts & A)]
            elif Ts <= Feven:
                v[T] = -w[len(Ts & D)]
            else:
                v[T] = Fraction(0)
        assert any(val != 0 for val in v.values())

        # Check (M_m^T v)_S == 0 for every S in F_m
        f_m1_set = set(faces[m + 1])
        for S in faces[m]:
            Sset = set(S)
            total = Fraction(0)
            for x in range(1, n + 1):
                if x not in Sset:
                    T = tuple(sorted(S + (x,)))
                    if T in f_m1_set:
                        total += v[T]
            assert total == 0

    # Proposition 8: exact face counts and Catalan difference
    for m, n_max in [(3, 14), (4, 13), (5, 13)]:
        k = 2 * m - 1
        for n in range(k + 1, n_max + 1):
            faces = vdw_faces_by_size(n, k)
            fm1_formula = sum(comb(L - 1, m - 1) * N1_formula(L, n, k) for L in range(m, 2 * m))
            fm_formula = (
                sum(comb(L - 1, m - 2) * N1_formula(L, n, k) for L in range(m - 1, 2 * m))
                - N1_formula(m - 1, n, k, even_only=True)
            )
            assert len(faces[m + 1]) == fm1_formula
            assert len(faces[m]) == fm_formula
            assert fm_formula > fm1_formula

    # Check Proposition 8 analytic Catalan difference formula for m=3..20, n=2m..80
    for m in range(3, 21):
        k = 2 * m - 1
        C_m = comb(2 * m, m) // (m + 1)
        assert C_m >= m + 2 and 2 * C_m >= 3 * m + 1
        for n in range(2 * m, 81):
            g1 = n // (k + 1)
            g2 = (n - 1) // k
            fm1 = sum(comb(L - 1, m - 1) * N1_formula(L, n, k) for L in range(m, 2 * m))
            fm = (
                sum(comb(L - 1, m - 2) * N1_formula(L, n, k) for L in range(m - 1, 2 * m))
                - N1_formula(m - 1, n, k, even_only=True)
            )
            catalan_diff = (
                C_m * (sum(range(1, g1 + 1)) + sum(n - k * g for g in range(g1 + 1, g2 + 1)))
                - sum(n - (m - 1) * g for g in range(2, g1 + 1, 2))
                - (m + 1) * sum(n - k * g for g in range(g1 + 1, g2 + 1) if g % 2 == 0)
            )
            assert fm - fm1 == catalan_diff > 0

    print("Odd k>=5 PASS: Prop 7 (M_m^T v == 0) and Prop 8 (|F_m| > |F_{m+1}| & Catalan diff) verified.")


def main() -> None:
    check_lemma2_commutator()
    check_even_part()
    check_odd_k3()
    check_odd_k5plus()
    print("PASS")


if __name__ == "__main__":
    main()

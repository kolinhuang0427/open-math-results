#!/usr/bin/env python3
"""Zero-float exact symbolic and polynomial-ring verification for OEIS A227543."""

from collections import defaultdict


def poly_add(a, b, sign=1):
    res = defaultdict(int, a)
    for m, c in b.items():
        res[m] += sign * c
        if res[m] == 0:
            del res[m]
    return dict(res)


def poly_mul(a, b):
    res = defaultdict(int)
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            # monomial tuples of equal length nvars
            m = tuple(x + y for x, y in zip(m1, m2))
            res[m] += c1 * c2
    return {m: c for m, c in res.items() if c != 0}


def series_inv_unit(S, deg):
    """Exact inverse of S(x) in R[[x]] truncated to x^deg, where S[0] == 1."""
    nvars = len(next(iter(S[0].keys())))
    zero_m = (0,) * nvars
    one_p = {zero_m: 1}
    assert S[0] == one_p
    inv = [one_p] + [{} for _ in range(deg)]
    for k in range(1, deg + 1):
        acc = {}
        for j in range(1, k + 1):
            if S[j] and inv[k - j]:
                acc = poly_add(acc, poly_mul(S[j], inv[k - j]), sign=-1)
        inv[k] = acc
    return inv


def series_mul(A, B, deg):
    res = [{} for _ in range(deg + 1)]
    for i in range(deg + 1):
        if not A[i]:
            continue
        for j in range(deg + 1 - i):
            if B[j]:
                res[i + j] = poly_add(res[i + j], poly_mul(A[i], B[j]), sign=1)
    return res


def series_shift_x_mul(f_poly, S, deg):
    """Compute f_poly * x * S truncated to x^deg."""
    res = [{}] + [poly_mul(f_poly, S[k - 1]) if S[k - 1] else {} for k in range(1, deg + 1)]
    return res


def main():
    # 1. Exact universal verification in ZZ[f_0, ..., f_{N-1}] up to degree N = 8
    N = 8
    zero_m = (0,) * N
    one_p = {zero_m: 1}
    f = [{tuple(1 if j == i else 0 for j in range(N)): 1} for i in range(N)]

    # Build B_m(x) in ZZ[f_0,...,f_{N-1}][[x]] mod x^{N+1} via backward CF from m = N
    # Truncating at B_N = 1/(1 - f_{N-1}? Wait B_m = 1/(1 - f_m*x*B_{m+1});
    # with B_N = 1, B_0 is exact through x^N, and to verify R_d - R_{d-1} = f_d*x*R_{d+1}
    # through x^N for d <= N-2, compute B_0..B_{N-1} up to x^N cleanly from B_N = [one_p] + [{}]*N).
    B = [None] * (N + 1)
    B[N] = [one_p] + [{} for _ in range(N)]
    for m in range(N - 1, -1, -1):
        sub = series_shift_x_mul(f[m], B[m + 1], N)
        # 1 - f[m]*x*B[m+1]
        denom = [one_p] + [poly_add({}, sub[k], sign=-1) for k in range(1, N + 1)]
        B[m] = series_inv_unit(denom, N)

    # Verify R_d - R_{d-1} = f_d * x * R_{d+1} mod x^{N+1} for 0 <= d <= N-2
    R = [None] * (N + 1)
    R_minus1 = [one_p] + [{} for _ in range(N)]
    cur = R_minus1
    for d in range(N):
        cur = series_mul(cur, B[d], N)
        R[d] = cur
    for d in range(N - 1):
        prev_R = R_minus1 if d == 0 else R[d - 1]
        lhs = [poly_add(R[d][k], prev_R[k], sign=-1) for k in range(N + 1)]
        rhs = series_shift_x_mul(f[d], R[d + 1], N)
        # Notice precision drops by 1 per step from B_N truncation: exact through degree N - d - 1
        prec = N - d - 1
        assert lhs[:prec + 1] == rhs[:prec + 1], f"Identity failed at d={d}"

    # Compute P(n, k) directly via Kurkov's recurrence in ZZ[f_0,...,f_{N-1}] for 0 <= n, k <= N
    P = [[{} for _ in range(N + 1)] for _ in range(N + 1)]
    for n in range(N + 1):
        P[n][0] = one_p
        for k in range(1, n + 1):
            P[n][k] = poly_add(P[n - 1][k], poly_mul(f[n - k], P[n][k - 1]), sign=1)

    for n in range(N + 1):
        assert P[n][n] == B[0][n], f"Universal polynomial mismatch at n={n}"

    # 2. Specialization f(m) = q^m in ZZ[q]: verify through Nq = 14 against A(x,q) = 1 + x*A(qx,q)*A(x,q)
    # and match all published rows n=0..8 of OEIS A227543 DATA.
    Nq = 14
    q_one = {(0,): 1}
    # Solve A(x, q) = sum_{n>=0} a_n(q) x^n from A(x,q) = 1 + x*A(qx,q)*A(x,q)
    a_q = [q_one] + [{} for _ in range(Nq)]
    for n in range(1, Nq + 1):
        # [x^n] x * (sum_{i>=0} q^i a_i(q) x^i) * (sum_{j>=0} a_j(q) x^j)
        acc = {}
        for i in range(n):
            j = n - 1 - i
            shifted_ai = {(e[0] + i,): c for e, c in a_q[i].items()}
            acc = poly_add(acc, poly_mul(shifted_ai, a_q[j]), sign=1)
        a_q[n] = acc

    # Kurkov's P(n, k) with f(m) = q^m
    Pq = [[{} for _ in range(Nq + 1)] for _ in range(Nq + 1)]
    for n in range(Nq + 1):
        Pq[n][0] = q_one
        for k in range(1, n + 1):
            fq = {(n - k,): 1}
            Pq[n][k] = poly_add(Pq[n - 1][k], poly_mul(fq, Pq[n][k - 1]), sign=1)

    for n in range(Nq + 1):
        assert Pq[n][n] == a_q[n], f"q-specialization mismatch at n={n}"

    # Compare flattened rows n = 0..8 against exact OEIS A227543 DATA
    oeis_data = [
        1,
        1,
        1, 1,
        1, 2, 1, 1,
        1, 3, 3, 3, 2, 1, 1,
        1, 4, 6, 7, 7, 5, 5, 3, 2, 1, 1,
        1, 5, 10, 14, 17, 16, 16, 14, 11, 9, 7, 5, 3, 2, 1, 1,
        1, 6, 15, 25, 35, 40, 43, 44, 40, 37, 32, 28, 22, 18, 13, 11, 7, 5, 3, 2, 1, 1,
        1, 7, 21, 41, 65, 86, 102, 115, 118, 118, 113, 106, 96, 85, 73, 63, 53, 42, 34, 26, 20, 15, 11, 7, 5, 3, 2, 1, 1,
    ]
    flat_rows = []
    for n in range(9):
        max_k = (n * (n - 1)) // 2
        row = [Pq[n][n].get((k,), 0) for k in range(max_k + 1)]
        assert all(deg[0] <= max_k for deg in Pq[n][n])
        flat_rows.extend(row)
    assert flat_rows == oeis_data

    print("PASS")


if __name__ == "__main__":
    main()

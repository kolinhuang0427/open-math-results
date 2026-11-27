"""Independent exact-arithmetic checker for targets/oeis-A177259/PROOF.md."""

from fractions import Fraction
from itertools import permutations
from math import comb, factorial
import sys


def p_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def p_add(a, b):
    res = [Fraction(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        res[i] += c
    for i, c in enumerate(b):
        res[i] += c
    return p_trim(res)


def s_trim(A, N):
    A = list(A[:N])
    while len(A) < N:
        A.append(Fraction(0))
    return A


def s_add(A, B, N):
    return [(A[i] if i < len(A) else Fraction(0)) + (B[i] if i < len(B) else Fraction(0)) for i in range(N)]


def s_mul(A, B, N):
    C = [Fraction(0)] * N
    for i in range(min(N, len(A))):
        if A[i] == 0:
            continue
        for j in range(min(N - i, len(B))):
            C[i + j] += A[i] * B[j]
    return C


def s_inv(A, N):
    assert A[0] != 0
    inv0 = Fraction(1) / A[0]
    B = [Fraction(0)] * N
    B[0] = inv0
    for n in range(1, N):
        s = sum(A[k] * B[n - k] for k in range(1, min(n + 1, len(A))))
        B[n] = -s * inv0
    return B


def s_pow(A, e: int, N):
    res = s_trim([Fraction(1)], N)
    base = s_trim(A, N)
    while e > 0:
        if e & 1:
            res = s_mul(res, base, N)
        e >>= 1
        if e:
            base = s_mul(base, base, N)
    return res


def s_dx(A, N):
    return [Fraction(i) * A[i] for i in range(1, min(N, len(A)))]


def s_compose(F, u, N):
    assert u[0] == 0
    res = [Fraction(0)] * N
    u_pow = s_trim([Fraction(1)], N)
    for k in range(min(N, len(F))):
        c = F[k]
        if c != 0:
            for i in range(N):
                res[i] += c * u_pow[i]
        u_pow = s_mul(u_pow, u, N)
    return res


def a_double_sum(n: int) -> int:
    total = 0
    for s in range(n + 1):
        for t in range((n - s) // 3 + 1):
            num = factorial(n - 2 * t)
            den = factorial(s) * factorial(t)
            assert num % den == 0
            sign = 1 if (s + t) % 2 == 0 else -1
            total += sign * (num // den)
    return total


def brute_force_derangements_no_adj_3cycles(n: int) -> int:
    count = 0
    for perm in permutations(range(n)):
        if any(perm[i] == i for i in range(n)):
            continue
        # Adjacent 3-cycle (i, i+1, i+2): perm[i] == i+1, perm[i+1] == i+2, perm[i+2] == i
        if any(perm[i] == i + 1 and perm[i + 1] == i + 2 and perm[i + 2] == i for i in range(n - 2)):
            continue
        count += 1
    return count


def main():
    oeis_data = [
        1, 0, 1, 1, 9, 41, 258, 1809, 14575, 131660, 1320264, 14551987,
        174887262, 2276174790, 31895551245, 478783042890, 7665081036273,
        130370168718467, 2347620603019159, 44620121619435141,
        892663172726141844, 18750621868455013979, 412602921349249182309,
    ]
    for n in range(9):
        assert brute_force_derangements_no_adj_3cycles(n) == oeis_data[n], f"Brute-force mismatch at n={n}"

    n_max = 60
    a_vals = [a_double_sum(n) for n in range(n_max + 1)]
    assert a_vals[:len(oeis_data)] == oeis_data, "Double-sum vs OEIS data mismatch"

    # Step 1 inner reindexing identity in Q[x] for k=0..20
    for k in range(21):
        lhs = []
        for t in range(k + 1):
            for s in range(k - t + 1):
                c = Fraction((-1) ** (t + s), factorial(t) * factorial(s))
                term = [Fraction(0)] * (2 * t) + [c]
                lhs = p_add(lhs, term)
        rhs = []
        for j in range(k + 1):
            c = Fraction((-1) ** j, factorial(j))
            term = [Fraction(0)] * (2 * j + 1)
            for i in range(j + 1):
                term[2 * i] += c * Fraction(comb(j, i))
            rhs = p_add(rhs, p_trim(term))
        assert lhs == rhs, f"Step 1 inner sum failed at k={k}"

    # Step 1 OGF identity in Q[[x]] up to O(x^36)
    N = 36
    y_ser = [Fraction(a_vals[n]) for n in range(N)]
    D_ser = s_trim([Fraction(1), Fraction(1), Fraction(0), Fraction(1)], N)
    inv_D = s_inv(D_ser, N)

    ogf_sum = [Fraction(0)] * N
    inv_D_pow = inv_D
    for m in range(N):
        coeff = Fraction(factorial(m))
        for i in range(m, N):
            ogf_sum[i] += coeff * inv_D_pow[i - m]
        inv_D_pow = s_mul(inv_D_pow, inv_D, N)
    assert ogf_sum == y_ser, "Step 1 OGF identity failed"

    # Step 2 ODE for F(u), D(x)*y(x) = F(u(x)), and ODE for y(x)
    F_u = [Fraction(factorial(m)) for m in range(N)]
    dF_u = s_dx(F_u, N)
    N2 = N - 1
    u2 = s_trim([Fraction(0), Fraction(0), Fraction(1)], N2)
    u_m1 = s_trim([Fraction(-1), Fraction(1)], N2)
    ode_F = s_add(
        s_add(s_mul(u2, dF_u, N2), s_mul(u_m1, F_u[:N2], N2), N2),
        s_trim([Fraction(1)], N2),
        N2,
    )
    assert ode_F == [Fraction(0)] * N2

    u_ser = [Fraction(0)] + inv_D[:-1]
    assert s_mul(D_ser, y_ser, N) == s_compose(F_u, u_ser, N)

    du_ser = s_dx(u_ser, N)
    one_m_2x3 = s_trim([Fraction(1), Fraction(0), Fraction(0), Fraction(-2)], N2)
    assert du_ser == s_mul(one_m_2x3, s_pow(inv_D, 2, N2), N2)

    dy_ser = s_dx(y_ser, N)
    x2_D = s_trim([Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(0), Fraction(1)], N2)
    poly_y = s_trim([Fraction(-1), Fraction(0), Fraction(1), Fraction(1), Fraction(3), Fraction(0), Fraction(2)], N2)
    ode_y = s_add(
        s_add(s_mul(x2_D, dy_ser, N2), s_mul(poly_y, y_ser[:N2], N2), N2),
        one_m_2x3,
        N2,
    )
    assert ode_y == [Fraction(0)] * N2, "Step 2 ODE for y(x) failed"

    # Step 3 recurrence for 6 <= n <= 60
    for n in range(6, n_max + 1):
        rhs = (
            (n - 1) * a_vals[n - 1]
            + (n - 1) * a_vals[n - 2]
            + a_vals[n - 3]
            + (n - 1) * a_vals[n - 4]
            + 2 * a_vals[n - 6]
        )
        assert a_vals[n] == rhs, f"Mathar recurrence failed at n={n}"

    print(f"PASS (brute-force n<=8, OEIS data n<=22, Steps 1-2 series to x^{N2-1}, Mathar recurrence 6<=n<={n_max})")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)

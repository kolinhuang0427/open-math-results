import math
import signal

signal.alarm(30)

OEIS_A360949 = [
    1,2,8,50,376,3124,27804,260496,2539616,25556330,263922884,2785341186,
    29948035032,327315887046,3630399545244,40813503158790,464662514679168,
    5354222585965310,62419468527625408,736098528973804246,8781173950238637928,
    105987886325647341056
]

OEIS_A161674_PREFIX = [
    0,1,4,5,6,7,8,9,12,13,16,17,20,21,22,23,24,25,28,29,30,31,32,33,36,37,38,39,40
]


def poly_mul(p, q, deg):
    r = [0] * (deg + 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j in range(min(len(q), deg + 1 - i)):
            r[i + j] += a * q[j]
    return r


def poly_pow(p, e, deg):
    r = [0] * (deg + 1)
    r[0] = 1
    base = p[: deg + 1]
    while e > 0:
        if e & 1:
            r = poly_mul(r, base, deg)
        e >>= 1
        if e:
            base = poly_mul(base, base, deg)
    return r


def compute_A_integer_rec(M: int):
    """Compute B[0..M] strictly in integers using the exact Step 1 recurrence,
    then verify A(x) = 1 + 2*B(x) satisfies 1 = Sum (-x/2)^n (A^n + (-1)^n)^n."""
    B = [0] * (M + 1)
    for k in range(1, M + 1):
        rhs = 0
        for n in range(2, k + 2):
            sub_deg = k + 1 - n
            # Build (1 + 2*B)^n truncated to sub_deg
            one_plus_2B = [1] + [2 * B[i] for i in range(1, sub_deg + 1)]
            An = poly_pow(one_plus_2B, n, sub_deg)
            An[0] += (-1) ** n
            assert all(c % 2 == 0 for c in An)
            half_An = [c // 2 for c in An]
            P = poly_pow(half_An, n, sub_deg)
            if n % 2 == 0:
                rhs += P[sub_deg]
            else:
                rhs -= P[sub_deg]
        B[k] = rhs
    A = [1] + [2 * B[k] for k in range(1, M + 1)]
    return A, B


def main():
    M = 60
    A, B = compute_A_integer_rec(M)

    # 1. Exact check against OEIS A360949 data (22 terms)
    assert A[: len(OEIS_A360949)] == OEIS_A360949

    # 2. Independent verification of the original functional equation 1 = Sum (-x/2)^n (A^n + (-1)^n)^n mod x^{M+1}
    # Multiply term n by 2^M to keep everything integer
    from fractions import Fraction
    total = [Fraction(0)] * (M + 1)
    total[0] = Fraction(1)
    for n in range(1, M + 1):
        sub_deg = M - n
        An = poly_pow(A[: sub_deg + 1], n, sub_deg)
        An[0] += (-1) ** n
        P = poly_pow(An, n, sub_deg)
        factor = (-Fraction(1, 2)) ** n
        for j in range(sub_deg + 1):
            total[n + j] += factor * P[j]
    assert total[0] == 1 and all(total[k] == 0 for k in range(1, M + 1))

    # 3. Verify Thue-Morse and A161674
    N_TM = 2000
    t = [bin(m).count("1") % 2 for m in range(N_TM + 10)]
    a161674 = [m for m in range(N_TM) if (t[m] + t[m + 2]) == 1]
    assert a161674[: len(OEIS_A161674_PREFIX)] == OEIS_A161674_PREFIX
    a161674_set = set(a161674)

    # 4. Verify Step 3 F_2[[y]] identity y^2 C(y)^2 + (1+y)C(y) + 1 = 0 up to N_TM
    c_mod2 = [(t[m] ^ t[m + 2]) for m in range(N_TM)]
    res_mod2 = [0] * N_TM
    res_mod2[0] ^= 1
    for i in range(N_TM):
        if c_mod2[i]:
            res_mod2[i] ^= 1
            if i + 1 < N_TM:
                res_mod2[i + 1] ^= 1
            if 2 * i + 2 < N_TM:
                res_mod2[2 * i + 2] ^= 1
    assert all(x == 0 for x in res_mod2[: N_TM - 5])

    # 5. Verify A360949 mod 4 conjecture for all 1 <= n <= M
    assert A[0] == 1
    for n in range(1, M + 1):
        expected = 2 if (n % 2 == 1 and ((n - 1) // 2) in a161674_set) else 0
        assert A[n] % 4 == expected, f"Mismatch at n={n}: {A[n] % 4} != {expected}"

    print(f"PASS: OEIS A360949 (22 terms) & A161674 (29 terms) matched; functional equation verified to x^{M}; "
          f"F_2[[y]] identity checked to y^{N_TM-6}; A[n] mod 4 conjecture verified for all 0 <= n <= {M}.")


if __name__ == "__main__":
    main()

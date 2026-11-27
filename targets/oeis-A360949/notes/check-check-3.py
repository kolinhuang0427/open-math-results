"""Independent exact-arithmetic verifier for targets/oeis-A360949/.

Written strictly from OEIS A360949 (rev 15), A161674 (rev 21), and PROOF.md,
without reading the author's verify.py or notes/.
Uses exact integer / Fraction polynomial arithmetic only (no floating point).
"""

from __future__ import annotations

import signal
from fractions import Fraction


def timeout_handler(signum, frame):
    raise TimeoutError("check-check-3.py exceeded 50s timeout")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(50)

OEIS_A360949 = [
    1,
    2,
    8,
    50,
    376,
    3124,
    27804,
    260496,
    2539616,
    25556330,
    263922884,
    2785341186,
    29948035032,
    327315887046,
    3630399545244,
    40813503158790,
    464662514679168,
    5354222585965310,
    62419468527625408,
    736098528973804246,
    8781173950238637928,
    105987886325647341056,
]

OEIS_A161674 = [
    0, 1, 4, 5, 6, 7, 8, 9, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25, 28, 29,
    30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 44, 45, 48, 49, 52, 53, 54, 55,
    56, 57, 60, 61, 64, 65, 68, 69, 70, 71, 72, 73, 76, 77, 80, 81, 84, 85,
    86, 87, 88, 89, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104,
]


def poly_mul_trunc(a: list, b: list, deg: int, mod2: bool = False) -> list:
    res = [0] * (deg + 1)
    for i in range(min(len(a), deg + 1)):
        ai = a[i]
        if not ai:
            continue
        for j in range(min(len(b), deg + 1 - i)):
            res[i + j] += ai * b[j]
    if mod2:
        res = [x & 1 for x in res]
    return res


def poly_pow_trunc(a: list, exp: int, deg: int, mod2: bool = False) -> list:
    res = [1] + [0] * deg
    base = (a + [0] * (deg + 1))[: deg + 1]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul_trunc(res, base, deg, mod2=mod2)
        e >>= 1
        if e > 0:
            base = poly_mul_trunc(base, base, deg, mod2=mod2)
    return res


def solve_A_exact(max_deg: int) -> list[int]:
    """Solve 1 = sum_{n>=0} (-x/2)^n (A(x)^n + (-1)^n)^n directly in Q[[x]] up to x^max_deg."""
    # Note: the n=1 term is (-x/2)*(A(x) - 1), so [x^{k+1}] of n=1 is -a_k / 2,
    # while n >= 2 terms have prefactor x^n and depend only on a_0 .. a_{k+1-n} (<= a_{k-1})!
    # We compute up to x^{max_deg + 1} so we determine a_0 .. a_{max_deg}.
    deg_eq = max_deg + 1
    A = [Fraction(1, 1)] + [Fraction(0, 1)] * max_deg
    for k in range(1, max_deg + 1):
        # Compute [x^{k+1}] of sum_{n=2}^{k+1} (-x/2)^n (A(x)^n + (-1)^n)^n using A[0..k-1]
        #Wait: at step k, A[k] is still 0, and n >= 2 terms only access A[0..k+1-n] <= A[k-1]!
        coeff_sum = Fraction(0, 1)
        A_trunc = A[: k]  # only degree <= k-1 needed for n >= 2
        for n in range(2, k + 2):
            need_deg = k + 1 - n
            An = poly_pow_trunc(A_trunc, n, need_deg)
            An[0] += (-1) ** n
            An_pow = poly_pow_trunc(An, n, need_deg)
            coeff_sum += (Fraction(-1, 2) ** n) * An_pow[need_deg]
        # Now -a_k / 2 + coeff_sum == 0  =>  a_k = 2 * coeff_sum
        ak = 2 * coeff_sum
        assert ak.denominator == 1, f"Non-integer a({k}) = {ak}"
        A[k] = ak
    return [int(c) for c in A]


def thue_morse(limit: int) -> list[int]:
    t = [0] * (limit + 1)
    for n in range(1, limit + 1):
        t[n] = t[n >> 1] ^ (n & 1)
    return t


def check_step1_and_conjecture() -> None:
    max_n = 35
    A = solve_A_exact(max_n)
    assert A[: len(OEIS_A360949)] == OEIS_A360949, f"A360949 mismatch: {A[:22]}"

    t = thue_morse(max(max_n + 5, 110))
    a161674_gen = [m for m in range(105) if (t[m] ^ t[m + 2]) == 1]
    assert a161674_gen == OEIS_A161674, "A161674 mismatch"

    assert A[0] == 1
    for n in range(1, max_n + 1):
        assert A[n] % 2 == 0
        if n % 2 == 0:
            assert A[n] % 4 == 0, f"Even n={n} failed A[n] == 0 mod 4"
        else:
            m = (n - 1) // 2
            expected_mod4 = 2 if (t[m] ^ t[m + 2]) == 1 else 0
            assert A[n] % 4 == expected_mod4, f"Odd n={n} failed mod 4 check"

    print(f"Step 1 & Data PASS: A360949 (n=0..{max_n}) and A161674 (m<=104) verified via exact Q[[x]] functional equation.")


def check_steps2_and_3_f2() -> None:
    """Verify every F_2[[x]] and F_2[[y]] identity in Steps 2-3 up to degree 80."""
    M = 80
    # Compute C(y) from y^2 C(y)^2 + (1 + y) C(y) + 1 = 0 in F_2[[y]]:
    # C(y) = (1 + y^2 C(y)^2) / (1 + y) => c_m = (c_{m-1} + [y^m](1 + y^2 C^2)) mod 2
    C = [0] * (M + 1)
    C[0] = 1
    for m in range(1, M + 1):
        # [y^m] (y^2 C(y)^2) = [y^{m-2}] C(y)^2 = (C[(m-2)//2] if (m-2) even >= 0 else 0)
        sq_term = C[(m - 2) // 2] if (m >= 2 and m % 2 == 0) else 0
        C[m] = (C[m - 1] ^ sq_term) & 1

    # Verify y^2 C^2 + (1+y) C + 1 == 0 in F_2[[y]] up to y^M
    C_sq = poly_pow_trunc(C, 2, M, mod2=True)
    y2_C_sq = [0, 0] + C_sq[:-2]
    one_p_y_C = [(C[m] ^ (C[m - 1] if m >= 1 else 0)) & 1 for m in range(M + 1)]
    eq_C = [(y2_C_sq[m] ^ one_p_y_C[m] ^ (1 if m == 0 else 0)) & 1 for m in range(M + 1)]
    assert all(v == 0 for v in eq_C)

    # Construct B(x) mod 2 = x * C(x^2) up to x^{2M+1} and verify (1+x^2)B == x + x^3 B^2 in F_2[[x]]
    X_deg = 2 * M + 1
    B = [0] * (X_deg + 1)
    for m in range(M + 1):
        if 2 * m + 1 <= X_deg:
            B[2 * m + 1] = C[m]
    B_sq = poly_pow_trunc(B, 2, X_deg, mod2=True)
    lhs = [(B[k] ^ (B[k - 2] if k >= 2 else 0)) & 1 for k in range(X_deg + 1)]
    rhs = [0] * (X_deg + 1)
    rhs[1] = 1
    for k in range(3, X_deg + 1):
        rhs[k] ^= B_sq[k - 3]
    assert lhs == rhs

    # Also verify B(x) mod 2 directly matches (A(x)-1)/2 mod 2 for n <= 35
    A = solve_A_exact(35)
    for n in range(1, 36):
        assert ((A[n] // 2) & 1) == B[n]

    # Step 3: T(y) satisfies (1+y)^3 T(y)^2 + (1+y)^2 T(y) + y == 0 in F_2[[y]]
    t = thue_morse(M + 5)
    T = t[: M + 1]
    T_sq = poly_pow_trunc(T, 2, M, mod2=True)
    p1y2 = [1, 0, 1]  # (1+y)^2 in F_2[y]
    p1y3 = [1, 1, 1, 1]  # (1+y)^3 in F_2[y]
    term_T2 = poly_mul_trunc(p1y3, T_sq, M, mod2=True)
    term_T1 = poly_mul_trunc(p1y2, T, M, mod2=True)
    eq_T = [(term_T2[m] ^ term_T1[m] ^ (1 if m == 1 else 0)) & 1 for m in range(M + 1)]
    assert all(v == 0 for v in eq_T)

    # C_tilde(y) = sum (t_m + t_{m+2}) y^m satisfies y^2 C_tilde^2 + (1+y) C_tilde + 1 == 0 and C_tilde == C
    C_tilde = [(t[m] ^ t[m + 2]) & 1 for m in range(M + 1)]
    assert C_tilde == C, "C_tilde != C in F_2[[y]]"

    print(f"Steps 2 & 3 PASS: all F_2[[x]] / F_2[[y]] identities and C(y) == C_tilde(y) verified up to deg {M}.")


def main() -> None:
    check_step1_and_conjecture()
    check_steps2_and_3_f2()
    print("PASS")


if __name__ == "__main__":
    main()

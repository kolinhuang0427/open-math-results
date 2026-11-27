#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A091524/PROOF.md.

Zero floating-point arithmetic is used anywhere: all comparisons and floors in
Q(sqrt(2)) are computed strictly with Python integers, Fractions, and math.isqrt.
"""

from fractions import Fraction
import math
import signal
import sys


# Timeout guard (single-core compute safety)
def _timeout_handler(signum, frame):
    raise TimeoutError("check-check-3.py exceeded 50s alarm")


signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(50)


# ---------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt(2)): element (p, q) represents p + q * sqrt(2)
# ---------------------------------------------------------------------------

def q_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q_mul(x, y):
    p1, q1 = x
    p2, q2 = y
    return (p1 * p2 + 2 * q1 * q2, p1 * q2 + q1 * p2)


def q_sign(x):
    """Exact sign of p + q*sqrt(2) in {-1, 0, +1}."""
    p, q = Fraction(x[0]), Fraction(x[1])
    if p == 0 and q == 0:
        return 0
    if q == 0:
        return 1 if p > 0 else -1
    if p == 0:
        return 1 if q > 0 else -1
    # Same sign?
    if (p > 0 and q > 0) or (p < 0 and q < 0):
        return 1 if p > 0 else -1
    # Opposite signs: compare p^2 vs 2*q^2
    # Clear denominators
    d = math.lcm(p.denominator, q.denominator)
    A = int(p * d)
    B = int(q * d)
    diff = A * A - 2 * B * B
    if diff == 0:
        raise AssertionError("Impossible rational equality to sqrt(2)")
    if A > 0:
        return 1 if diff > 0 else -1
    else:
        return -1 if diff > 0 else 1


def q_lt(x, y):
    return q_sign(q_sub(x, y)) < 0


def q_gt(x, y):
    return q_sign(q_sub(x, y)) > 0


def q_floor(x):
    """Exact floor(p + q*sqrt(2)) using integer isqrt and exact sign checks."""
    p, q = Fraction(x[0]), Fraction(x[1])
    if q == 0:
        return math.floor(p)
    d = math.lcm(p.denominator, q.denominator)
    A = int(p * d)
    B = int(q * d)
    # Initial integer approximation via isqrt(2*B^2)
    root = math.isqrt(2 * B * B)
    approx_num = A + (root if B > 0 else -(root + 1))
    k = approx_num // d
    # Exact strict bracket: k < (A + B*sqrt(2))/d < k + 1
    while q_sign((A - k * d, B)) < 0:
        k -= 1
    while q_sign((A - (k + 1) * d, B)) > 0:
        k += 1
    assert q_sign((A - k * d, B)) > 0 and q_sign((A - (k + 1) * d, B)) < 0
    return k


def q_frac(x):
    return q_sub(x, (Fraction(q_floor(x)), Fraction(0)))


SQRT2 = (Fraction(0), Fraction(1))
INV_SQRT2 = (Fraction(0), Fraction(1, 2))
ONE_PLUS_SQRT2 = (Fraction(1), Fraction(1))
ONE_PLUS_INV_SQRT2 = (Fraction(1), Fraction(1, 2))


def main():
    N_PART = 5000

    # -----------------------------------------------------------------------
    # 0. Primary-source OEIS reference data (verified live at rev cited below)
    # -----------------------------------------------------------------------
    # OEIS A003152 (rev 71, offset 1,2): floor(n*(1 + 1/sqrt(2)))
    oeis_A003152 = [
        1, 3, 5, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 23, 25, 27, 29, 30, 32,
        34, 35, 37, 39, 40, 42, 44, 46, 47, 49, 51, 52, 54, 56, 58, 59, 61, 63,
        64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 87, 88, 90, 92, 93,
        95, 97, 99, 100, 102, 104, 105, 107, 109, 110, 112, 114, 116,
    ]
    # OEIS A003151 (rev 96, offset 1,1): floor(n*(1 + sqrt(2)))
    oeis_A003151 = [
        2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 26, 28, 31, 33, 36, 38, 41, 43, 45,
        48, 50, 53, 55, 57, 60, 62, 65, 67, 70, 72, 74, 77, 79, 82, 84, 86, 89,
        91, 94, 96, 98, 101, 103, 106, 108, 111, 113, 115, 118, 120, 123, 125,
        127, 130, 132, 135, 137, 140, 142, 144,
    ]
    # OEIS A091524 (rev 27, offset 1,3): multiplier a(m) in alpha(m) = a(m)*sqrt(2) - b(m)
    oeis_A091524 = [
        1, 1, 2, 2, 3, 4, 3, 5, 4, 6, 7, 5, 8, 6, 9, 7, 10, 11, 8, 12, 9, 13,
        14, 10, 15, 11, 16, 12, 17, 18, 13, 19, 14, 20, 21, 15, 22, 16, 23, 24,
        17, 25, 18, 26, 19, 27, 28, 20, 29, 21, 30, 31, 22, 32, 23, 33, 24, 34,
        35, 25, 36, 26, 37, 38, 27, 39, 28, 40, 41, 29, 42, 30, 43, 31, 44,
    ]
    # OEIS A028982 (rev 156, offset 1,2): squares and twice squares
    oeis_A028982 = [
        1, 2, 4, 8, 9, 16, 18, 25, 32, 36, 49, 50, 64, 72, 81, 98, 100, 121,
        128, 144, 162, 169, 196, 200, 225, 242, 256, 288, 289, 324, 338, 361,
        392, 400, 441, 450, 484, 512, 529, 576, 578, 625, 648, 676, 722, 729,
        784, 800, 841, 882, 900, 961, 968, 1024,
    ]
    # OEIS A006337 (rev 104, offset 1,2): floor((n+1)*sqrt(2)) - floor(n*sqrt(2))
    oeis_A006337 = [
        1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2,
        1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2,
        1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2,
        1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2,
        1, 2, 1, 1, 2, 1, 2, 1, 1,
    ]

    # -----------------------------------------------------------------------
    # 1. Section 1: Beatty sequences B1, B2 and ordered union S = Z_+ U sqrt(2) Z_+
    # -----------------------------------------------------------------------
    def B1(k):
        return q_floor((Fraction(k), Fraction(k, 2)))

    def B2(k):
        return q_floor((Fraction(k), Fraction(k)))

    b1_vals = [B1(k) for k in range(1, N_PART + 1)]
    b2_vals = [B2(k) for k in range(1, N_PART + 1)]
    assert b1_vals[: len(oeis_A003152)] == oeis_A003152, "A003152 mismatch"
    assert b2_vals[: len(oeis_A003151)] == oeis_A003151, "A003151 mismatch"

    # Also verify B1(k) == k + floor(k/sqrt(2)) and B2(k) == k + floor(k*sqrt(2))
    for k in range(1, 1001):
        assert B1(k) == k + q_floor((Fraction(0), Fraction(k, 2)))
        assert B2(k) == k + q_floor((Fraction(0), Fraction(k)))

    # Merge Z_{>=1} and sqrt(2)*Z_{>=1} in exact order up to N_PART elements
    tau = [None] * (N_PART + 1)
    tau_origin = [None] * (N_PART + 1)  # ('B1', k) or ('B2', k)
    i, j = 1, 1
    for m in range(1, N_PART + 1):
        v1 = (Fraction(i), Fraction(0))
        v2 = (Fraction(0), Fraction(j))
        if q_lt(v1, v2):
            tau[m] = v1
            tau_origin[m] = (1, i)
            i += 1
        else:
            tau[m] = v2
            tau_origin[m] = (2, j)
            j += 1

    # Check partition property and tau_{B1(k)} = k, tau_{B2(k)} = k*sqrt(2)
    seen = {}
    for k in range(1, N_PART + 1):
        v1 = B1(k)
        v2 = B2(k)
        if v1 <= N_PART:
            assert v1 not in seen, f"Collision at {v1}"
            seen[v1] = (1, k)
            assert tau_origin[v1] == (1, k)
            assert tau[v1] == (Fraction(k), Fraction(0))
        if v2 <= N_PART:
            assert v2 not in seen, f"Collision at {v2}"
            seen[v2] = (2, k)
            assert tau_origin[v2] == (2, k)
            assert tau[v2] == (Fraction(0), Fraction(k))
    assert len(seen) == N_PART, "B1 and B2 did not partition [1..N_PART]"
    print(f"[PASS 1] Beatty partition & tau_m identity verified for 1 <= m <= {N_PART}")

    # -----------------------------------------------------------------------
    # 2. Section 2: Graham-Pollak sequence u_r^{(m)} = floor(x_r), inequalities,
    #    binary digits d_j^{(m)}, and alpha(m) = {k*sqrt(2)} = k*sqrt(2) - floor(k*sqrt(2))
    # -----------------------------------------------------------------------
    # Verify u_1^{(m)} = floor(x_1) = m for 1 <= m <= N_PART
    for m in range(1, N_PART + 1):
        x1 = q_mul(tau[m], ONE_PLUS_INV_SQRT2)
        assert q_floor(x1) == m, f"x1 floor mismatch at m={m}"

    # Verify u_{r}^{(m)} == floor(x_r) and Case 1 / Case 2 inequalities
    M_GP = 300
    R_GP = 26
    for m in range(1, M_GP + 1):
        _, k = tau_origin[m]
        u = m
        x = q_mul(tau[m], ONE_PLUS_INV_SQRT2)
        assert u == q_floor(x)

        u_seq = [None, u]  # 1-based: u_1 = m
        for r in range(1, R_GP):
            u_next = q_floor(q_mul(SQRT2, (Fraction(u) + Fraction(1, 2), Fraction(0))))
            x_next = q_mul(SQRT2, x)

            # Check Section 2 exact inequality Delta in (0, 1)
            alpha_r = q_frac(x)
            beta_r = q_frac(x_next)
            delta = q_add(q_mul(SQRT2, q_sub((Fraction(1, 2), Fraction(0)), alpha_r)), beta_r)
            assert q_gt(delta, (Fraction(0), Fraction(0))) and q_lt(delta, (Fraction(1), Fraction(0))), (
                f"Delta out of (0,1) at m={m}, r={r}"
            )
            # Check whether x is K + K*sqrt(2) (Case 1) or 2K + K*sqrt(2) (Case 2)
            # Note: x_1 = tau_m*(1 + 1/sqrt(2)); if tau_m = k then x_1 = k + (k/2)*sqrt(2)
            # Wait: check PROOF.md form for r >= 2 vs r = 1!
            if u_next != q_floor(x_next):
                raise AssertionError(f"u_r != floor(x_r) at m={m}, r={r+1}")
            u = u_next
            x = x_next
            u_seq.append(u)

        # Check binary bits d_j^{(m)} = u_{2j+2} - 2*u_{2j} for j = 1..12
        # and verify 0-based equivalence (u_0 = m => u_{2j+1} - 2*u_{2j-1})
        u0_seq = u_seq[1:]  # u0_seq[0] = u_1 = m
        partial_sum = Fraction(0)
        for j in range(1, 13):
            d_j = u_seq[2 * j + 2] - 2 * u_seq[2 * j]
            d_j_0based = u0_seq[2 * j + 1] - 2 * u0_seq[2 * j - 1]
            assert d_j == d_j_0based
            expected_bit = (
                q_floor((Fraction(0), Fraction((1 << j) * k)))
                - 2 * q_floor((Fraction(0), Fraction((1 << (j - 1)) * k)))
            )
            assert d_j == expected_bit, f"d_j mismatch at m={m}, j={j}"
            assert d_j in (0, 1)
            partial_sum += Fraction(d_j, 1 << j)

        # Verify partial_sum brackets {k*sqrt(2)} = k*sqrt(2) - floor(k*sqrt(2)) within (0, 2^-12)
        target_alpha = q_frac((Fraction(0), Fraction(k)))
        err = q_sub(target_alpha, (partial_sum, Fraction(0)))
        assert q_gt(err, (Fraction(0), Fraction(0))) and q_lt(err, (Fraction(1, 1 << 12), Fraction(0)))

    # Check OEIS A091524 EXAMPLE for m = 1..5: alpha(m) = -b(m) + a(m)*sqrt(2)
    expected_example = [(-1, 1), (-1, 1), (-2, 2), (-2, 2), (-4, 3)]
    for m, (neg_b, a_exp) in enumerate(expected_example, start=1):
        _, k = tau_origin[m]
        b = q_floor((Fraction(0), Fraction(k)))
        assert (k, -b) == (a_exp, neg_b)

    # Check all 75 live OEIS A091524 data terms
    a_seq = [None] + [tau_origin[m][1] for m in range(1, N_PART + 1)]
    assert a_seq[1 : len(oeis_A091524) + 1] == oeis_A091524, "A091524 data mismatch"
    print(f"[PASS 2] Graham-Pollak u_r=floor(x_r), Delta in (0,1), d_j bits, and all {len(oeis_A091524)} OEIS A091524 terms verified")

    # -----------------------------------------------------------------------
    # 3. Section 3 & 4: A028982, A006337, and Kurkov's identity a(n) = sqrt(A028982(n)/A006337(n))
    # -----------------------------------------------------------------------
    # Generate A028982 by sorting {k^2} U {2*k^2} directly
    vals_set = set()
    limit_k = 6000
    for k in range(1, limit_k + 1):
        vals_set.add(k * k)
        vals_set.add(2 * k * k)
    sorted_vals = sorted(vals_set)
    # Must contain all elements <= limit_k^2 without gaps
    assert sorted_vals[0] == 1
    A028982_gen = [None] + sorted_vals[:N_PART]
    assert A028982_gen[1 : len(oeis_A028982) + 1] == oeis_A028982, "A028982 data mismatch"

    # Generate A006337(n) = floor((n+1)*sqrt(2)) - floor(n*sqrt(2))
    A006337_gen = [None] + [
        q_floor((Fraction(0), Fraction(n + 1))) - q_floor((Fraction(0), Fraction(n)))
        for n in range(1, N_PART + 1)
    ]
    assert A006337_gen[1 : len(oeis_A006337) + 1] == oeis_A006337, "A006337 data mismatch"

    # Verify Beatty subsequence evaluations AND Kurkov's formula for all 1 <= n <= N_PART
    for n in range(1, N_PART + 1):
        kind, k = tau_origin[n]
        if kind == 1:
            assert A028982_gen[n] == k * k, f"A028982(B1({k})) mismatch"
            assert A006337_gen[n] == 1, f"A006337(B1({k})) mismatch"
        else:
            assert A028982_gen[n] == 2 * k * k, f"A028982(B2({k})) mismatch"
            assert A006337_gen[n] == 2, f"A006337(B2({k})) mismatch"

        num = A028982_gen[n]
        den = A006337_gen[n]
        assert num % den == 0, f"Non-integer quotient at n={n}"
        quot = num // den
        assert quot == a_seq[n] * a_seq[n], f"Kurkov square mismatch at n={n}"

    print(f"[PASS 3] A028982 (54 OEIS terms), A006337 (105 OEIS terms), Beatty subseqs, and Kurkov identity verified for 1 <= n <= {N_PART}")
    print("PASS")


if __name__ == "__main__":
    main()

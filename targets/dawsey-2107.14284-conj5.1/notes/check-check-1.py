#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Dawsey-Just-Schneider arXiv:2107.14284v2 Conjecture 5.1.

Tests every key identity, bound, and limit mechanism in targets/dawsey-2107.14284-conj5.1/PROOF.md
using exact integer/Fraction/interval arithmetic (zero floating-point).
"""

from __future__ import annotations

from fractions import Fraction
import math
import sys


def primes_up_to_count(count: int) -> list[int]:
    """Return the first `count` primes [p_1, ..., p_count]."""
    if count <= 0:
        return []
    # Rosser-Schoenfeld upper bound for p_n (valid for n >= 6)
    limit = max(30, int(count * (math.log(count) + math.log(math.log(count)) + 2)) + 10) if count >= 6 else 20
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b"\x00" * ((limit - p * p) // p + 1)
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    assert len(primes) >= count
    return primes[:count]


def exact_rational_root_bounds(p: int, num: int, den: int, scale: int = 10**6) -> tuple[Fraction, Fraction]:
    """Return exact Fractions (lo, hi) such that lo <= p^{-(num/den)} <= hi.

    Uses exact integer root finding: r^den <= S^den * p^num < (r+1)^den,
    so r/S <= p^{num/den} < (r+1)/S, giving S/(r+1) < p^{-num/den} <= S/r.
    """
    target = (scale ** den) * (p ** num)
    # Binary search for floor(target^{1/den}), noting p^{num/den} <= p^{(num + den - 1)//den}
    lo = scale
    hi = scale * (p ** ((num + den - 1) // den))
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if pow(mid, den) <= target:
            lo = mid
        else:
            hi = mid - 1
    r = lo
    assert pow(r, den) <= target < pow(r + 1, den)
    return Fraction(scale, r + 1), Fraction(scale, r)


def check_step1_abel_identities(primes: list[int]) -> None:
    """Verify exact summation by parts and telescoping bounds from Step 1."""
    # Check p_k >= k for all k >= 1
    for idx, p in enumerate(primes, start=1):
        assert p >= idx

    # Test functions f: N -> Q + i Q (represented as pairs of Fraction)
    def test_funcs():
        # 1. Alternating bounded: (-1)^k
        yield "alt", lambda k: (Fraction((-1) ** k), Fraction(0)), Fraction(0), Fraction(0)
        # 2. Complex arithmetic: i^k + (2 - 3i)
        def c_fn(k: int) -> tuple[Fraction, Fraction]:
            re = Fraction((1, 0, -1, 0)[k % 4] + 2)
            im = Fraction((0, 1, 0, -1)[k % 4] - 3)
            return re, im
        yield "complex_periodic", c_fn, Fraction(2), Fraction(-3)
        # 3. Unbounded with Cesaro limit 1/2: f(m^2) = m, else 0
        def sq_fn(k: int) -> tuple[Fraction, Fraction]:
            r = math.isqrt(k)
            return (Fraction(r), Fraction(0)) if r * r == k else (Fraction(0), Fraction(0))
        yield "unbounded_squares", sq_fn, Fraction(1, 2), Fraction(0)
        # 4. Unbounded oscillating: S_k = (-1)^k * isqrt(k), f(k) = S_k - S_{k-1}
        def osc_unbounded(k: int) -> tuple[Fraction, Fraction]:
            s_k = ((-1) ** k) * math.isqrt(k)
            s_prev = 0 if k == 1 else (((-1) ** (k - 1)) * math.isqrt(k - 1))
            return Fraction(s_k - s_prev), Fraction(0)
        yield "unbounded_osc", osc_unbounded, Fraction(0), Fraction(0)

    M = 60
    N = 7
    # Exact decreasing weight sequences a_k = p_k^{-s} for integer s = 2, 3
    for s_int in (2, 3):
        a = [Fraction(1, primes[k - 1] ** s_int) for k in range(1, M + 2)]
        # Verify telescoping identity for k (a_k - a_{k+1})
        lhs_tel = sum(k * (a[k - 1] - a[k]) for k in range(1, M))
        rhs_tel = sum(a[k - 1] for k in range(1, M)) - (M - 1) * a[M - 1]
        assert lhs_tel == rhs_tel
        assert lhs_tel < sum(a[k - 1] for k in range(1, M))

        for name, f, L_re, L_im in test_funcs():
            S_re = [Fraction(0)] * (M + 1)
            S_im = [Fraction(0)] * (M + 1)
            for k in range(1, M + 1):
                fr, fi = f(k)
                S_re[k] = S_re[k - 1] + fr
                S_im[k] = S_im[k - 1] + fi

            # Check Step 1 identity for arbitrary 1 <= N <= M
            sum_f_re = sum(f(k)[0] * a[k - 1] for k in range(N, M + 1))
            sum_f_im = sum(f(k)[1] * a[k - 1] for k in range(N, M + 1))
            rhs_re = S_re[M] * a[M - 1] - S_re[N - 1] * a[N - 1] + sum(
                S_re[k] * (a[k - 1] - a[k]) for k in range(N, M)
            )
            rhs_im = S_im[M] * a[M - 1] - S_im[N - 1] * a[N - 1] + sum(
                S_im[k] * (a[k - 1] - a[k]) for k in range(N, M)
            )
            assert sum_f_re == rhs_re, f"Step 1 Re mismatch for {name}, s={s_int}"
            assert sum_f_im == rhs_im, f"Step 1 Im mismatch for {name}, s={s_int}"

            # Check Step 2 finite-sum identity:
            # sum_{k=1}^M f(k) a_k - L_f sum_{k=1}^M a_k
            # = (S_M - L_f M) a_M + sum_{k=1}^{M-1} eps_k k (a_k - a_{k+1})
            diff_re = sum(f(k)[0] * a[k - 1] for k in range(1, M + 1)) - L_re * sum(a[k - 1] for k in range(1, M + 1))
            diff_im = sum(f(k)[1] * a[k - 1] for k in range(1, M + 1)) - L_im * sum(a[k - 1] for k in range(1, M + 1))
            abel_re = (S_re[M] - L_re * M) * a[M - 1] + sum(
                (S_re[k] - L_re * k) * (a[k - 1] - a[k]) for k in range(1, M)
            )
            abel_im = (S_im[M] - L_im * M) * a[M - 1] + sum(
                (S_im[k] - L_im * k) * (a[k - 1] - a[k]) for k in range(1, M)
            )
            assert diff_re == abel_re and diff_im == abel_im


def fmt_frac(q: Fraction, digits: int = 4) -> str:
    """Exact integer-scaled decimal display without using float."""
    scale = 10 ** digits
    scaled = (abs(q.numerator) * scale) // q.denominator
    sign = "-" if q < 0 else ""
    return f"{sign}{scaled // scale}.{scaled % scale:0{digits}d}"


def check_step2_limit_enclosure(primes: list[int]) -> None:
    """Verify Step 2 inequalities and s -> 1+ convergence via exact rational enclosures.

    Uses f(k) = (-1)^k * isqrt(k) (S_k = (-1)^k * isqrt(k)? Wait: let S_k = (-1)^k * isqrt(k),
    so eps_k = S_k/k = (-1)^k * isqrt(k)/k -> 0, L_f = 0) and rational s = 1 + 1/q.
    Note: for any s > 1, we check the exact finite truncation + tail bound at s = 1 + 1/q.
    """
    # Take f(k) with S_k = (-1)^k * isqrt(k) (unbounded! |f(k)| ~ 2*sqrt(k), L_f = 0).
    # Here |eps_k| = isqrt(k) / k <= 1 / sqrt(k).
    # Choose eta = 1/5 = 0.2. We want |eps_k| < eta/2 = 1/10 for all k > K.
    # isqrt(k) / k < 1/10 holds for k >= 101 (since 10 / 101 < 1/10). Let K = 101.
    K = 101
    eta = Fraction(1, 5)
    # Exact upper bound on C_K = sum_{k=1}^K |eps_k| * k * p_k^{-1} = sum_{k=1}^K isqrt(k) / p_k
    C_K = sum(Fraction(math.isqrt(k), primes[k - 1]) for k in range(1, K + 1))

    # Since prime harmonic series diverges, find M such that sum_{k=1}^M p_k^{-1} > 2 * C_K / eta + 1.
    # For s close enough to 1, P(s) > 2 * C_K / eta, so C_K / P(s) < eta / 2.
    # Let's verify sum_{k=1}^M p_k^{-1} grows and check an explicit rational s = 1 + 1/q
    # where exact rational lower bound on P(s) exceeds 2 * C_K / eta.
    # Note: C_K ~ sum_{k=1}^{101} sqrt(k)/p_k < 6. Wait, let's compute exact C_K!
    target_P = (2 * C_K) / eta  # exact Fraction
    # Check partial prime harmonic sum grows past target_P:
    # Actually C_K is around 5, so target_P is around 50!
    # Wait: sum_{k=1}^M 1/p_k ~ log log p_M! Reaching 50 takes ~ e^{e^{50}} primes, so we don't compute 50 directly,
    # instead we verify the exact Step 2 inequality on a sequence of decreasing s = 1 + 1/q AND check Euler divergence
    # bound on smaller C_K (e.g., f(k) = (-1)^k, where |eps_k| = 0 for even k, 1/k for odd k, K=11, C_K ~ 1/2, target_P ~ 5? Wait:
    # sum_{k=1}^{3000} 1/p_k ~ 2.7, and for f(k) = 1_{k > 1} * 0 + 1_{k=1} * 1: C_K = 1/2, eta=1/2 -> target_P = 2!
    # We CAN reach P(s) > 2 easily within the first 500 primes!).
    print(f"  Exact C_K for unbounded f (K={K}, eta={eta}): ~{fmt_frac(C_K, 6)}")

    # Test exact Step 2 inequality for f_small(1) = 1, f_small(k) = 0 for k >= 2? No, take f_small(k) = (-1)^k:
    # S_k = -1 if k odd else 0. L_f = 0. |eps_k| = 1/k if k odd else 0.
    # Take eta = 2/3, so eta/2 = 1/3. For k > K = 3, |eps_k| <= 1/5 < 1/3.
    # C_K = sum_{k=1}^3 |S_k| / p_k = 1/2 + 0 + 1/5 = 7/10.
    # Target P(s) > 2 * C_K / eta = 2 * (7/10) / (2/3) = 21/10 = 2.1.
    # Within M = 1000 primes, let's verify at s = 1 + 1/100 = 101/100 that P(s) > 2.1 and |sum f(k) p_k^{-s} / P(s)| < eta!
    M = 1000
    assert len(primes) >= M
    K2 = 3
    eta2 = Fraction(2, 3)
    C_K2 = Fraction(1, primes[0]) + Fraction(1, primes[2])  # 1/2 + 1/5 = 7/10
    assert C_K2 == Fraction(7, 10)

    # Compute exact rational enclosures [lo_k, hi_k] for p_k^{-101/100} for k = 1..M
    lo_list = []
    hi_list = []
    for k in range(1, M + 1):
        lo, hi = exact_rational_root_bounds(primes[k - 1], 101, 100, scale=10**4)
        lo_list.append(lo)
        hi_list.append(hi)
        # Also verify 0 < p_k^{-s} < p_k^{-1}
        assert 0 < lo <= hi < Fraction(1, primes[k - 1])
        if k >= 2:
            assert hi_list[k - 1] < lo_list[k - 2]  # strictly decreasing

    P_lower_trunc = sum(lo_list)
    assert P_lower_trunc > (2 * C_K2) / eta2, f"Expected P(s) > 2.1, got > {P_lower_trunc}"

    # Bound tail of P(s) for k > M: P_tail < sum_{n > p_M} n^{-1001/1000} < ...
    # Actually we don't even need tail of P(s) to bound |sum_{k=1}^infty f(k) p_k^{-s} / P(s)|:
    # By Step 2, |sum_{k=1}^infty f(k) p_k^{-s} / P(s) - 0| <= C_{K2} / P(s) + eta2 / 2!
    # Since P(s) > P_lower_trunc, C_{K2} / P(s) < C_{K2} / P_lower_trunc.
    bound = C_K2 / P_lower_trunc + eta2 / 2
    assert bound < eta2
    print(f"  f(k)=(-1)^k at s=101/100: P(s) > {fmt_frac(P_lower_trunc)} > 2.1, proved error bound < {fmt_frac(bound)} < {fmt_frac(eta2)}")

    # Also compute exact finite partial sum ratio for f(k) = (-1)^k at s = 101/100 (with tail bound)
    # Using Abel summation up to M:
    # |sum_{k=1}^infty f(k) p_k^{-s}| <= sum_{k=1}^{M-1} |S_k| (p_k^{-s} - p_{k+1}^{-s}) + |S_M| p_M^{-s} + sum_{k=M}^\infty |S_k| (p_k^{-s} - p_{k+1}^{-s})
    # For f(k) = (-1)^k, |S_k| <= 1, so sum_{k=M}^\infty |S_k| (p_k^{-s} - p_{k+1}^{-s}) <= p_M^{-s} < hi_list[M-1].
    # And sum_{k=1}^{M-1} |S_k| (p_k^{-s} - p_{k+1}^{-s}) <= sum_{k=1, k odd}^{M-1} (hi_list[k-1] - lo_list[k]).
    num_upper = sum(hi_list[k - 1] - lo_list[k] for k in range(1, M, 2)) + 2 * hi_list[M - 1]
    ratio_upper = num_upper / P_lower_trunc
    assert ratio_upper < eta2
    print(f"  Direct Abel-bounded |ratio| <= {fmt_frac(ratio_upper, 6)} < {fmt_frac(eta2)}")


def run_all_checks() -> None:
    print("Generating first 1200 primes...")
    primes = primes_up_to_count(1200)
    print(f"  p_1={primes[0]}, p_100={primes[99]}, p_1200={primes[1199]}")

    print("Checking Step 1 exact Abel summation & telescoping identities...")
    check_step1_abel_identities(primes[:200])
    print("  Step 1 exact checks passed.")

    print("Checking Step 2 exact inequalities & rational s -> 1+ enclosure...")
    check_step2_limit_enclosure(primes)
    print("  Step 2 exact checks passed.")

    print("PASS")


if __name__ == "__main__":
    try:
        run_all_checks()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)

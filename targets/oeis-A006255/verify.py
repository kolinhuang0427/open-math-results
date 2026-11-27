#!/usr/bin/env python3
"""Self-contained exact-arithmetic verifier for the proof of Padhi's (2026)
conjecture on OEIS A006255 (rev 106, 2026-06-19):

  Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n)
  except for n = 2, 3, 10, and 171.

Uses ONLY exact integer and Fraction arithmetic (no floating point).
Prints PASS on full verification, or FAIL with diagnostics.
"""

from fractions import Fraction
from math import floor, gcd, isqrt
import signal
import sys
import time


def _timeout(signum, frame):
    print("FAIL: verify.py exceeded 60s time limit")
    sys.exit(1)


signal.signal(signal.SIGALRM, _timeout)
signal.alarm(60)


# ---------------------------------------------------------------------------
# 1. Exact data embedded directly from PROOF.md
# ---------------------------------------------------------------------------

# 39 canonical half-leaves: (D, r, r_mir, M0, M0_mir, cycle_of_(num, den))
# Each entry represents BOTH:
#   - canonical leaf: m == r (mod D), cycle c_i, threshold M0
#   - mirror leaf:    m == r_mir = D - 1 - r (mod D), cycle 1 - c_i, threshold M0_mir
CANONICAL_HALF_LEAVES = [
    (6, 0, 5, 1, 1, [(2, 3), (0, 1), (3, 4)]),
    (30, 3, 26, 4, 3, [(1, 3), (3, 4), (3, 5)]),
    (30, 14, 15, 1, 1, [(1, 6), (1, 1), (2, 5)]),
    (60, 20, 39, 1, 1, [(5, 8), (0, 1), (4, 5)]),
    (210, 8, 201, 9, 2, [(3, 4), (2, 5), (4, 7)]),
    (210, 51, 158, 52, 54, [(3, 7), (1, 10), (8, 7), (-3, 5), (3, 2), (-2, 7), (4, 5)]),
    (420, 68, 351, 15, 37, [(2, 5), (3, 4), (0, 1), (11, 8), (-4, 5), (23, 14), (-1, 3), (1, 1), (1, 3)]),
    (420, 69, 350, 1, 1, [(2, 7), (1, 1), (3, 10)]),
    (420, 81, 338, 152, 129, [(1, 5), (8, 7), (-1, 2), (13, 7), (-6, 5), (18, 7), (-5, 3), (9, 4), (-1, 1), (8, 5), (-2, 7), (9, 10), (3, 7)]),
    (420, 110, 309, 41, 30, [(5, 7), (-1, 10), (10, 7), (-5, 8), (6, 5), (0, 1), (3, 5)]),
    (420, 111, 308, 1, 1, [(1, 8), (1, 1), (3, 7)]),
    (420, 128, 291, 549, 22, [(5, 8), (0, 1), (11, 8), (-4, 5), (2, 1), (-3, 5), (9, 7), (1, 10), (4, 7)]),
    (420, 188, 231, 39, 22, [(2, 5), (3, 4), (0, 1), (11, 8), (-4, 5), (19, 12), (-2, 7), (1, 1), (1, 3)]),
    (840, 141, 698, 1, 3, [(9, 16), (1, 3), (3, 4), (3, 7), (13, 15)]),
    (840, 170, 669, 451, 2350, [(6, 7), (-1, 4), (10, 7), (-5, 6), (74, 35), (-25, 16), (18, 7), (-2, 1), (45, 16), (-46, 35), (25, 12), (-22, 35), (65, 48), (2, 35), (5, 8)]),
    (840, 321, 518, 2, 1, [(9, 16), (1, 7), (1, 1), (1, 4), (3, 5)]),
    (840, 398, 441, 4, 22, [(41, 48), (-2, 7), (1, 1), (1, 3), (2, 5)]),
    (1260, 9, 1250, 29, 85, [(11, 21), (39, 40), (-3, 7), (3, 2), (-2, 3), (9, 5), (-11, 9), (27, 14), (-4, 9), (9, 7), (-1, 4), (1, 1), (9, 20)]),
    (1260, 189, 1070, 1, 1, [(0, 1), (7, 9), (9, 14)]),
    (1260, 230, 1029, 1176, 2290, [(38, 45), (5, 8), (2, 5), (5, 6), (-1, 5), (5, 3), (-1, 2), (16, 9), (-8, 7), (13, 6), (-5, 7), (22, 15), (-5, 28)]),
    (1260, 369, 890, 14, 12, [(1, 4), (1, 1), (-1, 5), (13, 8), (-1, 1), (2, 1), (-9, 14), (11, 9), (0, 1), (5, 6), (3, 7)]),
    (1260, 410, 849, 111, 220, [(1, 40), (10, 21), (11, 20), (0, 1), (5, 4), (-2, 5), (15, 8), (-6, 5), (5, 2), (-5, 3), (11, 5), (-10, 9), (7, 4), (-8, 9), (10, 7)]),
    (1260, 429, 830, 70, 3, [(1, 6), (3, 5), (3, 8), (1, 3), (3, 4), (-1, 9), (6, 5)]),
    (1260, 470, 789, 1, 1, [(7, 10), (5, 9), (4, 7), (3, 4), (0, 1)]),
    (1260, 609, 650, 70, 3, [(-1, 9), (6, 5), (1, 6), (3, 5), (3, 8), (1, 3), (3, 4)]),
    (2520, 21, 2498, 22, 1, [(6, 7), (7, 18), (3, 5), (2, 3), (0, 1)]),
    (2520, 50, 2469, 171, 23, [(74, 45), (-5, 28), (4, 3), (1, 7), (5, 9), (11, 14), (-2, 9), (19, 16), (-10, 21), (29, 20), (0, 1), (6, 5), (-5, 8), (2, 1), (-5, 4), (34, 15), (-55, 56)]),
    (2520, 98, 2421, 3, 10, [(7, 8), (-2, 7), (14, 9), (-1, 8), (2, 3), (7, 16), (2, 7)]),
    (2520, 249, 2270, 1, 3, [(3, 4), (1, 3), (3, 8), (33, 35), (-1, 9)]),
    (2520, 278, 2241, 1, 1, [(7, 16), (2, 9), (1, 1), (1, 3), (2, 5)]),
    (2520, 561, 1958, 18, 69, [(-51, 56), (67, 45), (-3, 28), (13, 15), (3, 7), (1, 6), (9, 7), (-9, 16), (5, 3), (-3, 4), (19, 9)]),
    (2520, 590, 1929, 39, 10, [(25, 16), (-2, 3), (19, 16), (2, 9), (5, 8), (6, 7), (-1, 4), (10, 7), (-2, 15)]),
    (2520, 818, 1701, 1, 1, [(2, 9), (1, 1), (5, 14)]),
    (2520, 861, 1658, 22, 259, [(21, 16), (-1, 21), (21, 20), (3, 7), (7, 45), (69, 56), (-7, 15), (3, 2), (-1, 5), (7, 8), (3, 5), (2, 3), (0, 1), (7, 6), (-3, 7)]),
    (2520, 938, 1581, 24, 70, [(4, 7), (0, 1), (10, 7), (-7, 8), (14, 9), (-1, 14), (7, 9)]),
    (2520, 1089, 1430, 460, 21, [(1, 3), (3, 8), (3, 5), (1, 6), (6, 5), (-2, 3), (9, 5), (-11, 9), (9, 4), (-1, 1), (13, 8), (-1, 5), (1, 1), (1, 5), (9, 14), (-1, 9), (9, 8)]),
    (2520, 1118, 1401, 1, 16, [(1, 4), (4, 7), (4, 9)]),
    (2520, 1310, 1209, 231, 30, [(25, 24), (-2, 7), (19, 16), (-2, 3), (7, 4), (-10, 9), (11, 5), (-5, 6), (8, 5), (-5, 12), (38, 35), (5, 16), (2, 5)]),
    (2520, 1778, 741, 116, 182, [(7, 10), (-1, 7), (7, 5), (-6, 7), (21, 10), (-11, 7), (14, 5), (-4, 3), (11, 5), (-7, 9), (10, 7), (0, 1), (4, 7)]),
]

# Explicit finite witness subsets S subset (n, n+p) for all 10 uncovered primes p not in {2, 3, 5, 19}
FINITE_WITNESSES = {
    7: [27],
    17: [147, 150],
    43: [910, 918, 935, 936],
    101: [5054, 5100, 5103],
    103: [5270, 5289, 5330, 5332],
    163: [13224, 13243, 13311],
    257: [32956, 32960, 33063, 33110],
    461: [106032, 106134, 106260],
    1097: [601704, 601798, 602156],
    3019: [4557000, 4557180, 4557465],
}


# ---------------------------------------------------------------------------
# 2. Exact number-theoretic helpers
# ---------------------------------------------------------------------------

def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    r = isqrt(x)
    return r * r == x


def sieve_primes(limit: int):
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(limit) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [p for p in range(2, limit + 1) if is_p[p]]


def odd_prime_factors(x: int):
    """Exact set of primes dividing x to an odd power (squarefree part factors)."""
    res = set()
    d = 2
    t = x
    while d * d <= t:
        if t % d == 0:
            c = 0
            while t % d == 0:
                t //= d
                c ^= 1
            if c:
                res.add(d)
        d += 1 if d == 2 else 2
    if t > 1:
        res.add(t)
    return res


def b_func(n: int) -> int:
    """b(n) = A006530(A007913(n)): greatest prime factor of squarefree part of n (1 if square)."""
    ps = odd_prime_factors(n)
    return max(ps) if ps else 1


def compute_exact_a(n: int) -> int:
    """Exact computation of Graham's sequence a(n) via F2 Gaussian elimination."""
    targ_ps = odd_prime_factors(n)
    if not targ_ps:
        return n
    p_idx = {}

    def to_vec(ps):
        v = 0
        for q in ps:
            if q not in p_idx:
                p_idx[q] = len(p_idx)
            v ^= 1 << p_idx[q]
        return v

    targ = to_vec(targ_ps)
    basis = {}
    m = n
    while True:
        m += 1
        v = to_vec(odd_prime_factors(m))
        t = v
        while t:
            lsb = t & -t
            if lsb in basis:
                t ^= basis[lsb]
            else:
                basis[lsb] = t
                break
        r = targ
        while r:
            lsb = r & -r
            if lsb in basis:
                r ^= basis[lsb]
            else:
                break
        if r == 0:
            return m


# ---------------------------------------------------------------------------
# 3. Verification routines
# ---------------------------------------------------------------------------

def exact_cycle_M0(cyc):
    """Recompute exact threshold M0 >= 1 from first principles so that for all m >= M0:
       (i)   2m^2 + m < f_i(m) < 2m^2 + 3m + 1,
       (ii)  f_i(m) != 2m^2 + 2m,
       (iii) f_i(m) != f_j(m) for all 0 <= i < j < k.
    """
    k = len(cyc)
    edges = []
    m0 = 1
    for i in range(k):
        c1, c2 = cyc[i], cyc[(i + 1) % k]
        s = c1 + c2
        p = c1 * c2
        assert Fraction(1, 2) < s < Fraction(3, 2), f"Non-strict slope {s}"
        assert {c1, c2} != {Fraction(0), Fraction(1)}, "Forbidden edge {0, 1}"
        # (2s - 1) m + 2p > 0  <=>  m > -2p / (2s - 1)
        m1 = floor((-2 * p) / (2 * s - 1)) + 1
        # (3 - 2s) m + 1 - 2p > 0  <=>  m > (2p - 1) / (3 - 2s)
        m2 = floor((2 * p - 1) / (3 - 2 * s)) + 1
        # 2(s - 1) m + 2p != 0
        m3 = 1
        if s != 1:
            r3 = (-p) / (s - 1)
            if r3.denominator == 1 and r3 >= 1:
                m3 = int(r3) + 1
        m0 = max(m0, m1, m2, m3)
        edges.append((s, p))
    # Pairwise distinctness: f_i(m) = f_j(m) <=> (s_i - s_j) m = p_j - p_i
    for i in range(k):
        si, pi = edges[i]
        for j in range(i + 1, k):
            sj, pj = edges[j]
            if si == sj:
                assert pi != pj, f"Duplicate edge polynomials at {i}, {j}"
            else:
                rij = (pj - pi) / (si - sj)
                if rij.denominator == 1 and rij >= 1:
                    m0 = max(m0, int(rij) + 1)
    return m0


def verify_leaf(D: int, r: int, cyc, expected_M0: int, label: str):
    assert 0 <= r < D, f"{label}: r out of range"
    assert 2520 % D == 0, f"{label}: D={D} does not divide 2520"
    k = len(cyc)
    assert k >= 3 and k % 2 == 1, f"{label}: cycle length {k} not odd >= 3"
    assert len(set(cyc)) == k, f"{label}: duplicate vertices"
    for c in cyc:
        assert c != Fraction(1, 2), f"{label}: forbidden vertex 1/2"

    # Verify exact congruence integrality for ALL m = D*t + r (linear mod a1*a2 => check t=0, 1)
    for i in range(k):
        c1, c2 = cyc[i], cyc[(i + 1) % k]
        a1, b1 = c1.denominator, c1.numerator
        a2, b2 = c2.denominator, c2.numerator
        mod = a1 * a2
        for t in (0, 1):
            m = D * t + r
            assert (2 * (a1 * m + b1) * (a2 * m + b2)) % mod == 0, (
                f"{label}: integrality failed at edge {i} ({c1}, {c2}), t={t}"
            )

    # Recompute exact M0 and check against stated value
    m0 = exact_cycle_M0(cyc)
    assert m0 == expected_M0, f"{label}: M0 mismatch ({m0} != {expected_M0})"

    # Direct evaluation check on the first 5 integers m >= M0 with m == r (mod D)
    m_start = m0 + ((r - m0) % D)
    for step in range(5):
        m = m_start + step * D
        vals = []
        prod = 1
        for i in range(k):
            c1, c2 = cyc[i], cyc[(i + 1) % k]
            v = 2 * (m + c1) * (m + c2)
            assert v.denominator == 1, f"{label}: non-integer at m={m}"
            iv = int(v)
            assert 2 * m * m + m < iv < 2 * m * m + 3 * m + 1, (
                f"{label}: out of (2m^2+m, 2m^2+3m+1) at m={m}, iv={iv}"
            )
            assert iv != 2 * m * m + 2 * m, f"{label}: hit 2m^2+2m at m={m}"
            vals.append(iv)
            prod *= iv
        assert len(set(vals)) == k, f"{label}: collision at m={m}"
        assert prod % 2 == 0 and is_perfect_square(prod // 2), (
            f"{label}: product not 2*square at m={m}"
        )


def verify_all():
    t0 = time.time()

    # Check 1: Reduction b(n)^2 >= 2n <=> n = k*p (p prime, 1 <= k <= p//2) for n <= 20,000
    for n in range(1, 20001):
        b = b_func(n)
        lhs = (b * b >= 2 * n)
        rhs = False
        if b >= 2 and n % b == 0:
            k = n // b
            if 1 <= k <= b // 2 and k % b != 0:
                rhs = True
        assert lhs == rhs, f"Reduction mismatch at n={n}"
    print("[OK] Step 1: Structural reduction verified for all 1 <= n <= 20,000.")

    # Check 2: Self-contained Erdős–Selfridge / Granville–Selfridge Cor. 1 construction
    # for all odd primes 5 <= p <= 500 and all 1 <= k <= (p-3)//2
    primes_500 = sieve_primes(500)
    es_pairs = 0
    for p in primes_500:
        if p < 5:
            continue
        m = (p - 1) // 2
        for k in range(1, m):
            n = k * p
            hi = (k + 1) * p
            if m == 2 * k or m == 2 * k + 1:
                S = [4 * k * (k + 1)]
            else:
                S = sorted([2 * k * (m + 1), (2 * k + 1) * m, (2 * k + 1) * (m + 1), 2 * (k + 1) * m])
            assert len(set(S)) == len(S)
            for x in S:
                assert n < x < hi
            prod = n * hi
            for x in S:
                prod *= x
            assert is_perfect_square(prod), f"ES construction failed at p={p}, k={k}"
            es_pairs += 1
    print(f"[OK] Step 2: 4-term interior construction verified on all {es_pairs} pairs (5 <= p <= 500, 1 <= k <= (p-3)/2).")

    # Check 3: All 39 canonical half-leaves + 39 mirrors = 78 full leaves
    assert len(CANONICAL_HALF_LEAVES) == 39
    class_to_M0 = {}
    max_M0 = 0
    for idx, (D, r, r_mir, M0, M0_mir, raw_cyc) in enumerate(CANONICAL_HALF_LEAVES, 1):
        assert r_mir == D - 1 - r, f"Leaf {idx}: mirror residue mismatch"
        cyc = [Fraction(num, den) for num, den in raw_cyc]
        cyc_mir = [1 - c for c in cyc]
        verify_leaf(D, r, cyc, M0, f"Leaf {idx} canon ({D}, {r})")
        verify_leaf(D, r_mir, cyc_mir, M0_mir, f"Leaf {idx} mirror ({D}, {r_mir})")
        max_M0 = max(max_M0, M0, M0_mir)
        for k in range(2520 // D):
            mc = r + k * D
            mm = r_mir + k * D
            assert mc not in class_to_M0, f"Overlap at m == {mc} (mod 2520)"
            assert mm not in class_to_M0, f"Overlap at m == {mm} (mod 2520)"
            class_to_M0[mc] = M0
            class_to_M0[mm] = M0_mir

    needed = {m for m in range(2520) if gcd(2 * m + 1, 210) == 1}
    assert len(needed) == 1152
    covered = set(class_to_M0.keys())
    assert needed.issubset(covered), f"Missing prime classes mod 2520: {needed - covered}"
    assert all(gcd(2 * m + 1, 210) > 1 for m in covered - needed)
    print(f"[OK] Step 3: All 78 leaves (39 canonical + 39 mirror) verified exact & pairwise disjoint; cover all 1,152/1,152 classes mod 2520 with gcd(2m+1,210)=1 (total {len(covered)} classes); max M0 = {max_M0}.")

    # Check 4: Enumerate ALL primes p > 7 whose covering leaf has m = (p-1)/2 < M0(leaf)
    primes_bound = sieve_primes(2 * max_M0 + 10)
    uncovered_gt7 = []
    for p in primes_bound:
        if p <= 7:
            continue
        m = (p - 1) // 2
        m0_leaf = class_to_M0[m % 2520]
        if m < m0_leaf:
            uncovered_gt7.append(p)
    expected_uncovered_gt7 = [17, 19, 43, 101, 103, 163, 257, 461, 1097, 3019]
    assert uncovered_gt7 == expected_uncovered_gt7, (
        f"Uncovered primes > 7 mismatch: got {uncovered_gt7}, expected {expected_uncovered_gt7}"
    )
    print(f"[OK] Step 4: Exact set of primes p > 7 with m < M0(leaf) is {uncovered_gt7} (9 non-exceptions + p=19).")

    # Check 5: Verify all 10 explicit finite witnesses (p = 7 and the 9 uncovered primes p > 7, p != 19)
    expected_witness_primes = sorted([7] + [p for p in uncovered_gt7 if p != 19])
    assert sorted(FINITE_WITNESSES.keys()) == expected_witness_primes
    for p in expected_witness_primes:
        S = FINITE_WITNESSES[p]
        n = p * (p - 1) // 2
        hi = n + p
        assert S == sorted(S) and len(set(S)) == len(S), f"Witness S for p={p} not strictly increasing"
        for x in S:
            assert n < x < hi, f"Witness element {x} out of ({n}, {hi}) for p={p}"
        prod = n * hi
        for x in S:
            prod *= x
        assert is_perfect_square(prod), f"Witness product not a square for p={p}"
    print(f"[OK] Step 5: All 10 explicit finite witnesses verified exact: {expected_witness_primes}.")

    # Check 6: Verify the 4 genuine exceptions n in {2, 3, 10, 171}
    expected_exc = {2: (2, 6), 3: (3, 8), 10: (5, 18), 171: (19, 195)}
    for n, (exp_b, exp_a) in expected_exc.items():
        b = b_func(n)
        assert b == exp_b, f"b({n}) = {b} != {exp_b}"
        assert b * b >= 2 * n, f"b({n})^2 < 2*{n}"
        an = compute_exact_a(n)
        assert an == exp_a and an > n + b, f"a({n}) = {an} (expected {exp_a} > {n + b})"
    print("[OK] Step 6: All 4 exceptions verified exact: a(2)=6>4, a(3)=8>6, a(10)=18>15, a(171)=195>190.")

    print(f"PASS ({time.time() - t0:.2f}s)")


if __name__ == "__main__":
    verify_all()

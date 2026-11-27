"""Independent exact checker for targets/oeis-A006255/ (PROOF.md).

Written strictly from live OEIS A006255 (rev 106), A007913 (rev 213), A006530 (rev 248),
and PROOF.md, without reading verify.py or notes/.
"""

from fractions import Fraction
from math import floor, gcd, isqrt, prod
import re


OEIS_A006255_DATA = [
    1, 6, 8, 4, 10, 12, 14, 15, 9, 18, 22, 20, 26, 21, 24, 16, 34, 27, 38, 30,
    28, 33, 46, 32, 25, 39, 35, 40, 58, 42, 62, 45, 44, 51, 48, 36, 74, 57, 52,
    50, 82, 56, 86, 55, 60, 69, 94, 54, 49, 63, 68, 65, 106, 70, 66, 72, 76, 87,
    118, 75, 122, 93, 77, 64, 78, 80, 134, 85, 92, 84,
]


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factors_odd_exps(n: int) -> tuple[int, int]:
    """Return (squarefree_part A007913(n), max_prime_factor A006530(squarefree_part))."""
    sf = 1
    gpf_sf = 1
    x = n
    d = 2
    while d * d <= x:
        cnt = 0
        while x % d == 0:
            x //= d
            cnt += 1
        if cnt % 2 == 1:
            sf *= d
            gpf_sf = d
        d += 1 if d == 2 else 2
    if x > 1:
        sf *= x
        gpf_sf = x
    return sf, gpf_sf


def gpf(n: int) -> int:
    if n <= 1:
        return 1
    ans = 1
    x = n
    d = 2
    while d * d <= x:
        while x % d == 0:
            ans = d
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        ans = x
    return ans


def test_lemma1_and_oeis_data() -> None:
    # Verify Lemma 1 structural assertions for 1 <= n <= 2000
    for n in range(1, 2001):
        sf, bn = prime_factors_odd_exps(n)
        if bn * bn >= 2 * n:
            assert is_prime(bn) and bn == gpf(n)
            assert n % bn == 0
            k = n // bn
            assert 1 <= k <= bn // 2 and k % bn != 0

    # Verify exact Graham a(n) for n = 1..70 against OEIS data
    # For small n, compute a(n) via DP / GF2 basis over prime parity vectors
    for n in range(1, len(OEIS_A006255_DATA) + 1):
        if is_square(n):
            a_n = n
        else:
            # Find smallest m > n such that subset of [n+1..m-1] * n * m is a square
            # Using GF(2) incremental span of prime-parity bitmasks
            def mask_of(val: int) -> int:
                m_bit = 0
                x = val
                d = 2
                while d * d <= x:
                    c = 0
                    while x % d == 0:
                        x //= d
                        c ^= 1
                    if c:
                        m_bit ^= 1 << d
                    d += 1 if d == 2 else 2
                if x > 1:
                    m_bit ^= 1 << x
                return m_bit

            basis: dict[int, int] = {}

            def can_make(target: int) -> bool:
                v = target
                while v:
                    lsb = v & -v
                    if lsb in basis:
                        v ^= basis[lsb]
                    else:
                        return False
                return True

            def insert(v: int) -> None:
                while v:
                    lsb = v & -v
                    if lsb in basis:
                        v ^= basis[lsb]
                    else:
                        basis[lsb] = v
                        return

            mn = mask_of(n)
            a_n = None
            for m in range(n + 1, 3 * n + 2):
                mm = mask_of(m)
                if can_make(mn ^ mm):
                    a_n = m
                    break
                insert(mm)
            assert a_n is not None
        assert a_n == OEIS_A006255_DATA[n - 1], f"a({n})={a_n} != {OEIS_A006255_DATA[n-1]}"
    print("Lemma 1 (1<=n<=2000) & exact Graham a(n) vs OEIS A006255 data (1<=n<=70): OK")


def test_lemma2() -> None:
    count = 0
    for p in range(5, 300):
        if not is_prime(p):
            continue
        m = (p - 1) // 2
        for k in range(1, m):
            count += 1
            x1 = 2 * k * (m + 1)
            x2 = (2 * k + 1) * m
            x3 = (2 * k + 1) * (m + 1)
            x4 = 2 * (k + 1) * m
            lo, hi = k * p, (k + 1) * p
            for x in (x1, x2, x3, x4):
                assert lo < x < hi
            if m == 2 * k:
                S = {x4}
            elif m == 2 * k + 1:
                S = {x1}
            else:
                S = {x1, x2, x3, x4}
                assert len(S) == 4
            assert is_square(k * (k + 1) * prod(S))
    print(f"Lemma 2 (all {count} pairs (p, k) for 5<=p<300): OK")


def parse_proof_tables():
    with open("targets/oeis-A006255/PROOF.md", "r", encoding="utf-8") as f:
        text = f.read()

    # Parse Table 1
    leaves = []
    t1_pat = re.compile(
        r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|",
        re.MULTILINE,
    )
    for m in t1_pat.finditer(text):
        idx, D, r, rp, k, M0, M0p, cyc_str = m.groups()
        cyc = [Fraction(tok.strip()) for tok in cyc_str.split(",")]
        leaves.append((int(idx), int(D), int(r), int(rp), int(k), int(M0), int(M0p), cyc))
    assert len(leaves) == 39, f"Expected 39 leaves in Table 1, got {len(leaves)}"

    # Parse Table 2
    witnesses = []
    t2_pat = re.compile(
        r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*\$\\\{([^}]+)\\\}\$\s*\|\s*\$(\d+)\$\s*\|",
        re.MULTILINE,
    )
    for m in t2_pat.finditer(text):
        p, mm, leaf_s, n, np_, s_str, root = m.groups()
        S = [int(x.strip()) for x in s_str.split(",")]
        witnesses.append((int(p), int(mm), leaf_s.strip(), int(n), int(np_), S, int(root)))
    assert len(witnesses) == 10, f"Expected 10 witnesses in Table 2, got {len(witnesses)}"
    return leaves, witnesses


def compute_M0_from_lemma4(cyc: list[Fraction]) -> int:
    k = len(cyc)
    M0 = 1
    si = [cyc[i] + cyc[(i + 1) % k] for i in range(k)]
    pi = [cyc[i] * cyc[(i + 1) % k] for i in range(k)]
    for i in range(k):
        assert Fraction(1, 2) < si[i] < Fraction(3, 2)
        assert {cyc[i], cyc[(i + 1) % k]} != {Fraction(0), Fraction(1)}
        # f_i(m) - (2m^2+m) > 0 => m > -2*p_i / (2*s_i - 1)
        b_lo = (-2 * pi[i]) / (2 * si[i] - 1)
        M0 = max(M0, floor(b_lo) + 1)
        # (2m^2+3m+1) - f_i(m) > 0 => m > (2*p_i - 1) / (3 - 2*s_i)
        b_hi = (2 * pi[i] - 1) / (3 - 2 * si[i])
        M0 = max(M0, floor(b_hi) + 1)
        # f_i(m) != 2m^2 + 2m
        if si[i] != 1:
            root = -pi[i] / (si[i] - 1)
            if root.denominator == 1 and root >= 1:
                M0 = max(M0, int(root) + 1)
        else:
            assert pi[i] != 0
    for i in range(k):
        for j in range(i + 1, k):
            if si[i] != si[j]:
                root = (pi[j] - pi[i]) / (si[i] - si[j])
                if root.denominator == 1 and root >= 1:
                    M0 = max(M0, int(root) + 1)
            else:
                assert pi[i] != pi[j]
    return M0


def check_leaf(D: int, r: int, cyc: list[Fraction], expected_M0: int) -> None:
    k = len(cyc)
    assert k >= 3 and k % 2 == 1
    assert 2520 % D == 0 and 0 <= r < D
    assert len(set(cyc)) == k
    assert Fraction(1, 2) not in cyc

    # Check congruence integrality at m = r and m = D + r
    for i in range(k):
        c1, c2 = cyc[i], cyc[(i + 1) % k]
        for m in (r, D + r):
            val = 2 * (m + c1) * (m + c2)
            assert val.denominator == 1, f"Non-integer f_{i}({m})={val} for (D={D}, r={r})"

    M0 = compute_M0_from_lemma4(cyc)
    assert M0 == expected_M0, f"M0 mismatch for (D={D}, r={r}): {M0} != {expected_M0}"

    # Verify first 5 integers >= M0 congruent to r mod D
    first_m = M0 + ((r - M0) % D)
    for t in range(5):
        m = first_m + t * D
        vals = []
        for i in range(k):
            v = 2 * (m + cyc[i]) * (m + cyc[(i + 1) % k])
            assert v.denominator == 1
            vi = int(v)
            assert 2 * m * m + m < vi < 2 * m * m + 3 * m + 1
            assert vi != 2 * m * m + 2 * m
            vals.append(vi)
        assert len(set(vals)) == k
        assert is_square(2 * prod(vals))


def test_tables_and_coverage() -> None:
    leaves, witnesses = parse_proof_tables()

    # Check all 78 leaves (39 canonical + 39 mirror)
    covered_by = {}
    leaf_M0_map = {}
    for idx, D, r, rp, k, M0, M0p, cyc in leaves:
        assert len(cyc) == k
        assert rp == (D - 1 - r) % D
        assert r != rp  # self-mirror wouldn't be disjoint!
        check_leaf(D, r, cyc, M0)
        mir_cyc = [1 - c for c in cyc]
        check_leaf(D, rp, mir_cyc, M0p)

        for mod_r, thresh in ((r, M0), (rp, M0p)):
            leaf_M0_map[(D, mod_r)] = thresh
            for x in range(mod_r, 2520, D):
                assert x not in covered_by, f"Overlap at {x} mod 2520!"
                covered_by[x] = (D, mod_r, thresh)

    assert len(covered_by) == 1476, f"Expected 1476 covered classes, got {len(covered_by)}"
    U = {m for m in range(2520) if gcd(2 * m + 1, 210) == 1}
    assert len(U) == 1152
    assert U.issubset(covered_by.keys()), "Not all 1152 classes in U are covered!"

    # Check all primes p = 2m+1 > 7 up to m = 2350 (and up to m = 3000) for m < M0
    uncovered_primes = []
    for m in range(4, 3000):
        p = 2 * m + 1
        if is_prime(p):
            D, mod_r, thresh = covered_by[m % 2520]
            if m < thresh:
                uncovered_primes.append(p)
    assert uncovered_primes == [17, 19, 43, 101, 103, 163, 257, 461, 1097, 3019], (
        f"Unexpected uncovered primes: {uncovered_primes}"
    )

    # Verify all 10 finite witnesses in Table 2
    expected_ps = [7, 17, 43, 101, 103, 163, 257, 461, 1097, 3019]
    assert [w[0] for w in witnesses] == expected_ps
    for p, mm, leaf_s, n, np_, S, root in witnesses:
        assert mm == (p - 1) // 2
        assert n == p * (p - 1) // 2
        assert np_ == n + p
        assert S == sorted(set(S))
        assert all(n < x < np_ for x in S)
        prod_val = n * np_ * prod(S)
        assert root * root == prod_val, f"Witness p={p} root mismatch"
    print("Tables 1 & 2 (78 leaves, 1152/1152 U coverage, 10 uncovered primes, 10 witnesses): OK")


def test_four_exceptions() -> None:
    # Exhaustive check that no S <= (n, n+b(n)) gives k(k+1)*square for n in {2, 3, 10, 171}
    for n, bn, k, expected_a in ((2, 2, 1, 6), (3, 3, 1, 8), (10, 5, 2, 18), (171, 19, 9, 195)):
        sf, gpf_sf = prime_factors_odd_exps(n)
        assert gpf_sf == bn and bn * bn >= 2 * n and n == k * bn
        interval = list(range(n + 1, n + bn))
        # Exhaustive over all 2^len(interval) subsets (max len = 18 -> 262144)
        # Use bitmask parity of primes for speed
        def mask_of(val: int) -> int:
            m_bit = 0
            x = val
            d = 2
            while d * d <= x:
                c = 0
                while x % d == 0:
                    x //= d
                    c ^= 1
                if c:
                    m_bit ^= 1 << d
                d += 1 if d == 2 else 2
            if x > 1:
                m_bit ^= 1 << x
            return m_bit

        target = mask_of(k * (k + 1))
        reach = {0}
        for x in interval:
            mx = mask_of(x)
            reach |= {r ^ mx for r in reach}
        assert target not in reach, f"n={n} unexpectedly hit target!"

        # Also verify actual a(n) == expected_a by finding smallest m > n+bn
        basis: dict[int, int] = {}
        for x in range(n + 1, expected_a):
            v = mask_of(x)
            while v:
                lsb = v & -v
                if lsb in basis:
                    v ^= basis[lsb]
                else:
                    basis[lsb] = v
                    break
            # Verify m = x cannot complete a square with n
            if x > n:
                t = mask_of(n) ^ mask_of(x)
                # wait: x is already inserted? check BEFORE inserting!
        # Re-run cleanly checking before insertion:
        basis.clear()
        mn = mask_of(n)
        found = None
        for m in range(n + 1, expected_a + 1):
            mm = mask_of(m)
            v = mn ^ mm
            ok = True
            while v:
                lsb = v & -v
                if lsb in basis:
                    v ^= basis[lsb]
                else:
                    ok = False
                    break
            if ok:
                found = m
                break
            v = mm
            while v:
                lsb = v & -v
                if lsb in basis:
                    v ^= basis[lsb]
                else:
                    basis[lsb] = v
                    break
        assert found == expected_a, f"Expected a({n})={expected_a}, got {found}"
    print("Section 6 (exhaustive non-existence at n+b(n) and exact a(n) for {2, 3, 10, 171}): OK")


def main() -> None:
    test_lemma1_and_oeis_data()
    test_lemma2()
    test_tables_and_coverage()
    test_four_exceptions()
    print("PASS")


if __name__ == "__main__":
    main()

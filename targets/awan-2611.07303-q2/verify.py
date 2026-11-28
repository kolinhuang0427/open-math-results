from fractions import Fraction
from itertools import combinations
from math import gcd

# 1. Exact brute-force check of B_{h,k}(q) for small q
def count_non_bh_bruteforce(h, k, q):
    bad = 0
    for subset in combinations(range(1, q + 1), k):
        # Compute |hA| via iterated sumset
        cur = {0}
        for _ in range(h):
            nxt = set()
            for s in cur:
                for a in subset:
                    nxt.add(s + a)
            cur = nxt
        # Compute M_{h,k} = binom(h + k - 1, k - 1)
        m_hk = 1
        for i in range(k - 1):
            m_hk = m_hk * (h + k - 1 - i)
        den = 1
        for i in range(1, k):
            den = den * i
        m_hk = Fraction(m_hk, den).numerator
        if len(cur) < m_hk:
            bad += 1
    return bad

def binom(n, k):
    num = 1
    den = 1
    for i in range(k):
        num *= n - i
        den *= i + 1
    q_val, r_val = divmod(num, den)
    assert r_val == 0
    return q_val

# 2. Exact closed-form formulas for (3, 3) and (2, 4)
def bad33_closed(q):
    m2, _ = divmod(q - 1, 2)
    m3, _ = divmod(q - 1, 3)
    return m2 * q - m2 * (m2 + 1) + 2 * m3 * q - 3 * m3 * (m3 + 1)

def f33(q):
    return Fraction(q * bad33_closed(q), binom(q, 3))

def cnt_D_closed(D):
    q1, _ = divmod(D - 1, 2)
    ans = 3 * q1
    if D % 2 == 0:
        ans += D - 2
    if D % 3 == 0:
        ans -= 2
    if D % 4 == 0:
        ans -= 2
    return ans

def cnt_D_bruteforce(D):
    ans = 0
    for x in range(1, D - 1):
        ys = set()
        if 2 * x < D:
            ys.add(2 * x)
        if (x + D) % 2 == 0:
            y2, _ = divmod(x + D, 2)
            if x < y2 < D:
                ys.add(y2)
        if 2 * x == D:
            for y in range(x + 1, D):
                ys.add(y)
        if D % 2 == 0:
            half, _ = divmod(D, 2)
            if x < half:
                ys.add(half)
        y5 = D - x
        if x < y5 < D:
            ys.add(y5)
        ans += len(ys)
    return ans

def P24(q):
    const_map = {
        0: Fraction(0, 1),
        1: Fraction(55, 24),
        2: Fraction(5, 3),
        3: Fraction(13, 8),
        4: Fraction(2, 3),
        5: Fraction(55, 24),
        6: Fraction(1, 1),
        7: Fraction(55, 24),
        8: Fraction(2, 3),
        9: Fraction(13, 8),
        10: Fraction(5, 3),
        11: Fraction(55, 24),
    }
    lin = Fraction(47, 12) if q % 2 == 0 else Fraction(25, 6)
    return Fraction(1, 3) * (q ** 3) - Fraction(53, 24) * (q ** 2) + lin * q - const_map[q % 12]

def f24(q):
    return Fraction(q * P24(q), binom(q, 4))

# Check brute force vs closed formulas
for q in range(3, 18):
    assert count_non_bh_bruteforce(3, 3, q) == bad33_closed(q)

for D in range(1, 61):
    assert cnt_D_closed(D) == cnt_D_bruteforce(D)

for q in range(4, 17):
    assert count_non_bh_bruteforce(2, 4, q) == P24(q)

# Verify second difference P24(q+1) - 2*P24(q) + P24(q-1) == cnt(q) across 12 residue classes at multiple m values (degree <= 1 polynomial check)
for m in range(1, 8):
    for r in range(12):
        qv = 12 * m + r
        assert P24(qv + 1) - 2 * P24(qv) + P24(qv - 1) == cnt_D_closed(qv)
assert P24(1) == 0 and P24(2) == 0

# Verify f33 non-monotonicity formulas for m = 1..50
for m in range(1, 51):
    assert f33(6 * m + 1) - f33(6 * m) == Fraction(2, (3 * m - 1) * (6 * m - 1))
    assert f33(6 * m + 2) - f33(6 * m + 1) == Fraction(-3, (6 * m - 1) * (6 * m + 1))

# Verify f24 exact numerator formulas for N_q across all 12 residues mod 12
even_coeffs = {
    0: (-54, 0),
    2: (2, -48),
    4: (-38, 0),
    6: (-30, 0),
    8: (-22, -48),
    10: (-14, 0),
}
odd_coeffs = {
    1: (28, -27),
    3: (36, -99),
    5: (44, -75),
    7: (52, -99),
    9: (12, -27),
    11: (68, -147),
}
for q in range(6, 140):
    diff = f24(q + 1) - f24(q)
    r = q % 12
    if q % 2 == 0:
        b, d = even_coeffs[r]
        num = 11 * q * q + b * q + d
        assert num > 0
    else:
        b, d = odd_coeffs[r]
        num = -(q * q) + b * q + d
        if q >= 71:
            assert num < 0
    assert diff == Fraction(num, q * (q - 1) * (q - 2) * (q - 3))

# Check c_{2,4} = 8 and c_{h,3} = 3 * sum phi(w) over w
norm_vols_24 = [Fraction(1, 12), Fraction(1, 12), Fraction(1, 24), Fraction(1, 24), Fraction(1, 12)]
assert 24 * sum(norm_vols_24) == 8

def phi(w):
    return sum(1 for u in range(1, w) if gcd(u, w) == 1)

for h in range(2, 8):
    # Each (u, w) contributes 3! * (one-half) over w = 3 over w
    c_h3 = sum(Fraction(3, w) for w in range(2, h + 1) for u in range(1, w) if gcd(u, w) == 1)
    expected = 3 * sum(Fraction(phi(w), w) for w in range(2, h + 1))
    assert c_h3 == expected

print("PASS")

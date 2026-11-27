"""
Exact pure-integer verification for OEIS A361430 and A298826.
Verifies:
  1. Direct matrix construction of A298674 / A298825 / A298826 against Werner Schulte's
     multiplicative formula (-1)^p * (e - 1), Vaclav Kotesovec's abs(A298826(n)) = A361430(n),
     and Ridouane Oudra's divisor formula for n = 1..120.
  2. Intermediate CRT reduction c(n) = (tau * b)(n) for n = 1..120.
  3. Exact match with OEIS %S/%T/%U data for both A361430 (n = 1..34) and A298826 (n = 1..64).
"""

from math import gcd


def mobius(n):
    if n == 1:
        return 1
    p = 2
    cnt = 0
    m = n
    while p * p <= m:
        if m % p == 0:
            m //= p
            cnt += 1
            if m % p == 0:
                return 0
        p += 1
    if m > 1:
        cnt += 1
    return -1 if (cnt % 2) else 1


def tau(n):
    c = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            c += 1 if d * d == n else 2
        d += 1
    return c


def factorize(n):
    fac = {}
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            fac[p] = e
        p += 1
    if m > 1:
        fac[m] = 1
    return fac


def verify_all():
    max_n = 120

    # 1. Exact T[u][v] = sum_{d | gcd(u, v)} mu(d)*d from A * B in A298674/A298825
    mu_vals = [0] + [mobius(i) for i in range(1, max_n + 3)]
    T = [[0] * (max_n + 3) for _ in range(max_n + 3)]
    for u in range(1, max_n + 3):
        for v in range(1, max_n + 3):
            g = gcd(u, v)
            T[u][v] = sum(mu_vals[d] * d for d in range(1, g + 1) if g % d == 0)

    # Verify T = A * B literally up to max_n + 2
    A_mat = [[1 if (r % c == 0) else 0 for c in range(1, max_n + 3)] for r in range(1, max_n + 3)]
    B_mat = [[(mu_vals[r] * r if (c % r == 0) else 0) for c in range(1, max_n + 3)] for r in range(1, max_n + 3)]
    for u in range(1, max_n + 3):
        for v in range(1, max_n + 3):
            ab_uv = sum(A_mat[u - 1][d - 1] * B_mat[d - 1][v - 1] for d in range(1, max_n + 3))
            assert ab_uv == T[u][v]

    # 2. Primary definition of A298826(n) = A298825(n)/n
    c_matrix = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        divs_n = [k for k in range(1, n + 1) if n % k == 0]
        row_sum = 0
        for m in range(1, n + 1):
            row_sum += sum(T[n // k][m] * T[k][m + 2] for k in divs_n)
        assert row_sum % n == 0
        c_matrix[n] = row_sum // n

    # 3. Direct CRT formula b(j) and (tau * b)(n)
    b = [0] * (max_n + 1)
    for j in range(1, max_n + 1):
        s = 0
        for d1 in range(1, j + 1):
            if j % d1 == 0:
                d2 = j // d1
                g = gcd(d1, d2)
                if 2 % g == 0:
                    s += mu_vals[d1] * mu_vals[d2] * g
        b[j] = s

    # Verify multiplicativity of b and prime-power values
    for u in range(1, 30):
        for v in range(1, 30):
            if u * v <= max_n and gcd(u, v) == 1:
                assert b[u * v] == b[u] * b[v]

    for n in range(1, max_n + 1):
        conv_n = sum(tau(n // j) * b[j] for j in range(1, n + 1) if n % j == 0)
        assert conv_n == c_matrix[n]

        fac = factorize(n)
        schulte = 1
        a361430_def = 1
        for p, e in fac.items():
            schulte *= ((-1 if p % 2 == 1 else 1) * (e - 1))
            a361430_def *= (e - 1)
        assert c_matrix[n] == schulte
        assert abs(c_matrix[n]) == a361430_def

        oudra = (-1 if (n + 1) % 2 else 1) * sum(
            mu_vals[d] * tau(d) * tau(n // d) for d in range(1, n + 1) if n % d == 0
        )
        assert oudra == c_matrix[n]

    # 4. Exact OEIS data checks
    oeis_a361430 = [
        1, 0, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 4, 0, 0
    ]
    oeis_a298826 = [
        1, 0, 0, 1, 0, 0, 0, 2, -1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -2, 0, 0, 0, 0, 4,
        0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
    ]
    assert [abs(c_matrix[n]) for n in range(1, len(oeis_a361430) + 1)] == oeis_a361430
    assert c_matrix[1:len(oeis_a298826) + 1] == oeis_a298826
    print("PASS")


if __name__ == "__main__":
    verify_all()

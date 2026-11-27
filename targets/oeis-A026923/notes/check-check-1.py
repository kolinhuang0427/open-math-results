#!/usr/bin/env python3
"""
Independent exact-arithmetic verifier for targets/oeis-A026923/
directly from OEIS A026923 definitions and PROOF.md without reading
verify.py or author notes. Zero floats.
"""
from __future__ import annotations

import sympy as sp


def verify_symbolic() -> None:
    x, y = sp.symbols("x y")
    F = x**3 * y / ((1 - x * y) * (1 - x**2 * y) * (1 - x**3 * y))
    F1 = sp.simplify(F.subs(y, 1))
    Fm1 = sp.simplify(F.subs(y, -1))

    D = (1 - x) ** 3 * (1 + x) ** 2 * (1 - x + x**2) * (1 + x**2) * (1 + x + x**2)
    assert sp.simplify(F1 - x**3 / ((1 - x) ** 3 * (1 + x) * (1 + x + x**2))) == 0
    assert sp.simplify(Fm1 - (-x**3) / ((1 + x) ** 2 * (1 + x**2) * (1 - x + x**2))) == 0

    t1 = sp.expand((1 + x) * (1 - x + x**2) * (1 + x**2))
    assert t1 == 1 + x**2 + x**3 + x**5
    t2 = sp.expand((1 - x) ** 3 * (1 + x + x**2))
    assert t2 == 1 - 2 * x + x**2 - x**3 + 2 * x**4 - x**5
    assert sp.expand(t1 + t2 - 2 * (1 - x + x**2 + x**4)) == 0

    A_barker = x**3 * (1 - x + x**2 + x**4) / D
    assert sp.simplify((F1 - Fm1) / 2 - A_barker) == 0

    D_exp = 1 - x - x**4 + x**5 - x**6 + x**7 + x**10 - x**11
    assert sp.expand(D - (1 - x) * (1 - x**6) * (1 - x**4)) == 0
    assert sp.expand(D - D_exp) == 0
    print("PASS verify_symbolic: parity projection, factored/expanded D(x), and Barker G.f. exact")


def verify_partitions_and_recurrence() -> None:
    Nmax = 120
    # 1. Direct exact partition count p_3(n, m): partitions of n into m parts with max part 3
    p_odd = [0] * (Nmax + 1)
    p_even_le3 = [0] * (Nmax + 1)  # partitions of k into an even number of parts <= 3 (k >= 0)
    for n in range(1, Nmax + 1):
        # n = 3 + c1 + 2*c2 + 3*c3 with c1,c2,c3 >= 0, m = 1 + c1 + c2 + c3 odd
        cnt = 0
        rem = n - 3
        if rem >= 0:
            for c3 in range(rem // 3 + 1):
                r2 = rem - 3 * c3
                for c2 in range(r2 // 2 + 1):
                    c1 = r2 - 2 * c2
                    m = 1 + c1 + c2 + c3
                    if m % 2 == 1:
                        cnt += 1
        p_odd[n] = cnt

    oeis_prefix = [
        0, 0, 1, 0, 1, 1, 3, 2, 4, 3, 6, 5, 8, 7, 11, 9, 13, 12, 17, 15, 20, 18,
        24, 22, 28, 26, 33, 30, 37, 35, 43, 40, 48, 45, 54, 51, 60, 57, 67, 63,
        73, 70, 81, 77, 88, 84, 96, 92, 104, 100, 113, 108, 121, 117, 131,
    ]
    assert p_odd[1:len(oeis_prefix) + 1] == oeis_prefix

    # Verify alternate OEIS description: a(n+5) = # partitions of n+2 into even # of parts <= 3 (for n >= 1)
    for k in range(Nmax + 1):
        cnt_ev = 0
        for c3 in range(k // 3 + 1):
            r2 = k - 3 * c3
            for c2 in range(r2 // 2 + 1):
                c1 = r2 - 2 * c2
                if (c1 + c2 + c3) % 2 == 0:
                    cnt_ev += 1
        p_even_le3[k] = cnt_ev
    for n in range(1, Nmax - 4):
        assert p_odd[n + 5] == p_even_le3[n + 2], f"Alternate bijection failed at n={n}"

    # 2. Exact G.f. series expansion D(x)*A(x) == x^3 - x^4 + x^5 + x^7 mod x^(Nmax+1)
    D_coeffs = [1, -1, 0, 0, -1, 1, -1, 1, 0, 0, 1, -1]
    N_coeffs = {3: 1, 4: -1, 5: 1, 7: 1}
    for n in range(1, Nmax + 1):
        conv = sum(D_coeffs[j] * p_odd[n - j] for j in range(min(n, 11) + 1))
        assert conv == N_coeffs.get(n, 0), f"D*A != N at n={n}: {conv}"

    # 3. 11-term recurrence for n >= 8 (hence all n > 11), with a(k) = 0 for k <= 0
    def a_at(k: int) -> int:
        return p_odd[k] if k >= 1 else 0

    for n in range(8, Nmax + 1):
        rhs = (
            a_at(n - 1)
            + a_at(n - 4)
            - a_at(n - 5)
            + a_at(n - 6)
            - a_at(n - 7)
            - a_at(n - 10)
            + a_at(n - 11)
        )
        assert p_odd[n] == rhs

    print(f"PASS verify_partitions_and_recurrence: direct partitions + bijection + D*A=N + 11-term rec (n<=120), a[1..15]={p_odd[1:16]}")


def main() -> None:
    verify_symbolic()
    verify_partitions_and_recurrence()
    print("PASS")


if __name__ == "__main__":
    main()

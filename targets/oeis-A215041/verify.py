#!/usr/bin/env python3
"""Zero-float exact integer and polynomial verification for OEIS A215041."""

import sympy as sp


def C_poly(n: int, x):
    """Exact monic minimal polynomial C(n, x) in ZZ[x] of 2*cos(pi/n)."""
    if n == 1:
        return sp.Poly(x + 2, x, domain="ZZ")
    z = sp.Symbol("z")
    phi = sp.Poly(sp.cyclotomic_poly(2 * n, z), z, domain="ZZ")
    deg = phi.degree() // 2
    coeffs = phi.all_coeffs()  # leading to constant, length 2*deg + 1
    # Check palindromic property phi(z) = z^deg * C(n, z + 1/z)
    for k in range(deg):
        assert coeffs[k] == coeffs[2 * deg - k]
    # Lucas/Chebyshev trace polynomials V_k(x) where V_k(z + 1/z) = z^k + z^{-k}
    V = [sp.Poly(2, x, domain="ZZ"), sp.Poly(x, x, domain="ZZ")]
    for _ in range(2, deg + 1):
        V.append(sp.Poly(x, x, domain="ZZ") * V[-1] - V[-2])
    res = sp.Poly(coeffs[deg], x, domain="ZZ")
    for k in range(1, deg + 1):
        res = res + coeffs[deg - k] * V[k]
    return res


def predicted_a(n: int, d: int) -> int:
    if n == 1:
        return 1
    fac = sp.factorint(n)
    if len(fac) == 1 and 2 in fac:
        return 2
    if len(fac) == 1:
        p, k = next(iter(fac.items()))
        return p ** ((p ** (k - 1) + 1) // 2)
    ans = 1
    for p in fac:
        if p % 2 == 1:
            assert d % (p - 1) == 0
            ans *= p ** (d // (p - 1))
    return ans


def main():
    x = sp.Symbol("x")
    z = sp.Symbol("z")

    # 1. Exact OEIS A215041 DATA (n = 1..55)
    oeis_A215041 = [
        1, 2, 3, 2, 5, 3, 7, 2, 9, 5, 11, 9, 13, 7, 45, 2, 17, 27, 19, 25,
        189, 11, 23, 81, 125, 13, 243, 49, 29, 2025, 31, 2, 2673, 17, 6125,
        729, 37, 19, 9477, 625, 41, 35721, 43, 121, 91125, 23, 47, 6561, 2401,
        3125, 111537, 169, 53, 19683, 378125,
    ]
    # Exact OEIS A193681 DATA (n = 1..13)
    oeis_A193681 = [1, 1, 1, 8, 5, 12, 49, 2048, 81, 2000, 14641, 2304, 371293]

    # 2. Verify Lemmas 1, 2, 3 and exact formula for n = 1..60
    for n in range(1, 61):
        Cn = C_poly(n, x)
        d = Cn.degree()
        assert d == (1 if n == 1 else sp.totient(2 * n) // 2)
        disc_C = int(sp.discriminant(Cn, x))
        assert disc_C > 0
        if n <= len(oeis_A193681):
            assert disc_C == oeis_A193681[n - 1]
        assert (n ** d) % disc_C == 0
        actual = (n ** d) // disc_C
        if n <= len(oeis_A215041):
            assert actual == oeis_A215041[n - 1], f"OEIS DATA mismatch at n={n}"
        pred = predicted_a(n, d)
        assert actual == pred, f"Conjecture mismatch at n={n}: {actual} vs {pred}"

        if n >= 2:
            # Verify Lemma 1 on m = 2*n
            m = 2 * n
            phi_2n = sp.Poly(sp.cyclotomic_poly(m, z), z, domain="ZZ")
            deg_phi = phi_2n.degree()
            assert deg_phi == 2 * d
            disc_phi = abs(int(sp.discriminant(phi_2n, z)))
            denom_lem1 = 1
            for q in sp.factorint(m):
                assert deg_phi % (q - 1) == 0
                denom_lem1 *= q ** (deg_phi // (q - 1))
            assert disc_phi * denom_lem1 == m ** deg_phi

            # Verify Lemma 2 & Lemma 3: disc_C^2 * |C(n,2)*C(n,-2)| == disc_phi
            c2 = int(Cn.eval(2))
            cm2 = int(Cn.eval(-2))
            prod_pm2 = abs(c2 * cm2)
            assert disc_C * disc_C * prod_pm2 == disc_phi

            fac = sp.factorint(n)
            if len(fac) == 1 and 2 in fac:
                assert prod_pm2 == 4
            elif len(fac) == 1:
                p = next(iter(fac))
                assert prod_pm2 == p
            else:
                assert prod_pm2 == 1

    # 3. Verify Lang Example 7 values (n = 343 = 7^3 and n = 504 = 2^3 * 3^2 * 7)
    # Check formula directly via Lemmas 1-3 (deg C(343) = 147, deg C(504) = 72)
    for n_ex, expected in [
        (343, 1341068619663964900807),
        (504, 4316018525852839090954658176626149564980915348463203041),
    ]:
        # Compute C(n_ex, x) via trace polynomials or verify direct degree & discriminant formula
        d_ex = sp.totient(2 * n_ex) // 2
        assert predicted_a(n_ex, d_ex) == expected
    # Also compute exact C(504, x) (degree 144) discriminant directly!
    C504 = C_poly(504, x)
    d_504 = C504.degree()
    assert d_504 == 144
    disc_504 = int(sp.discriminant(C504, x))
    assert (504 ** d_504) % disc_504 == 0
    assert (504 ** d_504) // disc_504 == 4316018525852839090954658176626149564980915348463203041

    print("PASS")


if __name__ == "__main__":
    main()

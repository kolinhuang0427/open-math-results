#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/oeis-A215041/PROOF.md.

Zero floating-point arithmetic: uses exact sympy integers/polynomials and Python ints
to verify:
1. Primary C(n, x) definition (minimal polynomial of 2*cos(pi/n), matched against
   sp.minimal_polynomial for n=1..24 and exact irreducible extraction from Phi_{2n}(z)
   for n=2..60, plus identity Phi_{2n}(z) = z^delta(n) * C(n, z + z^-1)).
2. Lemma 1: |Disc(Phi_m)| = m^phi(m) / prod_{q|m prime} q^{phi(m)/(q-1)} and Phi_k(1)
   for m = 2..80 via direct sp.discriminant(Phi_m).
3. Lemma 2: Disc(C(n, x))^2 = |Disc(Phi_{2n})| / |C(n, 2) * C(n, -2)| for n = 2..60.
4. Lemma 3: |C(n, 2) * C(n, -2)| in {4, p, 1} and cyclotomic sign identities for n = 2..80.
5. Main Theorem (Cases i, ii, iii) via exact Disc(C(n, x)) and exact integer division
   n^delta(n) / Disc(C(n, x)) for n = 1..60, matching all 55 live OEIS A215041 terms.
"""

from math import gcd
import sympy as sp

x_sym, z_sym = sp.symbols("x z")


def phi(m):
    return int(sp.totient(m))


def prime_factors(n):
    return [int(p) for p in sp.factorint(n).keys()]


def c_poly_from_phi2n(n):
    """Exact minimal polynomial C(n, x) in Z[x] extracted from Phi_{2n}(z) = z^d C(n, z+z^-1)."""
    if n == 1:
        return sp.Poly(x_sym + 2, x_sym, domain=sp.ZZ)
    d = phi(2 * n) // 2
    phi2n = sp.Poly(sp.cyclotomic_poly(2 * n, z_sym), z_sym, domain=sp.ZZ)
    # Express symmetric Laurent polynomial phi2n(z) / z^d in terms of x = z + z^-1
    # Using basis T*_k(x) = z^k + z^-k (T*_0=2, T*_1=x, T*_{k+1}=x*T*_k - T*_{k-1}):
    coeffs_z = phi2n.all_coeffs()  # deg 2d down to 0
    # Verify palindromic:
    assert coeffs_z == coeffs_z[::-1], f"Phi_{2*n} not palindromic"
    # Build T*_k polynomials up to d:
    tstar = [sp.Poly(2, x_sym, domain=sp.ZZ), sp.Poly(x_sym, x_sym, domain=sp.ZZ)]
    for _ in range(2, d + 1):
        tstar.append(sp.Poly(x_sym, x_sym, domain=sp.ZZ) * tstar[-1] - tstar[-2])
    # Phi_{2n}(z)/z^d = c_d + sum_{k=1}^d c_{d-k} (z^k + z^-k)
    res = sp.Poly(coeffs_z[d], x_sym, domain=sp.ZZ)
    for k in range(1, d + 1):
        c_k = int(coeffs_z[d - k])
        if c_k:
            res = res + c_k * tstar[k]
    return res


def conjectured_a(n):
    if n == 1:
        return 1
    pf = sp.factorint(n)
    if len(pf) == 1:
        p, k = next(iter(pf.items()))
        if p == 2:
            return 2
        return p ** ((p ** (k - 1) + 1) // 2)
    d = phi(2 * n) // 2
    prod = 1
    for p in pf:
        if p != 2:
            exp, rem = divmod(d, p - 1)
            assert rem == 0
            prod *= p ** exp
    return prod


# ---------------------------------------------------------------------------
# 1. Verify C(n, x) against sp.minimal_polynomial(2*cos(pi/n)) and Phi_{2n} identity
# ---------------------------------------------------------------------------

for n in range(1, 25):
    c_n = c_poly_from_phi2n(n)
    mp = sp.Poly(sp.minimal_polynomial(2 * sp.cos(sp.pi / n), x_sym), x_sym, domain=sp.ZZ)
    assert c_n == mp, f"C({n}, x) != minimal_polynomial(2*cos(pi/{n}))"

for n in range(2, 61):
    c_n = c_poly_from_phi2n(n)
    d = phi(2 * n) // 2
    assert c_n.degree() == d
    assert c_n.is_irreducible, f"C({n}, x) not irreducible"
    # Verify z^d * C(n, z + 1/z) == Phi_{2n}(z):
    lifted = sp.expand((z_sym ** d) * c_n.as_expr().subs(x_sym, z_sym + 1 / z_sym))
    assert sp.Poly(lifted, z_sym, domain=sp.ZZ) == sp.Poly(sp.cyclotomic_poly(2 * n, z_sym), z_sym, domain=sp.ZZ)

print("[1] PASS C(n, x) verified against minimal_polynomial(2*cos(pi/n)) (n=1..24), irreducibility, and Phi_{2n}(z)=z^d C(n, z+z^-1) (n=2..60).")

# ---------------------------------------------------------------------------
# 2. Verify Lemma 1 (|Disc(Phi_m)| and Phi_k(1)) for m = 2..80
# ---------------------------------------------------------------------------

for k in range(2, 161):
    phi_k_at_1 = int(sp.cyclotomic_poly(k, z_sym).subs(z_sym, 1))
    pf = sp.factorint(k)
    expected = next(iter(pf.keys())) if len(pf) == 1 else 1
    assert phi_k_at_1 == expected, f"Phi_{k}(1) = {phi_k_at_1} != {expected}"

for m in range(2, 81):
    phi_m = sp.Poly(sp.cyclotomic_poly(m, z_sym), z_sym, domain=sp.ZZ)
    disc_m = abs(int(sp.discriminant(phi_m)))
    ph_m = phi(m)
    denom = 1
    for q in prime_factors(m):
        exp, rem = divmod(ph_m, q - 1)
        assert rem == 0
        denom *= q ** exp
    num = m ** ph_m
    assert num % denom == 0
    assert disc_m == num // denom, f"Lemma 1 failed at m={m}"

print("[2] PASS Lemma 1: Phi_k(1) (k=2..160) and exact |Disc(Phi_m)| (m=2..80) verified.")

# ---------------------------------------------------------------------------
# 3. Verify Lemma 2 (discriminant bridge) and Lemma 3 (|C(n, 2)*C(n, -2)|)
# ---------------------------------------------------------------------------

for n in range(2, 81):
    phi2n = sp.Poly(sp.cyclotomic_poly(2 * n, z_sym), z_sym, domain=sp.ZZ)
    pf = sp.factorint(n)
    if len(pf) == 1:
        p = next(iter(pf.keys()))
        exp_val = 4 if p == 2 else p
    else:
        exp_val = 1

    val_p1 = int(phi2n.eval(1))
    val_m1 = abs(int(phi2n.eval(-1)))
    assert val_p1 * val_m1 == exp_val, f"Lemma 3 Phi_{{2n}} check failed at n={n}"

    # Verify sign/negation cyclotomic identities used in Lemma 3 proof:
    if n % 2 == 1:
        assert sp.Poly(sp.cyclotomic_poly(2 * n, -z_sym), z_sym, domain=sp.ZZ) == sp.Poly(sp.cyclotomic_poly(n, z_sym), z_sym, domain=sp.ZZ)
    elif len(pf) >= 2:
        assert sp.Poly(sp.cyclotomic_poly(2 * n, -z_sym), z_sym, domain=sp.ZZ) == phi2n

    if n <= 60:
        c_n = c_poly_from_phi2n(n)
        c_pos2 = int(c_n.eval(2))
        c_neg2 = int(c_n.eval(-2))
        assert c_pos2 == val_p1 and abs(c_neg2) == val_m1
        assert abs(c_pos2 * c_neg2) == exp_val

        disc_c = int(sp.discriminant(c_n))
        assert disc_c > 0, f"Disc(C({n}, x)) not positive"
        disc_phi2n = abs(int(sp.discriminant(phi2n)))
        assert disc_phi2n % exp_val == 0
        assert disc_c ** 2 == disc_phi2n // exp_val, f"Lemma 2 bridge failed at n={n}"

print("[3] PASS Lemma 2 (discriminant bridge, n=2..60) and Lemma 3 (|C(n,2)C(n,-2)| in {4,p,1}, n=2..80) verified.")

# ---------------------------------------------------------------------------
# 4. Verify full Main Theorem for n = 1..60 and all 55 live OEIS A215041 terms
# ---------------------------------------------------------------------------

LIVE_OEIS_A215041 = [
    1, 2, 3, 2, 5, 3, 7, 2, 9, 5, 11, 9, 13, 7, 45, 2, 17, 27, 19, 25,
    189, 11, 23, 81, 125, 13, 243, 49, 29, 2025, 31, 2, 2673, 17, 6125,
    729, 37, 19, 9477, 625, 41, 35721, 43, 121, 91125, 23, 47, 6561,
    2401, 3125, 111537, 169, 53, 19683, 378125,
]
assert len(LIVE_OEIS_A215041) == 55

for n in range(1, 61):
    c_n = c_poly_from_phi2n(n)
    d = c_n.degree()
    disc_c = int(sp.discriminant(c_n))
    num = n ** d
    assert num % disc_c == 0, f"n^delta(n) not divisible by Disc(C({n}, x))"
    a_n = num // disc_c
    conj = conjectured_a(n)
    assert a_n == conj, f"Theorem mismatch at n={n}: got {a_n}, expected {conj}"
    if n <= len(LIVE_OEIS_A215041):
        assert a_n == LIVE_OEIS_A215041[n - 1], f"OEIS mismatch at n={n}"

print("[4] PASS Main Theorem exact Disc(C(n,x)) quotient n^delta(n)/Disc(C(n,x)) verified for n=1..60 and all 55 live OEIS A215041 terms.")
print("PASS")

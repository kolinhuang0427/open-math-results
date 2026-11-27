"""Independent exact checker for targets/oeis-A108430/ (PROOF.md).

Written strictly from live OEIS A108430 (rev 14) and PROOF.md,
without reading verify.py.
"""

from math import comb
import sympy as sp


OEIS_A108430_DATA = [
    3,
    31,
    311,
    3151,
    32299,
    334335,
    3488239,
    36627487,
    386618387,
    4098713631,
    43611791783,
    465496885231,
    4981942135611,
    53443871159551,
    574500093677535,
    6186886528903231,
    66735614131858723,
    720897596248427295,
]


def c0(n: int) -> int:
    return n * (2 * n + 1) * (23982 * n - 28681)


def c1(n: int) -> int:
    return -640736 * n**3 + 1168048 * n**2 - 901220 * n + 247035


def c2(n: int) -> int:
    return 1196488 * n**3 - 6448608 * n**2 + 10992587 * n - 5911365


def c3(n: int) -> int:
    return 2 * (2 * n - 5) * (28283 * n - 6993) * (n - 3)


def a_binomial(n: int) -> int:
    num = sum(k * comb(n, 2 * n - k) * comb(n + k, n - 1) for k in range(n, 2 * n + 1))
    assert num % n == 0
    return num // n


def brute_force_paths(n: int) -> tuple[int, dict[int, int]]:
    """DP/enumeration of all first-quadrant paths from (0,0) to (3n,0) with u=(2,1), U=(1,2), d=(1,-1)."""
    # State: (x, y) -> {num_d: path_count}
    dp: dict[tuple[int, int], dict[int, int]] = {(0, 0): {0: 1}}
    target_x = 3 * n
    # Process by x strictly increasing since every step has dx in {1, 2}
    for x in range(target_x):
        # Collect states at this x
        items = [(y, counts) for (xx, y), counts in dp.items() if xx == x]
        for y, counts in items:
            for dx, dy, dd in ((2, 1, 0), (1, 2, 0), (1, -1, 1)):
                nx, ny = x + dx, y + dy
                if nx <= target_x and ny >= 0:
                    dest = dp.setdefault((nx, ny), {})
                    for k, cnt in counts.items():
                        dest[k + dd] = dest.get(k + dd, 0) + cnt
    end_counts = dp.get((target_x, 0), {})
    total_d = sum(k * cnt for k, cnt in end_counts.items())
    return total_d, end_counts


def test_combinatorics_and_data() -> None:
    # Check path counts and bivariate T(n, k) vs Lagrange inversion formula
    for n in range(1, 7):
        total_d, dist = brute_force_paths(n)
        assert total_d == a_binomial(n) == OEIS_A108430_DATA[n - 1]
        for j in range(n + 1):
            k = 2 * n - j
            expected_num = comb(n, j) * comb(3 * n - j, n - 1)
            assert expected_num % n == 0
            assert dist.get(k, 0) == expected_num // n

    # Check binomial formula against all 18 OEIS data values and recurrence up to n = 30
    vals = {0: 0, -1: 0, -2: 0}
    for n in range(1, 31):
        vals[n] = a_binomial(n)
        if n <= len(OEIS_A108430_DATA):
            assert vals[n] == OEIS_A108430_DATA[n - 1]

    assert c0(1) * vals[1] == -42291
    assert c0(2) * vals[2] + c1(2) * vals[1] == -49573
    for n in range(3, 31):
        assert c0(n) != 0
        lhs = c0(n) * vals[n] + c1(n) * vals[n - 1] + c2(n) * vals[n - 2] + c3(n) * vals[n - 3]
        assert lhs == 0, f"Recurrence failed at n={n}: {lhs}"
    print("Combinatorics, Lagrange T(n,k), OEIS data (n=1..18), and recurrence (n=3..30): OK")


def test_algebraic_proof_in_A() -> None:
    z, G = sp.symbols("z G")
    P = z * G**3 + z * G**2 - G + 1

    # 1. Irreducibility of P(z, G) over Q(z)
    P_poly = sp.Poly(P, G, domain=sp.QQ.frac_field(z))
    assert P_poly.is_irreducible, "P(z, G) must be irreducible over Q(z)"

    # Helper: represent element of A = Q(z)[G]/(P) as tuple (a0, a1, a2) in Q(z)^3
    def normalize(expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        poly = sp.Poly(sp.expand(expr), G, domain=sp.QQ.frac_field(z))
        _, rem = sp.div(poly, P_poly, domain=sp.QQ.frac_field(z))
        cs = rem.all_coeffs()
        # Pad on left to length 3: [coeff(G^2), coeff(G), coeff(1)]
        cs = [sp.Integer(0)] * (3 - len(cs)) + cs
        return (sp.cancel(cs[2]), sp.cancel(cs[1]), sp.cancel(cs[0]))

    def to_expr(vec: tuple[sp.Expr, sp.Expr, sp.Expr]):
        return vec[0] + vec[1] * G + vec[2] * G**2

    def mul_A(u, v):
        return normalize(to_expr(u) * to_expr(v))

    def inv_A(u):
        u_poly = sp.Poly(to_expr(u), G, domain=sp.QQ.frac_field(z))
        inv_poly = sp.invert(u_poly, P_poly)
        res = normalize(inv_poly.as_expr())
        assert mul_A(u, res) == (1, 0, 0), "Inverse check failed in A"
        return res

    # 2. Compute D = 1 - 2zG - 3zG^2 and its inverse in A
    D = normalize(1 - 2 * z * G - 3 * z * G**2)
    D_inv = inv_A(D)

    # A(z) = (z G^2 + 2 z G^3) / D in A
    A_vec = mul_A(normalize(z * G**2 + 2 * z * G**3), D_inv)
    # G'(z) = (G^3 + G^2) / D in A
    Gp_vec = mul_A(normalize(G**3 + G**2), D_inv)

    # Check P'(z, G) = 0 => G^3 + G^2 + (3zG^2 + 2zG - 1)*G'(z) == 0 in A
    check_deriv = normalize(G**3 + G**2 + (3 * z * G**2 + 2 * z * G - 1) * to_expr(Gp_vec))
    assert check_deriv == (0, 0, 0), f"Implicit differentiation failed: {check_deriv}"

    # Verify G_1(z) series and A(z) series match path counts up to z^10
    G1_ser = [sp.Rational(0)] * 11
    G1_ser[0] = sp.Rational(1)
    for m in range(1, 11):
        # G1 = 1 + z*G1^2 + z*G1^3
        poly_G1 = sum(G1_ser[i] * z**i for i in range(m))
        rhs = sp.expand(1 + z * poly_G1**2 + z * poly_G1**3)
        G1_ser[m] = sp.Poly(rhs, z).coeff_monomial(z**m)
    G1_expr = sum(G1_ser[i] * z**i for i in range(11))
    A_eval = sp.series(to_expr(A_vec).subs(G, G1_expr), z, 0, 11).removeO()
    for n in range(1, 11):
        coeff = sp.Poly(A_eval, z).coeff_monomial(z**n)
        assert coeff == a_binomial(n), f"A(z) series mismatch at z^{n}: {coeff}"

    # 3. Define theta = z * d/dz on A
    def theta_A(vec):
        a0, a1, a2 = vec
        # theta(a0 + a1*G + a2*G^2) = z*a0' + z*a1'*G + z*a2'*G^2 + z*(a1 + 2*a2*G)*G'
        base = normalize(z * sp.diff(a0, z) + z * sp.diff(a1, z) * G + z * sp.diff(a2, z) * G**2)
        chain = mul_A(normalize(z * a1 + 2 * z * a2 * G), Gp_vec)
        return (
            sp.cancel(base[0] + chain[0]),
            sp.cancel(base[1] + chain[1]),
            sp.cancel(base[2] + chain[2]),
        )

    def apply_poly_theta(poly_coeffs_0_to_3, vec):
        # poly_coeffs_0_to_3 = [d0, d1, d2, d3] for d0 + d1*theta + d2*theta^2 + d3*theta^3
        v0 = vec
        v1 = theta_A(v0)
        v2 = theta_A(v1)
        v3 = theta_A(v2)
        d0, d1, d2, d3 = poly_coeffs_0_to_3
        return tuple(
            sp.cancel(d0 * v0[i] + d1 * v1[i] + d2 * v2[i] + d3 * v3[i]) for i in range(3)
        )

    # Expand c0(n), c1(n), c2(n), c3(n) in monomial basis [1, n, n^2, n^3]
    n_sym = sp.Symbol("n")
    polys = [
        sp.Poly(c0(n_sym), n_sym),
        sp.Poly(c1(n_sym), n_sym),
        sp.Poly(c2(n_sym), n_sym),
        sp.Poly(c3(n_sym), n_sym),
    ]
    Phi = (sp.Integer(0), sp.Integer(0), sp.Integer(0))
    for r, p in enumerate(polys):
        coeffs = [p.coeff_monomial(n_sym**k) for k in range(4)]
        zr_A = tuple(sp.cancel(z**r * A_vec[i]) for i in range(3))
        term = apply_poly_theta(coeffs, zr_A)
        Phi = tuple(sp.cancel(Phi[i] + term[i]) for i in range(3))

    assert Phi[1] == 0 and Phi[2] == 0, f"Nonzero G/G^2 terms in Phi: {Phi}"
    assert sp.simplify(Phi[0] - (-42291 * z - 49573 * z**2)) == 0, f"Unexpected Phi[0]: {Phi[0]}"
    print(f"Exact differential-algebraic reduction in Q(z)[G]/(P): Phi(z) = {Phi[0]}: OK")


def main() -> None:
    test_combinatorics_and_data()
    test_algebraic_proof_in_A()
    print("PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact finite-field polynomial arithmetic verifier for targets/minac-2411.01768-rem5.14/.

Pure integer/tuple arithmetic (zero floats). Checks every counterexample directly from
the primary-source definition G_f(D): adjacent(a, b) <=> gcd(a - b, f) in D.
"""

from __future__ import annotations


def poly_norm(a: tuple[int, ...], p: int) -> tuple[int, ...]:
    res = [c % p for c in a]
    while res and res[-1] == 0:
        res.pop()
    return tuple(res)


def poly_deg(a: tuple[int, ...]) -> int:
    return len(a) - 1


def poly_add(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    n = max(len(a), len(b))
    res = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    return poly_norm(tuple(res), p)


def poly_sub(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    n = max(len(a), len(b))
    res = [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)]
    return poly_norm(tuple(res), p)


def poly_mul(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    if not a or not b:
        return ()
    res = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            res[i + j] += ai * bj
    return poly_norm(tuple(res), p)


def poly_divmod(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    assert b, "Division by zero polynomial"
    a_list = list(poly_norm(a, p))
    db = len(b) - 1
    inv_lc = pow(b[-1], p - 2, p)
    q_len = max(0, len(a_list) - db)
    q = [0] * q_len
    for k in range(q_len - 1, -1, -1):
        coeff = (a_list[k + db] * inv_lc) % p
        if coeff:
            q[k] = coeff
            for j in range(db + 1):
                a_list[k + j] = (a_list[k + j] - coeff * b[j]) % p
    return poly_norm(tuple(q), p), poly_norm(tuple(a_list), p)


def poly_mod(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    return poly_divmod(a, b, p)[1]


def poly_gcd_monic(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    a = poly_norm(a, p)
    b = poly_norm(b, p)
    while b:
        a, b = b, poly_mod(a, b, p)
    if not a:
        return ()
    inv_lc = pow(a[-1], p - 2, p)
    return tuple((c * inv_lc) % p for c in a)


def all_polys_below_deg(d: int, p: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for n in range(p**d):
        coeffs = []
        x = n
        for _ in range(d):
            coeffs.append(x % p)
            x //= p
        out.append(poly_norm(tuple(coeffs), p))
    return out


def is_irreducible(f: tuple[int, ...], p: int) -> bool:
    d = poly_deg(f)
    if d <= 0:
        return False
    if d == 1:
        return True
    for deg_test in range(1, d // 2 + 1):
        for coeffs in all_polys_below_deg(deg_test, p):
            # Test monic polynomials of degree deg_test
            cand = coeffs + (0,) * (deg_test - len(coeffs)) + (1,)
            if len(cand) - 1 == deg_test:
                if poly_mod(f, cand, p) == ():
                    return False
    return True


def divisors_of_powers(factors: list[tuple[tuple[int, ...], int]], p: int) -> list[tuple[int, ...]]:
    divs: list[tuple[int, ...]] = [(1,)]
    for irr, mult in factors:
        nxt: list[tuple[int, ...]] = []
        cur = (1,)
        for _ in range(mult + 1):
            for d in divs:
                nxt.append(poly_mul(d, cur, p))
            cur = poly_mul(cur, irr, p)
        divs = nxt
    return divs


def verify_case(
    name: str,
    p: int,
    g_factors: list[tuple[tuple[int, ...], int]],
    h_factors: list[tuple[tuple[int, ...], int]],
    check_full_adjacency: bool = True,
) -> None:
    all_factors = g_factors + h_factors
    irrs = [irr for irr, _ in all_factors]
    # Verify irreducibility and pairwise distinct degrees
    degs = [poly_deg(irr) for irr in irrs]
    for irr in irrs:
        assert is_irreducible(irr, p), f"{name}: {irr} not irreducible mod {p}"
    assert len(set(degs)) == len(degs), f"{name}: degrees not distinct: {degs}"

    g = (1,)
    for irr, e in g_factors:
        for _ in range(e):
            g = poly_mul(g, irr, p)
    h = (1,)
    for irr, e in h_factors:
        for _ in range(e):
            h = poly_mul(h, irr, p)
    assert poly_gcd_monic(g, h, p) == (1,)
    assert poly_deg(g) == poly_deg(h) >= 1
    d = poly_deg(g)
    f = poly_mul(g, h, p)

    div_f = set(divisors_of_powers(all_factors, p))
    div_g = set(divisors_of_powers(g_factors, p))
    div_h = set(divisors_of_powers(h_factors, p))

    D1 = {poly_mul(g, u, p) for u in div_h if u != h}
    D2 = {poly_mul(h, v, p) for v in div_g if v != g}
    assert D1 != D2 and D1.isdisjoint(D2)
    assert f not in D1 and f not in D2
    assert D1.issubset(div_f) and D2.issubset(div_f)

    D1_comp = (div_f - {f}) - D1
    D2_comp = (div_f - {f}) - D2
    assert D1_comp != D2_comp

    # Build vertex set R = F_p[x]/(f) and CRT map theta: R -> (F_p[x]/(g)) x (F_p[x]/(h))
    verts = all_polys_below_deg(2 * d, p)
    assert len(verts) == p ** (2 * d)

    def pad_to_d(poly: tuple[int, ...]) -> tuple[int, ...]:
        return poly + (0,) * (d - len(poly))

    theta: dict[tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]] = {}
    inv_theta: dict[tuple[tuple[int, ...], tuple[int, ...]], tuple[int, ...]] = {}
    for a in verts:
        key = (pad_to_d(poly_mod(a, g, p)), pad_to_d(poly_mod(a, h, p)))
        theta[a] = key
        inv_theta[key] = a
    assert len(inv_theta) == len(verts)

    # Explicit isomorphism bijection Phi: (x, y) -> (y, x) via padded coefficient tuples
    phi = {a: inv_theta[(theta[a][1], theta[a][0])] for a in verts}
    assert len(set(phi.values())) == len(verts)

    if check_full_adjacency:
        # Exhaustively verify every pair (a, b) directly from primary definition gcd(a - b, f) in D
        for a in verts:
            deg_D1 = 0
            deg_D2 = 0
            for b in verts:
                if a == b:
                    continue
                diff = poly_sub(a, b, p)
                gc = poly_gcd_monic(diff, f, p)
                e1 = gc in D1
                e2 = poly_gcd_monic(poly_sub(phi[a], phi[b], p), f, p) in D2
                assert e1 == e2, f"{name}: isomorphism failed at ({a}, {b})"
                # Also check complement graphs G_f(D1_comp) and G_f(D2_comp)
                ec1 = gc in D1_comp
                ec2 = poly_gcd_monic(poly_sub(phi[a], phi[b], p), f, p) in D2_comp
                assert ec1 == ec2
                if e1:
                    deg_D1 += 1
                if poly_gcd_monic(diff, f, p) in D2:
                    deg_D2 += 1
            assert deg_D1 == p**d - 1 and deg_D2 == p**d - 1
    else:
        # Verify generating sets S_D1, S_D2 directly against (g)/(f)\{0} and (h)/(f)\{0}
        S1 = {a for a in verts if a != () and poly_gcd_monic(a, f, p) in D1}
        S2 = {a for a in verts if a != () and poly_gcd_monic(a, f, p) in D2}
        assert len(S1) == p**d - 1 and len(S2) == p**d - 1
        assert {phi[a] for a in S1} == S2

    print(
        f"  VERIFIED {name}: q={p}, deg(f)={2*d}, irr_degs={degs}, "
        f"|R|={len(verts)}, |D1|={len(D1)}, |D2|={len(D2)}"
    )


def main() -> int:
    # 1. Minimal example over F_2[x]: f = x^2 (x^2 + x + 1) (16 vertices)
    verify_case(
        "F_2[x], f = x^2 (x^2+x+1)",
        p=2,
        g_factors=[((0, 1), 2)],
        h_factors=[((1, 1, 1), 1)],
        check_full_adjacency=True,
    )
    # 2. Minimal squarefree example over F_2[x]: f = x (x^2 + x + 1)(x^3 + x + 1) (64 vertices)
    verify_case(
        "F_2[x], f = x (x^2+x+1)(x^3+x+1) [squarefree]",
        p=2,
        g_factors=[((0, 1), 1), ((1, 1, 1), 1)],
        h_factors=[((1, 1, 0, 1), 1)],
        check_full_adjacency=True,
    )
    # 3. Cubic example over F_2[x]: f = x^3 (x^3 + x + 1) (64 vertices)
    verify_case(
        "F_2[x], f = x^3 (x^3+x+1)",
        p=2,
        g_factors=[((0, 1), 3)],
        h_factors=[((1, 1, 0, 1), 1)],
        check_full_adjacency=True,
    )
    # 4. Odd characteristic F_3[x]: f = x^2 (x^2 + 1) (81 vertices)
    verify_case(
        "F_3[x], f = x^2 (x^2+1)",
        p=3,
        g_factors=[((0, 1), 2)],
        h_factors=[((1, 0, 1), 1)],
        check_full_adjacency=True,
    )
    # 5. Odd characteristic F_5[x]: f = x^2 (x^2 + 2) (625 vertices)
    verify_case(
        "F_5[x], f = x^2 (x^2+2)",
        p=5,
        g_factors=[((0, 1), 2)],
        h_factors=[((2, 0, 1), 1)],
        check_full_adjacency=False,
    )
    print(
        "PASS: arXiv:2411.01768v2 Remark 5.14 refuted — explicit isomorphic gcd-graphs "
        "G_f(D_1) ~= G_f(D_2) with distinct-degree irreducible factors verified over F_2, F_3, F_5."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

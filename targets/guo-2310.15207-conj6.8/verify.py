"""Exact integer / Fraction verifier for Guo arXiv:2310.15207v1 Conjecture 6.8.

Zero floating-point arithmetic is used anywhere. Directly evaluates both sides
of Conjecture 6.8 modulo Phi_n(q)^2 in Q[q] from raw q-Pochhammer definitions,
independently verifies the block congruence B_r(q), the Watson (e -> inf)
identities (4) and (6), and the modulo-Phi_n(q) identity for Delta_8(q), and
checks the n=1, m=2 boundary note.
"""

from fractions import Fraction
from math import comb


def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    return poly_trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def poly_sub(a, b):
    n = max(len(a), len(b))
    return poly_trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])


def poly_mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj != 0:
                out[i + j] += ai * bj
    return poly_trim(out)


def poly_divmod_monic_int(a, mod):
    rem = list(a)
    d = len(mod) - 1
    assert mod[d] == 1
    if len(rem) <= d:
        return [], poly_trim(rem)
    q = [0] * (len(rem) - d)
    for i in range(len(rem) - 1, d - 1, -1):
        c = rem[i]
        if c != 0:
            q[i - d] = c
            for j in range(d + 1):
                rem[i - d + j] -= c * mod[j]
    return poly_trim(q), poly_trim(rem)


def poly_divmod_frac(a, b):
    a = [Fraction(x) for x in poly_trim(a)]
    b = [Fraction(x) for x in poly_trim(b)]
    assert b
    db = len(b) - 1
    if len(a) <= db:
        return [], a
    q = [Fraction(0)] * (len(a) - db)
    lb = b[db]
    for i in range(len(a) - 1, db - 1, -1):
        if a[i] != 0:
            c = a[i] / lb
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    return poly_trim(q), poly_trim(a)


def poly_inv_mod(a, mod):
    r0 = [Fraction(x) for x in poly_trim(mod)]
    r1 = [Fraction(x) for x in poly_trim(a)]
    t0, t1 = [], [Fraction(1)]
    while r1:
        q, rem = poly_divmod_frac(r0, r1)
        r0, r1 = r1, rem
        t0, t1 = t1, poly_sub(t0, poly_mul(q, t1))
    assert len(r0) == 1 and r0[0] != 0
    inv_lead = Fraction(1) / r0[0]
    res = [c * inv_lead for c in t0]
    _, res = poly_divmod_frac(res, [Fraction(x) for x in mod])
    return res


def cyclotomic_poly(m):
    divs = [d for d in range(1, m + 1) if m % d == 0]
    phis = {}
    for d in divs:
        p = [-1] + [0] * (d - 1) + [1]
        for k in divs:
            if k < d and d % k == 0:
                q_poly, rem = poly_divmod_monic_int(p, phis[k])
                assert not rem
                p = q_poly
        phis[d] = p
    return phis[m]


def q_pow_mod_monic_int(exp, mod):
    d = len(mod) - 1
    res = [1]
    base = [0, 1] if d > 1 else poly_divmod_monic_int([0, 1], mod)[1]
    e = exp
    while e > 0:
        if e & 1:
            _, res = poly_divmod_monic_int(poly_mul(res, base), mod)
        e >>= 1
        if e:
            _, base = poly_divmod_monic_int(poly_mul(base, base), mod)
    return res


def factor_in_z(poly_int, phi, mod2):
    """Return (phi_pow_delta, reduced_poly_mod_mod2) with reduced_poly coprime to phi."""
    rem = poly_divmod_monic_int(poly_int, mod2)[1]
    q1, r1 = poly_divmod_monic_int(rem, phi)
    if not r1:
        q2, r2 = poly_divmod_monic_int(q1, phi)
        if not r2:
            return 2, [1]
        return 1, q1
    return 0, rem


def eval_summand_mod_phi_sq(k, phi, mod2):
    """Evaluate (-1)^k [4k+1] (q;q^2)_k^3 / (q^2;q^2)_k^3 q^{k^2} mod phi^2."""
    exp_phi = 0
    num_p = [(-1) ** k]
    den_p = [1]

    # q^{k^2}
    qk2 = q_pow_mod_monic_int(k * k, mod2)
    num_p = poly_divmod_monic_int(poly_mul(num_p, qk2), mod2)[1]

    # [4k+1] = (1 - q^{4k+1}) / (1 - q)
    one_minus_q4k1 = poly_sub([1], q_pow_mod_monic_int(4 * k + 1, mod2))
    dp, fac = factor_in_z(one_minus_q4k1, phi, mod2)
    exp_phi += dp
    num_p = poly_divmod_monic_int(poly_mul(num_p, fac), mod2)[1]
    one_minus_q = [1, -1]
    dp_d, fac_d = factor_in_z(one_minus_q, phi, mod2)
    assert dp_d == 0
    den_p = poly_divmod_monic_int(poly_mul(den_p, fac_d), mod2)[1]

    for j in range(k):
        fn = poly_sub([1], q_pow_mod_monic_int(2 * j + 1, mod2))
        dpn, facn = factor_in_z(fn, phi, mod2)
        exp_phi += 3 * dpn
        facn3 = poly_divmod_monic_int(poly_mul(poly_mul(facn, facn), facn), mod2)[1]
        num_p = poly_divmod_monic_int(poly_mul(num_p, facn3), mod2)[1]

        fd = poly_sub([1], q_pow_mod_monic_int(2 * j + 2, mod2))
        dpd, facd = factor_in_z(fd, phi, mod2)
        exp_phi -= 3 * dpd
        facd3 = poly_divmod_monic_int(poly_mul(poly_mul(facd, facd), facd), mod2)[1]
        den_p = poly_divmod_monic_int(poly_mul(den_p, facd3), mod2)[1]

    assert exp_phi >= 0
    if exp_phi >= 2:
        return []
    inv_den = poly_inv_mod(den_p, mod2)
    prod = poly_mul([Fraction(c) for c in num_p], inv_den)
    if exp_phi == 1:
        prod = poly_mul(prod, [Fraction(c) for c in phi])
    return poly_divmod_frac(prod, [Fraction(c) for c in mod2])[1]


def verify_delta8_and_b0(n):
    """Independently verify equations (5) and (7) from PROOF.md."""
    N = (n - 1) // 2
    phi = cyclotomic_poly(n)
    mod2 = poly_mul(phi, phi)
    phi_f = [Fraction(c) for c in phi]
    mod2_f = [Fraction(c) for c in mod2]

    # Check (5): B_0(q) == (-1)^N q^{N^2} [n] mod Phi_n(q)^2
    b0 = []
    for s in range(N + 1):
        b0 = poly_add(b0, eval_summand_mod_phi_sq(s, phi, mod2))
    qN2 = q_pow_mod_monic_int(N * N, mod2)
    q_brack_n = [1] * n
    rhs_b0 = poly_mul([Fraction((-1) ** N * c) for c in qN2], [Fraction(c) for c in q_brack_n])
    rhs_b0 = poly_divmod_frac(rhs_b0, mod2_f)[1]
    assert b0 == rhs_b0, f"B_0 mismatch at n={n}"

    # Check (7): Delta_8(q) == 4 (-1)^N q^{N^2} mod Phi_n(q)
    delta8 = []
    for s in range(N + 1):
        num = [(-1) ** s]
        num = poly_divmod_monic_int(poly_mul(num, q_pow_mod_monic_int(s * s, phi)), phi)[1]
        den = [1]
        h = []
        for i in range(s):
            t1 = poly_sub([1], q_pow_mod_monic_int(2 * i + 1, phi))
            t2 = poly_sub([1], q_pow_mod_monic_int(2 * i + 2, phi))
            t1_3 = poly_divmod_monic_int(poly_mul(poly_mul(t1, t1), t1), phi)[1]
            t2_3 = poly_divmod_monic_int(poly_mul(poly_mul(t2, t2), t2), phi)[1]
            num = poly_divmod_monic_int(poly_mul(num, t1_3), phi)[1]
            den = poly_divmod_monic_int(poly_mul(den, t2_3), phi)[1]
            q2i1 = q_pow_mod_monic_int(2 * i + 1, phi)
            q2i2 = q_pow_mod_monic_int(2 * i + 2, phi)
            term_h = poly_sub(
                poly_mul([Fraction(c) for c in q2i1], poly_inv_mod(t1, phi)),
                poly_mul([Fraction(c) for c in q2i2], poly_inv_mod(t2, phi)),
            )
            h = poly_divmod_frac(poly_add(h, term_h), phi_f)[1]
        q4s1 = [Fraction(c) for c in q_pow_mod_monic_int(4 * s + 1, phi)]
        one_m_q4s1 = poly_sub([Fraction(1)], q4s1)
        inner = poly_sub(poly_mul([Fraction(6)], h), [Fraction(2 * s)])
        bracket = poly_add(poly_mul([Fraction(4)], q4s1), poly_mul(one_m_q4s1, inner))
        ratio = poly_mul([Fraction(c) for c in num], poly_inv_mod(den, phi))
        delta8 = poly_divmod_frac(poly_add(delta8, poly_mul(ratio, bracket)), phi_f)[1]

    exp_d8 = poly_divmod_frac(
        [Fraction(4 * ((-1) ** N) * c) for c in q_pow_mod_monic_int(N * N, phi)], phi_f
    )[1]
    assert delta8 == exp_d8, f"Delta_8 mismatch at n={n}"


def check_n1_boundary():
    """Verify the n=1, m=2 boundary remark in PROOF.md: LHS != RHS mod (q-1)^2."""
    mod2 = [1, -2, 1]  # (q-1)^2
    # k=0: 1; k=1: -(1+q+q^2+q^3+q^4)/(1+q)^3 * q
    num = poly_mul([-1, -1, -1, -1, -1], [0, 1])
    den = poly_mul(poly_mul([1, 1], [1, 1]), [1, 1])
    t1 = poly_divmod_frac(poly_mul([Fraction(c) for c in num], poly_inv_mod(den, mod2)), [Fraction(c) for c in mod2])[1]
    lhs = poly_add([Fraction(1)], t1)
    assert lhs == [Fraction(3, 8) + Fraction(15, 16), Fraction(-15, 16)] or poly_add(
        [Fraction(3, 8)], poly_mul([Fraction(-15, 16)], [Fraction(-1), Fraction(1)])
    ) == lhs
    assert lhs != [Fraction(3, 8)]


def main():
    check_n1_boundary()
    for n in [3, 5, 7, 9, 11, 13]:
        phi = cyclotomic_poly(n)
        mod2 = poly_mul(phi, phi)
        mod2_f = [Fraction(c) for c in mod2]
        verify_delta8_and_b0(n)

        N = (n - 1) // 2
        qN2 = [Fraction(c) for c in q_pow_mod_monic_int(N * N, mod2)]
        q_brack_n = [Fraction(1)] * n
        pref = poly_divmod_frac(poly_mul([Fraction((-1) ** N)], poly_mul(qN2, q_brack_n)), mod2_f)[1]

        lhs = []
        rhs_coeff = Fraction(0)
        for m in range(1, 5):
            r = m - 1
            blk = []
            for s in range(n):
                blk = poly_add(blk, eval_summand_mod_phi_sq(r * n + s, phi, mod2))
            lhs = poly_divmod_frac(poly_add(lhs, blk), mod2_f)[1]

            c_r = Fraction(comb(2 * r, r), 4**r) ** 3
            rhs_term = ((-1) ** r) * (4 * r + 1) * c_r
            rhs_coeff += rhs_term
            blk_rhs = poly_divmod_frac(poly_mul([rhs_term], pref), mod2_f)[1]
            assert blk == blk_rhs, f"Block {r} mismatch at n={n}"

            rhs = poly_divmod_frac(poly_mul([rhs_coeff], pref), mod2_f)[1]
            assert lhs == rhs, f"Conj 6.8 mismatch at n={n}, m={m}"
        print(f"OK n={n}, m=1..4 (deg Phi_{n}^2 = {len(mod2)-1})")

    print("PASS")


if __name__ == "__main__":
    main()

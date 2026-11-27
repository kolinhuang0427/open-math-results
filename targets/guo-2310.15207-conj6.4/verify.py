"""Exact integer / Fraction verifier for Guo arXiv:2310.15207v1 Conjectures 6.4 and 6.3.

Zero floating-point arithmetic is used anywhere. All polynomial operations work
directly in Z[q] or Q[q] modulo Phi_{n^s}(q)^2 from the raw q-Pochhammer
definitions (without assuming the proof's telescoping or Delta Q identities),
and intermediate proof lemmas are also verified independently.
"""

from fractions import Fraction


def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    return poly_trim(out)


def poly_sub(a, b):
    n = max(len(a), len(b))
    out = [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)]
    return poly_trim(out)


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
    """Exact integer-coefficient division of a by monic integer polynomial mod."""
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
    """Exact polynomial division over Q using Fraction."""
    a = [Fraction(x) for x in poly_trim(a)]
    b = [Fraction(x) for x in poly_trim(b)]
    assert b, "Division by zero polynomial"
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
    """Compute multiplicative inverse of polynomial a modulo mod in Q[q]."""
    r0 = [Fraction(x) for x in poly_trim(mod)]
    r1 = [Fraction(x) for x in poly_trim(a)]
    t0, t1 = [], [Fraction(1)]
    while r1:
        q, rem = poly_divmod_frac(r0, r1)
        r0, r1 = r1, rem
        t0, t1 = t1, poly_sub(t0, poly_mul(q, t1))
    assert len(r0) == 1 and r0[0] != 0, "Polynomial is not invertible modulo mod"
    inv_lead = Fraction(1) / r0[0]
    res = [c * inv_lead for c in t0]
    _, res = poly_divmod_frac(res, [Fraction(x) for x in mod])
    return res


def cyclotomic_poly(m):
    """Exact integer coefficients of Phi_m(q) = (q^m - 1) / prod_{d|m, d<m} Phi_d(q)."""
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
    """Compute q^exp mod (monic int poly mod) via binary exponentiation."""
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


def eval_ratio_mod_phi_sq(num_exps, den_exps, phi, mod2):
    """Evaluate prod_{m in num_exps}(1-q^m) / prod_{m in den_exps}(1-q^m) mod phi^2 in Q[q]."""
    exp_phi = 0
    num_p = [1]
    den_p = [1]

    for m in num_exps:
        _, rem_mod2 = poly_divmod_monic_int(poly_sub([1], q_pow_mod_monic_int(m, mod2)), mod2)
        q_phi, r_phi = poly_divmod_monic_int(rem_mod2, phi)
        if not r_phi:
            exp_phi += 1
            num_p = poly_divmod_monic_int(poly_mul(num_p, q_phi), mod2)[1]
        else:
            num_p = poly_divmod_monic_int(poly_mul(num_p, rem_mod2), mod2)[1]

    for m in den_exps:
        _, rem_mod2 = poly_divmod_monic_int(poly_sub([1], q_pow_mod_monic_int(m, mod2)), mod2)
        q_phi, r_phi = poly_divmod_monic_int(rem_mod2, phi)
        if not r_phi:
            exp_phi -= 1
            den_p = poly_divmod_monic_int(poly_mul(den_p, q_phi), mod2)[1]
        else:
            den_p = poly_divmod_monic_int(poly_mul(den_p, rem_mod2), mod2)[1]

    assert exp_phi >= 0, f"Denominator still divisible by Phi after cancellation: exp_phi={exp_phi}"
    if exp_phi >= 2:
        return []
    inv_den = poly_inv_mod(den_p, mod2)
    num_frac = [Fraction(c) for c in num_p]
    prod = poly_mul(num_frac, inv_den)
    if exp_phi == 1:
        prod = poly_mul(prod, [Fraction(c) for c in phi])
    _, res = poly_divmod_frac(prod, [Fraction(c) for c in mod2])
    return res


def conj4_factors(n, exp):
    u1 = (n**exp - 1) // 4
    u2 = (n ** (exp - 1) - 1) // 4
    num = [1 + 2 * j for j in range(u1)] + [2 * n + 2 * n * j for j in range(u2)]
    den = [2 + 2 * j for j in range(u1)] + [n + 2 * n * j for j in range(u2)]
    return num, den


def conj3_factors(n, exp):
    v1 = (n**exp - 1) // 2
    v2 = (n ** (exp - 1) - 1) // 2
    # [n] = (1 - q^n)/(1 - q)
    num = [n] + [3 + 4 * j for j in range(v1)] + [5 * n + 4 * n * j for j in range(v2)]
    den = [1] + [5 + 4 * j for j in range(v1)] + [3 * n + 4 * n * j for j in range(v2)]
    return num, den


def verify_proof_lemmas(n, s, r):
    """Independently verify Equations (3), (4), (5), (6), and vanishing mod Phi_N(q)."""
    N = n**s
    phi = cyclotomic_poly(N)
    phi_frac = [Fraction(c) for c in phi]

    # Verify Conjecture 6.4 Delta Q_4(a) and cancellation
    k0 = (n ** (r - 1) - 1) // 4
    k1 = (n**r - 1) // 4
    j0 = (n ** (r - 2) - 1) // 4
    odd_n_mults = sorted(2 * k + 1 for k in range(k0, k1) if (2 * k + 1) % n == 0)
    even_n_mults = sorted(2 * k + 2 for k in range(k0, k1) if (2 * k + 2) % n == 0)
    assert odd_n_mults == [n * (2 * j + 1) for j in range(j0, k0)]
    assert even_n_mults == [n * (2 * j + 2) for j in range(j0, k0)]

    # Block 0 quotients for R_4
    num_rem = [2 * (k0 + i) + 1 for i in range(N) if (2 * (k0 + i) + 1) % n != 0]
    den_rem = [2 * (k0 + i) + 2 for i in range(N) if (2 * (k0 + i) + 2) % n != 0]
    q_num = {m % N: m // N for m in num_rem}
    q_den = {m % N: m // N for m in den_rem}
    assert set(q_num.keys()) == set(q_den.keys()) == {a for a in range(1, N) if a % n != 0}
    sum_poly_4 = []
    for a in sorted(q_num):
        dq = q_num[a] - q_den[a]
        expected_dq = ((-1) ** (a - 1)) if a <= (N - 1) // 2 else ((-1) ** a)
        assert dq == expected_dq, f"Delta Q_4 mismatch at n={n},s={s},r={r},a={a}"
        q_a = [Fraction(0)] * a + [Fraction(1)]
        one_minus_qa = [Fraction(1)] + [Fraction(0)] * (a - 1) + [Fraction(-1)]
        term = poly_mul([Fraction(dq)], poly_mul(q_a, poly_inv_mod(one_minus_qa, phi_frac)))
        _, term = poly_divmod_frac(term, phi_frac)
        sum_poly_4 = poly_add(sum_poly_4, term)
    _, sum_poly_4 = poly_divmod_frac(sum_poly_4, phi_frac)
    assert sum_poly_4 == [], f"Sum for Conj 6.4 did not vanish mod Phi_{N}"

    # Verify Conjecture 6.3 cancellation and Delta Q_3(a)
    v0 = (n ** (r - 1) - 1) // 2
    v1 = (n**r - 1) // 2
    w0 = (n ** (r - 2) - 1) // 2
    mult_3 = sorted(4 * k + 3 for k in range(v0, v1) if (4 * k + 3) % n == 0)
    mult_5 = sorted(4 * k + 5 for k in range(v0, v1) if (4 * k + 5) % n == 0)
    assert mult_3 == [n * (4 * j + 3) for j in range(w0, v0)]
    assert mult_5 == [n * (4 * j + 5) for j in range(w0, v0)]

    num3_rem = [4 * (v0 + i) + 3 for i in range(N) if (4 * (v0 + i) + 3) % n != 0]
    den3_rem = [4 * (v0 + i) + 5 for i in range(N) if (4 * (v0 + i) + 5) % n != 0]
    q1 = {m % N: m // N for m in num3_rem}
    q2 = {m % N: m // N for m in den3_rem}
    assert set(q1.keys()) == set(q2.keys()) == {a for a in range(1, N) if a % n != 0}
    sum_poly_3 = []
    for a in sorted(q1):
        dq = q1[a] - q2[a]
        expected_dq = -2 if (a % 4 in (0, 1)) else 2
        assert dq == expected_dq, f"Delta Q_3 mismatch at n={n},s={s},r={r},a={a}"
        q_a = [Fraction(0)] * a + [Fraction(1)]
        one_minus_qa = [Fraction(1)] + [Fraction(0)] * (a - 1) + [Fraction(-1)]
        term = poly_mul([Fraction(dq)], poly_mul(q_a, poly_inv_mod(one_minus_qa, phi_frac)))
        _, term = poly_divmod_frac(term, phi_frac)
        sum_poly_3 = poly_add(sum_poly_3, term)
    _, sum_poly_3 = poly_divmod_frac(sum_poly_3, phi_frac)
    assert sum_poly_3 == [], f"Sum for Conj 6.3 did not vanish mod Phi_{N}"


def main():
    cases = [
        (5, 1, 2),
        (5, 1, 3),
        (5, 2, 3),
        (9, 1, 2),
        (9, 1, 3),
        (13, 1, 2),
        (17, 1, 2),
        (21, 1, 2),
    ]
    for n, s, r in cases:
        assert n % 4 == 1 and n > 1 and r > s >= 1
        N = n**s
        phi = cyclotomic_poly(N)
        mod2 = poly_mul(phi, phi)

        n4_r, d4_r = conj4_factors(n, r)
        n4_s, d4_s = conj4_factors(n, s)
        val4_r = eval_ratio_mod_phi_sq(n4_r, d4_r, phi, mod2)
        val4_s = eval_ratio_mod_phi_sq(n4_s, d4_s, phi, mod2)
        assert val4_r == val4_s, f"Conjecture 6.4 failed at (n={n}, s={s}, r={r})"

        n3_r, d3_r = conj3_factors(n, r)
        n3_s, d3_s = conj3_factors(n, s)
        val3_r = eval_ratio_mod_phi_sq(n3_r, d3_r, phi, mod2)
        val3_s = eval_ratio_mod_phi_sq(n3_s, d3_s, phi, mod2)
        assert val3_r == val3_s, f"Conjecture 6.3 failed at (n={n}, s={s}, r={r})"

        verify_proof_lemmas(n, s, r)
        print(f"OK n={n}, s={s}, r={r} (deg Phi_{N}^2 = {len(mod2)-1})")

    print("PASS")


if __name__ == "__main__":
    main()

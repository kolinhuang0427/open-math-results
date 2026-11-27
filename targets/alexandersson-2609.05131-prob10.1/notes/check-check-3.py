"""Independent exact-arithmetic and rigorous-interval verifier for
targets/alexandersson-2609.05131-prob10.1/ (PROOF.md).

Zero Python floats anywhere in this script. Uses pure int/Fraction for
n = 1..80 (exact Lemma 1.1 GF, DP cross-check, gamma-polynomials, and
primitive Sturm-Cauchy Cauchy index) and 40-digit outward-rounded mpmath.iv
for all analytic Regime B, Regime A, and Seam bounds (n >= 80).
"""

from fractions import Fraction
from math import comb, gcd, isqrt
from mpmath import iv

iv.dps = 40

# Table 1 (tab:ChowTriangle) from arXiv:2609.05131v2 parking-functions.tex L599-608
TAB_CHOW_TRIANGLE = {
    1: [1],
    2: [1, 1],
    3: [1, 7, 1],
    4: [1, 31, 31, 1],
    5: [1, 116, 391, 116, 1],
    6: [1, 407, 3480, 3480, 407, 1],
    7: [1, 1401, 26097, 62651, 26097, 1401, 1],
    8: [1, 4825, 178621, 865129, 865129, 178621, 4825, 1],
    9: [1, 16750, 1162684, 10228978, 20229895, 10228978, 1162684, 16750, 1],
}


def iv_frac(q: Fraction | int) -> iv.mpf:
    if isinstance(q, int):
        return iv.mpf(q)
    return iv.mpf(q.numerator) / iv.mpf(q.denominator)


def poly_add_zz(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul_zz(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def smirnov_dp_chow(n: int) -> list[int]:
    """Compute C_n(t) directly from Proposition 4.1 (eq:lastLetterRecurrence)."""
    m = n + 1
    F = [[1] for _ in range(m)]
    for _ in range(1, n):
        # Prefix sums and suffix sums
        pref = [[0]]
        for j in range(m):
            pref.append(poly_add_zz(pref[-1], F[j]))
        total = pref[m]
        nxt = []
        for j in range(m):
            # t * sum_{k < j} F[k] + sum_{k > j} F[k]
            low = [0] + pref[j]
            # sum_{k > j} F[k] = total - pref[j+1]
            pj1 = pref[j + 1]
            high = [
                (total[i] if i < len(total) else 0) - (pj1[i] if i < len(pj1) else 0)
                for i in range(max(len(total), len(pj1)))
            ]
            nxt.append(poly_add_zz(low, high))
        F = nxt
    tot = [0]
    for poly in F:
        tot = poly_add_zz(tot, poly)
    assert all(c % m == 0 for c in tot)
    return [c // m for c in tot]


def gf_chow(n: int) -> list[int]:
    """Compute C_n(t) in ZZ[t] via Lemma 1.1 second rational GF."""
    m = n + 1
    # Numerator at z^n is binom(m, n) = m (constant in t)
    # Wait: (1+z)^m = sum_{j=0}^n binom(m, j) z^j mod z^{n+1}
    # Denominator 1 - sum_{k=2}^n B_k(t) z^k where B_k(t) = binom(m, k) * (t + ... + t^{k-1})
    # Compute U(z) = 1 / (1 - sum_{k=2}^n B_k(t) z^k) mod z^{n+1}, truncated to deg n in t
    # Note: sum_{j=0}^n binom(m, j) U_{n-j}(t) = m * C_n(t)
    U: list[list[int]] = [[1]]  # U_0 = 1
    for r in range(1, n + 1):
        if r == 1:
            U.append([0])
            continue
        # U_r = sum_{k=2}^r binom(m, k) * (t + ... + t^{k-1}) * U_{r-k}
        # Note multiplying a poly P by (t + ... + t^{k-1}) is prefix-sum window
        acc = [0] * n
        for k in range(2, r + 1):
            u_prev = U[r - k]
            if u_prev == [0]:
                continue
            bm = comb(m, k)
            # pref[idx] = sum_{i=0}^{idx} u_prev[i]
            pref = []
            s = 0
            for d_i in range(n):
                s += u_prev[d_i] if d_i < len(u_prev) else 0
                pref.append(s)
            # coeff of t^d in (t + ... + t^{k-1}) * u_prev is sum_{i=max(0, d-(k-1))}^{d-1} u_prev[i]
            for d_i in range(1, n):
                hi = pref[d_i - 1]
                lo = pref[d_i - k] if d_i - k >= 0 else 0
                acc[d_i] += bm * (hi - lo)
        while len(acc) > 1 and acc[-1] == 0:
            acc.pop()
        U.append(acc)

    num_c = [0] * n
    for j in range(n + 1):
        bmj = comb(m, j)
        uj = U[n - j]
        for i, val in enumerate(uj):
            num_c[i] += bmj * val
    assert all(c % m == 0 for c in num_c)
    return [c // m for c in num_c]


def extract_gamma(C: list[int], n: int) -> list[int]:
    """Extract Gamma_n(u) in ZZ[u] from palindromic C_n(t)."""
    assert len(C) == n and C == list(reversed(C))
    d_n = (n - 1) // 2
    rem = list(C)
    gamma = []
    # Precompute powers of (1+t)
    one_p_t = [1, 1]
    pows = [[1]]
    for _ in range(n):
        pows.append(poly_mul_zz(pows[-1], one_p_t))
    for j in range(d_n + 1):
        g_j = rem[j]
        gamma.append(g_j)
        deg_pow = n - 1 - 2 * j
        base = pows[deg_pow]
        for idx, c in enumerate(base):
            rem[j + idx] -= g_j * c
    assert all(v == 0 for v in rem)
    assert gamma[0] == 1 and gamma[-1] > 0 and len(gamma) == d_n + 1
    return gamma


def trim_zz(p: list[int]) -> list[int]:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def primitive_part_zz(p: list[int]) -> list[int]:
    p = trim_zz(p)
    g = 0
    for c in p:
        g = gcd(g, abs(c))
    if g <= 1:
        return p
    return [c // g for c in p]


def pseudo_rem_neg(a: list[int], b: list[int]) -> list[int]:
    """Return -prem(a, b) with positive scaling multiplier, matching Sturm-Cauchy."""
    r = trim_zz(a)
    b = trim_zz(b)
    db = len(b) - 1
    assert db >= 0 and b[-1] != 0
    lcb = b[-1]
    abs_lcb = abs(lcb)
    while len(r) - 1 >= db and r != [0]:
        dr = len(r) - 1
        shift = dr - db
        lcr = r[-1]
        # Multiply r by abs_lcb > 0, subtract sign(lcb) * lcr * t^shift * b
        # Wait: abs_lcb * lcr - (lcr * sgn(lcb)) * lcb = abs_lcb * lcr - lcr * abs_lcb = 0!
        sgn_lcb = 1 if lcb > 0 else -1
        r = [c * abs_lcb for c in r]
        for idx, bc in enumerate(b):
            r[shift + idx] -= sgn_lcb * lcr * bc
        r = trim_zz(r)
    return primitive_part_zz([-c for c in r])


def sign_changes(seq: list[int]) -> int:
    nz = [1 if x > 0 else -1 for x in seq if x != 0]
    return sum(1 for i in range(len(nz) - 1) if nz[i] * nz[i + 1] < 0)


def cauchy_index_neg_inf_to_0(gamma_n: list[int], gamma_n1: list[int]) -> int:
    """Compute I_{-inf}^0(gamma_n / gamma_{n+1}) via exact primitive Sturm-Cauchy PRS."""
    prs = [primitive_part_zz(gamma_n1), primitive_part_zz(gamma_n)]
    while len(prs[-1]) > 1:
        nxt = pseudo_rem_neg(prs[-2], prs[-1])
        assert nxt != [0], "Non-coprime Gamma_n and Gamma_{n+1}!"
        prs.append(nxt)
    # Evaluate signs at -inf: (-1)^{deg p} * lc(p), and at 0: p[0]
    vals_neg_inf = [((-1) ** (len(p) - 1)) * p[-1] for p in prs]
    vals_zero = [p[0] for p in prs]
    assert all(v != 0 for v in vals_zero)
    return sign_changes(vals_neg_inf) - sign_changes(vals_zero)


def verify_analytic_identities() -> None:
    # Spot check Lemma 3.1 (Identity A) and Lemma 3.2 (Identity B) against exact C_n(-s)
    for n in (10, 15, 22):
        C = gf_chow(n)
        m = n + 1
        for s_q in (Fraction(1, 3), Fraction(4, 5)):
            s_iv = iv_frac(s_q)
            exact_val = iv.mpf(0)
            s_pow = iv.mpf(1)
            for idx, c in enumerate(C):
                exact_val += iv.mpf(c) * s_pow
                s_pow *= -s_iv

            # Identity A truncated at k = 40 + bound
            lhs_A = exact_val / (iv.mpf(1) + s_iv)
            sum_A = iv.mpf(0)
            for k in range(41):
                # a_k(n, s) = (1/m) * sum_{j=0}^n comb((k+1)m, n-j)*comb((k+1)m+j-1, j)*s^j
                M_k = (k + 1) * m
                ak = iv.mpf(0)
                sj = iv.mpf(1)
                for j in range(n + 1):
                    ak += iv.mpf(comb(M_k, n - j) * comb(M_k + j - 1, j)) * sj
                    sj *= s_iv
                ak /= iv.mpf(m)
                uk = (s_iv**k) * ak
                if k == 40:
                    tail_ub = uk
                else:
                    sum_A += ((-1) ** k) * uk
            # Verify discrepancy within tail_ub (alternating series? actually |rem| <= 2*uk for high k)
            assert abs((lhs_A - sum_A).a) <= iv.mpf(4) * tail_ub.b and abs((lhs_A - sum_A).b) <= iv.mpf(4) * tail_ub.b

            # Identity B: sum_{k=1}^m T_k(n, s) == -(m^2 * s / (1+s)^2) * C_n(-s)
            lhs_B = -(iv.mpf(m * m) * s_iv / ((iv.mpf(1) + s_iv) ** 2)) * exact_val
            y = -iv.log(s_iv) / iv.mpf(m)
            rho = iv.exp(-y)
            theta = iv.pi / iv.mpf(m)
            sum_B = iv.mpf(0)
            for k in range(1, m + 1):
                tk = iv.mpf(2 * k - 1) * theta
                wk = rho * iv.exp(iv.mpc(0, 1) * tk)
                Tk = wk * ((wk + s_iv) ** (n - 1)) / ((iv.mpf(1) - wk) ** (n + 1))
                sum_B += Tk.real
            assert abs(lhs_B - sum_B).b < (iv.mpf(10) ** (-20) * max(iv.mpf(1), abs(lhs_B))).b

    # Check Lemma 3.2(1) exact s = 1 formula (3.7) for odd n = 9, 15
    for q in (4, 7):
        n = 2 * q + 1
        m = n + 1
        C = gf_chow(n)
        c_m1 = sum(((-1) ** idx) * c for idx, c in enumerate(C))
        lhs = ((-1) ** q) * iv.mpf(c_m1)
        rhs = iv.mpf(0)
        for k in range(1, m + 1):
            tk = iv.mpf(2 * k - 1) * iv.pi / iv.mpf(m)
            rhs += (iv.cot(tk / 2) ** (2 * q)) / (iv.sin(tk / 2) ** 2)
        rhs /= iv.mpf(m * m)
        assert abs(lhs - rhs).b < (iv.mpf(10) ** (-20) * max(iv.mpf(1), abs(lhs))).b


def verify_regime_B_and_seam_B() -> dict[str, iv.mpf]:
    m0 = 81
    m0_iv = iv.mpf(m0)
    c_KA = iv_frac(Fraction(22, 10))
    Y_max = iv_frac(Fraction(23, 10))
    theta0 = iv.pi / m0_iv

    # Lemma 4.2(2) D_Phi
    D_Phi = (
        m0_iv
        - (Y_max**2 + iv.pi**2 / m0_iv) / (iv.mpf(12) * (iv.mpf(1) - iv.mpf(1) / (iv.mpf(4) * m0_iv**2)) ** 2)
        - iv.pi**2
    )
    assert D_Phi.a > 10

    # [SEAM-B]
    seam_B = iv.sqrt(m0_iv) * (iv.mpf(1) / c_KA - iv.mpf(1) / Y_max) - (
        iv_frac(Fraction(1, 8))
        + Y_max / (iv.mpf(12) * iv.sqrt(m0_iv) * (iv.mpf(1) - iv.mpf(1) / (iv.mpf(4) * m0_iv**2)))
    )
    assert seam_B.a > 0

    # rel_lo, rel_hi, rho_u, c_min, c_max, s_fac for N = n and N = n+1
    x0 = iv.pi / (Y_max * iv.sqrt(m0_iv))
    af0 = iv.atan2(x0, iv.mpf(1)) / x0
    u_lb_m0 = af0 * x0
    err_lo = (iv.pi * Y_max * (iv.mpf(1) + iv.mpf(1) / (iv.mpf(4) * m0_iv**2))) / (
        iv.mpf(12) * (m0_iv ** iv_frac(Fraction(3, 2))) * ((iv.mpf(1) - iv.mpf(1) / (iv.mpf(4) * m0_iv**2)) ** 2)
    ) + (iv.pi**3) / (iv.mpf(24) * (m0_iv**2) * iv.cos(theta0))
    err_hi = (
        iv.pi / (m0_iv * (m0_iv + 1))
        + iv.pi / (iv.e * (m0_iv - 1) * (m0_iv + 1))
        + (iv.pi**3) / (iv.mpf(24) * (m0_iv**2) * iv.cos(theta0))
    )
    rel_lo = err_lo / u_lb_m0
    rel_hi = err_hi / u_lb_m0
    rho_u = iv.mpf(1) / (iv.mpf(4) * D_Phi)

    params = {
        "n": (
            iv.mpf(1) / (iv.mpf(4) * (iv.mpf(1) + rho_u)),
            iv.mpf(1) / (iv.mpf(4) * (iv.mpf(1) - rho_u)),
        ),
        "n+1": (
            (iv.mpf(1) - rel_lo) - iv.mpf(1) / (iv.mpf(4) * (iv.mpf(1) - rho_u)),
            (iv.mpf(1) + rel_hi) + iv.mpf(1) / (iv.mpf(4) * (iv.mpf(1) - rho_u)),
        ),
    }
    s_fac = {}
    for key, (cmin, cmax) in params.items():
        assert cmin.a > 0 and (cmax * iv.pi / iv.mpf(2)).b < iv.pi.a
        phi_max = cmax * iv.pi / iv.mpf(2)
        s_fac[key] = iv.sin(phi_max) / phi_max

    y_max = Y_max / iv.sqrt(m0_iv)
    S_sh = (iv.exp(y_max / iv.mpf(2)) - iv.exp(-y_max / iv.mpf(2))) / y_max
    c3 = ((iv.mpf(1) - theta0**2 / iv.mpf(6)) ** 2) * (iv.mpf(1) - theta0**2 / iv.mpf(2))
    c5 = (iv.mpf(1) - ((iv.mpf(5) * theta0 / iv.mpf(2)) ** 2) / iv.mpf(6)) ** 2
    nu2 = iv.mpf(2) * (iv.pi**2) * c3
    nu3 = ((iv.mpf(25) * c5 - iv.mpf(1)) / iv.mpf(4)) * (iv.pi**2)

    def nu_k(k: int) -> iv.mpf:
        if k == 2:
            return nu2
        if k == 3:
            return nu3
        r = 2 * k - 1
        return iv.mpf(r * r) - (iv.pi**2) / iv.mpf(4)

    # (B3) lambda < 1
    b3_res = {}
    den_b3 = (S_sh**2 + iv.mpf(1)) * (iv.pi**2)
    B_b3_tail = iv.mpf(4) * nu_k(4) / den_b3
    p_b3 = m0_iv * B_b3_tail / (iv.mpf(1) + B_b3_tail)
    assert p_b3.a > 1
    tail_b3 = ((iv.mpf(1) + B_b3_tail) ** (-m0_iv / iv.mpf(2))) * (iv.mpf(1) + iv.mpf(7) / (iv.mpf(2) * (p_b3 - iv.mpf(1))))
    t2_b3 = (iv.mpf(1) + iv.mpf(4) * nu_k(2) / den_b3) ** (-m0_iv / iv.mpf(2))
    t3_b3 = (iv.mpf(1) + iv.mpf(4) * nu_k(3) / den_b3) ** (-m0_iv / iv.mpf(2))
    for key, (cmin, _) in params.items():
        denom = cmin * s_fac[key] * (iv.pi / iv.mpf(4))
        eb = (t2_b3 + t3_b3 + tail_b3) / denom
        assert eb.b < 1
        b3_res[key] = eb

    # (B4) lambda >= 1, Y_N <= 1/2 (Z = Y_N^{-2} >= 4)
    b4_res = {}
    Ck = {k: iv.mpf(4) * nu_k(k) / (S_sh**2 + iv.mpf(1)) for k in (2, 3, 4)}
    for k in (2, 3, 4):
        assert (m0_iv / (Ck[k] * (m0_iv / iv.mpf(2) - iv.mpf(1)))).b < 4
    p4_b4 = iv.mpf(4) * Ck[4] / (iv.mpf(1) + iv.mpf(4) * Ck[4] / m0_iv)
    assert p4_b4.a > 4

    def eta_over_u_b4(r_int: int, tail_cubic: bool = False) -> tuple[iv.mpf, iv.mpf]:
        # When tail_cubic=True, replace r^3 - r with r^3 so (r/7)^3 * 7^3 = r^3 dominates all r >= 7
        r = iv.mpf(r_int)
        r3m = (r**3) if tail_cubic else (r**3 - r)
        cZ = (r3m / iv.mpf(3)) * (iv.mpf(4) * iv.pi)
        den_fac = iv.mpf(1) - iv.mpf(1) / (iv.mpf(4) * m0_iv**2)
        c0 = (
            ((iv.pi * r3m) / (iv.mpf(540) * (m0_iv**2) * den_fac))
            + ((iv.mpf(2) * iv.pi * (r**3)) / (iv.mpf(76545) * (m0_iv**3)))
            + ((iv.mpf(4) * r) / iv.pi) * (iv.pi * iv.exp(-iv.pi * (iv.mpf(1) - iv.mpf(1) / m0_iv)))
        )
        return cZ, c0

    for key, (cmin, cmax) in params.items():
        den_fac_u = cmin * s_fac[key]
        sum_b4 = iv.mpf(0)
        for k in (2, 3):
            r_int = 2 * k - 1
            tk_Z4 = (iv.mpf(1) + iv.mpf(4) * Ck[k] / m0_iv) ** (-m0_iv / iv.mpf(2))
            cZ, c0 = eta_over_u_b4(r_int, False)
            ratio_k = (iv.mpf(r_int) * cmax + cZ * iv.mpf(4) + c0) * tk_Z4 / den_fac_u
            sum_b4 += ratio_k
        # Tail k >= 4 (r >= 7): scale cubic r^3 by (r/7)^3
        cZ7, c07 = eta_over_u_b4(7, True)
        t4_Z4 = (iv.mpf(1) + iv.mpf(4) * Ck[4] / m0_iv) ** (-m0_iv / iv.mpf(2))
        tail_geom = iv.mpf(1) + iv.mpf(7) / (iv.mpf(2) * (p4_b4 - iv.mpf(4)))
        tail_sum = (iv.mpf(7) * cmax + cZ7 * iv.mpf(4) + c07) * t4_Z4 * tail_geom / den_fac_u
        eb = sum_b4 + tail_sum
        assert eb.b < 1
        b4_res[key] = eb

    # (B5) 1/2 <= Y_N <= 23/10 (18 bins of width 1/10)
    b5_worst = {key: iv.mpf(0) for key in params}
    for bin_idx in range(18):
        Ya = iv_frac(Fraction(5 + bin_idx, 10))
        Yb = iv_frac(Fraction(6 + bin_idx, 10))
        assert (Ya * iv.sqrt(m0_iv) * (iv.mpf(1) - iv.mpf(1) / m0_iv)).a > 1
        x_hi = iv.pi / (Ya * iv.sqrt(m0_iv))
        af = iv.atan2(x_hi, iv.mpf(1)) / x_hi

        def tk_ub(k: int) -> iv.mpf:
            return (iv.mpf(1) + (iv.mpf(4) * nu_k(k)) / (m0_iv * S_sh**2 * Yb**2 + iv.pi**2)) ** (-m0_iv / iv.mpf(2))

        def eta_over_u_b5(r_int: int, tail_cubic: bool = False) -> iv.mpf:
            r = iv.mpf(r_int)
            r3m = (r**3) if tail_cubic else (r**3 - r)
            den_fac = iv.mpf(1) - iv.mpf(1) / (iv.mpf(4) * m0_iv**2)
            t1 = (r3m / iv.mpf(3)) * (iv.pi**2) / (af * (Ya**2))
            t2 = (iv.pi**2 * r3m * (Yb**2)) / (iv.mpf(540) * af * (m0_iv**2) * den_fac)
            t3 = (iv.mpf(8) * (iv.pi**2) * (r**3) * (Yb**4)) / (iv.mpf(76545) * af * (m0_iv**3))
            xm_lo = Ya * iv.sqrt(m0_iv)
            t4 = (r / af) * xm_lo * iv.exp(-xm_lo * (iv.mpf(1) - iv.mpf(1) / m0_iv))
            return t1 + t2 + t3 + t4

        # Tail k >= 10 (r >= 19)
        nu10 = nu_k(10)
        p_tail = iv.mpf(4) * nu10 / ((S_sh**2) * (Yb**2) + (iv.pi**2 + iv.mpf(4) * nu10) / m0_iv)
        assert p_tail.a > 4
        t10_ub = tk_ub(10)
        tail_mult = iv.mpf(1) + iv.mpf(19) / (iv.mpf(2) * (p_tail - iv.mpf(4)))

        for key, (cmin, cmax) in params.items():
            den_fac_u = cmin * s_fac[key]
            tot = iv.mpf(0)
            for k in range(2, 10):
                r_int = 2 * k - 1
                tot += tk_ub(k) * (iv.mpf(r_int) * cmax + eta_over_u_b5(r_int, False)) / den_fac_u
            tot += t10_ub * (iv.mpf(19) * cmax + eta_over_u_b5(19, True)) * tail_mult / den_fac_u
            assert tot.b < 1
            if tot.b > b5_worst[key].b:
                b5_worst[key] = tot

    return {"seam_B": seam_B, "B3": max(b3_res.values(), key=lambda x: x.b), "B4": max(b4_res.values(), key=lambda x: x.b), "B5": max(b5_worst.values(), key=lambda x: x.b)}


def verify_lemma_51_and_regime_A() -> dict[str, iv.mpf]:
    m0 = 81
    m0_iv = iv.mpf(m0)
    c_KA = iv_frac(Fraction(22, 10))
    k_min = 4  # floor(9 / 2.2)

    def beta(j: int) -> iv.mpf:
        jm, j0, jp = iv.mpf(j - 1), iv.mpf(j), iv.mpf(j + 1)
        return jp * iv.log(jp) - iv.mpf(2) * j0 * iv.log(j0) + jm * iv.log(jm)

    def c_const(j: int) -> iv.mpf:
        jm, j0, jp = iv.mpf(j - 1), iv.mpf(j), iv.mpf(j + 1)
        return -iv_frac(Fraction(3, 2)) * iv.log(j0 / jm) + iv_frac(Fraction(1, 2)) * iv.log(jp / j0)

    # Spot-check Lemma 5.1(2) exact bounds (5.3) & (5.4) on N = 24, 50, 80
    for N in (24, 50, 80):
        M = N + 1
        for j in range(2, 8):
            Rj = iv.mpf(comb((j + 1) * M, N)) / iv.mpf(comb(j * M, N))
            Rj1 = iv.mpf(comb((j + 1) * (M + 1), N + 1)) / iv.mpf(comb(j * (M + 1), N + 1))
            del_j = iv.log(Rj) - (iv.mpf(M) * beta(j) + c_const(j))
            assert del_j.a > 0 and del_j.b < (iv_frac(Fraction(13, 12)) / iv.mpf(M * j * (j - 1))).a
            q_diff = iv.log(Rj1 / Rj) - beta(j)
            assert q_diff.a > -(iv_frac(Fraction(5, 24)) / iv.mpf(M * j * (j - 1))).b
            assert q_diff.b < (iv_frac(Fraction(1, 6)) / iv.mpf(M * j * (j - 1))).a

    # Global s_max and E-perturbation bounds
    s_loss = (
        iv_frac(Fraction(3, 2)) / iv.mpf(k_min - 1)
        + (iv.mpf(1) / iv.mpf(3))
        * (
            iv.mpf(1) / iv.mpf(k_min)
            + iv.mpf(1) / iv.mpf(6 * k_min * (k_min**2 - 1))
            + iv.mpf(1) / iv.mpf(6 * m0 * k_min * (k_min - 1))
        )
    )
    s_max_m0 = iv.exp(-(c_KA * iv.sqrt(m0_iv) - s_loss))
    eps_E0 = iv.exp(iv.mpf((m0 + 1) * (m0 + 2)) * s_max_m0 / iv.mpf(2)) - iv.mpf(1)
    eps_E1 = iv.exp(iv.mpf(2 * (m0 + 1)) * s_max_m0) - iv.mpf(1)
    k_eps = (iv.sqrt(m0_iv) / c_KA) * iv.mpf(2 * (m0 + 1)) * s_max_m0 * iv.exp(iv.mpf(2 * (m0 + 1)) * s_max_m0)
    assert s_max_m0.b < iv_frac(Fraction(1, 10**8))
    assert eps_E0.b < iv_frac(Fraction(1, 10**4))

    # [DISJ-A]
    # Check M >= m0 step ratio for (M+1)(2M+1)(27/64)^M:
    # (M+2)(2M+3)/((M+1)(2M+1)) * 27/64 <= (83*165)/(82*163) * 27/64 < 1
    assert Fraction(83 * 165 * 27, 82 * 163 * 64) < 1
    R2_over_R1_ub = iv.mpf((m0 + 1) * (2 * m0 + 1)) * iv.exp(c_const(2) + iv_frac(Fraction(13, 24)) / m0_iv) * (
        iv_frac(Fraction(27, 64)) ** m0
    )
    Q1_ub = iv.mpf(4)
    Q2_ub = iv.exp(beta(2) + iv.mpf(1) / iv.mpf(12 * m0))
    disj_k1 = ((Q1_ub * Q2_ub) ** iv_frac(Fraction(1, 3))) * R2_over_R1_ub
    assert disj_k1.b < 1
    disj_k2_gap = (
        c_KA**2
        - iv_frac(Fraction(2, 3))
        - iv_frac(Fraction(13, 72)) / m0_iv
        - iv_frac(Fraction(2, 3)) * (beta(2) + iv.mpf(1) / iv.mpf(12 * m0))
    )
    assert disj_k2_gap.a > 0

    # [SEAM-A]
    M_loss = iv_frac(Fraction(3, 2)) * iv_frac(Fraction(k_min, k_min - 1)) + iv_frac(Fraction(1, 3)) * (
        iv.mpf(1) + iv.mpf(1) / iv.mpf(6 * (k_min**2 - 1)) + iv.mpf(1) / iv.mpf(6 * m0 * (k_min - 1))
    )
    y_KA_ub = (
        iv.mpf(1) / iv.mpf(k_min)
        + iv.mpf(1) / iv.mpf(6 * k_min * (k_min**2 - 1))
        + iv_frac(Fraction(13, 12)) / iv.mpf(m0 * m0 * k_min * (k_min - 1))
    )
    seam_A = (
        (iv.sqrt(m0_iv) / c_KA) * M_loss / (m0_iv - M_loss)
        + iv_frac(Fraction(1, 2))
        + y_KA_ub / (iv.mpf(12) * (iv.mpf(1) - iv.mpf(1) / iv.mpf(4 * m0 * m0)))
    )
    assert seam_A.b < 1

    # Helper for Q_k bounds: ln Q_k in [beta(k) - 5/(24 M_min k(k-1)), beta(k) + 1/(6 M_min k(k-1))]
    def lnQk_iv(k: int, M_min: int) -> iv.mpf:
        if k == 1:
            # Q_1(n) = 2*(2n+3)/(n+3) in [2*(2*80+3)/83, 4)
            return iv.mpf([iv.log(iv_frac(Fraction(2 * 163, 83))).a, iv.log(iv.mpf(4)).b])
        bk = beta(k)
        lo = (bk - iv_frac(Fraction(5, 24)) / iv.mpf(M_min * k * (k - 1))).a
        hi = (bk + iv_frac(Fraction(1, 6)) / iv.mpf(M_min * k * (k - 1))).b
        return iv.mpf([lo, hi])

    gammas = [
        iv_frac(Fraction(-1, 3)),
        iv_frac(Fraction(1, 3)),
        iv.mpf([iv_frac(Fraction(2, 3)).a, iv.mpf(1).b]),
        iv.mpf([iv.mpf(1).a, iv_frac(Fraction(4, 3)).b]),
    ]

    # [A-k=1]
    worst_k1 = iv.mpf(0)
    lnQ1 = lnQk_iv(1, m0)
    sR2_ub = iv.exp(iv_frac(Fraction(4, 3)) * lnQ1.b) * R2_over_R1_ub
    assert sR2_ub.b < iv_frac(Fraction(1, 2))
    for g_iv in gammas:
        Delta0 = -g_iv * lnQ1
        main_lb = abs(iv.exp(Delta0) - iv.mpf(1)).a
        assert main_lb > 0
        e_pert = (iv.exp(Delta0.b) + iv.mpf(1)) * eps_E0
        r_tail = (sR2_ub / (iv.mpf(1) - sR2_ub)) * (iv.mpf(1) + eps_E1)
        err = (e_pert + r_tail) / iv.mpf(main_lb)
        assert err.b < 1
        if err.b > worst_k1.b:
            worst_k1 = err

    # [A-k=2]
    worst_k2 = iv.mpf(0)
    lnQ2 = lnQk_iv(2, m0)
    sR3_ub = iv.exp(iv_frac(Fraction(4, 3)) * lnQ2.b + m0_iv * (beta(3) - beta(2)) + c_const(3) - c_const(2) + iv_frac(Fraction(13, 72)) / m0_iv)
    assert sR3_ub.b < iv_frac(Fraction(1, 2))
    for g_iv in gammas:
        Delta0 = -g_iv * lnQ2
        main_lb = abs(iv.exp(Delta0) - iv.mpf(1)).a
        assert main_lb > 0
        u0_u2_ub = iv.exp(Delta0.b) * R2_over_R1_ub * (iv.mpf(1) + eps_E0)
        e_pert = (iv.exp(Delta0.b) + iv.mpf(1)) * eps_E1
        r_tail = (sR3_ub / (iv.mpf(1) - sR3_ub)) * (iv.mpf(1) + eps_E1)
        err = (e_pert + u0_u2_ub + r_tail) / iv.mpf(main_lb)
        assert err.b < 1
        if err.b > worst_k2.b:
            worst_k2 = err

    # [A-k=3..25]
    worst_k3_25 = iv.mpf(0)
    for k in range(3, 26):
        M_min = max(m0, (484 * k * k) // 100)  # ceil or exact floor(2.2^2 * k^2): 2.2^2 = 484/100
        # Wait: m >= 2.2^2 * k^2 => exact rational M_min_rat = Fraction(484 * k * k, 100)
        M_min_iv = max(m0_iv, (c_KA * iv.mpf(k)) ** 2)
        lnQk = lnQk_iv(k, int(M_min_iv.a))
        for g_iv in gammas:
            Delta0 = -g_iv * lnQk
            main_lb = abs(iv.exp(Delta0) - iv.mpf(1)).a
            assert main_lb > 0
            err_num = (iv.exp(Delta0.b) + iv.mpf(1)) * eps_E1
            # Paired terms 1 <= r <= k-2
            for r in range(1, k - 1):
                SL = sum(beta(k - i) - beta(k) for i in range(1, r + 1))
                SR = sum(beta(k) - beta(k + i) for i in range(1, r + 1))
                CL = sum(c_const(k - i) - c_const(k) for i in range(1, r + 1))
                CR = sum(c_const(k) - c_const(k + i) for i in range(1, r + 1))
                assert (M_min_iv * SR).a > 1 and (SL - SR).a > 0
                del_L_ub = sum(iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf(k * (k - 1))) for _ in range(r))
                del_R_ub = sum(iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf((k + i) * (k + i - 1))) for i in range(1, r + 1))
                A0 = -(r + 1) * g_iv * lnQk - CL + del_L_ub
                B0 = r * g_iv * lnQk - CR + del_R_ub
                # Lower bounds for |A_r - B_r|
                del_L_sum = iv.mpf(0)
                for i in range(1, r + 1):
                    # |delta_k - delta_{k-i}| <= 13/(12 M (k-i)(k-i-1))
                    ki = k - i
                    del_L_sum += iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf(ki * (ki - 1)))
                del_R_abs = iv.mpf(r) * iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf(k * (k - 1)))
                d_const = abs(iv.mpf(2 * r + 1) * g_iv * lnQk + CL - CR).b + del_L_sum.b + del_R_abs.b
                max0 = max(A0.b, B0.b)
                diff_bound = min(iv.mpf(1), iv.mpf(d_const) + M_min_iv * (SL - SR))
                pair_ub = iv.exp(max0 - M_min_iv * SR) * diff_bound + (iv.exp(A0.b - (M_min_iv * SL).a) + iv.exp(B0.b - (M_min_iv * SR).a)) * eps_E1
                err_num += pair_ub

            # Right tail r >= k-1 (starts at u_{2k-1}/u_k)
            SR_tail = sum(beta(k) - beta(k + i) for i in range(1, k))
            CR_tail = sum(c_const(k) - c_const(k + i) for i in range(1, k))
            del_R_tail = sum(iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf((k + i) * (k + i - 1))) for i in range(1, k))
            q_R = iv.exp(
                (g_iv * lnQk).b
                - M_min_iv * (beta(k) - beta(2 * k))
                + (c_const(2 * k) - c_const(k))
                + iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf(2 * k * (2 * k - 1)))
            )
            assert q_R.b < iv_frac(Fraction(1, 2))
            first_R = iv.exp(((k - 1) * g_iv * lnQk).b - M_min_iv * SR_tail - CR_tail + del_R_tail)
            err_num += (first_R / (iv.mpf(1) - q_R)) * (iv.mpf(1) + eps_E1)

            # Left term u_0 / u_k = (u_1 / u_k) * (u_0 / u_1)
            SL_1 = sum(beta(k - i) - beta(k) for i in range(1, k - 1))
            CL_1 = sum(c_const(k - i) - c_const(k) for i in range(1, k - 1))
            del_L_1 = sum(iv_frac(Fraction(13, 12)) / (M_min_iv * iv.mpf((k - i) * (k - i - 1))) for i in range(1, k - 1))
            u1_uk_ub = iv.exp((-(k - 1) * g_iv * lnQk).b - M_min_iv * SL_1 - CL_1 + del_L_1)
            u0_u1_ub = iv.exp(Delta0.b) * R2_over_R1_ub
            err_num += u1_uk_ub * u0_u1_ub * (iv.mpf(1) + eps_E0)

            err = err_num / iv.mpf(main_lb)
            assert err.b < 1, f"A-k={k} failed: {err}"
            if err.b > worst_k3_25.b:
                worst_k3_25 = err

    # [A-k>=26] uniform all the way to infinity
    k0 = 26
    k0_iv = iv.mpf(k0)
    M0_big = (c_KA * k0_iv) ** 2
    q_lo = iv.mpf(1) - iv_frac(Fraction(5, 24)) / (M0_big * iv.mpf(k0 - 1))
    q_hi = iv.mpf(1) + iv.mpf(1) / iv.mpf(6 * (k0**2 - 1)) + iv.mpf(1) / iv.mpf(6 * M0_big * (k0 - 1))

    worst_k26 = iv.mpf(0)
    for g_iv in gammas:
        if g_iv.b < 0:
            g_abs = -g_iv.b
            main_k_lb = g_abs * q_lo
            k_del_ub = g_abs * q_hi
            eD_ub = iv.exp(k_del_ub / k0_iv)
        else:
            main_k_lb = g_iv.a * q_lo * (iv.mpf(1) - g_iv.a * q_lo / (iv.mpf(2) * k0_iv))
            k_del_ub = g_iv.b * q_hi
            eD_ub = iv.mpf(1)
        assert main_k_lb.a > 0

        # Head pairs 1 <= r <= 6
        head_tot = iv.mpf(0)
        x_min = c_KA**2
        for r in range(1, 7):
            a_Rr = sum(iv.mpf(i) / (iv.mpf(1) + iv.mpf(i) / k0_iv) for i in range(1, r + 1))
            assert (x_min * a_Rr).a > 1
            diff_r = sum(iv.mpf(2 * i * i) / (((iv.mpf(1) - iv.mpf(1) / k0_iv) ** 3) * (iv.mpf(1) - iv.mpf(i * i) / iv.mpf((k0 - 1) ** 2))) for i in range(1, r + 1))
            CL_k2 = sum(
                iv.mpf(i) * (iv.mpf(1) + (iv.mpf(1) / k0_iv if i == 1 else iv.mpf(0)))
                / ((iv.mpf(1) - iv.mpf(i) / k0_iv) * ((iv.mpf(1) - iv.mpf(i) / k0_iv) ** 2 - iv.mpf(1) / k0_iv**2))
                for i in range(1, r + 1)
            )
            CR_k2 = sum(iv.mpf(i) * (iv.mpf(1) + iv.mpf(2) / k0_iv) / (iv.mpf(1) - iv.mpf(1) / k0_iv**2) for i in range(1, r + 1))
            del_L_k2 = sum(iv_frac(Fraction(13, 12)) / (x_min * k0_iv * (iv.mpf(1) - iv.mpf(i) / k0_iv) * (iv.mpf(1) - iv.mpf(i + 1) / k0_iv)) for i in range(1, r + 1))
            del_R_abs_k2 = iv.mpf(r) * iv_frac(Fraction(13, 12)) / (x_min * k0_iv * (iv.mpf(1) - iv.mpf(1) / k0_iv))
            d_c = iv.mpf(2 * r + 1) * max(abs(g_iv.a), abs(g_iv.b)) * q_hi + (CL_k2 + CR_k2) / k0_iv + (del_L_k2 + del_R_abs_k2) / (k0_iv**2)
            A0_ub = (-(r + 1) * g_iv.a if g_iv.b < 0 else iv.mpf(0)) * q_hi / k0_iv + (CL_k2 + del_L_k2 / k0_iv) / (k0_iv**2)
            B0_ub = (r * g_iv.b if g_iv.a > 0 else iv.mpf(0)) * q_hi / k0_iv + (CR_k2 + del_R_abs_k2 / k0_iv) / (k0_iv**2)
            max0_k = max(A0_ub.b, B0_ub.b)
            pair_h = iv.exp(max0_k - x_min * a_Rr) * (d_c + x_min * diff_r) + (iv.exp(A0_ub.b - (x_min * a_Rr).a) + iv.exp(B0_ub.b - (x_min * a_Rr).a)) * k_eps
            head_tot += pair_h

        # Piece 1: 7 <= r <= floor(k/2)
        cL_p1_unit = (k0_iv / iv.mpf(2) + iv.mpf(2)) / (iv.mpf(2) * (k0_iv / iv.mpf(2)) * ((k0_iv / iv.mpf(2)) ** 2 - iv.mpf(1)))
        c_pos = (
            max(abs(g_iv.a), abs(g_iv.b)) * q_hi / (iv.mpf(7) * k0_iv)
            + cL_p1_unit
            + iv_frac(Fraction(13, 12)) / (iv.mpf(2) * M0_big * (k0_iv / iv.mpf(2)) * (k0_iv / iv.mpf(2) - iv.mpf(1)))
        )
        alpha1 = (c_KA**2) / iv.mpf(3) - c_pos
        assert alpha1.a > 1
        cR_p1_unit = (iv.mpf(1) + iv.mpf(2) / k0_iv) / (iv.mpf(2) * k0_iv * (iv.mpf(1) - iv.mpf(1) / k0_iv**2))
        c_poly = (
            iv.mpf(15) * max(abs(g_iv.a), abs(g_iv.b)) * q_hi / iv.mpf(343)
            + x_min * iv_frac(Fraction(40, 49)) / (((iv.mpf(1) - iv.mpf(1) / k0_iv) ** 3) * (iv.mpf(1) - iv_frac(Fraction(13, 25)) ** 2))
            + (iv_frac(Fraction(8, 49)) * k0_iv) * (cL_p1_unit + cR_p1_unit)
            + (iv.mpf(1) / iv.mpf(49)) * iv_frac(Fraction(13, 12)) / (x_min * (k0_iv**2)) * (
                iv.mpf(1) / ((iv.mpf(1) / iv.mpf(2)) * (iv.mpf(1) / iv.mpf(2) - iv.mpf(1) / k0_iv))
                + iv.mpf(1) / (iv.mpf(1) - iv.mpf(1) / k0_iv)
            )
        )
        rho1 = (iv_frac(Fraction(8, 7)) ** 3) * iv.exp(-iv.mpf(16) * alpha1)
        assert rho1.b < iv_frac(Fraction(1, 2))
        p1 = (
            c_poly * (iv.mpf(343) * iv.exp(-iv.mpf(56) * alpha1)) / (iv.mpf(1) - rho1) * (iv.mpf(1) + eps_E1)
            + iv.mpf(2) * k_eps * iv.exp(-iv.mpf(56) * alpha1) / (iv.mpf(1) - iv.exp(-iv.mpf(16) * alpha1))
        )

        # Piece 2: far tails r >= r_h := floor(k/2) + 1
        alpha2 = (c_KA**2) * iv_frac(Fraction(k0 * k0 - 1, k0 * k0)) / (iv.mpf(8) * (iv_frac(Fraction(3, 2)) + iv.mpf(1) / k0_iv))
        assert (iv.mpf(2) * alpha2 * (k0_iv**2)).a > 1
        nonM_tail_ub = (
            max(abs(g_iv.a), abs(g_iv.b)) * q_hi * (iv_frac(Fraction(1, 2)) + iv.mpf(1) / k0_iv)
            + iv_frac(Fraction(1, 2)) * (iv_frac(Fraction(1, 2)) + iv.mpf(1) / k0_iv) * (iv_frac(Fraction(1, 2)) + iv.mpf(2) / k0_iv) * (iv.mpf(1) + iv.mpf(2) / k0_iv) / (iv.mpf(1) - iv.mpf(1) / k0_iv**2)
            + (iv_frac(Fraction(1, 2)) + iv.mpf(1) / k0_iv) * iv_frac(Fraction(13, 12)) / (M0_big * k0_iv)
        )
        # Left tail: C_L < 0 so -C_L(r_h) > 0, bounded by (3/2)*(1/2 + 1/k0)/(1/2 - 2/k0)
        neg_CL_ub = iv_frac(Fraction(3, 2)) * (iv_frac(Fraction(1, 2)) + iv.mpf(1) / k0_iv) / (iv_frac(Fraction(1, 2)) - iv.mpf(2) / k0_iv)
        nonM_left_ub = (
            max(abs(g_iv.a), abs(g_iv.b)) * q_hi * (iv_frac(Fraction(1, 2)) + iv.mpf(2) / k0_iv)
            + neg_CL_ub
            + (iv_frac(Fraction(1, 2)) + iv.mpf(1) / k0_iv) * iv_frac(Fraction(13, 12)) / (M0_big * (k0_iv / iv.mpf(2) - iv.mpf(1)))
        )
        rho2 = iv_frac(Fraction(3, 2)) * iv.exp(q_hi / k0_iv - (c_KA**2) * k0_iv / iv.mpf(3) + iv.mpf(1))
        assert rho2.b < iv_frac(Fraction(1, 2))
        p2 = (
            k0_iv
            * (iv.exp(-alpha2 * (k0_iv**2) + nonM_tail_ub) + iv.exp(-alpha2 * (k0_iv**2) + nonM_left_ub))
            / (iv.mpf(1) - rho2)
            * (iv.mpf(1) + eps_E0)
        )

        e_pert = (eD_ub + iv.mpf(1)) * k_eps
        err = (head_tot + p1 + p2 + e_pert) / main_k_lb
        assert err.b < 1
        if err.b > worst_k26.b:
            worst_k26 = err

    return {
        "s_max_m0": s_max_m0,
        "eps_E0": eps_E0,
        "disj_k1": disj_k1,
        "disj_k2_gap": disj_k2_gap,
        "seam_A": seam_A,
        "A_k1": worst_k1,
        "A_k2": worst_k2,
        "A_k3_25": worst_k3_25,
        "A_k26": worst_k26,
    }


def main() -> None:
    print("[1/4] Checking Lemma 1.1 rational GF against Smirnov DP (n=1..15) and Table 1...")
    for n in range(1, 16):
        c_dp = smirnov_dp_chow(n)
        c_gf = gf_chow(n)
        assert c_dp == c_gf, f"DP vs GF mismatch at n={n}"
        assert sum(c_gf) == n ** (n - 1)
        if n in TAB_CHOW_TRIANGLE:
            assert c_gf == TAB_CHOW_TRIANGLE[n]
    print("      Exact match across n=1..15 and all 9 rows of Table 1.")

    print("[2/4] Verifying Gamma_n and Sturm-Cauchy Cauchy index I_{-inf}^0(Gamma_n/Gamma_{n+1}) = d_{n+1} for 1 <= n <= 80...")
    gammas = {}
    for n in range(1, 82):
        C = gf_chow(n)
        gammas[n] = extract_gamma(C, n)
    for n in range(1, 81):
        d_n1 = n // 2
        idx = cauchy_index_neg_inf_to_0(gammas[n], gammas[n + 1])
        assert idx == d_n1, f"Sturm-Cauchy mismatch at n={n}: {idx} != {d_n1}"
    print("      All 80 consecutive pairs n=1..80 passed exact integer Sturm-Cauchy.")

    print("[3/4] Checking analytic identities (3.2)-(3.7) & Regime B + Seam-B bounds (40-digit iv)...")
    verify_analytic_identities()
    res_B = verify_regime_B_and_seam_B()
    print(
        f"      Seam-B margin >= {iv.nstr(res_B['seam_B'].a, 7)}; "
        f"B3 <= {iv.nstr(res_B['B3'].b, 4)}; B4 <= {iv.nstr(res_B['B4'].b, 4)}; B5 <= {iv.nstr(res_B['B5'].b, 6)}"
    )

    print("[4/4] Checking Lemma 5.1, Seam-A, and Regime A bounds (all k >= 1 to inf, 40-digit iv)...")
    res_A = verify_lemma_51_and_regime_A()
    print(
        f"      Seam-A <= {iv.nstr(res_A['seam_A'].b, 6)}; A(k=1) <= {iv.nstr(res_A['A_k1'].b, 4)}; "
        f"A(k=2) <= {iv.nstr(res_A['A_k2'].b, 4)}; A(3..25) <= {iv.nstr(res_A['A_k3_25'].b, 6)}; "
        f"A(>=26) <= {iv.nstr(res_A['A_k26'].b, 6)}"
    )
    print("PASS")


if __name__ == "__main__":
    main()

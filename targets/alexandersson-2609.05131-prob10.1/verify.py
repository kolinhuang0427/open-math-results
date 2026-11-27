#!/usr/bin/env python3
"""
Standalone zero-float verification of Alexandersson (2026), arXiv:2609.05131v2,
Section 10, Problem 10.1 (prob:consecutiveChowInterlacing):

    For every n >= 1 (and trivially n = 0), H_{NC_{n+1}}(t) << H_{NC_{n+2}}(t).

Zero Python floats are used anywhere in this script:
  - Part 0 & Part 1 use pure exact Python integers (exact Smirnov DP cross-check,
    exact O(n^3) generating-function computation, exact gamma-polynomial expansion,
    and exact primitive integer Sturm-Cauchy index for all 1 <= n <= 80).
  - Part 2 uses 35-digit mpmath interval arithmetic (mpmath.iv) with exact rational
    inputs and rigorous outward-rounded .a / .b endpoints to certify every analytic
    inequality for ALL n >= 80 simultaneously.
"""

from math import comb, gcd
from mpmath import iv, mp, nstr

mp.dps = 35
iv.dps = 35
PI = iv.pi
E_CONST = iv.exp(iv.mpf(1))


def rat(p, q=1):
    """Exact interval enclosure of rational p/q (zero floats)."""
    return iv.mpf(p) / iv.mpf(q)


def iv_sinh(x):
    return (iv.exp(x) - iv.exp(-x)) / 2


def iv_atan(x):
    return iv.atan2(x, iv.mpf(1))


def fmt(x, digits=6):
    # x is a point iv.mpf (z.a or z.b); format its exact mpmath endpoint without Python float
    return nstr(mp.mpf(x._mpi_[1]), digits)


# =============================================================================
# PART 0 & PART 1: EXACT INTEGER VERIFICATION FOR 1 <= n <= n0 = 80
# =============================================================================

def smirnov_Cn_dp(n):
    """
    Direct Smirnov last-letter recurrence (Alexandersson Prop. 4.1, eq. (6)):
        F^{(m)}_{1, j}(t) = 1,
        F^{(m)}_{r+1, j}(t) = t * sum_{k < j} F^{(m)}_{r, k}(t)
                            +     sum_{k > j} F^{(m)}_{r, k}(t),
        C_n(t) = (1 / (n + 1)) * sum_{j = 1}^{n + 1} F^{(n + 1)}_{n, j}(t).
    Returns exact integer coefficient list [c_0, c_1, ..., c_{n-1}].
    """
    m = n + 1
    F = [[1] for _ in range(m)]
    for r in range(1, n):
        deg = r  # max degree of next row
        pref = [[0] * (deg + 1) for _ in range(m + 1)]
        for j in range(m):
            row = F[j]
            prev = pref[j]
            cur = pref[j + 1]
            for d, val in enumerate(row):
                cur[d] = prev[d] + val
            for d in range(len(row), deg + 1):
                cur[d] = prev[d]
        tot = pref[m]
        nxt = []
        for j in range(m):
            # sum_{k < j} is pref[j]; sum_{k > j} is tot - pref[j+1]
            p_lt = pref[j]
            p_le = pref[j + 1]
            poly = [0] * (deg + 1)
            for d in range(deg):
                poly[d] += tot[d] - p_le[d]
                poly[d + 1] += p_lt[d]
            nxt.append(poly)
        F = nxt
    C = [0] * n
    for j in range(m):
        for d, val in enumerate(F[j]):
            C[d] += val
    for d in range(n):
        assert C[d] % m == 0, f"Divisibility failed at n={n}, d={d}"
        C[d] //= m
    return C


def fast_Cn(n):
    """
    Exact O(n^3) integer computation of C_n(t) from the proved generating function:
        C_n(t) = (1/m) [z^n] (1+z)^m / (1 - sum_{k=2}^m comb(m,k)(t + ... + t^{k-1}) z^k),
    where m = n + 1, using prefix sums for multiplication by (t + ... + t^{k-1}).
    Returns exact integer coefficient list [c_0, c_1, ..., c_{n-1}].
    """
    m = n + 1
    if n == 1:
        return [1]
    binoms = [comb(m, k) for k in range(m + 1)]
    # P[r] = [z^r] 1 / (1 - sum_{k=2}^m comb(m,k)(t+...+t^{k-1}) z^k), deg <= r - 1 for r >= 2
    P = [[1]]  # P[0] = 1
    # S[r][a] = sum_{i=0}^a P[r][i] for 0 <= a <= max_deg
    S = [[1]]
    for r in range(1, n + 1):
        # max degree of P[r] is at most r - 1 (for r >= 2), 0 for r = 1
        if r == 1:
            P.append([0])
            S.append([0])
            continue
        cur = [0] * r  # degrees 0 .. r - 1
        for k in range(2, r + 1):
            b = binoms[k]
            s_prev = S[r - k]
            L = len(s_prev)
            # Add b * (t + t^2 + ... + t^{k-1}) * P[r-k](t):
            # coeff of t^a is b * (S[a-1] - S[a-k]) with S[idx]=0 for idx<0, S[idx]=S[L-1] for idx>=L
            top = s_prev[L - 1]
            hi = min(r - 1, (L - 1) + (k - 1))
            for a in range(1, hi + 1):
                u = s_prev[a - 1] if (a - 1) < L else top
                v = s_prev[a - k] if (a - k) >= 0 else 0
                cur[a] += b * (u - v)
        P.append(cur)
        # Build prefix sum S[r]
        sr = [0] * r
        acc = 0
        for a in range(r):
            acc += cur[a]
            sr[a] = acc
        S.append(sr)

    # C_n(t) = (1/m) * sum_{r=0}^n comb(m, n - r) * P[r](t)
    C = [0] * n
    for r in range(n + 1):
        b = binoms[n - r]
        pr = P[r]
        for a, val in enumerate(pr):
            C[a] += b * val
    for a in range(n):
        assert C[a] % m == 0, f"fast_Cn divisibility failed at n={n}, a={a}"
        C[a] //= m
    return C


def to_gamma(C):
    """
    Given palindromic C(t) of degree d = len(C) - 1, compute exact integer
    gamma-polynomial Gamma(u) = sum_{j=0}^{floor(d/2)} gamma_j u^j satisfying
        C(t) = sum_{j=0}^{floor(d/2)} gamma_j t^j (1 + t)^{d - 2j}.
    Asserts exact zero remainder (certifying palindromicity and exactness).
    """
    d = len(C) - 1
    rem = list(C)
    h = d // 2
    gam = []
    for j in range(h + 1):
        g = rem[j]
        gam.append(g)
        deg_factor = d - 2 * j
        for i in range(deg_factor + 1):
            rem[j + i] -= g * comb(deg_factor, i)
    assert all(x == 0 for x in rem), f"Non-zero remainder in gamma expansion: {rem}"
    return gam


def poly_trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_content(p):
    g = 0
    for c in p:
        g = gcd(g, abs(c))
    return g if g > 0 else 1


def poly_pos_pseudo_rem(A, B):
    """
    Exact primitive integer pseudo-remainder R satisfying
        c * A(u) = Q(u) * B(u) + R(u)
    with STRICTLY POSITIVE integer constant c > 0.
    """
    R = poly_trim(A)
    B = poly_trim(B)
    dB = len(B) - 1
    b = B[-1]
    assert b != 0
    abs_b = abs(b)
    sgn_b = 1 if b > 0 else -1
    while len(R) - 1 >= dB and not (len(R) == 1 and R[0] == 0):
        dR = len(R) - 1
        shift = dR - dB
        lead = R[-1]
        # R <- |b| * R - (sgn(b) * lead) * u^shift * B  (multiplier |b| > 0)
        mult = sgn_b * lead
        newR = [abs_b * c for c in R]
        for i, cb in enumerate(B):
            newR[i + shift] -= mult * cb
        R = poly_trim(newR)
        g = poly_content(R)
        if g > 1:
            R = [c // g for c in R]
    return R


def sign_changes(seq):
    nz = [1 if x > 0 else -1 for x in seq if x != 0]
    return sum(1 for i in range(len(nz) - 1) if nz[i] != nz[i + 1])


def verify_gamma_strict_interlacing(gam_n, gam_np1):
    """
    Exact Sturm-Cauchy proof that Gamma_n and Gamma_{n+1} have all simple strictly
    negative roots and strictly interlace with v_1 > u_1 > ... :
        I_{-inf}^0(Gamma_n / Gamma_{n+1}) == deg(Gamma_{n+1}),
    together with Gamma_n(0) > 0, Gamma_{n+1}(0) > 0, lc(Gamma_n) > 0, lc(Gamma_{n+1}) > 0,
    and deg(Gamma_{n+1}) in {deg(Gamma_n), deg(Gamma_n) + 1}.
    """
    f = poly_trim(gam_n)
    g = poly_trim(gam_np1)
    df, dg = len(f) - 1, len(g) - 1
    assert dg in (df, df + 1), f"Bad gamma degrees: {df}, {dg}"
    assert f[0] > 0 and g[0] > 0 and f[-1] > 0 and g[-1] > 0
    if dg == 0:
        return True
    # Signed remainder sequence p_0 = g, p_1 = f, c_i p_{i-1} = q_i p_i - p_{i+1} (c_i > 0)
    seq = [g, f]
    while len(seq[-1]) > 1:
        r = poly_pos_pseudo_rem(seq[-2], seq[-1])
        if len(r) == 1 and r[0] == 0:
            raise AssertionError("Non-trivial gcd between Gamma_n and Gamma_{n+1}!")
        neg_r = [-c for c in r]
        g_cont = poly_content(neg_r)
        if g_cont > 1:
            neg_r = [c // g_cont for c in neg_r]
        seq.append(neg_r)
    assert len(seq[-1]) == 1 and seq[-1][0] != 0
    # Signs at -inf: (-1)^{deg(p)} * lc(p); signs at 0: p[0]
    signs_minf = [((-1) ** (len(p) - 1)) * p[-1] for p in seq]
    signs_zero = [p[0] for p in seq]
    cauchy_idx = sign_changes(signs_minf) - sign_changes(signs_zero)
    assert cauchy_idx == dg, f"Cauchy index {cauchy_idx} != deg(Gamma_{{n+1}}) = {dg}"
    return True


def run_part1(n0=80):
    print(f"[Part 0] Cross-checking fast_Cn against direct Smirnov DP (eq:lastLetterRecurrence) for 1 <= n <= 15...")
    for n in range(1, 16):
        c_dp = smirnov_Cn_dp(n)
        c_fast = fast_Cn(n)
        assert c_dp == c_fast, f"Mismatch at n={n}: DP={c_dp} vs fast={c_fast}"
        assert sum(c_fast) == n ** (n - 1), f"Row sum mismatch at n={n}"
    print(f"  Exact match for all 1 <= n <= 15 (and row sums C_n(1) = n^(n-1)).")

    print(f"[Part 1] Computing C_1..C_{n0 + 1} and verifying strict interlacing Gamma_n << Gamma_{{n+1}} for 1 <= n <= {n0}...")
    gammas = {}
    for n in range(1, n0 + 2):
        Cn = fast_Cn(n)
        assert len(Cn) == n and Cn[0] == 1 and Cn[-1] == 1
        assert all(c > 0 for c in Cn)
        gam = to_gamma(Cn)
        assert len(gam) == (n - 1) // 2 + 1
        assert gam[0] == 1 and gam[-1] > 0
        gammas[n] = gam

    for n in range(1, n0 + 1):
        verify_gamma_strict_interlacing(gammas[n], gammas[n + 1])
    print(f"  Exact integer Sturm-Cauchy PASSED for ALL 1 <= n <= {n0} (C_1..C_{n0 + 1} simple, palindromic, strictly interlacing).")


# =============================================================================
# PART 2: ZERO-FLOAT 35-DIGIT INTERVAL CERTIFICATION FOR ALL n >= n0 = 80
# =============================================================================

def beta_iv(j):
    """Exact beta_j = (j+1)ln(j+1) - 2j ln(j) + (j-1)ln(j-1) for integer j >= 2."""
    jp, j0, jm = iv.mpf(j + 1), iv.mpf(j), iv.mpf(j - 1)
    return jp * iv.log(jp) - 2 * j0 * iv.log(j0) + jm * iv.log(jm)


def c_iv(j):
    """Exact c_j = -(3/2)ln(j/(j-1)) + (1/2)ln((j+1)/j) for integer j >= 2."""
    jp, j0, jm = iv.mpf(j + 1), iv.mpf(j), iv.mpf(j - 1)
    return -rat(3, 2) * iv.log(j0 / jm) + rat(1, 2) * iv.log(jp / j0)


def run_part2(n0=80, c_KA=rat(22, 10), Y_max=rat(23, 10)):
    m0 = n0 + 1  # 81, sqrt(m0) = 9 exact
    sm0 = iv.sqrt(iv.mpf(m0))
    th0 = PI / m0
    print(f"[Part 2] 35-digit mpmath.iv certification for ALL n >= {n0} (m0={m0}, c_KA={fmt(c_KA.b, 4)}, Y_max={fmt(Y_max.b, 4)})...")

    # -------------------------------------------------------------------------
    # 2.1 SEAM-B: Y(a_{KA+1}) < Y_max for ALL m >= m0
    # -------------------------------------------------------------------------
    # KA = floor(sqrt(m)/c_KA) > sqrt(m)/c_KA - 1, delta_{KA+1} < pi/8 =>
    #   Phi_n(a_{KA+1}) / pi > sqrt(m)/c_KA + 3/8.
    # Meanwhile Phi_n(s)/pi < sqrt(m)/Y + 1/2 + Y / (12*sqrt(m)*(1 - 1/(4*m^2))).
    # So Y(a_{KA+1}) < Y_max whenever LHS > RHS at m = m0 (LHS increasing, RHS decreasing in m):
    lhs_seamB = sm0 * (rat(1) / c_KA - rat(1) / Y_max)
    rhs_seamB = rat(1, 8) + Y_max / (12 * sm0 * (1 - rat(1, 4 * m0 * m0)))
    assert lhs_seamB.a > rhs_seamB.b, f"SEAM-B failed: {lhs_seamB} vs {rhs_seamB}"
    print(f"  [SEAM-B]    Y(a_{{KA+1}}) < {fmt(Y_max.b, 4)} CERTIFIED (margin >= {fmt((lhs_seamB - rhs_seamB).a, 6)})")

    # -------------------------------------------------------------------------
    # 2.2 REGIME B PHASE SHIFT & DERIVATIVE BOUNDS (0 < Y <= Y_max, all m >= m0)
    # -------------------------------------------------------------------------
    # Check lambda^2 + 1 <= 4*m^2 on all of Regime B (guarantees g_p'(u) < 0 and dE_A/dlam > 0):
    lam_sq_check = Y_max ** 2 / (PI ** 2) + rat(1, m0)
    assert lam_sq_check.b < 4 * m0

    # Relative phase-shift bounds on Delta_Phi(s) = Phi_{n+1}(s) - Phi_n(s):
    # u(s) = atan(pi / (Y*sqrt(m))) >= atan_fac * pi / (Y*sqrt(m)) where atan_fac = atan(x0)/x0 at x0 = pi/(Y_max*sqrt(m0))
    # Wait: atan(x)/x is decreasing on x > 0, and x = pi/(Y*sqrt(m)) can be large for small Y,
    # HOWEVER we only need err_lo(m)/u(s) and err_hi(m)/u(s) maximized at Y = Y_max (smallest u(s)!)
    # At Y = Y_max: x = pi / (Y_max * sqrt(m)) <= pi / (Y_max * sqrt(m0)) = x0, so u(s) >= (atan(x0)/x0) * pi / (Y_max * sqrt(m))!
    x0_Ymax = PI / (Y_max * sm0)
    atan_fac0 = iv_atan(x0_Ymax) / x0_Ymax
    assert atan_fac0.a > 0

    # Exact bounds on err_lo(m)/u(s) and err_hi(m)/u(s) (strictly decreasing in m >= m0, evaluated at m0):
    # err_lo(m) = pi*Y_max*(1 + 1/(4m^2)) / (12*m^{3/2}*(1 - 1/(4m^2))^2) + pi^3 / (24*m^2*cos(th0))
    # err_hi(m) = pi/(m*(m+1)) + pi/(e*(m-1)*(m+1)) + pi^3 / (24*m^2*cos(th0))
    cos_th0 = iv.cos(th0)
    assert cos_th0.a > 0
    err_lo_m0 = (
        PI * Y_max * (1 + rat(1, 4 * m0 * m0)) / (12 * m0 * sm0 * (1 - rat(1, 4 * m0 * m0)) ** 2)
        + PI ** 3 / (24 * m0 * m0 * cos_th0)
    )
    err_hi_m0 = (
        PI / (m0 * (m0 + 1))
        + PI / (E_CONST * (m0 - 1) * (m0 + 1))
        + PI ** 3 / (24 * m0 * m0 * cos_th0)
    )
    u_lb_Ymax_m0 = atan_fac0 * PI / (Y_max * sm0)
    rel_dPhi_lo = err_lo_m0 / u_lb_Ymax_m0
    rel_dPhi_hi = err_hi_m0 / u_lb_Ymax_m0

    # Derivative lower bound dPhi_n/du >= m0 - dEA_ub - dBn_ub > 0:
    dEA_ub = (Y_max ** 2 + PI ** 2 / m0) / (12 * (1 - rat(1, 4 * m0 * m0)) ** 2)
    assert (PI * (1 - rat(1, m0))).a > 1  # ensures (1+lam^2)*exp(-a*lam) <= 1 for all lam >= 0
    dBn_ub = PI ** 2
    D_Phi = m0 - dEA_ub - dBn_ub
    assert D_Phi.a > 10
    rho_u = rat(1, 4) / D_Phi
    assert rho_u.b < rat(1, 10)

    c_min_n = rat(1, 4) / (1 + rho_u)
    c_max_n = rat(1, 4) / (1 - rho_u)
    c_min_np1 = (1 - rel_dPhi_lo) - rat(1, 4) / (1 - rho_u)
    c_max_np1 = (1 + rel_dPhi_hi) + rat(1, 4) / (1 - rho_u)
    assert c_min_n.a > 0 and c_min_np1.a > 0
    assert (c_max_n * PI / 2).b < PI / 2
    assert (c_max_np1 * PI / 2).b < PI  # strictly inside (0, pi) so sin(phi) > 0 everywhere!

    # sin(phi) >= c_min * s_fac * u for all phi in [c_min*u, c_max*u] and u in (0, pi/2]:
    s_fac_n = iv.sin(c_max_n * PI / 2) / (c_max_n * PI / 2)
    s_fac_np1 = iv.sin(c_max_np1 * PI / 2) / (c_max_np1 * PI / 2)
    assert s_fac_n.a > 0 and s_fac_np1.a > 0

    # Magnitude numerator constants nu_k for k=2, k=3, and k>=4:
    y_max = Y_max / sm0
    sh_fac = iv_sinh(y_max / 2) / (y_max / 2)
    c3 = (1 - th0 ** 2 / 6) ** 2 * (1 - th0 ** 2 / 2)
    c5 = (1 - (5 * th0 / 2) ** 2 / 6) ** 2
    assert c3.a > 0 and c5.a > 0
    nu_2 = 2 * PI ** 2 * c3
    nu_3 = ((25 * c5 - 1) / 4) * PI ** 2

    # -------------------------------------------------------------------------
    # 2.3 REGIME B SUB-REGION (B3): lambda < 1 (for BOTH C_n and C_{n+1})
    # -------------------------------------------------------------------------
    # Use trivial |cos Phi_{N, k}| <= 1 and |cos Phi_N(s)| >= c_min * s_fac * (pi/4)
    # since u(s) = atan(1/lambda) > pi/4 on lambda < 1.
    denom_B3 = (sh_fac ** 2 + 1) * PI ** 2
    tk2_B3 = (1 + 4 * nu_2 / denom_B3) ** (-rat(m0, 2))
    tk3_B3 = (1 + 4 * nu_3 / denom_B3) ** (-rat(m0, 2))
    c_t4 = 1 - PI ** 2 / (4 * 49)
    B_t4_B3 = 4 * c_t4 * 49 / denom_B3
    p_t4_B3 = m0 * B_t4_B3 / (1 + B_t4_B3)
    assert p_t4_B3.a > 5
    mult_B3 = 1 + rat(7, 2) / (p_t4_B3 - 1)
    sum_tk_B3 = tk2_B3 + tk3_B3 + mult_B3 * (1 + B_t4_B3) ** (-rat(m0, 2))
    err_B3_Cn = sum_tk_B3 / (c_min_n * s_fac_n * PI / 4)
    err_B3_Cnp1 = sum_tk_B3 / (c_min_np1 * s_fac_np1 * PI / 4)
    assert err_B3_Cn.b < rat(1, 100) and err_B3_Cnp1.b < rat(1, 100)

    # -------------------------------------------------------------------------
    # 2.4 REGIME B SUB-REGION (B4): lambda >= 1 and Y <= 1/2 (Z = 1/Y^2 >= 4)
    # -------------------------------------------------------------------------
    # Here u(s) >= (pi/4) / lambda = pi^2 / (4*Y*sqrt(m)), so a_f = pi/4.
    # Also |T_k|/|T_1| <= (1 + C_k * Z / m)^(-m/2) where C_k = 4*nu_k / (sh_fac^2 + 1).
    err_B4_Cn = rat(0)
    err_B4_Cnp1 = rat(0)
    for k, nk in [(2, nu_2), (3, nu_3), (4, iv.mpf(49) - PI ** 2 / 4)]:
        r = 2 * k - 1
        Ck = 4 * nk / (sh_fac ** 2 + 1)
        # Verify Z * (1 + Ck*Z/m)^(-m/2) is strictly decreasing for Z >= 4 and all m >= m0:
        assert (m0 / (Ck * (rat(m0, 2) - 1))).b < 4
        tk_ub = (1 + 4 * Ck / m0) ** (-rat(m0, 2))
        # Exact eta_k / u at Z = 4, Y <= 1/2, m >= m0, a_f = pi/4:
        # At tail anchor k == 4 (r_0 = 7), use r_0^3 so (r/r_0)^3 * r_0^3 = r^3 > r^3 - r dominates all r >= 7!
        r3_b4 = r ** 3 if k == 4 else r ** 3 - r
        piece1 = (iv.mpf(r3_b4) / 3) * (4 * PI * 4)
        piece2 = (4 / PI) * (
            PI ** 2 * r3_b4 * rat(1, 4) / (540 * m0 * m0 * (1 - rat(1, 4 * m0 * m0)))
            + 8 * PI ** 2 * (r ** 3) * rat(1, 16) / (76545 * (m0 ** 3))
        )
        piece3 = 4 * r * iv.exp(-PI * (1 - rat(1, m0)))
        eta_u = piece1 + piece2 + piece3
        if k == 4:
            # Tail k >= 4 (r >= 7): 1 + B*x^2 >= (1+B)*x^{2B/(1+B)} with x = r/7, B = 4*C_4/m >= ...
            # Wait: p_4(m) = 4*C_4 / (1 + 4*C_4/m) is INCREASING in m >= m0, so min at m = m0!
            B4 = 4 * Ck / m0
            p4 = m0 * B4 / (1 + B4)
            assert p4.a > 10
            m_k = 1 + rat(7, 2) / (p4 - 4)
        else:
            m_k = rat(1)
        err_B4_Cn += m_k * tk_ub * (r * c_max_n + eta_u) / (c_min_n * s_fac_n)
        err_B4_Cnp1 += m_k * tk_ub * (r * c_max_np1 + eta_u) / (c_min_np1 * s_fac_np1)
    assert err_B4_Cn.b < rat(1, 100) and err_B4_Cnp1.b < rat(1, 100)

    # -------------------------------------------------------------------------
    # 2.5 REGIME B SUB-REGION (B5): 1/2 <= Y <= Y_max (partitioned into 18 bins)
    # -------------------------------------------------------------------------
    # Tail k >= 10 (r >= 19) exponent p_tail(m) = A / (sh_fac^2*Y_max^2 + (pi^2+A)/m) is
    # strictly INCREASING in m >= m0 and DECREASING in Y <= Y_max, so min at (m0, Y_max):
    c_tail = 1 - PI ** 2 / (4 * 19 ** 2)
    denom_tail_max = m0 * (sh_fac ** 2) * (Y_max ** 2) + PI ** 2
    B_tail = 4 * c_tail * (19 ** 2) / denom_tail_max
    p_tail = m0 * B_tail / (1 + B_tail)
    assert p_tail.a > 10
    tail_mult_B5 = 1 + rat(19, 2) / (p_tail - 4)

    worst_B5_Cn = rat(0)
    worst_B5_Cnp1 = rat(0)
    # Bins [5/10, 6/10], ..., [22/10, 23/10]
    for idx in range(5, 23):
        Ya = rat(idx, 10)
        Yb = rat(idx + 1, 10)
        x_hi = PI / (Ya * sm0)
        af = iv_atan(x_hi) / x_hi  # exact lower bound on atan(x)/x for all 0 < x <= x_hi
        # Check x = Y*sqrt(m) >= Ya*sqrt(m0) > 1/(1 - 1/m0) so x*exp(-(1-1/m)*x) is decreasing in Y and m:
        assert (Ya * sm0 * (1 - rat(1, m0))).a > 1
        B_fac_base = (Ya * sm0 / af) * iv.exp(-Ya * sm0 * (1 - rat(1, m0)))
        tot_Cn = rat(0)
        tot_Cnp1 = rat(0)
        for k in range(2, 11):
            r = 2 * k - 1
            if k == 2:
                nk = nu_2
            elif k == 3:
                nk = nu_3
            else:
                nk = iv.mpf(r * r) - PI ** 2 / 4
            tk_ub = (1 + 4 * nk / (m0 * (sh_fac ** 2) * (Yb ** 2) + PI ** 2)) ** (-rat(m0, 2))
            # At tail anchor k == 10 (r_0 = 19), use r_0^3 so (r/r_0)^3 * r_0^3 = r^3 > r^3 - r dominates all r >= 19!
            r3_b5 = r ** 3 if k == 10 else r ** 3 - r
            p1 = (iv.mpf(r3_b5) / 3) * (PI ** 2 / (Ya ** 2)) / af
            p2 = (
                PI ** 2 * r3_b5 * (Yb ** 2) / (540 * m0 * m0 * (1 - rat(1, 4 * m0 * m0)))
                + 8 * PI ** 2 * (r ** 3) * (Yb ** 4) / (76545 * (m0 ** 3))
            ) / af
            p3 = r * B_fac_base
            eta_u = p1 + p2 + p3
            mult = tail_mult_B5 if k == 10 else rat(1)
            tot_Cn += mult * tk_ub * (r * c_max_n + eta_u) / (c_min_n * s_fac_n)
            tot_Cnp1 += mult * tk_ub * (r * c_max_np1 + eta_u) / (c_min_np1 * s_fac_np1)
        if tot_Cn.b > worst_B5_Cn.b:
            worst_B5_Cn = tot_Cn
        if tot_Cnp1.b > worst_B5_Cnp1.b:
            worst_B5_Cnp1 = tot_Cnp1

    assert worst_B5_Cn.b < 1 and worst_B5_Cnp1.b < 1
    print(f"  [REGIME B]  (B3 lam<1):   Cn <= {fmt(err_B3_Cn.b, 4)}, Cnp1 <= {fmt(err_B3_Cnp1.b, 4)} (< 1)")
    print(f"  [REGIME B]  (B4 mid):     Cn <= {fmt(err_B4_Cn.b, 4)}, Cnp1 <= {fmt(err_B4_Cnp1.b, 4)} (< 1)")
    print(f"  [REGIME B]  (B5 main):    Cn <= {fmt(worst_B5_Cn.b, 5)}, Cnp1 <= {fmt(worst_B5_Cnp1.b, 5)} (< 1)")
    print(f"              (p_tail >= {fmt(p_tail.a, 5)}, k>=10 mult <= {fmt(tail_mult_B5.b, 5)})")

    # -------------------------------------------------------------------------
    # 2.6 REGIME A GLOBAL s_max, SEAM-A, AND DISJOINTNESS
    # -------------------------------------------------------------------------
    # Minimum KA at m = m0 = 81: floor(9 / (22/10)) = floor(90/22) = 4
    k_min_KA = 4
    assert iv.mpf(k_min_KA) <= sm0 / c_KA and sm0 / c_KA < iv.mpf(k_min_KA + 1)

    s_exp_loss = (
        rat(3, 2 * (k_min_KA - 1))
        + rat(1, 3) * (
            rat(1, k_min_KA)
            + rat(1, 6 * k_min_KA * (k_min_KA ** 2 - 1))
            + rat(1, 6 * m0 * k_min_KA * (k_min_KA - 1))
        )
    )
    s_max_A = iv.exp(-(c_KA * sm0 - s_exp_loss))
    # Monotonicity of (m+1)(m+2)*s_max(m) and sqrt(m)*(m+1)*s_max(m) for m >= m0:
    # Since sqrt(m) >= 9 > 4/c_KA, strictly decreasing in m >= m0!
    assert sm0.a > (4 / c_KA).b
    arg_E0 = rat((m0 + 1) * (m0 + 2), 2) * s_max_A
    arg_E1 = 2 * (m0 + 1) * s_max_A
    eps_E0 = iv.exp(arg_E0) - 1
    eps_E1 = iv.exp(arg_E1) - 1
    # Rigorous uniform upper bound on k * eps_E1(m) <= (sqrt(m)/c_KA) * arg_E1(m) * exp(arg_E1(m0)):
    k_eps_E1 = (sm0 / c_KA) * arg_E1 * iv.exp(arg_E1)
    assert eps_E0.b < rat(1, 100) and k_eps_E1.b < rat(1, 100)
    print(f"  [REGIME A0] s_max <= {fmt(s_max_A.b, 4)}, eps_E0 <= {fmt(eps_E0.b, 4)}, k*eps_E1 <= {fmt(k_eps_E1.b, 4)}")

    # SEAM-A: Phi_n(b_{KA}) / pi - KA < 1
    M_loss_seam = (
        rat(3, 2) * rat(k_min_KA, k_min_KA - 1)
        + rat(1, 3) * (
            1
            + rat(1, 6 * (k_min_KA ** 2 - 1))
            + rat(1, 6 * m0 * (k_min_KA - 1))
        )
    )
    assert M_loss_seam.b < m0
    y_KA_ub = (
        rat(1, k_min_KA)
        + rat(1, 6 * k_min_KA * (k_min_KA ** 2 - 1))
        + rat(13, 12 * m0 * m0 * k_min_KA * (k_min_KA - 1))
    )
    seamA_excess = (
        (sm0 / c_KA) * M_loss_seam / (m0 - M_loss_seam)
        + rat(1, 2)
        + y_KA_ub / (12 * (1 - rat(1, 4 * m0 * m0)))
    )
    assert seamA_excess.b < 1
    print(f"  [SEAM-A]    Phi_n(b_{{KA}})/pi - KA <= {fmt(seamA_excess.b, 5)} < 1 CERTIFIED")

    # DISJOINTNESS in Regime A: s_k^+ < s_{k+1}^- for ALL 1 <= k < KA
    # Shared upper bound on R_2(N)/R_1(N) for all N >= n0 (M = N+1 >= m0):
    R2_over_R1_ub = (
        iv.mpf((m0 + 1) * (2 * m0 + 1))
        * iv.exp(c_iv(2) + rat(13, 24 * m0))
        * (rat(27, 64) ** m0)
    )
    # Check monotonicity of (M+1)(2M+1)*(27/64)^M for M >= m0:
    assert (rat((m0 + 2) * (2 * m0 + 3), (m0 + 1) * (2 * m0 + 1)) * rat(27, 64)).b < 1
    Q1_lo = rat(2 * (2 * n0 + 3), n0 + 3)
    Q1_hi = rat(4)
    Q2_lo = iv.exp(beta_iv(2) - rat(5, 48 * m0))
    Q2_hi = iv.exp(beta_iv(2) + rat(1, 12 * m0))
    # k = 1 disjointness: s_1^+ / s_2^- = (Q_1 * Q_2)^{1/3} * R_2(n)/R_1(n) < 1
    disj_k1 = (Q1_hi * Q2_hi) ** rat(1, 3) * R2_over_R1_ub
    assert disj_k1.b < 1
    # k >= 2 disjointness: ln(R_k/R_{k+1}) > c_KA^2 - 2/3 - 13/(12*m0*6) > (2/3)*(beta_2 + 1/(12*m0)) >= (1/3)*(ln Q_k + ln Q_{k+1})
    disj_kge2_lhs = c_KA ** 2 - rat(2, 3) - rat(13, 72 * m0)
    disj_kge2_rhs = rat(2, 3) * (beta_iv(2) + rat(1, 12 * m0))
    assert disj_kge2_lhs.a > disj_kge2_rhs.b
    print(f"  [DISJ-A]    k=1 ratio <= {fmt(disj_k1.b, 4)} < 1; k>=2 gap >= {fmt((disj_kge2_lhs - disj_kge2_rhs).a, 5)} > 0 CERTIFIED")

    # -------------------------------------------------------------------------
    # 2.7 REGIME A: k = 1, k = 2, k = 3..25, AND UNIFORM k >= 26 (TO INFINITY)
    # -------------------------------------------------------------------------
    # k = 1:
    sR2_k1 = (Q1_hi ** rat(4, 3)) * R2_over_R1_ub
    assert sR2_k1.b < rat(1, 2)
    main_k1 = 1 - Q1_lo ** (-rat(1, 3))
    tail_k1 = (1 + eps_E1) * sR2_k1 / (1 - sR2_k1) + (Q1_hi ** rat(1, 3) + 1) * eps_E0
    err_k1 = tail_k1 / main_k1
    assert err_k1.b < 1
    print(f"  [A-k=1]     err <= {fmt(err_k1.b, 4)} < 1 CERTIFIED")

    # k = 2:
    main_k2 = 1 - Q2_lo ** (-rat(1, 3))
    u0_u2_k2 = (Q2_hi ** rat(2, 3)) * R2_over_R1_ub
    b3_m_b2 = beta_iv(3) - beta_iv(2)
    assert b3_m_b2.b < 0
    u3_u2_k2 = (Q2_hi ** rat(4, 3)) * iv.exp(m0 * b3_m_b2 + (c_iv(3) - c_iv(2)) + rat(13, 72 * m0))
    assert u3_u2_k2.b < rat(1, 2)
    tail_k2 = (
        (1 + eps_E0) * u0_u2_k2
        + (1 + eps_E1) * u3_u2_k2 / (1 - u3_u2_k2)
        + (Q2_hi ** rat(1, 3) + 1) * eps_E1
    )
    err_k2 = tail_k2 / main_k2
    assert err_k2.b < 1
    print(f"  [A-k=2]     err <= {fmt(err_k2.b, 4)} < 1 CERTIFIED")

    # k = 3..25:
    gam_cases = [
        ("Cn_lo", iv.mpf([rat(-1, 3).a, rat(-1, 3).b])),
        ("Cn_hi", iv.mpf([rat(1, 3).a, rat(1, 3).b])),
        ("Cnp1_a", iv.mpf([rat(2, 3).a, rat(1).b])),
        ("Cnp1_b", iv.mpf([rat(1).a, rat(4, 3).b])),
    ]
    worst_smallk = rat(0)
    for k in range(3, 26):
        ck_sq = (c_KA * k) ** 2
        M_min = iv.mpf(m0) if iv.mpf(m0).a >= ck_sq.a else iv.mpf(ck_sq.a)
        bk = beta_iv(k)
        lnQ = iv.mpf([
            (bk - rat(5, 24) / (M_min * k * (k - 1))).a,
            (bk + rat(1, 6) / (M_min * k * (k - 1))).b,
        ])
        for _tag, gam_iv in gam_cases:
            if gam_iv.b < 0:
                main_lb = iv.mpf((iv.exp(-gam_iv * lnQ) - 1).a)
            else:
                main_lb = iv.mpf((1 - iv.exp(-gam_iv * lnQ)).a)
            assert main_lb.a > 0
            tail_ub = rat(0)
            SL, SR, CL, CR, dL_err, dR_err = rat(0), rat(0), rat(0), rat(0), rat(0), rat(0)
            for r in range(1, k - 1):
                SL += beta_iv(k - r) - bk
                SR += bk - beta_iv(k + r)
                CL += c_iv(k - r) - c_iv(k)
                CR += c_iv(k) - c_iv(k + r)
                dL_err += rat(13, 12) / (M_min * (k - r) * (k - r - 1))
                dR_err += rat(13, 12) / (M_min * k * (k - 1))
                S_min = iv.mpf(min(SL.a, SR.a))
                assert (SL - SR).a > 0
                assert (M_min * S_min).a > 1  # guarantees (a + b*M)*exp(-c*M) decreasing for M >= M_min
                A0 = iv.mpf((-(r + 1) * gam_iv * lnQ - CL + dL_err).b)
                B0 = iv.mpf((r * gam_iv * lnQ - CR + dR_err).b)
                exp_ub = iv.exp(iv.mpf(max(A0.b, B0.b)) - M_min * S_min)
                diff_const = iv.mpf(abs((2 * r + 1) * gam_iv * lnQ + (CL - CR)).b) + iv.mpf(dL_err.b) + iv.mpf(dR_err.b)
                diff_M = M_min * iv.mpf((SL - SR).b)
                diff_tot = diff_const + diff_M
                min_factor = rat(1) if diff_tot.b >= 1 else diff_tot
                pair_b = exp_ub * min_factor + (iv.exp(A0 - M_min * iv.mpf(SL.a)) + iv.exp(B0 - M_min * iv.mpf(SR.a))) * eps_E1
                tail_ub += pair_b
            # Right tail r >= k - 1:
            SR_km1 = SR + (bk - beta_iv(2 * k - 1))
            CR_km1 = CR + (c_iv(k) - c_iv(2 * k - 1))
            dR_km1 = dR_err + rat(13, 12) / (M_min * k * (k - 1))
            q_tail_R = iv.exp(iv.mpf((gam_iv * lnQ - M_min * (bk - beta_iv(2 * k)) - (c_iv(k) - c_iv(2 * k)) + rat(13, 12) / (M_min * k * (k - 1))).b))
            assert q_tail_R.b < rat(1, 2)
            u_right_tail = iv.exp(iv.mpf(((k - 1) * gam_iv * lnQ - M_min * SR_km1 - CR_km1 + dR_km1).b)) / (1 - q_tail_R)
            # Left tail u_0 / u_k:
            A0_u1 = iv.mpf((-(k - 1) * gam_iv * lnQ - CL + dL_err).b)
            u1_uk = iv.exp(A0_u1 - M_min * iv.mpf(SL.a))
            u0_u1 = iv.exp(iv.mpf((-gam_iv * lnQ).b)) * R2_over_R1_ub
            u0_uk = u1_uk * u0_u1 * (1 + eps_E0)
            r0_E = (iv.exp(iv.mpf((-gam_iv * lnQ).b)) + 1) * eps_E1
            tot_err = (tail_ub + u_right_tail * (1 + eps_E1) + u0_uk + r0_E) / main_lb
            if tot_err.b > worst_smallk.b:
                worst_smallk = tot_err
    assert worst_smallk.b < 1
    print(f"  [A-k=3..25] worst err <= {fmt(worst_smallk.b, 5)} < 1 CERTIFIED")

    # Uniform k >= k0 = 26 (all the way to infinity, M >= c_KA^2 * k^2):
    k0 = 26
    M0_big = (c_KA * k0) ** 2
    q_lo_fac = 1 - rat(5, 24) / (M0_big * (k0 - 1))
    q_hi_fac = 1 + rat(1, 6 * (k0 ** 2 - 1)) + rat(1, 6) / (M0_big * (k0 - 1))

    # Closed-form constants for Piece 1 (7 <= r <= floor(k/2)):
    K_diff = rat(2) / ((1 - rat(1, k0)) * ((1 - rat(1, k0)) ** 2 - rat(1, 4)))
    K_c = 4 * (1 + rat(4, k0)) / (1 - rat(4, k0 * k0))
    K_d = rat(13, 3) / ((c_KA ** 2) * (1 - rat(2, k0)))
    C_pos = rat(4, 3) * q_hi_fac / (7 * k0) + K_c / (2 * k0 * k0) + K_d / (8 * (k0 ** 4))
    alpha_1 = (c_KA ** 2) / 3 - C_pos
    assert alpha_1.a > 1
    C_poly = (
        rat(4, 3) * q_hi_fac * rat(15, 343)
        + (c_KA ** 2) * K_diff / 2
        + K_c * rat(8, 49 * k0)
        + 2 * K_d / (49 * (k0 ** 3))
    )
    rho_1 = (rat(8, 7) ** 3) * iv.exp(-16 * alpha_1)
    assert rho_1.b < rat(1, 2)
    p1_tail = C_poly * 343 * iv.exp(-56 * alpha_1) / (1 - rho_1)
    p1_pert_sum = 2 * iv.exp(-56 * alpha_1) / (1 - iv.exp(-16 * alpha_1))

    # Closed-form constants for Piece 2 (r >= r_h = floor(k/2) + 1):
    alpha_2 = (c_KA ** 2) / (8 * (rat(3, 2) + rat(1, k0)))
    assert (2 * alpha_2 * k0 * k0).a > 1  # x * exp(-alpha_2 * x^2) decreasing for x >= k0
    C_2R = (
        rat(2, 3) * (1 + rat(2, k0)) * q_hi_fac
        + rat(3 * (k0 + 2), 4 * (k0 - 1))
        + rat(13, 24) * (1 + rat(2, k0)) / (M0_big * (k0 - 1))
    )
    rho_2R = iv.exp(
        rat(4, 3) * q_hi_fac / k0
        + rat(3, 2 * (k0 - 1))
        + rat(13, 12) / (M0_big * k0 * (k0 - 1))
        - (c_KA ** 2) * k0 / (3 + rat(2, k0))
    )
    assert rho_2R.b < rat(1, 2)
    p2_right = (1 + eps_E1) * k0 * iv.exp(C_2R - alpha_2 * k0 * k0) / (1 - rho_2R)

    C_2L = (
        rat(4, 3) * (rat(1, 2) + rat(2, k0)) * q_hi_fac
        + rat(3 * (k0 + 2), 2 * (k0 - 4))
        + rat(13, 12) * rat(k0 + 2, 2) / (M0_big * rat(k0 - 2, 2) * rat(k0 - 4, 2))
    )
    rho_2L = iv.exp(
        rat(4, 3) * q_hi_fac / k0
        + rat(3, k0 - 4)
        + rat(13, 12) / (M0_big * k0 * (k0 - 1))
        - (c_KA ** 2) * k0
    )
    assert rho_2L.b < rat(1, 2)
    p2_left = (1 + eps_E0) * k0 * iv.exp(C_2L - alpha_2 * k0 * k0) / (1 - rho_2L)
    p2_tail = p2_right + p2_left

    worst_bigk = rat(0)
    for _tag, gam_iv in gam_cases:
        if gam_iv.b < 0:
            main_k_lb = iv.mpf((-gam_iv * q_lo_fac).a)
        else:
            main_k_lb = iv.mpf((gam_iv * q_lo_fac * iv.exp(-gam_iv * q_hi_fac / k0)).a)
        assert main_k_lb.a > 0
        tail_k_ub = rat(0)
        # Sum of u_j^{(0)} / u_k^{(0)} across r = 0..6 and Piece 1 for exact eps_E1 perturbation:
        sum_u_pert = iv.exp(iv.mpf(max(rat(0).b, (-gam_iv).b)) * q_hi_fac / k0) + 1 + p1_pert_sum
        aR_sum, diff_sum, cL_sum, cR_sum = rat(0), rat(0), rat(0), rat(0)
        for r in range(1, 7):
            aR_sum += rat(r) / (1 + rat(r, k0))
            diff_sum += rat(2 * r * r) / ((1 - rat(1, k0)) * ((1 - rat(1, k0)) ** 2 - rat(r, k0) ** 2))
            cR_sum += rat(r) * (1 + rat(2, k0)) / ((1 - rat(1, k0 ** 2)) * k0)
            cL_sum += rat(r) * (1 + rat(2, k0 - r)) / (((1 - rat(r, k0)) ** 2) * (1 - rat(1, (k0 - r) ** 2)) * k0)
            d_err = rat(13, 12) * r / (M0_big * (k0 - r) * (k0 - r - 1))
            A0 = (iv.mpf(max(rat(0).b, (-gam_iv).b)) * (r + 1) * q_hi_fac + cL_sum) / k0 + d_err
            B0 = (iv.mpf(max(rat(0).b, gam_iv.b)) * r * q_hi_fac + cR_sum) / k0 + d_err
            assert (c_KA ** 2 * aR_sum).a > 1
            exp_ub = iv.exp(iv.mpf(max(A0.b, B0.b)) - (c_KA ** 2) * iv.mpf(aR_sum.a))
            k_diff = (2 * r + 1) * iv.mpf(abs(gam_iv).b) * q_hi_fac + (c_KA ** 2) * diff_sum + cL_sum + cR_sum + 2 * k0 * d_err
            tail_k_ub += exp_ub * k_diff
            sum_u_pert += 2 * exp_ub
        tot_big = (tail_k_ub + p1_tail + p2_tail + sum_u_pert * k_eps_E1) / main_k_lb
        if tot_big.b > worst_bigk.b:
            worst_bigk = tot_big

    assert worst_bigk.b < 1
    print(f"  [A-k>=26]   worst err <= {fmt(worst_bigk.b, 5)} < 1 CERTIFIED (p1 <= {fmt(p1_tail.b, 3)}, p2 <= {fmt(p2_tail.b, 3)})")


def main():
    run_part1(n0=80)
    run_part2(n0=80)
    print("PASS")


if __name__ == "__main__":
    main()

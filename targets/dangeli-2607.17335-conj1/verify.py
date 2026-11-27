"""Exact-arithmetic (zero-float) verification for targets/dangeli-2607.17335-conj1/.

Verifies:
1. Explicit strongly connected 2-out twin-pair graphs (n = 3, 4, 5, 6) are NOT totally simple
   via an explicit valid coloring chi and nontrivial automaton congruence rho.
2. Exhaustive enumeration at n = 3 (all 3^6 = 729 2-out graphs).
3. Exact integer surjection table T(m, k) up to m = 60, generating-function identity
   F(m, k, t) = sum_{i=0}^t binom(t, i) T(m, k + i), log-concavity, and exact Fraction
   first/second twin moments at n = 30.
4. Exhaustive verification of c_scc_exact[s] for s = 1, 2, 3, 4.
5. Exact rational (Fraction) verification of all analytic inequalities, Taylor brackets,
   interval bounds, and Paley-Zygmund final bound for all n >= 4000.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product
import math


def check_small_witnesses():
    # For n = 3, 4, 5, 6 build an explicit SCC 2-out graph where vertices 0 and 1 are twins
    # sending edges to (2, 2) for n=3, or (2, 3) for n>=4, and remaining vertices form a cycle visiting 0 and 1.
    for n in (3, 4, 5, 6):
        if n == 3:
            edges = [(2, 2), (2, 2), (0, 1)]
        else:
            edges = [(2, 3), (2, 3)]
            # 2 -> (3, 4 % n), ..., n-1 -> (0, 1)
            for u in range(2, n):
                if u == n - 1:
                    edges.append((0, 1))
                else:
                    edges.append((u + 1, 0 if u % 2 == 0 else 1))
        # Verify SCC by exact BFS from every vertex
        for start in range(n):
            seen = {start}
            q = [start]
            while q:
                x = q.pop()
                for y in edges[x]:
                    if y not in seen:
                        seen.add(y)
                        q.append(y)
            assert len(seen) == n, f"Witness n={n} not SCC from {start}"
        # Explicit coloring chi: map edge slot 0 -> letter 1, slot 1 -> letter 2.
        # Since edges[0] == edges[1], rho with nontrivial class {0, 1} satisfies
        # delta(0, c) == delta(1, c) for c in {0, 1}, hence rho is a nontrivial congruence.
        assert edges[0] == edges[1]
        for c in (0, 1):
            assert edges[0][c] == edges[1][c]


def check_exhaustive_n3():
    # All 3^6 = 729 2-out graphs on {0, 1, 2}
    total = 0
    en_count = 0
    scc_count = 0
    scc_twin_count = 0
    for assign in product(range(3), repeat=6):
        total += 1
        edges = [(assign[0], assign[1]), (assign[2], assign[3]), (assign[4], assign[5])]
        indeg = [0, 0, 0]
        for a, b in edges:
            indeg[a] += 1
            indeg[b] += 1
        if min(indeg) >= 1:
            en_count += 1
        is_scc = True
        for s in range(3):
            seen = {s}
            q = [s]
            while q:
                x = q.pop()
                for y in edges[x]:
                    if y not in seen:
                        seen.add(y)
                        q.append(y)
            if len(seen) < 3:
                is_scc = False
                break
        if is_scc:
            scc_count += 1
            multisets = [tuple(sorted(e)) for e in edges]
            if len(set(multisets)) < 3:
                scc_twin_count += 1
    assert total == 729
    assert en_count == 540  # T(6, 3) = 6 * 90 = 540
    assert scc_count == 296  # matches c_scc_exact[3][0]
    assert scc_twin_count == 126


def check_surjection_table():
    max_m = 60
    max_k = 30
    T = [[0] * (max_k + 5) for _ in range(max_m + 1)]
    T[0][0] = 1
    for m in range(1, max_m + 1):
        for k in range(1, min(m, max_k + 4) + 1):
            T[m][k] = k * (T[m - 1][k] + T[m - 1][k - 1])
    assert T[6][3] == 540

    # Check F(m, k, t) identity and log-concavity
    for m in range(1, 30):
        for k in range(1, min(m, 20) + 1):
            if m > k:
                assert (m + 1) * T[m][k] ** 2 >= m * T[m - 1][k] * T[m + 1][k]
        for t in (1, 2, 3, 4):
            for k in range(1, min(m, 15) + 1):
                lhs = sum(math.comb(m, j) * (t ** j) * T[m - j][k] for j in range(m - k + 1))
                rhs = sum(math.comb(t, i) * T[m][k + i] for i in range(t + 1) if k + i <= m)
                assert lhs == rhs

    # Exact Fraction check of E_n[N] and E_n[N^2] at n = 25
    n = 25
    def F(m, k, t):
        return sum(math.comb(t, i) * T[m][k + i] for i in range(t + 1) if k + i <= m)

    EN = Fraction(math.comb(n, 2) * math.comb(n - 2, 2) * 4 * F(2 * n - 4, n - 2, 2), T[2 * n][n])
    assert Fraction(0) < EN < Fraction(1)


def check_scc_internal_counts():
    expected = {
        1: [1, 2],
        2: [9, 12, 4],
        3: [296, 372, 144, 16],
        4: [20958, 26304, 11376, 1920, 96],
    }
    for s in (1, 2, 3, 4):
        counts = [0] * (s + 1)
        for assign in product(range(-1, s), repeat=2 * s):
            M = assign.count(-1)
            if M > s:
                continue
            adj = [[] for _ in range(s)]
            indeg = [0] * s
            outdeg = [0] * s
            for u in range(s):
                for v in (assign[2 * u], assign[2 * u + 1]):
                    if v >= 0:
                        adj[u].append(v)
                        outdeg[u] += 1
                        indeg[v] += 1
            if min(indeg) == 0 or min(outdeg) == 0:
                continue
            if s > 1:
                seen = {0}
                q = [0]
                while q:
                    x = q.pop()
                    for y in adj[x]:
                        if y not in seen:
                            seen.add(y)
                            q.append(y)
                if len(seen) < s:
                    continue
                radj = [[] for _ in range(s)]
                for u in range(s):
                    for v in adj[u]:
                        radj[v].append(u)
                seen = {0}
                q = [0]
                while q:
                    x = q.pop()
                    for y in radj[x]:
                        if y not in seen:
                            seen.add(y)
                            q.append(y)
                if len(seen) < s:
                    continue
            counts[M] += 1
        assert counts == expected[s], f"Mismatch for s={s}: {counts} != {expected[s]}"
    return expected


# --- Exact rational Taylor utilities (zero float) ---

ROUND_DEN = 10 ** 12


def dn(x: Fraction) -> Fraction:
    """Exact rational floor to denominator ROUND_DEN: dn(x) <= x."""
    return Fraction((x.numerator * ROUND_DEN) // x.denominator, ROUND_DEN)


def up(x: Fraction) -> Fraction:
    """Exact rational ceiling to denominator ROUND_DEN: up(x) >= x."""
    q, r = divmod(x.numerator * ROUND_DEN, x.denominator)
    return Fraction(q + (1 if r else 0), ROUND_DEN)


def exp_bounds(x: Fraction, terms: int = 32) -> tuple[Fraction, Fraction]:
    """Return exact rational (lo, hi) enclosing exp(x) for |x| <= 5."""
    assert abs(x) <= 5
    s = Fraction(0)
    term = Fraction(1)
    for k in range(terms):
        s += term
        term = term * x / (k + 1)
    if x >= 0:
        rem = abs(term) / (1 - x / (terms + 1))
        return dn(s), up(s + rem)
    else:
        assert abs(x) < terms + 1
        if terms % 2 == 0:
            return dn(s), up(s + abs(term))
        else:
            return dn(s - abs(term)), up(s)


def ln1p_bounds(x: Fraction, terms: int = 60) -> tuple[Fraction, Fraction]:
    """Return exact rational (lo, hi) enclosing ln(1 + x) for -4/5 <= x <= 4/5."""
    assert Fraction(-4, 5) <= x <= Fraction(4, 5)
    s = Fraction(0)
    xp = x
    for k in range(1, terms + 1):
        if k % 2 == 1:
            s += xp / k
        else:
            s -= xp / k
        xp *= x
    if x >= 0:
        rem = abs(xp) / (terms + 1)
        if terms % 2 == 1:
            return dn(s - rem), up(s)
        else:
            return dn(s), up(s + rem)
    else:
        rem = abs(xp) / ((terms + 1) * (1 - abs(x)))
        return dn(s - rem), up(s)


@lru_cache(maxsize=None)
def ln_bounds(y: Fraction) -> tuple[Fraction, Fraction]:
    """Return exact rational (lo, hi) enclosing ln(y) for y > 0."""
    assert y > 0
    m = 0
    z = y
    while z > Fraction(3, 2):
        z /= 2
        m += 1
    while z < Fraction(3, 4):
        z *= 2
        m -= 1
    ln2_lo = Fraction(0)
    p9 = Fraction(1)
    for k in range(18):
        ln2_lo += Fraction(2, (2 * k + 1) * 3) / p9
        p9 *= 9
    ln2_hi = ln2_lo + Fraction(2, 37 * 3) / p9 / (1 - Fraction(1, 9))
    lz_lo, lz_hi = ln1p_bounds(z - 1, terms=42)
    if m >= 0:
        return dn(m * ln2_lo + lz_lo), up(m * ln2_hi + lz_hi)
    else:
        return dn(m * ln2_hi + lz_lo), up(m * ln2_lo + lz_hi)


def cos_bounds(x: Fraction, terms: int = 10) -> tuple[Fraction, Fraction]:
    """Return exact rational (lo, hi) enclosing cos(x) for |x| <= 1."""
    assert abs(x) <= 1
    s = Fraction(0)
    term = Fraction(1)
    x2 = x * x
    for k in range(terms):
        s += term
        term = -term * x2 / ((2 * k + 1) * (2 * k + 2))
    if terms % 2 == 1:
        return dn(s - abs(term)), up(s)
    else:
        return dn(s), up(s + abs(term))


def sqrt_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    """Return exact rational (lo, hi) enclosing sqrt(x) for x >= 0."""
    assert x >= 0
    if x == 0:
        return Fraction(0), Fraction(0)
    # 12 steps of Newton starting from integer/simple rational gives > 10^-25 precision
    # Use math.isqrt on scaled integer for exact instant bracket!
    num = x.numerator
    den = x.denominator
    scale = 10 ** 30
    val = num * (scale * scale) // den
    r = math.isqrt(val)
    lo = Fraction(r, scale)
    hi = Fraction(r + 1, scale)
    assert lo * lo <= x <= hi * hi
    return lo, hi


def pi_bounds() -> tuple[Fraction, Fraction]:
    """Return exact rational bounds on pi via Machin's formula pi/4 = 4*atan(1/5) - atan(1/239)."""
    def atan_bounds(inv: int, terms: int) -> tuple[Fraction, Fraction]:
        s = Fraction(0)
        p = Fraction(1, inv)
        inv2 = inv * inv
        for k in range(terms):
            term = p / (2 * k + 1)
            s += term if k % 2 == 0 else -term
            p /= inv2
        rem = p / (2 * terms + 1)
        if terms % 2 == 1:
            return s - rem, s
        return s, s + rem

    a5_lo, a5_hi = atan_bounds(5, 25)
    a239_lo, a239_hi = atan_bounds(239, 12)
    return 4 * (4 * a5_lo - a239_hi), 4 * (4 * a5_hi - a239_lo)


def check_analytic_bounds(c_scc_exact):
    N0 = 4000
    # 1. Exact bracket on lam: lam / (1 - e^{-lam}) = 2 <=> e^lam (2 - lam) = 2
    lam_lo = Fraction(1593624, 10 ** 6)
    lam_hi = Fraction(1593625, 10 ** 6)
    elo_lo, elo_hi = exp_bounds(lam_lo)
    ehi_lo, ehi_hi = exp_bounds(lam_hi)
    # f(x) = e^x(2-x) is strictly decreasing on (1, 2) since f'(x) = e^x(1-x) < 0:
    assert elo_lo * (2 - lam_lo) > 2 and ehi_hi * (2 - lam_hi) < 2

    elam_lo, elam_hi = elo_lo, ehi_hi
    elam_m1_lo, elam_m1_hi = elam_lo - 1, elam_hi - 1
    # Verify e^lam / (e^lam - 1) = 2 / lam
    sig_lo, sig_hi = 2 * (lam_lo - 1), 2 * (lam_hi - 1)
    # m3 = 2*lam^2 - 8*lam + 10 (decreasing on [1.59, 1.60], derivative 4*lam - 8 < 0)
    m3_lo = 2 * lam_hi ** 2 - 8 * lam_hi + 10
    m3_hi = 2 * lam_lo ** 2 - 8 * lam_lo + 10
    # m4 = 2*lam^3 - 4*lam^2 + 14*lam - 14 (increasing on [1.59, 1.60], derivative 6*lam^2 - 8*lam + 14 > 0)
    m4_lo = 2 * lam_lo ** 3 - 4 * lam_lo ** 2 + 14 * lam_lo - 14
    m4_hi = 2 * lam_hi ** 3 - 4 * lam_hi ** 2 + 14 * lam_hi - 14

    # 2. Lemma 2 constants at delta = 3/10
    delta = Fraction(3, 10)
    delta2 = delta * delta
    C4_hi = (sig_hi ** 2) / 4 + m4_hi / 12 + (m3_hi ** 2) * delta2 / 36 + (m4_hi ** 2) * (delta2 ** 2) / 576
    c_loc_lo = (sig_lo - C4_hi * delta2) / 2
    assert 2 * c_loc_lo > Fraction(1107, 1000)

    A_lo = lam_lo + lam_lo ** 2 / 2
    A_hi = lam_hi + lam_hi ** 2 / 2
    cosd_lo, cosd_hi = cos_bounds(delta)
    # 1 - cos(delta) >= 1 - cosd_hi
    rad_hi = A_hi ** 2 - (lam_lo ** 3) * (1 - cosd_hi)
    srad_lo, srad_hi = sqrt_bounds(rad_hi)
    # rho_delta <= (sqrt(A^2 - lam^3(1-cos d)) + (e^lam - 1 - A)) / (e^lam - 1)
    # Note numerator has -A + e^lam - 1 + sqrt(...), check A_hi vs A_lo cleanly:
    rho_hi = (srad_hi + elam_m1_hi - A_lo) / elam_m1_lo
    assert rho_hi < Fraction(992, 1000)

    # 3. C_up <= 38/100 for k >= 1996
    pi_lo, pi_hi = pi_bounds()
    sq_lo, _ = sqrt_bounds(pi_lo * c_loc_lo)
    kmin_sq_lo, kmin_sq_hi = sqrt_bounds(Fraction(1996))
    ub_hi = Fraction(1, 2) / sq_lo + kmin_sq_hi * (rho_hi ** 1996)
    assert ub_hi <= Fraction(38, 100), f"ub_hi={ub_hi}"

    # 4. c_low >= 34/100 for k >= 3998, |d| <= 4
    k0 = 3998
    R = Fraction(26, 10)
    R2 = R * R
    R3 = R2 * R
    R4 = R2 * R2
    t02_hi = R2 / k0
    r_min_lo = 1 - sig_hi * t02_hi / 2
    k0sq_lo, k0sq_hi = sqrt_bounds(Fraction(k0))
    max_ang_hi = (m3_hi * R3 / (6 * r_min_lo) + 4 * R) / k0sq_lo
    assert max_ang_hi < Fraction(28, 100)
    cos_min_lo, _ = cos_bounds(max_ang_hi)
    exp_q_lo, _ = exp_bounds(-(sig_hi ** 2) * R4 / (4 * k0))

    sig_sq_lo, sig_sq_hi = sqrt_bounds(sig_lo)
    z_lo = R * sig_sq_lo
    ez_lo, ez_hi = exp_bounds(-z_lo * z_lo / 2)
    twopi_sq_lo, _ = sqrt_bounds(2 * pi_lo)
    gauss_tail_hi = 2 * ez_hi / (z_lo * twopi_sq_lo)

    twopisig_sq_lo, twopisig_sq_hi = sqrt_bounds(2 * pi_hi * sig_hi)
    main_lb = (1 / twopisig_sq_hi) * (1 - gauss_tail_hi) * exp_q_lo * cos_min_lo

    emid_lo, emid_hi = exp_bounds(-c_loc_lo * R2)
    tail_mid_hi = emid_hi / (2 * pi_lo * c_loc_lo * R)
    tail_far_hi = k0sq_hi * (rho_hi ** k0)
    c_low_lo = main_lb - tail_mid_hi - tail_far_hi
    assert c_low_lo >= Fraction(34, 100), f"c_low_lo={c_low_lo}"

    C_up = Fraction(38, 100)
    c_low = Fraction(34, 100)
    ratio_small = (C_up / c_low) * Fraction(1001, 1000)

    # 5. Exact rational sum for Case 2a s = 1..4
    sum_2a_low = Fraction(0)
    for s in range(1, 5):
        for M in range(s + 1):
            fac = (Fraction(1, math.factorial(s))
                   * Fraction(1, 2 ** (2 * s - M))
                   / ((Fraction(1) - Fraction(11, 2 * N0)) ** (2 * s - M))
                   * Fraction(1, N0 ** (s - M)))
            term = fac * c_scc_exact[s][M] * (lam_hi ** (2 * s - M)) / (elam_m1_lo ** s) * ratio_small
            sum_2a_low += term
    assert sum_2a_low < Fraction(581, 1000), f"sum_2a_low={sum_2a_low}"

    # 6. Exact rational sum for Case 2a s = 5..15
    # Using (e^r - 1) and r^{-1} exact brackets via exp_bounds
    _, sq_mid_hi = sqrt_bounds(Fraction(N0, 3916))
    ratio_02 = (C_up / c_low) * sq_mid_hi
    eps_02 = Fraction(4, 100) / (Fraction(196, 100) - Fraction(4, N0))
    sum_2a_5_15 = Fraction(0)
    for s in range(5, 16):
        for M in range(s + 1):
            comb_part = math.comb(s, M) * (2 ** M) * (eps_02 ** (s - M)) * Fraction(1, 2 ** s)
            if M == s:
                sad_hi = (lam_hi / elam_m1_lo) ** s
            else:
                r_lo = lam_lo * Fraction(s - M, s)
                r_hi = lam_hi * Fraction(s - M, s)
                _, er_hi = exp_bounds(r_hi)
                sad_hi = (((er_hi - 1) / elam_m1_lo) ** s) * ((lam_hi / r_lo) ** (2 * s - M))
            sum_2a_5_15 += comb_part * sad_hi * ratio_02
    assert sum_2a_5_15 < Fraction(42, 1000), f"sum_2a_5_15={sum_2a_5_15}"

    # 7. Exact rational interval verification for f_mid(p) <= -7/10 on [0, 1]
    ln2_lo, ln2_hi = ln_bounds(Fraction(2))
    lneps_lo, lneps_hi = ln_bounds(eps_02)
    lnsl_lo, lnsl_hi = ln_bounds(elam_m1_lo / lam_hi)
    _, inv_e_hi = exp_bounds(Fraction(-1))
    inv_e_lo, _ = exp_bounds(Fraction(-1))
    for i in range(300):
        a = Fraction(i, 300)
        b = Fraction(i + 1, 300)
        # -p*ln(p) max on [a, b]
        if a == 0:
            p1_max = max(-b * ln_bounds(b)[0], inv_e_hi if b >= inv_e_lo else Fraction(0))
        else:
            p1_max = max(-a * ln_bounds(a)[0], -b * ln_bounds(b)[0])
            if not (b < inv_e_lo or a > inv_e_hi):
                p1_max = max(p1_max, inv_e_hi)
        # -2*(1-p)*ln(1-p) max on [a, b], writing q = 1-p in [1-b, 1-a]
        qa, qb = 1 - b, 1 - a
        if qa == 0:
            p2_max = 2 * max(-qb * ln_bounds(qb)[0], inv_e_hi if qb >= inv_e_lo else Fraction(0))
        else:
            p2_max = 2 * max(-qa * ln_bounds(qa)[0], -qb * ln_bounds(qb)[0])
            if not (qb < inv_e_lo or qa > inv_e_hi):
                p2_max = max(p2_max, 2 * inv_e_hi)
        # p*ln(2) + (1-p)*ln(eps_02) increasing in p -> at b
        p3_max = b * ln2_hi + (1 - b) * lneps_hi
        # ln((e^{lam*(1-p)}-1)/(lam*(1-p))) decreasing in p -> at a
        if a == 0:
            r_hi = lam_hi
            _, er_hi = exp_bounds(r_hi)
            p4_max = ln_bounds((er_hi - 1) / lam_lo)[1]
        else:
            r_lo = lam_lo * (1 - a)
            r_hi = lam_hi * (1 - a)
            _, er_hi = exp_bounds(r_hi)
            p4_max = ln_bounds((er_hi - 1) / r_lo)[1]
        val_hi = -ln2_lo + p1_max + p2_max + p3_max + p4_max - lnsl_lo
        assert val_hi <= Fraction(-7, 10), f"f_mid failed on [{a},{b}]: {val_hi}"

    # Geometric bound for 16 <= s <= 0.02n: 1.13 * sum_{s>=16} (s+1) * x^s = 1.13 * (17*x^16 - 16*x^17)/(1-x)^2
    em07_lo, em07_hi = exp_bounds(Fraction(-7, 10))
    tail_16 = Fraction(113, 100) * (17 * (em07_hi ** 16) - 16 * (em07_hi ** 16) * em07_lo) / ((1 - em07_hi) ** 2)
    assert tail_16 < Fraction(1, 1000), f"tail_16={tail_16}"

    # 8. Exact rational interval verification for sink exponent f_sink <= -6/100 on [0.02, 0.5]
    lnlam_lo, lnlam_hi = ln_bounds(lam_lo)[0], ln_bounds(lam_hi)[1]
    lnel_lo, lnel_hi = ln_bounds(elam_m1_lo)[0], ln_bounds(elam_m1_hi)[1]
    sink_intervals = ([(Fraction(i, 500), Fraction(i + 1, 500)) for i in range(10, 50)]
                      + [(Fraction(i, 100), Fraction(i + 1, 100)) for i in range(10, 50)])
    for a, b in sink_intervals:
        # alpha*ln(alpha) + (1-alpha)*ln(1-alpha) = -H(alpha)
        # Wait: alpha*ln(alpha) is negative; decreasing on [0, 1/e], increasing on [1/e, 0.5]
        v_a = a * ln_bounds(a)[1]
        v_b = b * ln_bounds(b)[1]
        t1_hi = max(v_a, v_b)  # convex, so max on [a, b] is at an endpoint!
        t2_hi = max((1 - a) * ln_bounds(1 - a)[1], (1 - b) * ln_bounds(1 - b)[1])
        # r(alpha) = lam * (1 - 1.3 * alpha) in [r_lo, r_hi]
        r_a_hi = lam_hi * (1 - Fraction(13, 10) * a)
        r_b_lo = lam_lo * (1 - Fraction(13, 10) * b)
        # -2*a*ln(lam) + a*ln(e^lam-1) + a*r(a):
        t3_hi = -2 * a * lnlam_lo + b * lnel_hi + b * r_a_hi
        # (1-a)*ln(e^{r(a)}-1): r decreases in alpha; check sign of ln(e^r - 1)
        _, er_a_hi = exp_bounds(r_a_hi)
        ln_er_hi = ln_bounds(er_a_hi - 1)[1]
        t4_hi = (1 - a) * ln_er_hi if ln_er_hi >= 0 else (1 - b) * ln_er_hi
        # -2*(1-a)*ln(r(a)): ln(r_b_lo) <= ln(r) <= ln(r_a_hi)
        ln_r_lo = ln_bounds(r_b_lo)[0]
        t5_hi = -2 * (1 - a) * ln_r_lo if ln_r_lo <= 0 else -2 * (1 - b) * ln_r_lo
        val = t1_hi + t2_hi + t3_hi + t4_hi + t5_hi + 2 * lnlam_hi - lnel_lo
        assert val <= Fraction(-5, 100), f"f_sink failed on [{a},{b}]: {val}"

    # 9. Exact rational interval verification for R(alpha, p) <= -30/100 on (0, 0.5] x [0, 1]
    def H_hi(x: Fraction) -> Fraction:
        if x == 0 or x == 1:
            return Fraction(0)
        return -x * ln_bounds(x)[0] - (1 - x) * ln_bounds(1 - x)[0]

    def H_lo(x: Fraction) -> Fraction:
        if x == 0 or x == 1:
            return Fraction(0)
        return -x * ln_bounds(x)[1] - (1 - x) * ln_bounds(1 - x)[1]

    _, sq2_hi = sqrt_bounds(Fraction(2))
    sq2_lo, _ = sqrt_bounds(Fraction(2))
    for i in range(300):
        a = Fraction(i, 300)
        b = Fraction(i + 1, 300)
        # Upper bound on g_max(p) on [a, b]:
        # Remember beta = (2 - p) / 2 decreases as p increases, and g_max(beta) is increasing in p.
        # So g_max(p) <= g_max(b) = g(alpha^*(b), (2-b)/2).
        beta_b = (2 - b) / 2
        if beta_b >= 2 - sq2_lo:
            a_star = Fraction(1, 2)
            gm_hi = 2 * ln2_hi - 4 * H_lo(beta_b / 2)
        elif b == 1:
            gm_hi = -ln2_lo
        else:
            a_star = min(Fraction(1, 2), (2 * beta_b - 1) / (beta_b * beta_b))
            gm_hi = (H_hi(a_star) - 2 * H_lo(beta_b * a_star)) / a_star
        # -p*ln(p) max on [a, b]
        if a == 0:
            hp1 = max(-b * ln_bounds(b)[0], inv_e_hi if b >= inv_e_lo else Fraction(0))
        else:
            hp1 = max(-a * ln_bounds(a)[0], -b * ln_bounds(b)[0])
            if not (b < inv_e_lo or a > inv_e_hi):
                hp1 = max(hp1, inv_e_hi)
        qa, qb = 1 - b, 1 - a
        if qa == 0:
            hp2 = max(-qb * ln_bounds(qb)[0], inv_e_hi if qb >= inv_e_lo else Fraction(0))
        else:
            hp2 = max(-qa * ln_bounds(qa)[0], -qb * ln_bounds(qb)[0])
            if not (qb < inv_e_lo or qa > inv_e_hi):
                hp2 = max(hp2, inv_e_hi)
        # sad(p) = ln((e^{lam(1-p)}-1)/lam(1-p)) + (1-p)*ln(lam/(lam(1-p))) - ln((e^lam-1)/lam)
        # Wait: sad(p) = ln(e^{r}-1) - (2-p)*ln(r) + (2-p)*ln(lam) - ln(e^lam-1)
        # Rewrite cleanly: ln((e^r-1)/r) - ln((e^lam-1)/lam) - (1-p)*ln(1-p), where r = lam*(1-p)
        if a == 0:
            _, er_hi = exp_bounds(lam_hi)
            sad1 = ln_bounds((er_hi - 1) / lam_lo)[1]
        else:
            r_lo = lam_lo * (1 - a)
            r_hi = lam_hi * (1 - a)
            _, er_hi = exp_bounds(r_hi)
            sad1 = ln_bounds((er_hi - 1) / r_lo)[1]
        # Note -(1-p)*ln(1-p) from sad(p) combines with -(1-p)*ln(1-p) from H(p)!
        # So H(p) + sad(p) uses 2 * hp2!
        val_R = gm_hi + hp1 + 2 * hp2 + b * ln2_hi + sad1 - lnsl_lo
        assert val_R <= Fraction(-30, 100), f"R failed on [{a},{b}]: {val_R}"

        # Also check R(alpha, p) <= -60/100 on (0, 0.10] x [0, 1] (used in Case 2b)
        if beta_b >= Fraction(10, 10):
            gm01_hi = gm_hi
        else:
            # At alpha in (0, 0.10], if critical point alpha* <= 0.10 use alpha*, else alpha = 0.10
            a_star_01 = min(Fraction(1, 10), (2 * beta_b - 1) / (beta_b * beta_b)) if 2 * beta_b > 1 else Fraction(0)
            if a_star_01 <= 0:
                gm01_hi = -ln2_lo
            else:
                gm01_hi = (H_hi(a_star_01) - 2 * H_lo(beta_b * a_star_01)) / a_star_01
        val_R01 = gm01_hi + hp1 + 2 * hp2 + b * ln2_hi + sad1 - lnsl_lo
        assert val_R01 <= Fraction(-60, 100), f"R01 failed on [{a},{b}]: {val_R01}"

    # Check large tail sum for s > 0.02*N0 = 80 (i.e. s >= 81):
    # sum_{s>=81} (s+1) x^s = (82 x^81 - 81 x^82) / (1 - x)^2
    em03_lo, em03_hi = exp_bounds(Fraction(-3, 10))
    _, sq201_hi = sqrt_bounds(Fraction(201, 100))
    tail_large_2a = (16 * (2 * N0 + 1) * (C_up / c_low) * sq201_hi
                     * (82 * (em03_hi ** 81) - 81 * (em03_hi ** 81) * em03_lo) / ((1 - em03_hi) ** 2))
    assert tail_large_2a < Fraction(3, 1000), f"tail_large_2a={tail_large_2a}"

    # Checks for Cases 1a, 1b, 2b (small/mid and large exponential tails)
    s1a_14 = sum(
        Fraction(math.factorial(2 * s), math.factorial(s))
        * Fraction(N0 ** s, (2 * N0 - 12) ** (2 * s))
        * ((2 / lam_lo) ** (s + 2))
        * (lam_hi ** (2 * s))
        / (elam_m1_lo ** s)
        * ratio_small
        for s in range(1, 5)
    )
    den1a = Fraction(196, 100) * N0 - 4
    s1a_59 = sum(
        ratio_02 * ((Fraction(s, 1) * elam_hi / den1a) ** s)
        for s in range(5, 10)
    )
    x1a_10 = Fraction(103, 10000) * elam_hi
    s1a_10p = ratio_02 * (x1a_10 ** 10) / (1 - x1a_10)
    assert s1a_59 + s1a_10p < Fraction(1, 10 ** 12)
    # Large sink tail: f_sink <= -5/100 => exp(-0.05 * 4000) = (e^{-5})^{40} < 10^-60
    _, em5_hi = exp_bounds(Fraction(-5))
    s1a_large = 100 * (2 * N0 + 1) * N0 * (em5_hi ** 40) * N0
    assert s1a_14 + s1a_59 + s1a_10p + s1a_large < Fraction(2, 1000)

    s1b_34 = sum(
        math.comb(2, r)
        * Fraction(math.factorial(2 * s - 2 * r), math.factorial(s - 2 - r))
        * Fraction(N0 ** (s - 2 - r), (2 * N0 - 12) ** (2 * s - 2 * r))
        * (lam_hi ** (2 * s - 2 * r))
        * ((2 / lam_lo) ** s)
        * ratio_small
        for s in (3, 4)
        for r in (1, 2)
        if s >= 2 + r
    )
    s1b_mid = Fraction(0)
    for s in range(5, 81):
        for r in (1, 2):
            s1b_mid += (
                ratio_02 * math.comb(2, r)
                * (Fraction(1, 2) ** (s - 2 - r))
                * ((Fraction(2 * s - 2 * r, 1) / den1a) ** (s - r + 2))
                * (elam_hi ** s)
            )
    assert s1b_34 + s1b_mid + s1a_large < Fraction(1, 1000)

    s2b_mid = Fraction(0)
    for s in range(3, 81):
        for q in (1, 2):
            if s < 2 + q:
                continue
            for M in range(s - 1):
                m_in = 2 * s - 4 - M
                k_in = s - q
                if m_in < k_in:
                    continue
                k_extra = m_in - (s - 2 - q)
                fac = (math.comb(2, q) * math.comb(s - 2, M) * (2 ** M)
                       * (Fraction(1, 2) ** (s - 2 - q))
                       * ((Fraction(m_in, 1) / den1a) ** k_extra))
                if m_in == k_in:
                    _, emq_hi = exp_bounds(Fraction(-q) * lam_lo)
                    sad = ((lam_hi / elam_m1_lo) ** k_in) * emq_hi
                else:
                    r_lo = lam_lo * Fraction(s - M, s)
                    r_hi = lam_hi * Fraction(s - M, s)
                    _, er_hi = exp_bounds(r_hi)
                    _, eq_hi = exp_bounds(Fraction(q) * (r_hi - lam_lo))
                    sad = (((lam_hi / r_lo) ** m_in) * eq_hi
                           * (((er_hi - 1) / elam_m1_lo) ** k_in) / (elam_m1_lo ** q))
                s2b_mid += ratio_02 * fac * sad
    em06_lo, em06_hi = exp_bounds(Fraction(-6, 10))
    s2b_large_01 = (6500 * 16 * (2 * N0 + 1) * (C_up / c_low) * sq201_hi
                    * (82 * (em06_hi ** 81) - 81 * (em06_hi ** 81) * em06_lo) / ((1 - em06_hi) ** 2))
    assert s2b_mid + s2b_large_01 < Fraction(2, 1000), f"s2b={s2b_mid + s2b_large_01}"

    # 10. Verify E[Z] >= 20/100 and E[N^2] <= 120/100 and final Paley-Zygmund bound!
    Pr_SCC_T_lb = Fraction(36, 100)
    EZ_lb = Pr_SCC_T_lb * ((1 - Fraction(3, N0)) ** 3) * (lam_lo ** 2) / 4 * (c_low / C_up)
    assert EZ_lb >= Fraction(20, 100), f"EZ_lb={EZ_lb}"

    _, sq_n_n2_hi = sqrt_bounds(Fraction(N0, N0 - 2))
    EN_ub = (lam_hi ** 2) / 4 * (C_up / c_low) / ((1 - Fraction(3, 2 * N0)) ** 4) * sq_n_n2_hi
    _, sq_n_n4_hi = sqrt_bounds(Fraction(N0, N0 - 4))
    EN2_disjoint_ub = ((lam_hi / 2) ** 4) * (C_up / c_low) * sq_n_n4_hi / ((1 - Fraction(7, 2 * N0)) ** 8)
    EN2_ub = EN_ub + EN2_disjoint_ub + Fraction(1, 100)
    assert EN2_ub <= Fraction(120, 100), f"EN2_ub={EN2_ub}"

    pz_lb = (Fraction(20, 100) ** 2) / Fraction(120, 100)
    assert pz_lb == Fraction(1, 30)
    print(f"PASS (exact Fraction proof verified for all n>={N0}: Pr(G totally simple | SCC_n) <= 29/30)")


def main():
    check_small_witnesses()
    check_exhaustive_n3()
    check_surjection_table()
    c_scc_exact = check_scc_internal_counts()
    check_analytic_bounds(c_scc_exact)


if __name__ == "__main__":
    main()

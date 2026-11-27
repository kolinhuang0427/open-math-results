#!/usr/bin/env python3
"""Exact integer-interval verifier for Hare-Hichri (arXiv:2603.19554v1) Conjecture 3.3.

Verifies in pure 128-bit fixed-point integer interval arithmetic (no floating point in
any certification step) that for every 4 <= d <= 499 and every k >= 1, beta_d^k is
non-Parry, where beta_d > 1 is the Perron root of P_d(x) = x^d - x - 1.

Specifically:
1. Brackets beta_d in (b_lo, b_hi) by checking P_d(b_lo) < 0 < P_d(b_hi).
2. Certifies a complex root gamma_d with Im(gamma_d) > 0 via Rouche's theorem on a
   disk |z - z_*| < 2^-60.
3. Advances k = 1, 2, ... until |gamma_d|^{2k} > (3 + sqrt(5))/2 = theta_0^2 strictly,
   which disposes of this k and all larger k by Solomyak's bound (as |gamma_d| > 1).
4. For all smaller k:
   - d in {4, 5}: certifies the greedy digits of T_{beta_d^k}^n(1) and verifies
     Akiyama's divergence threshold |sigma(T_q^n(1))| > floor(q) / (|gamma_d^k| - 1).
   - 6 <= d <= 499: certifies 1 < q < 2, certifies m_0 via
     q^{m_0 - 2}(q - 1) < 1 < q^{m_0 - 1}(q - 1), and verifies
     |c^{2m_0 - 2} - c^{2m_0 - 3} - c^{m_0 - 2}| * (|c| - 1) > 1.
"""

import math
import sys

P = 128
S = 1 << P


def iv_from_int(n: int) -> tuple[int, int]:
    v = n << P
    return (v, v)


def iv_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def iv_sub(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] - b[1], a[1] - b[0])


def iv_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    a0, a1 = a
    b0, b1 = b
    p1 = a0 * b0
    p2 = a0 * b1
    p3 = a1 * b0
    p4 = a1 * b1
    return (min(p1, p2, p3, p4) >> P, (max(p1, p2, p3, p4) + S - 1) >> P)


def iv_sqr(a: tuple[int, int]) -> tuple[int, int]:
    a0, a1 = a
    if a0 <= 0 <= a1:
        mn = 0
        mx = max(a0 * a0, a1 * a1)
    else:
        p0 = a0 * a0
        p1 = a1 * a1
        mn = min(p0, p1)
        mx = max(p0, p1)
    return (mn >> P, (mx + S - 1) >> P)


def iv_pow(a: tuple[int, int], n: int) -> tuple[int, int]:
    res = (S, S)
    base = a
    while n > 0:
        if n & 1:
            res = iv_mul(res, base)
        n >>= 1
        if n:
            base = iv_sqr(base)
    return res


def iv_div(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    assert b[0] > 0
    a0, a1 = a
    b0, b1 = b
    lo = min((a0 << P) // b1, (a0 << P) // b0)
    hi = max(((a1 << P) + b0 - 1) // b0, ((a1 << P) + b1 - 1) // b1)
    return (lo, hi)


def iv_sqrt(a: tuple[int, int]) -> tuple[int, int]:
    assert a[0] >= 0
    lo = math.isqrt(a[0] << P)
    hi = math.isqrt((a[1] << P) - 1) + 1 if a[1] > 0 else 0
    return (lo, hi)


def civ_sub(z, w):
    return (iv_sub(z[0], w[0]), iv_sub(z[1], w[1]))


def civ_mul(z, w):
    zr, zi = z
    wr, wi = w
    return (
        iv_sub(iv_mul(zr, wr), iv_mul(zi, wi)),
        iv_add(iv_mul(zr, wi), iv_mul(zi, wr)),
    )


def civ_sqr(z):
    zr, zi = z
    two_zri = iv_mul(zr, zi)
    two_zri = (two_zri[0] << 1, two_zri[1] << 1)
    return (iv_sub(iv_sqr(zr), iv_sqr(zi)), two_zri)


def civ_pow(z, n: int):
    res = ((S, S), (0, 0))
    base = z
    while n > 0:
        if n & 1:
            res = civ_mul(res, base)
        n >>= 1
        if n:
            base = civ_sqr(base)
    return res


def civ_abs2(z):
    return iv_add(iv_sqr(z[0]), iv_sqr(z[1]))


def certify_beta(d: int) -> tuple[int, int]:
    # Untrusted float guess, refined by integer Newton, then certified by exact IVT.
    lo_f, hi_f = 1.0, 2.0
    for _ in range(60):
        mid = 0.5 * (lo_f + hi_f)
        if mid**d - mid - 1.0 < 0.0:
            lo_f = mid
        else:
            hi_f = mid
    x = int(round(0.5 * (lo_f + hi_f) * S))
    for _ in range(4):
        xd1 = iv_pow((x, x), d - 1)
        xd = iv_mul(xd1, (x, x))
        f = ((xd[0] + xd[1]) >> 1) - x - S
        df = (((xd1[0] + xd1[1]) >> 1) * d) - S
        x -= (f << P) // df
    step = 1 << (P - 80)
    b_lo = max(S + 1, x - step)
    b_hi = min((S << 1) - 1, x + step)
    p_lo = iv_sub(iv_sub(iv_pow((b_lo, b_lo), d), (b_lo, b_lo)), (S, S))
    p_hi = iv_sub(iv_sub(iv_pow((b_hi, b_hi), d), (b_hi, b_hi)), (S, S))
    assert p_lo[1] < 0 and p_hi[0] > 0, f"beta IVT check failed at d={d}"
    return (b_lo, b_hi)


def newton_gamma_point(d: int) -> tuple[int, int]:
    ang = 2.0 * math.pi / d
    r = 2.0 ** (1.0 / d)
    z = complex(r * math.cos(ang), r * math.sin(ang))
    for _ in range(40):
        f = z**d - z - 1
        df = d * (z ** (d - 1)) - 1
        z -= f / df
    xr = int(round(z.real * S))
    xi = int(round(z.imag * S))
    for _ in range(4):
        z_pt = ((xr, xr), (xi, xi))
        zd1 = civ_pow(z_pt, d - 1)
        zd = civ_mul(zd1, z_pt)
        f_iv = civ_sub(civ_sub(zd, z_pt), ((S, S), (0, 0)))
        df_iv = civ_sub(
            ((zd1[0][0] * d, zd1[0][1] * d), (zd1[1][0] * d, zd1[1][1] * d)),
            ((S, S), (0, 0)),
        )
        fr = (f_iv[0][0] + f_iv[0][1]) >> 1
        fi = (f_iv[1][0] + f_iv[1][1]) >> 1
        dfr = (df_iv[0][0] + df_iv[0][1]) >> 1
        dfi = (df_iv[1][0] + df_iv[1][1]) >> 1
        den = (dfr * dfr + dfi * dfi) >> P
        xr -= (fr * dfr + fi * dfi) // den
        xi -= (fi * dfr - fr * dfi) // den
    return xr, xi


def certify_gamma(d: int):
    xr, xi = newton_gamma_point(d)
    z_pt = ((xr, xr), (xi, xi))
    r_int = 1 << (P - 60)
    r_iv = (r_int, r_int)
    assert xi > r_int, f"gamma not in upper half-plane at d={d}"

    zd1 = civ_pow(z_pt, d - 1)
    zd = civ_mul(zd1, z_pt)
    f_iv = civ_sub(civ_sub(zd, z_pt), ((S, S), (0, 0)))
    df_iv = civ_sub(
        ((zd1[0][0] * d, zd1[0][1] * d), (zd1[1][0] * d, zd1[1][1] * d)),
        ((S, S), (0, 0)),
    )

    f_abs_hi = max(abs(f_iv[0][0]), abs(f_iv[0][1])) + max(
        abs(f_iv[1][0]), abs(f_iv[1][1])
    )
    df_abs = iv_sqrt(civ_abs2(df_iv))
    lhs = iv_mul(df_abs, r_iv)

    z_abs = iv_sqrt(civ_abs2(z_pt))
    r2_iv = iv_sqr(r_iv)
    zpr_pow = iv_pow(iv_add(z_abs, r_iv), d - 2)
    tail_hi = ((d * (d - 1)) // 2) * iv_mul(r2_iv, zpr_pow)[1]
    assert lhs[0] > f_abs_hi + tail_hi, f"Rouche check failed at d={d}"
    return ((xr - r_int, xr + r_int), (xi - r_int, xi + r_int))


def verify_all(d_max: int = 499) -> None:
    for d in range(4, d_max + 1):
        b_iv = certify_beta(d)
        g_civ = certify_gamma(d)
        g_abs2 = civ_abs2(g_civ)
        assert g_abs2[0] > S, f"|gamma_d| <= 1 at d={d}"

        c_civ = g_civ
        q_iv = b_iv
        k = 1
        while True:
            c_abs2 = civ_abs2(c_civ)
            v = 2 * c_abs2[0] - 3 * S
            if v > 0 and v * v > 5 * S * S:
                break

            c_abs = iv_sqrt(c_abs2)
            assert c_abs[0] > S, f"|c| <= 1 at d={d}, k={k}"
            c_abs_m1 = iv_sub(c_abs, (S, S))

            if d <= 5:
                q_fl = q_iv[0] >> P
                assert q_fl == (q_iv[1] >> P), f"ambiguous floor(q) at d={d}, k={k}"
                thresh = iv_div((q_fl << P, q_fl << P), c_abs_m1)
                thresh2 = iv_sqr(thresh)

                xc_civ = ((S, S), (0, 0))
                x_iv = (S, S)
                hit = False
                for _ in range(1, 50):
                    qx = iv_mul(q_iv, x_iv)
                    dig = qx[0] >> P
                    assert dig == (qx[1] >> P), f"ambiguous digit at d={d}, k={k}"
                    x_iv = iv_sub(qx, iv_from_int(dig))
                    xc_civ = civ_sub(civ_mul(c_civ, xc_civ), (iv_from_int(dig), (0, 0)))
                    if civ_abs2(xc_civ)[0] > thresh2[1]:
                        hit = True
                        break
                assert hit, f"Akiyama orbit failed at d={d}, k={k}"
            else:
                assert q_iv[0] >= S and q_iv[1] < (2 << P), f"q not in [1,2) at d={d}, k={k}"
                q_m1 = iv_sub(q_iv, (S, S))
                m0 = 2
                pow_q = q_iv
                while True:
                    prod = iv_mul(pow_q, q_m1)
                    if prod[0] > S:
                        break
                    assert prod[1] < S, f"ambiguous m0 at d={d}, k={k}, m0={m0}"
                    m0 += 1
                    pow_q = iv_mul(pow_q, q_iv)

                c_m0m2 = civ_pow(c_civ, m0 - 2)
                c_2m0m3 = civ_mul(c_m0m2, civ_mul(c_m0m2, c_civ))
                c_2m0m2 = civ_mul(c_2m0m3, c_civ)
                expr = civ_sub(civ_sub(c_2m0m2, c_2m0m3), c_m0m2)
                lhs_prod = iv_mul(civ_abs2(expr), iv_sqr(c_abs_m1))
                assert lhs_prod[0] > S, f"Akiyama block failed at d={d}, k={k}, m0={m0}"

            k += 1
            c_civ = civ_mul(c_civ, g_civ)
            q_iv = iv_mul(q_iv, b_iv)


if __name__ == "__main__":
    try:
        verify_all(499)
        print("PASS")
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)

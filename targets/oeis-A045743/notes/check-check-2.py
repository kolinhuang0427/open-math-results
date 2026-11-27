"""Independent exact-arithmetic checker for targets/oeis-A045743/PROOF.md."""

from math import comb
import sys
import sympy as sp


def a_closed(n: int) -> int:
    assert n >= 2
    s = 0
    for i in range((n - 2) // 2 + 1):
        s += comb(n - 2 + i, i) * comb(3 * n - 3 - i, n - 2 - 2 * i)
    assert s % (n - 1) == 0
    return s // (n - 1)


def s_mul(A: list[int], B: list[int], N: int) -> list[int]:
    C = [0] * N
    for i in range(min(N, len(A))):
        if A[i] == 0:
            continue
        for j in range(min(N - i, len(B))):
            C[i + j] += A[i] * B[j]
    return C


def s_inv_int(A: list[int], N: int) -> list[int]:
    assert A[0] in (1, -1)
    inv0 = A[0]
    B = [0] * N
    B[0] = inv0
    for n in range(1, N):
        s = sum(A[k] * B[n - k] for k in range(1, min(n + 1, len(A))))
        B[n] = -s * inv0
    return B


def s_pow(A: list[int], e: int, N: int) -> list[int]:
    res = [0] * N
    res[0] = 1
    base = list(A[:N]) + [0] * max(0, N - len(A))
    while e > 0:
        if e & 1:
            res = s_mul(res, base, N)
        e >>= 1
        if e:
            base = s_mul(base, base, N)
    return res


def s_dx(A: list[int]) -> list[int]:
    return [i * A[i] for i in range(1, len(A))]


def main():
    # 0. OEIS A045743 verbatim data (n=2..22) and closed form (n=2..50)
    oeis_data = [
        1, 3, 13, 66, 367, 2164, 13293, 84157, 545270, 3598244, 24100375,
        163416748, 1119592052, 7738412716, 53894849437, 377851866954,
        2664570714233, 18887568709788, 134501247038230, 961774761388430,
        6903072966224220,
    ]
    n_max = 50
    a_vals = {n: a_closed(n) for n in range(2, n_max + 1)}
    assert [a_vals[n] for n in range(2, 2 + len(oeis_data))] == oeis_data

    # 1. Step 1: Lagrange inversion & P(x, y(x)) = 0
    N = 32
    # Phi(t) = (1+t)^4 / (1 + t - t^2)
    num_phi = [1, 4, 6, 4, 1] + [0] * (N - 5)
    den_phi = [1, 1, -1] + [0] * (N - 3)
    phi = s_mul(num_phi, s_inv_int(den_phi, N), N)
    phi_pow = [1] + [0] * (N - 1)
    for m in range(1, 26):
        phi_pow = s_mul(phi_pow, phi, N)
        assert phi_pow[m - 1] == m * a_vals[m + 1], f"Lagrange coeff failed at m={m}"

    # G(x) = sum_{m>=1} a(m+1) x^m
    G = [0] + [a_vals[m + 1] for m in range(1, N)]
    G2 = s_mul(G, G, N)
    lhs_G = s_mul(G, [1 + G[i] - G2[i] if i == 0 else G[i] - G2[i] for i in range(N)], N)
    one_plus_G = [1 + G[0]] + G[1:]
    rhs_G = [0] + s_pow(one_plus_G, 4, N - 1)
    assert lhs_G == rhs_G, "G(x) functional equation failed"

    # y(x) = x * G(x), check P(x, y(x)) == 0
    y_ser = [0, 0] + [a_vals[n] for n in range(2, N)]
    y_ser = y_ser[:N]

    x, y = sp.symbols("x y")
    P_expr = x**4 + 4 * x**3 * y + 6 * x**2 * y**2 - x**2 * y + 4 * x * y**3 - x * y**2 + y**4 + y**3

    def eval_poly_series(expr, ser, deg_limit):
        poly_y = sp.Poly(expr, y)
        res = [0] * deg_limit
        y_pow = [1] + [0] * (deg_limit - 1)
        for deg in range(poly_y.degree() + 1):
            c_x = sp.Poly(poly_y.nth(deg), x)
            c_ser = [0] * deg_limit
            for (d,), val in c_x.terms():
                if d < deg_limit:
                    c_ser[d] = int(val)
            term = s_mul(c_ser, y_pow, deg_limit)
            for i in range(deg_limit):
                res[i] += term[i]
            y_pow = s_mul(y_pow, ser, deg_limit)
        return res

    assert eval_poly_series(P_expr, y_ser, N) == [0] * N, "P(x, y(x)) != 0"

    # 2. Step 2: N_1..N_4, exact polynomial division Q / P in Z[x, y], and ODE for y(x)
    Px = sp.diff(P_expr, x)
    Py = sp.diff(P_expr, y)
    N_polys = [None, -Px]
    for k in (1, 2, 3):
        Nk = N_polys[k]
        N_next = (Py * sp.diff(Nk, x) + N_polys[1] * sp.diff(Nk, y)) * Py - (2 * k - 1) * Nk * (
            Py * sp.diff(Py, x) + N_polys[1] * sp.diff(Py, y)
        )
        N_polys.append(sp.expand(N_next))

    # Check P_y^{2k-1} y^{(k)} = N_k(x, y(x)) in Z[[x]] for k=1..4
    M_ser = N - 4
    Py_ser = eval_poly_series(Py, y_ser, M_ser)
    yk = list(y_ser)
    for k in range(1, 5):
        yk = s_dx(yk)
        lhs_k = s_mul(s_pow(Py_ser, 2 * k - 1, M_ser), yk[:M_ser], M_ser)
        rhs_k = eval_poly_series(N_polys[k], y_ser, M_ser)
        assert lhs_k == rhs_k, f"N_{k} series identity failed"

    p_inhom = 52437120 * x**5 - 222762936 * x**4 - 86483718 * x**3
    p0 = -72 * x**3 * (225648 * x - 3034829)
    p1 = 48 * x**3 * (1430912 * x**2 - 9108520 * x - 2939805)
    p2 = 48 * x**3 * (31050464 * x**3 - 58671498 * x**2 - 54421082 * x + 516693)
    p3 = x**3 * (1910439936 * x**4 - 813515264 * x**3 - 3673122304 * x**2 + 140653072 * x + 2048955)
    p4 = 2 * x**4 * (753968 * x - 676909) * (256 * x**3 + 512 * x**2 - 32 * x - 5)
    pk = [p0, p1, p2, p3, p4]

    Q_expr = (
        Py**7 * (p_inhom + p0 * y)
        + Py**6 * p1 * N_polys[1]
        + Py**4 * p2 * N_polys[2]
        + Py**2 * p3 * N_polys[3]
        + p4 * N_polys[4]
    )
    Q_poly = sp.Poly(Q_expr, y, x, domain=sp.ZZ)
    P_poly = sp.Poly(P_expr, y, x, domain=sp.ZZ)
    _, rem = sp.div(Q_poly, P_poly, domain=sp.ZZ)
    assert rem.is_zero, "P(x,y) does not divide Q(x,y) in Z[x,y]"

    # Check ODE directly on y(x)
    ode_series = [0] * M_ser
    p_inhom_poly = sp.Poly(p_inhom, x, domain=sp.ZZ)
    for (d,), val in p_inhom_poly.terms():
        ode_series[d] += int(val)
    yk = list(y_ser)
    for k in range(5):
        pk_ser = [0] * M_ser
        for (d,), val in sp.Poly(pk[k], x, domain=sp.ZZ).terms():
            pk_ser[d] = int(val)
        term = s_mul(pk_ser, yk[:M_ser], M_ser)
        for i in range(M_ser):
            ode_series[i] += term[i]
        yk = s_dx(yk)
    assert ode_series == [0] * M_ser, "ODE for y(x) failed"

    # 3. Step 3: Exact coefficient extraction in Z[n] vs TARGET.md C_0..C_4
    n_sym = sp.Symbol("n")
    assert sp.Poly(p_inhom, x).degree() == 5
    C_extracted = [sp.Integer(0)] * 5
    for k in range(5):
        pk_poly = sp.Poly(pk[k], x, domain=sp.ZZ)
        for (d,), c_val in pk_poly.terms():
            j = d - k
            assert 0 <= j <= 4, f"Out-of-range shift d-k={j} in p_{k}"
            ff = sp.Integer(1)
            for i in range(k):
                ff *= (n_sym - j - i)
            C_extracted[j] += int(c_val) * ff

    C_target = [
        5 * n_sym * (n_sym - 1) * (n_sym - 2) * (1353818 * n_sym - 3651663),
        16 * (n_sym - 1) * (n_sym - 2) * (2236406 * n_sym**2 - 6864025 * n_sym + 2014500),
        -16 * (n_sym - 2) * (46338048 * n_sym**3 - 326486432 * n_sym**2 + 734160494 * n_sym - 506411475),
        8 * (2 * n_sym - 7) * (26592864 * n_sym**3 - 436441232 * n_sym**2 + 2071128458 * n_sym - 3030735075),
        128 * (94246 * n_sym - 334675) * (4 * n_sym - 19) * (2 * n_sym - 9) * (4 * n_sym - 17),
    ]
    for j in range(5):
        assert sp.expand(C_extracted[j] - C_target[j]) == 0, f"C_{j}(n) mismatch"

    # Verify recurrence directly on a_vals for 6 <= n <= 50
    for n in range(6, n_max + 1):
        c0_val = int(C_target[0].subs(n_sym, n))
        assert c0_val > 0
        lhs = sum(int(C_target[j].subs(n_sym, n)) * a_vals[n - j] for j in range(5))
        assert lhs == 0, f"Recurrence failed at n={n}"

    print(f"PASS (OEIS data n=2..22, Lagrange/P(x,y)=0, exact Z[x,y] div Q/P=R, Z[n] C_0..C_4 match, recurrence n=6..{n_max})")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)

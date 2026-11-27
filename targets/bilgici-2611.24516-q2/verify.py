"""Exact verification for bilgici-2611.24516-q2 over F_19[[y]]."""

P_MOD = 19
Y_DEG = 19
Q_DEG = P_MOD * Y_DEG


def inv_mod_19(x):
    x_mod = x % P_MOD
    if x_mod == 0:
        raise ZeroDivisionError("0 has no inverse mod 19")
    return pow(x_mod, P_MOD - 2, P_MOD)


def mul_series(a, b, deg):
    res = [0] * deg
    for i in range(deg):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(deg - i):
            res[i + j] = (res[i + j] + ai * b[j]) % P_MOD
    return res


def pow_series(base, exp, deg):
    res = [0] * deg
    res[0] = 1
    e = exp % P_MOD
    b = list(base)
    while e > 0:
        if e & 1:
            res = mul_series(res, b, deg)
        e >>= 1
        if e:
            b = mul_series(b, b, deg)
    return res


def shift_series(a, k, deg):
    if k >= deg:
        return [0] * deg
    return ([0] * k + a[: deg - k])


def add_scaled(a, ca, b, cb, deg):
    return [(ca * a[i] + cb * b[i]) % P_MOD for i in range(deg)]


def rho(x):
    r = x % P_MOD
    alt = P_MOD - r
    return r if r <= alt else alt


def main():
    # 1. Build P_1, ..., P_9 in F_19[[y]] mod y^19
    P = {}
    for a in range(1, 10):
        ser = [0] * Y_DEG
        ser[0] = 1
        for e in (a, P_MOD - a):
            for k in range(Y_DEG - 1, e - 1, -1):
                ser[k] = (ser[k] - ser[k - e]) % P_MOD
        P[a] = ser

    def G(A, B):
        return mul_series(
            mul_series(P[A], P[B], Y_DEG),
            mul_series(P[rho(A + B)], P[B - A], Y_DEG),
            Y_DEG,
        )

    # 2. Exact Table 1 (tab:B) definitions from arXiv:2611.24516v1
    B_tab = {
        0: add_scaled(G(3, 9), 1, shift_series(G(4, 6), 1, Y_DEG), 4, Y_DEG),
        1: add_scaled(G(4, 9), 9, shift_series(G(2, 6), 1, Y_DEG), 7, Y_DEG),
        2: add_scaled(G(2, 9), -3, shift_series(G(6, 7), 1, Y_DEG), 4, Y_DEG),
        3: add_scaled(G(3, 8), 8, shift_series(G(7, 9), 1, Y_DEG), -6, Y_DEG),
        4: add_scaled(G(4, 8), 9, shift_series(G(5, 6), 1, Y_DEG), 2, Y_DEG),
        5: add_scaled(G(2, 8), 8, G(5, 9), 2, Y_DEG),
        6: add_scaled(shift_series(G(1, 6), 1, Y_DEG), 3, shift_series(G(7, 8), 1, Y_DEG), -7, Y_DEG),
        7: add_scaled(G(1, 9), 6, shift_series(G(3, 4), 2, Y_DEG), 5, Y_DEG),
        8: add_scaled(G(5, 8), 6, shift_series(G(2, 3), 3, Y_DEG), -5, Y_DEG),
        9: add_scaled(G(3, 7), 7, shift_series(G(2, 4), 2, Y_DEG), -3, Y_DEG),
        10: add_scaled(G(1, 8), -8, G(4, 7), -2, Y_DEG),
        11: add_scaled(G(2, 7), 9, shift_series(G(3, 5), 1, Y_DEG), 2, Y_DEG),
        12: add_scaled(G(6, 9), -6, shift_series(G(4, 5), 1, Y_DEG), 8, Y_DEG),
        13: add_scaled(shift_series(G(2, 5), 1, Y_DEG), 3, shift_series(G(1, 3), 3, Y_DEG), 4, Y_DEG),
        14: add_scaled(G(5, 7), 7, shift_series(G(1, 4), 2, Y_DEG), 9, Y_DEG),
        15: add_scaled(G(6, 8), -4, shift_series(G(1, 2), 4, Y_DEG), -1, Y_DEG),
        16: add_scaled(G(1, 7), -1, shift_series(G(8, 9), 1, Y_DEG), 5, Y_DEG),
        17: [0] * Y_DEG,
        18: add_scaled(G(3, 6), -5, shift_series(G(1, 5), 1, Y_DEG), 1, Y_DEG),
    }

    # 3. Direct cross-check against f(q)^10 mod (19, q^361) (since P_0 = 1 + O(y^19) = 1 + O(q^361))
    f1 = [0] * Q_DEG
    f1[0] = 1
    for n in range(1, Q_DEG):
        for k in range(Q_DEG - 1, n - 1, -1):
            f1[k] = (f1[k] - f1[k - n]) % P_MOD
    f10 = pow_series(f1, 10, Q_DEG)

    for r in range(P_MOD):
        comp = [f10[P_MOD * k + r] for k in range(Y_DEG)]
        assert comp == B_tab[r], f"Table B mismatch at r={r}"

    # 4. Check logarithmic-derivative obstruction and direct product mismatch for all 18 nonzero rows
    for r in range(P_MOD):
        if r == 17:
            continue
        ser = B_tab[r]
        v = next(i for i in range(Y_DEG) if ser[i] != 0)
        c = ser[v]
        ic = inv_mod_19(c)
        f = [((ser[v + i] * ic) % P_MOD) if v + i < Y_DEG else 0 for i in range(Y_DEG)]

        # Compute d_1, ..., d_11 via Newton's identity
        d = [0] * 12
        for n in range(1, 12):
            s = sum(d[k] * f[n - k] for k in range(1, n)) % P_MOD
            d[n] = (n * f[n] - s) % P_MOD

        # Unique forced exponents e_1, ..., e_9 mod 19
        ae = [0] * 10
        e = [0] * 10
        for a in range(1, 10):
            s = sum(ae[m] for m in range(1, a) if a % m == 0) % P_MOD
            ae[a] = (-d[a] - s) % P_MOD
            e[a] = (ae[a] * inv_mod_19(a)) % P_MOD

        d10_pred = (-(ae[1] + ae[2] + ae[5]) - 10 * e[9]) % P_MOD
        d11_pred = (-ae[1] - 11 * e[8]) % P_MOD

        if r != 9:
            assert d[10] != d10_pred, f"Unexpected d10 match at r={r}"
        assert d[11] != d11_pred, f"Unexpected d11 match at r={r}"

        # Direct polynomial check: prod_{a=1}^9 P_a^{e_a} mod (19, y^12)
        prod = [0] * Y_DEG
        prod[0] = 1
        for a in range(1, 10):
            if e[a] != 0:
                prod = mul_series(prod, pow_series(P[a], e[a], Y_DEG), Y_DEG)
        assert prod[:10] == f[:10], f"Prefix mismatch at r={r}"
        assert prod[:12] != f[:12], f"Full match up to y^11 at r={r}"

    print("PASS")


if __name__ == "__main__":
    main()

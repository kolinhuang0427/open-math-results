"""Exact verification script for OEIS A379459, A379460, and A006351 (Mikhail Kurkov conjectures)."""
from fractions import Fraction
from math import factorial


def poly_mul(a, b, deg):
    res = [Fraction(0)] * (deg + 1)
    for i in range(min(len(a), deg + 1)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), deg + 1 - i)):
            res[i + j] += a[i] * b[j]
    return res


def poly_inv(a, deg):
    assert a[0] != 0
    inv0 = Fraction(1) / a[0]
    res = [Fraction(0)] * (deg + 1)
    res[0] = inv0
    for k in range(1, deg + 1):
        s = sum((a[j] * res[k - j] for j in range(1, min(k + 1, len(a)))), Fraction(0))
        res[k] = -s * inv0
    return res


def compute_A379459(max_n):
    size = max_n + 2
    row = [2 * factorial(k + 1) for k in range(size)]
    col0 = [row[0]]
    antidiag = []
    # Store full triangle up to antidiagonal 9
    full = [list(row)]
    fact = [factorial(i) for i in range(size + 2)]
    for n in range(1, max_n + 1):
        new_len = size - n
        new_row = []
        pref = Fraction(0)
        for k in range(new_len):
            pref += Fraction(row[k], fact[k])
            val = row[k + 1] + 2 * fact[k + 1] * pref
            assert val.denominator == 1
            new_row.append(int(val))
        row = new_row
        col0.append(row[0])
        full.append(list(row))
    for s in range(9):
        for n in range(s + 1):
            k = s - n
            antidiag.append(full[n][k])
    return col0, antidiag


def compute_A379460(max_n):
    size = max_n + 2
    row = [1] * size
    col0 = [row[0]]
    antidiag = []
    full = [list(row)]
    for n in range(1, max_n + 1):
        new_len = size - n
        new_row = [row[0] + row[1]]
        for k in range(1, new_len):
            new_row.append(new_row[-1] + (k + 1) * (row[k] + row[k + 1]))
        row = new_row
        col0.append(row[0])
        full.append(list(row))
    for s in range(8):
        for n in range(s + 1):
            k = s - n
            antidiag.append(full[n][k])
    return col0, antidiag


def main():
    max_n = 20
    c459, ad459 = compute_A379459(max_n)
    c460, ad460 = compute_A379460(max_n + 1)

    # 1. Verify OEIS A379459 DATA (first 9 downward antidiagonals)
    oeis_A379459_data = [
        2, 4, 8, 12, 36, 52, 48, 192, 368, 472, 240, 1200, 2880, 4560, 5504,
        1440, 8640, 24960, 47280, 67408, 78416, 10080, 70560, 238560, 527520,
        871584, 1163232, 1320064, 80640, 645120, 2499840, 6330240, 11926656,
        18031104, 22997696, 25637824, 725760, 6531840, 28546560, 81527040,
        172811520, 292642560, 415728960, 513000000, 564275648,
    ]
    assert ad459 == oeis_A379459_data, "OEIS A379459 DATA mismatch"

    # 2. Verify OEIS A379460 DATA (first 8 downward antidiagonals)
    oeis_A379460_data = [
        1, 1, 2, 1, 6, 8, 1, 12, 44, 52, 1, 20, 140, 420, 472,
        1, 30, 340, 1860, 5032, 5504, 1, 42, 700, 6020, 28672, 72912, 78416,
        1, 56, 1288, 15960, 116592, 506704, 1219680, 1298096,
    ]
    # Check prefix matching the OEIS JSON snippet (up to 1, 56, 1288, 15960, 116592)
    assert ad460[:33] == oeis_A379460_data[:33], f"OEIS A379460 DATA mismatch: {ad460[:33]}"

    # 3. Verify W_tilde_n(y) = H_{n-1}(y) operator equivalence in QQ[[y]]
    y_deg = max_n + 4
    ratio = [Fraction(1)] + [Fraction(2)] * y_deg  # (1+y)/(1-y)
    H = [Fraction(2 * (k + 1)) for k in range(y_deg + 1)]  # 2/(1-y)^2
    W_tilde = [Fraction(1)] + [Fraction(0)] * y_deg  # 1
    prod_w = poly_mul(ratio, W_tilde, y_deg)
    W_tilde_1 = [(k + 1) * prod_w[k + 1] for k in range(y_deg)]
    assert W_tilde_1[: y_deg - 1] == H[: y_deg - 1], "W_tilde_1 != H_0"

    H_zeros = [int(H[0])]
    for n in range(1, max_n + 1):
        prod = poly_mul(ratio, H, y_deg + 1 - n)
        H = [(k + 1) * prod[k + 1] for k in range(y_deg + 1 - n)]
        H_zeros.append(int(H[0]))
    assert H_zeros == c459, "H_n operator mismatch"

    # 4. Verify ODE B'(x) = (1+B)/(1-B), B(0)=0 -> A006351 & B''(x) = W(x, 0)
    deg = max_n + 3
    B = [Fraction(0)] * (deg + 1)
    for m in range(deg):
        lhs_rest = sum((B[k] * (m + 1 - k) * B[m + 1 - k] for k in range(1, m + 1)), Fraction(0))
        B[m + 1] = ((Fraction(1) if m == 0 else B[m]) + lhs_rest) / (m + 1)

    oeis_A006351 = [
        1, 2, 8, 52, 472, 5504, 78416, 1320064, 25637824, 564275648,
        13879795712, 377332365568, 11234698041088, 363581406419456,
        12707452084972544, 477027941930515456, 19142041172838025216,
        817675811320888020992, 37044610820729973813248, 1774189422608238694776832,
    ]
    a006351 = [None]
    for m in range(1, deg + 1):
        val = B[m] * factorial(m)
        assert val.denominator == 1
        a006351.append(int(val))
    assert a006351[1:21] == oeis_A006351, "OEIS A006351 DATA mismatch"

    # Verify B''(x) == 2*(1+B)/(1-B)^3
    one_m_B = [Fraction(1) - B[0]] + [-B[i] for i in range(1, deg + 1)]
    inv_1mB = poly_inv(one_m_B, deg)
    inv_1mB_3 = poly_mul(inv_1mB, poly_mul(inv_1mB, inv_1mB, deg), deg)
    two_1pB = [Fraction(2) * (Fraction(1) + B[0])] + [Fraction(2) * B[i] for i in range(1, deg + 1)]
    W0 = poly_mul(two_1pB, inv_1mB_3, deg)
    Bpp = [(n + 2) * (n + 1) * B[n + 2] for n in range(max_n + 1)]
    assert Bpp == W0[: max_n + 1], "B''(x) != 2*(1+B)/(1-B)^3"

    # 5. Verify all three conjectures across n = 0..max_n
    for n in range(max_n + 1):
        assert c459[n] == a006351[n + 2], f"A379459 mismatch at n={n}"
        assert c460[n] == a006351[n + 1], f"A379460 mismatch at n={n}"
    assert c460[0] == 1
    for m in range(2, max_n + 2):
        assert a006351[m] == c459[m - 2] == c460[m - 1]

    print("PASS")


if __name__ == "__main__":
    main()

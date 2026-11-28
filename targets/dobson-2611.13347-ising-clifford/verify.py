#!/usr/bin/env python3
"""Exact-arithmetic verification for targets/dobson-2611.13347-ising-clifford/PROOF.md.

Uses exact arithmetic in Q(zeta_16) represented as 8-tuples of Fractions
(c_0, ..., c_7) corresponding to sum_{k=0}^7 c_k * zeta_16^k with zeta_16^8 = -1.
Zero floating-point operations are used anywhere.
"""

from fractions import Fraction
import itertools


class Z16:
    """Exact element of Q(zeta_16), where zeta_16 = exp(i*pi/8), zeta_16^8 = -1."""
    __slots__ = ("c",)

    def __init__(self, coeffs=None):
        if coeffs is None:
            self.c = (Fraction(0),) * 8
        else:
            self.c = tuple(Fraction(x) for x in coeffs)
            assert len(self.c) == 8

    @classmethod
    def from_int(cls, n):
        return cls((n, 0, 0, 0, 0, 0, 0, 0))

    @classmethod
    def zeta_pow(cls, k):
        k = k % 16
        sign = 1
        if k >= 8:
            k -= 8
            sign = -1
        arr = [0] * 8
        arr[k] = sign
        return cls(arr)

    def __eq__(self, other):
        return isinstance(other, Z16) and self.c == other.c

    def __add__(self, other):
        return Z16([a + b for a, b in zip(self.c, other.c)])

    def __sub__(self, other):
        return Z16([a - b for a, b in zip(self.c, other.c)])

    def __neg__(self):
        return Z16([-a for a in self.c])

    def __mul__(self, other):
        res = [Fraction(0)] * 8
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(other.c):
                if b == 0:
                    continue
                idx = i + j
                if idx >= 8:
                    res[idx - 8] -= a * b
                else:
                    res[idx] += a * b
        return Z16(res)

    def conj(self):
        # conj(zeta_16^k) = zeta_16^{-k}
        res = Z16.from_int(0)
        for k, a in enumerate(self.c):
            if a != 0:
                res = res + Z16.from_int(1).scale(a) * Z16.zeta_pow(-k)
        return res

    def scale(self, q):
        return Z16([a * Fraction(q) for a in self.c])


ZERO = Z16.from_int(0)
ONE = Z16.from_int(1)
HALF = Z16((Fraction(1, 2), 0, 0, 0, 0, 0, 0, 0))
I_UNIT = Z16.zeta_pow(4)          # i = zeta_16^4
INV_SQRT2 = Z16((0, 0, Fraction(1, 2), 0, 0, 0, Fraction(-1, 2), 0))  # (zeta^2 - zeta^6)/2 = 1/sqrt(2)
ZETA_M1 = Z16.zeta_pow(-1)        # e^{-i pi / 8}
ZETA_P1 = Z16.zeta_pow(1)         # e^{+i pi / 8}
ZETA_P2 = Z16.zeta_pow(2)         # e^{+i pi / 4}


def mat_mul(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    out = [[ZERO for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(p):
            aik = A[i][k]
            if aik == ZERO:
                continue
            for j in range(m):
                out[i][j] = out[i][j] + aik * B[k][j]
    return out


def mat_dag(A):
    n = len(A)
    m = len(A[0])
    return [[A[j][i].conj() for j in range(n)] for i in range(m)]


def mat_scale(s, A):
    return [[s * x for x in row] for row in A]


def mat_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_kron(A, B):
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    out = [[ZERO for _ in range(ca * cb)] for _ in range(ra * rb)]
    for ia in range(ra):
        for ja in range(ca):
            a = A[ia][ja]
            if a == ZERO:
                continue
            for ib in range(rb):
                for jb in range(cb):
                    out[ia * rb + ib][ja * cb + jb] = a * B[ib][jb]
    return out


def mat_eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def kron_all(mats):
    res = mats[0]
    for m in mats[1:]:
        res = mat_kron(res, m)
    return res


def op_on(U, q, n):
    return kron_all([U if i == q else I2 for i in range(n)])


def apply_mat_vec(A, v):
    return [sum((row[j] * v[j] for j in range(len(v))), ZERO) for row in A]


def vec_kron(u, v):
    return [a * b for a in u for b in v]


I2 = [[ONE, ZERO], [ZERO, ONE]]
X2 = [[ZERO, ONE], [ONE, ZERO]]
Z2 = [[ONE, ZERO], [ZERO, -ONE]]
Y2 = [[ZERO, -I_UNIT], [I_UNIT, ZERO]]
S2 = [[ONE, ZERO], [ZERO, I_UNIT]]
H2 = mat_scale(INV_SQRT2, [[ONE, ONE], [ONE, -ONE]])
SQRT_X2 = mat_scale(HALF, [[ONE + I_UNIT, ONE - I_UNIT], [ONE - I_UNIT, ONE + I_UNIT]])
CZ4 = [
    [ONE, ZERO, ZERO, ZERO],
    [ZERO, ONE, ZERO, ZERO],
    [ZERO, ZERO, ONE, ZERO],
    [ZERO, ZERO, ZERO, -ONE],
]
CNOT4 = [
    [ONE, ZERO, ZERO, ZERO],
    [ZERO, ONE, ZERO, ZERO],
    [ZERO, ZERO, ZERO, ONE],
    [ZERO, ZERO, ONE, ZERO],
]


def braid_generators(m):
    """Return [B_0, ..., B_{2m}] as 2^m x 2^m exact matrices over Q(zeta_16)."""
    gens = []
    gens.append(mat_scale(ZETA_M1, op_on(S2, 0, m)))
    for j in range(m):
        gens.append(mat_scale(ZETA_M1, op_on(SQRT_X2, j, m)))
        if j < m - 1:
            ss_cz = mat_mul(mat_kron(S2, S2), CZ4)
            mats = [I2] * m
            mats[j] = ss_cz
            del mats[j + 1]
            gens.append(mat_scale(ZETA_M1, kron_all(mats)))
    gens.append(mat_scale(ZETA_M1, op_on(S2, m - 1, m)))
    return gens


def pauli_mat(x_bits, z_bits, m):
    mats = []
    for j in range(m):
        xb = (x_bits >> j) & 1
        zb = (z_bits >> j) & 1
        if xb == 0 and zb == 0:
            mats.append(I2)
        elif xb == 1 and zb == 0:
            mats.append(X2)
        elif xb == 0 and zb == 1:
            mats.append(Z2)
        else:
            mats.append(Y2)
    return kron_all(mats)


def pauli_mask(x_bits, z_bits, m):
    mask = 0
    for j in range(m):
        if (x_bits >> j) & 1:
            mask ^= (1 << (2 * j + 1)) ^ (1 << (2 * j + 2))
        if (z_bits >> j) & 1:
            mask ^= (1 << (2 * j + 2)) - 1
    return mask


def min_wt_gamma(mask, m):
    w = mask.bit_count()
    return min(w, 2 * m + 2 - w)


def verify_section_1():
    # Basic ring identity check
    assert INV_SQRT2 * INV_SQRT2 == HALF
    assert I_UNIT * I_UNIT == -ONE
    assert ZETA_P1 * ZETA_M1 == ONE

    for m in (2, 3, 4):
        Bs = braid_generators(m)
        assert len(Bs) == 2 * m + 1
        # Check unitarity and braid relations
        eye = mat_eye(1 << m)
        for k, B in enumerate(Bs):
            assert mat_mul(B, mat_dag(B)) == eye, f"Non-unitary B_{k} for m={m}"
        for k in range(len(Bs) - 1):
            lhs = mat_mul(Bs[k], mat_mul(Bs[k + 1], Bs[k]))
            rhs = mat_mul(Bs[k + 1], mat_mul(Bs[k], Bs[k + 1]))
            assert lhs == rhs, f"Braid relation failed at k={k}, m={m}"
            for l in range(k + 2, len(Bs)):
                assert mat_mul(Bs[k], Bs[l]) == mat_mul(Bs[l], Bs[k]), f"Comm failed {k},{l}"

        # Check B_{r-1} = e^{i pi/8} (I - i P_r) / sqrt(2) and P_r^2 = I
        Ps = [pauli_mat(0, 1, m)]
        for j in range(m):
            Ps.append(pauli_mat(1 << j, 0, m))
            if j < m - 1:
                Ps.append(pauli_mat(0, (1 << j) | (1 << (j + 1)), m))
        Ps.append(pauli_mat(0, 1 << (m - 1), m))
        for r, P in enumerate(Ps):
            rhs = mat_scale(ZETA_P1 * INV_SQRT2, mat_add(eye, mat_scale(-I_UNIT, P)))
            assert Bs[r] == rhs, f"Exp formula failed at r={r}, m={m}"

        # Check Lemma 1.1(1): conjugation on every pair Gamma_{a,b} = -i gamma_a gamma_b (0 <= a < b <= 2m+1)
        # where Gamma_{a,b} = i^{b - a - 1} P_{a+1} ... P_b (verified by product of (-i gamma_k gamma_{k+1}))
        gamma_pair = {}
        for a in range(2 * m + 2):
            for b in range(a + 1, 2 * m + 2):
                prod = eye
                for k in range(a, b):
                    prod = mat_mul(prod, Ps[k])
                # Wait: prod_{k=a}^{b-1} (-i gamma_k gamma_{k+1}) = (-i)^{b-a} * (gamma_a gamma_b)
                # since intermediate gamma_k^2 = I cancel in pairs!
                # So -i gamma_a gamma_b = i^{b - a - 1} * prod!
                coef = ONE
                for _ in range(b - a - 1):
                    coef = coef * I_UNIT
                gamma_pair[(a, b)] = mat_scale(coef, prod)
                assert mat_mul(gamma_pair[(a, b)], gamma_pair[(a, b)]) == eye

        # Verify conjugation of Gamma_{a,b} by every B_{r-1}:
        for r in range(1, 2 * m + 2):
            B = Bs[r - 1]
            Bd = mat_dag(B)
            for a in range(2 * m + 2):
                for b in range(a + 1, 2 * m + 2):
                    conj_mat = mat_mul(B, mat_mul(gamma_pair[(a, b)], Bd))
                    # Under B_{r-1}: r-1 -> +r, r -> -(r-1), others unchanged
                    def map_idx(idx):
                        if idx == r - 1:
                            return r, 1
                        if idx == r:
                            return r - 1, -1
                        return idx, 1
                    na, sa = map_idx(a)
                    nb, sb = map_idx(b)
                    sign = sa * sb
                    if na > nb:
                        na, nb = nb, na
                        sign = -sign
                    expected = mat_scale(Z16.from_int(sign), gamma_pair[(na, nb)])
                    assert conj_mat == expected, f"Lemma 1.1(1) failed for r={r}, ({a},{b})"

    # Verify Lemma 1.1(3) exhaustively for all 4^m Paulis for m = 3, 4, 5
    for m in (3, 4, 5):
        for xb in range(1 << m):
            for zb in range(1 << m):
                mask = pauli_mask(xb, zb, m)
                for k in range(m):
                    b1 = (mask >> (2 * k + 1)) & 1
                    b2 = (mask >> (2 * k + 2)) & 1
                    assert (b1 ^ b2) == ((zb >> k) & 1)
    print("Section 1 checks: PASS")


def verify_section_2():
    # Exhaustively verify Theorem 2.2 (H_1 on D=(0,1,2)) and Theorem 2.3 (C_GHZ on arbitrary D)
    # for n = 3 and a = 0, 1, 2, 3 (m <= 6).
    for a in (0, 1, 2, 3):
        m = 3 + a
        # Theorem 2.2: D = (0,1,2), A = (3..m-1), Q = Z_1
        A_std = list(range(3, m))
        for v in range(1 << a):
            z_anc = sum((1 << A_std[k]) for k in range(a) if (v >> k) & 1)
            mask = pauli_mask(0, (1 << 1) | z_anc, m)
            assert min_wt_gamma(mask, m) >= 4
        # Compare against X_{d'_1} for every d'_1 in 0..m-1:
        for dp1 in range(m):
            assert min_wt_gamma(pauli_mask(1 << dp1, 0, m), m) == 2

        # Theorem 2.3: arbitrary D = (d0, d1, d2) subset of 0..m-1, Q = Z_{d0} Z_{d1} Z_{d2}
        for D in itertools.combinations(range(m), 3):
            A = [j for j in range(m) if j not in D]
            z_data = (1 << D[0]) | (1 << D[1]) | (1 << D[2])
            for v in range(1 << len(A)):
                z_anc = sum((1 << A[k]) for k in range(len(A)) if (v >> k) & 1)
                mask = pauli_mask(0, z_data | z_anc, m)
                assert min_wt_gamma(mask, m) >= 4

    # Also verify C_GHZ = H_0 CNOT_{2,0} CNOT_{1,0} actually satisfies C_GHZ (Z_0 Z_1 Z_2) C_GHZ^dag = X_0
    H0 = op_on(H2, 0, 3)
    # CNOT_{c, t} with control c=1, target t=0 on 3 qubits:
    # build directly by basis action
    def cnot3(c, t):
        M = [[ZERO] * 8 for _ in range(8)]
        for x in range(8):
            # qubit idx 0 is MSB in kron(q0, q1, q2), so bit (2 - q)
            cb = (x >> (2 - c)) & 1
            y = x ^ (cb << (2 - t))
            M[y][x] = ONE
        return M

    C_ghz = mat_mul(H0, mat_mul(cnot3(2, 0), cnot3(1, 0)))
    zzz = pauli_mat(0, 0b111, 3)
    x0 = pauli_mat(0b001, 0, 3)  # bit 0 is qubit 0 in pauli_mat
    assert mat_mul(C_ghz, mat_mul(zzz, mat_dag(C_ghz))) == x0
    print("Section 2 checks: PASS")


def verify_section_3():
    # Verify Theorem 3.1 exact log-space Majorana tracker on sample circuits for m = 3, 4
    # against full 2^m x 2^m unitary matrix conjugation B^dag Z_0 B |0^m>.
    for m in (3, 4):
        Bs = braid_generators(m)
        Z0 = pauli_mat(0, 1, m)
        eye = mat_eye(1 << m)
        ket0m = [ONE] + [ZERO] * ((1 << m) - 1)

        def track_circuit(ops):
            # ops: list of (r_zero_based, power) where power in (+1, -1)
            # Track B^dag Z_0 B backwards from end of circuit to start:
            u, v, s = 0, 1, 0
            for r, pwr in reversed(ops):
                def step(idx):
                    if pwr == 1:
                        # B_r^dag gamma_r B_r = -gamma_{r+1}, B_r^dag gamma_{r+1} B_r = +gamma_r
                        if idx == r:
                            return r + 1, 1
                        if idx == r + 1:
                            return r, 0
                    else:
                        # B_r gamma_r B_r^dag = +gamma_{r+1}, B_r gamma_{r+1} B_r^dag = -gamma_r
                        if idx == r:
                            return r + 1, 0
                        if idx == r + 1:
                            return r, 1
                    return idx, 0
                u, fu = step(u)
                v, fv = step(v)
                s ^= fu ^ fv
                if u > v:
                    u, v = v, u
                    s ^= 1
            return (u % 2 == 0 and v == u + 1 and s == 1), (u, v, s)

        # Test all pairs of generators and a mix of 2- and 3-gate circuits including Z_0 -> -Z_0
        test_circuits = [
            [],
            [(0, 1)],
            [(1, 1), (1, 1)],                    # X_0
            [(1, 1), (1, 1), (0, 1)],            # X_0 then S_0
            [(0, 1), (1, 1), (1, 1), (0, 1)],    # B_0 X_0 B_0^dag? No, B_0 X_0 B_0
            [(1, 1), (2, 1), (3, -1), (4, 1), (1, 1)],
            [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (1, -1)],
            [(1, 1), (1, 1), (2, 1), (2, 1)],    # X_0 then Z_0 Z_1 -> flips Z_0 to -Z_0!
        ]
        for ops in test_circuits:
            B = eye
            for r, pwr in ops:
                G = Bs[r] if pwr == 1 else mat_dag(Bs[r])
                B = mat_mul(G, B)
            conj = mat_mul(mat_dag(B), mat_mul(Z0, B))
            out = apply_mat_vec(conj, ket0m)
            actual_accept = (out == [-x for x in ket0m])
            pred_accept, _ = track_circuit(ops)
            assert actual_accept == pred_accept, f"Tracker mismatch for ops={ops}: {actual_accept} vs {pred_accept}"

        # Also verify Theorem 3.2: every weight-2 Z-only Pauli mask corresponds to {2k, 2k+1}
        wt2_zs = []
        for zb in range(1, 1 << m):
            if min_wt_gamma(pauli_mask(0, zb, m), m) == 2:
                wt2_zs.append(zb)
        expected_zs = [(1 << 0), (1 << (m - 1))] + [(1 << (k - 1)) | (1 << k) for k in range(1, m)]
        assert set(wt2_zs) == set(expected_zs)
    print("Section 3 checks: PASS")


def verify_section_4():
    # Verify Theorem 4.1 exactly in Q(zeta_16) on n = 3 data qubits + 1 ancilla (m = 4)!
    m = 4
    Bs = braid_generators(m)
    eye = mat_eye(1 << m)

    # Check H_n = e^{-i pi/4} S_n sqrtX_n S_n on boundary qubit n=3:
    Sn = mat_scale(ZETA_P1, Bs[2 * m])        # S_3
    sqrtXn = mat_scale(ZETA_P1, Bs[2 * m - 1])  # sqrtX_3
    Hn = mat_scale(ZETA_P2.conj(), mat_mul(Sn, mat_mul(sqrtXn, Sn)))
    assert Hn == op_on(H2, m - 1, m)

    # Check Z_n = S_n^2, X_n = sqrtX_n^2, and Z_j from braids B_0^2 B_2^2 ... B_{2j}^2
    assert mat_mul(Sn, Sn) == op_on(Z2, m - 1, m)
    assert mat_mul(sqrtXn, sqrtXn) == op_on(X2, m - 1, m)
    for j in range(m):
        zj_braid = eye
        for k in range(j + 1):
            zj_braid = mat_mul(mat_scale(ZETA_P2, mat_mul(Bs[2 * k], Bs[2 * k])), zj_braid)
        assert zj_braid == op_on(Z2, j, m)

    # Check S_j 1-ancilla gadget on m=4 for EVERY data qubit j in {0, 1, 2}
    # and EVERY computational basis state |x0 x1 x2> (by linearity, all 8 basis states + superposition!)
    ket0 = [ONE, ZERO]
    ket1 = [ZERO, ONE]
    ket_plus_i = [INV_SQRT2, INV_SQRT2 * I_UNIT]
    # Prepare |+i>_3 from |0>_3 via Z_3 sqrtX_3:
    Zn = op_on(Z2, m - 1, m)
    prep_n = mat_mul(Zn, op_on(SQRT_X2, m - 1, m))
    assert apply_mat_vec(prep_n, [ONE] + [ZERO] * 15)[:2] == [x * ZETA_P2 for x in ket_plus_i]

    Xn = op_on(X2, m - 1, m)
    proj_X = [
        mat_scale(HALF, mat_add(eye, Xn)),
        mat_scale(HALF, mat_add(eye, mat_scale(-ONE, Xn))),
    ]

    # Basis state test vectors: all 8 computational basis vectors plus equal superposition of |000> and |111>
    test_states = []
    for idx in range(8):
        v = [ONE if k == idx else ZERO for k in range(8)]
        test_states.append(v)
    test_states.append([INV_SQRT2 if k in (0, 7) else ZERO for k in range(8)])

    for j in range(3):
        Zj = op_on(Z2, j, m)
        ZjZn = mat_mul(Zj, Zn)
        proj_ZZ = [
            mat_scale(HALF, mat_add(eye, ZjZn)),
            mat_scale(HALF, mat_add(eye, mat_scale(-ONE, ZjZn))),
        ]
        Sj_target = op_on(S2, j, 3)

        for psi in test_states:
            init = vec_kron(psi, ket_plus_i)
            s_psi = apply_mat_vec(Sj_target, psi)
            for m1 in (0, 1):
                for m2 in (0, 1):
                    post = apply_mat_vec(proj_X[m2], apply_mat_vec(proj_ZZ[m1], init))
                    if (m1 ^ m2) == 1:
                        post = apply_mat_vec(Zj, post)
                    # Reset ancilla 3 via X_3^{m2} H_3
                    post = apply_mat_vec(Hn, post)
                    if m2 == 1:
                        post = apply_mat_vec(Xn, post)
                    # Expected: (1/2) * phase * (S_j |psi>) (x) |0>_3
                    if m1 == 0:
                        phase = ONE
                    else:
                        phase = I_UNIT if m2 == 0 else -I_UNIT
                    expected = [HALF * phase * x for x in vec_kron(s_psi, ket0)]
                    assert post == expected, f"S_{j} gadget failed for m1={m1}, m2={m2}"

    # Verify CZ_{j, j+1} = e^{i pi/8} (Z_j S_j (x) Z_{j+1} S_{j+1}) B_{2j+2}
    for j in range(m - 1):
        ZjS = mat_mul(op_on(Z2, j, m), op_on(S2, j, m))
        Zj1S = mat_mul(op_on(Z2, j + 1, m), op_on(S2, j + 1, m))
        cz_synth = mat_scale(ZETA_P1, mat_mul(ZjS, mat_mul(Zj1S, Bs[2 * j + 2])))
        mats = [I2] * m
        mats[j] = CZ4
        del mats[j + 1]
        assert cz_synth == kron_all(mats)

    # Verify H_{j+1} CZ_{j,j+1} H_{j+1} == CNOT_{j,j+1}
    cz_01 = CZ4
    h_1 = mat_kron(I2, H2)
    assert mat_mul(h_1, mat_mul(cz_01, h_1)) == CNOT4
    print("Section 4 checks: PASS")


if __name__ == "__main__":
    verify_section_1()
    verify_section_2()
    verify_section_3()
    verify_section_4()
    print("OVERALL: PASS")

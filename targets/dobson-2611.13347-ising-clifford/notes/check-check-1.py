"""Independent exact Q(zeta_16) verifier for targets/dobson-2611.13347-ising-clifford."""

from __future__ import annotations

import itertools
import pathlib
import random
import tarfile
from fractions import Fraction


class Z16:
    """Exact element of Q(zeta_16) where zeta = e^{i*pi/8}, zeta^8 = -1."""

    __slots__ = ("c",)

    def __init__(self, coeffs: tuple[Fraction, ...] | list[Fraction | int]) -> None:
        assert len(coeffs) == 8
        self.c = tuple(x if isinstance(x, Fraction) else Fraction(x) for x in coeffs)

    @staticmethod
    def zero() -> Z16:
        return Z16([0] * 8)

    @staticmethod
    def one() -> Z16:
        return Z16([1, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def zeta(k: int) -> Z16:
        k_mod = k % 16
        sign = -1 if k_mod >= 8 else 1
        arr = [0] * 8
        arr[k_mod % 8] = sign
        return Z16(arr)

    @staticmethod
    def inv_sqrt2() -> Z16:
        # (zeta^2 - zeta^6) / 2 = cos(pi/4)
        arr = [Fraction(0)] * 8
        arr[2] = Fraction(1, 2)
        arr[6] = Fraction(-1, 2)
        return Z16(arr)

    def __add__(self, other: Z16) -> Z16:
        return Z16(tuple(a + b for a, b in zip(self.c, other.c)))

    def __sub__(self, other: Z16) -> Z16:
        return Z16(tuple(a - b for a, b in zip(self.c, other.c)))

    def __neg__(self) -> Z16:
        return Z16(tuple(-a for a in self.c))

    def __mul__(self, other: Z16) -> Z16:
        res = [Fraction(0)] * 8
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(other.c):
                if b == 0:
                    continue
                k = i + j
                if k < 8:
                    res[k] += a * b
                else:
                    res[k - 8] -= a * b
        return Z16(tuple(res))

    def scale(self, f: Fraction | int) -> Z16:
        fr = f if isinstance(f, Fraction) else Fraction(f)
        return Z16(tuple(a * fr for a in self.c))

    def conj(self) -> Z16:
        # conj(zeta^k) = zeta^{-k}; for k=0 -> c_0, for k=1..7 -> -c_{8-k} * ... wait:
        # zeta^{-k} = -zeta^{8-k} for k in 1..7!
        res = [self.c[0]] + [-self.c[8 - k] for k in range(1, 8)]
        return Z16(tuple(res))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Z16):
            return NotImplemented
        return self.c == other.c

    def is_zero(self) -> bool:
        return all(x == 0 for x in self.c)


def mat_mul(a: list[list[Z16]], b: list[list[Z16]]) -> list[list[Z16]]:
    n = len(a)
    m = len(b[0])
    inner = len(b)
    out = [[Z16.zero() for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(inner):
            aik = a[i][k]
            if aik.is_zero():
                continue
            for j in range(m):
                out[i][j] = out[i][j] + (aik * b[k][j])
    return out


def mat_dag(a: list[list[Z16]]) -> list[list[Z16]]:
    r, c = len(a), len(a[0])
    return [[a[j][i].conj() for j in range(r)] for i in range(c)]


def mat_kron(a: list[list[Z16]], b: list[list[Z16]]) -> list[list[Z16]]:
    ra, ca = len(a), len(a[0])
    rb, cb = len(b), len(b[0])
    out = [[Z16.zero() for _ in range(ca * cb)] for _ in range(ra * rb)]
    for i1 in range(ra):
        for j1 in range(ca):
            for i2 in range(rb):
                for j2 in range(cb):
                    out[i1 * rb + i2][j1 * cb + j2] = a[i1][j1] * b[i2][j2]
    return out


def mat_eye(dim: int) -> list[list[Z16]]:
    return [[Z16.one() if i == j else Z16.zero() for j in range(dim)] for i in range(dim)]


def mat_scale(a: list[list[Z16]], s: Z16) -> list[list[Z16]]:
    return [[x * s for x in row] for row in a]


def mat_add(a: list[list[Z16]], b: list[list[Z16]]) -> list[list[Z16]]:
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


I2 = mat_eye(2)
X2 = [[Z16.zero(), Z16.one()], [Z16.one(), Z16.zero()]]
Z2 = [[Z16.one(), Z16.zero()], [Z16.zero(), -Z16.one()]]
Y2 = [[Z16.zero(), -Z16.zeta(4)], [Z16.zeta(4), Z16.zero()]]
S2 = [[Z16.one(), Z16.zero()], [Z16.zero(), Z16.zeta(4)]]
SX2 = [
    [Z16([Fraction(1, 2), 0, 0, 0, Fraction(1, 2), 0, 0, 0]), Z16([Fraction(1, 2), 0, 0, 0, Fraction(-1, 2), 0, 0, 0])],
    [Z16([Fraction(1, 2), 0, 0, 0, Fraction(-1, 2), 0, 0, 0]), Z16([Fraction(1, 2), 0, 0, 0, Fraction(1, 2), 0, 0, 0])],
]
H2 = mat_scale([[Z16.one(), Z16.one()], [Z16.one(), -Z16.one()]], Z16.inv_sqrt2())


def op_on_qubit(m: int, j: int, gate: list[list[Z16]]) -> list[list[Z16]]:
    res = mat_eye(1)
    for q in range(m):
        res = mat_kron(res, gate if q == j else I2)
    return res


def two_qubit_cz(m: int, j: int) -> list[list[Z16]]:
    # CZ on adjacent j, j+1
    cz4 = mat_eye(4)
    cz4[3][3] = -Z16.one()
    res = mat_eye(1)
    q = 0
    while q < m:
        if q == j:
            res = mat_kron(res, cz4)
            q += 2
        else:
            res = mat_kron(res, I2)
            q += 1
    return res


def pauli_P(m: int, r: int) -> list[list[Z16]]:
    # r in 1..2m+1
    if r == 1:
        return op_on_qubit(m, 0, Z2)
    if r == 2 * m + 1:
        return op_on_qubit(m, m - 1, Z2)
    if r % 2 == 0:
        return op_on_qubit(m, (r - 2) // 2, X2)
    j = (r - 1) // 2
    return mat_mul(op_on_qubit(m, j - 1, Z2), op_on_qubit(m, j, Z2))


def braid_gen(m: int, idx: int) -> list[list[Z16]]:
    # idx in 0..2m
    ph = Z16.zeta(-1)
    if idx == 0:
        return mat_scale(op_on_qubit(m, 0, S2), ph)
    if idx == 2 * m:
        return mat_scale(op_on_qubit(m, m - 1, S2), ph)
    if idx % 2 == 1:
        return mat_scale(op_on_qubit(m, (idx - 1) // 2, SX2), ph)
    j = (idx - 2) // 2
    sj = op_on_qubit(m, j, S2)
    sj1 = op_on_qubit(m, j + 1, S2)
    return mat_scale(mat_mul(mat_mul(sj, sj1), two_qubit_cz(m, j)), ph)


def pauli_mask(m: int, x_bits: tuple[int, ...], z_bits: tuple[int, ...]) -> int:
    mask = 0
    for j in range(m):
        if x_bits[j]:
            mask ^= (1 << (2 * j + 1)) | (1 << (2 * j + 2))
        if z_bits[j]:
            mask ^= (1 << (2 * j + 2)) - 1
    return mask


def majorana_weight(m: int, mask: int) -> int:
    pop = mask.bit_count()
    return min(pop, 2 * m + 2 - pop)


def verify_majorana_and_nogo() -> None:
    # 1. Exact Q(zeta_16) matrix check for m = 1, 2, 3: B_{r-1} = zeta * (I - i P_r) / sqrt(2) and parity operator
    for m in (1, 2, 3):
        dim = 1 << m
        eye = mat_eye(dim)
        p_prod = eye
        for r in range(1, 2 * m + 2):
            pr = pauli_P(m, r)
            br = braid_gen(m, r - 1)
            rhs = mat_scale(mat_add(eye, mat_scale(pr, -Z16.zeta(4))), Z16.zeta(1) * Z16.inv_sqrt2())
            assert br == rhs, f"B_{r-1} formula failed at m={m}"
            if r % 2 == 1:
                p_prod = mat_mul(p_prod, pr)
        assert p_prod == eye
        # Verify Lemma 1.1(2),(3) over all 4^m Paulis
        for xb in itertools.product((0, 1), repeat=m):
            for zb in itertools.product((0, 1), repeat=m):
                mask = pauli_mask(m, xb, zb)
                assert mask.bit_count() % 2 == 0
                for k in range(m):
                    b1 = (mask >> (2 * k + 1)) & 1
                    b2 = (mask >> (2 * k + 2)) & 1
                    assert (b1 ^ b2) == zb[k]

    # 2. Check parity sign: (-i)^{m+1} gamma_0 ... gamma_{2m+1} = I, whereas i^{m+1} gives -I for even m!
    # At m=2, P1*P3*P5 = (-i)^3 gamma_0..5 = +i gamma_0..5 = I
    neg_i_pow_3 = (-Z16.zeta(4)) * (-Z16.zeta(4)) * (-Z16.zeta(4))
    pos_i_pow_3 = Z16.zeta(4) * Z16.zeta(4) * Z16.zeta(4)
    assert neg_i_pow_3 == Z16.zeta(4) and pos_i_pow_3 == -Z16.zeta(4)

    # 3. Verify Theorem 2.2 (Z_1 + ancilla Z) and Theorem 2.3 (arbitrary 3 data wires) weight >= 4
    for a in range(4):
        m = 3 + a
        for v in itertools.product((0, 1), repeat=a):
            zb = (0, 1, 0) + v
            assert majorana_weight(m, pauli_mask(m, (0,) * m, zb)) >= 4
        for d_wires in itertools.combinations(range(m), 3):
            anc = [q for q in range(m) if q not in d_wires]
            for v in itertools.product((0, 1), repeat=len(anc)):
                zb = [0] * m
                for dw in d_wires:
                    zb[dw] = 1
                for q, bit in zip(anc, v):
                    zb[q] = bit
                assert majorana_weight(m, pauli_mask(m, (0,) * m, tuple(zb))) >= 4

    print("MAJORANA_AND_NOGO: PASS")


def verify_ising_braid_logspace_tracker() -> None:
    rng = random.Random(261113347)
    for m in (2, 3):
        gens = [braid_gen(m, r) for r in range(2 * m + 1)]
        invs = [mat_dag(g) for g in gens]
        z0 = op_on_qubit(m, 0, Z2)
        ket0 = [[Z16.one()] if i == 0 else [Z16.zero()] for i in range(1 << m)]
        for _ in range(25):
            length = rng.randint(1, 14)
            word = [(rng.randint(0, 2 * m), rng.randint(0, 1)) for _ in range(length)]
            b_mat = mat_eye(1 << m)
            for idx, is_inv in word:
                b_mat = mat_mul(invs[idx] if is_inv else gens[idx], b_mat)
            # Log-space tracker (u, v, s) for B^dag Z_0 B
            u, v, s = 0, 1, 0
            for idx, is_inv in reversed(word):
                def map_m(x: int) -> tuple[int, int]:
                    if not is_inv:
                        if x == idx:
                            return idx + 1, 1
                        if x == idx + 1:
                            return idx, 0
                    else:
                        if x == idx:
                            return idx + 1, 0
                        if x == idx + 1:
                            return idx, 1
                    return x, 0
                u, fu = map_m(u)
                v, fv = map_m(v)
                s ^= fu ^ fv
                if u > v:
                    u, v = v, u
                    s ^= 1
            pred_accept = (u % 2 == 0) and (v == u + 1) and (s == 1)
            out_vec = mat_mul(b_mat, ket0)
            # Check exact expectation of Z_0 on B|0^m>
            conj_z0 = mat_mul(mat_dag(b_mat), mat_mul(z0, b_mat))
            expect = mat_mul(mat_dag(ket0), mat_mul(conj_z0, ket0))[0][0]
            actual_accept = (expect == -Z16.one())
            assert pred_accept == actual_accept, f"Tracker mismatch at m={m}: pred={pred_accept}, expect={expect.c}"
            assert actual_accept == (out_vec[0][0].is_zero() and all(out_vec[i][0].is_zero() for i in range(1 << (m - 1))))

    print("ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS")


def verify_1ancilla_clifford_gadget() -> None:
    # Exact Q(zeta_16) check of Theorem 4.1 S_j gadget on n=2 data qubits + 1 ancilla (m=3)
    m = 3
    anc = 2
    b_sx_anc = mat_scale(braid_gen(m, 2 * anc + 1), Z16.zeta(1))
    b_s_anc = mat_scale(braid_gen(m, 2 * anc + 2), Z16.zeta(1))
    x_anc = mat_mul(b_sx_anc, b_sx_anc)
    z_anc = mat_mul(b_s_anc, b_s_anc)
    h_anc = mat_scale(mat_mul(b_s_anc, mat_mul(b_sx_anc, b_s_anc)), Z16.zeta(-2))
    assert h_anc == op_on_qubit(m, anc, H2)

    eye8 = mat_eye(8)
    for j in (0, 1):
        # Compute Z_j via (B_0^2 B_2^2 ... B_{2j}^2) up to global phase
        z_j_braid = eye8
        for r in range(j + 1):
            br = braid_gen(m, 2 * r)
            z_j_braid = mat_mul(z_j_braid, mat_mul(br, br))
        # Verify z_j_braid == e^{-i*(j+1)*pi/4} * Z_j
        assert z_j_braid == mat_scale(op_on_qubit(m, j, Z2), Z16.zeta(-2 * (j + 1)))

        m1_op = mat_mul(op_on_qubit(m, j, Z2), op_on_qubit(m, anc, Z2))
        m2_op = op_on_qubit(m, anc, X2)
        prep_anc = mat_mul(z_anc, b_sx_anc)  # prepares e^{i*pi/4} |+i> on anc

        for m1 in (0, 1):
            proj1 = mat_scale(mat_add(eye8, mat_scale(m1_op, Z16.one() if m1 == 0 else -Z16.one())), Z16([Fraction(1, 2)] + [0] * 7))
            for m2 in (0, 1):
                proj2 = mat_scale(mat_add(eye8, mat_scale(m2_op, Z16.one() if m2 == 0 else -Z16.one())), Z16([Fraction(1, 2)] + [0] * 7))
                corr = z_j_braid if (m1 ^ m2) else eye8
                reset = h_anc if m2 == 0 else mat_mul(x_anc, h_anc)
                branch = mat_mul(reset, mat_mul(corr, mat_mul(proj2, mat_mul(proj1, prep_anc))))
                # On |psi> |0>_anc, branch must produce (phase/2) * (S_j |psi>) |0>_anc
                target_sj = op_on_qubit(m, j, S2)
                for basis in range(4):
                    idx0 = basis << 1  # ancilla = 0
                    vec = [[Z16.one()] if r == idx0 else [Z16.zero()] for r in range(8)]
                    out = mat_mul(branch, vec)
                    exp_out = mat_mul(target_sj, vec)
                    # Determine global phase factor for this (m1, m2)
                    nz = next(r for r in range(8) if not exp_out[r][0].is_zero())
                    ratio = out[nz][0]
                    # Compare out == 2 * ratio? Actually exp_out[nz][0] is 1 or i
                    if exp_out[nz][0] == Z16.zeta(4):
                        phase = ratio * (-Z16.zeta(4))
                    else:
                        phase = ratio
                    # Check |phase| == 1/2 (i.e. phase * conj(phase) == 1/4) and out == phase * exp_out
                    assert phase * phase.conj() == Z16([Fraction(1, 4)] + [0] * 7)
                    for r in range(8):
                        assert out[r][0] == phase * exp_out[r][0]

    # Check CZ_{0,1} identity from Theorem 4.1
    b2 = braid_gen(m, 2)
    z0_s0 = mat_mul(op_on_qubit(m, 0, Z2), op_on_qubit(m, 0, S2))
    z1_s1 = mat_mul(op_on_qubit(m, 1, Z2), op_on_qubit(m, 1, S2))
    cz01 = mat_scale(mat_mul(mat_mul(z0_s0, z1_s1), b2), Z16.zeta(1))
    assert cz01 == two_qubit_cz(m, 0)
    print("ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS")


def verify_source_and_docs() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2611.13347.src"
    target_md = (
        root / "targets" / "dobson-2611.13347-ising-clifford" / "TARGET.md"
    ).read_text(encoding="utf-8")
    proof_md = (
        root / "targets" / "dobson-2611.13347-ising-clifford" / "PROOF.md"
    ).read_text(encoding="utf-8")

    quote = "Is this still true if we allow ancilla qubits?"
    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        if quote not in target_md:
            failures.append("TARGET.md Problem (3) quote missing")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            sec5 = tf.extractfile("sections/5.tex").read().decode("utf-8")
        if quote not in target_md or quote not in sec5:
            failures.append("TARGET.md Problem (3) quote mismatch with sections/5.tex")

    if r"i^{m+1} \gamma_0" in proof_md or r"i^{m+1}\gamma_0" in proof_md:
        failures.append(
            "PROOF.md L25/L41 writes i^{m+1} gamma_0...gamma_{2m+1} = I, which equals -I for all even m "
            "(must be (-i)^{m+1} gamma_0...gamma_{2m+1} = P_1 P_3 ... P_{2m+1} = I)"
        )
    if "Definitions 3.1, 3.4, 3.6" in proof_md:
        failures.append(
            "PROOF.md L83 cites Definitions 3.1, 3.4, 3.6 for PUSC/LUSC, whereas def:USC is Definition 3.8 in sections/3.tex"
        )
    if "Proposition 3.5" in proof_md:
        failures.append(
            "PROOF.md L101 cites Proposition 3.5 for prop:5050, whereas prop:5050 is Proposition 3.7 (shared [theorem] counter)"
        )

    return failures


def main() -> int:
    verify_majorana_and_nogo()
    verify_ising_braid_logspace_tracker()
    verify_1ancilla_clifford_gadget()
    failures = verify_source_and_docs()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

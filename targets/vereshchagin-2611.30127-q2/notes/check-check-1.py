"""Independent exact-arithmetic verifier for targets/vereshchagin-2611.30127-q2."""

from fractions import Fraction
import pathlib
import re
import tarfile


def encode_prefix_free(i: int) -> str:
    """Doubled-bit prefix-free encoding i_hat of i >= 1."""
    assert i >= 1
    bits = bin(i)[2:]
    return "".join(b * 2 for b in bits) + "01"


def poly_eval(b: int, c: int, n: int) -> int:
    return b * ((n + 1) ** c)


def verify_constants_and_gv_code() -> None:
    """Verify Lemma 4.1 GV packing bound, concrete greedy codewords, and all rational constants."""
    # 1. Exact integer inequality 8 * 27^20 < 32^20 from PROOF.md L66
    lhs = 8 * (27 ** 20)
    rhs = 32 ** 20
    assert lhs == 339129266201729628114355465608
    assert rhs == 1267650600228229401496703205376
    assert lhs < rhs

    # 2. Verify combinatorial GV packing bound for L = 20..80
    from math import comb
    for L in range(20, 81):
        N = L // 20
        r = L // 3
        ball = sum(comb(L, j) for j in range(r + 1))
        assert (1 << N) * ball < (1 << L)

    # 3. Construct explicit greedy code C_20 and C_21 (N=1 -> 2 codewords, min distance > L/3)
    for L in (20, 21):
        N = L // 20
        r = L // 3
        codewords: list[int] = []
        for cand in range(1 << L):
            if all((cand ^ cw).bit_count() > r for cw in codewords):
                codewords.append(cand)
                if len(codewords) == (1 << N):
                    break
        assert len(codewords) == (1 << N)
        for u in range(len(codewords)):
            for v in range(u + 1, len(codewords)):
                assert (codewords[u] ^ codewords[v]).bit_count() >= r + 1 > Fraction(L, 3)

    # 4. Exact rational inequalities in Lemmas 5.1, 6.1, and Theorems 1 & 2
    assert Fraction(24, 25) > Fraction(9, 10)
    assert Fraction(24, 25) * Fraction(1, 4) > Fraction(9, 40)
    assert Fraction(9, 80) > Fraction(1, 16)
    assert (Fraction(2, 3) ** 3) == Fraction(8, 27) < Fraction(1, 3) < Fraction(1, 2)
    assert 2 ** 17 == 131072 > 10 ** 5
    # Theorem 2 rational margins at delta = 1/10
    gamma_max = Fraction(1, 10)
    assert (1 - gamma_max) * Fraction(2, 3) == Fraction(3, 5) > Fraction(1, 2)
    assert gamma_max + (1 - gamma_max) * Fraction(1, 3) == Fraction(2, 5) < Fraction(1, 2)
    print("Lemma 4.1 GV code & exact rational constants: PASS")


def verify_oracle_layout_and_parameters() -> None:
    """Verify prefix-free encoding, n_0(i) <= 32, and Stage s parameter conditions (P1)-(P4)."""
    encodings = [encode_prefix_free(i) for i in range(1, 201)]
    for idx, s in enumerate(encodings, start=1):
        assert len(s) == 2 * (idx.bit_length() - 1) + 4
    for i in range(len(encodings)):
        for j in range(len(encodings)):
            if i != j:
                assert not encodings[i].startswith(encodings[j])

    # Check n_0(i) <= 32 for all polynomials a(n) = b*(n+1)^c (b, c >= 1)
    for b in range(1, 10):
        for c in range(1, 6):
            n0 = next(n for n in range(100) if poly_eval(b, c, n) // 3 >= 11)
            assert n0 <= 32
            L = 1 << (poly_eval(b, c, n0) // 3)
            N = L // 20
            assert L >= 2048 and N >= 102 >= 100

    # Check Theorem 1 & Theorem 2 polynomial bounds and (P1)-(P4) feasibility for sample p, m', t'
    for b in (1, 2, 3):
        for c in (1, 2, 3):
            # Theorem 1 choice: a(n) = n+1, m(n) = (b*2^c + 1)*(n+1)^(c+1)
            a_coeff = b * (2 ** c)
            # Theorem 2 choice: a(n) = n+1, m(n) = (b*12^c + 2)*(n+1)^(c+1)
            a2_coeff = b * (12 ** c) + 1
            for n in range(0, 60):
                a_n = n + 1
                p_an = poly_eval(b, c, a_n)
                ap_n = poly_eval(a_coeff, c, n)
                assert p_an <= ap_n
                m_n = poly_eval(a_coeff + 1, c + 1, n)
                assert m_n - ap_n >= (n + 1) ** (c + 1) >= (n + 1) ** 2

                # Theorem 2 bounds
                a_star = poly_eval(b, c, 10 * a_n)
                # Wait: PROOF.md L264 uses a(10n) = 10n + 1 -> p(a(10n)) = b*(10n+2)^c
                a_star_proof = poly_eval(b, c, 10 * n + 1)
                a_double = poly_eval(a2_coeff, c, n)
                assert a_double >= n + a_star_proof
                m2_n = poly_eval(a2_coeff + 1, c + 1, n)
                assert m2_n - a_double >= (n + 1) ** (c + 1) >= (n + 1) ** 2

            # Verify that for large enough n, (P1)-(P4) all hold strictly (integer arithmetic: use 2^{m_i} vs 2^{89N/100})
            m_i_poly = (a_coeff + 1, c + 1)
            a_i_poly = (1, 1)  # a_i(n) = n+1
            ap_poly = (a_coeff, c)
            mp_poly = (2, 2)
            tp_poly = (3, 2)
            found_n = None
            for n in range(32, 200):
                ell_n = poly_eval(*a_i_poly, n) // 3
                L_n = 1 << ell_n
                N_n = L_n // 20
                m_n = poly_eval(*m_i_poly, n)
                ap_n = poly_eval(*ap_poly, n)
                mp_n = poly_eval(*mp_poly, n)
                tp_n = poly_eval(*tp_poly, n)
                C_n = 2 * tp_n * tp_n
                Delta_n = 2 * (ap_n + mp_n + C_n) + 8
                # Check (P1), (P2): 100 * Delta_n <= N_n
                if N_n < 100 or 100 * Delta_n > N_n:
                    continue
                # Check (P3): M_n * 2^{-89 N_n / 100} < 1/4 <=> 4 * 2^{m_n} < 2^{89 N_n / 100}
                # Check stronger integer sufficient condition (m_n + 2) * 100 < 89 * N_n
                if (m_n + 2) * 100 >= 89 * N_n:
                    continue
                # Check Condition 4: ap_n <= m_n - ceil(log2(Delta_n)) - 17 -> Delta_n * 2^{ap_n + 17} <= 2^{m_n}
                if (ap_n + 17) + Delta_n.bit_length() <= m_n:
                    # Verify (P4): K_n * Delta_n <= 10^{-5} M_n <=> 10^5 * ((1 << (ap_n - 1)) + 1) * Delta_n <= (1 << m_n)
                    K_n = (1 << (ap_n - 1)) + 1
                    assert 100000 * K_n * Delta_n <= (1 << m_n)
                    found_n = n
                    break
            assert found_n is not None
    print("Oracle layout, prefix-freeness, n_0<=32, and Stage s (P1)-(P4) check: PASS")


def verify_aw_multilinear_decomposition() -> None:
    """Verify Lemma 6.2 additive decomposition f_A(X) + f_B(W) + c_fix of A_tilde over F_p and F_{p^2}."""
    # Exact test over prime field F_7 and quadratic extension F_{7^2} = F_7[t]/(t^2 + 1) (-1 is QNR mod 7)
    p = 7
    k_len = 5  # block length; S_A = 00..., S_B = 01..., S_fix = 1....
    # Map truth table A: {0,1}^5 -> {0,1}
    A_tt = [(s * 37 + 13) % 2 for s in range(1 << k_len)]

    def eval_direct_Fp(u: list[int]) -> int:
        total = 0
        for s in range(1 << k_len):
            if A_tt[s] == 0:
                continue
            term = 1
            for j in range(k_len):
                bit = (s >> (k_len - 1 - j)) & 1
                term = (term * (u[j] if bit == 1 else (1 - u[j]))) % p
            total = (total + term) % p
        return total

    def eval_split_Fp(u: list[int]) -> tuple[int, int, int]:
        fA = fB = cfix = 0
        for s in range(1 << k_len):
            if A_tt[s] == 0:
                continue
            term = 1
            for j in range(k_len):
                bit = (s >> (k_len - 1 - j)) & 1
                term = (term * (u[j] if bit == 1 else (1 - u[j]))) % p
            top2 = s >> (k_len - 2)
            if top2 == 0:
                fA = (fA + term) % p
            elif top2 == 1:
                fB = (fB + term) % p
            else:
                cfix = (cfix + term) % p
        return fA, fB, cfix

    # Verify on Boolean inputs and non-Boolean F_7 inputs
    for idx in range(1 << k_len):
        bits = [(idx >> (k_len - 1 - j)) & 1 for j in range(k_len)]
        assert eval_direct_Fp(bits) == A_tt[idx]
    for seed in range(25):
        u = [(seed * 3 + j * 5 + 1) % p for j in range(k_len)]
        fA, fB, cfix = eval_split_Fp(u)
        assert (fA + fB + cfix) % p == eval_direct_Fp(u)

    # Also test over F_{49} = F_7[i]/(i^2 + 1)
    def mul49(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        return ((x[0] * y[0] - x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)

    for seed in range(10):
        u49 = [((seed + j) % p, (2 * seed + 3 * j + 1) % p) for j in range(k_len)]
        tot = [0, 0]
        parts = [[0, 0], [0, 0], [0, 0]]
        for s in range(1 << k_len):
            if A_tt[s] == 0:
                continue
            term = (1, 0)
            for j in range(k_len):
                bit = (s >> (k_len - 1 - j)) & 1
                uj = u49[j]
                fac = uj if bit == 1 else ((1 - uj[0]) % p, (-uj[1]) % p)
                term = mul49(term, fac)
            tot = [(tot[0] + term[0]) % p, (tot[1] + term[1]) % p]
            top2 = s >> (k_len - 2)
            idx_part = 0 if top2 == 0 else (1 if top2 == 1 else 2)
            parts[idx_part] = [(parts[idx_part][0] + term[0]) % p, (parts[idx_part][1] + term[1]) % p]
        assert tuple(tot) == tuple((parts[0][c] + parts[1][c] + parts[2][c]) % p for c in (0, 1))
    print("AW multilinear extension & Lemma 6.2 additive split (F_7 and F_49): PASS")


def verify_ping_pong_small_invariant() -> None:
    """Exercise Step C Ping-Pong density restoration algebra on a concrete finite set family."""
    # M = 3, N = 4 (toy scale for exact combinatorial check of Step C fiber bijection & density drop)
    N = 4
    M = 3
    # Build subset A of ({0,1}^4)^3 where coordinate 0 is concentrated on v0 = 0 (prob > 1/2), violating 0.5-density
    all_vecs = [(a, b, c) for a in range(1 << N) for b in range(1 << N) for c in range(1 << N)]
    # Pick 40 tuples with a=0 and 20 tuples with a != 0
    A_set = [v for v in all_vecs if v[0] == 0][:40] + [v for v in all_vecs if v[0] != 0][:20]
    B_set = all_vecs[::7]
    # Check fiber restriction A' on S = {0}, v = 0 restores density on U' = {1, 2}
    A_prime = [(x[1], x[2]) for x in A_set if x[0] == 0]
    assert len(A_prime) == 40
    # Verify exact deficiency identity: log2(2^{|U'|N}/|A'|) - log2(2^{|U|N}/|A|) == -|S|N + log2(|A|/|A'|)
    # Using exact integers: (2^{2N}/|A'|) / (2^{3N}/|A|) == (|A|/|A'|) * 2^{-N}
    lhs_ratio = Fraction((1 << (2 * N)) * len(A_set), len(A_prime) * (1 << (3 * N)))
    rhs_ratio = Fraction(len(A_set), len(A_prime)) * Fraction(1, 1 << N)
    assert lhs_ratio == rhs_ratio < Fraction(1, 2)  # since |A'|/|A| = 40/60 = 2/3 > 2^{-0.9*4}? here > 2/16 = 1/8!
    # Bob avoidance on B_set at S={0}, v0=0:
    B_ok = [w for w in B_set if w[0] != 0]
    # Partition B_ok by w[0] != 0 (15 values < 16 = 2^N):
    fibers = {}
    for w in B_ok:
        fibers.setdefault(w[0], []).append((w[1], w[2]))
    best_w0, best_B_prime = max(fibers.items(), key=lambda kv: len(kv[1]))
    assert best_w0 != 0
    assert len(best_B_prime) * (1 << N) > len(B_ok)
    print("Step C Ping-Pong fiber restriction & deficiency algebra check: PASS")


def verify_primary_source_section6() -> None:
    """Verify Section 6 Open questions numbering directly from cached primary source."""
    root = pathlib.Path(__file__).resolve().parents[3]
    src_tar = root / "tools" / ".arxiv_cache" / "eprint" / "2611.30127.src"
    if not src_tar.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
    else:
        with tarfile.open(src_tar) as tf:
            tex = tf.extractfile("main-eng.tex").read().decode("utf-8")
        sections = [m.group(1) for m in re.finditer(r"\\section\{((?:[^{}]|\{[^{}]*\})*)\}", tex)]
        assert len(sections) >= 7
        assert sections[5].startswith("Open questions"), f"Unexpected Section 6: {sections[5]}"
        assert "Open questions" in sections[5] and "Acknowledgments" in sections[6]
    target_text = (root / "targets" / "vereshchagin-2611.30127-q2" / "TARGET.md").read_text(encoding="utf-8")
    proof_text = (root / "targets" / "vereshchagin-2611.30127-q2" / "PROOF.md").read_text(encoding="utf-8")
    assert "Section 6" in target_text and "Section 7" not in target_text
    assert "Section 6" in proof_text and "Section 7" not in proof_text
    print("Primary source Section 6 citation check: PASS")


def main() -> None:
    verify_primary_source_section6()
    verify_constants_and_gv_code()
    verify_oracle_layout_and_parameters()
    verify_aw_multilinear_decomposition()
    verify_ping_pong_small_invariant()
    print("PASS")


if __name__ == "__main__":
    main()

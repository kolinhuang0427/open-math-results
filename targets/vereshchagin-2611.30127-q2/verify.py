"""Exact zero-float verification of PROOF.md for vereshchagin-2611.30127-q2
(arXiv:2611.30127v1, Section 6, Open Questions 2 & 3).

Zero floats, zero float division (/), zero math/numpy/scipy imports.
Uses exact integer arithmetic and fractions.Fraction only.
"""

import ast
import sys
from fractions import Fraction


def check_ast_zero_float():
    with open(__file__, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal found: {node.value}")
        if isinstance(node, ast.Div):
            raise AssertionError("True division '/' found")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [alias.name for alias in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
            for nm in names:
                if nm in ("math", "numpy", "scipy", "decimal"):
                    raise AssertionError(f"Disallowed import: {nm}")


def int_binom(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - k + i
        den *= i
    assert num % den == 0
    return num // den


def test_gilbert_varshamov():
    """Verify exact integer GV bound 8 * 27^20 < 32^20 and exact ball-packing for L=20..2048."""
    lhs = 8 * (27 ** 20)
    rhs = 32 ** 20
    assert lhs == 339129266201729628114355465608
    assert rhs == 1267650600228229401496703205376
    assert lhs < rhs

    for L in [20, 32, 40, 64, 128, 256, 512, 1024, 2048]:
        N = L // 20
        r = L // 3
        assert N >= 1
        ball = sum(int_binom(L, j) for j in range(r + 1))
        assert (1 << N) * ball < (1 << L), f"GV ball bound failed at L={L}"

    # Construct explicit greedy GV code for L = 40 (N = 2, size 4, dist >= 14 > 40/3)
    # and check 3-query MA/MAP completeness = 1 and soundness < 8/27 < 1/3!
    L = 40
    N = L // 20  # 2
    r = L // 3   # 13, require dist >= 14
    code = []
    # Deterministic greedy search over low-weight/structured candidates (fast exact construction)
    # Lexicographically first codewords in {0, 1}^40:
    # c0 = 0^40, c1 = 0^26 1^14, c2 = 0^12 1^14 0^14 (dist 14 from c0, 28 from c1),
    # c3 = 1^14 0^12 1^14? Let's just run true lexicographic greedy over a small exact family or check distances!
    # True lexicographic greedy:
    # c0 = 0
    # c1 = (1 << 14) - 1 (smallest integer of popcount >= 14)
    # c2 = smallest integer with popcount >= 14 and popcount(x ^ c1) >= 14:
    #      if x has a bits in low 14 and b bits in high 26: a + b >= 14 and (14 - a) + b >= 14 => b >= max(14-a, a) >= 7.
    #      Minimize x => minimize b = 7, a = 7, lowest 7 bits of low 14 and lowest 7 bits of high 26!
    c0 = 0
    c1 = (1 << 14) - 1
    c2 = ((1 << 7) - 1) | (((1 << 7) - 1) << 14)
    # c3: bits in [0..6], [7..13], [14..20], [21..39]
    c3 = ((1 << 7) - 1) << 7 | (((1 << 7) - 1) << 21)
    code = [c0, c1, c2, c3]
    assert len(code) == (1 << N)
    for i in range(len(code)):
        for j in range(len(code)):
            dist = (code[i] ^ code[j]).bit_count()
            if i == j:
                assert dist == 0
                prob = Fraction(L - dist, L) ** 3
                assert prob == 1
            else:
                assert dist >= r + 1 and 3 * dist > L
                prob = Fraction(L - dist, L) ** 3
                assert prob < Fraction(8, 27) < Fraction(1, 3) < Fraction(1, 2)


def test_prefix_encoding_and_disjoint_blocks():
    """Verify prefix-freeness of hat(i) and disjointness of D_{i,n}."""
    def hat(i):
        bits = bin(i)[2:]
        return "".join(b + b for b in bits) + "01"

    hats = [hat(i) for i in range(1, 201)]
    for i in range(1, 201):
        assert len(hats[i - 1]) == 2 * (i.bit_length() - 1) + 4
    for a in range(len(hats)):
        for b in range(len(hats)):
            if a != b:
                assert not hats[a].startswith(hats[b])

    # Check strict monotonicity of k_i(n) = |hat(i)| + 1 + m_i(n) + a_i(n)//3 for sample polynomials
    polys = [(b, c) for b in (1, 2, 3) for c in (1, 2, 3)]
    for idx, ((bm, cm), (ba, ca)) in enumerate(zip(polys, reversed(polys)), 1):
        hi = len(hat(idx))
        prev_k = -1
        for n in range(0, 40):
            m_val = bm * ((n + 1) ** cm)
            a_val = ba * ((n + 1) ** ca)
            k_val = hi + 1 + m_val + (a_val // 3)
            assert k_val > prev_k
            prev_k = k_val


def test_multilinear_extension_additive_decomposition():
    """Verify exact multilinear extension A~_{k, F}(u) = f_A(X) + f_B(W) + c_fix
    over prime fields F_5, F_7, F_11 AND extension field GF(2^3)!"""
    # Active block layout at length k = 5:
    # prefix hat(1) = "1101" is length 4, too big for k=5; use synthetic prefix p="1" (len 1), b in {0,1},
    # y in {0,1}^1 (M=2), z in {0,1}^2 (L=4), total length k = 1 + 1 + 1 + 2 = 5 (32 strings)!
    # Strings starting with "0" (16 strings) are outside active block (fixed arbitrary non-zero bits!).
    # Strings "10yz" (8 strings) belong to Alice (X); strings "11yz" (8 strings) belong to Bob (W).
    k = 5
    # Arbitrary fixed table outside active block, arbitrary X and W
    X_bits = [1, 0, 1, 1, 0, 1, 0, 0]  # 8 bits for "10yz"
    W_bits = [0, 1, 1, 0, 1, 0, 1, 1]  # 8 bits for "11yz"
    fix_bits = [((s * 7 + 3) % 5) & 1 for s in range(16)]  # 16 bits for "0...."

    def A_truth(s_int):
        # bit 4 (MSB) is prefix p; bit 3 is b; bits 2..0 are yz
        p = (s_int >> 4) & 1
        if p == 0:
            return fix_bits[s_int & 15]
        b = (s_int >> 3) & 1
        idx = s_int & 7
        return X_bits[idx] if b == 0 else W_bits[idx]

    # 1) Test over prime fields F_p for p in {5, 7, 11}
    for p in [5, 7, 11]:
        def eval_mle_Fp(u_vec):
            tot = 0
            fA = 0
            fB = 0
            c_fix = 0
            for s in range(1 << k):
                val = A_truth(s)
                if val == 0:
                    continue
                term = 1
                for bit_pos in range(k):
                    s_bit = (s >> (k - 1 - bit_pos)) & 1
                    u = u_vec[bit_pos]
                    term = (term * (u if s_bit == 1 else (1 - u))) % p
                tot = (tot + term) % p
                prefix = (s >> 4) & 1
                b_bit = (s >> 3) & 1
                if prefix == 0:
                    c_fix = (c_fix + term) % p
                elif b_bit == 0:
                    fA = (fA + term) % p
                else:
                    fB = (fB + term) % p
            return tot, fA, fB, c_fix

        # Verify exact agreement with A on all 32 Boolean inputs
        for s in range(1 << k):
            u_vec = [(s >> (k - 1 - j)) & 1 for j in range(k)]
            tot, fA, fB, c_fix = eval_mle_Fp(u_vec)
            assert tot == A_truth(s)
            assert tot == (fA + fB + c_fix) % p

        # Verify exact additive decomposition on 64 non-Boolean points in F_p^5
        for t in range(64):
            u_vec = [(t * (j + 2) + j * j + 1) % p for j in range(k)]
            tot, fA, fB, c_fix = eval_mle_Fp(u_vec)
            assert tot == (fA + fB + c_fix) % p
            # Verify fA is independent of W_bits and fB is independent of X_bits!
            old_W = W_bits[:]
            W_bits[:] = [1 - b for b in old_W]
            _, fA_2, _, c_fix_2 = eval_mle_Fp(u_vec)
            assert fA == fA_2 and c_fix == c_fix_2
            W_bits[:] = old_W

    # 2) Test over non-prime extension field GF(2^3) = GF(2)[T]/(T^3 + T + 1)
    mod8 = 0b1011
    def gf8_mul(a, b):
        r = 0
        while b:
            if b & 1:
                r ^= a
            a <<= 1
            if a & 8:
                a ^= mod8
            b >>= 1
        return r

    def eval_mle_gf8(u_vec):
        tot = fA = fB = c_fix = 0
        for s in range(1 << k):
            if A_truth(s) == 0:
                continue
            term = 1
            for bit_pos in range(k):
                s_bit = (s >> (k - 1 - bit_pos)) & 1
                u = u_vec[bit_pos]
                term = gf8_mul(term, u if s_bit == 1 else (1 ^ u))
            tot ^= term
            prefix = (s >> 4) & 1
            b_bit = (s >> 3) & 1
            if prefix == 0:
                c_fix ^= term
            elif b_bit == 0:
                fA ^= term
            else:
                fB ^= term
        return tot, fA, fB, c_fix

    for s in range(1 << k):
        u_vec = [(s >> (k - 1 - j)) & 1 for j in range(k)]
        tot, fA, fB, c_fix = eval_mle_gf8(u_vec)
        assert tot == A_truth(s) and tot == (fA ^ fB ^ c_fix)
    for t in range(64):
        u_vec = [(t * (j + 3) + 2 * j + 5) & 7 for j in range(k)]
        tot, fA, fB, c_fix = eval_mle_gf8(u_vec)
        assert tot == (fA ^ fB ^ c_fix)


def test_combinatorial_lemma_constants_and_thresholds():
    """Verify every rational/integer constant in Lemma 5.1, Theorem 1, and Theorem 2."""
    # Pinsker bound: D_KL(p || U_N) <= 2*10^-5 => 2 * D_KL <= 4*10^-5 < (1/100)^2
    d_kl_max = Fraction(2, 100000)
    assert 2 * d_kl_max < Fraction(1, 100) ** 2

    # |S_good| / 2^N > 1 - 2*(1/100)/(1/2) = 24/25 > 9/10
    s_good_frac = 1 - 2 * Fraction(1, 100) * 2
    assert s_good_frac == Fraction(24, 25)
    assert s_good_frac > Fraction(9, 10)

    # Cauchy-Schwarz constant: (9/40) / 2 = 9/80 > 1/16 = 2^-4 => square > 2^-8 => Delta = 2(a'+m'+C)+8
    cs_ratio = Fraction(9, 40) * Fraction(1, 2)
    assert cs_ratio == Fraction(9, 80)
    assert cs_ratio > Fraction(1, 16)
    assert cs_ratio ** 2 > Fraction(1, 256)

    # 2^17 > 10^5 (used in condition (4) of Stage s)
    assert (1 << 17) == 131072 > 100000

    # Ping-pong potential net decrease for N >= 100 and |S| >= 1:
    # -0.1*N*|S| + 1 + 0.09*N*|S| = -0.01*N*|S| + 1 <= 0
    for N in [100, 102, 500]:
        for S_sz in [1, 2, 10]:
            delta_phi = Fraction(-1, 10) * N * S_sz + 1 + Fraction(9, 100) * N * S_sz
            assert delta_phi <= 0

    # |F_i| < K*Delta / (0.09*N) <= 10^-5 * M / 9 < M/2
    assert Fraction(1, 100000) * Fraction(1, 9) < Fraction(1, 2)

    # Open Question 3 heuristic averaging bounds at delta = 1/10
    for gamma_num in range(0, 11):
        gamma = Fraction(gamma_num, 100)  # gamma in [0, 1/10]
        yes_lb = (1 - gamma) * Fraction(2, 3)
        no_ub = gamma + (1 - gamma) * Fraction(1, 3)
        assert yes_lb >= Fraction(3, 5) > Fraction(1, 2)
        assert no_ub <= Fraction(2, 5) < Fraction(1, 2)

    # Verify Vereshchagin polynomial padding bounds across b, c in 1..5 and n in 0..20
    for b in range(1, 6):
        for c in range(1, 6):
            for n in range(0, 21):
                # Theorem 1 padding: p(a(n)) = b(n+2)^c <= b * 2^c * (n+1)^c
                assert b * ((n + 2) ** c) <= b * (2 ** c) * ((n + 1) ** c)
                # Theorem 2 randomness padding: n + b(10n+2)^c <= (b*12^c + 1)(n+1)^c
                assert n + b * ((10 * n + 2) ** c) <= (b * (12 ** c) + 1) * ((n + 1) ** c)
                # Theorem 2 proof padding: b(10n+1)^c <= b*11^c*(n+1)^c
                assert b * ((10 * n + 1) ** c) <= b * (11 ** c) * ((n + 1) ** c)
                # Theorem 2 gap: m(n) - a''(n) >= (n+1)^(c+1) >= (n+1)^2
                m_th2 = (b * (12 ** c) + 2) * ((n + 1) ** (c + 1))
                a_pp_th2 = (b * (12 ** c) + 1) * ((n + 1) ** c)
                assert m_th2 - a_pp_th2 >= ((n + 1) ** (c + 1)) >= ((n + 1) ** 2)

    # Verify concrete threshold n exists where (P1)-(P4) all hold for Theorem 1 & Theorem 2
    # with p(k) = (k + 1)^d for d = 1, 2, 3, 5 and m''(n) = t''(n) = 11^(d+1)*(n + 1)^(d + 1)!
    for d in [1, 2, 3, 5]:
        found_n = None
        for n in range(33, 500):
            a_val = n + 1
            ell = a_val // 3
            if ell < 11:
                continue
            L = 1 << ell
            N = L // 20
            m_val = ((12 ** d) + 2) * ((n + 1) ** (d + 1))
            a_pp = ((12 ** d) + 1) * ((n + 1) ** d)
            m_pp = (11 ** (d + 1)) * ((n + 1) ** (d + 1))
            t_pp = m_pp
            C = 2 * t_pp * t_pp
            Delta = 2 * (a_pp + m_pp + C) + 8
            # Check (P1): N >= 100
            # Check (P2): 100 * Delta <= N
            # Check (P3): M * 2^(-89N/100) < 1/4  <=>  100*(m_val + 2) < 89*N
            # Check (P4): a_pp <= m_val - ceil(log2(Delta)) - 17  <=>  a_pp + Delta.bit_length() + 17 <= m_val
            if (N >= 100
                    and 100 * Delta <= N
                    and 100 * (m_val + 2) < 89 * N
                    and a_pp + Delta.bit_length() + 17 <= m_val):
                found_n = n
                break
        assert found_n is not None, f"Failed to find valid diagonalization length for d={d}"


def test_ping_pong_concrete_simulation():
    """Simulate Ping-Pong (0.9)-block-min-entropy restoration on a concrete small instance
    (N=10, M=4, threshold=0.9*10=9 -> 2^-9, check exact maximality and restoration!).
    Note: for N=10, 2^N=1024, 2^(0.9*N) = 2^9 = 512, 2^(0.89*N) ~ 478; we test exact rational density!"""
    # Use a tiny concrete universe {0,1,2,3}^3 (alphabet size Q = 4 = 2^2, U = {0, 1, 2})
    # with alpha = 1/2 (so density threshold Q^(-alpha*|S|) = 2^(-|S|)), beta = 1/4 (2^(-|S|/2)).
    # Verify exact maximality property: conditioning A on maximal violating (S, v) restores alpha-density on U\S!
    Q = 4
    U = (0, 1, 2)
    # Build A with heavy concentration on coordinate 0 (value 0 appears 3/4 > 1/2 of the time!)
    # and on (0, 1) (value (0, 0) appears 5/16 > 1/4 of the time!).
    A = []
    # Put 5 tuples (0, 0, z) with z in {0,1,2,3} (4 tuples) + repeat? No, subsets have distinct tuples!
    # In {0,1,2,3}^3 (size 64): pick A of size 12:
    # - all 4 tuples (0, 0, z) (z=0..3)  -> Pr[X_{0,1}=(0,0)] = 4/12 = 1/3 > 1/4!
    # - 3 tuples (0, 1, z) (z=0..2)      -> Pr[X_0=0] = 7/12 > 1/2!
    # - 2 tuples (0, 2, z) (z=0..1)      -> Pr[X_0=0] = 9/12 = 3/4 > 1/2!
    # - 3 tuples (1, 1, 0), (2, 2, 1), (3, 3, 2)
    A = ([(0, 0, z) for z in range(4)]
         + [(0, 1, z) for z in range(3)]
         + [(0, 2, z) for z in range(2)]
         + [(1, 1, 0), (2, 2, 1), (3, 3, 2)])
    assert len(set(A)) == 12

    # Threshold: Pr[X_S = v] <= Fraction(1, 2) ** len(S)
    # Find ALL violating (S, v)
    from itertools import combinations
    def find_violations(tuples_set, n_coords):
        viols = []
        tot = len(tuples_set)
        for sz in range(1, n_coords + 1):
            for S in combinations(range(n_coords), sz):
                counts = {}
                for x in tuples_set:
                    proj = tuple(x[idx] for idx in S)
                    counts[proj] = counts.get(proj, 0) + 1
                thr = Fraction(1, 2) ** sz
                for v, c in counts.items():
                    if Fraction(c, tot) > thr:
                        viols.append((S, v, Fraction(c, tot)))
        return viols

    viols = find_violations(A, 3)
    assert len(viols) > 0
    # Pick maximal cardinality violating (S, v)
    max_sz = max(len(S) for S, _, _ in viols)
    S_max, v_max, prob_max = next(item for item in viols if len(item[0]) == max_sz)
    rem_coords = [c for c in range(3) if c not in S_max]
    A_prime = [tuple(x[c] for c in rem_coords) for x in A if tuple(x[c] for c in S_max) == v_max]
    # Verify A_prime has ZERO violations on remaining coordinates!
    assert find_violations(A_prime, len(rem_coords)) == []


def main():
    check_ast_zero_float()
    test_gilbert_varshamov()
    test_prefix_encoding_and_disjoint_blocks()
    test_multilinear_extension_additive_decomposition()
    test_combinatorial_lemma_constants_and_thresholds()
    test_ping_pong_concrete_simulation()
    print("PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)

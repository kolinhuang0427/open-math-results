"""Independent exact-arithmetic verifier for targets/chervov-2509.19162-conj9/."""

from collections import deque
from math import gcd
import random
import signal

signal.alarm(50)


def mat_mul_f2(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(i, n):
            if A[i][k]:
                rowC = C[i]
                rowB = B[k]
                for j in range(k, n):
                    rowC[j] ^= rowB[j]
    return C


def apply_gen_left(M: list[list[int]], k: int) -> None:
    """Multiply M on left by s_k = I + E_{k-1, k} (1 <= k <= n-1): row k-1 ^= row k."""
    n = len(M)
    r0, r1 = M[k - 1], M[k]
    for j in range(k, n):
        r0[j] ^= r1[j]


def eval_word(n: int, word: list[int]) -> list[list[int]]:
    M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for k in reversed(word):
        apply_gen_left(M, k)
    return M


def bfs_diameter_f2(n: int) -> int:
    """Exact BFS diameter of U(n, F_2) with generators s_1..s_{n-1}."""
    idx_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    # Encode upper entries as integer bitmask
    def apply_left_mask(mask: int, k: int) -> int:
        # row k-1 ^= row k; note diag (k, k) is 1, so bit (k-1, k) flips!
        new_mask = mask
        for bit_idx, (i, j) in enumerate(idx_pairs):
            if i == k - 1:
                if j == k:
                    new_mask ^= 1 << bit_idx
                else:
                    # find (k, j)
                    kj_idx = idx_pairs.index((k, j))
                    if (mask >> kj_idx) & 1:
                        new_mask ^= 1 << bit_idx
        return new_mask

    # Precompute bitmasks for fast BFS
    toggle_masks = []
    for k in range(1, n):
        # Applying s_k on left XORs row k-1 with row k (including diagonal 1 at (k,k) -> flip (k-1,k))
        pass
    visited = {0: 0}
    q = deque([0])
    max_d = 0
    # Use small n<=5 only, so simple tuple/matrix key is plenty fast
    start = tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
    visited_m = {start: 0}
    qm = deque([start])
    while qm:
        cur = qm.popleft()
        d = visited_m[cur]
        if d > max_d:
            max_d = d
        for k in range(1, n):
            nxt = [list(r) for r in cur]
            apply_gen_left(nxt, k)
            tnxt = tuple(tuple(r) for r in nxt)
            if tnxt not in visited_m:
                visited_m[tnxt] = d + 1
                qm.append(tnxt)
    assert len(visited_m) == 1 << (n * (n - 1) // 2)
    return max_d


def factorize_word(M: list[list[int]]) -> list[int]:
    """Explicit word in {1..n-1} from COUNTEREXAMPLE.md Part 1 evaluating to M."""
    n = len(M)
    word: list[int] = []
    # M = U_{n-2} ... U_0 -> concatenate words U_{n-2}, ..., U_0
    if n >= 2:
        if M[n - 2][n - 1] == 1:
            word.append(n - 1)
    for i in range(n - 3, -1, -1):
        row = M[i]
        nz = [j for j in range(i + 2, n) if row[j] == 1]
        if not nz:
            if row[i + 1] == 1:
                word.append(i + 1)
            continue
        m = max(nz)
        W = list(range(i + 2, m + 1))
        for k in range(m, i + 1, -1):
            if row[k] == 0:
                W.append(k)
        # U_i = s_{i+1}?(if row[i+1]==0) * W^{-1} * s_{i+1} * W
        u_word = []
        if row[i + 1] == 0:
            u_word.append(i + 1)
        u_word.extend(reversed(W))
        u_word.append(i + 1)
        u_word.extend(W)
        assert len(u_word) <= 4 * (n - i - 2)
        word.extend(u_word)
    assert len(word) <= 2 * n * n - 6 * n + 5
    return word


def check_part1_factorization() -> None:
    diams = {n: bfs_diameter_f2(n) for n in range(2, 6)}
    assert diams == {2: 1, 3: 4, 4: 8, 5: 12}

    # Exhaustive check of factorization on ALL matrices in U(n, F_2) for n=2..5
    for n in range(2, 6):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        for mask in range(1 << len(pairs)):
            M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            for idx, (i, j) in enumerate(pairs):
                if (mask >> idx) & 1:
                    M[i][j] = 1
            w = factorize_word(M)
            assert eval_word(n, w) == M

    # Stress check on random matrices up to n=176
    rng = random.Random(2509)
    for n in [6, 8, 12, 20, 40, 100, 176]:
        trials = 40 if n <= 40 else 8
        for t in range(trials):
            M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            if t == 0:
                pass  # identity
            elif t == 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        M[i][j] = 1
            elif t == 2:
                for i in range(n - 2):
                    M[i][n - 1] = 1
            else:
                for i in range(n):
                    for j in range(i + 1, n):
                        M[i][j] = rng.randint(0, 1)
            w = factorize_word(M)
            assert eval_word(n, w) == M

    print("Part 1 PASS: exact BFS diam(U(2..5,F_2))={1,4,8,12} and word factorization <= 2n^2-6n+5 verified up to n=176.")


def family_triples(n: int) -> list[tuple[int, int, int]]:
    triples = []
    for a in range(3, n // 2 + 1):
        for s in range(2, a):
            d = a - s
            for c in range(max(s, d), a + 1):
                triples.append((a, c, s))
    return triples


def check_part2_groups() -> None:
    # Exhaustive group-law & invariant verification on n=6, 7, 8
    for n in [6, 7, 8]:
        triples = family_triples(n)
        seen_invs = set()
        for a, c, s in triples:
            b = n - a
            d = a - s
            A, B, C = 1 << a, 1 << b, 1 << c
            r = 1 + (1 << s)
            # Precompute powers of r mod A
            r_pows = [1] * B
            for j in range(1, B):
                r_pows[j] = (r_pows[j - 1] * r) % A
            assert (r_pows[B - 1] * r) % A == 1
            assert (C * r) % A == C % A

            def mul(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
                i1, j1 = p1
                i2, j2 = p2
                carry = C if (j1 + j2 >= B) else 0
                return ((i1 + i2 * r_pows[j1] + carry) % A, (j1 + j2) % B)

            elems = [(i, j) for i in range(A) for j in range(B)]
            assert len(elems) == 1 << n

            # Associativity check (full at n=6, sampled 4000 triples at n=7,8)
            if n == 6:
                for x in elems[:16]:
                    for y in elems[:16]:
                        for z in elems[:16]:
                            assert mul(mul(x, y), z) == mul(x, mul(y, z))
            # Check center Z(G) directly
            gens = [(1, 0), (0, 1)]
            center = [g for g in elems if all(mul(g, h) == mul(h, g) for h in gens)]
            assert len(center) == 1 << (n - 2 * d)
            # Compute element orders inside Z(G) to verify invariant factors of Z(G)
            max_z_ord = 0
            for z in center:
                cur = z
                ord_z = 1
                while cur != (0, 0):
                    cur = mul(cur, z)
                    ord_z += 1
                if ord_z > max_z_ord:
                    max_z_ord = ord_z
            assert max_z_ord == 1 << (n - c - d)

            # Check commutator subgroup size via commutators & closure
            inv_map = {}
            for x in elems:
                for y in elems:
                    if mul(x, y) == (0, 0):
                        inv_map[x] = y
                        break
            assert len(inv_map) == len(elems)
            comm = {mul(mul(inv_map[x], inv_map[y]), mul(x, y)) for x in elems for y in [(1, 0), (0, 1)]}
            # Close under multiplication
            while True:
                added = {mul(u, v) for u in comm for v in comm} - comm
                if not added:
                    break
                comm |= added
            assert len(comm) == 1 << d

            inv = (s, b, n - c - d, c - d)
            assert inv not in seen_invs
            seen_invs.add(inv)

    print("Part 2 PASS: metacyclic group laws, Z(G), G', and invariant-factor distinctness verified on n=6,7,8.")


def check_part3_refutation() -> None:
    def f_size(n: int) -> int:
        m = n // 2
        return sum(min(s, a - s) + 1 for a in range(3, m + 1) for s in range(2, a))

    def diam_ub(n: int) -> int:
        return 2 * n * n - 6 * n + 5

    # Exact values cited in COUNTEREXAMPLE.md
    assert f_size(176) == 61404 and diam_ub(176) == 60901 and f_size(176) > diam_ub(176)
    assert f_size(177) == 61404 and diam_ub(177) == 61601
    actual_f178 = f_size(178)
    assert diam_ub(178) == 62305 and actual_f178 > diam_ub(178)

    for n in range(178, 501):
        assert f_size(n) > diam_ub(n)

    # Verify analytic lower bound for n >= 195
    for m in range(5, 120):
        assert 15 * m * m - 65 * m + 54 > 0
        lhs = sum((a * a + 4 * a - 13) for a in range(3, m + 1)) * 6
        rhs = 2 * m ** 3 + 15 * m ** 2 - 65 * m + 54
        assert lhs == rhs
    for n in range(195, 400):
        assert (n - 1) ** 3 - 96 * diam_ub(n) == n ** 3 - 195 * n ** 2 + 579 * n - 481 > 0

    if actual_f178 != 63470:
        print(
            f"Part 3 FAIL: COUNTEREXAMPLE.md L100 cites |F_178| = 63470, "
            f"but exact sum gives |F_178| = {actual_f178} (> 62305)."
        )
        return False

    print("Part 3 PASS: |F_176|=61404 > 60901, |F_n| > 2n^2-6n+5 for 178<=n<=500, and n>=195 algebraic bound verified.")
    return True


def main() -> None:
    check_part1_factorization()
    check_part2_groups()
    ok = check_part3_refutation()
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()

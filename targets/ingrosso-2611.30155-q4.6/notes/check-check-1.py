#!/usr/bin/env python3
"""Independent exact-arithmetic checker for targets/ingrosso-2611.30155-q4.6."""

from collections import deque
from itertools import combinations


def build_group_from_table(elems: list, mul_fn) -> dict:
    """Build exact finite group representation (0..n-1) with verified axioms."""
    n = len(elems)
    idx = {e: i for i, e in enumerate(elems)}
    mul = [[idx[mul_fn(elems[i], elems[j])] for j in range(n)] for i in range(n)]
    # Find identity
    ident = None
    for e in range(n):
        if all(mul[e][x] == x and mul[x][e] == x for x in range(n)):
            ident = e
            break
    assert ident is not None
    # Find inverses
    inv = [None] * n
    for x in range(n):
        for y in range(n):
            if mul[x][y] == ident and mul[y][x] == ident:
                inv[x] = y
                break
        assert inv[x] is not None
    # Associativity
    for a in range(n):
        for b in range(n):
            ab = mul[a][b]
            for c in range(n):
                assert mul[ab][c] == mul[a][mul[b][c]]
    return {"n": n, "elems": elems, "mul": mul, "inv": inv, "id": ident}


def closure(G: dict, gens: set[int] | frozenset[int]) -> frozenset[int]:
    mul = G["mul"]
    inv = G["inv"]
    res = {G["id"]}
    for g in gens:
        res.add(g)
        res.add(inv[g])
    q = deque(res)
    while q:
        a = q.popleft()
        for b in list(res):
            for x in (mul[a][b], mul[b][a]):
                if x not in res:
                    res.add(x)
                    q.append(x)
    return frozenset(res)


def all_subgroups(G: dict) -> list[frozenset[int]]:
    n = G["n"]
    subs = {frozenset([G["id"]])}
    frontier = [frozenset([G["id"]])]
    while frontier:
        cur = frontier.pop()
        for g in range(n):
            if g not in cur:
                nxt = closure(G, cur | {g})
                if nxt not in subs:
                    subs.add(nxt)
                    frontier.append(nxt)
    return sorted(subs, key=lambda s: (len(s), sorted(s)))


def conj_set(G: dict, K: frozenset[int], g: int) -> frozenset[int]:
    mul = G["mul"]
    gi = G["inv"][g]
    return frozenset(mul[mul[gi][k]][g] for k in K)


def normalizer(G: dict, K: frozenset[int]) -> frozenset[int]:
    return frozenset(g for g in range(G["n"]) if conj_set(G, K, g) == K)


def pronormalizer(G: dict, K: frozenset[int]) -> frozenset[int]:
    res = set()
    for y in range(G["n"]):
        Ky = conj_set(G, K, y)
        J = closure(G, K | Ky)
        if any(conj_set(G, K, u) == Ky for u in J):
            res.add(y)
    return frozenset(res)


def subnormal_defect(G: dict, H: frozenset[int], subs: list[frozenset[int]]) -> int | None:
    """Exact BFS on normalizer-chain / subgroup lattice for minimum subnormal defect d."""
    if len(H) == G["n"]:
        return 0
    full = frozenset(range(G["n"]))
    # H = H_0 <| H_1 <| ... <| H_d = G
    # Equivalently, H_{i+1} <= N_G(H_i) and H_i <= H_{i+1}.
    dist = {H: 0}
    q = deque([H])
    while q:
        cur = q.popleft()
        d = dist[cur]
        if cur == full:
            return d
        norm = normalizer(G, cur)
        for nxt in subs:
            if cur.issubset(nxt) and nxt.issubset(norm) and nxt not in dist:
                dist[nxt] = d + 1
                q.append(nxt)
    return None


def analyze_group(G: dict, name: str) -> dict:
    n = G["n"]
    subs = all_subgroups(G)
    full = frozenset(range(n))
    p_sets = {K: pronormalizer(G, K) for K in subs}
    n_sets = {K: normalizer(G, K) for K in subs}

    # Norm N(G) = intersection of N_G(K), Pro-norm N_pro(G) = intersection of P_G(K)
    norm_G = frozenset.intersection(*n_sets.values())
    pronorm_G = frozenset.intersection(*p_sets.values())

    # Check Lemma 2: N_pro(G) is normal (conjugation-invariant)
    assert conj_set(G, pronorm_G, 0) == pronorm_G
    for g in range(n):
        assert conj_set(G, pronorm_G, g) == pronorm_G

    # Check Lemma 1: for every subnormal subgroup K, P_G(K) == N_G(K)
    defects = {}
    for K in subs:
        d = subnormal_defect(G, K, subs)
        defects[K] = d
        if d is not None:
            assert p_sets[K] == n_sets[K], f"{name}: Lemma 1 failed on {K}"

    # Check hypothesis: every subgroup K is pronormal (P_G(K) == G) or K <= N_pro(G)
    satisfies_hyp = all((p_sets[K] == full) or K.issubset(pronorm_G) for K in subs)
    max_defect = max(d for d in defects.values() if d is not None)
    if satisfies_hyp:
        assert max_defect <= 2, f"{name}: Upper bound defect <= 2 failed: {max_defect}"
        # Also verify K <| K^G <| G for every subnormal K
        for K, d in defects.items():
            if d is not None:
                K_G = closure(G, set().union(*(conj_set(G, K, g) for g in range(n))))
                assert K_G.issubset(n_sets[K])
                assert n_sets[K_G] == full

    print(f"{name} (|G|={n}, #subs={len(subs)}, |N|={len(norm_G)}, |N_pro|={len(pronorm_G)}, hyp={satisfies_hyp}, max_defect={max_defect}): OK")
    return {
        "subs": subs,
        "p_sets": p_sets,
        "n_sets": n_sets,
        "norm": norm_G,
        "pronorm": pronorm_G,
        "defects": defects,
        "satisfies_hyp": satisfies_hyp,
        "max_defect": max_defect,
    }


def main() -> None:
    # 1. Primary tightness witness: M_{16} = <a, x | a^8 = x^2 = 1, x^-1 a x = a^5>
    # Elements (i, j) = x^i * a^j with i in {0,1}, j in {0..7}:
    # (x^i a^j)(x^k a^l) = x^{i+k mod 2} a^{j * 5^k + l mod 8}
    m16_elems = [(i, j) for i in range(2) for j in range(8)]

    def m16_mul(u, v):
        i, j = u
        k, l = v
        return ((i + k) % 2, (j * (5 if k == 1 else 1) + l) % 8)

    M16 = build_group_from_table(m16_elems, m16_mul)
    res_m16 = analyze_group(M16, "M_16")
    assert res_m16["satisfies_hyp"] is True
    assert res_m16["max_defect"] == 2
    assert len(res_m16["norm"]) == 8 and res_m16["norm"] == res_m16["pronorm"]

    # Check exact subgroup claims in PROOF.md Section 3:
    idx_x = m16_elems.index((1, 0))
    idx_a4 = m16_elems.index((0, 4))
    idx_xa4 = m16_elems.index((1, 4))
    H_x = closure(M16, {idx_x})
    H_xa4 = closure(M16, {idx_xa4})
    assert len(H_x) == 2 and len(H_xa4) == 2
    # Every nontrivial subgroup not containing a^4 is {H_x, H_xa4}, and all others contain a^4 and are normal!
    non_a4 = [K for K in res_m16["subs"] if len(K) > 1 and idx_a4 not in K]
    assert set(non_a4) == {H_x, H_xa4}
    for K in res_m16["subs"]:
        if idx_a4 in K:
            assert res_m16["n_sets"][K] == frozenset(range(16))
    assert res_m16["defects"][H_x] == 2
    assert res_m16["defects"][H_xa4] == 2
    # Verify H^G = <x, a^4>
    H_G = closure(M16, {idx_x, idx_a4})
    assert len(H_G) == 4
    assert res_m16["n_sets"][H_G] == frozenset(range(16))
    assert H_G.issubset(res_m16["n_sets"][H_x])

    # 2. Additional sanity checks on groups from the paper:
    # (a) Dih(8) should FAIL the hypothesis (paper Section 2, line 257)
    d8_elems = [(i, j) for i in range(2) for j in range(4)]
    D8 = build_group_from_table(d8_elems, lambda u, v: ((u[0] + v[0]) % 2, (u[1] * (3 if v[0] else 1) + v[1]) % 4))
    res_d8 = analyze_group(D8, "D_8")
    assert res_d8["satisfies_hyp"] is False

    # (b) S_3 x S_3 (order 36, |N_pro| = 18 per paper line 289)
    s3_elems = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    s3xs3_elems = [(p1, p2) for p1 in s3_elems for p2 in s3_elems]
    S3xS3 = build_group_from_table(
        s3xs3_elems,
        lambda u, v: (tuple(u[0][v[0][i]] for i in range(3)), tuple(u[1][v[1][i]] for i in range(3))),
    )
    res_s3 = analyze_group(S3xS3, "S_3 x S_3")
    assert res_s3["satisfies_hyp"] is True
    assert len(res_s3["pronorm"]) == 18

    # (c) Non-nilpotent group of order 48: M_16 \ltimes C_3 (with a acting trivially, x inverting C_3)
    # (i, j, c) in {0,1} x Z_8 x Z_3: x^-1 c x = -c mod 3, a^-1 c a = c
    g48_elems = [(i, j, c) for i in range(2) for j in range(8) for c in range(3)]

    def g48_mul(u, v):
        i, j, c = u
        k, l, d = v
        return ((i + k) % 2, (j * (5 if k == 1 else 1) + l) % 8, (c * (2 if k == 1 else 1) + d) % 3)

    G48 = build_group_from_table(g48_elems, g48_mul)
    res_g48 = analyze_group(G48, "M_16 x| C_3")
    assert res_g48["satisfies_hyp"] is True
    assert res_g48["max_defect"] == 2

    print("PASS")


if __name__ == "__main__":
    main()

"""Exact integer verification for Question 4.6 of arXiv:2611.30155v1.

Verifies (zero floating-point arithmetic):
1. M_16 (order 16): every subgroup is pronormal or <= N_pro(M_16),
   and <x> has exact subnormal defect 2.
2. P_27 (order 27) and M_16 <| C_3 (order 48): same property,
   Lemma 1 (P_G(H) == N_G(H) for every subnormal H), and max defect == 2.
"""

import sys
from collections import deque


def build_semidirect_mod(i_mod: int, j_mod: int, a_mult: int, c_mod: int = 1, c_mult: int = 1):
    elts = [(i, j, c) for i in range(i_mod) for j in range(j_mod) for c in range(c_mod)]
    idx = {p: k for k, p in enumerate(elts)}
    m = len(elts)
    mul = [[0] * m for _ in range(m)]
    inv = [0] * m
    for a_i, (i1, j1, c1) in enumerate(elts):
        for b_i, (i2, j2, c2) in enumerate(elts):
            # (x^i1 a^j1 c^c1)(x^i2 a^j2 c^c2) = x^{i1+i2} a^{j1*a_mult^i2 + j2} c^{c1*c_mult^i2 + c2}
            p = (
                (i1 + i2) % i_mod,
                (j1 * pow(a_mult, i2, j_mod) + j2) % j_mod,
                (c1 * pow(c_mult, i2, c_mod) + c2) % c_mod,
            )
            prod = idx[p]
            mul[a_i][b_i] = prod
            if prod == 0:
                inv[a_i] = b_i
    return elts, mul, inv


def close_subgroup(m: int, mul, gens) -> frozenset:
    s = {0}
    elts = [0]
    for g in gens:
        if g not in s:
            s.add(g)
            elts.append(g)
    idx = 0
    while idx < len(elts):
        a = elts[idx]
        idx += 1
        for b in list(elts):
            for c in (mul[a][b], mul[b][a]):
                if c not in s:
                    s.add(c)
                    elts.append(c)
    return frozenset(s)


def all_subgroups(m: int, mul) -> list:
    cycs = []
    seen = set()
    for g in range(m):
        s = {0}
        x = g
        while x not in s:
            s.add(x)
            x = mul[x][g]
        fs = frozenset(s)
        if fs not in seen:
            seen.add(fs)
            cycs.append(fs)
    subs = list(cycs)
    i = 0
    while i < len(subs):
        H = subs[i]
        i += 1
        for C in cycs:
            if C.issubset(H):
                continue
            U = close_subgroup(m, mul, H | C)
            if U not in seen:
                seen.add(U)
                subs.append(U)
    subs.sort(key=len)
    return subs


def verify_group(name: str, elts, mul, inv, expected_subs: int, expected_npro: int, expected_max_def: int) -> None:
    m = len(elts)
    subs = all_subgroups(m, mul)
    assert len(subs) == expected_subs, f"{name}: got {len(subs)} subs, expected {expected_subs}"

    def conj(H, g):
        gi = inv[g]
        return frozenset(mul[mul[gi][h]][g] for h in H)

    npro = set(range(m))
    pronormal = {}
    for H in subs:
        is_pro = True
        for g in range(m):
            Hg = conj(H, g)
            if Hg == H:
                continue
            K = close_subgroup(m, mul, H | Hg)
            if not any(conj(H, u) == Hg for u in K):
                is_pro = False
                npro.discard(g)
        pronormal[H] = is_pro

    assert len(npro) == expected_npro, f"{name}: |N_pro|={len(npro)}, expected {expected_npro}"
    for H in subs:
        assert pronormal[H] or H.issubset(npro), f"{name}: subgroup of order {len(H)} violates property"

    full = frozenset(range(m))
    max_def = 0
    def2_examples = []
    for H in subs:
        # Subnormal defect via descending normal closure chain H_0 = G, H_{i+1} = H^{H_i}
        cur = full
        d = 0
        while cur != H:
            nxt = close_subgroup(m, mul, set().union(*(conj(H, g) for g in cur)))
            if nxt == cur:
                d = -1
                break
            cur = nxt
            d += 1
        if d >= 0:
            # Verify Lemma 1: for subnormal H, P_G(H) == N_G(H)
            p_set = set()
            n_set = set()
            for g in range(m):
                Hg = conj(H, g)
                if Hg == H:
                    n_set.add(g)
                    p_set.add(g)
                else:
                    K = close_subgroup(m, mul, H | Hg)
                    if any(conj(H, u) == Hg for u in K):
                        p_set.add(g)
            assert p_set == n_set, f"{name}: Lemma 1 failed on order {len(H)}"
            # Verify H <= H^G <= N_G(H) (defect <= 2)
            HG = close_subgroup(m, mul, set().union(*(conj(H, g) for g in full)))
            assert HG.issubset(n_set), f"{name}: H not normal in H^G"
            if d > max_def:
                max_def = d
            if d == 2:
                def2_examples.append(H)

    assert max_def == expected_max_def, f"{name}: max_def={max_def}, expected {expected_max_def}"
    print(f"{name}: |G|={m}, |subs|={len(subs)}, |N_pro|={len(npro)}, max_defect={max_def}, #defect2={len(def2_examples)} OK")


def main() -> None:
    # 1. M_16 = <x> <| <a>, o(x)=2, o(a)=8, x^-1 a x = a^5
    e16, m16, i16 = build_semidirect_mod(2, 8, 5)
    verify_group("M_16", e16, m16, i16, expected_subs=11, expected_npro=8, expected_max_def=2)

    # Check explicitly that <x> has defect 2 in M_16
    idx_x = e16.index((1, 0, 0))
    idx_a = e16.index((0, 1, 0))
    Hx = frozenset({0, idx_x})
    assert m16[m16[i16[idx_a]][idx_x]][idx_a] not in Hx, "<x> must not be normal in M_16"

    # 2. P_27 = <x> <| <a>, o(x)=3, o(a)=9, x^-1 a x = a^4
    e27, m27, i27 = build_semidirect_mod(3, 9, 4)
    verify_group("P_27", e27, m27, i27, expected_subs=10, expected_npro=9, expected_max_def=2)

    # 3. M_16 <| C_3 (order 48, x inverts C_3, a centralizes C_3)
    e48, m48, i48 = build_semidirect_mod(2, 8, 5, c_mod=3, c_mult=2)
    verify_group("M_16 <| C_3", e48, m48, i48, expected_subs=36, expected_npro=24, expected_max_def=2)

    print("PASS")


if __name__ == "__main__":
    main()

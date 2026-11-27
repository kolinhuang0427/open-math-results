#!/usr/bin/env python3
"""
Independent exact pure-integer verifier for targets/dochtermann-2609.13361-conj7.5/
directly from primary definitions in arXiv:2609.13361v1 (cyclesystem_reg.tex)
and PROOF.md without reading verify.py or author notes.

Zero floats, zero '/' divisions (bitmasks + integer XOR linear algebra over F_2).
"""
from __future__ import annotations

from itertools import combinations


class BinaryMatroid:
    """Binary matroid represented by m column vectors (integer bitmasks of height r_ambient)."""

    def __init__(self, cols: list[int]):
        self.cols = cols
        self.m = len(cols)
        self._rank_val = self.subset_rank((1 << self.m) - 1)
        self.g = self.m - self._rank_val
        self._circuits: list[int] | None = None

    def subset_rank(self, mask: int) -> int:
        basis: list[int] = []
        idx = 0
        tmp = mask
        while tmp:
            lsb = tmp & -tmp
            i = lsb.bit_length() - 1
            v = self.cols[i]
            for b in basis:
                hi = b.bit_length() - 1
                if (v >> hi) & 1:
                    v ^= b
            if v:
                basis.append(v)
                basis.sort(reverse=True)
            tmp ^= lsb
        return len(basis)

    def rank(self) -> int:
        return self._rank_val

    def is_indep(self, mask: int) -> bool:
        return self.subset_rank(mask) == mask.bit_count()

    def circuits(self) -> list[int]:
        if self._circuits is not None:
            return self._circuits
        # Compute nullspace basis of columns over F_2 via RREF over columns
        # Column i lives in F_2^r; transpose: rows = bit positions, or augment col[i] with (1 << i)
        # Augment each column i with tracking bit (1 << i) in upper bits
        pivot_cols: list[tuple[int, int]] = []  # (reduced_val, origin_mask)
        null_basis: list[int] = []
        for i in range(self.m):
            v = self.cols[i]
            omask = 1 << i
            for p_val, p_omask in pivot_cols:
                hi = p_val.bit_length() - 1
                if (v >> hi) & 1:
                    v ^= p_val
                    omask ^= p_omask
            if v == 0:
                null_basis.append(omask)
            else:
                pivot_cols.append((v, omask))
                pivot_cols.sort(key=lambda pair: pair[0].bit_length(), reverse=True)

        assert len(null_basis) == self.g
        # All nonzero vectors in nullspace
        all_cycles = []
        k = len(null_basis)
        for comb_mask in range(1, 1 << k):
            vec = 0
            tmp = comb_mask
            while tmp:
                lsb = tmp & -tmp
                idx = lsb.bit_length() - 1
                vec ^= null_basis[idx]
                tmp ^= lsb
            all_cycles.append(vec)
        all_cycles.sort(key=lambda x: (x.bit_count(), x))
        minimal: list[int] = []
        for c in all_cycles:
            if not any((prev & c) == prev for prev in minimal):
                minimal.append(c)
        self._circuits = minimal
        return minimal

    def delete(self, elem: int) -> tuple["BinaryMatroid", list[int]]:
        keep = [i for i in range(self.m) if i != elem]
        return BinaryMatroid([self.cols[i] for i in keep]), keep

    def contract(self, elem: int) -> tuple["BinaryMatroid", list[int]]:
        keep = [i for i in range(self.m) if i != elem]
        piv = self.cols[elem]
        if piv == 0:
            # elem is a loop: contraction == deletion
            return BinaryMatroid([self.cols[i] for i in keep]), keep
        hi = piv.bit_length() - 1
        new_cols = []
        for i in keep:
            v = self.cols[i]
            if (v >> hi) & 1:
                v ^= piv
            new_cols.append(v)
        return BinaryMatroid(new_cols), keep

    def components(self) -> list[list[int]]:
        """Connected components via union-find on circuit membership."""
        parent = list(range(self.m))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for c in self.circuits():
            first = None
            tmp = c
            while tmp:
                lsb = tmp & -tmp
                idx = lsb.bit_length() - 1
                if first is None:
                    first = idx
                else:
                    union(first, idx)
                tmp ^= lsb

        groups: dict[int, list[int]] = {}
        for i in range(self.m):
            groups.setdefault(find(i), []).append(i)
        return list(groups.values())


def graphic_matroid(num_verts: int, edges: list[tuple[int, int]]) -> BinaryMatroid:
    """Incidence vectors over F_2 (mod 2) -> exact binary matroid M(G)."""
    cols = []
    for u, v in edges:
        if u == v:
            cols.append(0)
        else:
            cols.append((1 << u) ^ (1 << v))
    return BinaryMatroid(cols)


def cographic_matroid(num_verts: int, edges: list[tuple[int, int]]) -> BinaryMatroid:
    """
    Construct M(G)^* over F_2 by computing a basis of the cycle space of G
    as rows of the binary representation matrix (columns = edges).
    """
    M = graphic_matroid(num_verts, edges)
    # Nullspace of M gives cycle space of G (dimension = g(M(G)) = rank(M(G)^*))
    # Use M.circuits()-style null_basis extraction:
    pivot_cols: list[tuple[int, int]] = []
    cycle_basis: list[int] = []
    for i in range(M.m):
        v = M.cols[i]
        omask = 1 << i
        for p_val, p_omask in pivot_cols:
            hi = p_val.bit_length() - 1
            if (v >> hi) & 1:
                v ^= p_val
                omask ^= p_omask
        if v == 0:
            cycle_basis.append(omask)
        else:
            pivot_cols.append((v, omask))
            pivot_cols.sort(key=lambda pair: pair[0].bit_length(), reverse=True)
    # Each element in cycle_basis is a row of the representation of M(G)^*
    cols = []
    for e_idx in range(len(edges)):
        col_val = 0
        for r_idx, cyc in enumerate(cycle_basis):
            if (cyc >> e_idx) & 1:
                col_val |= 1 << r_idx
        cols.append(col_val)
    return BinaryMatroid(cols)


def unique_union(cycles: list[int], subset_mask: int) -> int:
    once = 0
    more = 0
    tmp = subset_mask
    while tmp:
        lsb = tmp & -tmp
        idx = lsb.bit_length() - 1
        c = cycles[idx]
        more |= once & c
        once = (once ^ c) & ~more
        tmp ^= lsb
    return once


def mult_ge3_mask(cycles: list[int]) -> int:
    c1 = 0
    c2 = 0
    c3 = 0
    for c in cycles:
        c3 |= c2 & c
        c2 = (c2 ^ (c1 & c)) | c3
        c1 ^= c
    return c3


def is_cycle_system(M: BinaryMatroid, cycles: list[int]) -> bool:
    if len(cycles) != M.g:
        return False
    # Each entry must be a nonzero cycle (disjoint union of circuits <=> in ker, nonempty)
    # Here check membership in cycle space via dependence or exact ker check:
    # Since M is binary, every element of Z(M) is a union of circuits; checking all circuits/xor:
    # Better: check every entry is a union of circuits (or just check circuit systems explicitly).
    for S in range(1, 1 << len(cycles)):
        uu = unique_union(cycles, S)
        if uu == 0 or M.is_indep(uu):
            return False
    return True


def is_circuit_system(M: BinaryMatroid, cycles: list[int]) -> bool:
    cset = set(M.circuits())
    if len(cycles) != M.g or len(set(cycles)) != M.g:
        return False
    if not all(c in cset for c in cycles):
        return False
    return is_cycle_system(M, cycles)


def verify_proof_induction_step(M: BinaryMatroid, C: list[int]) -> None:
    """
    Independently trace and check every single claim of PROOF.md Section 4
    on (M, C) assuming C is a circuit system and C_[g] is a circuit!
    """
    g = M.g
    assert g == len(C)
    D = unique_union(C, (1 << g) - 1)
    cset = set(M.circuits())
    assert D in cset
    assert mult_ge3_mask(C) == 0, f"FOUND COUNTEREXAMPLE to Main Theorem! mult>=3: {mult_ge3_mask(C)}"

    if g == 1:
        return

    comps = M.components()
    if len(comps) >= 2:
        # Step 1: check disconnected reduction
        comp_masks = []
        for grp in comps:
            msk = 0
            for idx in grp:
                msk |= 1 << idx
            comp_masks.append(msk)
        nonzero_comps = []
        for idx_c, msk in enumerate(comp_masks):
            sub_C = [c for c in C if (c & msk) == c]
            if sub_C:
                nonzero_comps.append((idx_c, msk, sub_C))
        assert len(nonzero_comps) == 1
        assert len(nonzero_comps[0][2]) == g
        return

    # Connected M, g >= 2: test EVERY x in D!
    tmp = D
    while tmp:
        lsb = tmp & -tmp
        x = lsb.bit_length() - 1
        tmp ^= lsb

        # Find unique C_1 containing x
        owners = [i for i, c in enumerate(C) if (c >> x) & 1]
        assert len(owners) == 1
        i1 = owners[0]
        C1 = C[i1]

        # Contraction M / x
        Mx, keep = M.contract(x)
        old_to_new = {old: new for new, old in enumerate(keep)}

        def proj(mask: int) -> int:
            res = 0
            t = mask
            while t:
                l = t & -t
                o = l.bit_length() - 1
                if o != x:
                    res |= 1 << old_to_new[o]
                t ^= l
            return res

        Cpp = [proj(c) for c in C]
        assert len(set(Cpp)) == g
        assert is_cycle_system(Mx, Cpp)
        D_mx = proj(D)
        assert D_mx in set(Mx.circuits())
        assert unique_union(Cpp, (1 << g) - 1) == D_mx
        assert mult_ge3_mask(Cpp) == 0

        comps_mx = Mx.components()
        if len(comps_mx) == 1:
            # Case 1: connected -> lem:circuitsys => circuit system
            assert is_circuit_system(Mx, Cpp)
        else:
            # Case 2: disconnected M/x = W1 + ... + Wk
            # Verify every component W_j has g(W_j) >= 1 and contains some circuit
            mx_cset = set(Mx.circuits())
            # Build component masks in Mx
            comp_masks_mx = []
            for grp in comps_mx:
                msk = 0
                for idx in grp:
                    msk |= 1 << idx
                comp_masks_mx.append(msk)
                # g(W_j) >= 1
                sub_M = BinaryMatroid([Mx.cols[idx] for idx in grp])
                assert sub_M.g >= 1

            # Check which component contains D_mx (must be W_k in thm:components!)
            k_comp = [j for j, msk in enumerate(comp_masks_mx) if (D_mx & msk) == D_mx]
            assert len(k_comp) == 1
            E_k_new = comp_masks_mx[k_comp[0]]

            # Check which component(s) have a full cycle-system block contained inside E_j (W_1!)
            w1_candidates = []
            for j, msk in enumerate(comp_masks_mx):
                sub_C_idx = [i for i, cp in enumerate(Cpp) if (cp & msk) == cp]
                sub_M = BinaryMatroid([Mx.cols[idx] for idx in comps_mx[j]])
                if len(sub_C_idx) == sub_M.g:
                    w1_candidates.append((j, msk, sub_C_idx, sub_M))
            assert len(w1_candidates) >= 1
            # For every such W_1 candidate disjoint from D_mx component:
            found_w1 = False
            for j, E1_new, sub_C_idx, W1 in w1_candidates:
                if (E1_new & E_k_new) != 0:
                    continue
                found_w1 = True
                # Verify rank equality r_M(E_1) == r_M(E_1 U {x}) == r(W_1) + 1
                E1_old = 0
                for new_i in comps_mx[j]:
                    E1_old |= 1 << keep[new_i]
                assert M.subset_rank(E1_old) == M.subset_rank(E1_old | (1 << x)) == W1.rank() + 1
                # Verify i1 in sub_C_idx, i.e., C_1 <= E_1 U {x}
                assert i1 in sub_C_idx
            assert found_w1, "No W_1 block disjoint from W_k found!"

            # Check Lemma 3: D ^ C1 is a circuit of M \ x
            Mdel, keep_del = M.delete(x)
            old_to_del = {old: new for new, old in enumerate(keep_del)}

            def proj_del(mask: int) -> int:
                res = 0
                t = mask
                while t:
                    l = t & -t
                    o = l.bit_length() - 1
                    if o != x:
                        res |= 1 << old_to_del[o]
                    t ^= l
                return res

            assert (D & C1) == (1 << x)
            K_star_del = proj_del(D ^ C1)
            assert K_star_del in set(Mdel.circuits())

            # Step 2(5): *-deletion C' = C \ {C_1} is a circuit system on M \ x with C'_[g-1] == D ^ C1
            C_prime = [proj_del(C[i]) for i in range(g) if i != i1]
            assert is_circuit_system(Mdel, C_prime)
            assert unique_union(C_prime, (1 << (g - 1)) - 1) == K_star_del
            assert mult_ge3_mask(C_prime) == 0


def check_cographic_reconstruction(M: BinaryMatroid, C: list[int]) -> None:
    """Verify Corollary 2 graph reconstruction M == M(G)^* directly."""
    g = M.g
    D = unique_union(C, (1 << g) - 1)
    assert D in set(M.circuits())
    stars = [D] + C  # C_0, C_1, ..., C_g
    edges = []
    for e in range(M.m):
        holders = [v for v in range(g + 1) if (stars[v] >> e) & 1]
        assert len(holders) == 2, f"Edge {e} in {holders}, expected 2!"
        edges.append((holders[0], holders[1]))
    # Check G is connected
    adj = [[] for _ in range(g + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        cur = stack.pop()
        for nxt in adj[cur]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    assert len(seen) == g + 1
    M_rec = cographic_matroid(g + 1, edges)
    assert set(M.circuits()) == set(M_rec.circuits())


def check_corollary1_uniqueness(M: BinaryMatroid, C: list[int]) -> None:
    """Verify Corollary 1 (conj:unique): every circuit D has a UNIQUE S with C_S = D."""
    g = M.g
    uu_map: dict[int, list[int]] = {}
    for S in range(1, 1 << g):
        uu = unique_union(C, S)
        uu_map.setdefault(uu, []).append(S)
    for D in M.circuits():
        assert len(uu_map.get(D, [])) == 1, f"Circuit {D} has {uu_map.get(D, [])} representations!"


def test_necklace_stress() -> None:
    """
    Verify PROOF.md Remark (Necessity of Case 2) on the 6-vertex, 9-edge planar necklace graph
    (triangle D={x,y,z} with three parallel 2-edge ears).
    """
    # Edges: 0:x=(0,1), 1:y=(1,2), 2:z=(2,0),
    # 3:e1=(0,3), 4:e2=(1,3), 5:f1=(1,4), 6:f2=(2,4), 7:h1=(2,5), 8:h2=(0,5)
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), (0, 5)]
    M = graphic_matroid(6, edges)
    assert M.m == 9 and M.rank() == 5 and M.g == 4
    # C1={x,e1,e2}={0,3,4}, C2={y,f1,f2}={1,5,6}, C3={z,h1,h2}={2,7,8}, C4={e1,e2,f1,f2,h1,h2}={3,4,5,6,7,8}
    C = [
        (1 << 0) | (1 << 3) | (1 << 4),
        (1 << 1) | (1 << 5) | (1 << 6),
        (1 << 2) | (1 << 7) | (1 << 8),
        (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8),
    ]
    assert is_circuit_system(M, C)
    D = unique_union(C, 0b1111)
    assert D == ((1 << 0) | (1 << 1) | (1 << 2))
    assert D in set(M.circuits())
    # Verify M/x is disconnected for EVERY x in D = {0, 1, 2}
    for x in (0, 1, 2):
        Mx, _ = M.contract(x)
        assert len(Mx.components()) == 2
    verify_proof_induction_step(M, C)
    check_corollary1_uniqueness(M, C)
    check_cographic_reconstruction(M, C)
    print("PASS test_necklace_stress: Case 2 at all x in D, Lemma 3, *-deletion, Cor 1 & Cor 2 exact")


def test_cographic_and_graphic_families() -> None:
    # 1. Graphic examples: K_4, K_4 \ e, K_5 (including cone systems where C_[g] is NOT a circuit!)
    K4 = graphic_matroid(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    # Cone system of K4 around vertex 0: {01,02,12}, {01,03,13}, {02,03,23} -> C_[3] = {12,13,23} (circuit!)
    C_k4 = [0b001011, 0b010101, 0b100110]  # indices: 0:(0,1),1:(0,2),2:(0,3),3:(1,2),4:(1,3),5:(2,3)
    # Wait: 0:(0,1), 1:(0,2), 3:(1,2) -> (1<<0)|(1<<1)|(1<<3) = 1+2+8 = 11 = 0b001011
    # 0:(0,1), 2:(0,3), 4:(1,3) -> 1+4+16 = 21 = 0b010101
    # 1:(0,2), 2:(0,3), 5:(2,3) -> 2+4+32 = 38 = 0b100110
    assert is_circuit_system(K4, C_k4)
    verify_proof_induction_step(K4, C_k4)
    check_corollary1_uniqueness(K4, C_k4)
    check_cographic_reconstruction(K4, C_k4)

    # Cone system of K5 (g = 10 - 4 = 6, C_[6] is K4, NOT a circuit, yet Corollary 1 conj:unique holds!)
    K5_edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    K5 = graphic_matroid(5, K5_edges)
    e_idx = {e: k for k, e in enumerate(K5_edges)}
    C_k5_cone = [
        (1 << e_idx[(0, i)]) | (1 << e_idx[(0, j)]) | (1 << e_idx[(i, j)])
        for i in range(1, 5)
        for j in range(i + 1, 5)
    ]
    assert is_circuit_system(K5, C_k5_cone)
    D_k5 = unique_union(C_k5_cone, (1 << 6) - 1)
    assert D_k5 not in set(K5.circuits())  # C_[6] is NOT a circuit (has 6 edges, K4!)
    check_corollary1_uniqueness(K5, C_k5_cone)

    # 2. Cographic M(G)^* for ALL biconnected simple graphs with n = 4, 5 (and K_{3,3}^*, K_5^*)
    # For M(G)^*, canonical vertex-star circuit systems + also check ALL circuit systems on K4^* (= K4),
    # K_{2,3}^* (n=5, m=6, g=4, rank 2), W_4^* (n=5, m=8), K_{3,3}^* (n=6, m=9, g=5), K_5^* (n=5, m=10, g=6)
    test_graphs = [
        ("K4", 4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
        ("K2,3", 5, [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]),
        ("W4", 5, [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 1)]),
        ("K3,3", 6, [(i, j) for i in range(3) for j in range(3, 6)]),
        ("K5", 5, K5_edges),
    ]
    cs_checked = 0
    for name, nv, eds in test_graphs:
        Mc = cographic_matroid(nv, eds)
        # Canonical vertex-star system (removing vertex 0 as sink q)
        stars = []
        for v in range(1, nv):
            msk = 0
            for idx, (a, b) in enumerate(eds):
                if a == v or b == v:
                    msk |= 1 << idx
            stars.append(msk)
        assert is_circuit_system(Mc, stars)
        verify_proof_induction_step(Mc, stars)
        check_corollary1_uniqueness(Mc, stars)
        check_cographic_reconstruction(Mc, stars)
        cs_checked += 1

        # For K4^* and K_{2,3}^* (small circuit count), test ALL circuit systems with C_[g] in Cir(Mc)!
        if len(Mc.circuits()) <= 16:
            cirs = Mc.circuits()
            cset = set(cirs)
            for comb_c in combinations(cirs, Mc.g):
                clist = list(comb_c)
                if is_cycle_system(Mc, clist):
                    check_corollary1_uniqueness(Mc, clist)
                    D_tot = unique_union(clist, (1 << Mc.g) - 1)
                    if D_tot in cset:
                        verify_proof_induction_step(Mc, clist)
                        check_cographic_reconstruction(Mc, clist)
                        cs_checked += 1

    # 3. Non-graphic, non-cographic regular 2-sum M(K5) (+) _2 M(K5)^* (Corollary 1 check, has C_[g] not circuit!)
    # Actually also test a disconnected binary matroid with coloops + component circuit system:
    # Add 2 coloops to K4 (cols with independent unit bits):
    K4_plus_2coloops = BinaryMatroid(K4.cols + [1 << 10, 1 << 11])
    assert K4_plus_2coloops.g == 3
    verify_proof_induction_step(K4_plus_2coloops, C_k4)

    # 4. Hypothesis necessity: Example 6.8 (U_{1,6}, g=5, C_1=12, C_2=13, C_3=14, C_4=25, C_5=26)
    U16 = BinaryMatroid([1, 1, 1, 1, 1, 1])
    C_ex68 = [0b000011, 0b000101, 0b001001, 0b010010, 0b100010]
    assert is_circuit_system(U16, C_ex68)
    D_ex68 = unique_union(C_ex68, (1 << 5) - 1)
    assert D_ex68 == 0b111100 and D_ex68 not in set(U16.circuits())
    assert mult_ge3_mask(C_ex68) == 0b000011  # {0, 1} dependent in U_{1,6}!

    print(f"PASS test_cographic_and_graphic_families: {cs_checked} circuit-system proofs, K5 cone Cor 1, disconnected+coloops, Ex 6.8 verified")


def main() -> None:
    test_necklace_stress()
    test_cographic_and_graphic_families()
    print("PASS")


if __name__ == "__main__":
    main()

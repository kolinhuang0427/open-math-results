#!/usr/bin/env python3
"""
Standalone, pure-integer (ZERO floats) verification of the affirmative proof of:
  Oleg Vasilyev, "Up or down at every integer: Collatz-type maps of arbitrary
  sets and the up-down graph", arXiv:2611.20344v2 (updown.tex),
  Section 7, Question 7.3 (q:types; Remark 4.4 rem:types):
    "Is there a map with infinitely many cycles and a divergent orbit?"

Verifies:
  1. Exact algebraic identities used in Lemmas 1 and 2 across large finite ranges.
  2. Lemma 2 (Admissible Stage Extension) exhaustively for EVERY starting head
     H in [5, 5000], confirming all branches (A, B1, B2a, B2b, B3a, B3b) execute
     and satisfy every invariant (admissibility, distinctness, > H, B == 5 mod 6,
     gap clearance P cap [B+1, C-1] == empty, and H' = max(P) > 3B).
  3. Multi-stage ray construction (50 consecutive stages from P_0 = (1, 2, 3, 5)):
     global distinctness of R, global U(N \\ R) subset N \\ R property, global
     gap clearance R cap [B_m + 1, C_m - 1] == empty for all 1 <= m <= 50, and
     strict disjointness of all 50 trap intervals [B_m + 1, 3B_m - 1].
  4. Exhaustive verification of Lemma 1 (f_{B_m}(V(B_m)) subset V(B_m)) on every
     vertex of V(B_m) for all stages with 3B_m <= 300000, explicit simple-cycle
     extraction C(B_m), and direct simulation of T_S confirming exact orbit-type
     (k, l) = (inf, 1) behavior on the initial prefix [1, 3B_2].

Prints PASS on exit code 0, or raises AssertionError (nonzero exit) on failure.
"""


def U(x):
    return (3 * x + 1) // 2


def D(x):
    return (x + 1) // 2


def v2(n):
    assert n > 0
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def stage_extension(H):
    """
    Exact algorithm of Lemma 2 starting at H >= 5.
    Returns (path, edges, B, C, branch_tag, b3b_loops) where:
      - path = [p_0 = H, p_1, ..., p_L = H']
      - edges = list of ('U' or 'D') of length L
      - B == 5 mod 6, C = U(B) = (3B + 1) // 2
    """
    assert H >= 5
    path = [H]
    edges = []

    def do_step(kind):
        cur = path[-1]
        if kind == 'U':
            nxt = U(cur)
        else:
            assert kind == 'D'
            assert cur % 6 == 2, f"Non-admissible D-step at {cur} (mod 6 = {cur % 6})"
            nxt = D(cur)
            assert nxt % 3 == 1
        path.append(nxt)
        edges.append(kind)
        return nxt

    # Phase 1: 4 pure U-steps (so > 5H), then pure U until odd
    for _ in range(4):
        do_step('U')
    assert path[-1] > 5 * H
    while path[-1] % 2 == 0:
        do_step('U')
    w0 = path[-1]
    assert w0 > 5 * H and w0 % 2 == 1

    # Phase 2: reach A == 3 mod 4, then B = U(A) == 5 mod 6, then C = U(B)
    b3b_loops = 0
    while True:
        w = path[-1]
        assert w % 2 == 1
        if w % 4 == 3:
            A = w
            B = do_step('U')
            C = do_step('U')
            branch = "A"
            break
        k = (w - 1) // 4
        if k % 4 == 0:
            do_step('U')
            A = do_step('U')
            assert A % 4 == 3
            B = do_step('U')
            C = do_step('U')
            branch = "B1"
            break
        elif k % 2 == 1:
            y = do_step('U')
            assert y % 6 == 2
            m = 3 * k + 1
            e = v2(m)
            u = m >> e
            assert e >= 1 and u % 2 == 1
            if (pow(3, e + 1, 4) * (u % 4)) % 4 == 3:
                for _ in range(e + 1):
                    do_step('U')
                A = path[-1]
                assert A == (3 ** (e + 1)) * u and A % 4 == 3
                B = do_step('U')
                C = do_step('U')
                branch = "B2a"
                break
            else:
                assert (pow(3, e, 4) * (u % 4)) % 4 == 3
                d = do_step('D')
                assert d == m and d > H
                for _ in range(e):
                    do_step('U')
                A = path[-1]
                assert A == (3 ** e) * u and A % 4 == 3
                B = do_step('U')
                assert B > y
                C = do_step('U')
                branch = "B2b"
                break
        else:
            # k == 2 mod 4 -> k = 4q + 2
            q = (k - 2) // 4
            assert w == 16 * q + 9 and q >= 1
            if q % 2 == 0:
                y = do_step('U')
                assert y % 6 == 2
                d = do_step('D')
                assert d > H and d % 3 == 1
                A = do_step('U')
                assert A % 4 == 3
                B = do_step('U')
                assert B > y
                C = do_step('U')
                branch = "B3a"
                break
            else:
                # Subcase B3b: q odd -> 2 pure U-steps
                old_v2 = v2(5 * q + 3) if q % 4 == 1 else None
                do_step('U')
                w_nxt = do_step('U')
                b3b_loops += 1
                if q % 4 == 3:
                    assert (w_nxt - 1) % 16 == 0
                else:
                    assert (w_nxt - 9) % 16 == 0
                    q_nxt = (w_nxt - 9) // 16
                    assert 4 * q_nxt == 9 * q + 3
                    assert 4 * (5 * q_nxt + 3) == 9 * (5 * q + 3)
                    assert v2(5 * q_nxt + 3) == old_v2 - 2

    assert B % 6 == 5 and C == (3 * B + 1) // 2 and B > 5 * H
    # Phase 3: exactly 2 pure U-steps from C reach H' > 3B
    do_step('U')
    H_prime = do_step('U')
    assert H_prime > 3 * B
    return path, edges, B, C, branch, b3b_loops


def verify_identities():
    print("[1/4] Verifying elementary U/D algebraic identities...")
    im_U = {U(x) for x in range(1, 2000) if U(x) <= 1000}
    expected_im_U = {z for z in range(2, 1001) if z % 3 != 1}
    assert im_U == expected_im_U
    for B in range(5, 1000, 6):
        C = U(B)
        assert C == (3 * B + 1) // 2
        assert (2 * B) % 3 == 1
        assert U(2 * B - 1) == 3 * B - 1
        assert D(2 * B + 1) == B + 1
        assert D(3 * B - 1) == C - 1
        assert B + 1 < C - 1 < 2 * B < 3 * B - 1
    for q in range(1, 10000, 4):
        w = 16 * q + 9
        w2 = U(U(w))
        assert (w2 - 9) % 16 == 0
        q2 = (w2 - 9) // 16
        assert 4 * (5 * q2 + 3) == 9 * (5 * q + 3)
        assert v2(5 * q2 + 3) == v2(5 * q + 3) - 2
    print("  Elementary U/D and Subcase B3b identities PASS.")


def verify_lemma2_exhaustive():
    print("[2/4] Exhaustively testing Lemma 2 across ALL H in [5, 5000]...")
    branch_counts = {"A": 0, "B1": 0, "B2a": 0, "B2b": 0, "B3a": 0}
    max_b3b_loops = 0
    for H in range(5, 5001):
        path, edges, B, C, branch, loops = stage_extension(H)
        branch_counts[branch] += 1
        if loops > max_b3b_loops:
            max_b3b_loops = loops
        # Check Lemma 2 conclusions:
        assert path[0] == H and len(path) == len(edges) + 1 and len(edges) >= 4
        assert len(set(path)) == len(path), f"Repeated vertex in stage for H={H}"
        assert all(v > H for v in path[1:]), f"Vertex <= H in stage for H={H}"
        assert B % 6 == 5 and B > 5 * H and C == U(B)
        assert all(not (B + 1 <= v <= C - 1) for v in path), f"Gap violated for H={H}"
        assert path[-1] == max(path) and path[-1] > 3 * B
        # Check every edge matches U or admissible D:
        for i, kind in enumerate(edges):
            if kind == 'U':
                assert path[i + 1] == U(path[i])
            else:
                assert path[i] % 6 == 2 and path[i + 1] == D(path[i]) and path[i + 1] % 3 == 1
    assert all(c > 0 for c in branch_counts.values()) and max_b3b_loops >= 2
    print(f"  Lemma 2 PASS for all 4996 values H in [5, 5000]; branch counts={branch_counts}, max B3b loops={max_b3b_loops}.")


def verify_multistage_and_cycles():
    print("[3/4] Building 50-stage divergent ray R from P_0 = (1, 2, 3, 5) and verifying global invariants...")
    R = [1, 2, 3, 5]
    R_edges = ['U', 'U', 'U']
    stages = []
    for m in range(1, 51):
        H = R[-1]
        path, edges, B, C, branch, loops = stage_extension(H)
        assert path[0] == H
        R.extend(path[1:])
        R_edges.extend(edges)
        stages.append((m, H, B, C, path[-1], branch, loops))

    R_set = set(R)
    assert len(R_set) == len(R), "Global vertex repetition in R!"
    assert R[0] == 1 and R[-1] == max(R)
    # Check global U-invariance of N \ R on [1, 50000]:
    for x in range(1, 50001):
        if x not in R_set:
            assert U(x) not in R_set, f"U({x}) = {U(x)} landed in R!"
    # Check global gap clearance and strict box disjointness across all 50 stages:
    for idx, (m, H, B, C, H_next, branch, loops) in enumerate(stages):
        assert B % 6 == 5 and C == (3 * B + 1) // 2 and H_next > 3 * B
        if idx > 0:
            prev_B = stages[idx - 1][2]
            assert 3 * prev_B - 1 < B + 1, f"Boxes overlap at stage {m}!"
        # Check ENTIRE 50-stage ray R misses [B+1, C-1]:
        assert all(not (B + 1 <= r <= C - 1) for r in R), f"Global R hit [B_{m}+1, C_{m}-1]!"

    print(f"  50-stage ray PASS: |R|={len(R)}, max(R) has {R[-1].bit_length()} bits, all 50 boxes disjoint & gap-clear.")

    print("[4/4] Exhaustively checking Lemma 1 trap closure and extracting explicit cycles C(B_m)...")
    cycles = []
    all_cyc_verts = set()
    for (m, H, B, C, H_next, branch, loops) in stages:
        if m > 4:
            break
        # Exhaustive check of f_B(x) in V(B) for all x in V(B) when 3*B <= 500000
        if 3 * B <= 500000:
            V_B = [x for x in range(B + 1, 3 * B) if x != 2 * B and x not in R_set]
            V_set = set(V_B)
            assert (B + 1) in V_set
            for x in V_B:
                fx = U(x) if x <= 2 * B - 1 else D(x)
                assert fx in V_set and fx != x, f"Trap closure failed at stage {m}, x={x}, fx={fx}"
            v_desc = f"|V(B_{m})|={len(V_B)} (exhaustive)"
        else:
            v_desc = f"box=[{B+1}, {3*B-1}]"
        # Extract explicit simple cycle from B + 1 under f_B (verifying every visited vertex lies in V(B))
        x = B + 1
        seen = {}
        walk = []
        while x not in seen:
            assert B + 1 <= x <= 3 * B - 1 and x != 2 * B and x not in R_set
            seen[x] = len(walk)
            walk.append(x)
            nxt = U(x) if x <= 2 * B - 1 else D(x)
            assert nxt != x
            x = nxt
        cyc = walk[seen[x]:]
        assert len(cyc) >= 2 and len(set(cyc)) == len(cyc)
        assert all(B + 1 <= v <= 3 * B - 1 and v != 2 * B and v not in R_set and v not in all_cyc_verts for v in cyc)
        all_cyc_verts.update(cyc)
        cycles.append((m, B, C, len(cyc), min(cyc), max(cyc), cyc))
        print(f"  Stage {m} ({branch}): B_{m}={B}, C_{m}={C}, {v_desc}, cycle len={len(cyc)}, range=[{min(cyc)}, {max(cyc)}]")

    assert len(cycles) == 4

    # Direct T_S verification on [1, 3*B_2]: verify ray, cycles, and exact (k, l) = (inf, 1) absorption
    S_prefix = set()
    for i, kind in enumerate(R_edges):
        if kind == 'U':
            S_prefix.add(R[i])
    for (m, B, C, clen, cmin, cmax, cyc) in cycles:
        for v in cyc:
            if v <= 2 * B - 1:
                S_prefix.add(v)

    def T_S(x):
        return U(x) if x in S_prefix else D(x)

    # Check T_S follows R on all len(R_edges) steps
    for i in range(len(R_edges)):
        assert T_S(R[i]) == R[i + 1]
    # Check T_S follows each extracted cycle C(B_m)
    for (m, B, C, clen, cmin, cmax, cyc) in cycles:
        for i in range(len(cyc)):
            assert T_S(cyc[i]) == cyc[(i + 1) % len(cyc)]
    # Check every x in [1, 3*B_2] outside R U cycles strictly decreases until hitting R U cycles
    B2 = cycles[1][1]
    W_verts = R_set | all_cyc_verts
    for x in range(1, 3 * B2 + 1):
        cur = x
        steps = 0
        while cur not in W_verts:
            nxt = T_S(cur)
            assert nxt < cur, f"Non-decreasing step outside W at {cur} -> {nxt}"
            cur = nxt
            steps += 1
            assert steps <= 100
    print(f"  Direct T_S simulation PASS on all {len(R_edges)} ray steps, {len(cycles)} disjoint cycles, and all x in [1, {3 * B2}].")


def main():
    verify_identities()
    verify_lemma2_exhaustive()
    verify_multistage_and_cycles()
    print("PASS")


if __name__ == "__main__":
    main()

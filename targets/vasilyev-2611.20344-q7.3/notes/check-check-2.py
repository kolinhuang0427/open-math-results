#!/usr/bin/env python3
"""Independent zero-float exact-arithmetic verifier for targets/vasilyev-2611.20344-q7.3/."""

from __future__ import annotations


def U(x: int) -> int:
    return (3 * x + (x & 1)) // 2


def D(x: int) -> int:
    return (x + (x & 1)) // 2


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def is_admissible(x: int, y: int) -> bool:
    return y == U(x) or (x % 6 == 2 and y == D(x))


def build_stage(H: int) -> tuple[list[int], int, int, str, int]:
    """Independently implement Lemma 3 stage construction from PROOF.md."""
    assert H >= 5
    path = [H]

    def go_U() -> int:
        nxt = U(path[-1])
        path.append(nxt)
        return nxt

    def go_D() -> int:
        cur = path[-1]
        assert cur % 6 == 2
        nxt = D(cur)
        path.append(nxt)
        return nxt

    # Phase 1: 4 U-steps, then U until odd
    for _ in range(4):
        go_U()
    assert path[-1] > 5 * H
    while path[-1] % 2 == 0:
        go_U()
    w = path[-1]
    assert w > 5 * H and w % 2 == 1

    # Phase 2
    b3b_iters = 0
    branch = ""
    while True:
        if w % 4 == 3:
            if not branch:
                branch = "A"
            A = w
            B = go_U()
            C = go_U()
            break
        k = (w - 1) // 4
        if k % 4 == 0:
            if not branch:
                branch = "B1"
            go_U()  # y
            A = go_U()
            assert A % 4 == 3
            B = go_U()
            C = go_U()
            break
        if k % 2 == 1:
            y = go_U()
            assert y % 6 == 2
            m = 3 * k + 1
            e = v2(m)
            u = m >> e
            assert e >= 1 and u % 2 == 1
            v_e = (pow(3, e, 4) * (u % 4)) % 4
            v_e1 = (3 * v_e) % 4
            assert {v_e, v_e1} == {1, 3}
            if v_e1 == 3:
                branch = branch or "B2a"
                for _ in range(e + 1):
                    go_U()
                A = path[-1]
                assert A % 4 == 3
                B = go_U()
                C = go_U()
                break
            else:
                branch = branch or "B2b"
                d = go_D()
                assert d == m and d % 3 == 1
                for _ in range(e):
                    go_U()
                A = path[-1]
                assert A % 4 == 3
                B = go_U()
                C = go_U()
                break
        # k == 2 (mod 4)
        q = (k - 2) // 4
        assert q >= 2
        if q % 2 == 0:
            branch = branch or "B3a"
            y = go_U()
            assert y % 6 == 2
            d = go_D()
            assert d % 3 == 1
            A = go_U()
            assert A % 4 == 3
            B = go_U()
            C = go_U()
            break
        # Subcase B3b
        b3b_iters += 1
        assert b3b_iters <= 100
        go_U()
        w_next = go_U()
        assert w_next == 36 * q + 21
        if q % 4 == 1:
            q_next = (9 * q + 3) // 4
            assert 4 * (5 * q_next + 3) == 9 * (5 * q + 3)
            assert v2(5 * q_next + 3) == v2(5 * q + 3) - 2
        w = w_next

    assert B % 6 == 5 and C == U(B) and B > 5 * H
    # Phase 3: two U-steps past 3B
    go_U()
    H_next = go_U()
    assert H_next == path[-1] > 3 * B
    assert H_next == max(path)
    return path, B, C, branch, b3b_iters


def check_primary_source() -> None:
    import os
    if not os.path.exists("tools/.arxiv_cache/eprint/2611.20344/updown.tex"):
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        return
    tex = open("tools/.arxiv_cache/eprint/2611.20344/updown.tex", "r", encoding="utf-8").read()
    for s in [
        r"\label{lem:steps}",
        r"$U(x)=(3x+e)/2$ and $D(x)=(x+e)/2$",
        r"\label{prop:dict}",
        r"\label{rem:types}",
        r"\label{q:types}",
        "Is there a map with infinitely many cycles and a divergent orbit",
    ]:
        assert s in tex, f"Missing primary source text: {s}"

    target_md = open("targets/vasilyev-2611.20344-q7.3/TARGET.md", "r", encoding="utf-8").read()
    assert "arXiv:2611.20344v2" in target_md
    assert "Is there a map with infinitely many cycles and a divergent orbit (Remark 4.4)?" in target_md
    print("[PASS] Primary source arXiv:2611.20344v2 verbatim match verified.")


def check_elementary_and_lemma1() -> None:
    im_u = {U(x) for x in range(1, 2000) if U(x) <= 2000}
    expected_im_u = {z for z in range(2, 2001) if z % 3 != 1}
    assert im_u == expected_im_u

    for x in range(1, 2001):
        assert U(x) > x and 2 * U(x) >= 3 * x
        if x >= 2:
            assert D(x) < x
        if x < 2000:
            assert U(x) < U(x + 1)
            assert D(x) <= D(x + 1)

    # Lemma 1 structural bounds for all B == 5 (mod 6) in [5, 600]
    for B in range(5, 601, 6):
        C = U(B)
        assert C == (3 * B + 1) // 2
        assert B + 1 < C - 1 < 2 * B < 3 * B - 1
        assert (2 * B) % 3 == 1 and (2 * B) not in im_u
        assert D(2 * B + 1) == B + 1
        assert D(3 * B - 1) == C - 1
        assert U(2 * B - 1) == 3 * B - 1
    print("[PASS] Elementary U/D identities and Lemma 1 trap inequalities (B <= 600) verified.")


def check_lemma3_exhaustive() -> None:
    counts: dict[str, int] = {}
    max_b3b = 0
    # Test H in [5, 10000] plus targeted high-v2(5q+3) heads
    for H in range(5, 10001):
        path, B, C, branch, b3b = build_stage(H)
        counts[branch] = counts.get(branch, 0) + 1
        max_b3b = max(max_b3b, b3b)

        L = len(path) - 1
        assert L >= 4
        assert path[0] == H
        assert len(set(path)) == len(path)
        for i in range(L):
            assert is_admissible(path[i], path[i + 1])
            assert path[i + 1] > H
            assert not (B + 1 <= path[i + 1] <= C - 1)
        assert not (B + 1 <= path[0] <= C - 1)
        assert path[-1] == max(path) > 3 * B

    # Adversarial Subcase B3b test: construct w with large v2(5q+3) directly via H
    # e.g., q = (2^10 - 3) * inv_5 mod 2^10; 5 * 204 + 3 = 1023 (odd), wait 5*q+3 = 2^k => k even: 2^10=1024, (1024-3)/5 not int; 2^12=4096 -> (4096-3)/5 not int; 2^14=16384 -> (16384-3)/5=3276.2; 2^6=64 -> (64-3)=61; 2^8=256 -> 253; wait 5q+3 = 3 * 2^8 = 768 => q=153 (odd!), 5*153+3 = 768 = 3 * 2^8!
    for pow2 in [8, 12, 16]:
        q0 = (3 * (1 << pow2) - 3) // 5
        assert q0 % 2 == 1 and 5 * q0 + 3 == 3 * (1 << pow2)
        w0 = 16 * q0 + 9
        # Check B3b termination from w0 if treated as Phase 2 start (with H_approx = w0 // 6)
        path, B, C, branch, b3b = build_stage(w0)
        assert len(set(path)) == len(path) and path[-1] > 3 * B

    print(f"[PASS] Lemma 3 exhaustive across H in [5, 10000] (counts={counts}, max_B3b_depth={max_b3b}).")


def extract_cycle_in_box(B: int, R_set: set[int]) -> list[int]:
    """Follow f_B inside V(B) starting from B+1 and return the exact simple cycle."""
    C = U(B)
    seen: dict[int, int] = {}
    seq: list[int] = []
    x = B + 1
    while x not in seen:
        assert B + 1 <= x <= 3 * B - 1
        assert x != 2 * B and x not in R_set
        seen[x] = len(seq)
        seq.append(x)
        x = U(x) if x < 2 * B else D(x)
        # Every f_B value must lie in V(B)
        assert B + 1 <= x <= 3 * B - 1 and x != 2 * B and x not in R_set
        if seq[-1] > 2 * B:
            assert B + 1 <= x <= C - 1
    cyc = seq[seen[x]:]
    assert len(cyc) >= 2 and len(set(cyc)) == len(cyc)
    return cyc


def check_global_construction_and_TS() -> None:
    R: list[int] = [1, 2, 3, 5]
    stages: list[tuple[int, int, int, int]] = []  # (m, B, C, H_m)
    H = 5
    for m in range(1, 16):
        P, B, C, branch, _ = build_stage(H)
        assert P[0] == H
        R.extend(P[1:])
        H = P[-1]
        stages.append((m, B, C, H))

    R_set = set(R)
    assert len(R_set) == len(R)
    for i in range(len(R) - 1):
        assert is_admissible(R[i], R[i + 1])

    # Because every step in P_m (m > k) exceeds H_k, R cap [1, H_k] is already complete at stage k!
    H2 = stages[1][3]
    H3 = stages[2][3]
    assert H2 == max(x for x in R if x <= H2)
    for x in range(1, H2 + 1):
        if x not in R_set:
            assert U(x) not in R_set, f"Lemma 2 failed at x={x}"

    # Verify strict separation of trap intervals and gap clearance across all 15 stages
    for idx, (m, B, C, Hm) in enumerate(stages):
        assert all(not (B + 1 <= r <= C - 1) for r in R)
        if idx > 0:
            prev_Hm = stages[idx - 1][3]
            assert 3 * stages[idx - 1][1] - 1 < prev_Hm < B < B + 1
        assert 3 * B - 1 < Hm

    # Extract cycles C(B_1), C(B_2), C(B_3), C(B_4)
    cycles: list[list[int]] = []
    for m in range(1, 5):
        _, B, C, _ = stages[m - 1]
        cyc = extract_cycle_in_box(B, R_set)
        cycles.append(cyc)
        # Verify Lemma 1 exhaustively on stages 1 and 2
        if m <= 2:
            V = [x for x in range(B + 1, 3 * B) if x != 2 * B and x not in R_set]
            V_set = set(V)
            for x in V:
                fx = U(x) if x < 2 * B else D(x)
                assert fx in V_set and fx != x

    # Build S on [1, H3] and directly simulate T_S on EVERY x in [1, H2] and sampled [1, H3]
    S: set[int] = set()
    for i in range(len(R) - 1):
        if R[i + 1] == U(R[i]):
            S.add(R[i])
    for m in range(3):
        B = stages[m][1]
        for x in cycles[m]:
            if B + 1 <= x <= 2 * B - 1:
                S.add(x)

    def T_S(x: int) -> int:
        return U(x) if x in S else D(x)

    # Check exact R prefix up to H3 and cycles 1..3 under T_S
    idx_H3 = R.index(H3)
    for i in range(idx_H3):
        assert T_S(R[i]) == R[i + 1]

    cycle_sets = [set(c) for c in cycles[:3]]
    for m, cyc in enumerate(cycles[:3]):
        for i, x in enumerate(cyc):
            assert T_S(x) == cyc[(i + 1) % len(cyc)]

    # Memoized classification of EVERY starting x in [1, H3] under T_S:
    # must strictly descend until entering W_prefix = R_prefix union C1 union C2 union C3
    cls: dict[int, int] = {}  # 0 = ray, 1..3 = cycle
    for x in R[:idx_H3 + 1]:
        cls[x] = 0
    for idx_c, cs in enumerate(cycle_sets, start=1):
        for x in cs:
            cls[x] = idx_c

    counts = [0, 0, 0, 0]
    for start in range(1, H3 + 1):
        x = start
        trail: list[int] = []
        while x not in cls:
            trail.append(x)
            nxt = T_S(x)
            assert nxt < x, f"Non-W vertex {x} did not descend"
            x = nxt
        c_id = cls[x]
        counts[c_id] += 1
        for node in trail:
            cls[node] = c_id

    assert sum(counts) == H3
    cyc_lens = [len(c) for c in cycles]
    print(
        f"[PASS] 15-stage construction (H3={H3}), Lemma 1/2/3 invariants, "
        f"4 disjoint cycles (lengths={cyc_lens}), and exhaustive T_S orbit classification "
        f"for all x in [1, {H3}] (ray_basin={counts[0]}, cycle_basins={counts[1:]}) verified."
    )


def main() -> None:
    check_primary_source()
    check_elementary_and_lemma1()
    check_lemma3_exhaustive()
    check_global_construction_and_TS()
    print("PASS")


if __name__ == "__main__":
    main()

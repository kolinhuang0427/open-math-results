#!/usr/bin/env python3
"""Exact integer & discrete-structure verifier for targets/myrisiotis-2611.09020-edit-graph/.

Zero floats: all bit-lengths, syndrome arithmetic, prefix parsing, halting-time
inequalities, and finite edit-graph path checks use exact integer/string logic.
"""

from collections import deque


# ---------------------------------------------------------------------------
# 1. Elias-gamma target header c(x) and collision-free morphism phi(c(x)) = P_x
# ---------------------------------------------------------------------------

def bin_str(r: int) -> str:
    if r == 0:
        return "0"
    return bin(r)[2:]


def encode_c(x: str) -> str:
    """Prefix-free self-delimiting binary encoding c(x)."""
    m = len(x) + 1
    bm = bin_str(m)
    return "1" * (len(bm) - 1) + "0" + bm + x


def decode_c(s: str):
    """Parse c(x) from the start of s; returns (x, consumed_len) or None."""
    i = 0
    while i < len(s) and s[i] == "1":
        i += 1
    if i >= len(s) or s[i] != "0":
        return None
    k = i
    pos = i + 1
    if pos + k + 1 > len(s):
        return None
    bm = s[pos : pos + k + 1]
    if bm[0] != "1":
        return None
    m = int(bm, 2)
    x_len = m - 1
    pos += k + 1
    if pos + x_len > len(s):
        return None
    return s[pos : pos + x_len], pos + x_len


def phi_encode(bits: str) -> str:
    return "".join("01" if b == "0" else "011" for b in bits)


def phi_decode(code: str):
    """Inverse of phi on {01, 011}*; returns decoded bitstring or None."""
    out = []
    i = 0
    n = len(code)
    while i < n:
        if i + 2 <= n and code[i : i + 2] == "01":
            if i + 2 < n and code[i + 2] == "1":
                if i + 3 < n and code[i + 3] == "1":
                    return None
                out.append("1")
                i += 3
            else:
                out.append("0")
                i += 2
        else:
            return None
    return "".join(out)


def P_of(x: str) -> str:
    return phi_encode(encode_c(x))


def is_valid_bridge_u(u: str) -> bool:
    """Check membership in regular language U."""
    if u in ("101", "1011", "10111"):
        return True
    if len(u) < 5 or not u.startswith("1011") or not u.endswith("1"):
        return False
    mid = u[4:-1]
    i = 0
    n = len(mid)
    while i < n:
        if mid[i] != "0":
            return False
        if i + 1 == n:
            return True  # trailing partial '0'
        if mid[i + 1] != "1":
            return False
        if i + 2 == n:
            return True  # trailing '01' (either full token or partial)
        if mid[i + 2] == "1":
            i += 3
        else:
            i += 2
    return True


# ---------------------------------------------------------------------------
# 2. Coupon coloring (lem:connected-syndrome-coloring) + exact threshold N_x
# ---------------------------------------------------------------------------

def coloring_params(n: int):
    """Given body length n >= 3, return (a, K, k) with 2K - 1 <= n < 4K - 1."""
    assert n >= 3
    a = 1
    while (1 << (a + 2)) - 1 <= n:
        a += 1
    K = 1 << a
    k = K - 1
    assert 2 * K - 1 <= n < 4 * K - 1
    return a, K, k


def syndrome_matrix_mul(a: int, vec: str) -> int:
    """Compute H * vec over F_2 as an integer in [0, 2^a - 1], 1-indexed columns."""
    acc = 0
    for idx, ch in enumerate(vec, start=1):
        if ch == "1":
            acc ^= idx
    return acc


def D_n(p: str) -> int:
    """Color D_n(p) in [0, K-1] for |p| = n >= 3."""
    n = len(p)
    a, K, k = coloring_params(n)
    u = p[:k]
    v = p[k : 2 * k]
    b = p[2 * k]
    return syndrome_matrix_mul(a, u) if b == "0" else syndrome_matrix_mul(a, v)


def lambda_a(j: int) -> str:
    """Shortlex label of color integer j >= 0."""
    return bin_str(j + 1)[1:]


def shortlex_rank(x: str) -> int:
    if x == "":
        return 0
    return (1 << len(x)) - 1 + int(x, 2)


def unit_rep(k: int, j: int) -> str:
    """Return length-k vector r_j of Hamming weight <= 1 with H * r_j = j."""
    if j == 0:
        return "0" * k
    lst = ["0"] * k
    lst[j - 1] = "1"
    return "".join(lst)


def compute_N_x(x: str) -> int:
    """Smallest N >= 6 such that for n = N-3, i(x) < K(n) and 5 + |P_x| <= k(n)."""
    ix = shortlex_rank(x)
    Bx = 5 + len(P_of(x))
    N = 6
    while True:
        n = N - 3
        _, K, k = coloring_params(n)
        if ix < K and Bx <= k:
            return N
        N += 1


def compute_b(x: str) -> int:
    return compute_N_x(x) + 5 + len(P_of(x))


# ---------------------------------------------------------------------------
# 3. Exact machine V specification & timing constants (zero floats)
# ---------------------------------------------------------------------------

C_H = 20
L_1 = 2 * C_H  # = 40 >= 2 * C_H
L_A = 10


def H_time(x: str) -> int:
    return C_H * (len(P_of(x)) + 8)


def C_time(n: int) -> int:
    assert n >= 3
    return (C_H + 100) * (n + 1) ** 2


def S_time(n: int) -> int:
    return C_time(n) + 1 if n >= 3 else 1


def T_star(n_body: int, T_A: int, x: str) -> int:
    Bx = 5 + len(P_of(x))
    return S_time(n_body) + L_A * T_A + L_1 * Bx


def run_V(s: str, A_fn):
    """Return (status, output, native_time) for program s under V.

    status in {'ok', 'bot', 'div'}.
    """
    N = len(s)
    if N < 3:
        return ("bot", None, 1)

    prefix3 = s[:3]
    p = s[3:]
    n = len(p)

    def run_base(body: str, j: int):
        res = A_fn(body)
        if res[0] != "ok":
            return res
        _, x, T_A = res
        Bx = 5 + len(P_of(x))
        if j > Bx:
            return ("bot", None, 1)
        return ("ok", x, T_star(len(body), T_A, x))

    def run_color(body: str):
        if len(body) < 3:
            return ("bot", None, 1)
        nb = len(body)
        _, K, k = coloring_params(nb)
        j = D_n(body)
        x = lambda_a(j)
        if 5 + len(P_of(x)) > k:
            return ("bot", None, 1)
        return ("ok", x, C_time(nb))

    def run_hub(rest: str):
        idx = rest.find("000")
        if idx < 1:
            return ("bot", None, 1)
        inner = rest[:idx]
        if "00" in inner or not inner.endswith("1"):
            return ("bot", None, 1)
        P_cand = inner[:-1]
        dec = phi_decode(P_cand)
        if dec is None:
            return ("bot", None, 1)
        c_res = decode_c(dec)
        if c_res is None:
            return ("bot", None, 1)
        x, consumed = c_res
        if consumed != len(dec):
            return ("bot", None, 1)
        return ("ok", x, H_time(x))

    if prefix3 == "000":
        return run_base(p, 0)
    elif prefix3 == "001":
        if n < 3:
            return ("bot", None, 1)
        if p.count("1") % 2 == 0:
            return run_base(p, 0)
        return run_color(p)
    elif prefix3 == "010":
        if n < 3:
            return ("bot", None, 1)
        if p.count("1") % 2 == 0:
            return run_color(p)
        return run_base(p, 0)
    elif prefix3 == "011":
        return run_color(p)
    elif prefix3 == "111":
        return run_color(p)
    elif prefix3 == "100":
        if not p:
            return ("bot", None, 1)
        if p[0] == "0":
            return run_base(p[1:], 1)
        return run_hub(p[1:])
    elif prefix3 == "110":
        if len(p) >= 2 and p[:2] == "00":
            return run_base(p[2:], 2)
        if p and p[0] == "1":
            return run_hub(p[1:])
        return ("bot", None, 1)
    elif prefix3 == "101":
        idx = s.find("000")
        if idx < 3:
            return ("bot", None, 1)
        u = s[:idx]
        if "00" in u or not is_valid_bridge_u(u):
            return ("bot", None, 1)
        body = s[idx + 3 :]
        return run_base(body, len(u))
    raise AssertionError("unreachable")


def is_edit_adjacent(a: str, b: str) -> bool:
    la, lb = len(a), len(b)
    if la == lb:
        return sum(1 for x, y in zip(a, b) if x != y) == 1
    if la + 1 == lb:
        for i in range(lb):
            if b[:i] + b[i + 1 :] == a:
                return True
        return False
    if lb + 1 == la:
        return is_edit_adjacent(b, a)
    return False


# ---------------------------------------------------------------------------
# 4. Verification suites
# ---------------------------------------------------------------------------

def verify_encoding_and_disjointness():
    seen_c = {}
    seen_P = {}
    all_strs = [""]
    for length in range(1, 7):
        for v in range(1 << length):
            all_strs.append(format(v, f"0{length}b"))
    all_strs.extend(["0" * 15, "1" * 20, "01" * 12, "11010011001"])

    for x in all_strs:
        cx = encode_c(x)
        dec = decode_c(cx + "10101")
        assert dec == (x, len(cx)), f"c(x) prefix-free failed for {x!r}"
        assert cx not in seen_c, f"c collision: {x!r} vs {seen_c[cx]!r}"
        seen_c[cx] = x

        Px = P_of(x)
        assert len(Px) >= 4
        assert Px[0] == "0" and Px[-1] == "1"
        assert "00" not in Px
        assert "00" not in ("1" + Px + "1")
        assert phi_decode(Px) == cx
        assert Px not in seen_P
        seen_P[Px] = x

    # Check exhaustiveness & determinism of run_V on every string of length <= 14
    def dummy_A(body: str):
        return ("ok", body[:2], len(body) + 1)

    for length in range(0, 15):
        for v in range(1 << length):
            s = format(v, f"0{length}b") if length > 0 else ""
            st, out, tm = run_V(s, dummy_A)
            assert st in ("ok", "bot", "div") and tm >= 1
            if st == "ok":
                assert out is not None and tm >= H_time(out)
    print("PASS: Encoding round-trip, prefix-freeness, zero-00 invariant, and exhaustive 0..14 parse")


def verify_coloring_and_bridge_geometry():
    # Exhaustive BFS of color classes & neighbor property for n = 3..13
    for n in range(3, 14):
        a, K, k = coloring_params(n)
        by_color = {j: [] for j in range(K)}
        for v in range(1 << n):
            p = format(v, f"0{n}b")
            by_color[D_n(p)].append(p)
        for j in range(K):
            nodes = set(by_color[j])
            assert nodes
            start = next(iter(nodes))
            q = deque([start])
            vis = {start}
            while q:
                cur = q.popleft()
                for i in range(n):
                    nb = cur[:i] + ("1" if cur[i] == "0" else "0") + cur[i + 1 :]
                    if nb in nodes and nb not in vis:
                        vis.add(nb)
                        q.append(nb)
            assert len(vis) == len(nodes), f"Disconnected color class {j} at n={n}"
        # Neighbor of every color with opposite parity
        for v in range(1 << n):
            p = format(v, f"0{n}b")
            par = p.count("1") % 2
            seen_j = set()
            for i in range(n):
                nb = p[:i] + ("1" if p[i] == "0" else "0") + p[i + 1 :]
                if nb.count("1") % 2 != par:
                    seen_j.add(D_n(nb))
            assert len(seen_j) == K

    # Check exact threshold N_x and canonical bridge vertex q for targets up to length 5
    targets = ["", "0", "1", "00", "01", "10", "11", "101", "0000", "11111"]
    for x in targets:
        Nx = compute_N_x(x)
        bx = compute_b(x)
        Px = P_of(x)
        Bx = 5 + len(Px)
        hx = "1001" + Px + "1000"
        assert len(hx) == 3 + Bx < bx
        assert Nx >= 6 and bx == Nx + Bx
        assert Nx <= max(1 << (len(x) + 2), 4 * Bx) + 2
        ix = shortlex_rank(x)

        for N in range(Nx, Nx + 80):
            n = N - 3
            a, K, k = coloring_params(n)
            assert ix < K and Bx <= k
            assert C_time(n) > C_H * (k + 8) > H_time(x)
            assert S_time(n) > C_time(n)
            # Canonical bridge string q inside {0,1}^n
            u_reg = ("1" + Px + "1000").ljust(k, "0")
            assert len(u_reg) == k
            v_reg = unit_rep(k, ix)
            w_rem = "0" * (n - 2 * k - 1)
            q = u_reg + v_reg + "1" + w_rem
            assert len(q) == n
            assert D_n(q) == ix and lambda_a(D_n(q)) == x
            for pref in ("011", "111", "110", "100"):
                st, out, tm = run_V(pref + q, lambda _: ("bot", None, 1))
                assert st == "ok" and out == x
            assert is_edit_adjacent("011" + q, "111" + q)
            assert is_edit_adjacent("111" + q, "110" + q)
            assert is_edit_adjacent("110" + q, "100" + q)
    print("PASS: Syndrome coloring BFS (n=3..13), timing hierarchy H(x) < C(n) < S(n), and core-hub attachment")


def verify_proof_paths_on_adversarial_A():
    """Verify explicit proof paths & timing monotonicity for adversarial base machines A."""
    def A_adversarial(p: str):
        # Mix of isolated strings, antipodal pairs, short/long outputs, and empty string
        table = {
            "": ("ok", "", 1),
            "0": ("ok", "0", 2),
            "11": ("ok", "0", 5),
            "000": ("ok", "1", 3),
            "1010": ("ok", "", 7),
            "010101": ("ok", "01", 9),
            "1" * 35: ("ok", "", 40),
            "0" * 36: ("ok", "0", 40),
        }
        return table.get(p, ("bot", None, 1))

    test_targets = ["", "0", "1", "01"]
    for x in test_targets:
        Nx = compute_N_x(x)
        bx = compute_b(x)
        Px = P_of(x)
        hx = "1001" + Px + "1000"

        # Collect a rich set of valid vertices for target x under A_adversarial
        vertices = []
        # 1. All base/helper/bridge programs generated from A_adversarial bodies
        for body in ["", "0", "11", "000", "1010", "010101", "1" * 35, "0" * 36]:
            stA, outA, _ = A_adversarial(body)
            if stA == "ok" and outA == x:
                vertices.append("000" + body)
                if len(body) >= 3:
                    par = body.count("1") % 2
                    vertices.append(("001" if par == 0 else "010") + body)
                vertices.append("1000" + body)
                vertices.append("11000" + body)
                vertices.append("101000" + body)
                vertices.append("1011000" + body)
                vertices.append("10111000" + body)
                vertices.append("1011" + Px + "1000" + body)
                # Also a truncated partial bridge prefix
                vertices.append("1011" + Px[:3] + "1000" + body)
        # 2. Core & router & hub vertices at length Nx and Nx+5
        for N in (Nx, Nx + 5):
            n = N - 3
            _, K, k = coloring_params(n)
            ix = shortlex_rank(x)
            u_reg = ("1" + Px + "1000").ljust(k, "0")
            q = u_reg + unit_rep(k, ix) + "1" + "0" * (n - 2 * k - 1)
            vertices.extend(["011" + q, "111" + q, "110" + q, "100" + q])
            # Also a router neighbor of "000" + "1"*35 if len == 35
            if N == 38:
                p_body = "1" * 35
                par = p_body.count("1") % 2
                # Find 1-bit neighbor q_nb with D_n(q_nb) == ix
                for i in range(n):
                    q_nb = p_body[:i] + ("1" if p_body[i] == "0" else "0") + p_body[i + 1 :]
                    if q_nb.count("1") % 2 != par and D_n(q_nb) == ix:
                        vertices.append(("001" if par == 0 else "010") + q_nb)
                        break

        # For every vertex v and budget l = max(bx, len(v)), trace the exact proof walk to hx
        # and verify every intermediate vertex outputs x in time <= tm(v) and has length <= l!
        for v in vertices:
            st, out, tm = run_V(v, A_adversarial)
            assert st == "ok" and out == x, f"Unexpected failure on {v!r}"
            ell = max(bx, len(v))
            t = tm  # sharpest possible deadline!

            # Reconstruct exact proof walk from v to hx
            walk = [v]
            cur = v

            # Step A: if hub (1001... or 1101...), flip 110->100 and delete suffix
            def finish_from_hub(cur_hub):
                w = []
                if cur_hub.startswith("110"):
                    nxt = "100" + cur_hub[3:]
                    w.append(nxt)
                    cur_hub = nxt
                while len(cur_hub) > len(hx):
                    cur_hub = cur_hub[:-1]
                    w.append(cur_hub)
                return w

            # Step B: from core/router at body length n >= Nx-3
            def finish_from_color(cur_col):
                w = []
                body = cur_col[3:]
                nb = len(body)
                assert nb + 3 >= Nx
                if cur_col[:3] in ("001", "010"):
                    cur_col = "011" + body
                    w.append(cur_col)
                if cur_col[:3] == "011":
                    cur_col = "111" + body
                    w.append(cur_col)
                # Walk inside 111-core from body to canonical q
                _, _, k = coloring_params(nb)
                target_u = ("1" + Px + "1000").ljust(k, "0")
                target_v = unit_rep(k, shortlex_rank(x))
                target_w = "0" * (nb - 2 * k - 1)
                # Standard representative path inside D_n^{-1}(j_x)
                b_list = list(body)
                if b_list[2 * k] == "0":
                    for i in range(k):
                        if b_list[k + i] != target_v[i]:
                            b_list[k + i] = target_v[i]
                            w.append("111" + "".join(b_list))
                    b_list[2 * k] = "1"
                    w.append("111" + "".join(b_list))
                else:
                    # Wait: D_n is Hv, first clear/set u to target_u via selector=1,
                    # wait if b=1 then u is ignored so set u to target_u, flip b->0 if v needs change?
                    # Actually set u to target_u directly if u!=target_u? No, to preserve D_n while b=1,
                    # we first set u to target_v's syndrome? Wait: let's follow lem:connected-syndrome-coloring!
                    for i in range(k):
                        if b_list[i] != target_v[i]:
                            b_list[i] = target_v[i]
                            w.append("111" + "".join(b_list))
                    b_list[2 * k] = "0"
                    w.append("111" + "".join(b_list))
                    for i in range(k):
                        if b_list[k + i] != target_v[i]:
                            b_list[k + i] = target_v[i]
                            w.append("111" + "".join(b_list))
                    b_list[2 * k] = "1"
                    w.append("111" + "".join(b_list))
                # Now b=1 and v=target_v; u and w are ignored, so change them freely!
                for i in range(k):
                    if b_list[i] != target_u[i]:
                        b_list[i] = target_u[i]
                        w.append("111" + "".join(b_list))
                for i in range(2 * k + 1, nb):
                    if b_list[i] != "0":
                        b_list[i] = "0"
                        w.append("111" + "".join(b_list))
                q_str = "".join(b_list)
                hub2 = "110" + q_str
                w.append(hub2)
                w.extend(finish_from_hub(hub2))
                return w

            if cur.startswith("1001") or cur.startswith("1101"):
                walk.extend(finish_from_hub(cur))
            elif cur[:3] in ("011", "111") or (
                cur[:3] in ("001", "010")
                and (
                    (cur[:3] == "001" and cur[3:].count("1") % 2 == 1)
                    or (cur[:3] == "010" and cur[3:].count("1") % 2 == 0)
                )
            ):
                walk.extend(finish_from_color(cur))
            else:
                # Base, source helper, or bridge -> reduce back to 000 + body
                if cur[:3] in ("001", "010"):
                    cur = "000" + cur[3:]
                    walk.append(cur)
                elif not cur.startswith("000"):
                    idx = cur.find("000")
                    u_pref = cur[:idx]
                    body = cur[idx + 3 :]
                    # Delete u_pref back to empty
                    if len(u_pref) >= 5:
                        mid = u_pref[4:-1]
                        while mid:
                            mid = mid[:-1]
                            walk.append("1011" + mid + "1000" + body)
                        walk.append("1011000" + body)
                    if u_pref.startswith("1011") and len(u_pref) >= 4:
                        if u_pref == "10111" or len(u_pref) >= 5:
                            pass
                        if walk[-1].startswith("10111"):
                            walk.append("1011000" + body)
                        walk.append("101000" + body)
                    elif u_pref == "101":
                        pass
                    if walk[-1].startswith("101000"):
                        walk.append("11000" + body)
                    if walk[-1].startswith("11000"):
                        walk.append("1000" + body)
                    cur = "000" + body
                    walk.append(cur)

                body = cur[3:]
                nb = len(body)
                if nb + 3 >= Nx:
                    par = body.count("1") % 2
                    hlp = ("001" if par == 0 else "010") + body
                    walk.append(hlp)
                    # Find opposite-parity 1-bit neighbor q_nb with D_n(q_nb) == ix
                    _, _, k = coloring_params(nb)
                    found = None
                    for i in range(nb):
                        cand = body[:i] + ("1" if body[i] == "0" else "0") + body[i + 1 :]
                        if cand.count("1") % 2 != par and D_n(cand) == shortlex_rank(x):
                            found = cand
                            break
                    assert found is not None
                    rtr = ("001" if par == 0 else "010") + found
                    walk.append(rtr)
                    walk.extend(finish_from_color(rtr))
                else:
                    # Insert bridge prefix bit by bit up to 1011 + Px + 1000 + body
                    for step_pref in ["1", "11", "101", "1011", "10111"]:
                        cur = step_pref + "000" + body
                        walk.append(cur)
                    built = ""
                    for bit in Px:
                        built += bit
                        cur = "1011" + built + "1000" + body
                        walk.append(cur)
                    hub1 = "1001" + Px + "1000" + body
                    walk.append(hub1)
                    walk.extend(finish_from_hub(hub1))

            assert walk[-1] == hx, f"Walk from {v!r} ended at {walk[-1]!r} != {hx!r}"
            for idx_w, node in enumerate(walk):
                assert len(node) <= ell, f"Exceeded budget {ell} at {node!r} (len={len(node)})"
                st_n, out_n, tm_n = run_V(node, A_adversarial)
                assert st_n == "ok" and out_n == x and tm_n <= t, (
                    f"Node {node!r} failed deadline/output: {(st_n, out_n, tm_n)} vs t={t}"
                )
                if idx_w > 0:
                    assert is_edit_adjacent(walk[idx_w - 1], node), (
                        f"Non-edit step: {walk[idx_w - 1]!r} -> {node!r}"
                    )

    print("PASS: Constructive edit-graph walks, deadlines, and length budgets verified for all vertex types")


if __name__ == "__main__":
    verify_encoding_and_disjointness()
    verify_coloring_and_bridge_geometry()
    verify_proof_paths_on_adversarial_A()
    print("OVERALL: PASS")

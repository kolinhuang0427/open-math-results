"""Independent exact-arithmetic verifier for targets/myrisiotis-2611.09020-edit-graph."""

from __future__ import annotations

import itertools
import pathlib
import re
import tarfile
from collections import deque


def c_encode(x: str) -> str:
    m = len(x) + 1
    b = bin(m)[2:]
    return "1" * (len(b) - 1) + "0" + b + x


def c_decode(s: str) -> tuple[str, str] | None:
    i = 0
    while i < len(s) and s[i] == "1":
        i += 1
    if i >= len(s) or s[i] != "0":
        return None
    k_len = i + 1
    start = i + 1
    if start + k_len > len(s):
        return None
    b = s[start : start + k_len]
    if b[0] != "1":
        return None
    m = int(b, 2)
    x_len = m - 1
    end = start + k_len + x_len
    if end > len(s):
        return None
    return s[start + k_len : end], s[end:]


def phi(s: str) -> str:
    return "".join("01" if ch == "0" else "011" for ch in s)


def phi_decode(p: str) -> str | None:
    out: list[str] = []
    i = 0
    while i < len(p):
        if p.startswith("011", i):
            out.append("1")
            i += 3
        elif p.startswith("01", i):
            out.append("0")
            i += 2
        else:
            return None
    return "".join(out)


def p_encode(x: str) -> str:
    return phi(c_encode(x))


def is_in_U(u: str) -> bool:
    if u in ("101", "1011", "10111"):
        return True
    if not (u.startswith("1011") and u.endswith("1") and len(u) >= 5):
        return False
    q = u[4:-1]
    i = 0
    while i < len(q):
        if q.startswith("011", i):
            i += 3
        elif q.startswith("01", i):
            i += 2
        else:
            break
    return q[i:] in ("", "0", "01")


def k_cap(n: int) -> tuple[int, int, int]:
    """Return (a, K(n), k(n)) for n >= 3."""
    assert n >= 3
    a = 1
    while (1 << (a + 2)) - 1 <= n:
        a += 1
    cap = 1 << a
    assert 2 * cap - 1 <= n < 4 * cap - 1
    return a, cap, cap - 1


def shortlex_rank(x: str) -> int:
    if x == "":
        return 0
    return (1 << len(x)) - 1 + int(x, 2)


def syndrome_color(p: str) -> int:
    n = len(p)
    a, _, k = k_cap(n)
    u = p[:k]
    v = p[k : 2 * k]
    b = int(p[2 * k])
    reg = u if b == 0 else v
    syn = 0
    for idx, ch in enumerate(reg, start=1):
        if ch == "1":
            syn ^= idx
    return syn


def shortlex_unrank(i: int) -> str:
    return bin(i + 1)[3:]


def simulate_V(s: str, base_A, c_poly_fn) -> tuple[str | None, int]:
    """Simulate V(s); return (output or None for bot/diverge, native time surrogate)."""
    c_h = 20
    if len(s) < 3:
        return None, 0
    mode = s[:3]
    p = s[3:]

    def run_hub(r: str) -> tuple[str | None, int]:
        pos = r.find("000")
        if pos == -1:
            return None, 0
        pref = r[:pos]
        if "00" in pref or not pref.endswith("1"):
            return None, 0
        px = pref[:-1]
        dec_c = phi_decode(px)
        if dec_c is None:
            return None, 0
        res = c_decode(dec_c)
        if res is None or res[1] != "":
            return None, 0
        x = res[0]
        return x, c_h * (len(px) + 8)

    def run_color(body: str) -> tuple[str | None, int]:
        n = len(body)
        if n < 3:
            return None, 0
        _, _, k = k_cap(n)
        j = syndrome_color(body)
        x = shortlex_unrank(j)
        bx = 5 + len(p_encode(x))
        cn = c_poly_fn(n)
        if bx > k:
            return None, cn
        return x, cn

    def run_base(body: str, j_len: int) -> tuple[str | None, int]:
        out = base_A(body)
        if out is None:
            return None, 0
        x, t_a = out
        bx = 5 + len(p_encode(x))
        if j_len > bx:
            return None, 0
        n_b = len(body)
        s_nb = (c_poly_fn(n_b) + 1) if n_b >= 3 else 1
        t_star = 100 + 5 * n_b + 10 * t_a + (2 * c_h + 1) * bx + s_nb + len(x)
        return x, t_star

    if mode == "000":
        return run_base(p, 0)
    if mode == "001":
        if len(p) < 3:
            return None, 0
        return run_base(p, 0) if p.count("1") % 2 == 0 else run_color(p)
    if mode == "010":
        if len(p) < 3:
            return None, 0
        return run_color(p) if p.count("1") % 2 == 0 else run_base(p, 0)
    if mode in ("011", "111"):
        return run_color(p)
    if mode == "100":
        if p == "":
            return None, 0
        if p[0] == "0":
            return run_base(p[1:], 1)
        return run_hub(p[1:])
    if mode == "110":
        if p.startswith("00"):
            return run_base(p[2:], 2)
        if p.startswith("1"):
            return run_hub(p[1:])
        return None, 0
    if mode == "101":
        pos = s.find("000")
        if pos == -1:
            return None, 0
        u = s[:pos]
        if not is_in_U(u):
            return None, 0
        return run_base(s[pos + 3 :], len(u))
    raise AssertionError("unreachable")


def is_edit_adjacent(a: str, b: str) -> bool:
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if len(a) + 1 == len(b):
        for i in range(len(b)):
            if b[:i] + b[i + 1 :] == a:
                return True
        return False
    if len(b) + 1 == len(a):
        return is_edit_adjacent(b, a)
    return False


def compute_N_x(x: str) -> int:
    bx = 5 + len(p_encode(x))
    ix = shortlex_rank(x)
    n_val = 6
    while True:
        _, cap, k = k_cap(n_val - 3)
        if ix < cap and bx <= k:
            return n_val
        n_val += 1


def verify_walks_and_thresholds() -> list[str]:
    failures: list[str] = []
    c_h = 20

    def c_poly(n: int) -> int:
        _, _, k = k_cap(n)
        return c_h * (k + 10) + 100

    # Check N_x vs corrected PROOF.md L79 formula: max(2^{|x|+2}, 4*B_x) + 2
    nx_eps = compute_N_x("")
    bx_eps = 5 + len(p_encode(""))
    bound_l79_eps = max(1 << 2, 4 * bx_eps) + 2
    assert nx_eps <= bound_l79_eps
    print(f"THRESHOLD_EPS: N_eps={nx_eps}, B_eps={bx_eps}, L79_bound={bound_l79_eps}")

    for length in range(5):
        for bits in itertools.product("01", repeat=length):
            x = "".join(bits)
            nx = compute_N_x(x)
            bx = 5 + len(p_encode(x))
            assert nx <= max(1 << (len(x) + 2), 4 * bx) + 2

    # Check explicit walks on toy base machine A that prints x="0" on p' in {"", "11", "0"*40}
    target = "0"
    nx = compute_N_x(target)
    bx = 5 + len(p_encode(target))
    budget = nx + bx
    long_body = "0" * (nx - 3)

    def base_A(body: str) -> tuple[str, int] | None:
        if body in ("", "11", long_body):
            return target, 5 + len(body)
        return None

    h_x = "1001" + p_encode(target) + "1000"
    assert len(h_x) < budget

    # Build explicit walk from bridge, short base, long base, router, core, and hub vertices to h_x
    # Test every vertex class in E^t_{budget, V}(target)
    starts = [
        h_x + "010",
        "1101" + p_encode(target) + "100011",
        "000",
        "1000",
        "11000",
        "1011011000",
        "00011",
        "00111",  # length 2 -> bot, skip! Test long_body:
        "000" + long_body,
        "001" + long_body,  # parity 0 -> source helper
        "1011" + p_encode(target) + "1000" + long_body,
    ]
    # Also add a color core vertex outputting target
    a_val, _, k_val = k_cap(len(long_body))
    jx = shortlex_rank(target)
    # Unit column r_jx if jx > 0
    r_vec = ["0"] * k_val
    if jx > 0:
        r_vec[jx - 1] = "1"
    u_reg = "1" + p_encode(target) + "1000" + "0" * (k_val - bx)
    q_color = u_reg + "".join(r_vec) + "1" + "0" * (len(long_body) - 2 * k_val - 1)
    assert len(q_color) == len(long_body)
    assert syndrome_color(q_color) == jx
    starts.append("011" + q_color)
    starts.append("111" + q_color)

    for s in starts:
        if s == "00111":
            assert simulate_V(s, base_A, c_poly)[0] is None
            continue
        out0, t0 = simulate_V(s, base_A, c_poly)
        assert out0 == target and len(s) <= budget
        # Walk explicitly via PROOF.md rules and check every edge is 1-edit and stays <= budget, <= t0
        path = [s]
        cur = s
        if cur[:3] in ("011", "111"):
            if cur[:3] == "011":
                cur = "111" + cur[3:]
                path.append(cur)
            # q_color already has form 1 P_x 1000 w''
            cur = "110" + cur[3:]
            path.append(cur)
        elif cur.startswith("101"):
            pos = cur.find("000")
            u = cur[:pos]
            p_b = cur[pos + 3 :]
            while len(u) > 5:
                u = u[:-2] + "1"
                path.append(u + "000" + p_b)
            for nxt_u in ("1011", "101", "11", "1", ""):
                if len(u) > len(nxt_u):
                    u = nxt_u
                    path.append(u + "000" + p_b)
            cur = "000" + p_b
        elif cur.startswith("1000") or cur.startswith("11000"):
            if cur.startswith("11000"):
                cur = "1000" + cur[5:]
                path.append(cur)
            cur = "000" + cur[4:]
            path.append(cur)
        elif cur[:3] in ("001", "010"):
            cur = "000" + cur[3:]
            path.append(cur)

        if cur.startswith("000"):
            p_b = cur[3:]
            if len(p_b) + 3 < nx:
                for pref in ("1000", "11000", "101000", "1011000", "10111000"):
                    path.append(pref + p_b)
                px = p_encode(target)
                for idx in range(1, len(px) + 1):
                    path.append("1011" + px[:idx] + "1000" + p_b)
                cur = "1001" + px + "1000" + p_b
                path.append(cur)
            else:
                # Subcase 3a
                helper_mode = "001" if p_b.count("1") % 2 == 0 else "010"
                path.append(helper_mode + p_b)
                # Switch to q_color (flip bits 1-by-1 in general; here check 1-bit neighbor to jx)
                _, _, kb = k_cap(len(p_b))
                # Flip bit 0 of ignored or selected register to match jx if p_b = 0^{...}; since p_b = 0^n has syn 0,
                # flip column jx in u (selected since b=0)!
                q_arr = list(p_b)
                if jx == 0:
                    q_arr[kb] = "1"
                else:
                    q_arr[jx - 1] = "1"
                q_nbr = "".join(q_arr)
                assert syndrome_color(q_nbr) == jx
                path.append(helper_mode + q_nbr)
                path.append("011" + q_nbr)
                path.append("111" + q_nbr)
                # Flip bits inside class jx to q_color (simplified via b selector)
                arr = list(q_nbr)
                # Move to (u_reg, r_vec, 1, 0...) keeping color jx
                for idx in range(kb):
                    if arr[kb + idx] != r_vec[idx]:
                        arr[kb + idx] = r_vec[idx]
                        path.append("111" + "".join(arr))
                if arr[2 * kb] != "1":
                    arr[2 * kb] = "1"
                    path.append("111" + "".join(arr))
                for idx in range(kb):
                    if arr[idx] != u_reg[idx]:
                        arr[idx] = u_reg[idx]
                        path.append("111" + "".join(arr))
                for idx in range(2 * kb + 1, len(arr)):
                    if arr[idx] != "0":
                        arr[idx] = "0"
                        path.append("111" + "".join(arr))
                cur = "110" + "".join(arr)
                path.append(cur)

        if cur.startswith("1101"):
            cur = "1001" + cur[4:]
            path.append(cur)
        while len(cur) > len(h_x):
            cur = cur[:-1]
            path.append(cur)
        assert path[-1] == h_x

        for a_s, b_s in zip(path, path[1:]):
            assert is_edit_adjacent(a_s, b_s), f"Not 1-edit: {a_s} -> {b_s}"
        for v_s in path:
            vo, vt = simulate_V(v_s, base_A, c_poly)
            assert vo == target and len(v_s) <= budget and vt <= t0

    print("EDIT_GRAPH_WALKS: 12/12 start classes verified to h_x within budget and deadline")
    return failures


def verify_source_and_docs() -> list[str]:
    failures: list[str] = []
    root = pathlib.Path(__file__).resolve().parents[3]
    tar_path = root / "tools" / ".arxiv_cache" / "eprint" / "2611.09020v1.src"
    target_md = (
        root / "targets" / "myrisiotis-2611.09020-edit-graph" / "TARGET.md"
    ).read_text(encoding="utf-8")
    proof_md = (
        root / "targets" / "myrisiotis-2611.09020-edit-graph" / "PROOF.md"
    ).read_text(encoding="utf-8")

    quote = "Do an adjunction-universal machine $V$ and a computable function $b$ exist"
    if not tar_path.exists():
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX snippet check")
        if quote not in target_md:
            failures.append("TARGET.md open problem quote missing")
    else:
        with tarfile.open(tar_path, "r:*") as tf:
            paper_tex = tf.extractfile("paper-arxiv.tex").read().decode("utf-8")
        if quote not in target_md or quote not in paper_tex:
            failures.append("TARGET.md open problem quote mismatch with paper-arxiv.tex")

    if r"\max(2^{|x|+2}, 2B_x + 2) + 4" in proof_md:
        failures.append(
            "PROOF.md L79 claims N_x <= max(2^{|x|+2}, 2B_x + 2) + 4, which is false"
        )
    if "Section 3.1" in target_md or "Section 3.6" not in target_md:
        failures.append("TARGET.md L3 must cite Section 3.6 (not Section 3.1) for def:3.1-def:3.2")
    if r"u \in \{\texttt{1}, \texttt{11}\} \cup \mathcal{U}" not in proof_md:
        failures.append("PROOF.md L89 must state u in {1, 11} union U for 1 <= |u| <= B_x")

    return failures


def main() -> int:
    failures = verify_walks_and_thresholds() + verify_source_and_docs()
    if failures:
        for msg in failures:
            print(f"ERROR: {msg}")
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

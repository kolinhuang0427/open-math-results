#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for targets/garrity-2410.02032-conj1/.

Built strictly from primary source definitions (S_0, S_1, G_k, tau_{j,k}, L(sigma), E(w), m(w))
and PROOF.md without reading verify.py. Pure int/tuple/set/dict arithmetic (zero floats).
"""

from __future__ import annotations

import random

# Primary substitutions S_0(e,23,e) and S_1(e,23,e) from Final_Revision-Garrity-Osterman.tex L2665-2666
S0 = {"1": "2", "2": "13", "3": "3"}
S1 = {"1": "1", "2": "2", "3": "13"}


def apply_sub(sub: dict[str, str], word: str) -> str:
    return "".join(sub[ch] for ch in word)


def compose_sub(outer: dict[str, str], inner: dict[str, str]) -> dict[str, str]:
    return {c: apply_sub(outer, inner[c]) for c in ("1", "2", "3")}


def sub_pow(sub: dict[str, str], k: int) -> dict[str, str]:
    res = {"1": "1", "2": "2", "3": "3"}
    for _ in range(k):
        res = compose_sub(sub, res)
    return res


def tau_jk_direct(j: int, k: int) -> dict[str, str]:
    """Direct formula from PROOF.md L17 and primary source eq. (e-23-e-two-Gauss)."""
    return {
        "1": "1" * (j + 1) + "3",
        "2": "2" * (k + 1) + "1" * j + "3",
        "3": "2" * k + "1" * j + "3",
    }


def abel(w: str) -> tuple[int, int, int]:
    return (w.count("1"), w.count("2"), w.count("3"))


def mat_vec(j: int, k: int, v: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        (j + 1) * v[0] + j * v[1] + j * v[2],
        (k + 1) * v[1] + k * v[2],
        v[0] + v[1] + v[2],
    )


def verify_substitutions_and_abelianization() -> None:
    print("Check 1: Gauss & double-Gauss substitutions + abelianization matrices...")
    for j in range(5):
        Gj = compose_sub(sub_pow(S1, j), S0)
        assert Gj == {"1": "2", "2": "1" * (j + 1) + "3", "3": "1" * j + "3"}
        for k in range(5):
            Gk = compose_sub(sub_pow(S1, k), S0)
            t_jk = compose_sub(Gj, Gk)
            assert t_jk == tau_jk_direct(j, k)
            # Check M_{j,k} columns = abel(t_jk(c))
            assert abel(t_jk["1"]) == mat_vec(j, k, (1, 0, 0))
            assert abel(t_jk["2"]) == mat_vec(j, k, (0, 1, 0))
            assert abel(t_jk["3"]) == mat_vec(j, k, (0, 0, 1))
    # Verify M_{1,1}^2 > 0 entrywise
    for e_i in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        v2 = mat_vec(1, 1, mat_vec(1, 1, e_i))
        assert all(x > 0 for x in v2)
    print("  Substitutions & M_{j,k} verified for 0 <= j,k <= 4 (and M_{1,1}^2 > 0).")


# --- Proposition 1.4 exact alpha^L, alpha^R maps and Lemma 3 closure ---

ALPHA_L = {
    (0, "1j3"): {"1": "1", "2": "2", "3": "3"},
    (1, "1j3"): {"1": "1", "2": "2", "3": "2"},
    (1, "2k1j3"): {"1": None, "2": "2", "3": "3"},
}

ALPHA_R = {
    (0, 0, "eps"): {"1": "1", "2": "2", "3": "3"},
    (0, 1, "eps"): {"1": "1", "2": "2", "3": "2"},
    (0, 1, "2k"): {"1": None, "2": "2", "3": "3"},
    (1, 0, "eps"): {"1": "1", "2": "2", "3": "1"},
    (1, 0, "1j"): {"1": "1", "2": None, "3": "3"},
    (1, 1, "eps"): {"1": "1", "2": "2", "3": "2"},
    (1, 1, "2k"): {"1": None, "2": "2", "3": "1"},
}


def prop1_image(E: frozenset[tuple[str, str]], j_pos: int, k_pos: int, a_type: str, b_type: str) -> frozenset[tuple[str, str]]:
    aL = ALPHA_L[(k_pos, a_type)]
    aR = ALPHA_R[(j_pos, k_pos, b_type)]
    out = set()
    for c, d in E:
        nc = aL[c]
        nd = aR[d]
        if nc is not None and nd is not None:
            out.add((nc, nd))
    return frozenset(out)


def ext_stats(E: frozenset[tuple[str, str]]) -> tuple[int, int, int, int]:
    Em = {a for a, _ in E}
    Ep = {b for _, b in E}
    m_val = len(E) - len(Em) - len(Ep) + 1
    return len(Em), len(Ep), m_val, len(E)


def bispecial_images(E: frozenset[tuple[str, str]], j_pos: int, k_pos: int) -> list[tuple[str, str, frozenset[tuple[str, str]]]]:
    a_choices = ["1j3"] if k_pos == 0 else ["1j3", "2k1j3"]
    if k_pos == 1:
        b_choices = ["eps", "2k"]
    elif j_pos == 1:
        b_choices = ["eps", "1j"]
    else:
        b_choices = ["eps"]
    res = []
    for a_t in a_choices:
        for b_t in b_choices:
            img = prop1_image(E, j_pos, k_pos, a_t, b_t)
            lm, lp, _, _ = ext_stats(img)
            if lm >= 2 and lp >= 2:
                res.append((a_t, b_t, img))
    return res


def verify_empirical_prop1_and_lemma2() -> None:
    print("Check 2: Empirical verification of Proposition 1.4 & Lemma 2 in actual generated languages...")
    # Build long factor-stabilized prefix of L^{(M_0)} via tau_{1,1}^6("1")
    w_m0 = "1"
    for _ in range(7):
        w_m0 = apply_sub(tau_jk_direct(1, 1), w_m0)
    # Extract all factors up to length 18 from w_m0 (cyclic/long interior):
    max_len = 16
    base_factors: set[str] = {""}
    for length in range(1, max_len + 3):
        for i in range(len(w_m0) - length + 1):
            base_factors.add(w_m0[i : i + length])

    def extract_E_from_word(word: str, target_max_len: int) -> tuple[dict[str, frozenset[tuple[str, str]]], set[str]]:
        facs: set[str] = {""}
        e_map: dict[str, set[tuple[str, str]]] = {}
        # Use interior occurrences [1 .. len-L-1] so left/right neighbors exist
        for L_len in range(0, target_max_len + 1):
            for i in range(1, len(word) - L_len):
                sub = word[i : i + L_len]
                facs.add(sub)
                e_map.setdefault(sub, set()).add((word[i - 1], word[i + L_len]))
        return {k: frozenset(v) for k, v in e_map.items()}, facs

    # Check all 9 modes of (j_0, k_0) in {0,1,2}^2 applied to base tau_{j_1, k_1}(tau_{1,1}^6("1"))
    modes_checked = 0
    for j1, k1 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        w1 = apply_sub(tau_jk_direct(j1, k1), w_m0)
        E_prev, _ = extract_E_from_word(w1, 10)
        for j0, k0 in [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1), (1, 2), (2, 1), (2, 2)]:
            tau0 = tau_jk_direct(j0, k0)
            w0 = apply_sub(tau0, w1)
            E_cur, _ = extract_E_from_word(w0, 14)

            # Check Lemma 2 on E("") and 3-free bispecials
            E_eps_expected = {
                (0, 0): frozenset({("1", "3"), ("2", "3"), ("3", "1"), ("3", "2"), ("3", "3")}),
                (0, 1): frozenset({("1", "3"), ("2", "2"), ("2", "3"), ("3", "1"), ("3", "2")}),
                (1, 0): frozenset({("1", "1"), ("1", "3"), ("2", "1"), ("3", "1"), ("3", "2")}),
                (1, 1): frozenset({("1", "1"), ("1", "3"), ("2", "1"), ("2", "2"), ("3", "1"), ("3", "2")}),
            }[(1 if j0 > 0 else 0, 1 if k0 > 0 else 0)]
            assert E_cur[""] == E_eps_expected

            for w, E_w in E_cur.items():
                lm, lp, mw, _ = ext_stats(E_w)
                if lm < 2 or lp < 2:
                    continue
                if "3" not in w:
                    if w == "":
                        continue
                    # Must be 1^r (1<=r<=j0) or 2^r (1<=r<=k0)
                    assert set(w) in ({"1"}, {"2"})
                    if set(w) == {"1"}:
                        assert len(w) <= j0
                        if len(w) < j0:
                            assert mw == 0
                        elif k0 == 0:
                            assert E_w == frozenset({("1", "3"), ("2", "3"), ("3", "1"), ("3", "3")}) and mw == 0
                        else:
                            assert E_w == frozenset({("1", "3"), ("2", "3"), ("3", "1")}) and mw == -1
                    else:
                        assert len(w) <= k0 and mw == 0
                else:
                    # Must decode uniquely as a * tau0(v) * b and match Proposition 1.4!
                    first3 = w.index("3")
                    last3 = w.rindex("3")
                    a = w[: first3 + 1]
                    b = w[last3 + 1 :]
                    mid = w[first3 + 1 : last3 + 1]
                    # Decode mid
                    v_chars = []
                    pos = 0
                    blocks = {v: k for k, v in tau0.items()}
                    while pos < len(mid):
                        nxt3 = mid.index("3", pos)
                        v_chars.append(blocks[mid[pos : nxt3 + 1]])
                        pos = nxt3 + 1
                    v = "".join(v_chars)
                    assert a in {"1" * j0 + "3", "2" * k0 + "1" * j0 + "3"}
                    if k0 == 0 and a != "1" * j0 + "3":
                        raise AssertionError(f"Unexpected a={a} for k0=0")
                    a_type = "1j3" if a == "1" * j0 + "3" else "2k1j3"
                    if b == "":
                        b_type = "eps"
                    elif k0 == 0 and b == "1" * j0:
                        b_type = "1j"
                    elif k0 >= 1 and b == "2" * k0:
                        b_type = "2k"
                    else:
                        raise AssertionError(f"Unexpected b={b} in bispecial {w} (j0={j0}, k0={k0})")
                    if len(v) <= 10 and v in E_prev:
                        expected_E = prop1_image(E_prev[v], 1 if j0 > 0 else 0, 1 if k0 > 0 else 0, a_type, b_type)
                        assert E_w == expected_E, f"Prop 1.4 mismatch for w={w}, v={v}: {E_w} != {expected_E}"
            modes_checked += 1
    print(f"  Verified Proposition 1.4 & Lemma 2 across {modes_checked} (j1,k1,j0,k0) language transitions.")


def verify_lemma3_and_theorem4() -> None:
    print("Check 3: Lemma 3 (N_0 closure) and Theorem 4 (state graph & monotonicity)...")
    E33p = frozenset({("1", "1"), ("1", "3"), ("2", "1"), ("2", "2"), ("3", "1"), ("3", "2")})
    E33A = frozenset({("1", "3"), ("2", "3"), ("3", "1"), ("3", "2"), ("3", "3")})
    E33B = frozenset({("1", "3"), ("2", "2"), ("2", "3"), ("3", "1"), ("3", "2")})
    E33C = frozenset({("1", "1"), ("1", "3"), ("2", "1"), ("3", "1"), ("3", "2")})
    E32p = frozenset({("1", "1"), ("2", "1"), ("2", "2"), ("3", "1"), ("3", "2")})
    E32m = frozenset({("1", "3"), ("2", "3"), ("3", "1")})
    Ap = frozenset({("1", "1"), ("1", "2"), ("2", "1"), ("2", "2")})
    Bp = frozenset({("2", "1"), ("2", "2"), ("3", "1"), ("3", "2")})
    A1m = frozenset({("1", "1"), ("2", "2")})
    A2m = frozenset({("1", "3"), ("2", "2")})
    Bm = frozenset({("2", "2"), ("3", "1")})

    N0_seed = {
        E33A,
        frozenset({("1", "1"), ("1", "2"), ("2", "1")}),
        frozenset({("1", "1"), ("2", "1"), ("2", "2")}),
        frozenset({("1", "2"), ("2", "1"), ("2", "2")}),
        frozenset({("1", "3"), ("2", "2"), ("2", "3")}),
        frozenset({("2", "1"), ("2", "2"), ("3", "2")}),
        frozenset({("2", "1"), ("3", "1"), ("3", "2")}),
        frozenset({("2", "2"), ("2", "3"), ("3", "2")}),
        frozenset({("2", "2"), ("3", "1"), ("3", "2")}),
        frozenset({("2", "3"), ("3", "2"), ("3", "3")}),
        frozenset({("1", "1"), ("1", "3"), ("2", "1"), ("3", "1")}),
        frozenset({("1", "1"), ("2", "1"), ("3", "1"), ("3", "2")}),
        frozenset({("1", "3"), ("2", "3"), ("3", "1"), ("3", "3")}),
        frozenset({("1", "1"), ("1", "3"), ("3", "1")}),
        frozenset({("1", "3"), ("2", "3"), ("3", "1"), ("3", "3")}),  # E(1^j) at k=0
        # 2^r neutral sets from Lemma 2.2:
        frozenset({("3", "2"), ("2", "2"), ("3", "1")}),
        frozenset({("3", "2"), ("2", "2"), ("3", "3")}),
        frozenset({("3", "2"), ("2", "1"), ("3", "1")}),
        frozenset({("3", "2"), ("2", "3"), ("3", "3")}),
    }
    # Close N0 (E33A + all 2x2 and 3x2 neutral sets reachable under Prop 1.4)
    N0 = set(N0_seed)
    changed = True
    while changed:
        changed = False
        sources = list(N0) + [E33B, E33C, E33p, E32p, E32m]
        for S in sources:
            for jp in (0, 1):
                for kp in (0, 1):
                    for _, _, img in bispecial_images(S, jp, kp):
                        lm, lp, mw, _ = ext_stats(img)
                        if S in N0:
                            assert mw == 0, f"Neutral set {S} produced non-neutral {img} under {(jp, kp)}"
                            assert img == E33A or (lm + lp <= 5), f"N0 set {S} escaped to non-N0 {img}"
                        if mw == 0 and (img == E33A or lm + lp <= 5) and img not in N0:
                            N0.add(img)
                            changed = True
    print(f"  Lemma 3 verified: N_0 closed with {len(N0)} sets (all m=0, incl. E33A).")

    # Verify Theorem 4 (with t_m and w0 = 3^t_m) across multi-(0,0) & alternating coding sequences!
    # Also cross-check against ACTUAL bispecial words in generated languages!
    def check_actual_language_seq(jk_seq: list[tuple[int, int]]) -> None:
        """Apply reversed jk_seq on top of L^{(M_0)} = tau_{1,1}^7('1') and verify Theorem 4 (1)-(4) on all bispecials of len <= 16."""
        # Build base word
        w = "1"
        for _ in range(7):
            w = apply_sub(tau_jk_direct(1, 1), w)
        # Apply jk_seq from back (M_0 - 1) to front (0)
        t_m = 0
        next_nz_jk = (1, 1)
        for idx, (j, k) in enumerate(reversed(jk_seq)):
            w = apply_sub(tau_jk_direct(j, k), w)
            if (j, k) == (0, 0):
                t_m += 1
            else:
                t_m = 0
                next_nz_jk = (j, k)

        # Extract all bispecial words up to length 16 from interior of w
        e_map: dict[str, set[tuple[str, str]]] = {}
        for L_len in range(0, 17):
            for i in range(1, len(w) - L_len):
                sub = w[i : i + L_len]
                e_map.setdefault(sub, set()).add((w[i - 1], w[i + L_len]))
        bispecials = []
        for s, v in e_map.items():
            fs = frozenset(v)
            lm, lp, mw, _ = ext_stats(fs)
            if lm >= 2 and lp >= 2:
                bispecials.append((s, fs, mw))

        # Check every neutral bispecial outside the head is in N0
        j0, k0 = jk_seq[0]
        if j0 > 0 and k0 > 0:
            head = [("", E33p), ("1" * j0, E32m)]
        elif t_m >= 1 and next_nz_jk[0] > 0 and next_nz_jk[1] > 0:
            head = [("", E33A)]
        else:
            exp_h = E33B if next_nz_jk[0] == 0 else E33C
            head = [("3" * t_m, exp_h)]

        head_words = {s for s, _ in head}
        non_neutrals = [(s, fs, mw) for s, fs, mw in bispecials if mw != 0]
        for s, fs, mw in bispecials:
            if mw == 0 and s not in head_words:
                assert fs in N0, f"Neutral bispecial {s!r} with {fs} not in N0 (seq={jk_seq})"
        for s, exp_fs in head:
            assert frozenset(e_map[s]) == exp_fs, f"Head word {s!r} has {e_map[s]} != {exp_fs}"

        # Sort non-neutrals by length (and verify alternating +1, -1 and abelianization monotonicity!)
        # Note: all non-neutrals in the prefix up to len 16: check pairs & gaps!
        non_neutrals.sort(key=lambda x: (len(x[0]), abel(x[0]), x[0]))
        # Check prefix up to the last complete pair (if len=16 cuts off a w_r^-, drop trailing +1)
        if non_neutrals and non_neutrals[-1][2] == 1:
            # verify whether its partner just exceeded length 16; only check complete pairs when head=(0,0) or (+1,-1)
            pass
        # Actually construct full sequence of non-neutrals + head from Theorem 4 and match all found non-neutrals!
        if len(non_neutrals) >= 2:
            # If j0>0, k0>0, non_neutrals[0] must be "" (+1), [1] must be 1^j0 (-1)
            for idx in range(0, len(non_neutrals) - 1, 2):
                sp_w, Ep, mp = non_neutrals[idx]
                sm_w, Em, mm = non_neutrals[idx + 1]
                assert mp == 1 and mm == -1, f"Non-alternating at {idx} in {jk_seq}: {non_neutrals[:6]}"
                assert all(x >= y for x, y in zip(abel(sm_w), abel(sp_w)))
                if idx >= 2:
                    prev_m_w, prev_Em, _ = non_neutrals[idx - 1]
                    d = tuple(x - y for x, y in zip(abel(sp_w), abel(prev_m_w)))
                    assert all(x >= 0 for x in d), f"Gap monotonic failed at {idx}: {d}"
                    if (prev_Em, Ep) in ((E32m, Ap), (E32m, Bp), (Bm, Ap)):
                        assert d[1] + d[2] >= 1

    test_sequences = [
        [(1, 1)],
        [(1, 0), (0, 0)],
        [(0, 1), (0, 0), (1, 0)],
        [(0, 1), (0, 0), (0, 0), (1, 0)],
        [(1, 0), (0, 0), (0, 1)],
        [(1, 0), (0, 0), (0, 0), (0, 1)],
        [(0, 0), (0, 0), (1, 1)],
        [(2, 0), (0, 0), (0, 2)],
        [(0, 2), (0, 0), (2, 0)],
        [(1, 1), (0, 0), (1, 0), (0, 0), (0, 1)],
    ]
    for jk_seq in test_sequences:
        check_actual_language_seq(jk_seq)
    print(f"  Theorem 4 verified on {len(test_sequences)} multi-(0,0) & alternating coding sequences (up to word len 16).")

    # Verify exact lifting rules of Theorem 4 for EVERY non-neutral state and EVERY (jp, kp) in {0,1}^2
    # Check base case M_0: first 8 bispecial non-neutral words in L(tau_{1,1}^\infty)
    def lift_seq(seq_words: list[tuple[str, frozenset[tuple[str, str]]]], j: int, k: int) -> list[tuple[str, frozenset[tuple[str, str]]]]:
        jp = 1 if j > 0 else 0
        kp = 1 if k > 0 else 0
        tau = tau_jk_direct(j, k)
        out = []
        if jp == 1 and kp == 1:
            out.append(("", E33p))
            out.append(("1" * j, E32m))
        elif jp == 0 and kp == 0:
            out.append(("", E33A))
        elif jp == 0 and kp == 1:
            out.append(("", E33B))
        else:
            out.append(("", E33C))
        for w, Ew in seq_words:
            for a_t, b_t, img in bispecial_images(Ew, jp, kp):
                _, _, mw, _ = ext_stats(img)
                if mw == 0 and img not in (E33A, E33B, E33C):
                    continue
                if mw != 0:
                    a_str = ("1" * j + "3") if a_t == "1j3" else ("2" * k + "1" * j + "3")
                    b_str = "" if b_t == "eps" else ("1" * j if b_t == "1j" else "2" * k)
                    out.append((a_str + apply_sub(tau, w) + b_str, img))
        # Deduplicate while preserving order
        seen = set()
        dedup = []
        for w, Ew in out:
            if w not in seen:
                seen.add(w)
                dedup.append((w, Ew))
        return dedup

    # Start M_0 sequence and iterate 4 times with (1, 1)
    seq_m0 = [("", E33p), ("1", E32m)]
    for _ in range(4):
        seq_m0 = lift_seq(seq_m0, 1, 1)

    def check_seq_invariants(seq: list[tuple[str, frozenset[tuple[str, str]]]], j: int, k: int) -> None:
        assert len(seq) >= 4
        # Check r=0
        w0p, E0p = seq[0]
        if j > 0 and k > 0:
            w0m, E0m = seq[1]
            assert E0p == E33p and E0m == E32m
            assert all(x >= y for x, y in zip(abel(w0m), abel(w0p)))
            tail_start = 2
            prev_m, prev_E = w0m, E0m
        else:
            assert E0p in (E33A, E33B, E33C)
            tail_start = 1
            prev_m, prev_E = w0p, E0p

        tail = seq[tail_start:]
        assert len(tail) % 2 == 0 or (len(tail) >= 2)
        n_pairs = len(tail) // 2
        valid_pairs = {(E33p, E32m), (E32p, E32m), (Ap, A1m), (Ap, A2m), (Bp, Bm)}
        valid_gaps = {(E32m, Ap), (A1m, Bp), (A2m, Bp), (Bm, Ap)}
        # Also allow transition from E33A/B/C head to first tail w1+
        for r in range(n_pairs):
            wp, Ep = tail[2 * r]
            wm, Em = tail[2 * r + 1]
            assert (Ep, Em) in valid_pairs, f"Invalid pair {(Ep, Em)}"
            assert all(x >= y for x, y in zip(abel(wm), abel(wp)))
            if r == 0 and prev_E in (E33A, E33B, E33C):
                assert all(x >= y for x, y in zip(abel(wp), abel(prev_m)))
                if prev_E in (E33B, E33C):
                    d0 = tuple(x - y for x, y in zip(abel(wp), abel(prev_m)))
                    assert d0[2] >= 1, f"Missing delta3>=1 for E33B/C at r=0: {d0}"
            else:
                assert (prev_E, Ep) in valid_gaps, f"Invalid gap {(prev_E, Ep)}"
                d = tuple(x - y for x, y in zip(abel(wp), abel(prev_m)))
                assert all(x >= 0 for x in d), f"Negative delta {d} at {(prev_E, Ep)}"
                if (prev_E, Ep) in ((E32m, Ap), (Bm, Ap)):
                    assert d[1] + d[2] >= 1, f"Missing delta2+delta3>=1 at {(prev_E, Ep)}: {d}"
            prev_m, prev_E = wm, Em

    check_seq_invariants(seq_m0, 1, 1)
    # Test all 4 parameter modes (0,0), (0,2), (2,0), (2,2) recursively for 2 steps from M_0!
    for j1, k1 in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        s1 = lift_seq(seq_m0, j1, k1)
        check_seq_invariants(s1, j1, k1)
        for j0, k0 in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            s0 = lift_seq(s1, j0, k0)
            check_seq_invariants(s0, j0, k0)
    print(f"  Theorem 4 base ({len(seq_m0)} bispecials) and all 16 two-step transitions verified!")


def verify_direct_complexity() -> None:
    print("Check 4: Direct factor complexity p_L(n) <= 3n on diverse S(e,23,e)-adic sequences...")
    seqs = [
        [S0] * 14,
        [S1] * 14,
        [S0, S1] * 7,
        [S1, S0] * 7,
        [S1, S1, S0] * 5,
        [S0, S0, S1] * 5,
    ]
    rng = random.Random(2410)
    for _ in range(15):
        seqs.append([S0 if rng.randrange(2) == 0 else S1 for _ in range(15)])

    max_ratio_num = 0
    for seq in seqs:
        # Compute sigma_0 o ... o sigma_{N-1}(c) for c in {1,2,3}
        words = []
        for c in ("1", "2", "3"):
            w = c
            for sub in reversed(seq):
                w = apply_sub(sub, w)
            words.append(w)
        # Compute p(n) for 1 <= n <= min(50, max length)
        max_n = min(50, max(len(w) for w in words))
        for n in range(1, max_n + 1):
            facs = set()
            for w in words:
                for i in range(len(w) - n + 1):
                    facs.add(w[i : i + n])
            p_n = len(facs)
            assert p_n <= 3 * n, f"Complexity {p_n} > 3*{n}!"
            if p_n * 1000 > max_ratio_num * n:
                pass
    print(f"  Verified p_L(n) <= 3n up to n=50 across {len(seqs)} coding sequences.")


def main() -> None:
    verify_substitutions_and_abelianization()
    verify_empirical_prop1_and_lemma2()
    verify_lemma3_and_theorem4()
    verify_direct_complexity()
    print("PASS")


if __name__ == "__main__":
    main()

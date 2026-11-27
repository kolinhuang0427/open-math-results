"""Exact-arithmetic verification script for PROOF.md (Schwob, arXiv:2606.12129v1, Conjecture 8.7).

Uses pure integer arithmetic only (zero floats, zero true-division '/' operators).
Prints PASS on success (exit code 0) or FAIL on any check failure (exit code 1).
"""

import ast
import itertools
import sys


# ---- Core exact D_n arithmetic (clean notation: s_0 swaps+negates (1,2), s_i swaps (i,i+1) for 1<=i<=n-1) ----

def length_dn(w):
    n = len(w)
    c = 0
    for i in range(n):
        wi = w[i]
        for j in range(i + 1, n):
            wj = w[j]
            if wi > wj:
                c += 1
            if wi + wj < 0:
                c += 1
    return c


def apply_s_right(w, k):
    """Right multiplication w * s_k (0 <= k <= n-1): s_0 swaps+negates pos (0,1), s_k swaps pos (k-1,k)."""
    arr = list(w)
    if k == 0:
        arr[0], arr[1] = -w[1], -w[0]
    else:
        arr[k - 1], arr[k] = arr[k], arr[k - 1]
    return tuple(arr)


def apply_s_left(w, k):
    """Left multiplication s_k * w (0 <= k <= n-1): s_0 swaps values 1<->-2, -1<->2; s_k swaps values k<->k+1."""
    arr = list(w)
    if k == 0:
        for i, val in enumerate(arr):
            if val == 1:
                arr[i] = -2
            elif val == 2:
                arr[i] = -1
            elif val == -1:
                arr[i] = 2
            elif val == -2:
                arr[i] = 1
    else:
        a, b = k, k + 1
        for i, val in enumerate(arr):
            if val == a:
                arr[i] = b
            elif val == b:
                arr[i] = a
            elif val == -a:
                arr[i] = -b
            elif val == -b:
                arr[i] = -a
    return tuple(arr)


def apply_refl(w, typ, p, q):
    """Apply reflection t_{p,q}^+ (typ==0) or t_{p,q}^- (typ==1) on 0-based positions p < q."""
    arr = list(w)
    if typ == 0:
        arr[p], arr[q] = arr[q], arr[p]
    else:
        arr[p], arr[q] = -arr[q], -arr[p]
    return tuple(arr)


def perm_mul(u, v):
    """Composition (u * v)(i) = u(v(i)) on 1-based signed permutations."""
    return tuple(u[x - 1] if x > 0 else -u[-x - 1] for x in v)


def upper_covers_dn(w):
    n = len(w)
    lw = length_dn(w)
    res = set()
    for i in range(n):
        wi = w[i]
        for j in range(i + 1, n):
            wj = w[j]
            if wi < wj:
                t = apply_refl(w, 0, i, j)
                if length_dn(t) == lw + 1:
                    res.add(t)
            if wi + wj > 0:
                t = apply_refl(w, 1, i, j)
                if length_dn(t) == lw + 1:
                    res.add(t)
    return res


def lower_covers_dn(w):
    n = len(w)
    lw = length_dn(w)
    res = set()
    for i in range(n):
        wi = w[i]
        for j in range(i + 1, n):
            wj = w[j]
            if wi > wj:
                t = apply_refl(w, 0, i, j)
                if length_dn(t) == lw - 1:
                    res.add(t)
            if wi + wj < 0:
                t = apply_refl(w, 1, i, j)
                if length_dn(t) == lw - 1:
                    res.add(t)
    return res


def is_weak_cover(u, v):
    if length_dn(v) != length_dn(u) + 1:
        return False
    return any(apply_s_right(u, k) == v for k in range(len(u)))


def is_strict_cover(u, v):
    return (v in upper_covers_dn(u)) and (not is_weak_cover(u, v))


def comm_up(a, b):
    return upper_covers_dn(a) & upper_covers_dn(b)


def comm_lo(a, b):
    return lower_covers_dn(a) & lower_covers_dn(b)


def tau_aut(w):
    """Dynkin automorphism tau(w) = t_1 w t_1 swapping s_0 <-> s_1: negates pos 0 and value +-1."""
    arr = list(w)
    arr[0] = -arr[0]
    arr = [-x if abs(x) == 1 else x for x in arr]
    return tuple(arr)


def in_wj0(w):
    return all(x > 0 for x in w)


def in_wj1(w):
    return in_wj0(tau_aut(w))


def in_wjn1(w):
    return w[-1] == len(w)


def in_q0(w):
    lw = length_dn(w)
    return all(length_dn(apply_s_left(w, k)) > lw for k in range(1, len(w)))


def in_qn1(w):
    lw = length_dn(w)
    return all(length_dn(apply_s_left(w, k)) > lw for k in range(len(w) - 1))


def q_of_subset(n, A_1based):
    """Construct q(A) in ^{J_0} D_n for even-sized subset A of {1..n}."""
    A = set(A_1based)
    assert len(A) % 2 == 0
    neg_vals = list(range(-len(A), 0))
    pos_vals = list(range(len(A) + 1, n + 1))
    ni = 0
    pi = 0
    out = []
    for pos in range(1, n + 1):
        if pos in A:
            out.append(neg_vals[ni])
            ni += 1
        else:
            out.append(pos_vals[pi])
            pi += 1
    return tuple(out)


# ---- Check 0: AST zero-float / zero-division self-audit ----

def check_0_zero_floats():
    with open(__file__, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=__file__)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            raise AssertionError(f"Float literal detected: {node.value}")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            raise AssertionError("True division '/' detected")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            raise AssertionError("float() call detected")
    print("[OK] Check 0: Zero-float / zero-division AST self-audit passed.")


# ---- Check 1: Lemma 1 (Common Covers of Reflection Neighbors) exhaustively on D_4 + D_3 Type II check ----

def check_1_lemma1():
    # Explicit D_3 Type II check in Lemma 1 proof:
    # g = t_{1,2}^+ t_{2,3}^+ sends (1,2,3) -> (2,3,1); for r3 in {t12^-, t23^-, t13^-}, r3*g has order 4 (not a reflection)
    e3 = (1, 2, 3)
    for p, q in ((0, 1), (1, 2), (0, 2)):
        r3 = apply_refl(e3, 1, p, q)
        r4 = apply_refl(apply_refl(r3, 0, 0, 1), 0, 1, 2)
        assert perm_mul(r4, r4) != e3, f"Unexpected involution for {(p, q)}: {r4}"

    # Exhaustive check over ALL 192 elements of D_4 (upper and lower cover pairs):
    elems = []
    for p in itertools.permutations(range(1, 5)):
        for signs in itertools.product((-1, 1), repeat=4):
            if signs.count(-1) % 2 == 0:
                elems.append(tuple(s * x for s, x in zip(signs, p)))
    assert len(elems) == 192
    refls = [(t, i, j) for i in range(4) for j in range(i + 1, 4) for t in (0, 1)]
    up_map = {w: upper_covers_dn(w) for w in elems}
    lo_map = {w: lower_covers_dn(w) for w in elems}

    up_pairs = 0
    lo_pairs = 0
    for u in elems:
        lu = length_dn(u)
        u_ups = [(r, apply_refl(u, *r)) for r in refls if apply_refl(u, *r) in up_map[u]]
        for i in range(len(u_ups)):
            r1, a = u_ups[i]
            s1 = {r1[1], r1[2]}
            for j in range(i + 1, len(u_ups)):
                r2, b = u_ups[j]
                s2 = {r2[1], r2[2]}
                comm = up_map[a] & up_map[b]
                cands = set()
                w12 = apply_refl(a, *r2)
                if length_dn(w12) == lu + 2 and w12 in up_map[a] and w12 in up_map[b]:
                    cands.add(w12)
                if len(s1 & s2) == 1:
                    w21 = apply_refl(b, *r1)
                    if length_dn(w21) == lu + 2 and w21 in up_map[a] and w21 in up_map[b]:
                        cands.add(w21)
                assert comm == cands, f"Upper cover Lemma 1 fail at {u}, {r1}, {r2}"
                up_pairs += 1

        u_los = [(r, apply_refl(u, *r)) for r in refls if apply_refl(u, *r) in lo_map[u]]
        for i in range(len(u_los)):
            r1, a = u_los[i]
            s1 = {r1[1], r1[2]}
            for j in range(i + 1, len(u_los)):
                r2, b = u_los[j]
                s2 = {r2[1], r2[2]}
                comm = lo_map[a] & lo_map[b]
                cands = set()
                w12 = apply_refl(a, *r2)
                if length_dn(w12) == lu - 2 and w12 in lo_map[a] and w12 in lo_map[b]:
                    cands.add(w12)
                if len(s1 & s2) == 1:
                    w21 = apply_refl(b, *r1)
                    if length_dn(w21) == lu - 2 and w21 in lo_map[a] and w21 in lo_map[b]:
                        cands.add(w21)
                assert comm == cands, f"Lower cover Lemma 1 fail at {u}, {r1}, {r2}"
                lo_pairs += 1

    print(f"[OK] Check 1: Lemma 1 verified exhaustively on D_4 ({up_pairs} upper pairs, {lo_pairs} lower pairs).")


# ---- Check 2: Explicit quotients ^{J_0} D_n, ^{J_{n-1}} D_n and their join-irreducibles (n = 4..7) ----

def check_2_quotients_and_jirrs():
    for n in (4, 5, 6, 7):
        # 1) ^{J_0} D_n via all 2^{n-1} even-sized subsets A of {1..n}
        q0_set = set()
        for r in range(0, n + 1, 2):
            for A in itertools.combinations(range(1, n + 1), r):
                q = q_of_subset(n, A)
                assert in_q0(q), f"q({A}) not in ^J0 D_{n}: {q}"
                q0_set.add(q)
        assert len(q0_set) == (1 << (n - 1))

        # Check all weak covers inside ^{J_0} D_n and extract join-irreducibles outside W_{J_1} U W_{J_{n-1}}
        jirrs_outside = set()
        for q in q0_set:
            lq = length_dn(q)
            if lq == 0:
                continue
            wlc = [apply_s_right(q, k) for k in range(n)
                   if length_dn(apply_s_right(q, k)) == lq - 1 and apply_s_right(q, k) in q0_set]
            if len(wlc) == 1 and (not in_wj1(q)) and (not in_wjn1(q)):
                jirrs_outside.add(q)

        # Expected set {q_{(a, n)} : 2 <= a <= n-1}
        expected_q0 = set()
        for a in range(2, n):
            if a % 2 == 0:
                qa = tuple(range(a + 1, n + 1)) + tuple(-x for x in range(a, 0, -1))
            elif a < n - 1:
                qa = (-(a + 1),) + tuple(range(a + 2, n + 1)) + tuple(-x for x in range(a, 0, -1))
            else:
                qa = tuple(-x for x in range(n, 0, -1))
            expected_q0.add(qa)
        assert jirrs_outside == expected_q0, f"J(^J0 D_{n}) mismatch: {jirrs_outside} != {expected_q0}"

        # 2) ^{J_{n-1}} D_n of size 2n
        qn1_set = set()
        for k in range(1, n + 1):
            qp = tuple(range(1, k)) + (n,) + tuple(range(k, n))
            assert in_qn1(qp)
            qn1_set.add(qp)
        q1m = (-n, -1) + tuple(range(2, n))
        assert in_qn1(q1m)
        qn1_set.add(q1m)
        for k in range(2, n + 1):
            qm = (-1,) + tuple(range(2, k)) + (-n,) + tuple(range(k, n))
            assert in_qn1(qm)
            qn1_set.add(qm)
        assert len(qn1_set) == 2 * n

        jirrs_n1 = set()
        for q in qn1_set:
            lq = length_dn(q)
            if lq == 0:
                continue
            wlc = [apply_s_right(q, k) for k in range(n)
                   if length_dn(apply_s_right(q, k)) == lq - 1 and apply_s_right(q, k) in qn1_set]
            if len(wlc) == 1 and (not in_wj0(q)) and (not in_wj1(q)):
                jirrs_n1.add(q)
        expected_qn1 = {(-1,) + tuple(range(2, k)) + (-n,) + tuple(range(k, n)) for k in range(3, n + 1)}
        assert jirrs_n1 == expected_qn1, f"J(^Jn1 D_{n}) mismatch"

    print("[OK] Check 2: Explicit quotients ^J0 D_n, ^J_{n-1} D_n & join-irreducibles verified for n = 4..7.")


# ---- Check 3: Lemma 9 (Universal Spin-Quotient Propagation) exhaustively for n = 4..7 ----

def check_3_lemma9_spin_prop():
    total_pairs = 0
    for n in (4, 5, 6, 7):
        q0_set = {
            q_of_subset(n, A)
            for r in range(0, n + 1, 2)
            for A in itertools.combinations(range(1, n + 1), r)
        }
        for u in q0_set:
            lu = length_dn(u)
            for t in range(n):
                ut = apply_s_right(u, t)
                if length_dn(ut) != lu + 1 or ut not in q0_set:
                    continue
                for k in range(1, n):
                    su = apply_s_left(u, k)
                    if is_strict_cover(u, su):
                        sut = apply_s_left(ut, k)
                        assert comm_up(su, ut) == {sut}, f"Lemma 9 failed at n={n}, u={u}, k={k}, t={t}"
                        total_pairs += 1
    print(f"[OK] Check 3: Lemma 9 (Universal Spin-Quotient Propagation) verified exhaustively ({total_pairs} pairs, n = 4..7).")


# ---- Check 4: Lemmas 6, 7, 8, 10 explicit step-by-step verification across n = 4..10 ----

def check_4_lemmas_6_to_10():
    for n in range(4, 11):
        # --- Lemma 6: No 3-Cycle (Case B1) ---
        d = tuple(range(4, n))
        u0 = (2, 3, 1, n) + d
        v0 = (2, n, 1, 3) + d
        assert in_wj0(u0) and in_wj0(v0) and is_strict_cover(u0, v0)
        u1 = (-3, -2, 1, n) + d
        v1 = (-n, -2, 1, 3) + d
        assert is_weak_cover(u0, u1) and comm_up(v0, u1) == {v1}
        u2 = (-3, 1, -2, n) + d
        v2 = (-n, 1, -2, 3) + d
        assert is_weak_cover(u1, u2) and comm_up(v1, u2) == {v2}
        u3 = (-1, 3, -2, n) + d
        v3 = (-1, n, -2, 3) + d
        assert is_weak_cover(v3, v2) and is_weak_cover(u3, u2) and comm_lo(u2, v3) == {u3}
        b0 = (-1, -2, 3, n) + d
        u4 = (-1, -2, n, 3) + d
        v4 = (-1, 3, n, -2) + d
        assert is_weak_cover(b0, u3) and is_weak_cover(b0, u4)
        assert is_weak_cover(u4, v3) and is_weak_cover(u3, v4) and comm_up(u3, u4) == {v3, v4}
        w0 = (-2, -1, n, 3) + d
        w1 = (-2, 3, n, -1) + d
        assert in_wj1(w0) and in_wj1(w1) and is_strict_cover(w0, w1) and is_weak_cover(w0, u4)
        v5 = (3, -2, n, -1) + d
        assert is_weak_cover(w1, v5) and comm_up(w1, u4) == {v4, v5}
        cu, cv = u4, v5
        for pos in range(2, n - 1):
            nu = apply_refl(cu, 0, pos, pos + 1)
            nv = apply_refl(cv, 0, pos, pos + 1)
            assert is_weak_cover(nu, cu) and is_weak_cover(nv, cv) and comm_lo(cu, nv) == {nu}
            cu, cv = nu, nv
        assert in_wjn1(cu) and in_wjn1(cv) and is_strict_cover(cu, cv)
        # Check W_{J_0 cap J_{n-1}}-components: s_1 left descent of cu, no left descent in {1..n-2} of cv
        assert length_dn(apply_s_left(cu, 1)) < length_dn(cu)
        assert all(length_dn(apply_s_left(cv, k)) > length_dn(cv) for k in range(1, n - 1))

        # --- Lemma 7: No Internal Root s_{n-2} (Case B2) ---
        m = n - 1
        r = tuple(range(3, n - 1))
        x = (-1, -m, n, 2) + r
        y = (-1, n, -m, 2) + r
        assert is_weak_cover(x, y)
        e1 = (n, -m, -1, 2) + r
        e2 = (-n, -m, 1, 2) + r
        e3 = (-1, 2, n, -m) + r
        f1 = (-m, n, -1, 2) + r
        f2 = (m, n, 1, 2) + r
        f3 = (-1, 2, -m, n) + r
        for ei in (e1, e2, e3):
            assert is_strict_cover(x, ei)
        for fi in (f1, f2, f3):
            assert is_strict_cover(fi, y)
        assert comm_up(e1, e2) == set() and comm_up(e1, e3) == set() and comm_up(e2, e3) == set()
        b1 = (-m, -1, n, 2) + r
        b2 = (m, 1, n, 2) + r
        b3 = (-1, -m, 2, n) + r
        assert is_weak_cover(b1, x) and is_weak_cover(b1, f1) and comm_up(x, f1) == {e1, y}
        assert is_weak_cover(b2, x) and is_weak_cover(b2, f2) and comm_up(x, f2) == {e2, y}
        assert is_weak_cover(b3, x) and is_weak_cover(b3, f3) and comm_up(x, f3) == {e3, y}
        c12 = (1, n, m, 2) + r
        c13 = (-m, 2, -1, n) + r
        c23 = (m, 2, 1, n) + r
        assert comm_lo(f1, f2) == {c12} and in_wj0(c12) and in_wj0(f2) and is_strict_cover(c12, f2)
        assert comm_lo(f1, f3) == {c13} and in_wj1(c13) and in_wj1(f1) and is_strict_cover(c13, f1)
        assert comm_lo(f2, f3) == {c23} and is_strict_cover(c23, f3)
        cu, cv = c23, f3
        for pos in range(3, n - 1):
            nu = apply_refl(cu, 0, pos, pos + 1)
            nv = apply_refl(cv, 0, pos, pos + 1)
            assert is_weak_cover(nu, cu) and is_weak_cover(nv, cv) and comm_lo(cu, nv) == {nu}
            cu, cv = nu, nv
        assert in_wjn1(cu) and in_wjn1(cv) and is_strict_cover(cu, cv)
        # Check K = {s_0..s_{n-3}} left descents: s_1 is left descent of cu, NONE in K for cv
        assert length_dn(apply_s_left(cu, 1)) < length_dn(cu)
        assert all(length_dn(apply_s_left(cv, k)) > length_dn(cv) for k in range(n - 2))

        # --- Lemma 8: Case (G2) Splitting ---
        q2m = (-1, -n) + tuple(range(2, n))
        q3m = (-1, 2, -n) + tuple(range(3, n))
        y1 = (n, 2, 1) + tuple(range(3, n))
        s0u = (1, n) + tuple(range(2, n))
        s0v = (2, n, 1) + tuple(range(3, n))
        s1u = (-n, -1) + tuple(range(2, n))
        s1v = (-n, -2, 1) + tuple(range(3, n))
        z1 = (-2, -n, 1) + tuple(range(3, n))
        assert in_wj0(s0u) and in_wj0(s0v) and is_strict_cover(s0u, s0v)
        assert is_weak_cover(s0u, s1u) and comm_up(s0v, s1u) == {s1v}
        assert is_weak_cover(s1u, q2m) and comm_up(s1v, q2m) == {z1}
        assert is_weak_cover(y1, z1) and is_weak_cover(q2m, q3m) and is_strict_cover(y1, q3m)
        assert comm_lo(z1, q3m) == {q2m, y1}

        for k in range(4, n + 1):
            mk = k - 1
            rest = tuple(range(2, mk)) + tuple(range(mk + 1, n))
            bu0, bv0 = (1, n, mk) + rest, (mk, n, 1) + rest
            bu1, bv1 = (-n, -1, mk) + rest, (-n, -mk, 1) + rest
            u2k, a2k = (-1, -n, mk) + rest, (-mk, -n, 1) + rest
            assert in_wj0(bu0) and in_wj0(bv0) and is_strict_cover(bu0, bv0)
            assert is_weak_cover(bu0, bu1) and comm_up(bv0, bu1) == {bv1}
            assert is_weak_cover(bu1, u2k) and comm_up(bv1, u2k) == {a2k}
            for j in range(2, mk):
                pj = (-1,) + tuple(range(2, j))
                sj = tuple(range(j + 1, mk)) + tuple(range(mk + 1, n))
                uj = pj + (-n, mk, j) + sj
                aj = (-mk, -n, 1, 2) + sj if j == 2 else pj[:-1] + (mk, -n, j - 1, j) + sj
                vj = pj + (j, mk, -n) + sj
                assert is_strict_cover(uj, aj) and is_strict_cover(uj, vj)
                assert comm_up(aj, vj) == set()
                if j < mk - 1:
                    wj = pj + (-n, j, mk) + sj
                    uj1 = pj + (j, -n, mk) + sj
                    aj1 = pj + (mk, -n, j) + sj
                    assert is_weak_cover(wj, uj) and is_weak_cover(wj, uj1)
                    assert comm_up(uj, uj1) == {vj, aj1}
                else:
                    qkm = (-1,) + tuple(range(2, k)) + (-n,) + tuple(range(k, n))
                    assert vj == qkm

        # --- Lemma 10: Case (G1) Splitting ---
        # Part 1: 2 <= a <= n - 2 (explicit Phase 1 + Phase 2 chains for y_A and explicit chains for y_B)
        for a in range(2, n - 1):
            if a % 2 == 0:
                q = tuple(range(a + 1, n + 1)) + tuple(-x for x in range(a, 0, -1))
                qp = tuple(range(a + 1, n)) + (-a, n) + tuple(-x for x in range(a - 1, 0, -1))
                qmid = tuple(range(a + 1, n)) + tuple(-x for x in range(a, 0, -1)) + (n,)
                cA = tuple(range(a + 1, n - 1)) + (-a, n - 1, n) + tuple(-x for x in range(a - 1, 0, -1))
                yA = apply_s_right(cA, n - a)
                cB = tuple(range(a + 1, n)) + (-a, -(a - 1), n) + tuple(-x for x in range(a - 2, 0, -1))
                yB = apply_s_right(cB, n - a)
            else:
                q = (-(a + 1),) + tuple(range(a + 2, n + 1)) + tuple(-x for x in range(a, 0, -1))
                qp = (-(a + 1),) + tuple(range(a + 2, n)) + (-a, n) + tuple(-x for x in range(a - 1, 0, -1))
                qmid = (-(a + 1),) + tuple(range(a + 2, n)) + tuple(-x for x in range(a, 0, -1)) + (n,)
                if a == n - 2:
                    cA = (n - 2, n - 1, n) + tuple(-x for x in range(n - 3, 0, -1))
                    yA = apply_s_right(cA, 2)
                else:
                    cA = (-(a + 1),) + tuple(range(a + 2, n - 1)) + (-a, n - 1, n) + tuple(-x for x in range(a - 1, 0, -1))
                    yA = apply_s_right(cA, n - a)
                cB = (-(a + 1),) + tuple(range(a + 2, n)) + (-a, -(a - 1), n) + tuple(-x for x in range(a - 2, 0, -1))
                yB = apply_s_right(cB, n - a)

            # Verify y_A diamond: comm_up(qp, yA) == {q, s_{n-1} qp}
            sn1_qp = apply_s_left(qp, n - 1)
            assert is_weak_cover(cA, qp) and is_weak_cover(cA, yA) and is_weak_cover(yA, sn1_qp)
            assert comm_up(qp, yA) == {q, sn1_qp}
            # Explicit Phase 1 (u0_A -> qmid inside ^{J_0 cap J_{n-1}} D_{n-1} keeping -1 at pos n-2 and +n at pos n-1):
            cur = (-2,) + tuple(range(3, n)) + (-1, n)
            assert in_wj1(cur) and in_q0(cur) and is_strict_cover(cur, apply_s_left(cur, n - 1))
            # Move greedily toward qmid's minus-set inside {1..n-1} keeping -1 at pos n-1 and +n at pos n:
            target_A = {i + 1 for i, val in enumerate(qmid) if val < 0}
            while cur != qmid:
                cur_A = {i + 1 for i, val in enumerate(cur) if val < 0}
                assert (n - 1) in cur_A and n not in cur_A
                assert is_strict_cover(cur, apply_s_left(cur, n - 1))
                # Either add {1, 2} via s_0 if needed, or shift a minus right!
                moved = False
                if len(cur_A) < len(target_A) and (1 not in cur_A) and (2 not in cur_A):
                    nxt = apply_s_right(cur, 0)
                    assert is_weak_cover(cur, nxt) and in_q0(nxt)
                    cur = nxt
                    moved = True
                else:
                    # Find rightmost element of cur_A (except n-1) that can shift right and is strictly left of its target slot
                    # Simple sorted matching: shift rightmost movable minus whose current pos < target pos
                    s_cur = sorted(cur_A)
                    s_tgt = sorted(target_A)
                    # Shift right to make room for s_0 if len(cur_A) < len(target_A), else match suffix of target_A
                    offset = len(s_tgt) - len(s_cur)
                    for idx_m in range(len(s_cur) - 2, -1, -1):
                        p = s_cur[idx_m]
                        goal_p = s_tgt[idx_m + offset]
                        if p < goal_p and (p + 1) not in cur_A:
                            nxt = apply_s_right(cur, p)
                            assert is_weak_cover(cur, nxt) and in_q0(nxt)
                            cur = nxt
                            moved = True
                            break
                assert moved, f"Phase 1 stuck at n={n}, a={a}, cur={cur}, qmid={qmid}"
            # Phase 2: slide +n left from pos n-1 (0-based) to pos n-a:
            for pos in range(n - 1, n - a, -1):
                assert is_strict_cover(cur, apply_s_left(cur, n - 1))
                nxt = apply_s_right(cur, pos)
                assert is_weak_cover(cur, nxt) and in_q0(nxt)
                cur = nxt
            assert cur == qp

            # Verify y_B diamond: comm_up(qp, yB) == {q, s_{a-1} qp}
            sa1_qp = apply_s_left(qp, a - 1)
            assert is_weak_cover(cB, qp) and is_weak_cover(cB, yB) and is_weak_cover(yB, sa1_qp)
            assert comm_up(qp, yB) == {q, sa1_qp}
            # Explicit chain for y_B:
            if a == 2:
                cur = (-2, 3, -1) + tuple(range(4, n + 1))
                assert in_wjn1(cur) and in_q0(cur)
                for p in range(3, n):  # slide -1 right past 4..n
                    assert is_strict_cover(cur, apply_s_left(cur, 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                for p in range(1, n - 2):  # slide -2 right past 3..n-1
                    assert is_strict_cover(cur, apply_s_left(cur, 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                assert cur == qp
            elif a % 2 == 1:
                cur = tuple(range(a, n)) + tuple(-x for x in range(a - 1, 0, -1)) + (n,)
                assert in_wjn1(cur) and in_q0(cur)
                for p in range(n - 1, n - a, -1):  # slide +n left past -1..-(a-1)
                    assert is_strict_cover(cur, apply_s_left(cur, a - 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                assert is_strict_cover(cur, apply_s_left(cur, a - 1))
                cur = apply_s_right(cur, 0)  # s_0: (a, a+1) -> (-(a+1), -a)
                assert in_q0(cur)
                for p in range(2, n - a):  # slide -a right past a+2..n-1
                    assert is_strict_cover(cur, apply_s_left(cur, a - 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                assert cur == qp
            else:
                cur = (-a,) + tuple(range(a + 1, n)) + tuple(-x for x in range(a - 1, 0, -1)) + (n,)
                assert in_wjn1(cur) and in_q0(cur)
                for p in range(n - 1, n - a, -1):  # slide +n left past -1..-(a-1)
                    assert is_strict_cover(cur, apply_s_left(cur, a - 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                for p in range(1, n - a):  # slide -a right past a+1..n-1
                    assert is_strict_cover(cur, apply_s_left(cur, a - 1))
                    cur = apply_s_right(cur, p)
                    assert in_q0(cur)
                assert cur == qp

        # Part 2: Top element a = n - 1
        if n % 2 == 1:
            q_top = (n,) + tuple(-x for x in range(n - 1, 0, -1))
            u = (n - 1, n - 2) + tuple(-x for x in range(n - 3, 0, -1)) + (n,)
            v = (n - 3, n - 2, -(n - 1)) + tuple(-x for x in range(n - 4, 0, -1)) + (n,)
            assert in_wjn1(u) and in_wjn1(v) and is_strict_cover(u, v)
            # Check parabolic factorization u = s_{n-2} q*, v = s_{n-2} s_{n-3} q*
            qstar = (n - 2, n - 1) + tuple(-x for x in range(n - 3, 0, -1)) + (n,)
            assert in_q0(qstar) and apply_s_left(qstar, n - 2) == u
            assert apply_s_left(apply_s_left(qstar, n - 3), n - 2) == v
            for pos in range(n - 1, 2, -1):
                nu = apply_s_right(u, pos)
                nv = apply_s_right(v, pos)
                assert is_weak_cover(u, nu) and is_weak_cover(v, nv) and comm_up(v, nu) == {nv}
                u, v = nu, nv
            y_top = apply_s_right(u, 0)
            z_top = apply_s_right(v, 0)
            assert is_weak_cover(u, y_top) and is_weak_cover(v, z_top) and comm_up(v, y_top) == {z_top}
            assert is_strict_cover(y_top, q_top) and comm_up(z_top, q_top) == set()
        else:
            q_top = tuple(-x for x in range(n, 0, -1))
            u = (-(n - 1),) + tuple(range(2, n - 1)) + (-1, n)
            v = (-(n - 1),) + tuple(range(2, n - 2)) + (n, -1, n - 2)
            assert in_wj1(u) and in_wj1(v) and is_strict_cover(u, v)
            # Verify tau factorization: tau(u) = x * qtilde, tau(v) = (x s_{n-1}) * qtilde
            tu, tv = tau_aut(u), tau_aut(v)
            qtilde = tuple(range(2, n)) + (1, n)
            x_par = (1, n - 1) + tuple(range(2, n - 1)) + (n,)
            xp_par = apply_s_right(x_par, n - 1)
            assert is_weak_cover(x_par, xp_par)
            assert perm_mul(x_par, qtilde) == tu and perm_mul(xp_par, qtilde) == tv
            # Explicit D_{n-3} rearrangement on positions 0..n-4 (disjoint from last 3 positions!):
            # Flip pairs (2,3), (4,5), ..., (n-4, n-3) via adjacent swaps + s_0, then sort to (-(n-1), -(n-3), ..., -2):
            for pair_lo in range(2, n - 3, 2):
                # Move pair_lo and pair_lo+1 to positions 0, 1:
                for val in (pair_lo, pair_lo + 1):
                    target_pos = 0 if val == pair_lo else 1
                    p = u.index(val)
                    while p > target_pos:
                        nu = apply_s_right(u, p)
                        nv = apply_s_right(v, p)
                        assert length_dn(nu) - length_dn(u) == length_dn(nv) - length_dn(v)
                        if length_dn(nu) > length_dn(u):
                            assert comm_up(v, nu) == {nv}
                        else:
                            assert comm_lo(u, nv) == {nu}
                        u, v = nu, nv
                        p -= 1
                # Apply s_0 at pos (0, 1) to negate both:
                nu, nv = apply_s_right(u, 0), apply_s_right(v, 0)
                assert is_weak_cover(u, nu) and is_weak_cover(v, nv) and comm_up(v, nu) == {nv}
                u, v = nu, nv
            # Bubble-sort first n-3 entries into (-(n-1), -(n-3), -(n-4), ..., -2):
            target_pref = (-(n - 1),) + tuple(-x for x in range(n - 3, 1, -1))
            for idx_t, val in enumerate(target_pref):
                p = u.index(val)
                while p > idx_t:
                    nu, nv = apply_s_right(u, p), apply_s_right(v, p)
                    assert length_dn(nu) - length_dn(u) == length_dn(nv) - length_dn(v)
                    if length_dn(nu) > length_dn(u):
                        assert comm_up(v, nu) == {nv}
                    else:
                        assert comm_lo(u, nv) == {nu}
                    u, v = nu, nv
                    p -= 1
            assert u == target_pref + (n - 2, -1, n)
            # Slide n-2 (resp n) left past -2, ..., -(n-3), -(n-1):
            for pos in range(n - 3, 0, -1):
                nu, nv = apply_s_right(u, pos), apply_s_right(v, pos)
                assert is_weak_cover(u, nu) and is_weak_cover(v, nv) and comm_up(v, nu) == {nv}
                u, v = nu, nv
            # Slide n (resp n-2) left past -1, ..., -(n-3):
            for pos in range(n - 1, 2, -1):
                nu, nv = apply_s_right(u, pos), apply_s_right(v, pos)
                assert is_weak_cover(u, nu) and is_weak_cover(v, nv) and comm_up(v, nu) == {nv}
                u, v = nu, nv
            assert is_strict_cover(u, q_top) and comm_up(v, q_top) == set()

    print("[OK] Check 4: Lemmas 6, 7, 8, and 10 (all explicit chains & rhombuses) verified 100% for n = 4..10.")


# ---- Check 5: End-to-end exact check of D_4 (15 minuscule middle orders & Theorem 3) ----

def check_5_d4_end_to_end():
    """Verify all 15 minuscule middle orders on D_4 satisfy Theorem 3 and all pr:rhombus conditions."""
    n = 4
    elems = [
        tuple(s * x for s, x in zip(signs, p))
        for p in itertools.permutations(range(1, n + 1))
        for signs in itertools.product((-1, 1), repeat=n)
        if signs.count(-1) % 2 == 0
    ]
    id_w = (1, 2, 3, 4)
    w0_all = (-1, -2, -3, -4)
    adj_cox = {0: {2}, 1: {2}, 2: {0, 1, 3}, 3: {2}}

    def is_min_in(J, s):
        # Connected component of s in J
        comp = {s}
        st = [s]
        while st:
            u = st.pop()
            for v in adj_cox[u]:
                if v in J and v not in comp:
                    comp.add(v)
                    st.append(v)
        degs = {u: sum(1 for v in adj_cox[u] if v in comp) for u in comp}
        if max(degs.values()) <= 2:
            return True
        return degs[s] == 1

    def enum_min_seqs(J):
        if not J:
            return [()]
        out = []
        for s in sorted(J):
            if is_min_in(J, s):
                for rest in enum_min_seqs(J - {s}):
                    out.append((s,) + rest)
        return out

    memo_cov = {}

    def covers_of_seq(seq):
        if not seq:
            return frozenset()
        if seq in memo_cov:
            return memo_cov[seq]
        s = seq[0]
        K = set(seq)
        Kp = K - {s}
        # Build W_K and W_Kp
        def gen_sub(G):
            vis = {id_w}
            st = [id_w]
            while st:
                u = st.pop()
                for k in G:
                    v = apply_s_right(u, k)
                    if v not in vis:
                        vis.add(v)
                        st.append(v)
            return vis

        WK = gen_sub(K)
        WKp = gen_sub(Kp)
        Q = {w for w in WK if all(length_dn(apply_s_left(w, t)) > length_dn(w) for t in Kp)}
        assert len(WKp) * len(Q) == len(WK)
        sub_cov = covers_of_seq(seq[1:])
        edges = set()
        for q in Q:
            for x, xp in sub_cov:
                edges.add((perm_mul(x, q), perm_mul(xp, q)))
        for q in Q:
            lq = length_dn(q)
            for k in K:
                qp = apply_s_right(q, k)
                if qp in Q and length_dn(qp) == lq + 1:
                    for x in WKp:
                        edges.add((perm_mul(x, q), perm_mul(x, qp)))
        res = frozenset(edges)
        memo_cov[seq] = res
        return res

    min_orders = {covers_of_seq(seq) for seq in enum_min_seqs({0, 1, 2, 3})}
    assert len(min_orders) == 15

    # Verify each minuscule middle order satisfies pr:rhombus and Theorem 3 unique split!
    w0_par = {}
    for s_star in (0, 1, 2, 3):
        J = {0, 1, 2, 3} - {s_star}
        vis = {id_w}
        st = [id_w]
        while st:
            u = st.pop()
            for k in J:
                v = apply_s_right(u, k)
                if v not in vis:
                    vis.add(v)
                    st.append(v)
        w0J = max(vis, key=length_dn)
        w0_par[s_star] = perm_mul(w0J, w0_all)  # ^J w_0

    split_counts = {0: 0, 1: 0, 3: 0}
    for E in min_orders:
        adj_up = {w: set() for w in elems}
        adj_lo = {w: set() for w in elems}
        for u, v in E:
            adj_up[u].add(v)
            adj_lo[v].add(u)
        # Check pr:rhombus (exact unique common upper/lower cover for every pair of covers)
        for u in elems:
            ups = list(adj_up[u])
            for i in range(len(ups)):
                for j in range(i + 1, len(ups)):
                    assert len(adj_up[ups[i]] & adj_up[ups[j]]) == 1
            los = list(adj_lo[u])
            for i in range(len(los)):
                for j in range(i + 1, len(los)):
                    assert len(adj_lo[los[i]] & adj_lo[los[j]]) == 1
        # Check Theorem 3: unique s_star with s not <=_L ^J w_0 for all s in J
        def leq(a, b):
            vis = {a}
            st = [a]
            while st:
                x = st.pop()
                if x == b:
                    return True
                for y in adj_up[x]:
                    if y not in vis:
                        vis.add(y)
                        st.append(y)
            return False

        splits = [
            s_star
            for s_star in (0, 1, 2, 3)
            if all(not leq(apply_s_right(id_w, s), w0_par[s_star]) for s in ({0, 1, 2, 3} - {s_star}))
        ]
        assert len(splits) == 1 and splits[0] in (0, 1, 3)
        split_counts[splits[0]] += 1

    assert split_counts == {0: 5, 1: 5, 3: 5}
    print(f"[OK] Check 5: All 15 minuscule middle orders on D_4 verified end-to-end (splits={split_counts}).")


def main():
    try:
        check_0_zero_floats()
        check_1_lemma1()
        check_2_quotients_and_jirrs()
        check_3_lemma9_spin_prop()
        check_4_lemmas_6_to_10()
        check_5_d4_end_to_end()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()

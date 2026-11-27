"""Independent exact verifier for targets/derycke-2402.15372-conj7_1 (Conjecture 6.1).

Directly implements the primary-source Abelian sandpile CTI/ITC processes on S_{n,d}
(arXiv:2402.15372v3, Section 2) and tests all formulas and lemmas in PROOF.md
using 100% exact integer / polynomial arithmetic (zero floating point).
"""

from functools import lru_cache
import sympy as sp

# --- Pure integer bivariate polynomial arithmetic in Z[q, t] ---
PolyQT = dict[tuple[int, int], int]


def poly_add(a: PolyQT, b: PolyQT, sign: int = 1) -> PolyQT:
    res = dict(a)
    for k, v in b.items():
        nv = res.get(k, 0) + sign * v
        if nv == 0:
            res.pop(k, None)
        else:
            res[k] = nv
    return res


def poly_mul(a: PolyQT, b: PolyQT) -> PolyQT:
    res: PolyQT = {}
    for (q1, t1), v1 in a.items():
        for (q2, t2), v2 in b.items():
            key = (q1 + q2, t1 + t2)
            nv = res.get(key, 0) + v1 * v2
            if nv == 0:
                res.pop(key, None)
            else:
                res[key] = nv
    return res


def poly_q_mul_t_shift(a: PolyQT, b_q: dict[int, int], q_shift: int = 0, t_shift: int = 0) -> PolyQT:
    res: PolyQT = {}
    for (qa, ta), va in a.items():
        for qb, vb in b_q.items():
            key = (qa + qb + q_shift, ta + t_shift)
            nv = res.get(key, 0) + va * vb
            if nv == 0:
                res.pop(key, None)
            else:
                res[key] = nv
    return res


# --- Exact q-binomials in Z[q] represented as dict[int, int] ---
def qpoly_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    res: dict[int, int] = {}
    for d1, v1 in a.items():
        for d2, v2 in b.items():
            nv = res.get(d1 + d2, 0) + v1 * v2
            if nv == 0:
                res.pop(d1 + d2, None)
            else:
                res[d1 + d2] = nv
    return res


def qpoly_add(a: dict[int, int], b: dict[int, int], q_shift: int = 0) -> dict[int, int]:
    res = dict(a)
    for d, v in b.items():
        nv = res.get(d + q_shift, 0) + v
        if nv == 0:
            res.pop(d + q_shift, None)
        else:
            res[d + q_shift] = nv
    return res


@lru_cache(maxsize=None)
def qbin(n: int, k: int) -> dict[int, int]:
    if k < 0 or k > n:
        return {}
    if k == 0 or k == n:
        return {0: 1}
    return qpoly_add(qbin(n - 1, k), qbin(n - 1, k - 1), q_shift=n - k)


def qtri(m: int, k1: int, k2: int, k3: int) -> dict[int, int]:
    assert k1 + k2 + k3 == m
    if min(k1, k2, k3) < 0:
        return {}
    return qpoly_mul(qbin(m, k1), qbin(m - k1, k2))


# --- 1. Direct Abelian Sandpile CTI/ITC on S_{n,d} ---
def weakly_decreasing_tuples(length: int, max_val: int):
    if length == 0:
        yield ()
        return
    def rec(rem: int, hi: int, cur: list[int]):
        if rem == 0:
            yield tuple(cur)
            return
        for val in range(hi, -1, -1):
            cur.append(val)
            yield from rec(rem - 1, val, cur)
            cur.pop()
    yield from rec(length, max_val, [])


def is_recurrent_dhar(a: list[int], b: list[int], n: int, d: int) -> bool:
    """Dhar's burning test: topple sink (adds 1 to every v in V and w in W); must burn all n+d vertices."""
    deg_v = n + d
    deg_w = n + 1
    va = [x + 1 for x in a]
    wb = [y + 1 for y in b]
    toppled_v = [False] * n
    toppled_w = [False] * d
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not toppled_v[i] and va[i] >= deg_v:
                toppled_v[i] = True
                changed = True
                for j in range(n):
                    if j != i:
                        va[j] += 1
                for j in range(d):
                    wb[j] += 1
        for j in range(d):
            if not toppled_w[j] and wb[j] >= deg_w:
                toppled_w[j] = True
                changed = True
                for i in range(n):
                    va[i] += 1
    return all(toppled_v) and all(toppled_w)


def run_cti_or_itc(a_init: tuple[int, ...], b_init: tuple[int, ...], n: int, d: int, cti_first: bool) -> tuple[int, int]:
    """Simulate parallel CTI or ITC toppling after sink topples; return (wtopple, first_round_size)."""
    deg_v = n + d
    deg_w = n + 1
    va = [x + 1 for x in a_init]
    wb = [y + 1 for y in b_init]
    done_v = [False] * n
    done_w = [False] * d
    wtopple = 0
    rnd = 0
    first_round = 0
    while not (all(done_v) and all(done_w)):
        rnd += 1
        c1 = c2 = 0
        if cti_first:
            uv = [i for i in range(n) if not done_v[i] and va[i] >= deg_v]
            for i in uv:
                done_v[i] = True
                va[i] -= deg_v
                for j in range(n):
                    if j != i:
                        va[j] += 1
                for j in range(d):
                    wb[j] += 1
            uw = [j for j in range(d) if not done_w[j] and wb[j] >= deg_w]
            for j in uw:
                done_w[j] = True
                wb[j] -= deg_w
                for i in range(n):
                    va[i] += 1
            c1, c2 = len(uv), len(uw)
        else:
            uw = [j for j in range(d) if not done_w[j] and wb[j] >= deg_w]
            for j in uw:
                done_w[j] = True
                wb[j] -= deg_w
                for i in range(n):
                    va[i] += 1
            uv = [i for i in range(n) if not done_v[i] and va[i] >= deg_v]
            for i in uv:
                done_v[i] = True
                va[i] -= deg_v
                for j in range(n):
                    if j != i:
                        va[j] += 1
                for j in range(d):
                    wb[j] += 1
            c1, c2 = len(uw), len(uv)
        assert c1 + c2 > 0
        if rnd == 1:
            first_round = c1 + c2
        wtopple += rnd * (c1 + c2)
    return wtopple, first_round


def direct_sandpile_polys(n: int, d: int) -> tuple[dict[int, PolyQT], dict[int, PolyQT], int]:
    base_height = n * d + n * (n - 1) // 2
    cti_by_r: dict[int, PolyQT] = {}
    itc_by_r: dict[int, PolyQT] = {}
    count = 0
    for a in weakly_decreasing_tuples(n, n + d - 1):
        for b in weakly_decreasing_tuples(d, n):
            if not is_recurrent_dhar(list(a), list(b), n, d):
                continue
            count += 1
            lvl = sum(a) + sum(b) - base_height
            wt_cti, r_cti = run_cti_or_itc(a, b, n, d, True)
            wt_itc, r_itc = run_cti_or_itc(a, b, n, d, False)
            kc = (lvl, wt_cti - (n + d))
            ki = (lvl, wt_itc - (n + d))
            cti_by_r.setdefault(r_cti, {})
            cti_by_r[r_cti][kc] = cti_by_r[r_cti].get(kc, 0) + 1
            itc_by_r.setdefault(r_itc, {})
            itc_by_r[r_itc][ki] = itc_by_r[r_itc].get(ki, 0) + 1
    return cti_by_r, itc_by_r, count


# --- 2. Propositions 1.1 and 2.1 Cell Formulas ---
def gen_weak_comps(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in gen_weak_comps(total - x, length - 1):
            yield (x,) + rest


def prop_1_1_cti(n: int, d: int) -> dict[int, PolyQT]:
    by_r: dict[int, PolyQT] = {}
    for k in range(1, n + 2):
        for p in gen_weak_comps(n, k):
            if any(p[i] < 1 for i in range(1, k)):
                continue
            for q in gen_weak_comps(d, k):
                if p[0] + q[0] < 1:
                    continue
                r = p[0] + q[0]
                q_exp = sum(pi * (pi - 1) // 2 for pi in p)
                t_exp = sum(i * (p[i] + q[i]) for i in range(k))
                qpoly = qbin(r, q[0])
                for i in range(1, k):
                    qpoly = qpoly_mul(qpoly, qbin(p[i] + p[i - 1] + q[i - 1] - 1, p[i]))
                    qpoly = qpoly_mul(qpoly, qbin(p[i] + q[i] - 1, q[i]))
                term = {(q_exp + deg, t_exp): coeff for deg, coeff in qpoly.items()}
                by_r[r] = poly_add(by_r.get(r, {}), term)
    return by_r


def prop_2_1_itc(n: int, d: int) -> dict[int, PolyQT]:
    by_r: dict[int, PolyQT] = {}
    for k in range(1, n + 2):
        for a in gen_weak_comps(n, k):
            if any(a[i] < 1 for i in range(k - 1)):
                continue
            for b in gen_weak_comps(d, k):
                if a[k - 1] + b[k - 1] < 1:
                    continue
                r = a[0] + b[0]
                q_exp = sum(ai * (ai - 1) // 2 for ai in a)
                t_exp = sum(i * (a[i] + b[i]) for i in range(k))
                qpoly = {0: 1}
                for i in range(k):
                    prev_a = 1 if i == 0 else a[i - 1]
                    qpoly = qpoly_mul(qpoly, qtri(a[i] + b[i] + prev_a - 1, a[i], b[i], prev_a - 1))
                term = {(q_exp + deg, t_exp): coeff for deg, coeff in qpoly.items()}
                by_r[r] = poly_add(by_r.get(r, {}), term)
    return by_r


# --- 3. Generating Functions H_a(X, Y), G_tilde_r(X, Y), P_r, P_tilde_r ---
def verify_gf_up_to(N_max: int) -> None:
    # H_coeff[(n, d, a)] -> PolyQT in Z[q, t] for n + d <= N_max, 0 <= a <= N_max
    H: dict[tuple[int, int, int], PolyQT] = {}
    for n in range(N_max + 1):
        for d in range(N_max + 1 - n):
            H[(n, d, 0)] = {(0, 0): 1} if (n == 0 and d == 0) else {}
    for tot in range(N_max + 1):
        for n in range(tot + 1):
            d = tot - n
            for a in range(1, N_max + 1):
                if n == 0:
                    qpoly = qbin(d + a - 1, d)
                    H[(0, d, a)] = {(deg, 0): coeff for deg, coeff in qpoly.items()}
                else:
                    acc: PolyQT = {}
                    for m in range(1, n + 1):
                        q_m = m * (m - 1) // 2
                        for b in range(d + 1):
                            prev = H[(n - m, d - b, m)]
                            if not prev:
                                continue
                            tri = qtri(m + b + a - 1, m, b, a - 1)
                            acc = poly_add(acc, poly_q_mul_t_shift(prev, tri, q_shift=q_m, t_shift=(n - m) + (d - b)))
                    H[(n, d, a)] = acc

    # G_tilde[(n, d, r)] -> PolyQT for n + d <= N_max, 1 <= r <= N_max
    Gt: dict[tuple[int, int, int], PolyQT] = {}
    for tot in range(N_max + 1):
        for n in range(tot + 1):
            d = tot - n
            for r in range(1, N_max + 1):
                if tot == 0:
                    Gt[(0, 0, r)] = {(0, 0): 1}
                else:
                    acc = {}
                    for p in range(1, n + 1):
                        q_p = p * (p - 1) // 2
                        for s in range(d + 1):
                            prev = Gt[(n - p, d - s, p + s)]
                            if not prev:
                                continue
                            fac = qpoly_mul(qbin(p + r - 1, p), qbin(p + s - 1, s))
                            acc = poly_add(acc, poly_q_mul_t_shift(prev, fac, q_shift=q_p, t_shift=(n - p) + (d - s)))
                    Gt[(n, d, r)] = acc

    # Compare P_r and P_tilde_r at all (n, d) with 1 <= r <= n + d <= N_max
    for r in range(1, N_max + 1):
        for tot in range(r, N_max + 1):
            for n in range(tot + 1):
                d = tot - n
                # P_r coeff at X^n Y^d
                pr: PolyQT = {}
                for a in range(min(r, n) + 1):
                    rem_d = d - (r - a)
                    if rem_d < 0:
                        continue
                    h_part = H[(n - a, rem_d, a)]
                    if not h_part:
                        continue
                    fac = qbin(r, a)
                    pr = poly_add(pr, poly_q_mul_t_shift(h_part, fac, q_shift=a * (a - 1) // 2, t_shift=0))

                # P_tilde_r coeff at X^n Y^d
                ptr: PolyQT = {}
                for p1 in range(min(r, n) + 1):
                    rem_d = d - (r - p1)
                    if rem_d < 0:
                        continue
                    g_part = Gt[(n - p1, rem_d, r)]
                    if not g_part:
                        continue
                    fac = qbin(r, p1)
                    ptr = poly_add(ptr, poly_q_mul_t_shift(g_part, fac, q_shift=p1 * (p1 - 1) // 2, t_shift=0))

                assert pr == ptr, f"GF mismatch at r={r}, n={n}, d={d}"
                if n == 0:
                    expected = {(0, 0): 1} if d == r else {}
                    assert pr == expected
                else:
                    # Also verify t^{-r} P_r(tx, ty) = F^{ITC}_{n,d,r}:
                    # [X^n Y^d] P_r(X, Y) * t^{n + d - r} should match prop_2_1_itc
                    f_itc = prop_2_1_itc(n, d).get(r, {})
                    shifted = {(q_e, t_e + n + d - r): v for (q_e, t_e), v in pr.items()}
                    assert shifted == f_itc, f"GF vs Prop 2.1 mismatch at r={r}, n={n}, d={d}"


# --- 4. Lemmas 4.2 and 4.3 in SymPy exact polynomial rings ---
def qpoch(u, q, m: int):
    res = sp.Integer(1)
    for j in range(m):
        res *= 1 - u * q**j
    return sp.expand(res)


def sp_qbin(n: int, k: int, q):
    if k < 0 or k > n:
        return sp.Integer(0)
    res = sp.Integer(0)
    for deg, coeff in qbin(n, k).items():
        res += coeff * q**deg
    return res


def verify_lemmas_sympy() -> None:
    q, a, b, u = sp.symbols("q a b u")
    c = q**2

    # Lemma 4.2 for N = 0..5 (cleared denominator (q;q)_N (q^2;q)_N q^{2N})
    for N in range(6):
        denom = sp.expand(qpoch(q, q, N) * qpoch(c, q, N) * c**N)
        lhs = sp.expand(c**N * qpoch(a, q, N) * qpoch(b, q, N))
        rhs = sp.Integer(0)
        for j in range(N + 1):
            term = sp.cancel(denom / (qpoch(q, q, N - j) * qpoch(q, q, j) * qpoch(c, q, j) * c**j))
            term *= qpoch(a * b / c, q, N - j)
            for i in range(j):
                term *= (a - c * q**i) * (b - c * q**i)
            rhs += term
        assert sp.cancel(lhs - rhs) == 0, f"Lemma 4.2 failed at N={N}"

    # Lemma 4.3 for 1 <= r, r' <= 7
    for r in range(1, 8):
        for rp in range(1, 8):
            K_u = sum(
                q ** (p * (p - 1) // 2) * sp_qbin(p + r - 1, p, q) * sp_qbin(rp - 1, p - 1, q) * u**p
                for p in range(1, rp + 1)
            )
            lhs = sp.expand(qpoch(-u, q, r) * K_u)
            rhs_sum = sum(
                q ** (ai * (ai - 1) // 2) * sp_qbin(r, ai, q) * sp_qbin(rp + ai - 1, rp, q) * u**ai
                for ai in range(1, r + 1)
            )
            rhs = sp.expand(qpoch(-u, q, rp) * rhs_sum)
            assert sp.expand(lhs - rhs) == 0, f"Lemma 4.3 failed at r={r}, r'={rp}"

    # Telescoping q-binomial identity in Theorem 4.4 (PROOF.md L196)
    for rp in range(1, 8):
        for m in range(1, rp + 1):
            k = rp - m
            for ai in range(1, 8):
                lhs = sp.expand(sp_qbin(rp + ai - 1, rp, q) * sp_qbin(rp, m, q))
                rhs = sp.expand(sp_qbin(m + ai - 1, m, q) * sp_qbin(m + ai + k - 1, k, q))
                assert lhs == rhs


def main() -> None:
    # 1. Direct sandpile vs Propositions 1.1 & 2.1 for n + d <= 6 (exact CTI == ITC)
    total_configs = 0
    for tot in range(1, 7):
        for n in range(1, tot + 1):
            d = tot - n
            cti_d, itc_d, cnt = direct_sandpile_polys(n, d)
            total_configs += cnt
            cti_p = prop_1_1_cti(n, d)
            itc_p = prop_2_1_itc(n, d)
            assert cti_d == cti_p, f"Direct CTI != Prop 1.1 at (n,d)=({n},{d})"
            assert itc_d == itc_p, f"Direct ITC != Prop 2.1 at (n,d)=({n},{d})"
            assert cti_d == itc_d, f"Refined CTI != ITC at (n,d)=({n},{d})"

    # Check primary-source Example (S_{2,2}, qtss1.tex L1025-1028)
    s22_cti_by_r = prop_1_1_cti(2, 2)
    s22_total: PolyQT = {}
    for p in s22_cti_by_r.values():
        s22_total = poly_add(s22_total, p)
    expected_s22 = {
        (5, 0): 1, (0, 5): 1, (4, 1): 1, (1, 4): 1, (3, 2): 1, (2, 3): 1,
        (4, 0): 1, (0, 4): 1, (3, 1): 2, (1, 3): 2, (2, 2): 2, (3, 0): 2, (0, 3): 2,
        (2, 1): 3, (1, 2): 3, (2, 0): 1, (0, 2): 1, (1, 1): 2, (1, 0): 1, (0, 1): 1,
    }
    assert s22_total == expected_s22, "Mismatch with qtss1.tex S_{2,2} example"

    # 2. Propositions 1.1 == 2.1 for n + d <= 9
    for tot in range(7, 10):
        for n in range(1, tot + 1):
            d = tot - n
            assert prop_1_1_cti(n, d) == prop_2_1_itc(n, d), f"Prop 1.1 != Prop 2.1 at ({n},{d})"

    # 3. Generating-function equality P_r^{(N)} == P_tilde_r^{(N)} for N <= 7
    verify_gf_up_to(7)

    # 4. Lemmas 4.2, 4.3, and Theorem 4.4 telescoping q-binomial identity
    verify_lemmas_sympy()

    print("PASS")
    print(f"Verified direct sandpile CTI=ITC ({total_configs} recurrent configs, n+d<=6 + S_{{2,2}} example), Prop 1.1=2.1 (n+d<=9), GF N<=7, Lemma 4.2 (N<=5), Lemma 4.3 (r,r'<=7).")


if __name__ == "__main__":
    main()

"""Exact pure-integer verifier for PROOF.md of Hardt-Wallach Conjecture 7.5 (arXiv:2412.06976v2)."""
import itertools
from collections import defaultdict


def poly_add(a, b, sign=1):
    res = dict(a)
    for k, v in b.items():
        nv = res.get(k, 0) + sign * v
        if nv == 0:
            res.pop(k, None)
        else:
            res[k] = nv
    return res


def partial_i(poly, i):
    """Exact divided difference operator partial_i on polynomial dict."""
    res = defaultdict(int)
    for m, c in poly.items():
        a, b = m[i], m[i + 1]
        if a == b:
            continue
        ml = list(m)
        if a > b:
            for t in range(a - b):
                ml[i] = a - 1 - t
                ml[i + 1] = b + t
                res[tuple(ml)] += c
        else:
            for t in range(b - a):
                ml[i] = b - 1 - t
                ml[i + 1] = a + t
                res[tuple(ml)] -= c
    return {k: v for k, v in res.items() if v != 0}


def pi_i(poly, i):
    """Exact isobaric Demazure operator pi_i(f) = partial_i(x_i * f)."""
    xf = {}
    for m, c in poly.items():
        ml = list(m)
        ml[i] += 1
        xf[tuple(ml)] = c
    return partial_i(xf, i)


_key_memo = {}


def key_poly(alpha, width=None):
    """Compute Demazure character kappa_alpha as exact monomial dict."""
    if width is None:
        width = len(alpha)
    a_pad = tuple(list(alpha) + [0] * (width - len(alpha)))
    if a_pad in _key_memo:
        return _key_memo[a_pad]
    lam = sorted(a_pad, reverse=True)
    cur = list(lam)
    word = []
    for i in range(len(a_pad)):
        if cur[i] != a_pad[i]:
            j = i + 1
            while cur[j] != a_pad[i]:
                j += 1
            for k in range(j - 1, i - 1, -1):
                cur[k], cur[k + 1] = cur[k + 1], cur[k]
                word.append(k)
    poly = {tuple(lam): 1}
    for k in word:
        poly = pi_i(poly, k)
    _key_memo[a_pad] = poly
    return poly


def perm_from_code(code):
    N = len(code)
    avail = list(range(N + sum(code) + 2))
    w = []
    for c in code:
        w.append(avail.pop(c))
    w.extend(avail)
    while w and w[-1] == len(w) - 1:
        w.pop()
    return tuple(w)


_schub_memo = {}


def schub_poly(w, width):
    """Exact Schubert polynomial S_w(x) via Lascoux-Schutzenberger transition."""
    p = list(w)
    while p and p[-1] == len(p) - 1:
        p.pop()
    tp = tuple(p)
    if not tp:
        return {(0,) * width: 1}
    if (tp, width) in _schub_memo:
        return _schub_memo[(tp, width)]
    r = max(i for i in range(len(tp) - 1) if tp[i] > tp[i + 1])
    s = max(i for i in range(r + 1, len(tp)) if tp[i] < tp[r])
    up = list(tp)
    up[r], up[s] = up[s], up[r]
    res = {}
    for m, c in schub_poly(up, width).items():
        ml = list(m)
        ml[r] += 1
        res[tuple(ml)] = res.get(tuple(ml), 0) + c
    for a in range(r):
        if up[a] < up[r] and all(not (up[a] < up[k] < up[r]) for k in range(a + 1, r)):
            t = list(up)
            t[a], t[r] = t[r], t[a]
            res = poly_add(res, schub_poly(t, width), 1)
    _schub_memo[(tp, width)] = res
    return res


def expand_in_schub(poly, width):
    """Exact Schubert basis expansion using reverse-lex-leading monomial x^{code(w)}."""
    cur = dict(poly)
    coeffs = {}
    while cur:
        lead_m = max(cur.keys(), key=lambda m: m[::-1])
        c = cur[lead_m]
        code = list(lead_m)
        while code and code[-1] == 0:
            code.pop()
        w = perm_from_code(code)
        coeffs[w] = coeffs.get(w, 0) + c
        sw = schub_poly(w, width)
        cur = poly_add(cur, sw, -c)
    return {k: v for k, v in coeffs.items() if v != 0}


def xi_of_schub_exp(coeffs):
    """Compute xi(sum c_w S_w) = sum c_w sum_{s_k w < w} S_{s_k w}."""
    res = {}
    for w, c in coeffs.items():
        pos = {val: idx for idx, val in enumerate(w)}
        for k in range(len(w) - 1):
            if pos[k + 1] < pos[k]:
                nw = list(w)
                nw[pos[k]], nw[pos[k + 1]] = nw[pos[k + 1]], nw[pos[k]]
                while nw and nw[-1] == len(nw) - 1:
                    nw.pop()
                t = tuple(nw)
                res[t] = res.get(t, 0) + c
    return {k: v for k, v in res.items() if v != 0}


def eta_set(alpha):
    seen = {0}
    res = []
    for i, a in enumerate(alpha):
        if a not in seen:
            seen.add(a)
            res.append(i)
    return res


def gen_parts(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for x in range(min(n, max_part), 0, -1):
        for rest in gen_parts(n - x, x):
            yield (x,) + rest


def gen_comps(total, parts):
    if parts == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in gen_comps(total - x, parts - 1):
            yield (x,) + rest


def main():
    # 1. Verify Lemma 1 (xi partial_i = partial_i xi) on ALL w in S_5 and all i in 1..4
    for p in itertools.permutations(range(5)):
        while p and p[-1] == len(p) - 1:
            p = p[:-1]
        for i in range(4):
            # partial_i(xi(S_p))
            xi_p = xi_of_schub_exp({p: 1})
            lhs = {}
            for u, c in xi_p.items():
                uu = list(u) + list(range(len(u), 5))
                if uu[i] > uu[i + 1]:
                    uu[i], uu[i + 1] = uu[i + 1], uu[i]
                    while uu and uu[-1] == len(uu) - 1:
                        uu.pop()
                    t = tuple(uu)
                    lhs[t] = lhs.get(t, 0) + c
            lhs = {k: v for k, v in lhs.items() if v != 0}
            # xi(partial_i(S_p))
            pp = list(p) + list(range(len(p), 5))
            if pp[i] > pp[i + 1]:
                pp[i], pp[i + 1] = pp[i + 1], pp[i]
                while pp and pp[-1] == len(pp) - 1:
                    pp.pop()
                rhs = xi_of_schub_exp({tuple(pp): 1})
            else:
                rhs = {}
            assert lhs == rhs, f"Lemma 1 commutation failed at p={p}, i={i}"
    print("Lemma 1 PASS (xi*partial_i = partial_i*xi on all S_5)")

    # 2. Verify Lemma 3 (dominant w(lam), S_{w(lam)} = x^lam, left descents <-> eta(lam),
    #    and S_{s_k w(lam)} = kappa_{lam - delta_i}) for ALL partitions |lam| <= 8.
    for d in range(1, 9):
        for lam in gen_parts(d):
            w = perm_from_code(lam)
            width = len(lam) + 1
            # 132-avoiding check
            for a, b, c in itertools.combinations(range(len(w)), 3):
                assert not (w[a] < w[c] < w[b]), f"Not 132-avoiding: lam={lam}, w={w}"
            # S_{w(lam)} == x^lam
            sw = schub_poly(w, width)
            expected_mon = tuple(list(lam) + [0])
            assert sw == {expected_mon: 1}, f"S_w != x^lam at lam={lam}"
            # left descents bijection and term-by-term key identity
            pos = {v: idx for idx, v in enumerate(w)}
            left_descs = {k + 1 for k in range(len(w) - 1) if pos[k + 1] < pos[k]}
            eta_vals = {lam[i] for i in eta_set(lam)}
            assert left_descs == eta_vals, f"Descents mismatch at lam={lam}"
            for i in eta_set(lam):
                k = lam[i] - 1
                nw = list(w)
                nw[pos[k]], nw[pos[k + 1]] = nw[pos[k + 1]], nw[pos[k]]
                sp = schub_poly(nw, width)
                al = list(lam) + [0]
                al[i] -= 1
                kp = key_poly(tuple(al))
                assert sp == kp, f"Term identity failed at lam={lam}, i={i}"
    print("Lemma 3 PASS (all partitions up to size 8)")

    # 3. Direct end-to-end check of Conjecture 7.5 on ALL compositions of size <= 6 (width 4)
    #    plus shifted compositions (sh=2 up to size 5) and size 7-8 multi-part samples.
    for d in range(1, 7):
        for alpha in gen_comps(d, 4):
            shifts = (0, 2) if d <= 5 else (0,)
            for sh in shifts:
                a_sh = (0,) * sh + alpha
                w_len = len(a_sh)
                kp = key_poly(a_sh, width=w_len)
                lhs = xi_of_schub_exp(expand_in_schub(kp, w_len))
                rhs_poly = {}
                for i in eta_set(a_sh):
                    al2 = list(a_sh)
                    al2[i] -= 1
                    rhs_poly = poly_add(rhs_poly, key_poly(tuple(al2), width=w_len), 1)
                rhs = expand_in_schub(rhs_poly, w_len)
                assert lhs == rhs, f"Conj 7.5 failed at alpha={a_sh}"

    # Additional size 7 and size 8 diverse multi-part compositions (including repeated & zero entries)
    extra_alphas = [
        (3, 1, 2, 1),
        (1, 3, 1, 2),
        (0, 2, 1, 2, 2),
        (2, 0, 3, 0, 2),
        (1, 2, 3, 1, 0),
        (2, 2, 1, 2, 1),
        (0, 1, 3, 1, 2, 1),
    ]
    for alpha in extra_alphas:
        w_len = len(alpha)
        kp = key_poly(alpha, width=w_len)
        lhs = xi_of_schub_exp(expand_in_schub(kp, w_len))
        rhs_poly = {}
        for i in eta_set(alpha):
            al2 = list(alpha)
            al2[i] -= 1
            rhs_poly = poly_add(rhs_poly, key_poly(tuple(al2), width=w_len), 1)
        rhs = expand_in_schub(rhs_poly, w_len)
        assert lhs == rhs, f"Conj 7.5 failed at extra alpha={alpha}"

    print("Conjecture 7.5 end-to-end check PASS")
    print("PASS")


if __name__ == "__main__":
    main()

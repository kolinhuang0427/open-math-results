"""Exact zero-float verification of the winning strategy in G_{n, M} for arXiv:2611.32205v1 Q3.5(1)."""
import math
import random
from itertools import product


def poly_add(p, q):
    n = max(len(p), len(q))
    pp = list(p) + [0] * (n - len(p))
    qq = list(q) + [0] * (n - len(q))
    res = [pp[i] + qq[i] for i in range(n)]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return tuple(res)


def poly_sub(p, q):
    return poly_add(p, tuple(-x for x in q))


def poly_scale(c, p):
    if c == 0:
        return (0,)
    res = [c * x for x in p]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return tuple(res)


def poly_mul(p, q):
    res = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            res[i + j] += a * b
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return tuple(res)


def poly_pow(p, exp):
    assert exp >= 0
    res = (1,)
    base = p
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul(res, base)
        e >>= 1
        if e > 0:
            base = poly_mul(base, base)
    return res


def poly_cmp(p, q):
    d = poly_sub(p, q)
    if d == (0,):
        return 0
    return 1 if d[-1] > 0 else -1


def poly_is_std_bound(p, bound):
    return len(p) == 1 and abs(p[0]) <= bound


class ExpStrategy:
    """Exact implementation of Exp-er's winning strategy over Z[omega]_{>=0} (a Z-DOSR)."""

    def __init__(self, n, M):
        self.n = n
        self.M = M
        self.B = [0] * (n + 1)
        self.B[n] = M
        for k in range(n - 1, 0, -1):
            self.B[k] = 2 * (self.B[k + 1] ** 2) + self.B[k + 1]

        self.N = [0] * (n + 1)
        self.N[n] = M
        for k in range(n - 1, 0, -1):
            self.N[k] = 2 * self.B[k + 1] * self.N[k + 1] + self.B[k]

        self.F = [1] * (n + 2)
        for k in range(n, 0, -1):
            self.F[k] = 2 * (math.factorial(self.B[k]) ** 2) * self.F[k + 1]

        self.Mod = [1] * (n + 1)
        self.Mod[n] = math.factorial(self.B[n])
        for k in range(n - 1, 0, -1):
            self.Mod[k] = math.factorial(self.B[k + 1]) * self.Mod[k + 1]
        self.Mod0 = math.factorial(self.B[1]) * self.Mod[1]

        self.E = [0] * (n + 1)
        self.E0 = [0] * (n + 1)
        self.E[1] = self.F[1]
        self.E0[1] = self.Mod0 + self.N[1]
        for k in range(2, n + 1):
            self.E[k] = self.B[k] * k * self.E[k - 1] + self.F[k]
            self.E0[k] = ((3 * self.B[1]) ** k) * self.N[1] + self.B[k] + self.B[k] * k * self.E0[k - 1] + self.Mod0
        self.K = n * M * max(self.E[n], self.E0[n]) + M + 10

        self.a = []
        self.U = []
        self.V = []
        self.S = []
        self.e = []

    def T(self, r_idx, k):
        mult = (4 * self.B[1]) ** k
        return poly_add(poly_scale(mult, self.S[r_idx]), ((4 * self.B[1]) ** (k + 1) * self.N[1],))

    def step(self, a_k):
        k = len(self.a) + 1
        assert poly_cmp(a_k, (0,)) >= 0
        self.a.append(a_k)
        Bk = self.B[k]
        Nk = self.N[k]

        sum_a = (0,)
        for ai in self.a:
            sum_a = poly_add(sum_a, ai)
        curr_S = poly_add(poly_scale(Bk, sum_a), (Bk + 1,))

        need_new = False
        if len(self.V) == 0:
            if poly_cmp(curr_S, (Nk + 1,)) > 0:
                need_new = True
        else:
            if poly_cmp(poly_sub(curr_S, (1,)), self.T(len(self.V) - 1, k)) > 0:
                need_new = True

        if need_new:
            self.S.append(curr_S)
            U_new = poly_add(
                poly_scale((4 * self.B[1]) ** (self.n + 1), curr_S),
                ((4 * self.B[1]) ** (self.n + 2) * self.N[1] + 1,),
            )
            self.U.append(U_new)
            self.V.append(U_new)
            for row in self.e:
                row.append(0)

        s = len(self.V)
        e_k = [0] * (s + 1)

        tuples = []
        ranges = [range(-Bk, Bk + 1)] * (k + 1)
        for tup in product(*ranges):
            if tup[k] == 0:
                continue
            L_val = (tup[0],)
            for i in range(k):
                L_val = poly_add(L_val, poly_scale(tup[i + 1], self.a[i]))
            if poly_cmp(L_val, (0,)) < 0:
                continue
            tuples.append((tup, L_val))

        pinned_tup = None
        pinned_val = None
        for tup, L_val in tuples:
            if poly_is_std_bound(L_val, Nk):
                pinned_tup = tup
                pinned_val = L_val[0]
                break

        if pinned_tup is not None:
            ck = pinned_tup[k]
            for r in range(s, 0, -1):
                rhs = -sum(pinned_tup[i + 1] * self.e[i][r] for i in range(k - 1))
                assert rhs % ck == 0
                e_k[r] = rhs // ck
            rhs0 = pinned_val - pinned_tup[0] - sum(pinned_tup[i + 1] * self.e[i][0] for i in range(k - 1))
            assert rhs0 % ck == 0
            e_k[0] = rhs0 // ck
            self.e.append(e_k)
            return e_k

        active = tuples[:]
        pin_0_from_r1 = None
        for r in range(s, 0, -1):
            Tr_prev = (Nk,) if r == 1 else self.T(r - 2, k)
            lb_strict = None
            lb_weak = None
            ub_strict = None
            ub_weak = None

            for tup, L_val in active:
                ck = tup[k]
                is_strict = poly_cmp(L_val, Tr_prev) > 0
                num = -sum(tup[i + 1] * self.e[i][r] for i in range(k - 1))
                if ck > 0:
                    val = (num, ck, tup, L_val)
                    if is_strict:
                        if lb_strict is None or val[0] * lb_strict[1] > lb_strict[0] * val[1]:
                            lb_strict = val
                    else:
                        if lb_weak is None or val[0] * lb_weak[1] > lb_weak[0] * val[1]:
                            lb_weak = val
                else:
                    mk = -ck
                    val = (-num, mk, tup, L_val)
                    if is_strict:
                        if ub_strict is None or val[0] * ub_strict[1] < ub_strict[0] * val[1]:
                            ub_strict = val
                    else:
                        if ub_weak is None or val[0] * ub_weak[1] < ub_weak[0] * val[1]:
                            ub_weak = val

            step_F = self.F[k + 1]
            lb, lb_is_str = None, False
            if lb_strict is not None and lb_weak is not None:
                if lb_strict[0] * lb_weak[1] >= lb_weak[0] * lb_strict[1]:
                    lb, lb_is_str = lb_strict, True
                else:
                    lb, lb_is_str = lb_weak, False
            elif lb_strict is not None:
                lb, lb_is_str = lb_strict, True
            elif lb_weak is not None:
                lb, lb_is_str = lb_weak, False

            ub, ub_is_str = None, False
            if ub_strict is not None and ub_weak is not None:
                if ub_strict[0] * ub_weak[1] <= ub_weak[0] * ub_strict[1]:
                    ub, ub_is_str = ub_strict, True
                else:
                    ub, ub_is_str = ub_weak, False
            elif ub_strict is not None:
                ub, ub_is_str = ub_strict, True
            elif ub_weak is not None:
                ub, ub_is_str = ub_weak, False

            if lb is not None and ub is not None:
                diff = ub[0] * lb[1] - lb[0] * ub[1]
                assert diff >= 0
                if diff == 0:
                    if lb_is_str or ub_is_str:
                        assert r == 1
                        pin_0_from_r1 = (lb[2], lb[3])
                    assert lb[0] % (lb[1] * step_F) == 0
                    x = lb[0] // lb[1]
                else:
                    assert lb[0] % (lb[1] * step_F) == 0 and ub[0] % (ub[1] * step_F) == 0
                    L_int = lb[0] // lb[1]
                    U_int = ub[0] // ub[1]
                    if U_int - L_int >= 2 * step_F:
                        x = L_int + step_F
                    elif not lb_is_str:
                        x = L_int
                    elif not ub_is_str:
                        x = U_int
                    else:
                        raise AssertionError("Gap too small")
            elif lb is not None:
                assert lb[0] % (lb[1] * step_F) == 0
                L_int = lb[0] // lb[1]
                x = L_int + step_F if lb_is_str else L_int
            elif ub is not None:
                assert ub[0] % (ub[1] * step_F) == 0
                U_int = ub[0] // ub[1]
                x = U_int - step_F if ub_is_str else U_int
            else:
                x = step_F

            e_k[r] = x
            active = [
                (tup, L_val)
                for tup, L_val in active
                if tup[k] * x + sum(tup[i + 1] * self.e[i][r] for i in range(k - 1)) == 0
            ]

        if pin_0_from_r1 is not None:
            ptup, pval = pin_0_from_r1
            assert len(pval) == 1
            ck = ptup[k]
            rhs0 = pval[0] - ptup[0] - sum(ptup[i + 1] * self.e[i][0] for i in range(k - 1))
            assert rhs0 % ck == 0
            e_k[0] = rhs0 // ck
        else:
            e_k[0] = a_k[0] % self.Mod[k]

        self.e.append(e_k)
        self.verify_invariant_round(k)
        return e_k

    def verify_invariant_round(self, k):
        s = len(self.V)
        Bk = self.B[k]
        Nk = self.N[k]
        for i in range(k):
            for r in range(1, s + 1):
                assert abs(self.e[i][r]) <= self.E[k]
                assert self.e[i][r] % self.F[k + 1] == 0
            assert abs(self.e[i][0]) <= self.E0[k]
            assert (self.e[i][0] - self.a[i][0]) % self.Mod[k] == 0
        sum_a = (0,)
        for ai in self.a:
            sum_a = poly_add(sum_a, ai)
        cap_lhs = poly_add(poly_scale(Bk, sum_a), (Bk,))
        if s >= 1:
            assert poly_cmp(cap_lhs, self.T(s - 1, k)) <= 0
        else:
            assert poly_cmp(cap_lhs, (Nk,)) <= 0
        for tup in product(range(-Bk, Bk + 1), repeat=k + 1):
            L_val = (tup[0],)
            for i in range(k):
                L_val = poly_add(L_val, poly_scale(tup[i + 1], self.a[i]))
            v = [sum(tup[i + 1] * self.e[i][j] for i in range(k)) for j in range(s + 1)]
            v[0] += tup[0]
            if poly_is_std_bound(L_val, Nk):
                assert all(x == 0 for x in v[1:])
                assert v[0] == L_val[0]
            elif poly_cmp(L_val, (Nk,)) > 0:
                top_r = 0
                for r in range(s, 0, -1):
                    if v[r] != 0:
                        top_r = r
                        break
                if top_r == 0:
                    assert len(L_val) == 1 and 0 < L_val[0] <= ((3 * self.B[1]) ** k) * self.N[1]
                    assert v[0] == L_val[0]
                else:
                    assert v[top_r] >= 1
                    assert poly_cmp(L_val, self.T(top_r - 1, k)) <= 0

    def verify_game_exact(self, check_concrete=False):
        s = len(self.V)
        for i in range(self.n):
            for r in range(1, s + 1):
                assert abs(self.e[i][r]) <= self.E[self.n]
            assert abs(self.e[i][0]) <= self.E0[self.n]

        # Build concrete V_1, ..., V_s in Z[omega]_{>0} when requested (using exact small K_eff when exponents fit)
        concrete_V = None
        if check_concrete:
            max_neg = 0
            for tup in product(range(-self.M, self.M + 1), repeat=self.n + 1):
                v = [sum(tup[i + 1] * self.e[i][j] for i in range(self.n)) for j in range(s + 1)]
                v[0] += tup[0]
                for x in v:
                    if -x > max_neg:
                        max_neg = -x
            K_eff = max_neg + 1
            assert K_eff <= self.K
            concrete_V = []
            for r in range(s):
                P = (2 ** K_eff,)
                for j in range(r):
                    P = poly_mul(P, poly_pow(concrete_V[j], K_eff))
                concrete_V.append(poly_mul(self.U[r], P))

        for tup in product(range(-self.M, self.M + 1), repeat=self.n + 1):
            L_val = (tup[0],)
            for i in range(self.n):
                L_val = poly_add(L_val, poly_scale(tup[i + 1], self.a[i]))
            cmp0 = poly_cmp(L_val, (0,))
            if cmp0 < 0:
                continue
            v = [sum(tup[i + 1] * self.e[i][j] for i in range(self.n)) for j in range(s + 1)]
            v[0] += tup[0]
            if cmp0 == 0:
                assert all(x == 0 for x in v)
            else:
                top_r = 0
                for r in range(s, 0, -1):
                    if v[r] != 0:
                        top_r = r
                        break
                if top_r == 0:
                    assert len(L_val) == 1 and L_val[0] > 0
                    assert v[0] == L_val[0]
                    assert 2 ** v[0] > L_val[0]
                else:
                    assert v[top_r] >= 1
                    assert poly_cmp(self.U[top_r - 1], L_val) > 0
                    if concrete_V is not None:
                        # Compute exact quotient z = 2^{v[0]} * prod V_r^{v[r]} in Z[omega]
                        z = poly_pow(concrete_V[top_r - 1], v[top_r] - 1)
                        z = poly_mul(z, self.U[top_r - 1])
                        P_num = (2 ** (K_eff + v[0]),)
                        for j in range(top_r - 1):
                            P_num = poly_mul(P_num, poly_pow(concrete_V[j], K_eff + v[j + 1]))
                        z = poly_mul(z, P_num)
                        assert poly_cmp(z, L_val) > 0


def run():
    # 0. Explicit n=1 base-case edge cases (including a1 = 2M) and (2,1)/(3,1) audit edge cases
    for n, M, moves in [
        (1, 1, [(1,)]),
        (1, 1, [(2,)]),
        (1, 2, [(1,)]),
        (1, 2, [(4,)]),
        (2, 1, [(8,), (4,)]),
    ]:
        st = ExpStrategy(n, M)
        for ak in moves:
            st.step(ak)
        st.verify_game_exact(check_concrete=True)

    # 1. Explicit edge cases for n=3, M=1 (including r=1 collision and r>=2 weak-weak equality)
    edge_cases_3_1 = [
        [(0, 1), (8, 1), (4, 1)],
        [(0, 1, 0), (8, 1, 1), (4, 1, 1)],
        [(37,), (2,), (13,)],
        [(21,), (5,), (1,)],
        [(51,), (52,), (103,)],
        [(52,), (5,), (47,)],
        [(50,), (51,), (1,)],
        [(4,), (2,), (1,)],
        [(0, 1), (0, 0, 1), (0, 0, 0, 1)],
        [(0, 0, 0, 1), (0, 0, 1), (0, 1)],
        [(0, 1), (0, 100), (0, 99)],
        [(0, 6), (0, 3), (0, 2)],
        [(1, 6), (2, 3), (3, 1)],
        [(0, 2), (5, 1), (5, 3)],
        [(0, 0, 1), (0, 10, 1), (0, 20, 0)],
        [(0, 0, 1), (1, 0, 0), (1, 0, 1)],
    ]
    for moves in edge_cases_3_1:
        st = ExpStrategy(3, 1)
        for ak in moves:
            st.step(ak)
        st.verify_game_exact(check_concrete=False)

    # Concrete Z[omega] product check for n=2, M=1 (where B_1=3 gives small K_eff)
    edge_cases_2_1 = [
        [(0, 1), (0, 0, 1)],
        [(0, 0, 1), (0, 1)],
        [(5,), (2,)],
        [(10,), (3,)],
        [(0, 2), (0, 1)],
        [(1, 2), (0, 1)],
    ]
    for moves in edge_cases_2_1:
        st = ExpStrategy(2, 1)
        for ak in moves:
            st.step(ak)
        st.verify_game_exact(check_concrete=True)

    # 2. Deterministic PRNG stress tests across (n, M)
    rng = random.Random(261132205)
    for n, M, trials, concrete in [(2, 1, 25, True), (2, 2, 25, False), (2, 3, 15, False), (3, 1, 40, False)]:
        for _ in range(trials):
            st = ExpStrategy(n, M)
            moves = []
            for k in range(n):
                kind = rng.randint(0, 5)
                if k == 0 or kind == 0:
                    deg = rng.choice([0, 1, 2])
                    p = [rng.randint(0, 60) if deg == 0 else rng.randint(0, 10) for _ in range(deg + 1)]
                    if deg > 0:
                        p[-1] = rng.randint(1, 5)
                    ak = tuple(p)
                elif kind == 1:
                    ak = (rng.randint(-5, 10),)
                    for prev in moves:
                        ak = poly_add(ak, poly_scale(rng.randint(-2, 2), prev))
                    if poly_cmp(ak, (0,)) < 0:
                        ak = poly_scale(-1, ak)
                elif kind == 2:
                    prev = rng.choice(moves)
                    d = rng.choice([2, 3])
                    ak = tuple(x // d for x in prev)
                    if ak == (0,):
                        ak = (1,)
                elif kind == 3:
                    ak = (rng.randint(0, 60),)
                elif kind == 4:
                    prev = rng.choice(moves)
                    ak = poly_add(prev, (rng.randint(0, 10), rng.randint(0, 2)))
                else:
                    prev = rng.choice(moves)
                    ak = poly_mul(prev, (0, 0, 1))
                moves.append(ak)
                st.step(ak)
            st.verify_game_exact(check_concrete=concrete)

    print("Exact G_{n,M} strategy verified across 4 n=1 edge cases, 7 concrete Z[omega] (2,1) edge cases, 16 (3,1) edge cases, and 105 adversarial trials.")
    print("PASS")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Independent zero-float exact-arithmetic verifier for targets/kovalyov-2611.32205-q1/."""

from __future__ import annotations

from fractions import Fraction
import itertools
import math
import re


def check_primary_source_and_numbering() -> None:
    import os
    if not os.path.exists("tools/.arxiv_cache/eprint/2611.32205/main.tex"):
        print("[SKIP] local tools/.arxiv_cache not present; skipping TeX numbering check")
        return
    tex = open("tools/.arxiv_cache/eprint/2611.32205/main.tex", "r", encoding="utf-8").read()
    lines = tex.splitlines()
    sec = 0
    cnt = 0
    q_num = None
    pat = re.compile(
        r"\\begin\{(theorem|lemma|proposition|corollary|definition|question)\}"
        r"(?:\[[^\]]*\])?(?:\\label(?:\[[^\]]*\])?\{([^}]+)\})?"
    )
    for line in lines:
        if r"\section{" in line:
            sec += 1
            cnt = 0
        m = pat.search(line)
        if m:
            cnt += 1
            if m.group(1) == "question":
                q_num = f"{sec}.{cnt}"

    assert q_num == "3.5", f"Expected Question 3.5 in main.tex, got {q_num}"
    assert r"\item Is  $\IOpen + (\Exp)$ conservative over $\IOpen$?" in tex
    assert r"\item More generally, what is the $\mathcal L_{OSR}$-fragment of $\IOpen + (\Exp)$?" in tex

    target_md = open("targets/kovalyov-2611.32205-q1/TARGET.md", "r", encoding="utf-8").read()
    proof_md = open("targets/kovalyov-2611.32205-q1/PROOF.md", "r", encoding="utf-8").read()
    assert "arXiv:2611.32205v1" in target_md
    assert "Is  $\\IOpen + (\\Exp)$ conservative over $\\IOpen$?" in target_md
    assert "Question 3.5(1)" in target_md
    assert "Question 3.5(1)" in proof_md and "Question 3.5(2)" in proof_md
    assert "(3 B_1)^k N_1" in proof_md

    print("[PASS] Primary source arXiv:2611.32205v1 verbatim statement, definitions, and Question 3.5 numbering verified.")


def check_step1_and_strategy() -> None:
    """Test PROOF.md Section 2 parameters, patched Step 1 split (s_old>=1 vs s_old=0), and Inductive Invariant I_k."""
    def neg(a):
        return tuple(-x for x in a)

    def add(a, b):
        return tuple(x + y for x, y in zip(a, b))

    def mul_int(c, a):
        return tuple(c * x for x in a)

    def cmp0(a):
        for x in reversed(a):
            if x != 0:
                return 1 if x > 0 else -1
        return 0

    def cmp(a, b):
        return cmp0(add(a, neg(b)))

    def is_std(a):
        return all(x == 0 for x in a[1:])

    def run_game(n: int, M: int, plays: list[tuple[int, ...]]) -> None:
        B = {n: M}
        for k in range(n, 1, -1):
            B[k - 1] = 2 * B[k] ** 2 + B[k]
        N = {n: M}
        for k in range(n, 1, -1):
            N[k - 1] = 2 * B[k] * N[k] + B[k - 1]
        F = {n + 1: 1}
        for k in range(n, 0, -1):
            F[k] = 2 * (math.factorial(B[k]) ** 2) * F[k + 1]
        mu = {n: math.factorial(B[n])}
        for k in range(n, 0, -1):
            mu[k - 1] = math.factorial(B[k]) * mu[k]
        E = {1: F[1]}
        for k in range(2, n + 1):
            E[k] = B[k] * k * E[k - 1] + F[k]
        E0 = {1: mu[0] + N[1]}
        for k in range(2, n + 1):
            E0[k] = (3 * B[1]) ** k * N[1] + B[k] + B[k] * k * E0[k - 1] + mu[0]
        K = n * M * max(E[n], E0[n]) + M + 10

        dim = len(plays[0])

        def std(c: int) -> tuple[int, ...]:
            return (c,) + (0,) * (dim - 1)

        def make_T(Sr, j: int):
            return add(mul_int((4 * B[1]) ** j, Sr), std((4 * B[1]) ** (j + 1) * N[1]))

        s = 0
        T_thresh = {}
        e_vec: list[list[int]] = []
        a_list: list[tuple[int, ...]] = []

        for k in range(1, n + 1):
            ak = plays[k - 1]
            a_list.append(ak)
            sum_a = std(0)
            for a in a_list:
                sum_a = add(sum_a, a)
            S_curr = add(mul_int(B[k], sum_a), std(B[k] + 1))
            cap_lhs = add(mul_int(B[k], sum_a), std(B[k]))
            s_old = s
            created = False
            if (s == 0 and cmp(cap_lhs, std(N[k])) > 0) or (s >= 1 and cmp(cap_lhs, T_thresh[(s, k)]) > 0):
                s += 1
                created = True
                for j in range(1, n + 1):
                    T_thresh[(s, j)] = make_T(S_curr, j)
                for ev in e_vec:
                    ev.append(0)
                if s_old >= 1:
                    rhs87 = add(mul_int(B[k], add(sum_a, neg(ak))), std(B[k] + N[k]))
                    assert cmp(ak, rhs87) > 0

            Tk = []
            for cs in itertools.product(range(-B[k], B[k] + 1), repeat=k + 1):
                if cs[k] == 0:
                    continue
                L = std(cs[0])
                for i in range(k):
                    L = add(L, mul_int(cs[i + 1], a_list[i]))
                if cmp0(L) >= 0:
                    Tk.append((cs, L))

            pinned = next(((cs, L) for (cs, L) in Tk if cmp(L, std(N[k])) <= 0), None)
            ek = [0] * (s + 1)
            if pinned is not None:
                cs1, L1 = pinned
                d1 = L1[0]
                for r in range(1, s + 1):
                    num = -sum(cs1[i + 1] * e_vec[i][r] for i in range(k - 1))
                    assert num % cs1[k] == 0
                    ek[r] = num // cs1[k]
                num0 = d1 - cs1[0] - sum(cs1[i + 1] * e_vec[i][0] for i in range(k - 1))
                assert num0 % cs1[k] == 0
                ek[0] = num0 // cs1[k]
            else:
                if created:
                    assert all(cs[k] > 0 for (cs, _) in Tk)
                Ar = list(Tk)
                collision_tuple = None
                step = F[k + 1]
                for r in range(s, 0, -1):
                    prev_T = std(N[k]) if r == 1 else T_thresh[(r - 1, k)]
                    weak_lbs = []
                    strict_lbs = []
                    weak_ubs = []
                    strict_ubs = []
                    for cs, L in Ar:
                        rhs_sum = sum(cs[i + 1] * e_vec[i][r] for i in range(k - 1))
                        strict = cmp(L, prev_T) > 0
                        if cs[k] > 0:
                            alpha = Fraction(-rhs_sum, cs[k])
                            assert alpha.denominator == 1 and int(alpha) % step == 0
                            (strict_lbs if strict else weak_lbs).append((int(alpha), cs, L))
                        else:
                            m_k = -cs[k]
                            beta = Fraction(rhs_sum, m_k)
                            assert beta.denominator == 1 and int(beta) % step == 0
                            (strict_ubs if strict else weak_ubs).append((int(beta), cs, L))

                    if r == 1:
                        # At r = 1 in Step 3, every bound in A_1 has L(a) > N_k (strict!)
                        assert not weak_lbs and not weak_ubs
                        max_alpha = max((x[0] for x in strict_lbs), default=None)
                        min_beta = min((x[0] for x in strict_ubs), default=None)
                        if max_alpha is not None and min_beta is not None and max_alpha == min_beta:
                            ek[r] = max_alpha
                            collision_tuple = max(strict_lbs, key=lambda x: x[0])
                        else:
                            lo = (max_alpha + step) if max_alpha is not None else None
                            hi = (min_beta - step) if min_beta is not None else None
                            if lo is not None and hi is not None:
                                assert lo <= hi
                                ek[r] = lo
                            elif lo is not None:
                                ek[r] = lo
                            elif hi is not None:
                                ek[r] = hi
                            else:
                                ek[r] = 0
                    else:
                        lo_cands = [x[0] for x in weak_lbs] + [x[0] + step for x in strict_lbs]
                        hi_cands = [x[0] for x in weak_ubs] + [x[0] - step for x in strict_ubs]
                        lo = max(lo_cands) if lo_cands else None
                        hi = min(hi_cands) if hi_cands else None
                        if lo is not None and hi is not None:
                            assert lo <= hi, f"Empty I_r at k={k}, r={r}: [{lo}, {hi}]"
                            ek[r] = lo
                        elif lo is not None:
                            ek[r] = lo
                        elif hi is not None:
                            ek[r] = hi
                        else:
                            ek[r] = 0
                    assert abs(ek[r]) <= E[k] and ek[r] % step == 0
                    Ar = [(cs, L) for (cs, L) in Ar if sum(cs[i + 1] * e_vec[i][r] for i in range(k - 1)) + cs[k] * ek[r] == 0]
                if collision_tuple is not None:
                    _, cs_dag, L_dag = collision_tuple
                    assert is_std(L_dag)
                    d_dag = L_dag[0]
                    num0 = d_dag - cs_dag[0] - sum(cs_dag[i + 1] * e_vec[i][0] for i in range(k - 1))
                    assert num0 % cs_dag[k] == 0
                    ek[0] = num0 // cs_dag[k]
                else:
                    ek[0] = ak[0] % mu[k]

            e_vec.append(ek)
            # Check I_k invariants: ALL tuples in [-B_k, B_k]^{k+1} (including c_k == 0 and negative L!)
            for i in range(k):
                assert abs(e_vec[i][0]) <= E0[k]
                assert (e_vec[i][0] - a_list[i][0]) % mu[k] == 0
                for r in range(1, s + 1):
                    assert abs(e_vec[i][r]) <= E[k]
                    assert e_vec[i][r] % F[k + 1] == 0
            # Check I_k(3) Upper cap
            if s >= 1:
                assert cmp(cap_lhs, T_thresh[(s, k)]) <= 0
            else:
                assert cmp(cap_lhs, std(N[k])) <= 0

            for cs in itertools.product(range(-B[k], B[k] + 1), repeat=k + 1):
                L = std(cs[0])
                for i in range(k):
                    L = add(L, mul_int(cs[i + 1], a_list[i]))
                sgn = cmp0(L)
                if sgn < 0:
                    continue  # covered by negation -L
                v0 = cs[0] + sum(cs[i + 1] * e_vec[i][0] for i in range(k))
                vr = [sum(cs[i + 1] * e_vec[i][r] for i in range(k)) for r in range(1, s + 1)]
                assert all(abs(v) < K for v in vr) and abs(v0) < K
                if cmp(L, std(N[k])) <= 0:
                    assert all(v == 0 for v in vr) and is_std(L) and v0 == L[0]
                else:
                    if all(v == 0 for v in vr):
                        assert is_std(L) and 0 < L[0] <= (3 * B[1]) ** k * N[1] and v0 == L[0]
                    else:
                        r_max = max(idx + 1 for idx, v in enumerate(vr) if v != 0)
                        assert vr[r_max - 1] >= 1 and cmp(L, T_thresh[(r_max, k)]) <= 0

    # Run diverse standard and nonstandard Challenger plays (w_1 << w_2 << ...)
    run_game(1, 1, [(1,)])
    run_game(1, 1, [(2,)])                         # n=1, a1=2M bound test (AUDIT.md Defect 1)
    run_game(1, 2, [(1,)])
    run_game(1, 2, [(4,)])                         # n=1, M=2, a1=2M bound test (AUDIT.md Defect 1)
    run_game(2, 1, [(0, 0), (1, 0)])
    run_game(2, 1, [(0, 1), (0, 2)])
    run_game(2, 1, [(2, 1), (4, 2)])
    run_game(2, 1, [(0, 1), (5, 2)])
    run_game(2, 1, [(0, 1, 0), (0, 0, 1)])
    run_game(2, 2, [(1, 1, 0), (3, 2, 0)])
    run_game(3, 1, [(1, 0, 0), (0, 0, 0), (0, 1, 0)])
    run_game(3, 1, [(0, 1, 0), (3, 2, 0), (-1, 1, 1)])
    run_game(3, 1, [(0, 1), (8, 1), (4, 1)])       # r=1 exact collision play (AUDIT.md Defect 5.2)
    run_game(3, 1, [(0, 1, 0), (8, 1, 1), (4, 1, 1)])  # r>=2 weak-weak equality play (AUDIT.md Defect 2)

    print("[PASS] Winning strategy I_k (incl. c_k=0, I_k(3), n=1 a1=2M, r=1 collision, r>=2 weak-weak equality) verified across 14 Z-DOSR plays.")


def main() -> None:
    check_primary_source_and_numbering()
    check_step1_and_strategy()
    print("PASS")


if __name__ == "__main__":
    main()

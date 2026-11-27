"""Independent exact-integer verifier for targets/ulfarsson-2603.16004-conj1 (Conjecture 2.9).

Directly implements PAP, 1-point inflations, Lemma 0, Lemma 2 constructions,
Claim 3A/3B, Theorem 3 (Self-Inflation Dichotomy), and exact SG / reverse-strategy
game trees using pure integer arithmetic (zero floating point).
"""

from itertools import combinations, permutations


def std(seq: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    """Standardize distinct values into 1..m."""
    ordered = sorted(seq)
    rank = {v: i + 1 for i, v in enumerate(ordered)}
    return tuple(rank[x] for x in seq)


def rev(p: tuple[int, ...]) -> tuple[int, ...]:
    return p[::-1]


def asc(p: tuple[int, ...]) -> int:
    return sum(1 for i in range(len(p) - 1) if p[i] < p[i + 1])


def des(p: tuple[int, ...]) -> int:
    return sum(1 for i in range(len(p) - 1) if p[i] > p[i + 1])


def inflate(gamma: tuple[int, ...], j: int, t: int, eps: str) -> tuple[int, ...]:
    """1-based index j in gamma; eps in {'+', '-'}."""
    v = gamma[j - 1]
    block = tuple(range(v, v + t)) if eps == "+" else tuple(range(v + t - 1, v - 1, -1))
    out: list[int] = []
    for idx, val in enumerate(gamma, start=1):
        if idx == j:
            out.extend(block)
        elif val < v:
            out.append(val)
        else:
            out.append(val + t - 1)
    return tuple(out)


def contains_pattern(perm: tuple[int, ...], pat: tuple[int, ...]) -> bool:
    """Exact backtracking pattern containment check (1-based patterns)."""
    n = len(perm)
    k = len(pat)
    if n < k:
        return False
    chosen: list[int] = []

    def dfs(start: int, pi: int) -> bool:
        if pi == k:
            return True
        need = k - pi
        for pos in range(start, n - need + 1):
            val = perm[pos]
            ok = True
            for prev_i, prev_val in enumerate(chosen):
                if (pat[prev_i] < pat[pi]) != (prev_val < val):
                    ok = False
                    break
            if ok:
                chosen.append(val)
                if dfs(pos + 1, pi + 1):
                    return True
                chosen.pop()
        return False

    return dfs(0, 0)


def shadow(perm: tuple[int, ...], k: int) -> set[tuple[int, ...]]:
    return {std([perm[i] for i in idxs]) for idxs in combinations(range(len(perm)), k)}


def verify_threshold() -> None:
    for k in range(3, 501):
        n0 = k + ((2 * k + 1) * (k - 1)) ** 2 + 1
        assert n0 == 4 * k**4 - 4 * k**3 - 3 * k**2 + 3 * k + 2
        assert n0 > (k - 1) ** 2 + 1
        assert n0 - k >= ((2 * k + 1) * (k - 1)) ** 2 + 1 > 2 * k - 2 > k
        assert n0 - k + 1 > n0 - k > k


def verify_lemma_0() -> None:
    # (1) Reversal identity & (2) Shadow stabilization
    for m in (3, 4):
        for gamma in permutations(range(1, m + 1)):
            for j in range(1, m + 1):
                for eps in ("+", "-"):
                    neg_eps = "-" if eps == "+" else "+"
                    for t in range(1, 6):
                        assert rev(inflate(gamma, j, t, eps)) == inflate(rev(gamma), m + 1 - j, t, neg_eps)
                    sh_m = shadow(inflate(gamma, j, m, eps), m)
                    assert shadow(inflate(gamma, j, m + 1, eps), m) == sh_m
                    assert shadow(inflate(gamma, j, m + 2, eps), m) == sh_m

    # (3) Contiguous monotone-block inflation from explicit grid-cell construction
    for eps in ("+", "-"):
        # Take pi in S_8 with monotone block B of size 4 inside a single grid cell of A
        for j in range(1, 5):
            pi = inflate((2, 4, 1, 3), j, 4, eps)
            block_pos = set(range(j - 1, j - 1 + 4))
            # Pick subset R intersecting B in s >= 1 points and A in >= 1 points
            for s in (1, 2, 3):
                for b_sub in combinations(sorted(block_pos), s):
                    a_pos = [idx for idx in range(len(pi)) if idx not in block_pos]
                    for a_sub in combinations(a_pos, 2):
                        R_pos = sorted(a_sub + b_sub)
                        tau = std([pi[i] for i in R_pos])
                        first_j = next(idx + 1 for idx, pos in enumerate(R_pos) if pos in block_pos)
                        for t in range(1, 4 - s + 2):
                            for Bp in combinations(sorted(block_pos), t + s - 1):
                                combined = sorted(a_sub + Bp)
                                assert std([pi[i] for i in combined]) == inflate(tau, first_j, t, eps)


def verify_theorem_3_and_claims() -> None:
    # Exhaustive check of Claim 3A, Claim 3B, Theorem 3 for k = 3, 4, 5, 6
    for k in (3, 4, 5, 6):
        id_k = tuple(range(1, k + 1))
        idr_k = id_k[::-1]
        for p in permutations(range(1, k + 1)):
            if p == id_k or p == idr_k:
                continue
            pr = rev(p)
            hit_pos = False
            hit_neg = False
            for j in range(1, k + 1):
                for eps in ("+", "-"):
                    inf = inflate(pr, j, k, eps)
                    if contains_pattern(inf, p):
                        if eps == "+":
                            hit_pos = True
                        else:
                            hit_neg = True
                        # Directly check Claim 3A on a concrete k-subset S of inf with std(S) == p
                        W_pos = set(range(j - 1, j - 1 + k))
                        found_witness = False
                        for S_pos in combinations(range(len(inf)), k):
                            if std([inf[idx] for idx in S_pos]) != p:
                                continue
                            S_W = [idx for idx in S_pos if idx in W_pos]
                            t = len(S_W)
                            if 2 <= t <= k - 1:
                                S_A = [idx for idx in S_pos if idx not in W_pos]
                                Sp = sorted(S_A + [S_W[0]])
                                q = std([inf[idx] for idx in Sp])
                                m = len(q)
                                assert 2 <= m <= k - 1
                                assert contains_pattern(pr, q)
                                if eps == "+":
                                    assert des(q) == des(p)
                                else:
                                    assert asc(q) == asc(p)
                                assert (p[0] < p[-1]) == (q[0] < q[-1])
                                found_witness = True
                                break
                        assert found_witness
            assert not (hit_pos and hit_neg), f"Theorem 3 failed for p={p}"

        # Exhaustive check of Claim 3B for k = 3, 4, 5
        if k <= 5:
            for pi in permutations(range(1, k + 1)):
                for m in range(2, k):
                    for r_idxs in combinations(range(k), m):
                        tau = std([pi[idx] for idx in r_idxs])
                        assert asc(tau) <= asc(pi)
                        assert des(tau) <= des(pi)
                        if asc(tau) == asc(pi):
                            assert pi[0] >= pi[r_idxs[0]] and pi[r_idxs[-1]] >= pi[-1]
                        if des(tau) == des(pi):
                            assert pi[0] <= pi[r_idxs[0]] and pi[r_idxs[-1]] <= pi[-1]


def verify_lemma_2_small() -> None:
    # Verify Lemma 2's witness construction for all non-monotone p in S_k, beta in S_{k+1} extending p, sign eps, k=3,4
    for k in (3, 4):
        n_test = 2 * k - 2 + k  # suffices for |B_0| >= 2k-2 and n-k >= k
        id_k = tuple(range(1, k + 1))
        idr_k = id_k[::-1]
        for p in permutations(range(1, k + 1)):
            if p == id_k or p == idr_k:
                continue
            pr = rev(p)
            # All 1-point extensions beta in S_{k+1} containing p at removal of i0
            betas_seen: set[tuple[tuple[int, ...], int]] = set()
            for beta in permutations(range(1, k + 2)):
                for i0 in range(1, k + 2):
                    if std([beta[idx] for idx in range(k + 1) if idx != i0 - 1]) == p:
                        betas_seen.add((beta, i0))
            for beta, i0 in betas_seen:
                for eps in ("+", "-"):
                    neg_eps = "-" if eps == "+" else "+"
                    # Minimal F compatible with I_k(beta, i0, eps)
                    sh_sig = shadow(inflate(beta, i0, k, eps), k)
                    if p in sh_sig:
                        continue
                    # sigma has B_0 of size n_test - k >= 2k - 2
                    # Simulate Case 1 vs Case 2 on sigma and sigma^r
                    sh_sig_r = {rev(x) for x in sh_sig}
                    if p not in sh_sig_r:
                        # Case 1: sigma^r avoids F u {p} and contains p^r
                        assert pr in sh_sig_r
                        continue
                    # Case 2: p^r in sh_sig; find R_1 in sigma = I_{n_test-k}(beta, i0, eps)
                    sigma = inflate(beta, i0, n_test - k, eps)
                    B0_pos = set(range(i0 - 1, i0 - 1 + (n_test - k)))
                    found_R1 = False
                    for R1_pos in combinations(range(len(sigma)), k):
                        if std([sigma[idx] for idx in R1_pos]) != pr:
                            continue
                        s1 = sum(1 for idx in R1_pos if idx in B0_pos)
                        assert 1 <= s1 <= k - 1
                        j1 = next(idx + 1 for idx, pos in enumerate(R1_pos) if pos in B0_pos)
                        sh_om1 = shadow(inflate(pr, j1, k, eps), k)
                        assert sh_om1 <= sh_sig
                        if p not in sh_om1:
                            found_R1 = True
                            break
                        # Subcase 2b: find j2 in I_k(p^r, j1, eps) -> P_2 -> j2, sign -eps
                        inf1 = inflate(pr, j1, k, eps)
                        W1_pos = set(range(j1 - 1, j1 - 1 + k))
                        for P2_pos in combinations(range(len(inf1)), k):
                            if std([inf1[idx] for idx in P2_pos]) == p:
                                R2_pos = [len(inf1) - 1 - pos for pos in reversed(P2_pos)]
                                W1r_pos = {len(inf1) - 1 - pos for pos in W1_pos}
                                j2 = next(idx + 1 for idx, pos in enumerate(R2_pos) if pos in W1r_pos)
                                sh_om2 = shadow(inflate(pr, j2, k, neg_eps), k)
                                assert sh_om2 <= sh_sig_r
                                assert p not in sh_om2
                                found_R1 = True
                                break
                        if found_R1:
                            break
                    assert found_R1


def verify_pap_game_k3() -> None:
    k = 3
    patterns = list(permutations(range(1, k + 1)))
    for n in (3, 4, 5, 6):
        sh_map = {pi: shadow(pi, k) for pi in permutations(range(1, n + 1))}
        memo_sg: dict[frozenset[tuple[int, ...]], int] = {}

        def sg(F: frozenset[tuple[int, ...]]) -> int:
            if F in memo_sg:
                return memo_sg[F]
            avail = {p for pi, sh in sh_map.items() if sh.isdisjoint(F) for p in sh}
            if not avail:
                memo_sg[F] = 0
                return 0
            vals = {sg(F | {p}) for p in avail}
            m = 0
            while m in vals:
                m += 1
            memo_sg[F] = m
            return m

        assert sg(frozenset()) == 0, f"sg(S_{n}, 3) != 0"

        # Verify reverse strategy wins from every reachable reverse-closed F
        memo_win: dict[frozenset[tuple[int, ...]], bool] = {}

        def p2_reverse_wins(F: frozenset[tuple[int, ...]]) -> bool:
            if F in memo_win:
                return memo_win[F]
            avail = [p for p in patterns if p not in F and any(sh.isdisjoint(F) and p in sh for sh in sh_map.values())]
            for p in avail:
                F1 = F | {p}
                pr = rev(p)
                if pr in F1 or not any(sh.isdisjoint(F1) and pr in sh for sh in sh_map.values()):
                    memo_win[F] = False
                    return False
                if not p2_reverse_wins(F1 | {pr}):
                    memo_win[F] = False
                    return False
            memo_win[F] = True
            return True

        assert p2_reverse_wins(frozenset()), f"Reverse strategy failed at n={n}, k=3"


def main() -> None:
    verify_threshold()
    verify_lemma_0()
    verify_theorem_3_and_claims()
    verify_lemma_2_small()
    verify_pap_game_k3()
    print("PASS")
    print("Verified n0(k) for k=3..500, Lemma 0(1)-(3), Lemma 2 (k=3,4), Claims 3A/3B & Thm 3 (k=3..6), and exact PAP SG/reverse strategy (k=3, n=3..6).")


if __name__ == "__main__":
    main()

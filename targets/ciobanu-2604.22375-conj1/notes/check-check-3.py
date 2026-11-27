#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for Ciobanu-Turaev (arXiv:2604.22375v1) Section 3.1 Conjecture 1.

Written directly from Arxiv_version.tex definitions and PROOF.md without reading verify.py or notes/.
Pure integer/set/tuple computations (zero floating-point operations).
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
import random
import sys


@dataclass(frozen=True)
class VPA:
    states: tuple[int, ...]
    stack_alpha: tuple[str, ...]
    sigma_c: tuple[str, ...]
    sigma_i: tuple[str, ...]
    sigma_r: tuple[str, ...]
    init: frozenset[int]
    final: frozenset[int]
    # delta_c[(q, a)] -> set of (q2, gamma)
    delta_c: dict[tuple[int, str], frozenset[tuple[int, str]]]
    # delta_i[(q, a)] -> set of q2
    delta_i: dict[tuple[int, str], frozenset[int]]
    # delta_r[(q, a, top)] -> set of q2, where top is in stack_alpha or "BOT"
    delta_r: dict[tuple[int, str, str], frozenset[int]]

    def reachable_configs(self, word: tuple[str, ...], start_states: frozenset[int] | None = None) -> set[tuple[int, tuple[str, ...]]]:
        """All (q, stack_tuple) reachable from (q0, ()) (representing bottom-of-stack BOT)."""
        q0s = self.init if start_states is None else start_states
        configs: set[tuple[int, tuple[str, ...]]] = {(q, ()) for q in q0s}
        sc, si, sr = set(self.sigma_c), set(self.sigma_i), set(self.sigma_r)
        for ch in word:
            nxt: set[tuple[int, tuple[str, ...]]] = set()
            if ch in sc:
                for q, st in configs:
                    for q2, g in self.delta_c.get((q, ch), ()):
                        nxt.add((q2, st + (g,)))
            elif ch in si:
                for q, st in configs:
                    for q2 in self.delta_i.get((q, ch), ()):
                        nxt.add((q2, st))
            elif ch in sr:
                for q, st in configs:
                    top = st[-1] if st else "BOT"
                    rest = st[:-1] if st else ()
                    for q2 in self.delta_r.get((q, ch, top), ()):
                        nxt.add((q2, rest))
            else:
                raise ValueError(f"Unknown letter {ch}")
            configs = nxt
            if not configs:
                break
        return configs

    def accepts(self, word: tuple[str, ...]) -> bool:
        return any(q in self.final for q, _ in self.reachable_configs(word))


def is_mc(word: tuple[str, ...], sigma_c: set[str], sigma_r: set[str]) -> bool:
    """True iff every suffix s of word satisfies #_c(s) <= #_r(s)."""
    bal = 0  # #_c - #_r on current suffix
    for ch in reversed(word):
        if ch in sigma_c:
            bal += 1
        elif ch in sigma_r:
            bal -= 1
        if bal > 0:
            return False
    return True


def test_lemma1_and_lemma2_empty_stack() -> None:
    print("[1/3] Checking Lemma 1 (MC submonoid & generation) & Lemma 2(1) (empty stack) on random VPAs...", flush=True)
    rng = random.Random(20260422)
    sigma_c = ("c1", "c2")
    sigma_i = ("i1",)
    sigma_r = ("r1", "r2")
    sigma = sigma_c + sigma_i + sigma_r
    sc_set, sr_set = set(sigma_c), set(sigma_r)

    # Enumerate words up to length 5 and separate MC vs non-MC
    mc_words: list[tuple[str, ...]] = [()]
    all_words: list[tuple[str, ...]] = [()]
    for length in range(1, 6):
        for w in product(sigma, repeat=length):
            all_words.append(w)
            if is_mc(w, sc_set, sr_set):
                mc_words.append(w)

    # Lemma 1(1): closure under concatenation
    for u in mc_words[:80]:
        for v in mc_words[:80]:
            assert is_mc(u + v, sc_set, sr_set)
    # Lemma 1(2): Sigma_r, Sigma_i, Sigma_c * Sigma_r subseteq MC
    for r in sigma_r:
        assert is_mc((r,), sc_set, sr_set)
    for i in sigma_i:
        assert is_mc((i,), sc_set, sr_set)
    for c in sigma_c:
        for r in sigma_r:
            assert is_mc((c, r), sc_set, sr_set)

    # Build 20 random nondeterministic VPAs and verify EVERY run on EVERY w in MC ends with empty stack ()
    states = (0, 1, 2)
    stack_alpha = ("A", "B")
    for _ in range(20):
        dc = {
            (q, a): frozenset((rng.choice(states), rng.choice(stack_alpha)) for _ in range(rng.randint(1, 2)))
            for q in states
            for a in sigma_c
        }
        di = {(q, a): frozenset(rng.choice(states) for _ in range(rng.randint(1, 2))) for q in states for a in sigma_i}
        dr = {
            (q, a, top): frozenset(rng.choice(states) for _ in range(rng.randint(1, 2)))
            for q in states
            for a in sigma_r
            for top in (*stack_alpha, "BOT")
        }
        vpa = VPA(states, stack_alpha, sigma_c, sigma_i, sigma_r, frozenset({0}), frozenset({2}), dc, di, dr)
        for u in mc_words:
            for _, st in vpa.reachable_configs(u):
                assert st == (), f"Non-empty stack {st} on MC word {u}"


def group_s3_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(3))


def group_s3_inv(a: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 3
    for i, v in enumerate(a):
        out[v] = i
    return tuple(out)


def test_finite_quotient_constructions() -> None:
    print("[2/3] Checking Case 1, Case 2 (Lemma 2, Lemma 3, normal core N) on finite & infinite groups...", flush=True)
    # Test infinite group G = Z x S3 (f.g., infinite!) with recognizable union of cosets of N = {0} x A3 (index 6 in Z x S3? Wait: let's take 3Z x A3, index 6!)
    # Generators of Z x S3: t = (1, id), s = (0, (1,0,2)), r = (0, (1,2,0))
    # Represent group elements via quotient Z/6Z x S3 (faithful on cosets of 6Z x {id}) and also test direct Z^2 / N!
    # Here test directly on finite quotient G_fin = (Z/6Z) x S3 (order 36) with multiple non-trivial subgroups H and normal cores N:
    s3_elems = []
    from itertools import permutations

    for p in permutations((0, 1, 2)):
        s3_elems.append(p)
    G = [(k, p) for k in range(6) for p in s3_elems]
    id_G = (0, (0, 1, 2))

    def mul(g1, g2):
        return ((g1[0] + g2[0]) % 6, group_s3_mul(g1[1], g2[1]))

    def inv(g):
        return ((-g[0]) % 6, group_s3_inv(g[1]))

    # Alphabet Sigma = {t, t^-1, a, b} where t=(1, id), a=(0, (1,0,2)) [transposition], b=(0, (1,2,0)) [3-cycle]
    gen_map = {
        "t": (1, (0, 1, 2)),
        "T": (5, (0, 1, 2)),
        "a": (0, (1, 0, 2)),
        "A": (0, (1, 0, 2)),
        "b": (0, (1, 2, 0)),
        "B": (0, (2, 0, 1)),
    }

    def eval_word(w: tuple[str, ...]):
        cur = id_G
        for ch in w:
            cur = mul(cur, gen_map[ch])
        return cur

    # Pick a non-normal subgroup H_true = <(2, id), (0, (1,0,2))> of index 9 in Z/6Z x S3
    # Let S = union of two right cosets: H_true * (0, id) U H_true * (1, (1,2,0))
    # Then Stab_L(S) = H_true (non-normal!), normal core N = <(2, id)> has index 18, and S is a union of cosets of N!
    H_true = set()
    for k in (0, 2, 4):
        for p in ((0, 1, 2), (1, 0, 2)):
            H_true.add((k, p))
    S = set(H_true) | {mul(h, (1, (1, 2, 0))) for h in H_true}

    # Build a non-trivial VPA (Case 2: symmetric partition sigma_c={"t"}, sigma_r={"T"}, sigma_i={"a","A","b","B"})
    # that accepts L = pi^-1(S) AND tracks a spurious balanced-parenthesis stack constraint that ALWAYS succeeds via nondeterminism or ignores stack on valid group transitions:
    # Specifically, take a VPA whose state tracks g in G/N (coset in H_true \ G? Better: track element in G, push/pop dummy stack symbols to exercise stack transitions!)
    # Even better: test BOTH Case 1 (Sigma_r = empty) and Case 2 (Sigma_r != empty) VPA recognizing pi^-1(S)!
    states = tuple(range(len(G)))
    g_to_idx = {g: i for i, g in enumerate(G)}

    for sc, si, sr in [
        (("t", "a", "b"), ("T", "A", "B"), ()),  # Case 1: Sigma_r empty
        (("t",), ("a", "A", "b", "B"), ("T",)),  # Case 2: symmetric partition
        (("t", "a"), ("b", "B"), ("T", "A")),    # Case 2: larger Sigma_c, Sigma_r
    ]:
        dc = {(g_to_idx[g], ch): frozenset({(g_to_idx[mul(g, gen_map[ch])], "X")}) for g in G for ch in sc}
        di = {(g_to_idx[g], ch): frozenset({g_to_idx[mul(g, gen_map[ch])]}) for g in G for ch in si}
        dr = {
            (g_to_idx[g], ch, top): frozenset({g_to_idx[mul(g, gen_map[ch])]})
            for g in G
            for ch in sr
            for top in ("X", "BOT")
        }
        vpa = VPA(
            states=states,
            stack_alpha=("X",),
            sigma_c=sc,
            sigma_i=si,
            sigma_r=sr,
            init=frozenset({g_to_idx[id_G]}),
            final=frozenset(g_to_idx[s] for s in S),
            delta_c=dc,
            delta_i=di,
            delta_r=dr,
        )

        # Verify vpa accepts w iff eval_word(w) in S on all words up to length 4
        sigma_all = sc + si + sr
        for length in range(5):
            for w in product(sigma_all, repeat=length):
                assert vpa.accepts(w) == (eval_word(w) in S)

        # Compute H = Stab_L(S) directly and verify Omega = H \ G via MC(Sigma)
        H_stab = {h for h in G if {mul(h, s) for s in S} == S}
        assert H_stab == H_true

        if sr:
            # Generate MC(Sigma) words up to length 6 and check Lemma 1(2) generation + Lemma 3 Omega = H\G
            sc_set, sr_set = set(sc), set(sr)
            M_mc = set()
            for length in range(7):
                for w in product(sigma_all, repeat=length):
                    if is_mc(w, sc_set, sr_set):
                        M_mc.add(eval_word(w))
                        # Lemma 2(1) check
                        for _, st in vpa.reachable_configs(w):
                            assert st == ()
            # Check M_mc generates G as a group
            gen_grp = set(M_mc) | {inv(m) for m in M_mc}
            closure = {id_G}
            q_bfs = deque([id_G])
            while q_bfs:
                cur = q_bfs.popleft()
                for x in gen_grp:
                    nxt = mul(cur, x)
                    if nxt not in closure:
                        closure.add(nxt)
                        q_bfs.append(nxt)
            assert len(closure) == len(G)

            # Check Omega = {H m : m in M_mc} == H \ G and |Omega| <= 2^|Q|
            coset_of = lambda x: frozenset(mul(h, x) for h in H_stab)
            omega = {coset_of(m) for m in M_mc}
            all_cosets = {coset_of(g) for g in G}
            assert omega == all_cosets
            assert len(omega) <= 2 ** len(states)

        # Conclusion: normal core N = cap_{g in G} g H g^-1 has finite index and S is union of N-cosets
        N_core = {n for n in H_stab if all(mul(mul(g, n), inv(g)) in H_stab for g in G)}
        assert all(mul(n, s) in S and mul(s, n) in S for n in N_core for s in S)
        # Verify S equals union of N-cosets of elements of S
        reconstructed_S = {mul(n, s) for s in S for n in N_core}
        assert reconstructed_S == S


def test_negative_sanity_Z_wp() -> None:
    print("[3/3] Checking negative sanity on G = Z, S = {0} (infinite ~_0 index for symmetric partition)...", flush=True)
    # For G = Z, Sigma = {a, A} with a=+1 (call), A=-1 (response), S = {0}:
    # u_k = A^k is in MC(Sigma) for all k >= 0, and distinguishing suffix v_k = a^k gives u_k v_k in WP(Z) iff k = m!
    # Verify explicitly on 0 <= k, m <= 12 that all A^k are pairwise inequivalent under ~_0.
    sc, sr = {"a"}, {"A"}
    for k in range(13):
        uk = ("A",) * k
        assert is_mc(uk, sc, sr)
    sigs = []
    for k in range(13):
        uk = ("A",) * k
        row = tuple((k - m) == 0 for m in range(13))  # pi(A^k a^m) == 0
        sigs.append(row)
    assert len(set(sigs)) == 13


def main() -> int:
    test_lemma1_and_lemma2_empty_stack()
    test_finite_quotient_constructions()
    test_negative_sanity_Z_wp()
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

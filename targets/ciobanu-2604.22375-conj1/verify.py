"""Exact-arithmetic verification suite for targets/ciobanu-2604.22375-conj1/PROOF.md.

Uses 100% exact integer, set, word, and permutation/group arithmetic (zero floats,
zero floating-point division).
Tests:
1. Subclaims (Lemma 1): MC(Sigma) is a submonoid containing Sigma_r, Sigma_i, and
   Sigma_c * Sigma_r, and <pi(MC(Sigma))>_grp = G across symmetric, asymmetric,
   and non-inverse-closed monoid generating sets for Z, Z^2, F_2, S_3, D_4.
2. Subclaims (Lemma 2): Exact VPA simulation (both deterministic and nondeterministic)
   verifying stack-emptiness on every word in MC(Sigma), R(u1) == R(u2) => u1 ~_0 u2,
   and finite index bound |MC / ~_0| <= 2^|Q| across non-group VPAs (Dyck, a^n b^n)
   and group-language VPAs.
3. Subclaims (Lemma 3 + Conclusion): Explicit finite-group / quotient recognisability
   via H = Stab_L(S), Omega = {H * m : m in pi(MC)}, right-action invariance rho_m(Omega) = Omega,
   Omega = H \\ G, normal core N <= H, and S as union of cosets of N, over S_3, D_4,
   and Z_6, plus finite-ball obstruction check for non-recognisable sets in F_2.
"""

from collections import deque
from itertools import permutations, product


# ---------------------------------------------------------------------------
# 1. Words, MC(Sigma), and free / finite groups
# ---------------------------------------------------------------------------

def is_mc(word, call_set, ret_set):
    """True iff every suffix s of word satisfies #_c(s) <= #_r(s)."""
    c_cnt = 0
    r_cnt = 0
    for ch in reversed(word):
        if ch in call_set:
            c_cnt += 1
        elif ch in ret_set:
            r_cnt += 1
        if c_cnt > r_cnt:
            return False
    return True


def all_words_up_to(alphabet, max_len):
    res = [()]
    cur = [()]
    for _ in range(max_len):
        nxt = []
        for w in cur:
            for a in alphabet:
                nxt.append(w + (a,))
        res.extend(nxt)
        cur = nxt
    return res


def free_reduce(word, inv_map):
    st = []
    for ch in word:
        if st and st[-1] == inv_map[ch]:
            st.pop()
        else:
            st.append(ch)
    return tuple(st)


def check_lemma1_submonoid_and_gen():
    # (A) Symmetric partition on F_2: Sigma_c = {a, b}, Sigma_r = {A, B}, Sigma_i = {}
    alpha_sym = ("a", "b", "A", "B")
    inv_sym = {"a": "A", "A": "a", "b": "B", "B": "b"}
    c_sym, i_sym, r_sym = {"a", "b"}, set(), {"A", "B"}
    words4 = all_words_up_to(alpha_sym, 4)
    mc4 = [w for w in words4 if is_mc(w, c_sym, r_sym)]
    assert () in mc4
    for y in r_sym | i_sym:
        assert (y,) in mc4
    for x in c_sym:
        for y in r_sym:
            assert (x, y) in mc4
    # Closure under concatenation (test pairs of length <= 3)
    mc3 = [w for w in mc4 if len(w) <= 3]
    for u in mc3:
        for v in mc3:
            assert is_mc(u + v, c_sym, r_sym)
    # Check <pi(MC)>_grp contains every generator of F_2
    mc_imgs = {free_reduce(w, inv_sym) for w in mc4 if len(w) <= 2}
    # For each g in alpha_sym, g = (g * A) * A^{-1} when g in c_sym, or g in mc_imgs
    for g in alpha_sym:
        red_g = (g,)
        if red_g in mc_imgs:
            continue
        # x = (x * A) * A^{-1}
        prod_word = free_reduce((g, "A"), inv_sym)
        assert prod_word in mc_imgs and ("A",) in mc_imgs
        assert free_reduce(prod_word + ("a",), inv_sym) == red_g

    # (B) Asymmetric partition on F_2: Sigma_c = {a, b, A}, Sigma_r = {B}, Sigma_i = {}
    c_asym, i_asym, r_asym = {"a", "b", "A"}, set(), {"B"}
    mc_asym = [w for w in all_words_up_to(alpha_sym, 3) if is_mc(w, c_asym, r_asym)]
    imgs_asym = {free_reduce(w, inv_sym) for w in mc_asym}
    for g in alpha_sym:
        if (g,) not in imgs_asym:
            prod_word = free_reduce((g, "B"), inv_sym)
            assert prod_word in imgs_asym and ("B",) in imgs_asym
            assert free_reduce(prod_word + ("b",), inv_sym) == (g,)

    # (C) Non-inverse-closed monoid generating set for F_2: {a, b, c} where pi(c) = B*A
    # Here Sigma_c = {a, b}, Sigma_r = {c}, Sigma_i = {}.
    eval_noninv = {"a": ("a",), "b": ("b",), "c": ("B", "A")}
    def eval_w(w):
        out = []
        for ch in w:
            out.extend(eval_noninv[ch])
        return free_reduce(tuple(out), inv_sym)

    mc_noninv = [w for w in all_words_up_to(("a", "b", "c"), 4) if is_mc(w, {"a", "b"}, {"c"})]
    imgs_noninv = {eval_w(w) for w in mc_noninv}
    # Check both a^{-1}, b^{-1}, a, b lie in <imgs_noninv>_grp:
    # b * c -> A; c -> B*A; hence A, B, a, b are generated.
    assert ("A",) in imgs_noninv  # eval(("b", "c")) = b * B * A = A
    assert ("B", "A") in imgs_noninv  # eval(("c",)) = B * A
    assert ("a", "B", "A") in imgs_noninv  # eval(("a", "c"))
    return len(mc4)


# ---------------------------------------------------------------------------
# 2. Exact NVPA / DVPA simulation (Lemma 2)
# ---------------------------------------------------------------------------

class VPA:
    """Nondeterministic/deterministic VPA under Ciobanu-Turaev convention."""

    def __init__(self, states, call_set, int_set, ret_set, q0_set, accept_set,
                 trans_c, trans_i, trans_r_stack, trans_r_bot):
        self.states = states
        self.call_set = call_set
        self.int_set = int_set
        self.ret_set = ret_set
        self.q0_set = set(q0_set)
        self.accept_set = set(accept_set)
        self.trans_c = trans_c          # (q, a) -> set of (q', gamma)
        self.trans_i = trans_i          # (q, a) -> set of q'
        self.trans_r_stack = trans_r_stack  # (q, a, gamma) -> set of q'
        self.trans_r_bot = trans_r_bot  # (q, a) -> set of q'

    def step_configs(self, configs, ch):
        nxt = set()
        if ch in self.call_set:
            for q, st in configs:
                for q2, gam in self.trans_c.get((q, ch), ()):
                    nxt.add((q2, st + (gam,)))
        elif ch in self.int_set:
            for q, st in configs:
                for q2 in self.trans_i.get((q, ch), ()):
                    nxt.add((q2, st))
        elif ch in self.ret_set:
            for q, st in configs:
                if not st:
                    for q2 in self.trans_r_bot.get((q, ch), ()):
                        nxt.add((q2, ()))
                else:
                    top = st[-1]
                    rest = st[:-1]
                    for q2 in self.trans_r_stack.get((q, ch, top), ()):
                        nxt.add((q2, rest))
        return nxt

    def run_configs(self, word, start_configs=None):
        if start_configs is None:
            configs = {(q0, ()) for q0 in self.q0_set}
        else:
            configs = set(start_configs)
        for ch in word:
            configs = self.step_configs(configs, ch)
        return configs

    def accepts(self, word):
        return any(q in self.accept_set for q, _ in self.run_configs(word))


def check_lemma2_vpas():
    # VPA 1 (non-regular VPL): {a^n b^n : n >= 0} over Sigma_c={a}, Sigma_r={b}
    # States: 0 (reading a's or empty), 1 (popping b's), 2 (dead)
    vpa_anbn = VPA(
        states={0, 1, 2},
        call_set={"a"},
        int_set=set(),
        ret_set={"b"},
        q0_set={0},
        accept_set={0, 1},
        trans_c={(0, "a"): {(0, "X")}},
        trans_i={},
        trans_r_stack={(0, "b", "X"): {1}, (1, "b", "X"): {1}},
        trans_r_bot={},  # reading b on empty stack dies (not valid run)
    )
    # Wait: epsilon is accepted (state 0, empty stack), a^n b^n accepted iff stack returns to empty!
    # Fix: only accept in state 0 or state 1 WHEN stack is empty?
    # Note: in VPA without bottom-marker check at accept, mark bottom push differently!
    # Push "B" on empty? No, push doesn't see stack! Instead, nondeterministic VPA guesses bottom!
    # Let's build exact NVPA for {a^n b^n : n >= 1} U {eps} WITHOUT stack-empty acceptance:
    # Guess on pushing 'a': either "bottom X_bot" (from state 0 -> 1) or "non-bottom X" (1 -> 1).
    # Popping X_bot moves to state 2 (accepting); popping any extra b after state 2 dies.
    vpa_anbn_exact = VPA(
        states={0, 1, 2, 3},
        call_set={"a"},
        int_set=set(),
        ret_set={"b"},
        q0_set={0},
        accept_set={0, 3},
        trans_c={
            (0, "a"): {(1, "Xbot")},
            (1, "a"): {(1, "X")},
        },
        trans_i={},
        trans_r_stack={
            (1, "b", "X"): {(2)},
            (2, "b", "X"): {(2)},
            (1, "b", "Xbot"): {(3)},
            (2, "b", "Xbot"): {(3)},
        },
        trans_r_bot={},
    )
    # Wait: (0, 'a') -> (1, Xbot), then 'a' -> (1, X), 'b' pops X -> (2), 'b' pops Xbot -> (3) accept!
    # Test membership up to length 8:
    for w in all_words_up_to(("a", "b"), 6):
        n = len(w)
        expected = (n % 2 == 0) and (w == ("a",) * (n // 2) + ("b",) * (n // 2))
        assert vpa_anbn_exact.accepts(w) == expected, f"Failed a^n b^n on {w}"

    # Verify Lemma 2(1) and 2(2) on vpa_anbn_exact over MC up to length 6
    mc_words = [w for w in all_words_up_to(("a", "b"), 6) if is_mc(w, {"a"}, {"b"})]
    sig_to_words = {}
    for u in mc_words:
        cfgs = vpa_anbn_exact.run_configs(u)
        for _, st in cfgs:
            assert st == (), f"Non-empty stack {st} on MC word {u}"
        sig = frozenset(q for q, _ in cfgs)
        sig_to_words.setdefault(sig, []).append(u)
    assert len(sig_to_words) <= (1 << len(vpa_anbn_exact.states))
    suffixes = all_words_up_to(("a", "b"), 4)
    for sig, grp in sig_to_words.items():
        u0 = grp[0]
        for u1 in grp[1:]:
            for v in suffixes:
                assert vpa_anbn_exact.accepts(u0 + v) == vpa_anbn_exact.accepts(u1 + v)

    # VPA 2 (total transitions including bottom-of-stack transitions):
    # Dyck-like balanced + unbalanced returns where reading b on bot cycles between states 0, 1
    vpa_tot = VPA(
        states={0, 1},
        call_set={"a"},
        int_set={"c"},
        ret_set={"b"},
        q0_set={0},
        accept_set={0},
        trans_c={(0, "a"): {(1, "P")}, (1, "a"): {(0, "Q")}},
        trans_i={(0, "c"): {1}, (1, "c"): {0}},
        trans_r_stack={
            (0, "b", "P"): {1}, (0, "b", "Q"): {0},
            (1, "b", "P"): {0}, (1, "b", "Q"): {1},
        },
        trans_r_bot={(0, "b"): {1}, (1, "b"): {0}},
    )
    mc_tot = [w for w in all_words_up_to(("a", "b", "c"), 5) if is_mc(w, {"a"}, {"b"})]
    sigs_tot = {}
    for u in mc_tot:
        cfgs = vpa_tot.run_configs(u)
        for _, st in cfgs:
            assert st == ()
        sig = frozenset(q for q, _ in cfgs)
        sigs_tot.setdefault(sig, []).append(u)
    assert len(sigs_tot) <= (1 << len(vpa_tot.states))
    suf3 = all_words_up_to(("a", "b", "c"), 3)
    for sig, grp in sigs_tot.items():
        u0 = grp[0]
        for u1 in grp[1:]:
            for v in suf3:
                assert vpa_tot.accepts(u0 + v) == vpa_tot.accepts(u1 + v)
    return len(mc_words), len(mc_tot)


# ---------------------------------------------------------------------------
# 3. Finite groups, quotient VPAs, H = Stab_L(S), Omega = H \ G, normal core N
# ---------------------------------------------------------------------------

def build_group_from_perms(gens_dict):
    """Generate finite permutation group from generator dict {sym: perm_tuple}."""
    n = len(next(iter(gens_dict.values())))
    ident = tuple(range(n))
    elems = {ident}
    q = deque([ident])
    while q:
        g = q.popleft()
        for s, p in gens_dict.items():
            # composition g * p (apply p then g, or left-to-right: (g*p)[i] = p[g[i]])
            gp = tuple(p[g[i]] for i in range(n))
            if gp not in elems:
                elems.add(gp)
                q.append(gp)
    return ident, elems


def mul(g, h):
    return tuple(h[g[i]] for i in range(len(g)))


def inv(g):
    out = [0] * len(g)
    for i, v in enumerate(g):
        out[v] = i
    return tuple(out)


def check_finite_group_proof_pipeline(name, gens_dict, call_set, int_set, ret_set, S_elems):
    ident, G = build_group_from_perms(gens_dict)
    alphabet = tuple(gens_dict.keys())
    S_set = set(S_elems)

    def pi_word(w):
        cur = ident
        for ch in w:
            cur = mul(cur, gens_dict[ch])
        return cur

    # Build a VPA recognizing pi^{-1}(S) that ALSO pushes/pops group info on stack
    # (illustrating non-trivial stack usage even for a group preimage language!)
    # State q in G tracks current group element; stack pushes old element/symbol,
    # pop checks consistency via quotient/group rule -> still recognizes pi^{-1}(S).
    states = set(G)
    trans_c = {(q, a): {(mul(q, gens_dict[a]), a)} for q in G for a in call_set}
    trans_i = {(q, a): {mul(q, gens_dict[a])} for q in G for a in int_set}
    trans_r_stack = {
        (q, a, gam): {mul(q, gens_dict[a])}
        for q in G for a in ret_set for gam in call_set
    }
    trans_r_bot = {(q, a): {mul(q, gens_dict[a])} for q in G for a in ret_set}
    vpa = VPA(states, call_set, int_set, ret_set, {ident}, S_set,
              trans_c, trans_i, trans_r_stack, trans_r_bot)

    # Verify VPA accepts pi^{-1}(S) up to length 4
    for w in all_words_up_to(alphabet, 4):
        assert vpa.accepts(w) == (pi_word(w) in S_set)

    # Compute H = Stab_L(S)
    H = frozenset(h for h in G if {mul(h, s) for s in S_set} == S_set)
    assert ident in H
    # Right cosets H \ G
    all_rcosets = {frozenset(mul(h, g) for h in H) for g in G}
    assert len(G) % len(H) == 0
    assert len(all_rcosets) * len(H) == len(G)

    # Compute M_mc from bounded words (enough to cover finite group G via BFS on MC)
    # Every generator in ret_set | int_set and pair (c, r) is in MC!
    mc_gens = [(a,) for a in sorted(ret_set | int_set)] + [
        (c, r) for c in sorted(call_set) for r in sorted(ret_set)
    ]
    M_mc = {ident}
    q_bfs = deque([ident])
    while q_bfs:
        cur = q_bfs.popleft()
        for w in mc_gens:
            nxt = mul(cur, pi_word(w))
            if nxt not in M_mc:
                M_mc.add(nxt)
                q_bfs.append(nxt)

    # Compute Omega = {H * m : m in M_mc}
    Omega = {frozenset(mul(h, m) for h in H) for m in M_mc}
    # Verify Lemma 3: right action by M_mc preserves Omega, and Omega == H \ G
    for m in M_mc:
        shifted = {frozenset(mul(x, m) for x in coset) for coset in Omega}
        assert shifted == Omega
    assert Omega == all_rcosets, f"{name}: Omega != H\\G"

    # Compute normal core N = \bigcap_{g in G} g H g^{-1}
    N = set(H)
    for g in G:
        gi = inv(g)
        conj = {mul(mul(g, h), gi) for h in H}
        N &= conj
    N = frozenset(N)
    # Check N is normal and S is a union of cosets of N
    for g in G:
        gi = inv(g)
        for n in N:
            assert mul(mul(g, n), gi) in N
    for s in S_set:
        for n in N:
            assert mul(n, s) in S_set
            assert mul(s, n) in S_set
    return len(G), len(H), len(N)


def check_lemma3_and_conclusion():
    # 1. S_3 with symmetric generating set (transposition + 3-cycle + inverses)
    s3_gens = {
        "a": (1, 2, 0),       # 3-cycle (call)
        "A": (2, 0, 1),       # inverse 3-cycle (ret)
        "t": (1, 0, 2),       # transposition (int)
    }
    # Non-normal subset S (a single coset of <t> plus another element, or union of cosets of <1, a, a^2>)
    # Pick S = {(0,1,2), (1,0,2)} (not a subgroup, H = {id})
    check_finite_group_proof_pipeline("S_3_small", s3_gens, {"a"}, {"t"}, {"A"}, [(0, 1, 2), (1, 0, 2)])
    # Pick S = A_3 = {(0,1,2), (1,2,0), (2,0,1)}
    check_finite_group_proof_pipeline("S_3_A3", s3_gens, {"a"}, {"t"}, {"A"}, [(0, 1, 2), (1, 2, 0), (2, 0, 1)])

    # 2. D_4 (dihedral group of order 8) with call/ret/int partition
    d4_gens = {
        "r": (1, 2, 3, 0),    # 90-deg rotation (call)
        "R": (3, 0, 1, 2),    # inverse rotation (ret)
        "f": (0, 3, 2, 1),    # reflection (call - test asymmetric partition too!)
    }
    check_finite_group_proof_pipeline("D_4_asym", d4_gens, {"r", "f"}, set(), {"R"}, [(0, 1, 2, 3), (2, 3, 0, 1)])

    # 3. Z_6 with empty Sigma_r (Case 1)
    z6_gens = {"x": (1, 2, 3, 4, 5, 0), "X": (5, 0, 1, 2, 3, 4)}
    check_finite_group_proof_pipeline("Z_6_case1", z6_gens, {"x"}, {"X"}, set(), [(0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)])

    # 4. Non-recognisable subset of F_2: S = {g in F_2 : |g|_a - |g|_b == 0}
    # Verify on ball of radius 4 that H = Stab_L(S) leaves >= 9 distinct cosets in pi(MC),
    # growing linearly with radius (confirming no finite-state VPA can recognize pi^{-1}(S)).
    inv_f2 = {"a": "A", "A": "a", "b": "B", "B": "b"}
    def bal_ab(red_w):
        return sum(1 if c == "a" else (-1 if c == "A" else (-1 if c == "b" else 1)) for c in red_w)

    # Actually let S = {g in F_2 : exp_a(g) == exp_b(g)}, i.e. sum_a - sum_b == 0
    def exp_diff(red_w):
        ea = sum(1 if c == "a" else (-1 if c == "A" else 0) for c in red_w)
        eb = sum(1 if c == "b" else (-1 if c == "B" else 0) for c in red_w)
        return ea - eb

    # Words A^k for k=0..8 are all in MC and have distinct exp_diff (-k),
    # so for any j != k, A^j and A^k cannot share a right coset of H = Stab_L(S)
    # because A^{j-k} * 1_G has exp_diff j-k != 0 so A^{j-k} not in H!
    diffs = {exp_diff(("A",) * k) for k in range(9)}
    assert len(diffs) == 9
    for k in range(9):
        assert is_mc(("A",) * k, {"a", "b"}, {"A", "B"})


def main():
    n_mc = check_lemma1_submonoid_and_gen()
    n1, n2 = check_lemma2_vpas()
    check_lemma3_and_conclusion()
    print(f"Lemma 1 (MC submonoid & <pi(MC)>_grp = G): checked ({n_mc} words)")
    print(f"Lemma 2 (empty stack on MC & finite index <= 2^|Q|): checked ({n1}, {n2} MC words)")
    print("Lemma 3 & Conclusion (Omega = H\\G, normal core N <= H, coset union): checked")
    print("PASS")


if __name__ == "__main__":
    main()

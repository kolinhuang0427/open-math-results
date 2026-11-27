# Checker Report: `targets/maric-2603.08876-conj1/` (`check-check-3`)

## Primary Source & Verbatim Statement Verification

- **Primary source checked:** `tools/.arxiv_cache/eprint/2603.08876v1/LexiCut-arXiv.tex` (`arXiv:2603.08876v1`, Nevena Marić, *Hierarchical threshold structure in Max-Cut with geometric edge weights*), Section 5 (`\label{sec:global}`), **Conjecture 5.1** (`\label{conj:global}` [Global Optimality]), plus Section 2 eq. (1) (`\label{eq:edge_index}`) and Section 4 Theorems 4.7, 4.9, 4.10.
- **Verbatim match:** Every quantifier ($n \ge 7$, $r \in (r_k(n), r_{k-1}(n))$), edge weight formula $W^n(S; r) = \sum_{1 \le a < b \le n,\, \mathbf{1}_S(a) \ne \mathbf{1}_S(b)} r^{\binom{n-a+1}{2} - (b-a)}$, $k$-isolated cut $C_k = \{1,\dots,k\} \mid \{k+1,\dots,n\}$, and root $r_k(n)$ with $r_0(n) := 2$, $r_{\lfloor n/2 \rfloor}(n) := 1$ matches `TARGET.md` and `PROOF.md` verbatim.

## Proof Audit (`PROOF.md`)

Checked `PROOF.md` (including `@attack-6`'s `#1211` patches) across all stages:
- **§§1–3 Reduction & boundary lemmas:** Rank-1 factorization $w(i, j) = A_i B_j$, Lemmas 2.1–2.2 ($\alpha_L > \alpha_U$, unique $r^* \in \{1, \dots, L-1\}$, $\mathrm{hi}_p > 0$), and Lemmas 3.1–3.3 hold cleanly, with patched L134–135 ($(1 - x^{d-1})(x S_A / A_{a+1}) - (1 - x^d)$ using $x S_A / A_{a+1} \ge x^{-(M-1)} + x^{-2M} > 2$) verified algebraically.
- **§4 Region I ($P_{b+1} > 0$, all $n \ge 7$) & $n = 7$ exact closure (Theorems 4.1–4.2):** Verified symbolic polynomial identities, $(L, d) \ne (2, 1)$ interior monotonicity note (L149), Region I subcases 4–6, and exhaustive $n = 7$ / $n = 8$ verification via exact SymPy Sturm chains.
- **§5 Theorem 5.1 (Lemma A, $r^L \le 61/50$):** Verified Hermite–Hadamard midpoint bound, $S_{\mathrm{err}}$ integral bound, Proposition 5.0(3) $G(x)$ identity, and all finite pairs $3 \le L \le 11$ plus $L \ge 12$.
- **§5 Theorem 5.2 (Lemma B1, $a \ge 2$, $r^L \ge 61/50$):** Verified Steps 1–3 (`L >= 12` 2D check, `6 <= M <= 29`, `M >= 30` using valid universal upper bound `1 + u` on subtracted factor, all `27` active pairs `(4, 1)` + `5 <= L <= 11`, plus explicit infeasibility proof for `(4, 2)` via $1 + S(x) < u^{-1} + u^{-2}$). *(Non-breaking prose notes: on L169 `(7,1,4)` over `[231/256, 467/512]`, `[L_sw, U_sw]` alone already closes `(7,1,4)` without invoking `delta_3`; on L278, `(4, 2)` is counted among the `27` pairs for `4 <= L <= 11` and excluded by `1 + S < u^{-1} + u^{-2}`.)*
- **§5 Theorem 5.3 (Lemma B2, $a = 1, r^* = 1$):** Verified `Lam >= 17`, `[1, 17] x [1/5, 1] x [ln(61/50), ln(133/100)]` 3D dual-number MVT subdivision (positive integral clipped to `0` when `u_* <= 2/11`), all `73` finite `(L, d)` pairs (`3 <= L <= 10`), `B2(b)` `L >= 9` 2D box check, and `20` pairs (`4 <= L <= 8`) with the repaired $x^M + x^{2M-1} \ge 1$ pruning condition.
- **§5–6 Theorem 5.4 (Lemma C, $a = 1, r^* \ge 2$) & Main Theorem:** Verified $r^* \ge 3$ ($M = 6..25$ and $M \ge 26$), $r^* = 2$ ($M \ge 35$ and all `493` pairs for `6 <= M <= 34` with the repaired $x^M + x^{2M-1} < 1 \le x^M + x^{2M-1} + x^{3M-3}$ bounds), and Section 6 global optimality synthesis.

## Independent Exact Verification (`notes/check-check-3.py`)

Repaired per `AUDIT.md` §3 (`**(M-1)` -> `**M` on L1018, L1094, L1225, L1229, L1274, L1276; `!= (4, 1)` -> `!= (4, 2)` + `(4, 2)` infeasibility assertion on L691; `1 + u` bound on L611) and verified end-to-end after final edit (`FLOAT_COUNT: 0` via AST check):

```text
[1/6] Checking symbolic identities (Lemmas 2.1, 2.2, Prop 5.0(3), Lemma 5.2) & n=7,8 exhaustive cuts...
[2/6] Checking Lemma 3.2, Lemma 3.3, Theorem 4.1, and exact Sturm chains for n=7 (Theorem 4.2)...
[3/6] Checking Theorem 5.1 (Lemma A, r^L <= 61/50) via rigorous interval subdivision...
[4/6] Checking Theorem 5.2 (Lemma B1, a >= 2, r^L >= 61/50)...
[5/6] Checking Theorem 5.3 (Lemma B2, a=1, r*=1)...
[6/6] Checking Theorem 5.4 (Lemma C, a=1, r* >= 2)...
PASS
FLOAT_COUNT: 0
```

## Verdict

**PASS** (`Gate 2` cleared by `@watch-6` `#701` and `@watch-1` `#707`; ready for `@audit-1` re-audit alongside `#1211`).

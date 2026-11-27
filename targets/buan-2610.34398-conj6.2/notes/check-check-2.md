# Blind Check Report — `targets/buan-2610.34398-conj6.2/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty: PASS per `watch-1` `#1230`, `watch-5` `#1226`, `watch-6` `#1261`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary source checked:** [tools/.arxiv_cache/eprint/2610.34398/lifting_arxiv_25102026.tex](file:///Users/kolinhuang/Documents/open-math/tools/.arxiv_cache/eprint/2610.34398/lifting_arxiv_25102026.tex) lines 1913–1945 (Section 7.1 `\subsection{TF-ordered $\tau$-rigid modules}` `\label{sec:conj1}`, **Conjecture 7.2** `\label{conj:TFordered}`, **Theorem 7.1** `\label{thm:TF-bij}`), plus cited `[BHM]` statements (`thm:main1`, `setupCZ`, `prop:FZaddC`, `prop:FZ-defined`, `lem:fU-projectives`, `prop:FZ-projectives`, `thm:reduction-functor`) and Examples 1–3 (`L1997–2250`).
- **`TARGET.md` comparison:** Matches verbatim — claims that for a $\tau$-tilting finite finite-dimensional $k$-algebra $\Lambda$, two-sided ideal $I \subseteq \mathrm{rad}\Lambda$, $F = (\Lambda/I) \otimes_\Lambda -$, TF-ordered $\tau_{\Lambda/I}$-rigid module $(M_1,\dots,M_t)$, and $(N_1,\dots,N_t) = L_I(M_1,\dots,M_t) = \omega^{-1}\Delta_I\omega_I(M_1,\dots,M_t)$, we have $F(N_i) = M_i^{r_i} \amalg X$ with $X \in \mathrm{add}(\coprod_{j=i+1}^t M_j)$ and integer $r_i \ge 1$. Note that directory slug `buan-2610.34398-conj6.2` tracks Section 7.1 Conjecture 7.2 (`\label{conj:TFordered}`), documented explicitly in `TARGET.md` and `PROOF.md`.

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/buan-2610.34398-conj6.2/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/buan-2610.34398-conj6.2/notes/check-check-2.py) (zero floating-point arithmetic; pure-Python `int` and `fractions.Fraction` exact linear algebra over $\mathbb{Q}$, building bound quiver algebras, 2-term silting mutation, Nakayama $\tau = \ker(\nu d)$, Jasso reduction $\Gamma = \mathrm{End}_\Lambda(Q_Z)^{\mathrm{op}}$ and $\Gamma/I_Z$, and recursive $L_I$ from scratch).
- **Command & result:** `.venv/bin/python -u targets/buan-2610.34398-conj6.2/notes/check-check-2.py` exited with code `0` (`PASS` in `13.84s`):
  - Verified Eq. (1) $\dim\mathrm{Hom}_K(P_X, P_Y[1]) = \dim\mathrm{Hom}_A(Y, \tau_A X)$, Lemma 2.1(c) & Corollary 3 ($F(P_Z) \cong P_C$, $F(Z) \cong C$, $\mathrm{add} F(P_{B_Z}) = \mathrm{add} P_{B_C}$), recursive Jasso reduction $L_I$, Strong Theorem 1 ($F(P_{N_i})$ has zero shifted projective summands $R[1]$, $g_{\Lambda/I}(F(N_i)) = g_\Lambda(N_i)$, and matching $P_0, P_1$), Conjecture 7.2, and sharp multiplicity $r_i = 1$ across all **434** TF-ordered $\tau_{\Lambda/I}$-rigid sequences in 8 algebra-quotient pairs:
    1. `Paper Ex 1: A3 -> A3/<ba>`: 29 seqs (12 length-3, matching Figure 1 count; 1 non-lifted module with $R[1] \ne 0$).
    2. `Paper Ex 2a: <cab, b^2, c^2> -> A2`: 6 seqs (1 term with $X \ne 0$; 1 non-lifted module with $R[1] \ne 0$).
    3. `Paper Ex 2b: R_2 A_2 -> A2`: 6 seqs.
    4. `Paper Ex 3: C2/J^3 -> C2/J^2`: 8 seqs.
    5. `C3/J^4 -> C3/J^3`: 63 seqs.
    6. `2-cycle <ga, bag> -> A3`: 38 seqs (2 non-lifted modules with $R[1] \ne 0$).
    7. `D4 -> D4/<ca>`: 246 seqs (25 terms with $X \ne 0$; 2 non-lifted modules with $R[1] \ne 0$).
    8. `Pi(A3) -> A3`: 38 seqs (5 terms with $X \ne 0$; 4 non-lifted modules with $R[1] \ne 0$).

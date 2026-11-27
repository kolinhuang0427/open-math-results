# Check Report: `targets/garrity-2410.02032-conj1/`

- **Checker:** `@check-1`
- **Verdict:** **PASS** (re-checked after `#840` patches resolving all `AUDIT.md` §1–§4 items)
- **Primary Source:** `tools/.arxiv_cache/eprint/2410.02032/Final_Revision-Garrity-Osterman.tex` (`arXiv:2410.02032v2`, Section 4 Def 12 L664, Section 5 Cor 1 L753, Section 7 Props 18–19 L1945/L1974, Section 8 Conjecture 1 `conj:e-23-e` L2149–2151, Section 10 L2659–2746, Section 12 Appendix L2837–2895)
- **Verifier Script:** `targets/garrity-2410.02032-conj1/notes/check-check-1.py` (exact integer/string/set arithmetic, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` and `PROOF.md` match `Final_Revision-Garrity-Osterman.tex` verbatim for Conjecture 1 (`conj:e-23-e`, Section 8), Substitutions $S_0, S_1$ (Section 10), Section 4 Definition 12, Section 5 Corollary 1, Section 7 Propositions 18–19, Section 10, and Section 12 Appendix (L2889–2895).

## 2. Independent Verification Summary
Re-ran `.venv/bin/python -u targets/garrity-2410.02032-conj1/notes/check-check-1.py` (exit code 0, `PASS`):
- **Check 1 (Substitutions & abelianization):** Verified $G_k = S_1^k \circ S_0$, $\tau_{j,k} = G_j \circ G_k$, and $M_{j,k}$ for $0 \le j,k \le 4$, plus $M_{1,1}^2 > 0$ entrywise.
- **Check 2 (Proposition 1.4 & Lemma 2 in actual languages):** Verified all $36$ parameter combinations $(j_1,k_1) \in \{0,1\}^2$ followed by $(j_0,k_0) \in \{0,1,2\}^2$ against actual generated factors up to length $14$: every age-0 bispecial matches Lemma 2 and every bispecial containing $3$ matches Proposition 1.4.
- **Check 3 (Lemma 3 & tightened Theorem 4 invariant):**
  - Closed $\mathcal{N}_0$ across all 4 modes $(j>0, k>0) \in \{0,1\}^2$: all neutral, zero escapes.
  - Verified Theorem 4 invariants (1)–(4) with tightened 4-transition set $\mathcal{T}_{\ge 1} = \{(E_{32}^-, A^+), (A_1^-, B^+), (A_2^-, B^+), (B^-, A^+)\}$, $r=0$ $E_{33}^B/E_{33}^C$ gap $\Delta_3 \ge 1$, and $(0,0)$-step words $3^{t_m}(13^{t_m})^j$ on base case, $16$ two-step transitions, and $10$ multi-$(0,0)$ / alternating coding sequences up to word length $16$.
- **Check 4 (Direct complexity):** Verified $p_{\mathcal{L}}(n) \le 3n$ up to $n = 50$ across $21$ $S(e,23,e)$-adic coding sequences.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.

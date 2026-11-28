# Blind Independent Audit Report — `targets/gaevoy-2606.25895-src2-1/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2606.25895/{lipics.tex,lipics-v2021.cls,preamble.tex,static.tex,static/introduction.tex,static/definitions.tex,static/tseitin.tex,static/open.tex}`, live arXiv API query, `TARGET.md`, `PROOF.md`, independent checker's `notes/check-check-2.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Nikita Gaevoy, *"The Power of Small Symmetries"*, `arXiv:2606.25895v1` (`2026-06-24`, verified sole version via live `tools/arxiv_fetch.py query --id-list 2606.25895 --no-cache`; MFCS 2026 LIPIcs Vol. 386, Art. 97), Section 2 (`static/definitions.tex` L3–142) & Section 6 (`static/open.tex` L3–5).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming both boundary-case fixes from initial FAIL `#1933` were cleanly applied in `PROOF.md`; publication label: **"written proof, internally audited"**).

---

## 1. Primary Source & Statement Fidelity Check

Verified verbatim against `tools/.arxiv_cache/eprint/2606.25895/`:
- **Macro & definitions (`preamble.tex` L15–19; `static/definitions.tex` L3–105, L127–142):**
  - `\SRCII[1]` expands to `1\text{-SRC-II}` (Resolution with local complementary $1$-symmetries).
  - Definition 1 (`$k$-symmetry`, L3–13): bijection on literals with $\phi(\neg x) = \neg\phi(x)$ fixing all variables except at most $k$; complementary $1$-symmetries include single-variable sign flips $\phi_v(v) = \neg v$.
  - Definition 2 (`\SRCIII[k]`, L15–40) & Definition 4 (`\SRCII[k]`, L55–59): local $k$-symmetry rule infers $\phi(B_1), \dots, \phi(B_l) \vdash \phi(A)$ from a previously inferred justification $B_1, \dots, B_l \vdash A$, requiring all $B_i$ and all $\phi(B_i)$ to belong to the input CNF $\Phi$ (and all $\phi(B_i)$ to have appeared earlier in the proof).
  - Definition 8 (L92–94): $S_\Pi(\Phi)$ is the minimum number of steps.
  - Definition 9 (L100–105): $A$ is *exponentially separated* from $B$ if there exists a family $\Phi_n$ with $S_A(\Phi_n) = \mathcal{O}(\mathrm{poly}(n))$ and $S_B(\Phi_n) = 2^{\Omega(n)}$.
  - Compiled LIPIcs numbering (`lipics-v2021.cls` L1154–1171 shared `theorem` counter, verified across `static/*.tex`): Section 2 (`definitions.tex`), Section 4 (`tseitin.tex`, Definition 21, Section 4.1, Theorem 22 `thrm:haastad`, Corollary 24 `cor:Rectangular4`), Section 6 (`open.tex`). Every single section/theorem/definition citation in `TARGET.md` and `PROOF.md` matches verbatim!
- **Open question quotes (`static/open.tex` L3–5 & `static/definitions.tex` L141–142):** Verified verbatim in `TARGET.md` L25–27, L32 and `PROOF.md` L5.
- **`TARGET.md` fidelity:** **PASS** (zero defects).

---

## 2. Line-by-Line Mathematical Verification of `PROOF.md`

- **Section 1 (L27–46) — Definitions & Guarded Tseitin Formula:**
  - Exact match to Gaevoy Definitions 1, 2, 4, 8, 9 and Definition 21.
  - **DEFECT 1 (`PROOF.md` L45 & L147, boundary case $n = 2$):**
    L45 states that $\widetilde{\operatorname{Ts}}(G, \alpha)$ *"has $N = |E| + 1$ variables, $\sum_{v \in V} 3 \cdot 2^{\deg(v) - 1}$ clauses, and maximum clause width $\Delta(G) + 1$"*, and L147 states Phase 0 *"uses exactly $\sum_{v \in V} (2^{\deg(v)-1} + 2^{\deg(v)}) = \sum_{v \in V} 3 \cdot 2^{\deg(v)-1}$ steps"*.
    For $n = 2$ ($G = K_2$, which is inside the quantifier $n \ge 2$ of the Main Theorem, Lemma 1, and Theorem 5), the two vertices share the unique incident edge set $\partial(v_1) = \partial(v_2) = \{e\}$, so $\operatorname{All}(v_1) = \operatorname{All}(v_2) = \{e, \neg e\}$ and the set $\widetilde{\operatorname{Ts}}(K_2, \alpha)$ has **$4$** distinct clauses, not $6 = \sum_{v} 3 \cdot 2^{\deg(v)-1}$! (For all connected simple graphs on $n \ge 3$ vertices, the sets $\partial(v)$ are pairwise distinct and the exact equality holds.)
    - **Fix:** Change L45 to *"at most $\sum_{v \in V} 3 \cdot 2^{\deg(v) - 1}$ clauses (with equality for $n \ge 3$)"* and L147 to *"at most $\sum_{v \in V} (2^{\deg(v)-1} + 2^{\deg(v)}) = \sum_{v \in V} 3 \cdot 2^{\deg(v)-1}$ steps"*.
- **Section 2 (L49–77) — Lemma 1 (Self-Contained Expander Existence):** **100% SOUND.**
  - Verified every step: 8 independent random permutations $\pi_1, \dots, \pi_8 \in S_n$ ($\Delta \le 16$, $|E| \le 8n$), $s = \lfloor u/8 \rfloor < n - u$, $t = u + s < n$, exact probability $\left(\binom{t}{u}/\binom{n}{u}\right)^8 \le (9u/8n)^{8u}$, monotonicity of $(en/x)^x$ on $(0, n)$ (including $s = 0$), exact integer bound $(2B)^8 = 157464 \cdot 9^{64} \cdot 2^8 / 2^{247} < 2^{231}/2^{247} < 1$, union bound $\sum_{u=1}^{\lfloor n/2 \rfloor} p_u < \sum_{u=1}^\infty 2^{-u} = 1$, connectivity and $|E_n| \ge n/2$.
- **Section 3 (L81–136) — Lemmas 2, 3, 4 (Exponential Resolution Lower Bound):** **100% SOUND.**
  - **Lemma 2 (Restriction $\{g \mapsto 1\}$):** Verified input, $x = g$, and $x \neq g$ resolution cases (non-tautologicality, subclause invariant, size $\le s$).
  - **Lemma 3 (Ben-Sasson–Wigderson Tseitin Width):** Verified satisfiability of $\operatorname{Ts}(U, \alpha)$ for proper $U \subsetneq V$, subadditivity of $\mu$, $n/3 < \mu(C^*) \le 2n/3$ (including $n = 2$), single-edge flip forcing every $e \in \partial_G(U^*)$ into $C^*$, and $w(C^*) \ge e(G)n/3$.
  - **Lemma 4 (Ben-Sasson–Wigderson Size-Width):** Verified base cases ($r = 0$, $m = 0$), literal averaging ($> \frac{d}{2N_0}b$), injective fat-clause tracking under restriction $\Pi \mapsto \Pi_1$, lifting $\Sigma_1$ to width $\le d + r$ deriving $\square$ or $\neg \ell$, resolving $\neg \ell$ with $C \lor \ell$ in $\Sigma_0$, and exact parameter choice $d = k + \lfloor (W-k-1)/2 \rfloor$, $r = \lceil (W-k-1)/2 \rceil$ yielding $S_{\mathrm{Res}}(\Phi) \ge \exp((W-k-1)^2 / (8N))$.
- **Section 4 (L139–190) — Theorem 5 (Quadratic $1\text{-SRC-II}$ Upper Bound):** **100% SOUND.**
  - Verified the Local Sign-Flip Simulation Subroutine: every chained step $\phi_g \to \phi_{f_1} \to \dots \to \phi_{f_s} \to \phi_g$ strictly obeys Gaevoy Definitions 1, 2, 4 — all intermediate premise sets stay in $\mathcal{L}_1(U) \subseteq \Phi$ (already present from Phase 0), and because $|F \cap \partial(u)|$ is even for all $u \in U$, the final $\phi_g$ lands back in $\mathcal{L}_0(U) \subseteq \Phi$!
  - Verified BFS spanning-tree cut induction, parity matching of Cases A & B, disjointness of $S \subseteq \partial_G(U_{t-1})$ and $F_1 \subseteq E(T[U_{t-1}])$, non-tautologicality of the complete binary resolution tree on $E_t$ (all 5 variable sets pairwise disjoint), Phase 2 derivation of $g$ and $\square$, and total step count bound $\le \sum_v 3 \cdot 2^{\deg(v)-1} + (n-1)(2^{\Delta-1}(m+4)-1) + 2^\Delta = O(2^\Delta nm)$.
- **Section 5 (L194–211) — Main Theorem & Bounded-Depth Frege Corollary:** **100% SOUND**, with one tiny edge-case fix:
  - Main Theorem arithmetic verified: $N_n = \Theta(n)$, $M_n = \Theta(n)$, width $\le 17$, $S_{1\text{-SRC-II}}(\Phi_n) = O(n^2) = O(N_n^2)$, and for $n \ge 816$ ($48 \cdot 17 = 816$), $S_{\mathrm{Res}}(\Phi_n) \ge \exp(n/147456) = 2^{\Omega(n)} = 2^{\Omega(N_n)}$ ($48^2 \cdot 64 = 147456$).
  - Bounded-depth Frege Corollary verified (including the $O(n^2)$ 6-step local $1$-symmetry simulation of Gaevoy Corollary 24's $4$-cycle flips and Håstad's Theorem 22 lower bound under $g \mapsto 1$).
  - **DEFECT 2 (`PROOF.md` L208, boundary case $n = 1$):** Change *"For odd $n$"* to *"For odd $n \ge 3$"* (since $H_1$ is not a simple $4$-regular graph with $2n^2$ edges and $24n^2$ clauses).

---

## 3. Independent Verifier Audit (`notes/check-check-2.py`)

- Re-executed `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py`: exited `0`, raw stdout:
  - `[PASS] Primary source arXiv:2606.25895v1 verbatim quotes, macros, & compiled numbering verified.`
  - `[PASS] Lemma 1 exact integer/rational bounds (2<=n<=40) & concrete expanders verified.`
  - `[PASS] Strict 1-SRC-II Cook-Reckhow checker, Theorem 5 proofs (K2..M20), Res unfolding + Lemma 2 restriction, H3 4-cycle simulation, & Lemma 3 expansion verified.`
  - `PASS`
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Verified file MD5s at initial audit:
  - `TARGET.md`: `a3f3dac212004b66dff2471cbef3d3d9`
  - `PROOF.md`: `37f9001e116191a23721924d327be1f6`
  - `notes/check-check-2.md`: `fecf43eff37002f3537013fe2bae80ff`
  - `notes/check-check-2.py`: `ba7850331a0b26f45adf2c9a7a6cf240`
- Verifier logic inspected line-by-line (L1–695): **PASS** (strict Cook–Reckhow checker + pure Res unfolding + Lemma 2 restriction; already uses `phase0_count <= sum_bound_input`, so no changes needed to `check-check-2.{md,py}`).

---

## 4. Gate 2 Novelty Status

- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`2026-11-27T19:34Z`–`19:35Z`, `0/811` snapshot hits, `2606.25895v1` sole arXiv version, OpenAlex `cited_by_count: 0`, OpenCitations `[]`, ECCC `/year/2026/` clear, GH/Zenodo/HexagonMath/Papex/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

Following `@attack-4` (`#1937`), `@audit-2` re-verified the patched `PROOF.md` verbatim on disk and re-executed the independent verifier:

1. **Defect 1 resolved (`PROOF.md` L45 & L147):** Updated to *"at most $\sum_{v \in V} 3 \cdot 2^{\deg(v) - 1}$ clauses (with equality for connected simple graphs on $|V| \ge 3$ vertices, where the incident edge sets $\partial(v)$ are pairwise distinct)"* (L45) and *"at most $\sum_{v \in V} (2^{\deg(v)-1} + 2^{\deg(v)}) = \sum_{v \in V} 3 \cdot 2^{\deg(v)-1}$ steps (with equality for $n \ge 3$)"* (L147).
2. **Defect 2 resolved (`PROOF.md` L208):** Updated *"For odd $n$"* $\to$ *"For odd $n \ge 3$"* in the Bounded-Depth Frege Corollary.
3. **Final independent re-run by `@audit-2`:**
   - Command: `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py` -> exit `0`, raw stdout:
     - `[PASS] Primary source arXiv:2606.25895v1 verbatim quotes, macros, & compiled numbering verified.`
     - `[PASS] Lemma 1 exact integer/rational bounds (2<=n<=40) & concrete expanders verified.`
     - `[PASS] Strict 1-SRC-II Cook-Reckhow checker, Theorem 5 proofs (K2..M20), Res unfolding + Lemma 2 restriction, H3 4-cycle simulation, & Lemma 3 expansion verified.`
     - `PASS`
   - AST zero-float check: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
   - Verified file MD5s: `TARGET.md` `a3f3dac212004b66dff2471cbef3d3d9`, `PROOF.md` `b298368b215afc8a8bc3a784158f7fcd`, `notes/check-check-2.md` `fecf43eff37002f3537013fe2bae80ff`, `notes/check-check-2.py` `ba7850331a0b26f45adf2c9a7a6cf240`.

**Final Verdict: PASS** (publication label: **"written proof, internally audited"**). Handing off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`, including ECCC & conference coverage) prior to coordinator reporting.

# Independent Check Report (`@check-2`): `targets/gaevoy-2606.25895-src2-1/`

**Verdict:** `PASS`

## 1. Primary Source & Restatement Verification
- **Primary source:** `tools/.arxiv_cache/eprint/2606.25895/` (Nikita Gaevoy, *The Power of Small Symmetries*, `arXiv:2606.25895v1`, `static/definitions.tex`, `static/tseitin.tex`, `static/open.tex`, `preamble.tex`).
- **Match check:** `TARGET.md` and `PROOF.md` quote Section 6 (`static/open.tex` lines 3–5) and Section 2 (`static/definitions.tex` lines 141–142) verbatim, accurately note `\SRCII[1]` compiles to `$1\text{-SRC-II}$`, and match compiled numbering (`Section 2`, `Section 4`, `Section 6`, `Definition 9`, `Definition 21`, `Theorem 22`, `Corollary 24`).
- **`PROOF.md` review:**
  - **Lemma 1 (Expander existence):** Sound 8-permutation random graph bound ($n \ge 2$, $\Delta \le 16$, $n/2 \le |E| \le 8n$, $e(G_n) > 1/8$), exact probability/combinatorial inequalities verified including $(2B)^8 < 1$.
  - **Lemmas 2–4 (Resolution lower bound):** Guard restriction $\{g \mapsto 1\}$ reducing $\widetilde{\operatorname{Ts}}(G, \alpha)$ to $\operatorname{Ts}(G, \alpha)$, Ben-Sasson–Wigderson Tseitin width lower bound $e(G)n/3$ (including $n=2$ base case), and size-width tradeoff yielding $S_{\mathrm{Res}}(\Phi_n) \ge \exp(n/147456)$ for $n \ge 816$ verified complete and airtight.
  - **Theorem 5 & Bounded-Depth Frege Corollary:** Local $1$-symmetry sign-flip bridge via $\phi_g \to \phi_{f_1} \to \dots \to \phi_{f_s} \to \phi_g$, BFS spanning-tree cut induction, Phase 2 derivation of $g$ and $\square$ in total size $\le \sum_v 3 \cdot 2^{\deg(v)-1} + (n-1)(2^{\Delta-1}(m+4)-1) + 2^\Delta = O(2^\Delta nm)$, and $6$-step local $1$-symmetry simulation of toroidal $4$-cycles for $\widetilde{T}_n$ verified.

## 2. Independent Exact Verifier (`notes/check-check-2.py`)
- **Methodology:** Zero-floating-point Python (`int` and `fractions.Fraction` only), written directly from `arXiv:2606.25895v1` and `PROOF.md`.
- **Checks performed:**
  1. Verbatim `static/open.tex`, `static/definitions.tex`, `preamble.tex` macro `\SRCII[1]`, and compiled LIPIcs numbering check (`Sec. 2, 4, 6`, `Thm. 22`, `Cor. 24`).
  2. Lemma 1 exact integer inequality (`157464 * 9**64 * 2**8 < 2**247`), exact `Fraction` union bound (`< 1` for all $2 \le n \le 40$), concrete 8-permutation expander sampling with exact edge expansion $e(G_n) > 1/8$ for $n \in \{10, 14, 18\}$, and exact Main Theorem arithmetic (`48*17 = 816`, `48**2 * 64 = 147456`).
  3. Strict Cook–Reckhow `1-SRC-II` verifier (enforcing $|\operatorname{supp}(\phi)| \le 1$, $L(j) \subseteq \Phi$, $\phi(L(j)) \subseteq \Phi$, prior derivation of $\phi(L(j))$, non-tautological resolution) on explicit Theorem 5 proofs constructed for $K_2$ ($n=2$), $K_4$ ($n=4$), $K_{3,3}$ ($n=6$), an irregular graph ($n=7$, degrees $1$–$4$), Petersen ($n=10$), $3 \times 3$ toroidal grid $H_3$ ($n=9$), and Möbius ladder $M_{20}$ ($n=20$).
  4. Independent recursive unfolding of `1-SRC-II` proofs to pure Resolution and Lemma 2 $\{g \mapsto 1\}$ restriction to pure Resolution refutations of $\operatorname{Ts}(G, \alpha)$ on $K_2, K_4, K_{3,3}, \text{Irreg7}$; $6$-step local $1$-symmetry simulation of $4$-cycle flips on $\widetilde{T}_3$; exact `Fraction` edge expansion $e(G)$ on $K_4$ (`2`), $K_{3,3}$ (`5/3`), and Petersen (`1`).
- **Run command & output:**
  ```text
  .venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py
  [PASS] Primary source arXiv:2606.25895v1 verbatim quotes, macros, & compiled numbering verified.
  [PASS] Lemma 1 exact integer/rational bounds (2<=n<=40) & concrete expanders verified.
  [PASS] Strict 1-SRC-II Cook-Reckhow checker, Theorem 5 proofs (K2..M20), Res unfolding + Lemma 2 restriction, H3 4-cycle simulation, & Lemma 3 expansion verified.
  PASS
  ```
  (Exit code `0`.)

## 3. Gate Status
- Gate 1: `PASS` (recorded in `TARGET.md`).
- Gate 2: `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

# Independent Blind Audit — `targets/bui-2508.04602-conj8.1/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:10Z`
- **Verdict:** **PASS**

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against the arXiv TeX source `tools/.arxiv_cache/eprint/2508.04602/article.tex` (`arXiv:2508.04602v1`, sole version on arXiv; Hong Duc Bui, *"On existence of a compatible triangulation with the double circle order type"*):
- **Numbering:** Line 23 declares `\newtheorem{conjecture}{Conjecture}[section]`. The document has `\section{Introduction}` (1), `\section{Related Works}` (2), `\section{Notation}` (3), `\section{A Divide-and-conquer Helper Tool}` (4), `\section{Another Divide-and-conquer Helper Tool}` (5), `\section{On Compatible Triangulation of Polygons}` (6), `\section{Main Result}` (7), and `\section{Discussion}` (8, line 1149). The conjecture at line 1194 inside `\subsection{Matching Problem and Acyclicity of State Graph}` (line 1163) is the sole conjecture in Section 8, hence **Conjecture 8.1**.
- **Exact Statement:** `TARGET.md` and `PROOF.md` faithfully match lines 1188–1217 of `article.tex`: a planar point set $Q$ in general position with $|Q| = 2n$ and $|\mathrm{CH}(Q)| = n$ (requiring $n \ge 3$), hull vertices $Q_1, \dots, Q_n$ in cyclic order, interior points $B_1, \dots, B_n$, and the directed state graph $G$ on $S_n$ with edge $\pi \to \rho$ iff $\rho$ swaps $\pi_i$ and $\pi_j$ ($i \neq j$) for a pair of nontrivially intersecting triangles $T_i(\pi) = \triangle Q_i B_{\pi_i} Q_{i+1}$ and $T_j(\pi) = \triangle Q_j B_{\pi_j} Q_{j+1}$.
- **Scope note on order types:** In `article.tex` (`\label{def_order_type}`, lines 62–64), an *order type* is defined as an equivalence class of realizable planar point sets in $\mathbb{R}^2$. As noted in `PROOF.md` (line 79), triangle intersection depends only on the order type, and every realizable planar order type admits a realization in $\mathbb{R}^2$ on which the potential $\Phi$ is defined. (Non-realizable abstract chirotopes are outside both the paper's definition of order type and the proof.)

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Setup & Domain (lines 7–13):**
   - Counterclockwise cyclic indexing of $Q_1, \dots, Q_n$ (modulo $n$) is without loss of generality by reflection. Requiring $|\mathrm{CH}(Q)| = n$ and $n$ interior points in general position indeed implies $n \ge 3$.
   - Nontrivial intersection (beyond a shared convex-hull vertex when $j \equiv i \pm 1 \pmod n$) matches the geometric swap rule for non-crossing triangle matchings.
2. **Lemma 1 — General-Position Intersection Equivalence (lines 19–26):**
   - Checked all cases for $i \neq j$, $a \neq b$, $n \ge 3$:
     - Reverse implication ($\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset \implies$ nontrivial intersection): immediate since open interiors contain no vertices.
     - Forward implication: if $X \in (T_i \cap T_j) \setminus (\{Q_i, Q_{i+1}\} \cap \{Q_j, Q_{j+1}\})$, then $X$ cannot be a common vertex since $B_a \neq B_b$.
     - If $X \in \mathrm{int}(T_i)$ (or symmetrically $\mathrm{int}(T_j)$), non-degeneracy of $T_j$ (general position) implies every open neighborhood of $X$ meets $\mathrm{int}(T_j)$, giving $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$.
     - If $X \in \partial T_i \cap \partial T_j$, general position forbids any vertex of one triangle from lying in the relative interior of an edge of the other, so $X \in \mathrm{relint}(e_i) \cap \mathrm{relint}(e_j)$. Because $n \ge 3$ ($Q_i Q_{i+1} \neq Q_j Q_{j+1}$) and $B_a \neq B_b$, the two edges have distinct unordered pairs of endpoints in $Q$, hence at least 3 distinct points of $Q$; general position therefore prevents collinearity, forcing a transverse crossing and a nonempty open wedge in $\mathrm{int}(T_i) \cap \mathrm{int}(T_j)$. Airtight.
3. **Lemma 2 — Positivity of Oriented Edge-Height Functions (lines 30–40):**
   - $\ell_k(X) = \det(Q_{k+1} - Q_k, X - Q_k)$ is affine in $X$ and equals $2\mathrm{Area}_{\mathrm{signed}}(\triangle Q_k Q_{k+1} X)$.
   - Properties (1)–(3) follow directly from counterclockwise hull order and general position (no three points collinear, so no third point of $Q$ lies on $\overline{Q_k Q_{k+1}}$).
   - Property (4): for $i \neq j$ and $n \ge 3$, $\{Q_i, Q_{i+1}\} \neq \{Q_j, Q_{j+1}\}$, so at least one of $Q_i, Q_{i+1}$ lies outside $\{Q_j, Q_{j+1}\}$ (strictly positive $\ell_j$), while the other has $\ell_j \ge 0$; thus $\ell_j(Q_i) + \ell_j(Q_{i+1}) > 0$. Airtight.
4. **Lemma 3 — Strict Area-Product Decrease on Every Swap (lines 44–66):**
   - Pick $Z \in \mathrm{int}(T_i(\pi)) \cap \mathrm{int}(T_j(\pi))$, so $Z = \alpha Q_i + \beta Q_{i+1} + \gamma B_{\pi_i}$ with $\alpha, \beta, \gamma > 0$ and $\alpha + \beta + \gamma = 1$.
   - By affineness and Lemma 2(1),(3),(4): $\ell_i(Z) = \gamma \ell_i(B_{\pi_i}) > 0$ and $\ell_j(Z) = \alpha \ell_j(Q_i) + \beta \ell_j(Q_{i+1}) + \gamma \ell_j(B_{\pi_i}) > \gamma \ell_j(B_{\pi_i}) > 0$.
   - Dividing positive quantities yields $\ell_i(Z)/\ell_j(Z) < \ell_i(B_{\pi_i})/\ell_j(B_{\pi_i})$.
   - Symmetrically from $Z \in \mathrm{int}(T_j(\pi))$: $\ell_j(Z)/\ell_i(Z) < \ell_j(B_{\pi_j})/\ell_i(B_{\pi_j})$.
   - Multiplying both strict inequalities between positive real numbers cancels $\ell_i(Z), \ell_j(Z)$ and gives $\ell_i(B_{\pi_j})\ell_j(B_{\pi_i}) < \ell_i(B_{\pi_i})\ell_j(B_{\pi_j})$.
   - Post-swap non-intersection follows cleanly by contradiction via Lemma 1 and the reversed inequality. Airtight.
5. **Main Theorem (lines 70–79):**
   - $\Phi(\pi) = \prod_{k=1}^n \ell_k(B_{\pi_k}) > 0$ for every $\pi \in S_n$.
   - Along any directed edge $\pi \to \rho$ swapping $i, j$, all factors $k \notin \{i, j\}$ cancel identically, so $\Phi(\rho)/\Phi(\pi) = \frac{\ell_i(B_{\pi_j})\ell_j(B_{\pi_i})}{\ell_i(B_{\pi_i})\ell_j(B_{\pi_j})} < 1$, i.e. $\Phi(\rho) < \Phi(\pi)$ strictly.
   - Strict monotonicity of a real-valued potential on a finite graph ($|S_n| = n!$) implies $G$ is a DAG, and any directed path has at most $n! - 1$ edges. Airtight.

---

## 3. Independent Verification & Gate 2 Check

- **Independent Checker Re-run (`notes/check-check-1.py`):**
  - Command: `.venv/bin/python targets/bui-2508.04602-conj8.1/notes/check-check-1.py`
  - Exit code: `0`
  - Raw output: `Total: 34 instances, 96940 directed swap edges verified. PASS`
  - Script independently constructs exact integer point sets across $n \in \{3, 4, 5, 6, 7\}$ (general position checked via nonzero orientation determinants), verifies Lemma 1 (segment crossing / point-in-triangle equivalence against exact rational interior witness), Lemma 3 ($\Phi(\rho) < \Phi(\pi)$ and post-swap disjointness), and full DAG acyclicity via Kahn's algorithm for $n \le 6$.
- **Gate 2 Novelty Receipts:** Verified all three receipts (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`) — all **PASS** (`We-Solve/research#56` covers Theorems 7.1–7.2 only, not §8.2; `AlexenderSokolov` hit is CC-BY license metadata only; OpenAlex `cited_by_count: 0`).

---

## 4. Verdict & Handoff

**PASS.** No mathematical, logical, citation, or statement-fidelity gaps remain. Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.

---

## 5. Lean 4 Formalization Statement-Fidelity Audit (`2026-11-27T10:53Z`) — **PASS**

- **File audited:** [Bui250804602Conj81.lean](file:///Users/kolinhuang/Documents/open-math/lean/OpenMath/Bui250804602Conj81.lean) (865 lines), imported in [OpenMath.lean](file:///Users/kolinhuang/Documents/open-math/lean/OpenMath.lean#L17).
- **Primary-source statement fidelity (`tools/.arxiv_cache/eprint/2508.04602/article.tex`, Section 8.2, Conjecture 8.1, L1188–1217):**
  - `PointConfig n` (`hn : 3 ≤ n`, `Q, B : Fin n → Pt`, `inj : Function.Injective (Sum.elim Q B)`, `general_position`, `hull_ccw`, `interior_pos`): faithfully captures every planar point set in general position of size $2n$ with $|\mathrm{CH}(Q)| = n$ (up to plane reflection to counterclockwise hull order; $n \ge 3$ is forced automatically by $|Q|=2n, |\mathrm{CH}(Q)|=n$). Zero hidden hypotheses or vacuity.
  - `InClosedTri`, `InOpenTri`, `Tri`, `OpenTri`, `TrianglesIntersect` (sharing a point outside `{Q i, Q (i+1)} ∩ {Q j, Q (j+1)}`), and `StateEdge` (swapping `π i` and `π j` for `i ≠ j` with intersecting triangles `T_i(π)` and `T_j(π)`) match `article.tex` L1198–1211 verbatim.
  - Main theorems `PointConfig.bui_conjecture_8_2_acyclic` (`¬ Relation.TransGen cfg.StateEdge π π`), `PointConfig.bui_conjecture_8_2_terminates` (`L ≤ n.factorial - 1`), and `PointConfig.swapped_triangles_disjoint` prove exact acyclicity, termination, and post-swap disjointness. (Note: the theorem identifiers reference Section 8.2, matching the docstring *"Section 8.2 Conjecture"*; the shared `[section]` counter numbers it Conjecture 8.1.)
- **Hygiene & kernel verification:**
  - `grep -nE 'sorry|admit|axiom |native_decide|unsafe|implemented_by|extern |partial ' lean/OpenMath/Bui250804602Conj81.lean`: 0 matches (`HYGIENE_CLEAN`).
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Bui250804602Conj81.lean` — exit `0`, 0 errors/warnings; `#print axioms` reports solely `[propext, Classical.choice, Quot.sound]` for all 6 exported theorems.

**Lean Audit Verdict: PASS.** Handed off directly to `@coordinator`.

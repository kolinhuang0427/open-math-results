# Blind Audit Report: `bartnicki-2303.08771-conj3`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:33Z` (re-audited `2026-11-27T09:39Z`)
**Verdict:** **PASS** (after Section-3 citation fix) — Counterexample verified by hand proof and exact computation (`"counterexample, verified by exact computation"`).

## 1. Primary-Source Fidelity & Blocking Citation Fix
Checked verbatim against BOTH:
1. `arXiv:2303.08771v1` (`tools/.arxiv_cache/eprint/2303.08771/Zlamasy_III_11.tex`, confirmed latest arXiv version `2023-03-15`), and
2. The published open-access journal version: Tomasz Bartnicki, Sebastian Czerwiński, Jarosław Grytczuk, and Zofia Miechowicz, *"Strong Arboricity of Graphs"*, *Graphs and Combinatorics* **41** (2025), Art. 80, published online 2 July 2025, `DOI: 10.1007/s00373-025-02934-5` (OpenAlex `W4411944715`, `cited_by_count = 0`).

- **Statement verbatim check:** Both `Zlamasy_III_11.tex` (lines 248–252) and *Graphs and Combinatorics* **41** (2025), Art. 80 (pp. 7–8) state **Conjecture 3** verbatim:
  > Every graph $G$ satisfies $\zeta(G) \leqslant \mathrm{col}(G)$.
  Definitions of woody coloring, broken cycle $C - e$, strongly woody coloring (no monochromatic broken cycle, equivalently woody in every single-edge contraction $G/e$), strong arboricity $\zeta(G)$, and coloring number $\mathrm{col}(G)$ match verbatim.
- **BLOCKING CITATION FIX NEEDED:**
  `Zlamasy_III_11.tex` has only **three** top-level `\section`s:
  - Section 1: `Introduction` (line 85)
  - Section 2: `The results` (line 105; with subsections 2.1–2.4)
  - **Section 3:** `Final remarks and open problems` (line 236; likewise **Section 3** on pp. 7–8 of *Graphs and Combinatorics* **41** (2025), Art. 80).
  Currently, `TARGET.md` (lines 3, 12, 18) and `COUNTEREXAMPLE.md` (line 5) erroneously cite **"Section 5"**. Please fix `Section 5` $\to$ `Section 3` in `TARGET.md` (lines 3, 12, 18) and `COUNTEREXAMPLE.md` (line 5), and update `TARGET.md` (lines 3 & 31) to also cite the published open-access journal version *Graphs and Combinatorics* **41** (2025), Art. 80 (`DOI: 10.1007/s00373-025-02934-5`, pp. 7–8, confirming Conjecture 3 remains open in print).

## 2. Mathematical Audit of `COUNTEREXAMPLE.md` (PASS — Zero Gaps)
Audited every claim independently line by line:
- **Graph $G$:** $9$ vertices $A=\{0,1,2,3\}$, $B=\{4,5,6\}$, $C=\{7,8\}$; $24$ edges $E_A = K_4$, $E_{AB} = K_{4,3}$, $E_{BC} = K_{3,2}$. Simple graph.
- **$\mathrm{col}(G) = 5$:** Ordering $(0,1,2,3,4,5,6,7,8)$ has max back-degree $4$ (so $\mathrm{col}(G) \le 5$), while $G[A \cup \{4\}] \cong K_5$ has minimum degree $4$ (so $\mathrm{col}(G) \ge 5$). Rigorous.
- **Hand proof of $\zeta(G) > 5$ (Claims 1–5):**
  - *Claim 1:* Strongly woody $\implies$ woody (deleting any edge of a monochromatic cycle yields a monochromatic broken cycle), and every component of $F_i$ is an induced tree (any chord $uv \in E(G) \setminus E(T)$ closes a monochromatic broken cycle $P_{uv}$ in $T$). Rigorous.
  - *Claim 2:* Any component containing an $E_A$-edge is an isolated $K_2$ in $A$ (otherwise a triangle in $A$ or with $B$ violates induced tree, and $C$ has no edges to $A$). Thus every component meeting $B$ meets $A$ in $\le 1$ vertex (if $\ge 2$, the $E_A$-edge between them would be forced into $T$), giving $e_{AB}(F) \le 3$, $e_A(F) \le 2$, and $3 e_A(F) + e_{AB}(F) \le 6$ with equality iff $(e_A, e_{AB}) \in \{(2,0), (1,3)\}$. Rigorous.
  - *Claim 3:* Summing gives $30 = 3|E_A| + |E_{AB}| \le 30$, forcing $1$ Type-I class ($F_5$) and $4$ Type-II classes ($F_1,\dots,F_4$). Rigorous.
  - *Claim 4:* Up to $S_4$-symmetry, $F_5 \cap E_A = \{\{0,1\},\{2,3\}\}$ and $F_1,\dots,F_4$ take $\{0,2\},\{2,1\},\{1,3\},\{3,0\}$. Allowed colors on $E_{AB}$ form the single $8$-cycle $0-c_2-3-c_1-1-c_4-2-c_3-0$ with exactly two perfect matchings $M_X, M_Y$. Rigorous.
  - *Claim 5:* By pigeonhole, two vertices $b_1, b_2 \in B$ share a matching (WLOG $M_X$). Any edge $\{b_r, c\} \in F_i$ ($i \in \{1..4\}$) completes the monochromatic broken $4$-cycle $(b_{3-r} - a_X(i) - b_r - c)$, contradiction. Hence all four edges between $\{b_1, b_2\}$ and $C = \{7, 8\}$ lie in $F_5$, forming a monochromatic $C_4$, contradiction. Rigorous.
- **Exact value $\zeta(G) = 6$:** Explicit $6$-coloring in lines 69–74 partitions all $24$ edges into $6$ strongly woody color classes.

## 3. Independent Mechanical Verification (PASS)
Audited and ran `targets/bartnicki-2303.08771-conj3/notes/check-check-3.py` (pure Python `int`, zero floats):
- Command: `.venv/bin/python -u targets/bartnicki-2303.08771-conj3/notes/check-check-3.py`
- Result: exit `0`, raw `PASS` (`col(G) = 5` via ordering + all $511$ nonempty induced subgraphs; explicit $6$-coloring verified across all $24$ edge contractions $G/e$; all $3292$ strongly woody color classes enumerated and verified against $G/e$; exact-cover search confirms $\zeta(G) > 5$ and $\zeta(G) = 6$).

## 4. Action Required for Re-Audit (Resolved)
Patch `Section 5` $\to$ `Section 3` in `TARGET.md` (lines 3, 12, 18) and `COUNTEREXAMPLE.md` (line 5), and record the published journal reference *Graphs and Combinatorics* **41** (2025), Art. 80 (`DOI: 10.1007/s00373-025-02934-5`, pp. 7–8) in `TARGET.md`, then re-ping `@audit-3` for immediate re-audit PASS.

## 5. Re-Audit Verdict (`2026-11-27T09:39Z`)
Verified `@scout-9`'s edits in `TARGET.md` (lines 3, 8, 12, 18, 32) and `COUNTEREXAMPLE.md` (line 5): all `Section 5` references are corrected to `Section 3`, and the open-access published journal citation (*Graphs and Combinatorics* **41** (2025), Art. 80, `DOI: 10.1007/s00373-025-02934-5`, pp. 7–8, Conjecture 3 retained verbatim, OpenAlex `W4411944715` with `cited_by_count = 0`) is properly recorded. All mathematics (Claims 1–5) and independent exact verification (`.venv/bin/python -u targets/bartnicki-2303.08771-conj3/notes/check-check-3.py`, raw `PASS`) remain intact.

**Verdict: PASS** (`"counterexample, verified by exact computation"`). Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final coordinator verification.

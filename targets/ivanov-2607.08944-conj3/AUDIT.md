# Blind Adversarial Audit Report: `targets/ivanov-2607.08944-conj3/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T10:06Z`
- **Verdict:** **PASS** (after re-audit of `#600` patch; initial audit at `10:06Z` was FAIL due to 0-based `\mathbf{e}_{3+j}` typo in 1-based notation on L34/L44/L45, now resolved — see §5)
- **Files Audited (strictly blind):** Primary source `tools/.arxiv_cache/eprint/2607.08944/main.tex` (`arXiv:2607.08944v1`), `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (`arXiv:2607.08944v1`)

- **Latest Version Check:** Live arXiv query (`tools/arxiv_fetch.py query --id-list 2607.08944`) confirms `2607.08944v1` (`2026-07-09`, Illya Ivanov, *"Illuminating Primitive Polytopes"*) is the sole version, with no journal ref or DOI.
- **Theorem Counter Check (`main.tex` L64–76):** `theorem`, `recap`, `lemma`, `proposition`, `conjecture`, `problem`, `corollary`, and `claim` share the single global `[theorem]` counter:
  1. Conjecture 1 (L215, Illumination Conjecture)
  2. Theorem 2 (`thm:fleanill`, L243)
  3. Theorem 3 (`thm:facleanposbas`, L263)
  4. Corollary 4 (`cor:flean_crit`, L267)
  5. Claim 5 (L291)
  6. **Conjecture 6 (`\label{conj:fleanverts}`, L310–312)**
- **Verbatim Match:** `TARGET.md` L14–15 and `COUNTEREXAMPLE.md` L6–7 match `main.tex` L310–312 verbatim: *"A primitive polytope in $\mathbb{E}^d, d\ge 4$ has at most $2^d$ vertices, even fewer if it isn't an affine $d$-cube."*

---

## 2. Blocking Defect Found

### Blocking Defect 1 — Wrong basis-vector index `\mathbf{e}_{3+j}` in 1-based coordinate notation (`COUNTEREXAMPLE.md` L34, L44, L45)

`COUNTEREXAMPLE.md` L15 fixes coordinates in $\mathbb{R}^{13}$ as $(x_1, x_2, x_3, y_0, y_1, \dots, y_9)$ and uses **1-based** standard basis vectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ for $(x_1, x_2, x_3)$ on L34–35. In this 1-based indexing, the coordinate $y_j$ ($j = 0, \dots, 9$) is coordinate $4 + j$, with basis vector **$\mathbf{e}_{4+j}$**, **not** $\mathbf{e}_{3+j}$:
- **L34:** Writes `$\sum_{j=0}^9 (\mathbf{e}_{3+j} + (-\mathbf{e}_{3+j} + \mathbf{e}_1 + \mathbf{e}_2 - j\mathbf{e}_3))$`, where at $j = 0$ the vector $\mathbf{e}_{3+0} = \mathbf{e}_3$ collides with the $x_3$-coordinate basis vector.
- **L44–45:** Lists the ray certificates for $y_j \le 1$ and $-y_j + x_1 + x_2 - j x_3 \le 119 + j^2$ ($j = 0, \dots, 9$) as $\mathbf{r} = +\mathbf{e}_{3+j}$ and $\mathbf{r} = -\mathbf{e}_{3+j}$. Evaluated literally at $j = 0$, $\mathbf{r} = +\mathbf{e}_3 = (0, 0, 1, \mathbf{0})$ fails the certificate condition for $y_0 \le 1$ ($\mathbf{a}_{y_0 \le 1} \cdot \mathbf{e}_3 = 0 \ngtr 0$ and $\mathbf{a}_3 \cdot \mathbf{e}_3 = +1 \nleq 0$).
- **Required fix:** Replace `\mathbf{e}_{3+j}` with `\mathbf{e}_{4+j}` (or equivalently `\mathbf{e}_{y_j}`) on L34, L44, and L45.

---

## 3. Non-Blocking Precision Items (Fix in the Same Patch)

1. **`COUNTEREXAMPLE.md` L36:** Before concluding that $\{\mathbf{a}_1, \dots, \mathbf{a}_{24}\}$ positively spans $\mathbb{R}^{13}$ (equivalently $\mathbf{0} \in \mathrm{int}\mathrm{conv}\{\mathbf{a}_i\}$) from $\sum_{i=1}^{24} \mu_i \mathbf{a}_i = \mathbf{0}$ ($\mu_i > 0$), explicitly note that $\{\mathbf{a}_i\}$ linearly spans $\mathbb{R}^{13}$ (since it contains all $13$ standard basis vectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf{e}_4, \dots, \mathbf{e}_{13}$).
2. **`COUNTEREXAMPLE.md` L59 (optional clarity):** Note briefly why every vertex of $P$ projects to a vertex of $P_x$ (because $L_j(x) \le y_j \le 1$ has affine endpoints in $x$, so a convex combination $x = \frac{1}{2}(x' + x'')$ in $P_x$ lifts to a convex combination in $P$), confirming $8704$ is the exact total vertex count (while already $\ge 8704 > 8192$ suffices for refutation).

---

## 4. Independent Verification of Underlying Counterexample

- **Polytope validity & primitivity:** Verified by hand and by running `.venv/bin/python targets/ivanov-2607.08944-conj3/notes/check-check-2.py` (exit code `0`, raw `PASS`, `FLOAT_CONSTANTS: 0`):
  - $\mathbf{0} \in \mathrm{int} P$ ($b_i > 0$ for all $24$ inequalities), $\mathrm{rank}(A) = 13$, and $\sum_{i=1}^{24} \mu_i \mathbf{a}_i = \mathbf{0}$ with $\mu = (1, 1, 56, 11, 1, \dots, 1) > \mathbf{0}$, so $P$ is a bounded $13$-polytope.
  - All $24$ ray certificates (with the true $y_j$-coordinate vectors $\pm \mathbf{e}_{4+j}$) satisfy $\mathbf{a}_i \cdot \mathbf{r}_i > 0$ and $\mathbf{a}_m \cdot \mathbf{r}_i \le 0$ ($m \neq i$), proving every single-facet spill is unbounded (so all $24$ halfspaces are irredundant facets, $P$ is primitive, and $24 < 26$ implies $P$ is not an affine $13$-cube).
  - Hand-checked all $24$ vertices of $P_x$: $2$ with $r(x) = 0$ (`(-300,100,100)` & reflection), $4$ with $r(x) = 1$ (`(20,100,100)`, `(-1699/10,100,-301/10)` & reflections), and $18$ with $r(x) = 2$ (`(20-m^2-m, 100, -2m-1)` for $m = 0,\dots,8$ & reflections, where $(120+j^2) - (x_1+x_2-jx_3) = (j-m)(j-m-1)$ vanishes iff $j \in \{m, m+1\}$), lifting to $2\cdot 2^{10} + 4\cdot 2^9 + 18\cdot 2^8 = 8704 > 8192 = 2^{13}$ distinct full-rank vertices of $P$.
- **Gate 2 receipts:** `notes/novelty-gate2-watch-{1,5,6}.md` all PASS.
- **Note on `notes/check-check-2.py`:** Script logic is 100% exact (`0` floats, uses 0-based `3 + j` consistently); docstring L4 says `Theorem 2` where `main.tex` has `Theorem 3` (`thm:facleanposbas`) — minor doc nit, no code change required.

---

## 5. Re-Audit Following `#600` Patch (`2026-11-27T10:16Z`) — **PASS**

Re-read `targets/ivanov-2607.08944-conj3/COUNTEREXAMPLE.md` in full:
- **Blocking Defect 1 (`COUNTEREXAMPLE.md` L34, L44, L45) — RESOLVED:** All three occurrences of `\mathbf{e}_{3+j}` were replaced with `\mathbf{e}_{4+j}` (matching 1-based $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ for $(x_1, x_2, x_3)$ and coordinates $(x_1, x_2, x_3, y_0, \dots, y_9)$).
- **Non-blocking item (`COUNTEREXAMPLE.md` L36) — RESOLVED:** Explicitly notes that $\{\mathbf{a}_i\}$ linearly spans $\mathbb{R}^{13}$ via the standard basis $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3, \mathbf{e}_{4+j}$ ($j = 0, \dots, 9$).
- **Independent Verifier (`notes/check-check-2.py`, unchanged):** Already executed cleanly (`exit 0`, `FLOAT_CONSTANTS: 0`, raw `PASS`: `Verified 24-facet primitive 13-polytope P: 24 P_x vertices, 8704 distinct full-rank vertices (> 2^13 = 8192).`).

**Final Verdict:** **PASS.** Ready for Gate 3 freshness check (`<1h`) before reporting.

---

## 6. Independent Lean 4 Statement-Fidelity Audit (`2026-11-27T12:01Z`) — **PASS**

- **Auditor:** `audit-3` (`auto`)
- **Lean Module:** `lean/OpenMath/Ivanov260708944Conj6.lean` (imported on L22 of `lean/OpenMath.lean`)
- **Charter Label:** `machine-checked counterexample in Lean 4`
- **Primary-Source Fidelity (`arXiv:2607.08944v1`, `main.tex` L237–238, L250, L254–269, L310–312):**
  - `dot`, `HRep`, `HRep.poly`, `HRep.polyOmit`, `IsBounded`, `HRep.HasNonemptyInt` ($\exists x_0, \forall i, a_i \cdot x_0 < b_i$, guaranteeing $x_0 \in \mathrm{int} P$), `HRep.IsPrimitive` (`HasNonemptyInt ∧ IsBounded poly ∧ ∀ i, ¬ IsBounded (polyOmit i)` — which automatically forces minimality/irredundancy of all $m$ facet halfspaces so every spill is unbounded, literally matching `main.tex` L237–238), and `IsVertex` (standard extreme-point definition) faithfully capture Ivanov's exact definitions with zero weakening or circularity.
  - `witnessHRep` encodes the exact 24 halfspaces in $\mathbb{R}^{13}$ (`x₁, x₂, x₃ ≤ 100`, `-x₁ - x₂ - x₃ ≤ 100`, `y_j ≤ 1`, `-y_j + x₁ + x₂ - j x₃ ≤ 119 + j²` for $j = 0, \dots, 9$).
  - `witness_isPrimitive`, `witness_has_8704_vertices`, `refutes_ivanov_conjecture_6` (`d = 13 ≥ 4`, `24` facets, `8704 > 2^13` distinct extreme points), and `not_ivanov_conjecture_6` directly refute Conjecture 6 (`\label{conj:fleanverts}`).
  - *(Minor non-blocking docstring nit: L25–26 mentions `|x_k| ≤ 1700` and `∑ μ_i a_i = 0`, whereas L392 directly proves `|v k| ≤ 2000` for boundedness — strictly equivalent and does not affect any formal statement or proof.)*
- **Type-Check & Axiom Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Ivanov260708944Conj6.lean`
  - Exit code: `0`, zero warnings, zero `sorry`/`admit`/`axiom`/`native_decide`/`unsafe`/`implemented_by`/`extern`.
  - `#print axioms` strictly `[propext, Classical.choice, Quot.sound]` for all 4 main theorems (`witness_isPrimitive`, `witness_has_8704_vertices`, `refutes_ivanov_conjecture_6`, `not_ivanov_conjecture_6`).

# Independent Blind Audit — `targets/lau-2208.14707-conj2/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:18Z`
- **Verdict:** **`FAIL`** *(1 blocking primary-source numbering defect: the conjecture is numbered **Conjecture 2.2** in both `arXiv:2208.14707v1` and the published *Discrete Math. Lett.* 11 (2023) article, not "Conjecture 2"; all mathematical content, independent verification, and Gate 2 receipts PASS)*

---

## 1. Blocking Issue to Fix (`TARGET.md` & `COUNTEREXAMPLE.md`)

- **Conjecture numbering mismatch (`Conjecture 2` -> `Conjecture 2.2`):**
  - Inspected verbatim BOTH the arXiv LaTeX/PDF (`tools/.arxiv_cache/eprint/2208.14707/A_note_on_local_antimagic_chromatic_number_of_lexicographic_product_graphs.{tex,pdf}`, preamble line 140 `\newtheorem{conjecture}{Conjecture}[section]`, Section 2, p. 8, lines 817 & 819) AND the published journal PDF (*Discrete Math. Lett.* 11 (2023), 76–83, `DOI:10.47443/dml.2022.149`, p. 82).
  - In **both** versions, the paper ends Section 2 with **Conjecture 2.1** and **Conjecture 2.2** — the target statement is **Conjecture 2.2** (not "Conjecture 2").
  - Also note for precision that the published *Discrete Math. Lett.* 11 (2023) p. 82 wording reads: *"Conjecture 2.2. For graphs $G$ and $H$, $\chi_{la}(G[H]) = \chi(G)\chi(H)$ if and only if $\chi(G)\chi(H) = 2\chi(H) + \lceil\frac{\chi(H)}{k}\rceil$, where $k \ge 1$ and $2k+1$ is the length of a shortest odd cycle in $G$."* (Mathematically identical to `arXiv:2208.14707v1` line 819.)
  - **Fix:** Update `Conjecture 2` to `Conjecture 2.2` in `TARGET.md` (lines 2, 14, 23) and `COUNTEREXAMPLE.md` (lines 1, 5, 41) (keeping the existing folder slug `targets/lau-2208.14707-conj2/` unchanged), and ping `@audit-2` for immediate re-audit PASS.

---

## 2. What Passed (No Rework Needed)

1. **Statement & Hypothesis Fidelity:** Verified verbatim against both `arXiv:2208.14707v1` and published *Discrete Math. Lett.* 11 (2023) 76–83 (`DOI:10.47443/dml.2022.149`). Both graphs $G = K_4$ and $H = K_2$ are disjoint connected simple non-null graphs with no extra restriction omitted from Conjecture 2.2. (Moreover, even under the paper's strictest Corollary 2.4 hypotheses of regular graphs with balanced even/odd incident labels on $H$, taking $G = K_4$ and $H = K_{2,2,2}$ yields $\chi_{la}(G[H]) = 12 = \chi(G)\chi(H) \neq 9$, confirming that $(K_4, K_2)$ does not exploit any hidden hypothesis.)
2. **Mathematical Audit (`COUNTEREXAMPLE.md`):**
   - Shortest odd cycle in $G = K_4$ is $C_3$ of length $3 = 2k + 1$, giving $k = 1 \ge 1$.
   - $\chi(K_4) = 4$, $\chi(K_2) = 2$, $\chi(K_4)\chi(K_2) = 8$.
   - $K_4[K_2] \cong K_8$ ($8$ vertices, $28$ edges), so $\chi_{la}(K_4[K_2]) \ge \chi(K_8) = 8$.
   - Hand-checked all 8 row sums of the explicit lexicographic bijection $f : E(K_8) \to \{1, \dots, 28\}$: $f^+(0) = 28$, $f^+(1) = 64$, $f^+(2) = 90$, $f^+(3) = 108$, $f^+(4) = 120$, $f^+(5) = 128$, $f^+(6) = 134$, $f^+(7) = 140$ — pairwise distinct, hence $\chi_{la}(K_4[K_2]) = 8 = \chi(K_4)\chi(K_2)$.
   - RHS: $2\chi(H) + \lceil \chi(H)/k \rceil = 4 + 2 = 6 \neq 8$, refuting the "only if" direction of Conjecture 2.2.
   - Infinite-family remark ($G = K_m, H = K_n$ for $m \ge 4, n \ge 2 \implies mn \ge 8 \ge 3$): verified that the lexicographic labeling gives strictly increasing vertex sums $f^+(0) < f^+(1) < \dots < f^+(mn-1)$ for all $mn \ge 3$.
3. **Independent Checker Re-run (`notes/check-check-2.py`):**
   - Command: `.venv/bin/python targets/lau-2208.14707-conj2/notes/check-check-2.py`
   - Exit code: `0`
   - Raw output: `PASS (G=K4, H=K2: k=1, chi(G)*chi(H)=chi_la(G[H])=8 != 2*chi(H)+ceil(chi(H)/k)=6)`
4. **Gate 2 Novelty Receipts:** Verified all three (`notes/novelty-gate2-watch-{1,5,6}.md`) — all **PASS**; additionally verified OpenAlex on published DOI `10.47443/dml.2022.149` returns `cited_by_count: 0`.

---

## 3. Handoff

Returned to `@scout-9` and `@triage` for the quick `Conjecture 2` -> `Conjecture 2.2` numbering fix in `TARGET.md` and `COUNTEREXAMPLE.md`. Ping `@audit-2` once updated for immediate re-audit PASS and Gate 3 handoff.

---

## 4. Re-Audit Verdict (`@audit-2`, `2026-11-27T09:22Z`) — **PASS**

Verified `@scout-9`'s fixes in `targets/lau-2208.14707-conj2/TARGET.md` (lines 2, 14, 23) and `COUNTEREXAMPLE.md` (lines 1, 5, 41): all references now accurately state **Conjecture 2.2** matching both `arXiv:2208.14707v1` (p. 8, line 819) and published *Discrete Math. Lett.* 11 (2023), pp. 76–83 (`DOI:10.47443/dml.2022.149`, p. 82).

All prior checks (explicit counterexample $(G, H) = (K_4, K_2)$, independent verifier `.venv/bin/python targets/lau-2208.14707-conj2/notes/check-check-2.py` raw `PASS`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) remain clear.

**Final Verdict: PASS** (label: `"counterexample, verified by exact computation"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.

---

## 5. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T11:58Z`) — **PASS**

- **Module audited:** `lean/OpenMath/Lau220814707Conj22.lean` (imported in `lean/OpenMath.lean` L18).
- **Primary-source & `COUNTEREXAMPLE.md` fidelity:** Verified verbatim against `tools/.arxiv_cache/eprint/2208.14707/A_note_on_local_antimagic_chromatic_number_of_lexicographic_product_graphs.tex` (`arXiv:2208.14707v1`, Abstract L208, §1 definitions L218–236, §2 Conjecture 2.2 L819; *Discrete Math. Lett.* 11 (2023), p. 82) and `COUNTEREXAMPLE.md`:
  - Graph definitions match primary source verbatim: `IsProperColoring`/`chromaticNumber` (L45–54), `HasCycleOfLen`/`IsShortestOddCycleLen` (L57–64, simple cycles of length $2k+1 \ge 3$ with $k \ge 1$), `lexProd` (L68–77, $V(G) \times V(H)$ with $(u, u') \sim (v, v') \iff u \sim_G v \lor (u = v \land u' \sim_H v')$), `vertexSum` / `IsLocalAntimagicLabeling` / `numColors` / `localAntimagicChromaticNumber` (L87–114), and exact rational ceiling `natCeilDiv a b := Nat.ceil ((a : ℚ) / (b : ℚ))` (L117–118).
  - Main theorems verified faithful:
    - `lexLabelK8_vertexSums` (L590–599): verifies all 8 exact vertex sums `(28, 64, 90, 108, 120, 128, 134, 140)` of the lexicographic `1..28` edge labeling on $K_8$.
    - `refutes_lau_conjecture_2_2_K4_K2` (L619–629): proves $K_4$ and $K_2$ are connected and non-null, `IsShortestOddCycleLen K_4 1`, $\chi(K_4) = 4$, $\chi(K_2) = 2$, $\chi_{la}(K_4[K_2]) = \chi(K_4)\chi(K_2) = 8 \ne 6 = 2\chi(K_2) + \lceil \chi(K_2)/1 \rceil$.
    - `refutes_lau_conjecture_2_2_infinite_family` (L643–651): establishes the full infinite family $(K_m, K_n)$ for all $m \ge 4, n \ge 2$.
    - `not_lau_conjecture_2_2` (L672–680): directly negates the universally quantified biconditional of Conjecture 2.2 over connected non-null finite simple graphs (no vacuous or weakened hypotheses).
- **Hygiene & kernel verification:**
  - Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or `set_option`.
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Lau220814707Conj22.lean` -> exit code `0`, zero warnings.
  - `#print axioms` on `lexLabelK8_vertexSums`, `refutes_lau_conjecture_2_2_K4_K2`, `refutes_lau_conjecture_2_2_infinite_family`, and `not_lau_conjecture_2_2`: strictly `[propext, Classical.choice, Quot.sound]`.
- **Verdict:** **PASS** (upgrades status label to `machine-checked counterexample in Lean 4`).

# Adversarial Audit Report (`audit-1`): `targets/vasilyev-2611.20344-q7.3/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Audited UTC:** `2026-11-27T14:02Z`
- **Target:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (2026-11-18, `updown.tex`), Section 7 (*Questions*), **Question 7.3** (`\label{q:types}`, lines 1991–1993; referencing **Remark 4.4** `\label{rem:types}`, lines 1134–1145).
- **Files Inspected (Strict Isolation):** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2611.20344/updown.tex` (live `arxiv.org/abs/2611.20344` confirmed `[v2]` is latest version). Author `verify.py` and scratch `notes/` were **not** read.
- **Verdict:** **PASS** (`"written proof, internally audited"`)

---

## 1. Primary-Source, Version, & Citation Fidelity — PASS

- Verified verbatim against `tools/.arxiv_cache/eprint/2611.20344/updown.tex` (`2611.20344v2`, latest on arXiv):
  - **Question 7.3** (`\label{q:types}`, L1991–1993): *"Is there a map with infinitely many cycles and a divergent orbit (Remark 4.4)?"* — matches `TARGET.md` and `PROOF.md` verbatim.
  - **Remark 4.4** (`\label{rem:types}`, L1134–1145): exact definition of equivalence of divergent orbits (eventually coinciding) and orbit type $(k, l)$ (number of cycles and classes of divergent orbits), explicitly stating *"We do not know whether a map can have infinitely many cycles and a divergent orbit (Question 7.3)."*
  - All compiled numbers verified against `\newtheorem{theorem}{Theorem}[section]` shared counters: `Lemma 2.1` (`lem:steps`), `Definition 2.2` (`def:G`), `Proposition 2.3` (`prop:dict`), `Remark 4.4` (`rem:types`), `Question 7.3` (`q:types`).
  - Confirmed $T_S$ is defined for arbitrary $S \subseteq \mathbb{N}$ ($\mathbb{N} = \{1, 2, 3, \dots\}$) with $U(x) = \lceil 3x/2 \rceil$, $D(x) = \lceil x/2 \rceil$, and divergent orbits correspond to rays (infinite simple paths in $G$, L169).
- **Gate 2 novelty clear:** Passed by `@watch-1` (`#1482`), `@watch-6` (`#1483`), and `@watch-5` (`#1485`) with receipts in `notes/novelty-gate2-watch-{1,5,6}.md`.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

Every step, modular congruence, inequality, loop termination argument, and global disjointness claim was checked line by line:

1. **§1 Elementary Properties (L16–29) — PASS:** $U(2m) = 3m$, $U(2m-1) = 3m-1$ strictly increasing/injective with $\mathrm{Im}(U) = \{z \ge 2 : z \not\equiv 1 \pmod 3\}$; $D$ non-decreasing with $D(x) < x$ for $x \ge 2$; admissible $D$-steps ($x \equiv 2 \pmod 6$) land at $x/2 \equiv 1 \pmod 3 \notin \mathrm{Im}(U)$.
2. **Lemma 1 (Closed-Box Trap Lemma, L34–62) — PASS:** For $B \ge 5$, $B \equiv 5 \pmod 6$, $C = (3B+1)/2$, we have $B+1 < C-1 < 2B < 3B-1$ (checked down to $B = 5$: $6 < 7 < 10 < 14$). Hypothesis (ii) gives $B+1 \in V(B) \ne \emptyset$. On $[B+1, 2B-1]$, $U(x) \in [B+2, 3B-1]$, $U(x) \notin R$ by (i), and $2B \equiv 1 \pmod 3 \notin \mathrm{Im}(U) \implies U(x) \ne 2B$. On $[2B+1, 3B-1]$, $D(x) \in [B+1, (3B-1)/2] = [B+1, C-1]$, avoiding $2B$ and avoiding $R$ by (ii). Since $x \ge 6 \ge 2$, $f_B(x) \ne x$; finite iteration in $V(B)$ yields a simple cycle $C(B)$ of length $\ge 2$ in $[B+1, 3B-1] \setminus R$.
3. **Lemma 2 (Admissible Ray $U$-Invariance, L65–69) — PASS:** $U(x) = r_t \ge 2 > r_0 = 1 \implies t \ge 1$; admissible $D$-steps land in $1 \pmod 3 \notin \mathrm{Im}(U)$, forcing $r_t = U(r_{t-1})$, so injectivity of $U$ yields $x = r_{t-1} \in R$.
4. **Lemma 3 (Admissible Stage Extension, L72–110) — PASS:**
   - **Phase 1:** $U^4(H) \ge \frac{81}{16} H > 5H \ge 25$, followed by $v_2(x_0)$ $U$-steps reaching odd $w_0 > 5H \ge 25$.
   - **Phase 2:** Exhaustive case split on odd $w > 25$: Case A ($w \equiv 3 \pmod 4$) and Case B ($w = 4k+1$, $k \ge 7$): Subcases B1 ($k \equiv 0 \pmod 4$), B2a/B2b ($k$ odd, $3k+1 = 2^e u$, $e \ge 1$, $\{3^e u, 3^{e+1} u\} \equiv \{1,3\} \pmod 4$, verifying $d = (3w+1)/4 > H$ and $B > y$ for both $e=1$ and $e \ge 2$), B3a ($k = 4q+2, q = 2r \ge 2$: $y=48r+14 \to d=24r+7 \to A=36r+11 \to B=54r+17 > y$), and B3b ($q$ odd: $w' = 36q+21 \equiv 1 \pmod 4$; $q \equiv 3 \pmod 4 \implies k' \equiv 0 \pmod 4$ enters B1 immediately; $q \equiv 1 \pmod 4 \implies q' = (9q+3)/4$ satisfies $4(5q'+3) = 9(5q+3)$ so $v_2(5q'+3) = v_2(5q+3) - 2$, guaranteeing termination in $\le \lfloor v_2(5q_0+3)/2 \rfloor$ iterations).
   - **Pairwise distinctness (Subcases B2b & B3a):** Clean backward induction using injectivity of $U$, $p_j \in \mathrm{Im}(U)$ ($1 \le j \le t_y$), $d > p_0$, and $d \notin \mathrm{Im}(U)$.
   - **Phase 3:** Two final $U$-steps from $C$ yield $H' = U^2(C) \ge \frac{27B+9}{8} > 3B$, with every prior vertex $\le B < C$, ensuring $P \cap [B+1, C-1] = \emptyset$ and $H' = \max(P) > 3B$.
5. **§3 Main Theorem (L114–137) — PASS:** Concatenating $P_0 = (1, 2, 3, 5)$ with Lemma 3 stages yields an admissible ray $R$ (disjoint intervals $[1, H_0]$ and $(H_{m-1}, H_m]$), global gap clearance $R \cap [B_m+1, C_m-1] = \emptyset$ for all $m \ge 1$, pairwise disjoint trap intervals $[B_m+1, 3B_m-1]$ (as $3B_m - 1 < H_m < B_{m+1}$), and explicit $S$ giving $T_S(r_t) = r_{t+1}$, $T_S|_{C(B_m)} = f_{B_m}$, and strict descent $T_S(x) = D(x) < x$ outside $W = R \cup \bigcup_{m \ge 1} C(B_m)$ (note $U(x) > x \ge D(x)$ ensures no ambiguity on $R$). Exact orbit type $(k, l) = (\infty, 1)$ proved cleanly.

---

## 3. Independent Exact Verification — PASS

- **Checker AST check:** `FLOATS: [] FLOAT_CALLS: []` on `targets/vasilyev-2611.20344-q7.3/notes/check-check-2.py`.
- **Executed checker:** `.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/notes/check-check-2.py` -> exit code `0`, raw output:
  - `[PASS] Primary source arXiv:2611.20344v2 verbatim match verified.`
  - `[PASS] Elementary U/D identities and Lemma 1 trap inequalities (B <= 600) verified.`
  - `[PASS] Lemma 3 exhaustive across H in [5, 10000] (counts={'A': 4995, 'B3a': 836, 'B2b': 1268, 'B2a': 1239, 'B1': 1658}, max_B3b_depth=4).`
  - `[PASS] 15-stage construction (H3=1182213), Lemma 1/2/3 invariants, 4 disjoint cycles (lengths=[43, 363, 10857, 35752]), and exhaustive T_S orbit classification for all x in [1, 1182213] (ray_basin=327659, cycle_basins=[680166, 157196, 17192]) verified.`
  - `PASS`

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Ready for Gate 3 freshness verification (`@watch-1`, `@watch-5`, `@watch-6`).

---

## 4. Independent Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27`) — PASS

- **Module:** `lean/OpenMath/Vasilyev261120344Q73.lean` (imported at `lean/OpenMath.lean` L28).
- **Primary-Source Fidelity (`tools/.arxiv_cache/eprint/2611.20344/updown.tex`, `arXiv:2611.20344v2`):**
  - `U x := (3 * x + 1) / 2` and `D x := (x + 1) / 2` match `Definition 1.1` (`def:TS`, L99, L106: $\lceil 3x/2 \rceil$ and $\lceil x/2 \rceil$ on $\mathbb{N}_+ = \{1, 2, 3, \dots\}$) identically for all even and odd $x \ge 1$.
  - `T S x := if x ∈ S then U x else D x` matches `eq:TS` (L102) verbatim; positivity `∀ x ∈ S, 1 ≤ x`, `1 ≤ x₀`, `1 ≤ cyc m`, and `∀ x ≥ 1` faithfully restrict to $\mathbb{N}_+$.
  - `IsPeriodicPoint`, `Orbit`, `IsDivergentOrbit` (injective forward orbit in $\mathbb{N}_+$, plus `Filter.Tendsto (fun t => (T S)^[t] 1) atTop atTop`), and `EventuallyCoincide` match `Remark 4.4` (`rem:types`, L1134–1145) and `Question 7.3` (`q:types`, L1991–1993) verbatim.
  - `vasilyev_question_7_3_orbit_type_infty_one` (L958–967) proves exact orbit type $(k, l) = (\infty, 1)$ (divergent orbit of $1$ tending to $+\infty$, infinitely many pairwise disjoint cycles of length $\ge 2$ all disjoint from `Orbit (T S) 1`, and complete dichotomy for all $x \ge 1$); `vasilyev_question_7_3` (L1138–1145) extracts the direct affirmative answer to Question 7.3.
- **Forbidden Token Audit:** `grep -nE "\b(sorry|admit|axiom|native_decide|unsafe|implemented_by|extern|set_option)\b"` returned `0` matches.
- **Standalone Lean 4 Verification:**
  - Command: `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Vasilyev261120344Q73.lean`
  - Result: `EXIT=0`, `0` warnings.
  - `#print axioms`: `closed_box_trap`, `admissible_stage_extension`, `vasilyev_question_7_3_orbit_type_infty_one`, `vasilyev_question_7_3` depend only on `[propext, Classical.choice, Quot.sound]` (`admissible_ray_U_inv` depends on `[propext, Quot.sound]`).
- **Lean 4 Audit Verdict:** **PASS** (eligible for upgrade to `"Lean-verified"`).

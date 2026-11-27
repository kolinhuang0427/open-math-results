# Adversarial Audit Report: `targets/oeis-A394511/`

- **Auditor:** `audit-1`
- **Verdict:** **PASS** (re-audited after `@scout-6` fixed the $k = 5$ inequality on `COUNTEREXAMPLE.md` L11 & L73)
- **Charter Label:** `"counterexample, verified by exact computation"`
- **Gate 3 Status:** Gate 3 Clear (`notes/novelty-gate3-watch-{1,5,6}.md`, all PASS; no `CONTESTED.md`)

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary source: OEIS `A394511` (`https://oeis.org/search?q=id:A394511&fmt=json`, rev `47`, `2026-06-06T04:04:55-04:00`), plus companion OEIS entries `A395802` (rev `16`), `A396859` (rev `6`), and GitHub check of `pexley-math` (`404`).
- `targets/oeis-A394511/TARGET.md`
- `targets/oeis-A394511/COUNTEREXAMPLE.md` (updated revision fixing L11 & L73)
- `targets/oeis-A394511/notes/check-check-3.md`
- `targets/oeis-A394511/notes/check-check-3.py`
- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` (and confirmed absence of `CONTESTED.md`).

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Primary-Source Statement Fidelity

- **Live OEIS `A394511` (rev `47`, `2026-06-06`):**
  - Name: *"Minimum number of cells in a connected enclosing shell of an n-cell connected hole on the truncated-square (4.8.8) Archimedean tiling."*
  - Comment: *"The 4.8.8 (truncated square) tiling has regular squares and octagons in a 1:1 ratio, symmetry group p4mm. For a connected n-cell hole H, the corona C(H) is the set of cells edge-adjacent to H but not in H. An enclosing shell S is a connected superset of C(H), disjoint from H, with the cells outside H union S also connected. a(n) is the minimum |S|."*
  - Conjecture (`_Peter Exley_`, Jun 05 2026): *"Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole, |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6, equivalently a(n) = a(n - 5) + 2 for n >= 11."*
  - Data (`offset 1`): 23 terms `4,8,8,8,8,10,10,10,12,12,12,12,12,14,14,14,14,14,16,16,16,16,16` (in particular `a(20) = 16`).
- **Match:** The coordinate edge-adjacency model $G_{4.8.8}$ (octagons $\mathrm{O}(x, y)$ adjacent orthogonally to $\mathrm{O}(x\pm 1, y), \mathrm{O}(x, y\pm 1)$ and diagonally to $\mathrm{S}(x,y), \mathrm{S}(x-1,y), \mathrm{S}(x,y-1), \mathrm{S}(x-1,y-1)$; squares $\mathrm{S}(i, j)$ adjacent exclusively to $\mathrm{O}(i+\alpha, j+\beta)$ for $\alpha,\beta \in \{0, 1\}$) matches the regular `4.8.8` tiling and OEIS `EXAMPLE`s (`n = 1, 2, 5`) verbatim.

---

## 3. Adversarial Mathematical & Computational Audit

- **Explicit finite counterexample ($H(3, 5)$):**
  - Connected hole $H(3, 5)$ has $3 \cdot 5 = 15$ octagons, $2 \cdot 4 = 8$ interior squares, and $2(2) + 2(4) = 12$ perimeter edge squares, totaling $n = 35$ cells.
  - Exact corona $S = C(H(3, 5))$ consists of $2(3) + 2(5) = 16$ side octagons and $4$ corner squares, totaling $|S| = 20$ cells forming a single closed cycle (hence connected and disjoint from $H(3, 5)$).
  - Exterior $E = V(G_{4.8.8}) \setminus (H \cup S)$ is connected: all exterior octagons form one connected component (the 4 corner octagons attach orthogonally to $\mathbb{Z}^2 \setminus [-1, 3] \times [-1, 5]$) and every exterior square touches at least one exterior octagon.
  - Therefore $a(35) \le 20 < 22 = 2\lceil (35 + 17)/5 \rceil$, directly refuting Exley's formula AND refuting the recurrence $a(n) = a(n - 5) + 2$ ($n \ge 11$) since $a(20) = 16$ from OEIS Data would force $a(35) = 22$.
  - Additional verified small counterexamples: $H(3, 5) \setminus \{\mathrm{O}(0,0)\}$ ($n = 34$, $|S| = 20 < 22$) and $H(4, 4)$ ($n = 37$, $|S| = 20 < 22$).
- **General rectangular family $H(R, C)$ ($R, C \ge 2$) & infinite family ($R = C = k \ge 4$):**
  - All 5 square subsets are pairwise disjoint for $R, C \ge 2$, giving $|H(R, C)| = 2RC + R + C - 3$ and $|C(H(R, C))| = 2R + 2C + 4$ with connected $H$, single-cycle corona $S = C(H)$, and connected infinite exterior $E$.
  - **Fix verified on L11 & L73:** For $R = C = k \ge 4$, $n_k = 2k^2 + 2k - 3$ gives $2\lceil (n_k + 17)/5 \rceil = 2\lceil (2k^2 + 2k + 14)/5 \rceil \ge \frac{4k^2 + 4k + 28}{5} > 4k + 4$, since $\frac{4k^2 + 4k + 28}{5} - (4k + 4) = \frac{4k^2 - 16k + 8}{5} = \frac{4(k-2)^2 - 8}{5} > 0$ for all $k \ge 4$ (at $k = 4$, $8/5 > 0$). **No gaps remain.**
- **Independent verifier re-execution:** Re-ran `.venv/bin/python -u /Users/kev/Documents/open-math/targets/oeis-A394511/notes/check-check-3.py`: exited with status `0`, outputting `PASS` (verified $G_{4.8.8}$ symmetry, $H(R, C)$ and $S(R, C)$ for all $2 \le R, C \le 10$, explicit counterexamples $n = 35, 34, 37$, OEIS `a(20) = 16` recurrence refutation, and infinite family inequality for $k = 4, \ldots, 1000$).

---

## 4. Novelty Status

- Live OEIS `A394511` rev `47` (`2026-06-06`) unchanged (`Conjectured (UNVERIFIED beyond n = 23)`). Companion OEIS `A395802` / `A396859` cover different tilings (`3.6.3.6` and `3.3.4.3.4`), and `pexley-math` GitHub user returns `404`.
- Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` all PASS; no `CONTESTED.md`.
- **Gate 3 receipts (all PASS, no `CONTESTED.md`):**
  - `targets/oeis-A394511/notes/novelty-gate3-watch-1.md` (`2026-11-27T06:56:00Z`, PASS): Sweep 19 snapshots, live OEIS `A394511` rev 47, Zenodo, and 14+ competing repos incl. `joaquimmj/oeis-conjectures` clear.
  - `targets/oeis-A394511/notes/novelty-gate3-watch-5.md` (`2026-11-27T06:49:04Z`, PASS): 542 snapshots, live OEIS rev 47, arXiv, Zenodo, `trureturing`, and 15 competing repos clear for `A394511`/`394511`.
  - `targets/oeis-A394511/notes/novelty-gate3-watch-6.md` (`2026-11-27T07:01:00Z`, PASS): 629 discovered repo snapshots (Sweep #7), live OEIS rev 47, live `trureturing`, and Zenodo clear.
- Ready for final report to `@coordinator` with label `"counterexample, verified by exact computation"`.


---

## 5. Lean 4 Statement-Fidelity Audit (`lean/OpenMath/OeisA394511.lean`)

- **Auditor:** `@audit-1`
- **Verdict:** **PASS** (statement-faithful, zero `sorry`/warnings, standard axioms only)
- **Imported in:** `lean/OpenMath.lean` (line 13: `import OpenMath.OeisA394511`)
- **Verification Command:** `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/OeisA394511.lean` -> exit code `0`, zero warnings, `#print axioms` output strictly `[propext, Quot.sound]` (`isConnectedSet_iff_induce_connected`) and `[propext, Classical.choice, Quot.sound]` (`SRect_isValidEnclosingShell`, `a394511_rect_le`, `a394511_35_le_20`, `not_exley_conjecture_formula`, `exley_infinite_family_refutation`, `not_exley_conjecture_recurrence`).
- **Statement-Fidelity Audit vs. Live OEIS `A394511` (rev. 47, `2026-06-06`):**
  - **Tiling graph (`G488`):** Exact edge-adjacency simple graph of the regular `4.8.8` truncated-square Archimedean tiling (`oct x y` orthogonally adjacent to `oct (x ± 1) y, oct x (y ± 1)` and diagonally to the 4 adjacent `sq i j`; `sq i j` adjacent exclusively to its 4 surrounding octagons; symmetry and irreflexivity proved).
  - **Connectivity (`IsConnectedSet`):** Proved equivalent (`isConnectedSet_iff_induce_connected`) to Mathlib's `(G488.induce A).Connected`.
  - **Corona & valid enclosing shell (`IsInCorona`, `IsValidEnclosingShell`):** Matches OEIS verbatim on all 5 clauses: `H` connected (`Finset Tile`), `S` connected (`Finset Tile`), `Disjoint H S`, `C(H) ⊆ S`, and `(H ∪ S)ᶜ` connected.
  - **Sequence definition (`a394511`) & `Nat.sInf` non-vacuity:** Defined as `sInf {k | ∃ H S, H.card = n ∧ IsValidEnclosingShell H S ∧ S.card = k}`. Every upper bound (`a394511_rect_le`, `a394511_35_le_20`, and `n = 261` in `not_exley_conjecture_recurrence`) exhibits an explicit valid finite witness `(HRect R C, SRect R C)`, so `sInf` is the genuine minimum of an inhabited set (no `sInf ∅ = 0` loophole).
  - **Refuted statements:**
    - `not_exley_conjecture_formula`: `¬ (∀ n : ℕ, 6 ≤ n → a394511 n = 2 * Nat.ceil (((n : ℚ) + 17) / 5))` (uses exact rational division in `ℚ` and `Nat.ceil`, matching `2*ceiling((n + 17)/5)` for `n >= 6` verbatim; witnessed by `n = 35`, `a394511 35 ≤ 20 < 22`).
    - `exley_infinite_family_refutation`: proves `6 ≤ 2*k^2 + 2*k - 3` and `a394511 (2*k^2 + 2*k - 3) < 2 * Nat.ceil ((((2*k^2 + 2*k - 3 : ℕ) : ℚ) + 17) / 5)` for all `k ≥ 4`.
    - `not_exley_conjecture_recurrence`: unconditionally proves `¬ (∀ n : ℕ, 11 ≤ n → a394511 n = a394511 (n - 5) + 2)` via `n = 261 = 11 + 5*50` (`a394511 261 ≤ 48 < 100 ≤ a394511 11 + 100`), matching OEIS `a(n) = a(n - 5) + 2 for n >= 11` verbatim without needing external OEIS data axioms.
  - **Minor docstring note (non-blocking):** Line 28 parenthetically remarks `S_rect R C` equals the exact corona of `H_rect R C`; the Lean code proves `C(H) ⊆ S` (`SRect_contains_corona`), which is the exact requirement of `IsValidEnclosingShell`.

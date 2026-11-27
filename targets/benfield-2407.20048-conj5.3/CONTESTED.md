# CONTESTED — `targets/benfield-2407.20048-conj5.3/` (Clause (v) Already Refuted in `the-omega-institute/trureturing#9448` / PR #9451)

- **Detected UTC:** `2026-11-27T09:04Z`
- **Watcher:** `watch-1` (Gate 2 novelty check)
- **Target Owner / Status:** `scout-11` / `candidate`
- **Competing Source Links:**
  - https://github.com/the-omega-institute/trureturing/issues/9448 (`closed`, `2026-09-22T08:35:06Z` -> `10:43:30Z`, PR #9451 merged at `708968483b4104bcc227cc4d65a0d40fccfdf930`)
  - https://github.com/the-omega-institute/trureturing/blob/main/Problems/pisano-order-range-refutation.md
  - Lean 4 module: `D5/S3/Arith/PisanoOrderRangeRefutation.lean` (`result : ¬ claim`, standard axioms)

## Exact Comparison Against `targets/benfield-2407.20048-conj5.3/`

- **Clause (v) ALREADY REFUTED (`2026-09-22`):**
  - `trureturing#9448` / `Problems/pisano-order-range-refutation.md` formally refutes Conjecture 5.3 clause (v) of `arXiv:2407.20048v2` (*"$\{0,1,2\}$ if $b \neq \pm 1$ and $|a|-|b| = 1$"*) in Lean 4 at $(a, b) = (3, 2)$, $m = 13$ ($\pi_{(3,2)}(13) = 12$, zeros at $0, 4, 8$, so $\omega_{(3,2)}(13) = 3 \notin \{0,1,2\}$).
  - `trureturing#9448` also identifies the same root-cause defect ($\pm 1$ roots of $x^2 - ax - b$ correspond to $|b|-|a|=1$ when $b>0$ rather than $|a|-|b|=1$) and numerically checks $(3,4)$ over $m \le 20000$ giving $\{0,1,2\}$.
- **Clause (vi) NOT SETTLED by `trureturing#9448`:**
  - `trureturing/Problems/pisano-order-range-refutation.md` explicitly notes: *"This settlement refutes clause (v) as published. It does not prove the corrected clause... supported here only by the measured ranges above, not by a proof."* It makes no formal claim or proof regarding clause (vi) (*"infinite in all other cases"*).
  - By contrast, Section 2 of `targets/benfield-2407.20048-conj5.3/COUNTEREXAMPLE.md` proves that for $(a, b) = (3, 4)$ (which falls under clause (vi)), $\omega_{(3,4)}(m) \in \{0, 1, 2\}$ for **all** $m > 1$ (exact range $\{0, 1, 2\}$), refuting clause (vi) directly.

Work on `targets/benfield-2407.20048-conj5.3/` must pause pending `@triage` / `@audit-*` ruling on whether to rescope strictly to clause (vi) with prior credit for clause (v).

---

## Auditor Contest Ruling (`audit-1`, `2026-11-27T09:08Z`)

- **Ruling:** **`partial-overlap-still-open`**
- **Strict Blindness:** Inspected ONLY `arXiv:2407.20048v2` (`fiborder.tex`, lines 690–750), `targets/benfield-2407.20048-conj5.3/TARGET.md`, `CONTESTED.md`, `the-omega-institute/trureturing#9448`, PR `#9451` (`Problems/pisano-order-range-refutation.md`, merged `2026-09-22`), and `tools/novelty_grep.py` across 605 snapshots. Did **not** read `COUNTEREXAMPLE.md`, `verify.py`, or any author/checker `notes/`.
- **Exact Clause-by-Clause Comparison:**
  1. **Conjecture 5.3 clause (v)** (*"$\{0,1,2\}$ if $b \neq \pm 1$ and $|a|-|b| = 1$"*): **`resolved-elsewhere`**. `the-omega-institute/trureturing#9448` / PR `#9451` (merged `2026-09-22`) formally refuted clause (v) in Lean 4 via $(a,b) = (3,2)$, $m = 13$ ($\pi_{(3,2)}(13) = 12$, $\omega_{(3,2)}(13) = 3 \notin \{0,1,2\}$). Must NOT be claimed as a new result and must be explicitly credited.
  2. **Conjecture 5.3 clause (vi)** (*"infinite in all other cases"*): **`STILL OPEN`**. In `fiborder.tex` L729–741, pairs such as $(a,b) = (3,4)$ (and all $b = a + 1$ with $a \ge 2$) satisfy $b \neq \pm 1$ and $|a| - |b| = -1 \neq 1$, so they fall strictly under **clause (vi)**. `trureturing#9448` / PR `#9451` explicitly restricted its settlement to refuting clause (v) (*"the rest of Conjecture 5.3 is untouched by this settlement"* and *"does not prove the corrected clause... supported here only by the measured ranges above, not by a proof"*, echoing the paper's own finite check $m < 20{,}000$ at L724). Proving finiteness of the range of $\omega_{(a,b)}(m)$ over **all** $m > 1$ for a clause-(vi) pair such as $(3,4)$ genuinely settles clause (vi) (and Conjecture 5.4 immediately following it) for the first time.
- **Required Action Before Audit:** `@scout-11` should rescope `TARGET.md` and `COUNTEREXAMPLE.md` strictly to **Conjecture 5.3 clause (vi)** (explicitly crediting `trureturing#9448` / PR `#9451`, `2026-09-22`, for prior refutation of clause (v) and dropping any novelty claim on clause (v)), then route through `@check-2` and blind audit (`@audit-1` remains blind).


---

## Subsequent External Settlement Notice (`watch-3`, `2026-11-27T13:47Z`)

- **Detected UTC:** `2026-11-27T13:46Z` (Sweep 10)
- **Watcher:** `watch-3`
- **Target Owner / Status:** `scout-11` / `reported` (committed in `f762d70` at `2026-11-27T09:19:50Z`, **~4h earlier** than the external commit below)
- **Competing Source Links:**
  - https://github.com/LuminaBench/solved-conjectures/tree/main/solves/missing-pisano-orders (commit `cb89a27373a88bdb9aeb4f0d8035806291d8d751`, `2026-11-27T13:23:29Z`)
  - https://github.com/LuminaBench/solved-conjectures/blob/main/solves/missing-pisano-orders/paper.tex
- **Exact Comparison Against `targets/benfield-2407.20048-conj5.3/`:**
  - **Prior / Timestamp Priority:** Our rescoped refutation of Conjecture 5.3 clause (vi) via $(a,b) = (3,4)$ ($\{\omega_{(3,4)}(m) : m > 1\} = \{0,1,2\}$) was committed and reported to `RESULTS.md` in `f762d70` at `2026-11-27T09:19:50Z`. LuminaBench's `solves/missing-pisano-orders/` was committed ~4h later at `2026-11-27T13:23:29Z`.
  - **Scope & Witness Comparison:** LuminaBench targets Conjecture 5.4 (formalizing in `Spec.lean` / `Proof.lean` `¬ (∀ a b : ℤ, b ≠ 1 → b ≠ -1 → |a| - |b| ≠ 1 → ∀ n : ℕ, 0 < n → Set.Infinite {m : ℕ | 0 < m ∧ f a b m = n})` via $(a,b) = (0,-2)$, which has unbounded zero counts omitting $n=2$), AND in Section 2 of `paper.tex` (*"A family with positive parameters"*) proves that for every $t \ge 2$, the positive case-(vi) pair $(a,b) = (t^2 - t, t^3)$ (starting at $(2,8)$) satisfies $\omega_{(a,b)}(m) \le 1$ for every modulus $m$, which also independently refutes Conjecture 5.3 clause (vi) (using a different witness family than our $(3,4)$).

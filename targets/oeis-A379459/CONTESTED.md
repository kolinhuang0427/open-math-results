# Partial Prior Resolution Notice — `targets/oeis-A379459/`

- **Detected UTC:** `2026-11-27T11:48:00Z` (by `watch-6` Sweep 6)
- **Target:** OEIS `A379459` (`rev. 4`) / `A379460` (`rev. 4`) / `A006351` (`rev. 195`) — claims three Kurkov conjectures:
  1. `A379459`: `A_459(n, 0) = A006351(n + 2)` (with `A_459(0, k) = 2*(k+1)!`)
  2. `A379460`: `A_460(n, 0) = A006351(n + 1)` (with `A_460(0, k) = 1`, `A(n, k) = A(n, k-1) + (k+1)*(A(n-1, k) + A(n-1, k+1))`)
  3. `A006351`: `a(n) = A379459(n-2, 0) = A379460(n-1, 0)` for `n > 1`.

## Prior Public Settlement of `A379460(n, 0) = A006351(n + 1)`

- **Repository:** `https://github.com/insorrowmeow/oeis-sequence-proofs`
- **Commit:** `62bc090`, committed **`2026-11-27T11:08:09Z`** (prior to target start `11:39:36Z`).
- **Exact Files:** `proofs/research-batch-09/YokeRows.md` (*The first column of the R-recursion for yoke-chains*, citing MathOverflow `481674`) and `proofs/research-batch-09/YokeRows.lean`.
- **Exact Comparison:** `YokeRows.lean` defines `next u 0 = u 0 + u 1`, `next u (q+1) = next u q + (q+2)*(u (q+1) + u (q+2))` from `rows 0 = fun _ => 1` — literally `A379460` — and proves `(1-y) F_{n+1} = G_n'` with `G_{n+1} = H G_n'`, yielding **`R(n, 0) = A006351(n + 1)`** for every `n >= 0`.

## Open Remainder

- **`A379459(n, 0) = A006351(n + 2)`** (and hence the `a(n) = A379459(n-2, 0)` half of `A006351`'s `FORMULA`) is **NOT** in `insorrowmeow/oeis-sequence-proofs` and remains open/novel.
- Recommend rescoping `targets/oeis-A379459/` strictly to **`A379459(n, 0) = A006351(n + 2)`** (explicitly citing `insorrowmeow/oeis-sequence-proofs` `YokeRows.{md,lean}` as prior settlement of `A379460(n, 0) = A006351(n + 1)`).

---

## Independent Contest Ruling (`@audit-2`, `2026-11-27T11:51Z`)

- **Ruling:** **`partial-overlap-still-open`**
- **Verbatim verification:** Inspected `insorrowmeow/oeis-sequence-proofs` commit `62bc0904513720ccfc9c27b08ec42de31ba695f4` (`2026-11-27T11:08:09Z`), specifically `proofs/research-batch-09/YokeRows.md`, `proofs/research-batch-09/YokeRows.lean`, `proofs/research-batch-09/A217061.md`, `proofs/research-batch-09/FactorialSweep.lean`, and `README.md` / repo tree:
  1. **`A379460(n, 0) = A006351(n + 1)` — `resolved-elsewhere`:** `YokeRows.md` + `YokeRows.lean` (citing MathOverflow `481674` without naming `A379460`) define the exact `A379460` recurrence from `rows 0 = fun _ => 1`, verify `(1-y) F_{n+1} = G_n'` and `G_{n+1} = H G_n'` in Lean 4 (zero `sorry`/`axiom`), and prove $R(n, 0) = \mathrm{A006351}(n+1)$ for all $n \ge 0$, committed 31 minutes before `targets/oeis-A379459/` started (`11:39:36Z`).
  2. **`A379459(n, 0) = A006351(n + 2)` — STILL OPEN:** Neither `YokeRows.{md,lean}` nor `A217061.md`/`FactorialSweep.lean` (which uses initial row $v_j = 1$ for `A379458`, not $2(k+1)!$) nor any other file in `insorrowmeow/oeis-sequence-proofs` mentions or settles `A379459(n, 0) = A006351(n + 2)` (nor the `a(n) = A379459(n-2, 0)` clause of `A006351`).
- **Action:** Hold Gate 3 / Gate 5. `@scout-6` must rescope `targets/oeis-A379459/{TARGET.md,PROOF.md}` strictly to **`A379459(n, 0) = A006351(n + 2)`** (and the `a(n) = A379459(n-2, 0)` half of `A006351`), crediting `insorrowmeow/oeis-sequence-proofs` (`62bc090`, `YokeRows.{md,lean}`) as prior settlement of `A379460(n, 0) = A006351(n + 1)` and dropping any novelty claim on `A379460`, then ping `@audit-2` for re-audit.

# Contest Ruling (`audit-1`): `targets/benfield-2407.20048-conj5.3/`

- **Date (UTC):** `2026-11-27T09:08Z`
- **Auditor:** `audit-1` (strictly blind — did NOT read `COUNTEREXAMPLE.md`, `verify.py`, or author/checker `notes/`)
- **Ruling:** **`partial-overlap-still-open`**

## Basis

1. **Primary source verified verbatim (`arXiv:2407.20048v2`, `fiborder.tex` L729–745):**
   - Conjecture 5.3 (`\label{finite-orders}`) gives a 6-part classification of the range of $\omega_{(a,b)}(m)$ ($m > 1$): clause (v) claims $\{0,1,2\}$ when $b \neq \pm 1$ and $|a| - |b| = 1$; clause (vi) claims **infinite in all other cases**.
2. **Competing publication verified verbatim (`the-omega-institute/trureturing#9448` / PR `#9451`, `Problems/pisano-order-range-refutation.md`, merged `2026-09-22`):**
   - **Clause (v) is `resolved-elsewhere`:** Lean 4 refutation at $(a,b) = (3,2)$, $m = 13$ ($\omega_{(3,2)}(13) = 3 \notin \{0,1,2\}$).
   - **Clause (vi) is `STILL OPEN`:** PR `#9451` explicitly states *"the rest of Conjecture 5.3 is untouched by this settlement"* and *"This settlement refutes clause (v) as published. It does not prove the corrected clause... supported here only by the measured ranges above, not by a proof."* No other snapshot in `watch/snapshots/**` (605 files) resolves `2407.20048` Conjecture 5.3 clause (vi).
   - Pairs such as $(a,b) = (3,4)$ satisfy $b = 4 \neq \pm 1$ and $|3| - |4| = -1 \neq 1$, falling strictly under clause (vi); proving a finite range of $\omega_{(3,4)}(m)$ for all $m > 1$ is a genuine universal refutation of clause (vi) (and of the subsequent Conjecture 5.4).
3. **Rescoping directive:** `@scout-11` may rescope `TARGET.md` and `COUNTEREXAMPLE.md` strictly to **Conjecture 5.3 clause (vi)** with explicit prior credit to `trureturing#9448` / PR `#9451` (`2026-09-22`) for clause (v) and no novelty claim on clause (v), then submit for independent check and blind audit.

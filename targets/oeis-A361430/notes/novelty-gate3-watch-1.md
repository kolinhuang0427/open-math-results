# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A361430/`

- **Checked (UTC):** `2026-11-27T11:01:08Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `636` files)
- **Result:** **PASS** — OEIS `A361430` (Kotesovec) and `A298826` (Oudra, Kotesovec, Schulte) conjectures remain unproved in OEIS and all checked literature/repos.
- **Audit Target:** `targets/oeis-A361430/AUDIT.md` (`@audit-1`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A361430" "A298826"`):**
   - `0` lines across `0/636` files (`1.25s`).
2. **Zenodo OEIS IDs Index (`grep -nE "A361430|A298826" watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`A361430` rev. `41`, `A298826` rev. `125`):**
   - `A361430` rev. `41` (`2026-07-05`) still marks `Conjecture: a(n) = abs(A298826(n)).`.
   - `A298826` rev. `125` (`2025-06-10`) still marks all three formulas (`Oudra` Nov 19 2019, `Kotesovec` Mar 12 2023, `Schulte` Jun 09 2025) as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=...` for `"A361430"`, `"A298826"`):**
   - `total: 0` for both.
5. **GitHub (`gh search issues/prs "A361430"`):**
   - `0` issues; `2` PRs (`hieplam/ai-dict#32` unrelated release; `mesuef1974/PVG-ANT-Central-Mind#65` inspected via `gh api`: closed unmerged PR merely observing an internal observable `I_1(n)` matches `A361430` — unrelated to `A298826` or Kotesovec/Schulte/Oudra conjectures).
6. **Web Search (`search_web`):**
   - `"A361430" OR "A298826" "Kotesovec" OR "Schulte" OR "Oudra" conjecture proof` — finds unrelated Schulte/Oudra conjectures (`A006472`, `A248186`), zero prior proof for `A361430`/`A298826`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.

# OEIS A347063: Refutation of Ianakiev's $18k + 12$ Double Zumkeller Conjecture

- **Source:** OEIS [A347063](https://oeis.org/A347063) (rev. 51, 2026-07-24T17:37:53-04:00), `COMMENT` section, submitted by Ivan N. Ianakiev (Oct 01 2024).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:07:08Z
- **Updated:** 2026-11-27T11:07:50Z
- **Identifiers:** `OEIS:A347063`, `OEIS:A348713`, `OEIS:A083207`

## Verbatim Conjecture Statement

From OEIS `A347063` (rev. 51, `NAME` and `COMMENT` sections):

> **NAME:** Double Zumkeller numbers: numbers whose set of divisors can be partitioned into two disjoint subsets with equal sums and equal cardinalities.
>
> **COMMENT:**
> - `It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]. - _Ivan N. Ianakiev_, Oct 01 2024`

*(Note: `A347063` also carries a separate `COMMENT` conjecture: `"Conjecturally, if y is a term of this sequence, then so is 2y."` Our refutation here targets Ivan N. Ianakiev's `18k+12` conjecture above; computationally we found 0 counterexamples to the `2y` closure conjecture among all 4,332 Double Zumkeller numbers $y \le 20000$.)*

## Gate 1 Novelty Receipt

- `watch/snapshots/` (`novelty_grep.py A347063`): `0` hits across `0/651` files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md` & `watch/snapshots/zenodo-23114921-oeis-ids.md`: `0` matches.
- `tools/arxiv_fetch.py query '"Double Zumkeller"'`: `0` results.
- `gh search code '"A347063"'`, `gh search repos "A347063 OR \"Double Zumkeller\""`, `gh search issues "A347063"`: `0` matches.
- Web search (`search_web`): no published proof or counterexample for `18k+12` or `3468` in `A347063`.
- `targets/`: no existing `targets/oeis-A347063` directory.

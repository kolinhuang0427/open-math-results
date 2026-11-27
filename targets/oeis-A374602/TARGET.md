# OEIS A374602: Subsequence Periodicity and Algorithm for Nearly Regular Pythagorean Hyperrectangles

- **Source:** OEIS [A374602](https://oeis.org/A374602) (rev. 31, 2024-11-15T23:31:14-05:00), Comments, plus linked sequences [A377290](https://oeis.org/A377290) (rev. 7) and [A377291](https://oeis.org/A377291) (rev. 7), submitted by Charles L. Hohn.
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T10:51:07Z
- **Updated:** 2026-11-27T11:35:00Z
- **Identifiers:** `OEIS:A374602`, `OEIS:A377290`, `OEIS:A377291`, `OEIS:A375336`, `OEIS:A373666`

## Verbatim Conjecture Statement

From OEIS `A374602` (rev. 31, `NAME` and `COMMENT` sections):

> **NAME:** Array of successive integer solutions to `sqrt((d-c)*b^2 + c*(b+1)^2)` for nonsquare integers `d >= 2` (`d=A000037(n)` for `n >= 1`), where `b` and `c` are positive integers and `c < d`, read by antidiagonals.
>
> **COMMENT:**
> - `T(n,k)` is the diagonal lengths of increasingly nearly regular `d`-dimensional Pythagorean hyperrectangles.
> - Each row `n` divides into equal length, geometrically periodic subsequences, each with its own subsequence period length (`A377290`) and geometric growth factor (`A377291`); it is conjectured that this is the case for all `n`, and that all solutions conform as such and that there are no solutions that do not, but these are not proven.
> - It is also not known if there is an algorithm for generating values for all rows other than testing all possible values for a row until a subsequence pattern emerges.

From OEIS `A377290` (`NAME` and `COMMENT`) and `A377291` (`NAME` and `FORMULA`):

> `A377290`: For each row `n` in array `A374602(n, k)`, the period size, as a count of terms, that divides the row into congruent subsequences.
> Here "congruent" means: 1) In the defining formula of `A374602`: `sqrt((d-c)*b^2 + c*(b+1)^2)`, `A374602(n, k)` and `A374602(n, k+a(n))` have equal `c` values (see Example), and also 2) `A374602(n, k+a(n))/A374602(n, k)` converges to a limit as `k->oo`, shown in `A377291`.

## Gate 1 Novelty Receipt

- `watch/snapshots/` (`novelty_grep.py A374602 A377290 A377291`): `0` lines across `0/635` files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`: `0` matches.
- `gh search code` (`"A374602"`, `"A377290"`, `"A377291"`): `0` matches.
- `gh search repos "A374602 OR A377290 OR Hohn"` & `gh search issues`: `0` matches.
- Web search (`search_web`): only references the OEIS entries themselves, stating the conjecture and lack of an algorithm remain open.
- `targets/`: no existing folder matching `374602`, `377290`, or `377291`.

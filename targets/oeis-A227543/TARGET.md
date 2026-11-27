# OEIS A227543: Mikhail Kurkov's Continued-Fraction Row-Recurrence Conjecture

- **Source:** OEIS [A227543](https://oeis.org/A227543) (rev. 113, 2026-10-03T19:42:30-04:00), `FORMULA` section, submitted by Mikhail Kurkov (Sep 26 2024).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:11:36Z
- **Updated:** 2026-11-27T11:12:10Z
- **Identifiers:** `OEIS:A227543`, `OEIS:A138158`, `OEIS:A047998`, `OEIS:A129182`

## Verbatim Conjecture Statement

From OEIS `A227543` (rev. 113, `NAME` and `FORMULA` sections):

> **NAME:** Triangle defined by g.f. `A(x,q)` such that: `A(x,q) = 1 + x*A(q*x,q)*A(x,q)`, as read by terms `k=0..n*(n-1)/2` in rows `n>=0`.
>
> **FORMULA:**
> `Conjecture: b(n) = P(n, n) where b(n) is an integer sequence with g.f. B(x) = 1/(1 - f(0)*x/(1 - f(1)*x/(1 - f(2)*x/(1 - f(3)*x/(1 - f(4)*x/(1 -...)))))), P(n, k) = P(n-1, k) + f(n-k)*P(n, k-1) for 0 < k <= n with P(n, k) = 0 for k > n, P(n, 0) = 1 for n >= 0 and where f(n) is an arbitrary function. In fact for this sequence we have f(n) = q^n. - _Mikhail Kurkov_, Sep 26 2024`

## Gate 1 Novelty Receipt

- `watch/snapshots/` (`novelty_grep.py A227543 "Mikhail Kurkov"`): `0` hits across `0/651` files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md` & `watch/snapshots/zenodo-23114921-oeis-ids.md`: `0` matches.
- `tools/arxiv_fetch.py query '"A227543"'` and `query 'au:Kurkov'`: `0` matches on `A227543` or continued fractions (only unrelated physics papers by M. A. Kurkov).
- `gh search code '"A227543"'` & `gh search repos "A227543 OR Kurkov"`: `0` matches. `gh search issues "A227543"`: only 1 open preregistration issue `#24510` on a different entry (`A140717`).
- Cross-referenced entries `A138158`, `A047998`, `A129182` and `search_web`: no proof of Kurkov's conjecture found.
- `targets/`: no existing `targets/oeis-A227543` directory.

# OEIS A379459 / A006351: Antidiagonal Array Equivalence for Series-Parallel Networks

- **Source:** OEIS [A379459](https://oeis.org/A379459) (rev. 4, `NAME` and `FORMULA` sections), submitted by Mikhail Kurkov (Dec 23 2024), and the `A379459` half of OEIS [A006351](https://oeis.org/A006351) (rev. 195, `FORMULA` section, Jan 16 2025).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:39:36Z
- **Updated:** 2026-11-27T11:54:00Z
- **Identifiers:** `OEIS:A379459`, `OEIS:A006351`

## Scope Note (Per `CONTESTED.md`)

OEIS `A006351` pairs `A379459` and `A379460` in `a(n) = A379459(n-2,0) = A379460(n-1,0)`. As recorded in `CONTESTED.md` (Sweep 6, `#1344`), the `A379460(n, 0) = A006351(n + 1)` equality was settled prior to our start in `insorrowmeow/oeis-sequence-proofs` (`62bc090`, `2026-11-27T11:08:09Z`, `proofs/research-batch-09/YokeRows.{md,lean}` via MathOverflow `481674`). This target is strictly scoped to the remaining open conjecture **`A379459(n, 0) = A006351(n + 2)`** ($n \ge 0$, equivalently `A006351(n) = A379459(n - 2, 0)` for $n > 1$).

## Verbatim Conjecture Statements

From OEIS `A379459` (rev. 4) and `A006351` (rev. 195):

> **A379459 NAME:** `Array read by downward antidiagonals: A(n,k) = A(n-1,k+1) + 2*(k+1)!*Sum_{j=0..k} A(n-1,j)/j! with A(0,k) = 2*(k+1)!, n >= 0, k >= 0.`
>
> **A379459 FORMULA:**
> `Conjecture: A(n,0) = A006351(n+2).`
>
> **A006351 NAME:** `Number of series-parallel networks with n labeled edges. Also called yoke-chains by Cayley and MacMahon.`
>
> **A006351 FORMULA:**
> `E.g.f. is reversion of 2*log(1+x)-x.`
> `Conjecture: a(n) = A379459(n-2,0) = A379460(n-1,0) for n > 1 with a(1) = 1. - _Mikhail Kurkov_, Jan 16 2025`
> *(Scoped here strictly to `a(n) = A379459(n-2,0)` for $n > 1$; `A379460(n-1,0) = a(n)` is prior-settled in `insorrowmeow/oeis-sequence-proofs` `YokeRows.{md,lean}`.)*

## Gate 1 Novelty Receipt

Checked at `2026-11-27T11:39:36Z`:
- `tools/novelty_grep.py A379459 --max-total 0` and `tools/novelty_grep.py A379460 --max-total 0` -> `0` hits across `0/658` snapshot files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`, `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, and `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) -> `0` hits.
- Zenodo API (`zenodo.org/api/records?q=A379459`, `q=A379460`) -> `0` hits.
- arXiv API (`all:A379459`, `all:A379460`) -> `0` results.
- GitHub code/issues (`gh search code`, `gh search issues`) -> `0` math code hits; only open preregistration `the-omega-institute/trureturing#27785` (`state: open`, `comments: 0`, explicitly stating no proof is included).
- Web search -> returns only the OEIS pages.

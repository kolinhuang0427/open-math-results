---
source: https://oeis.org/A061313 (rev. 2026-11-01), https://oeis.org/A007305, https://oeis.org/A007306
status: reported
owner: scout-6
updated: 2026-11-27T01:40:00Z
identifiers: [A061313, A007305, A007306, Hirzebruch continued fraction, Andrei Zabolotskii]
---

# Target: OEIS A061313 (Zabolotskii 2020 Hirzebruch Continued Fraction Conjecture)

## Verbatim Statement
From OEIS **A061313** (author: `_Henry Bottomley_`, Jun 06 2001; latest revision `2026-11-01T16:49:49-05:00`):

- **Name:**
  > Minimal number of steps to get from 1 to n by (a) subtracting 1 or (b) multiplying by 2.
- **Formula:**
  > a(2n) = a(n)+1; a(2n+1) = a(n+1)+2; a(1) = 0.
- **Comment (Conjecture):**
  > Conjecture: a(n)+2 is the sum of the terms of the Hirzebruch (negative) continued fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n). - _Andrei Zabolotskii_, Apr 17 2020

Cross-references:
- `A007305` (`offset 0`): Numerators of Farey (or Stern-Brocot) tree fractions: `0, 1, 1, 1, 2, 1, 2, 3, 3, ...`.
- `A007306` (`offset 0`): Denominators of Farey tree fractions (the Stern-Brocot subtree in `[0, 1]`): `1, 1, 2, 3, 3, 4, 5, 5, 4, ...`.

**Scope note on $n = 1$:** For all $n \ge 2$, $r(n) = \mathrm{A007305}(n)/\mathrm{A007306}(n) \in (0, 1)$ has canonical Hirzebruch continued fraction $[[1; c_1, \dots, c_k]]$ ($c_i \ge 2$), and the conjecture holds unconditionally. At $n = 1$, $r(1) = 1/1$ has canonical Hirzebruch continued fraction $[[1]]$ (sum $1$), whereas $a(1) + 2 = 2$; this boundary exception is proved explicitly alongside the universal $n \ge 2$ theorem.

## Gate 1 Novelty Receipt
- Checked at: `2026-11-26T23:08:00Z` – `23:16:08Z`
- `watch/snapshots/` (`tools/novelty_grep.py A061313`): `0` hits across `333` files.
- `tools/arxiv_fetch.py query "all:A061313"`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A061313+OR+%22Zabolotskii%22&size=5`): `3` hits (`zenodo.20634736`, `zootaxa.1763.1.2`, `zenodo.24161984`), none on `A061313`.
- GitHub code search (`gh search code A061313` in general + `aliromman/math`, `trureturing`, `joaquimmj/oeis-conjectures`, `1337isnot1337/solved-conjectures`): only `joeis`, `loda-programs`, and programming challenge implementations of `A061313`; `0` results in the competing math repos.
- Web search (`"A061313" "Hirzebruch" OR "Zabolotskii" "Stern-Brocot"`): surfaces only OEIS `A061313` and companion `A008687`; no published proof found.
- OEIS `A061313` and `A008687` checked live (`2026-11-26`): both comments remain marked `Conjecture:`.
- Not covered: closed-access venues not indexed by arXiv/Zenodo/web.

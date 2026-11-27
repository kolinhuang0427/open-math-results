# OEIS A215041: Normalized Discriminant Quotient of Minimal Polynomials of $2\cos(\pi/n)$

- **Source:** OEIS [A215041](https://oeis.org/A215041) (rev. 10), `FORMULA` section, and Wolfdieter Lang, *The field $\mathbb{Q}(2\cos(\pi/n))$, its Galois group and length ratios in the regular $n$-gon*, `arXiv:1210.1018` (`ArXivngonGalois2017.tex`, Mar 2017, §3 L541–555 and Open Problems L928).
- **Status:** reported
- **Owner:** scout-6
- **Started:** 2026-11-27T11:18:11Z
- **Updated:** 2026-11-27T11:32:00Z
- **Identifiers:** `OEIS:A215041`, `OEIS:A193681`, `OEIS:A187360`, `OEIS:A193679`, `OEIS:A055034`

## Verbatim Conjecture Statement

From OEIS `A215041` (rev. 10, `NAME` and `FORMULA` sections):

> **NAME:** `a(n) = n^degree(C(n,x))/discriminant(C(n,x))` for the minimal polynomials `C(n,x)` of `2*cos(Pi/n)`, given in `A187360`.
>
> **FORMULA:**
> `a(n) = (n^delta(n))/Discriminant(C(n,x)), n>=1, with the minimal polynomials C(n,x) of 2*cos(Pi/n), with coefficient triangle given in A187360, and their degree delta(n) given in A055034(n).`
> `a(1) = 1. Conjectures for a(n), n>=2:`
> `i) a(2^k) = 2, k>=1;`
> `ii) a(p^k) = p^((p^(k-1)+1)/2), for odd prime p and k>=1;`
> `iii) a(n) = product(p^(delta(n)/(p-1)), odd p|n) otherwise.`

Equivalently, from `arXiv:1210.1018` (`ArXivngonGalois2017.tex` L542–550 & L928, listed under **Open problems**):
> `o) q(1) = 1 (clear).`
> `i) If n = 2^k for k in N then q(n) = 2.`
> `ii) If n = p^k for odd prime p and k in N then q(n) = p^{(p^{k-1}+1)/2}.`
> `iii) if n = 2^{k_2} p(i_1)^{k_{i_1}} ... p(i_N)^{k_{i_N}} ... then q(n) = \prod_{odd p | n} p^{\delta(n)/(p-1)}.`

## Gate 1 Novelty Receipt

- `watch/snapshots/` (`novelty_grep.py A215041`): `0` lines across `0/651` files.
- `watch/snapshots/zenodo-23112421-oeis-ids.md` & `zenodo-23114921-oeis-ids.md`: `0` matches.
- `tools/arxiv_fetch.py query '"A215041" OR "A193681"'`: `0` results (`arXiv:1210.1018` lists the conjecture as Open Problem #1).
- `gh search code '"A215041"'`, `gh search repos "A215041"`, `gh search issues "A215041"`: `0` matches.
- OEIS `A215041` (rev. 10), `A193681` (rev. 24), `A187360` (rev. 56), `A193679` (rev. 31), and `search_web`: no published proof found.
- `targets/`: no existing `targets/oeis-A215041` directory.

# Independent Check Report: targets/chervov-2509.19162-conj9/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary sources checked:**
  - `arXiv:2509.19162v2` (`2026-04-01T15:54:42Z`, latest version of 2), *"CayleyPy Growth: Efficient growth computations and hundreds of new conjectures on Cayley graphs (Brief version)"*, cached TeX source `tools/.arxiv_cache/eprint/2509.19162/mainv2.tex`.
  - Live OEIS JSON API for `A136184` (revision `31`: *"Number of metacyclic groups of order 2^n"*, Data starts `1,2,4,8,12,19,26,37,48,...`).
- **Exact conjecture match:**
  - `mainv2.tex` Subsection `"Bounds on the diameters of unitriangular groups"` (lines 2203–2231), 9th `\begin{Conj}` environment (lines 2229–2231):
    > The diameter of $U(n,\mathbb{Z}/2\mathbb{Z})$ with respect to the fundamental root transvections is equal to the number of metacyclic groups of order $2^n$ (\href{https://oeis.org/A136184}{OEIS A136184}).
- **Fidelity:** `TARGET.md` and `COUNTEREXAMPLE.md` (with line 100 corrected from `62943` to `63470` by `@scout-12`) match `arXiv:2509.19162v2` and OEIS `A136184` rev 31 verbatim.

## 2. Independent Mechanical Check

- Independently wrote `targets/chervov-2509.19162-conj9/notes/check-check-3.py` (strictly without reading `verify.py` or `notes/*`), verifying:
  - **Part 1 (`diam(U(n, F_2)) <= 2n^2 - 6n + 5`):** Exhaustive BFS confirms diameters `1, 4, 8, 12` for `n = 2..5` (`n = 2` already fails: `1 < 2 = M(2)`); constructive word factorization verified on all matrices in `U(n, F_2)` for `n = 2..5` and stressed on random matrices up to `n = 176`.
  - **Part 2 (`F_n` metacyclic family):** Direct finite-group multiplication law, `(C*r) % A == C % A` (including split `c = a`), center $Z(G)$, commutator subgroup $G'$, and invariant-factor distinctness verified directly for `n = 6, 7, 8`.
  - **Part 3 (`|F_n| > 2n^2 - 6n + 5`):** Exact sums confirm $|\mathcal{F}_{176}| = 61404 > 60901 = 2(176)^2 - 6(176) + 5$, $|\mathcal{F}_{178}| = 63470 > 62305$ (matching `COUNTEREXAMPLE.md` L100), $|\mathcal{F}_n| > 2n^2 - 6n + 5$ for all `178 <= n <= 500`, and the `n >= 195` algebraic lower bound (`15m^2 - 65m + 54 > 0`, sum identity, and `n^3 - 195n^2 + 579n - 481 > 0`).

- **Command run:**
```bash
.venv/bin/python -u targets/chervov-2509.19162-conj9/notes/check-check-3.py
```

- **Raw output:**
```text
Part 1 PASS: exact BFS diam(U(2..5,F_2))={1,4,8,12} and word factorization <= 2n^2-6n+5 verified up to n=176.
Part 2 PASS: metacyclic group laws, Z(G), G', and invariant-factor distinctness verified on n=6,7,8.
Part 3 PASS: |F_176|=61404 > 60901, |F_n| > 2n^2-6n+5 for 178<=n<=500, and n>=195 algebraic bound verified.
PASS
```

# Independent Check Report: targets/daugherty-2610.29291-conj6.1/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - `arXiv:2610.29291v1` (`2026-10-21T06:45:39Z`, sole version), *"Counting and constructing Latin tableaux"* by Spencer Daugherty, Michaela Fahnestock, Shawn Huxtable, Michael Larson, Nourah Al Munayes, and Storey Peacock, cached TeX source `tools/.arxiv_cache/eprint/2610.29291/final.tex`.
- **Exact conjecture & definition match:**
  - Section 6 (`\section{Open problems}`), lines 717–719, Conjecture 6.1 (`\label{conj:box}`):
    > If $\lambda$ and $\mu$ are wide partitions where $\lambda_i = \mu_i + 1$ for some $i\in [\ell(\lambda)-1]$ and $\lambda_j=\mu_j$ when $j \not=i$, then $LT(\lambda) \geq LT(\mu)$.
  - Wide partition definition (Section 2, lines 256–265, 302–304): $\lambda$ is *wide* iff $\nu \succeq \nu'$ for every subpartition $\nu \subseteq \lambda$ (deleting any subset of rows; equivalently every lower subpartition), where $\succeq$ is dominance order ($\sum_{j=1}^k \nu_j \ge \sum_{j=1}^k \nu'_j$).
  - Latin tableau definition (Section 2, lines 306–310; Section 4, line 520): a diagram of shape $\lambda$ filled with integers such that $i$ appears $\lambda'_i$ times (type $\lambda'$, equivalently row $i$ contains $1$ through $\lambda_i$) and each integer appears at most once in any row or column; $LT(\lambda)$ is the number of such tableaux.
  - Note: Line 721 of `final.tex` explicitly discusses the exact pair $\mu = (6,5,5,3,2,1)$ and $\lambda = (6,5,5,3,3,1)$ (with $n = 22 \to 23$, $i = 5$), right after line 715 notes computational verification only up to $n \le 22$.
- **Fidelity:** `TARGET.md` and `COUNTEREXAMPLE.md` match `arXiv:2610.29291v1` verbatim with zero quantifier, hypothesis, or definition drift.

## 2. Independent Mechanical Check

- Independently wrote `targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py` (strictly without reading `verify.py`) directly implementing:
  - Exhaustive wideness over all $2^{\ell(\lambda)} - 1$ non-empty subpartitions (all row subsets, not only lower subpartitions).
  - Exact memoized backtracking enumeration `count_latin_tableaux(lam)` directly enforcing Definition 2.5 (type $\lambda'$, no row repeats, no column repeats).
- Verified sanity checks from `final.tex` ($LT((3,2))=6$, $LT((4,4,2,1))=12$, $LT((4,4,2,2))=8$, $LT((3,3,2))=4$, $LT((4,4,3,1))=40$, $LT((5,4,4,3,1))=32$) and all three counterexample pairs in `COUNTEREXAMPLE.md`:
  - Main counterexample ($i = 5 \in [5]$): $\mu = (6,5,5,3,2,1)$ (wide, $LT(\mu) = 56$) $\to \lambda = (6,5,5,3,3,1)$ (wide, $LT(\lambda) = 32 < 56$).
  - Additional pairs ($i = 5 \in [5]$): $(6,6,4,3,2,1)$ ($88$) $\to (6,6,4,3,3,1)$ ($64$) and $(6,6,5,3,2,1)$ ($2080$) $\to (6,6,5,3,3,1)$ ($1984$).

- **Command run:**
```bash
.venv/bin/python targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py
```

- **Raw output:**
```text
Sanity checks PASS: paper's examples (3,2), (4,4,2,1)->(4,4,2,2), (3,3,2), (4,4,3,1)->(5,4,4,3,1) match.
Pair PASS: mu=(6, 5, 5, 3, 2, 1) (wide, LT=56) -> lam=(6, 5, 5, 3, 3, 1) (wide, LT=32) at i=5
Pair PASS: mu=(6, 6, 4, 3, 2, 1) (wide, LT=88) -> lam=(6, 6, 4, 3, 3, 1) (wide, LT=64) at i=5
Pair PASS: mu=(6, 6, 5, 3, 2, 1) (wide, LT=2080) -> lam=(6, 6, 5, 3, 3, 1) (wide, LT=1984) at i=5
PASS
```

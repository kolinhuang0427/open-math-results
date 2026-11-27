# Check Report: `targets/oeis-A124380/` (`@check-1`)

- **Verdict:** **PASS**
- **Primary Source:** Live OEIS `A124380` (`rev. 39`, Oct 22 2025, `fmt=text`).
- **Verifier Script:** `targets/oeis-A124380/notes/check-check-1.py` (exact Python `int` + zero-float `mpmath.iv` at `dps = 30`, built directly from OEIS OGF and `PROOF.md` without reading `verify.py` or author `notes/`).

## 1. Primary Source & Statement Verification
- `TARGET.md` and `PROOF.md` match live OEIS `A124380` rev. 39 (`%N` O.g.f. $\sum_{n \ge 0} x^n \prod_{k=0}^n (1+kx)$, `%S/%T/%U` $n=0..29$, `%F` Kotesovec Sep 18 2024 conjecture) verbatim.
- Elementary symmetric representation $a(n) = \sum_{r=0}^{\lfloor n/2 \rfloor} e_r(1,\dots,n-r)$, Lemma 1 factorial bounds ($k! \le a(n) \le (k+1)(2k+1)^{3e(2k+1)^{3/4}+2}k!$), and Section 3 $\log(k!)$ integral comparison and asymptotic proof verified line by line.

## 2. Independent Exact & Interval Verification
Ran `.venv/bin/python -u targets/oeis-A124380/notes/check-check-1.py` (`FLOATS: []`, exit code `0`, `PASS`):
- Exact OGF $A(x)$ coefficients match OEIS `%S/%T/%U` ($n = 0..29$).
- Section 1 identity $a(n) = \sum_{r=0}^{\lfloor n/2 \rfloor} e_r(1,\dots,n-r)$ verified for all $n = 0..160$.
- Lemma 1 termwise & final factorial bounds and Section 3 $\log(k!)$ integral sandwich verified in exact `int` + `mpmath.iv` (`dps = 30`) for all $n = 4..160$.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`watch-1` pending).

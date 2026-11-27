# Blind Audit Report: `targets/oeis-A188648/` (`@audit-2`)

**Verdict: PASS**

---

## 1. Primary Source & Statement Fidelity

- **Primary source verified live:** `https://oeis.org/search?q=id:A188648&fmt=json` (OEIS `A188648`, **revision 46**, `2022-09-06T04:25:16-04:00`).
- **Verbatim check against `TARGET.md`:**
  - `NAME`: `Binomial sums a(n) = Sum_{k=0..n} (binomial(2n-k,k))^2.` — exact match.
  - `OFFSET`: `0,2` — exact match.
  - `DATA`: all 21 terms `a(0) = 1` through `a(20) = 4069232436916151` — exact match.
  - `FORMULA` (Velin Yanev, Oct 31 2019): `Conjecture: a(n) = hypergeom([-n,-n,n+1,n+1], [1/2,1/2,1], 1/16). - _Velin Yanev_, Oct 31 2019` — exact match.

---

## 2. Line-by-Line Proof Verification (`PROOF.md`)

- **Termination (L12–14):** Since $-n \in \mathbb{Z}_{\le 0}$, $(-n)_k = 0$ for all $k > n$, while $(1/2)_k$, $(1)_k = k!$, and $k!$ are strictly positive for all $k \ge 0$; thus the ${}_4F_3$ series terminates cleanly at $k = n$ for every $n \ge 0$.
- **Numerator & denominator simplification (L16–26):** For every $0 \le k \le n$:
  - $(-n)_k(n+1)_k = (-1)^k \frac{n!}{(n-k)!}\cdot\frac{(n+k)!}{n!} = (-1)^k\frac{(n+k)!}{(n-k)!}$ (including $k = 0$).
  - $(1/2)_k k! 4^k = \frac{(2k-1)!!}{2^k} \cdot k! \cdot 2^k \cdot 2^k = (2k-1)!!(2k)!! = (2k)!$ (including $k = 0$ with $(-1)!! = 0!! = 1$).
  - Squaring and using $(1)_k = k!$ and $4^{2k} = 16^k$ gives the $k$-th summand $\binom{n+k}{2k}^2 = \binom{n+k}{n-k}^2$ (valid since $0 \le 2k \le n+k$).
- **Reindexing (L28–29):** Substituting $j = n - k$ ($0 \le j \le n$) yields $\sum_{j=0}^n \binom{2n-j}{j}^2 = a(n)$ for all $n \ge 0$ (including $n = 0$: $1 = 1$). **PASS.**

---

## 3. Independent Verification & Gate 2 Novelty

- **Checker script:** Re-ran `.venv/bin/python -u targets/oeis-A188648/notes/check-check-3.py` — `exit 0`, raw output `PASS`, AST `FLOAT_CONSTANTS: 0` (exact `int`/`Fraction` check of all 21 OEIS `DATA` terms, termination at $k=n+1$, termwise match, and full sum for $0 \le n \le 30$).
- **Zenodo & Gate 2 receipts:** Independently verified `0` hits for `A188648` in `watch/snapshots/zenodo-23112421-oeis-ids.md`; all three Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) PASS.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

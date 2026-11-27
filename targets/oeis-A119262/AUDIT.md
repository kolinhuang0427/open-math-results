# Adversarial Audit Report (`audit-1`): `targets/oeis-A119262/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A119262` — Benedict W. J. Irwin (Apr 19 2017) Hessenberg determinant conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and live OEIS `A119262` (rev. 55, `2026-02-23T22:55:40-05:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A119262` JSON (rev. 55, `2026-02-23T22:55:40-05:00`, offset `0,5`):
  - `NAME`: `Number of B-trees of order infinity with n leaves, where a(n) = Sum_{k=1..floor(n/2)} a(k)*C(n-k-1,n-2*k) for n >= 2, with a(0)=0, a(1)=1.`
  - `FORMULA`: `Conjecture: Let M_n be an n X n matrix whose elements are m_ij = 0 for i < j - 1, m_ij = -1 for i = j - 1, and m_ij = binomial(i - j, n - i) otherwise. Then a(n + 1) = Det(M_n). - _Benedict W. J. Irwin_, Apr 19 2017`
  - Scoped unambiguously to Irwin's Apr 19 2017 determinant conjecture (1-indexed $1 \le i, j \le n$, verified at $n = 1, 2, 3$ and against all 29 OEIS terms $a(0..28)$).

## 2. Line-by-Line Mathematical Audit
- **Step 1 (`PROOF.md` L21–36):** Reversing row and column orders via $r = n - i, c = n - j \in \{0, \dots, n-1\}$ produces $B_n = P_n M_n P_n^{-1}$ with $\det(M_n) = \det(B_n)$ and $n$-independent entries $b_{r,c} = 0$ ($r > c + 1$), $-1$ ($r = c + 1$), $\binom{c-r}{r}$ ($r \le c$), making $B_n$ the leading $n \times n$ principal submatrix of a single infinite upper-Hessenberg matrix $B$. Exact.
- **Step 2 (`PROOF.md` L38–53):** Expanding $d_n := \det(B_n)$ ($d_0 := 1$) along column $c = n - 1$ gives cofactor signs $(-1)^{(r+1)+n} = (-1)^{r+(n-1)}$; each minor $B_n^{(r, n-1)}$ is block upper-triangular with top-left block $B_r$ (det $d_r$) and bottom-right $(n-1-r) \times (n-1-r)$ upper-triangular block with diagonal entries $-1$ (det $(-1)^{n-1-r}$), including boundary cases $r = 0$ and $r = n - 1$. Signs cancel ($(-1)^{2(n-1)} = 1$), yielding $d_n = \sum_{r=0}^{n-1}\binom{n-1-r}{r} d_r$ for all $n \ge 1$. Exact.
- **Step 3 (`PROOF.md` L55–60):** Truncating at $r \le \lfloor(n-1)/2\rfloor$ (since $0 \le n - 1 - r < r$ otherwise), reindexing $k = r + 1 \in \{1, \dots, \lfloor(n+1)/2\rfloor\}$, and applying $\binom{n-k}{k-1} = \binom{n-k}{n+1-2k}$ yields $d_n = \sum_{k=1}^{\lfloor(n+1)/2\rfloor} d_{k-1}\binom{n-k}{n+1-2k}$ for all $n \ge 1$. Since $d_0 = 1 = a(1)$ and $k - 1 \le n - 1 < n$, strong induction proves $d_n = a(n+1)$ for all $n \ge 0$, hence $\det(M_n) = a(n+1)$ for all $n \ge 1$. Completely airtight.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A119262/notes/check-check-1.py` -> exit code `0`, `PASS` (verified $a(0..28)$ against OEIS rev. 55, $P_n M_n P_n^{-1} = B_n$ and principal submatrix property for $1 \le n \le 20$, all block minor identities for $1 \le n \le 12$, Laplace recurrence, and exact SymPy $\det(M_n) = a(n+1)$ for $1 \le n \le 20$).
- **Gate 2 novelty receipts:** `watch-6` (`#730`) and `watch-1` (`#735`) clear (incl. `zenodo-23112421-oeis-ids.md`); `@watch-5` will also verify at Gate 3.
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).

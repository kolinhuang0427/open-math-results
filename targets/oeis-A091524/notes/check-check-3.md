# Independent Check Report (`check-3`): `targets/oeis-A091524/`

## 1. Primary-Source Fidelity Check
Checked live OEIS JSON API (`https://oeis.org/search?q=id:...&fmt=json`) directly:
- **OEIS `A091524`** (rev `27`, `2025-02-16`, offset `1,3`):
  - Name: `a(m) is the multiplier of sqrt(2) in the constant alpha(m) = a(m)*sqrt(2) - b(m), where alpha(m) is the value of the constant determined by the binary bits in the recurrence associated with the Graham-Pollak sequence.`
  - Formula (Kurkov, Apr 25 2024): `Conjecture: a(n) = sqrt(A028982(n)/A006337(n)).`
  - Formula (Cloitre, Oct 13 2007): `a(floor(n*(1+sqrt(2))))=n; a(floor(n*(1+1/sqrt(2))))=n, n>=1`.
  - Example (`m=1..5`): `-1+sqrt(2), -1+sqrt(2), -2+2*sqrt(2), -2+2*sqrt(2), -4+3*sqrt(2)`.
  - First 75 data terms match `TARGET.md` and `PROOF.md` definitions (`1,1,2,2,3,4,3,5,...`).
- **OEIS `A028982`** (rev `156`, `2026-05-30`, offset `1,2`): `Squares and twice squares.` (`54` live data terms).
- **OEIS `A006337`** (rev `104`, `2026-10-29`, offset `1,2`): `a(n) = floor( (n+1)*sqrt(2) ) - floor( n*sqrt(2) ).` (`105` live data terms).
- **OEIS `A003152`** (rev `71`, offset `1,2`): `floor(n*(1+1/sqrt(2))).` (`68` live data terms).
- **OEIS `A003151`** (rev `96`, offset `1,1`): `floor(n*(1+sqrt(2))).` (`60` live data terms).

Result: `TARGET.md` statement matches live OEIS `A091524` rev `27` (and auxiliary sequences `A028982`, `A006337`, `A003152`, `A003151`) with zero definition or quantifier drift.

## 2. Independent Mechanical Verification
Written strictly from primary-source OEIS definitions and `PROOF.md` without reading `verify.py` or author scratch notes, using pure exact arithmetic in `Q(sqrt(2))` (`Fraction` + `math.isqrt`, zero floats):
- Script: `targets/oeis-A091524/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/oeis-A091524/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[PASS 1] Beatty partition & tau_m identity verified for 1 <= m <= 5000
[PASS 2] Graham-Pollak u_r=floor(x_r), Delta in (0,1), d_j bits, and all 75 OEIS A091524 terms verified
[PASS 3] A028982 (54 OEIS terms), A006337 (105 OEIS terms), Beatty subseqs, and Kurkov identity verified for 1 <= n <= 5000
PASS
```

## 3. Proof Text Re-Check (Post-Patch)
Verified the patched Section 2 of `targets/oeis-A091524/PROOF.md` (lines 31–49):
- Case split $r \ge 2$ ($K \in \mathbb{Z}_{\ge 1}$), $r = 1, \tau_m = k\sqrt{2}$ ($x_1 = k(1+\sqrt{2})$, $K = k \in \mathbb{Z}_{\ge 1}$), and $r = 1, \tau_m = k$ ($x_1 = k + \frac{k}{2}\sqrt{2}$, $K = \frac{k}{2} \in \frac{1}{2}\mathbb{Z}_{\ge 1}$, $2K = k \in \mathbb{Z}_{\ge 1}$) covers every $(m, r)$ pair cleanly.
- In all cases $\{x_r\} = \{K\sqrt{2}\} \in (0, 1) \setminus \{1/2\}$ (since $K \in \frac{1}{2}\mathbb{Z}_{\ge 1} \subset \mathbb{Q}_{>0}$ and $\sqrt{2} \notin \mathbb{Q}$), and the inequalities for Case 1 ($x_r = K + K\sqrt{2}$) and Case 2 ($x_r = 2K + K\sqrt{2}$, $\alpha < 1/2$ and $\alpha > 1/2$) hold strictly.

## 4. Verdict
- **Primary-source fidelity:** `PASS`
- **Computational checks:** `PASS` (re-run 2026-11-27T08:49Z, exit 0)
- **Proof text check:** `PASS`
- **Gate 2 novelty:** `PASS` (`watch-1` and `watch-6` receipts present in `notes/novelty-gate2-watch-{1,6}.md`; `watch-5` Gate 2 requested per `#20`).

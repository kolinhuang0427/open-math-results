# Adversarial Audit Report (`audit-1`): `targets/oeis-A347063/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A347063` (rev. 51, Jul 24 2026 `17:37:53`) — Refutation of Ivan N. Ianakiev's Oct 01, 2024 conjecture that $18k + 12 \in \mathrm{A347063}$ for all $k \ge 1$
- **Audited Files:** `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, live OEIS `A347063` rev. 51 (`fmt=text`) and `b347063.txt`, `watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`
- **Verdict:** **PASS** *(Re-audit after `#1056` fix removing `/tmp/b347063_check.txt` from `notes/check-check-1.py`; standalone verifier and `COUNTEREXAMPLE.md` are 100% PASS.)*

---

## 1. Primary-Source & Statement Fidelity — PASS

- **Live OEIS `A347063` (`#51 Jul 24 2026 17:37:53`):**
  - `%N`: `Double Zumkeller numbers: numbers whose set of divisors can be partitioned into two disjoint subsets with equal sums and equal cardinalities.` — verbatim match.
  - `%C`: `It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]. - _Ivan N. Ianakiev_, Oct 01 2024` — verbatim match.
  - Live `b347063.txt` jumps directly from `716 3465` to `717 3472`, confirming `3468` is absent.
- **Snapshot cross-check:** `A347063` has `0` hits in both `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`.
- **Gate 2 novelty receipts:** Present from `watch-1` (`#1021`), `watch-5` (`#1010`), `watch-6` (`#1008`).

---

## 2. Line-by-Line Mathematical Audit of `COUNTEREXAMPLE.md` — PASS

- **Section 1 (Infinite counterexample family $n = 12p^2$ for all primes $p \ge 17$, L15–58):**
  - Since $p \ge 17 > 3$ is prime, $p^2 \equiv 1 \pmod 3$, so $p^2 = 3m + 1$ ($m \ge 96$) and $n = 12p^2 = 18(2m) + 12 = 18k + 12$ with $k = \frac{2(p^2 - 1)}{3} \in \mathbb{Z}_{\ge 192}$ ($p = 17 \implies k = 192, n = 3468$).
  - Since $\gcd(12, p^2) = 1$, $D(12p^2) = D_0 \times \{1, p, p^2\}$ with $D_0 = \{1, 2, 3, 4, 6, 12\}$ ($|D_0| = 6$, sum $28$), $\tau(n) = 18$, $\sigma(n) = 28(1 + p + p^2)$, and any Double Zumkeller partition $D(n) = A \sqcup B$ requires $|A| = 9$ and $\sum_{x \in A} x = 14p^2 + 14p + 14$.
  - Writing $A = (p^2 U_2) \sqcup (p U_1) \sqcup U_0$ ($U_i \subseteq D_0$, disjoint by $p$-adic valuation) with $s_i = \sum_{u \in U_i} u \in [0, 28]$:
    - $s_2 \ge 15 \implies s_2 p^2 + s_1 p + s_0 \ge 15p^2 \ge 14p^2 + 17p > 14p^2 + 14p + 14$ (as $3p \ge 51 > 14$).
    - $s_2 \le 13 \implies (14p^2 + 14p + 14) - (13p^2 + 28p + 28) = p(p - 14) - 14 \ge 17 \cdot 3 - 14 = 37 > 0$.
    - Thus $s_2 = 14$, leaving $s_1 p + s_0 = 14p + 14$.
    - $s_1 \ge 15 \implies 15p > 14p + 14$ ($p \ge 17$); $s_1 \le 13 \implies 13p + 28 = 14p + 14 - (p - 14) < 14p + 14$.
    - Thus $s_1 = s_0 = 14$.
  - Exhaustive check on $D_0 = \{1, 2, 3, 4, 6, 12\}$: subsets summing to $14$ are exclusively $\{2, 12\}$ (size $2$) and $\{1, 3, 4, 6\}$ (size $4$). Both have even size, forcing $|A| = |U_2| + |U_1| + |U_0| \equiv 0 \pmod 2$, contradicting $|A| = 9$.
  - Completely elementary and airtight.
- **Section 2 (Minimality of $k = 192$, $n = 3468$, L62–66):**
  - Verified independently by exact bitmask DP with explicit witness reconstruction for every $1 \le k \le 191$ and brute-force enumeration of all $\binom{18}{9} = 48620$ nine-element subsets of $D(3468)$ (`0` hitting $\sigma(3468)/2 = 4298$).

---

## 3. Required Fix in `notes/check-check-1.py` (Blocking Reproducibility Defect)

- **Issue (`targets/oeis-A347063/notes/check-check-1.py` L160–173):** `check_minimality_and_bfile()` opens a hardcoded ephemeral file `/tmp/b347063_check.txt` (`with open("/tmp/b347063_check.txt") as f:`). While it currently passes on this machine because the file still sits in `/tmp`, the standalone verification command `.venv/bin/python -u targets/oeis-A347063/notes/check-check-1.py` will fail with `FileNotFoundError` on any clean machine or after `/tmp` cleanup.
- **Fix (`@check-1`):** Remove the hardcoded `/tmp/b347063_check.txt` read from `notes/check-check-1.py` so the script is 100% self-contained and offline-reproducible (the live `b347063.txt` cross-check is already recorded in `check-check-1.md` and confirmed independently by this audit). No edits to `COUNTEREXAMPLE.md` are needed.

---

## 4. Re-Audit Verification (`#1056`) — PASS

Re-read `targets/oeis-A347063/notes/check-check-1.py` and `notes/check-check-1.md`, confirmed zero `/tmp` references remain in `notes/check-check-1.py`, and re-executed `.venv/bin/python -u targets/oeis-A347063/notes/check-check-1.py` (exit code `0`, `PASS`, pure standalone exact integer arithmetic).

**Final Verdict:** **PASS**. Ready for Gate 3 novelty verification.

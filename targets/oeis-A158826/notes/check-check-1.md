# Independent Check Report: `oeis-A158826`

**Checker:** `check-1`
**Verdict:** **PASS** (re-checked after `PROOF.md` line 29 fix)

## 1. Primary Source Fidelity
- Verified verbatim against live OEIS A158826 (`https://oeis.org/search?q=id:A158826&fmt=text`, rev. 54, May 25 2026):
  - Offset `1,2`, name `Third iteration of x*C(x) where C(x) is the Catalan function (A000108).`
  - Mathar's Aug 30 2021 recurrence in `TARGET.md` and `PROOF.md` matches the live OEIS record verbatim (`n >= 6`).

## 2. Proof & Independent Mechanical Verification
- Checked all algebraic and formal power series steps in `PROOF.md`:
  - `PROOF.md` line 29 now states $1 - 4F(t) = (1 - 2t)^2$, $1 - 2f(u) = \sqrt{1 - 4u}$, and $1 - 4f(u) = -1 + 2\sqrt{1 - 4u}$, which is exact and yields Irwin's nested-radical formula.
  - Step 1 ($P_3(y(x)) = x$), Step 2 ($U(y) = 0$ identically in $\mathbb{Z}[y]$ and unit $P_3'(y(x)) = 1 + O(x)$), and Step 3 (coefficient extraction at $[x^{n-4}]$ for $n \ge 6$) are sound.
- Independent exact verifier `targets/oeis-A158826/notes/check-check-1.py` (`sympy` + exact Python `int`, zero floats, written without reading `verify.py` or author notes):
  - Command: `.venv/bin/python targets/oeis-A158826/notes/check-check-1.py` -> `PASS`.
  - Verified $P_3(y) = F(F(F(y)))$, implicit derivatives $y', y'', y''', y''''$, $U(y) = 0$ identically in $\mathbb{Z}[y]$, symbolic Step 3 coefficient extraction in $\mathbb{Z}[n]$ matching all 6 polynomials in Mathar's recurrence, first 21 OEIS `%S/%T/%U` terms, $P_3(y(x)) \equiv x \pmod{x^{100}}$, and Mathar's recurrence for $6 \le n \le 99$.

## 3. Gate 2 Novelty Status
- Gate 2 passed (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`). Ready for blind audit.

# Independent Check Report: `oeis-A061313` (`check-1`)

- **Checked at (UTC):** `2026-11-26T23:33:53Z`
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity and independent exact verification of all $\mathrm{SL}_2(\mathbb{Z})$ matrix identities, BFS steps, Stern–Brocot enumeration, Hirzebruch continued fractions, and $n=1$ boundary)

## 1. Primary-Source Fidelity Check

- **Primary sources fetched:**
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A061313&fmt=json`), revision `58` (`2026-11-01T16:49:49-05:00`).
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A007305&fmt=json`, rev `117`, `offset: "0,5"`) and `A007306` (rev `342`, `offset: "0,3"`).
- **Exact fields checked in `A061313`:**
  - `name`: *"Minimal number of steps to get from 1 to n by (a) subtracting 1 or (b) multiplying by 2."* (`offset: "1,3"`)
  - `formula`: `a(2n) = a(n)+1; a(2n+1) = a(n+1)+2; a(1) = 0.`
  - `comment`: `Conjecture: a(n)+2 is the sum of the terms of the Hirzebruch (negative) continued fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n). - _Andrei Zabolotskii_, Apr 17 2020`
  - `data`: 90 terms (`0,1,3,2,5,...`).
- **Word-for-word comparison against `TARGET.md` and `PROOF.md`:**
  - Exact recurrence, minimal-step definition, Stern–Brocot fraction definition `A007305(n)/A007306(n)`, Hirzebruch (negative) continued fraction definition, and explicit boundary exception at `n = 1` (`[[1]]` sum `1 != 2 = a(1) + 2`) match verbatim. Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from the live OEIS `A061313`, `A007305`, `A007306` JSON records and the proof steps in `PROOF.md`, without reading `verify.py` or `notes/explore.py`.
- **Verifier script:** `targets/oeis-A061313/notes/check-check-1.py` (exact `fractions.Fraction` and integer $2 \times 2$ matrix arithmetic).
- **Verified claims & lemmas:**
  1. **Step 2 $\mathrm{SL}_2(\mathbb{Z})$ matrix identities:** Verified $L J = H(1) H(2)$, $J^{-1} L J = H(2)$, and $H(c) (J^{-1} R J) = H(c+1)$ for $-5 \le c \le 14$.
  2. **`A061313` recurrence & BFS:** Matched all 90 published OEIS `A061313` data terms and independently verified via BFS that `a(n)` equals the minimal steps from `1` to `n` via `-1` or `*2` for all $1 \le n \le 100$.
  3. **Stern–Brocot enumeration & Step 1 matrix recursion:** Built $r(n)$ level-by-level via Farey mediants up to $n = 4096$, matched all 33 published `A007305`/`A007306` prefix terms ($n = 0..32$), and verified $M(2m-1) = M(m) L$, $M(2m) = M(m) R$ for all $2 \le n \le 4096$.
  4. **Main Theorem & $n=1$ boundary:** Verified $n = 1$ gives `[[1]]` with sum $1 \neq 2 = a(1) + 2$; for ALL $2 \le n \le 4096$, verified $r(n) = [[1; c_1, \dots, c_k]]$ ($c_i \ge 2$), $P(n) = H(1) H(c_1) \cdots H(c_k)$, and $1 + \sum c_i = a(n) + 2$.

### Command & Raw Output

Command:
```bash
.venv/bin/python targets/oeis-A061313/notes/check-check-1.py
```

Raw output:
```text
Step 2 SL_2(Z) identities (L, R, J, H(c)): OK
A061313 OEIS data (90 terms) & BFS minimal steps (n=1..100): OK
A007305/A007306 (33 terms) & Step 1 M(n) recursion (2<=n<=4096): OK
n=1 exception ([[1]] sum 1 != 2) & Main Theorem P(n)=prod H(c_i), sum=a(n)+2 (2<=n<=4096): OK
PASS
```

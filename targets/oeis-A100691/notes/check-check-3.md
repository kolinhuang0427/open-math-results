# Independent Check Report (`check-3`) — `targets/oeis-A100691/`

- **Checked at (UTC):** 2026-11-26T20:21Z
- **Checker:** `check-3` (independent; written without reading `verify.py`)
- **Primary sources inspected (live OEIS JSON API):**
  - `https://oeis.org/search?q=id:A100691&fmt=json` — OEIS **A100691** (revision 11, `2022-07-22T09:50:24-04:00`)
  - `https://oeis.org/search?q=id:A193641&fmt=json` — OEIS **A193641** (revision 48, `2026-09-16T10:42:19-04:00`)

## 1. Primary-Source Fidelity & Definition Match

- **A100691 (rev 11):**
  - Name: `"Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."`
  - Offset: `0,2`
  - Data: `1,4,12,30,70,158,352,780,1724,3806,8398,18526,40864,90132,198796,...`
  - Formula:
    - `G.f.: (1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)]= 1+2*(2+z^2)/((z-1)*(z^2+2*z-1)).`
    - `a(n) = 2*a(n-1) + a(n-3) + 6 for n >= 4.`
    - `Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022`
- **A193641 (rev 48):**
  - Name: `"Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."`
  - Offset: `0,3`
  - Data: `1,1,3,7,15,33,73,161,355,783,1727,3809,8401,...`
  - Formula: `Empirical: a(n) = 2*a(n-1) + a(n-3).`
- **Definition check:**
  - In `A193641`, "subsequence of length 1 or 2" means **contiguous** subarray (length-1 `[0]` or length-2 `[1,-1]`, `[-1,1]`), confirmed by `A193641(3) = 7` (non-contiguous would include `[1,0,-1]` and `[-1,0,1]`, giving `9 != 7`).
  - In `A100691`, `n`-step self-avoiding paths on the triangular lattice strip $\mathbb{Z} \times \{0,1\}$ (rooted walks starting at a fixed vertex, by translation and $(x,y) \mapsto (-x, 1-y)$ symmetry equivalent to $(0,0)$) match `s(0..4) = 1, 4, 12, 30, 70`.
  - No statement, quantifier, offset, or definition drift in `TARGET.md` or `PROOF.md`.

## 2. Independent Mechanical Verification

Wrote independent exact verifier `targets/oeis-A100691/notes/check-check-3.py` strictly from the OEIS primary definitions and `PROOF.md`, without reading `verify.py`:
- **Part 1 (`A193641` & `a_OEIS`):** Brute-force enumeration over `{-1, 0, 1}^n` for `0 <= n <= 10`, verifying `U(n)`, `V(n)`, `W(n)` counts and exact transitions, `b(m) = 2*b(m-1) + b(m-3)` (`m >= 3`), agreement with OEIS `A193641(0..10)`, symbolic identity `(1 - 2z - z^3) * G_OEIS(z) = 1 + 2z + 4z^2 + 5z^3 + 6z^4/(1-z)` in SymPy, and `a_OEIS(n) = A193641(n+2) - 3` for `n >= 1`. Also confirmed the formula-line typo `G_OEIS(z) != 1 + 2*(2+z^2)/((z-1)*(z^2+2*z-1))`.
- **Part 2 (Triangular strip SAW):** Independent 3-edge-cut finite-state column transfer automaton (`pre=8`, `post=7` states) solved symbolically over $\mathbb{Q}(z)$ in SymPy, plus independent brute-force DFS over `0 <= n <= 14` (and start-row symmetry `(0,0)` vs `(0,1)` for `0 <= n <= 10`), confirming:
  - $F_{\mathrm{SAW}}(z) = \frac{1 + z^2 - z^3 + z^5}{(1-z)^2 (1 - 2z - z^3)}$, matching DFS `s(0..7) = [1, 4, 12, 30, 70, 160, 360, 802]` through `n = 14`;
  - $F_{\mathrm{SAW}}(z) - G_{\mathrm{OEIS}}(z) = \frac{2z^5}{(1-z)^2(1 - 2z - z^3)}$, with positive coefficients `2, 8, 22, 54, 126, ...` for all `n >= 5`, so `s(5) = 160 != 158 = A193641(7) - 3`.

- **Command run:**
  ```bash
  .venv/bin/python targets/oeis-A100691/notes/check-check-3.py
  ```
- **Raw output:**
  ```text
  Part 1 PASS: A193641 brute-force (n<=10), U/V/W transitions, and a_OEIS(n)=A193641(n+2)-3 verified.
  Part 2 PASS: Transfer matrix (pre=8, post=7) matches DFS (n<=14): s(0..7)=[1, 4, 12, 30, 70, 160, 360, 802], s(5)=160 != 158=A193641(7)-3.
  PASS
  ```

## 3. Verdict

**PASS** — Primary sources match `TARGET.md` and `PROOF.md` verbatim, and both parts of `PROOF.md` (`a_OEIS(n) = A193641(n+2) - 3` for all `n >= 1`, and the combinatorial triangular-strip SAW erratum `s(5) = 160 != 158`, `s(n) > A193641(n+2) - 3` for all `n >= 5`) pass independent exact verification.

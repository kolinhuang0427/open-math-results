# Adversarial Audit Report: `targets/oeis-A100691/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-26T21:05Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (with exact-computation verification for Part 1's recurrence/transitions, exact finite enumeration for the `n = 5` combinatorial counterexample `s(5) = 160 != 158`, and independent symbolic transfer-matrix verification over $\mathbb{Q}(z)$ for all $n \ge 5$). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/oeis-A100691/notes/check-check-3.py` (authored by `check-3` strictly from primary OEIS definitions, independently audited line-by-line and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary sources (live OEIS JSON API, fetched directly):
  - `A100691` (revision 11, 2022-07-22, Emeric Deutsch / R. J. Mathar)
  - `A193641` (revision 48, 2026-09-16, R. H. Hardin / Alois P. Heinz)
  - Sibling Labelle strip sequences `A100692`, `A100693` (Emeric Deutsch, Dec 7 2004, same citation J. Labelle *Bull. ICA* 17, 1996) and `A038577` (J. Labelle *Bull. ICA* 23, 1998).
- `targets/oeis-A100691/TARGET.md`
- `targets/oeis-A100691/PROOF.md`
- `targets/oeis-A100691/notes/check-check-3.md` and `notes/check-check-3.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,5,6}.md`).

Author scratch notes (`notes/screen-*`) and the finder's `verify.py` were **not** read.

---

## 2. Primary-Source Fidelity & Definition Audit

1. **OEIS `A100691` (rev 11, 2022-07-22):**
   - Exact Name: `"Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."`
   - Exact Data (offset `0,2`): `1, 4, 12, 30, 70, 158, 352, 780, 1724, 3806, ...`
   - Exact Formula entries: `G.f.: (1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)] = 1+2*(2+z^2)/((z-1)*(z^2+2*z-1)).`, `a(n) = 2*a(n-1) + a(n-3) + 6 for n >= 4.`, `Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022`.
   - Note confirmed: the second formula on line 1 (`1+2*(2+z^2)/((z-1)*(z^2+2*z-1))`) is an existing OEIS typo for `1 + 2*z*(2+z^2)/((1-z)*(1-2*z-z^3))`.
2. **OEIS `A193641` (rev 48, 2026-09-16):**
   - Exact Name: `"Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."`
   - Exact Data (offset `0,3`): `1, 1, 3, 7, 15, 33, 73, 161, 355, 783, ...`
   - Exact Formula: `Empirical: a(n) = 2*a(n-1) + a(n-3).`
   - Examples (`n=6`) and Alois P. Heinz's Maple DP (Sep 16 2026) confirm unambiguously that "subsequence of length 1 or 2" means **contiguous** subarray (length-1 `[0]` or adjacent length-2 `[1,-1]`/`[-1,1]`), and the recurrence remains marked `Empirical` with no proof recorded.
3. **Sibling Labelle Strip Verification (`A038577`, `A100692`, `A100693`):**
   - Independently ran brute-force DFS for rooted $n$-step SAWs starting at $(0,0)$ on:
     - Square strip $\mathbb{Z} \times \{0,1\}$: `1, 3, 6, 12, 20, 36, 58, 100, 160, 268, 430` — exact match with `A038577` (Labelle 1998).
     - Hexagonal vertical-brickwall strip $\mathbb{Z} \times \{-1,0,1\}$: `1, 3, 4, 4, 6, 10, 10, 8, 12, 20, 20` — exact match with `A100692` (Labelle 1996 / Deutsch Dec 7 2004).
     - Hexagonal vertical-brickwall strip $\mathbb{Z} \times \{0,1,2\}$: `1, 2, 3, 5, 6, 7, 9, 14, 14, 14, 22` — exact match with `A100693` (Labelle 1996 / Deutsch Dec 7 2004).
   - This confirms beyond doubt that Labelle's strip-path definition is standard rooted $n$-step SAWs from $(0,0)$, and the triangular lattice strip $\mathbb{Z} \times \{0,1\}$ is uniquely the 4-regular infinite strip $P_\infty^2$ (vertices $\mathbb{Z} \times \{0,1\}$, horizontal, vertical, and one diagonal direction).

---

## 3. Adversarial Audit of Both Parts of `PROOF.md`

### 3.1 Part 1 — Proof of `A193641` Recurrence & `a_OEIS(n) = A193641(n+2) - 3` (`n >= 1`)

Audited every step line-by-line; **zero gaps found**:
- The 3-class partition `U(n)`, `V(n)`, `W(n)` of prefixes `(x_1,...,x_n) in {-1, 0, 1}^n` with `1..n-1` covered inside `x_1..x_n` is exhaustive and disjoint. In particular, in `W(n)` where `x_n in {-1, 1}` is uncovered inside `x_1..x_n`, `x_n` cannot help cover `x_{n-1}` either (else `x_{n-1} + x_n = 0` would also cover `x_n`), so `(x_1,...,x_{n-1})` is necessarily valid (`U(n-1) \sqcup V(n-1)`).
- Every transition for `n >= 0` is bijective and exact:
  - `U(n+1) = U(n) + V(n) = b(n)` (appending `0` to valid arrays; `W(n)` cannot be followed by `0` without leaving `x_n` permanently uncovered).
  - `W(n+1) = 2*U(n) + V(n)` (appending `+-1` to `U(n)`, or `x_n` to `V(n)`).
  - `V(n+1) = V(n) + W(n)` (appending `-x_n` to `V(n)` or `W(n)`; any prefix with some `i <= n-1` uncovered can never become valid by appending `x_{n+1}`).
- Initial values `U(0)=1, V(0)=0, W(0)=0` give `b(0)=1, b(1)=1, b(2)=3`.
- Algebraic elimination gives `U(n)=b(n-1)` and `V(n)=b(n)-b(n-1)` (`n >= 1`), `W(n) = b(n-1)+b(n-2)` (`n >= 2`), and `b(n+1) - b(n) = V(n+1) = b(n) + b(n-2)` (`n >= 2`), yielding `b(m) = 2*b(m-1) + b(m-3)` for all `m >= 3`.
- Setting `c(n) = b(n+2) - 3` (`n >= 1`) gives `c(1..4) = 4, 12, 30, 70` and `c(n) = 2*c(n-1) + c(n-3) + 6` for `n >= 4`. Exact polynomial identity `(1 - 2z - z^3) G_OEIS(z) = (1 + z + 2z^2 + z^3 + z^4)/(1 - z) = 1 + 2z + 4z^2 + 5z^3 + 6z^4/(1-z)` shows `a_OEIS(n)` satisfies the identical recurrence and initial values, proving `a_OEIS(n) = A193641(n+2) - 3` for all `n >= 1`.

### 3.2 Part 2 — Combinatorial-Definition Reading (`s(5) = 160 != 158` and All `n >= 5`)

- **Exact finite counterexample at `n = 5`:** Independently verified by pure brute-force DFS (`check-check-3.py` through `n <= 14`, plus fresh independent DFS during audit) that `s(0..5) = 1, 4, 12, 30, 70, 160`, so `s(5) = 160 != 158 = A193641(7) - 3`.
- **Exact transfer matrix for all `n >= 5`:** Audited the independent 3-edge-cut column transfer automaton in `check-check-3.py` (`pre=8, post=7` states):
  - Every edge of $\mathbb{Z} \times \{0,1\}$ lies uniquely in either column $x$ (vertical edge) or cut $C_x$ (horizontal bottom, diagonal, horizontal top).
  - Removing the empty-column self-loop `(0,(),()) -> (0,(),())` in $M_L$ ensures $M_L(0) = 0$ (strict power-series invertibility) and counts each path from its true leftmost column $x_{\min} \le 0$ exactly once.
  - Enforcing `deg(0,0) = 1` in column $x = 0$, forbidding cycles, degree $> 2$, premature closed components, and $> 2$ endpoints, and making `accept_state = (2, (), ())` absorbing with no outgoing edges in $M_R$ (so $M_R(0)^2 = 0$, strict power-series invertibility) counts every undirected simple path with endpoint $(0,0)$ — in bijection with directed SAWs starting at $(0,0)$ — at its true rightmost column $x_{\max} \ge 0$ exactly once.
  - Exact SymPy solution yields $F_{\mathrm{SAW}}(z) = \frac{1 + z^2 - z^3 + z^5}{(1-z)^2 (1-2z-z^3)}$, matching DFS identically for all $0 \le n \le 14$, while $G_{\mathrm{OEIS}}(z) = \frac{1 + z^2 - z^3 - z^5}{(1-z)^2 (1-2z-z^3)}$ (a single sign error `-z^5` vs `+z^5` that cancels a factor of `1-z`).
  - Hence $F_{\mathrm{SAW}}(z) - G_{\mathrm{OEIS}}(z) = \frac{2z^5}{(1-z)^2 (1-2z-z^3)}$ has strictly positive coefficients for all $n \ge 5$, proving `s(n) > A193641(n+2) - 3` for every `n >= 5`.
- **Verifier Re-run:** `.venv/bin/python /Users/kev/Documents/open-math/targets/oeis-A100691/notes/check-check-3.py` exited with code `0`:
  ```text
  Part 1 PASS: A193641 brute-force (n<=10), U/V/W transitions, and a_OEIS(n)=A193641(n+2)-3 verified.
  Part 2 PASS: Transfer matrix (pre=8, post=7) matches DFS (n<=14): s(0..7)=[1, 4, 12, 30, 70, 160, 360, 802], s(5)=160 != 158=A193641(7)-3.
  PASS
  ```

### 3.3 Minor Non-Blocking Caveats

1. `PROOF.md` Part 2 summarizes the 3-edge-cut transfer matrix (citing 9 right-of-origin states in `verify.py` vs 7 minimal right-of-origin states in `check-check-3.py`) without writing out the transition table in prose; however, the `n = 5` counterexample `s(5) = 160 != 158` is completely elementary and the full rational GF $F_{\mathrm{SAW}}(z)$ was independently reconstructed and verified from scratch in `check-check-3.py`.
2. J. Labelle, *Bull. ICA* 17 (1996), 47–61 is print-only and was not directly inspected; thus we cannot attribute whether the `-z^5` vs `+z^5` sign error originated in Labelle (1996) or in Deutsch's 2004 OEIS submission (though `A038577`, `A100692`, and `A100693` confirm Labelle's rooted-SAW definition).

---

## 4. Novelty Assessment (Gate 3 Clear)

- Live OEIS `A100691` (rev 11) still marks Mathar's 2022 formula as `Conjecture:`, live OEIS `A193641` (rev 48, Sep 16 2026) still marks `a(n) = 2*a(n-1) + a(n-3)` as `Empirical:`, and live OEIS searches for `4,12,30,70,160,360,802` and `2,8,22,54,126` return zero results.
- Gate 2 receipts (`novelty-gate2-watch-{1,5,6}.md`) all passed with no `CONTESTED.md`.
- **Gate 3 Clear (pre-report window, `2026-11-26T21:12:06Z`–`21:14:45Z`):** All three watchers filed fresh live PASS receipts with zero `CONTESTED.md` matches: `notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md` (noting shared-IP OpenAlex 429; Gate 2 OpenAlex check clear at `20:18Z`), and `notes/novelty-gate3-watch-6.md`. Ready for coordinator final verification.

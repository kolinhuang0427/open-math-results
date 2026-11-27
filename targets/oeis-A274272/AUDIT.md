# Blind Audit: `targets/oeis-A274272/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (`written proof, internally audited`)
- **Audited Files:** `targets/oeis-A274272/TARGET.md`, `targets/oeis-A274272/PROOF.md`, `targets/oeis-A274272/notes/check-check-1.md`, `targets/oeis-A274272/notes/check-check-1.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON (`2026-11-27`) for `A274272` (`rev. 12`, offset `0,2`); `0` hits across all `658` files in `watch/snapshots/**` (including Zenodo compendia and `mylesparslow-conjecture-ledger.md`).

---

## 1. Primary-Source & Statement Fidelity

- Verified verbatim match between live OEIS `A274272` (`rev. 12`, offset `0,2`) and `TARGET.md` L14–22:
  - `NAME`: `Number of partitions of 5^n into at most four parts.`
  - `FORMULA`: `Coefficient of x^(5^n) in 1/((1-x)*(1-x^2)*(1-x^3)*(1-x^4)).` and Colin Barker's Jun 17 2016 `Conjectures (Start)`–`(End)` block (closed form $a(n) = (57 + 8(-1)^n + 63 \cdot 5^n + 3 \cdot 5^{1+2n} + 125^n)/144$, order-5 recurrence for $n > 4$, and rational g.f.).

---

## 2. Adversarial Line-by-Line Proof Audit (`PROOF.md`)

1. **Section 1 (Generating function & partial fraction decomposition):**
   - Ferrers conjugation identifies partitions of $m$ into $\le 4$ parts with partitions of $m$ with parts in $\{1, 2, 3, 4\}$, giving $a(n) = [x^{5^n}] F(x)$ for $F(x) = \frac{1}{(1-x)(1-x^2)(1-x^3)(1-x^4)}$ (all $n \ge 0$).
   - Verified both the partial fraction expansion (L24) and the cleared-denominator polynomial identity ($= 288$, L26–27). **Verified.**
2. **Section 2 (Exact extraction at $m = 5^n$, $n \ge 0$):**
   - $m = 5^n$ is odd and satisfies $5^n \equiv (-1)^n \pmod 3$.
   - Verified all four pole contributions by hand: $x = 1$ gives $\frac{2m^3 + 30m^2 + 135m + 175}{288}$; $x = -1$ (odd $m$) gives $\frac{-9m - 45}{288}$; $x = \pm i$ gives $0$ (even power series); primitive cube roots of unity give $\frac{1-x^2}{9(1-x^3)}$ extracting $\frac{(-1)^n - 1}{18} = \frac{16(-1)^n - 16}{288}$.
   - Summing and dividing by $2$ yields $a(n) = \frac{57 + 8(-1)^n + 63 \cdot 5^n + 3 \cdot 5^{1+2n} + 125^n}{144}$ for all $n \ge 0$. **Verified.**
3. **Section 3 (Rational g.f. & order-5 linear recurrence):**
   - Summing the five geometric series over common denominator $D(x) = (1-x)(1+x)(1-5x)(1-25x)(1-125x) = 1 - 155x + 3874x^2 - 15470x^3 - 3875x^4 + 15625x^5$ yields numerator $1 - 149x + 3129x^2 - 5655x^3 - 6750x^4$ (degree $4$), whence $[x^n](D(x)G(x)) = 0$ gives the exact order-5 recurrence for all $n > 4$. **Verified.**

---

## 3. Independent Computation Check

- Inspected `targets/oeis-A274272/notes/check-check-1.py` via AST: zero floats (`[]`), all `/` operate strictly on exact SymPy expressions.
- Independently executed `.venv/bin/python -u targets/oeis-A274272/notes/check-check-1.py`: exited `0` with raw `PASS` (exact symbolic PFD/cleared identity/pole formulas/$G(x)$; direct partition enumeration at $m = 1, 5, 25$ and exact integer DP at $5^0..5^4$; live OEIS prefix $a(0..14)$; $D(x)G(x) = N(x)$ and recurrence for $0 \le n \le 60$).

---

## 4. Handoff

**PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`), instructing them to mention `@coordinator` on PASS with verifier command `.venv/bin/python -u targets/oeis-A274272/notes/check-check-1.py` and paths `targets/oeis-A274272/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

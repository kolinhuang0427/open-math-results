# Blind Audit: `targets/oeis-A028495/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/oeis-A028495/TARGET.md`, `targets/oeis-A028495/PROOF.md`, `targets/oeis-A028495/notes/check-check-3.md`, `targets/oeis-A028495/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON for `A028495` (`rev. 162`, `2026-10-28`, offset `0,3`), `A160389` (`rev. 125`, `2026-02-17`), and `A116425` (`rev. 57`, `2026-07-25`), plus `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits).

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against live OEIS JSON:
- **OEIS `A028495`** (`rev. 162`, `2026-10-28T21:52:26-04:00`, offset `0,3`):
  - **Name:** `Expansion of g.f. (1-x^2)/(1-x-2*x^2+x^3).`
  - **Data (`a(0)..a(36)`):** `1,1,2,3,6,10,19,33,61,...,874055885` (37 terms match `TARGET.md` L22 verbatim).
  - **Conjecture (`%F`, `_Bill McEachen_`, Feb 11 2026):** `Conjectures: a(n) ~ A160389 * a(n-1). Also a(n) ~ sqrt(A116425)*a(n-1).`
- **OEIS `A160389`** (`rev. 125`, `2026-02-17`): `Decimal expansion of 2*cos(Pi/7).` (`1.8019377...`)
- **OEIS `A116425`** (`rev. 57`, `2026-07-25`): `Decimal expansion of 2 + 2*cos(2*Pi/7).` (`3.2469796...`)
- *Minor cosmetic note (non-blocking):* `TARGET.md` L28–29 cites `(rev. 12)` and `(rev. 11)` for `A160389`/`A116425` (live OEIS revisions are `#125` and `#57`); the quoted definitions match verbatim.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

Audited every line (`L1–42`) of `PROOF.md`:
1. **Characteristic Polynomial & Cyclotomic Roots (`Lemma 1`, L9–26):**
   - Reciprocal denominator $P(r) := r^3 - r^2 - 2r + 1 = x^{-3}(1 - x - 2x^2 + x^3)|_{x=1/r}$. Exact.
   - For $k \in \{1, 3, 5\}$, $\zeta = e^{ik\pi/7}$ satisfies $\zeta^7 = -1$ and $\zeta \ne -1$, so $(\zeta^7+1)/(\zeta+1) = \zeta^6 - \zeta^5 + \zeta^4 - \zeta^3 + \zeta^2 - \zeta + 1 = 0$. Dividing by $\zeta^3$ and substituting $r = \zeta + \zeta^{-1} = 2\cos(k\pi/7)$ via $\zeta^2 + \zeta^{-2} = r^2 - 2$ and $\zeta^3 + \zeta^{-3} = r^3 - 3r$ yields $P(r) = 0$.
   - Since $\cos$ is strictly decreasing on $[0, \pi]$, $r_1 = 2\cos(\pi/7) > r_2 = 2\cos(3\pi/7) > r_3 = 2\cos(5\pi/7)$ are three distinct real roots exhausting the cubic $P(r)$.
   - Exact rational endpoint evaluations verified independently:
     $P(-3/2) = -13/8 < 0 < 1 = P(-1)$, $P(0) = 1 > 0 > -1/8 = P(1/2)$, $P(3/2) = -7/8 < 0 < 1 = P(2)$.
     By IVT, $r_3 \in (-3/2, -1)$, $r_2 \in (0, 1/2)$, and $r_1 \in (3/2, 2)$, establishing strict dominance $r_1 > 3/2 > |r_3| > 1 > 1/2 > r_2 > 0$.
   - Since $\cos(\pi/7) > 0$, $(2\cos(\pi/7))^2 = 4\cos^2(\pi/7) = 2 + 2\cos(2\pi/7) \implies 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$. Exact.
2. **Partial Fractions & Asymptotic Ratio (`Theorem`, L30–42):**
   - Since $1 - x - 2x^2 + x^3 = \prod_{j=1}^3 (1 - r_j x)$ has distinct nonzero reciprocal roots $1/r_j$ and $\deg(1 - x^2) = 2 < 3$, partial fraction decomposition gives $\frac{1-x^2}{1-x-2x^2+x^3} = \sum_{j=1}^3 \frac{c_j}{1 - r_j x}$ with $c_j = \frac{1 - r_j^{-2}}{\prod_{i \ne j}(1 - r_i/r_j)} = \frac{r_j^2 - 1}{\prod_{i \ne j}(r_j - r_i)} = \frac{r_j^2 - 1}{P'(r_j)}$, yielding $a(n) = \sum_{j=1}^3 c_j r_j^n$ for all $n \ge 0$. (Independently verified algebraically: $7(r^2-1) \equiv (2+r)P'(r) \pmod{P(r)}$, so $c_j = (2+r_j)/7$, matching Kociemba's closed formula on OEIS.)
   - Since $r_1 > 3/2$ and $r_1 > r_2 > r_3$, both $r_1^2 - 1 > 5/4 > 0$ and $P'(r_1) = (r_1 - r_2)(r_1 - r_3) > 0$, so $c_1 > 0$.
   - Because $|r_2/r_1| < 1/3 < 1$ and $|r_3| < 3/2 < r_1 \implies |r_3/r_1| < 1$, $a(n) = c_1 r_1^n(1 + o(1))$ (with $a(n) \ne 0$ for all large $n$), giving $\lim_{n\to\infty} a(n)/a(n-1) = r_1 = 2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)}$.

Zero gaps, zero floats, zero edge-case defects.

---

## 3. Independent Verification & Novelty Status

- Re-ran independent checker script (pure `int`/`Fraction` + SymPy exact algebra, zero floats):
  - Command: `.venv/bin/python -u targets/oeis-A028495/notes/check-check-3.py`
  - Result: exit code `0`, raw `PASS`.
- Independent auditor check confirmed all rational evaluations of $P(r)$ and $7(r^2-1) - (2+r)P'(r) \equiv 0 \pmod{P(r)}$ in SymPy.
- Checked `watch/snapshots/zenodo-23112421-oeis-ids.md`: `0` hits for `A028495`.
- Gate 2 novelty PASS receipts present from `watch-1` (`#882`), `watch-5` (`#876`), and `watch-6` (`#879`).

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Handing off directly to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).

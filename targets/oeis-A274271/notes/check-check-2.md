# Blind Check Report — `targets/oeis-A274271/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty: PASS per `watch-1` `#1235`, `watch-5` `#1234`, `watch-6` `#1261`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary source checked:** Live OEIS JSON for [A274271](https://oeis.org/A274271) (`rev. 12`, offset `0,2`).
- **`TARGET.md` comparison:** Matches verbatim — `NAME: Number of partitions of 3^n into at most four parts.` and Colin Barker's Jun 17 2016 `FORMULA` conjectures:
  - $a(n) = ((3+3^n)^2(9+3^n))/144$ for $n > 1$,
  - $a(n) = 40a(n-1) - 390a(n-2) + 1080a(n-3) - 729a(n-4)$ for $n > 4$,
  - G.f.: $(1-37x+288x^2-405x^3-81x^4)/((1-x)(1-3x)(1-9x)(1-27x))$.

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/oeis-A274271/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A274271/notes/check-check-2.py) (zero floating-point arithmetic; pure-Python `int`, `fractions.Fraction`, and exact `sympy` over $\mathbb{Q}(x)$).
- **Command & result:** `.venv/bin/python -u targets/oeis-A274271/notes/check-check-2.py` exited with code `0` (`PASS`):
  1. `Partition GF & live DATA`: expanded $F(x) = 1/((1-x)(1-x^2)(1-x^3)(1-x^4))$ up to $x^{6561}$ ($n=0..8$), verifying $a(0)=1$, closed form for $n=1..8$, and all 19 live OEIS `A274271` `DATA` terms ($n=0..18$).
  2. `Section 1`: verified exact partial fraction identity and cleared-denominator polynomial identity (L24–L30) in $\mathbb{Q}(x)$.
  3. `Section 2`: verified each of the four pole contributions ($x=1$, $x=-1$, $x=\pm i$, $\Phi_3(x)$) and closed form for $n=1..25$.
  4. `Section 3`: verified the geometric series sum $-\frac{1}{9} + \frac{1}{144}(\dots) = G(x)$, denominator expansion $(1-x)(1-3x)(1-9x)(1-27x) = 1-40x+390x^2-1080x^3+729x^4$, and 4-term linear recurrence for $n=0..40$.

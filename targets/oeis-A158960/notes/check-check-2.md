# Check Report: `targets/oeis-A158960/` (`@check-2`)

- **Primary Source Fidelity:** Verified against live OEIS **A158960** (revision 28, offset `0,2`, M. F. Hasler Feb 16 2014 denominator conjecture). `TARGET.md` and `PROOF.md` match the physicists' Hermite polynomial recurrence $H_n(1/5)$, the sequence definition $a(n) = 5^n H_n(1/5)$, and the reduced denominator conjecture $5^n$ verbatim.
- **Proof & Computation Verification (`check-check-2.py` -> `PASS`):**
  - Computed $H_n(1/5)$ directly in exact `fractions.Fraction` from $H_0(x)=1, H_1(x)=2x, H_n(x)=2x H_{n-1}(x)-2(n-1)H_{n-2}(x)$ for $0 \le n \le 100$.
  - Verified $b(n) = 5^n H_n(1/5) = 2 b(n-1) - 50(n-1) b(n-2) \in \mathbb{Z}$, $b(n) \equiv 2^n \not\equiv 0 \pmod 5$, and hence exact reduced denominator $5^n$ and numerator $b(n)$ for all $0 \le n \le 100$ (plus Greubel's explicit formula for $n \le 40$ and all 18 live OEIS rev. 28 data terms).
- **Script & Result:** `.venv/bin/python -u targets/oeis-A158960/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `novelty-gate2-watch-5.md` `PASS` (`@watch-1`/`@watch-6` pending per `#653`).

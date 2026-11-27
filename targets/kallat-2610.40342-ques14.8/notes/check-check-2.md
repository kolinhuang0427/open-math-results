# Check Report: `targets/kallat-2610.40342-ques14.8/` (`@check-2`)

- **Primary Source Fidelity:** Verified against `arXiv:2610.40342v1` (`paper1_valuation_calculus.tex`, Section 13 Definition 13.1 `def:types` L1011–1013 and Lemma 13.2 `lem:typeB` L1017–1025, Section 14 Question 14.8 `prob:composite` L1212–1214). `TARGET.md` and `COUNTEREXAMPLE.md` match verbatim (including the `#705` fixes to Section 13 / Def 13.1 / Lemma 13.2, `(1.2)` at `COUNTEREXAMPLE.md` L47, and the general Legendre bound at L58).
- **Counterexample Verification (`check-check-2.py` -> `PASS`):**
  - Directly computed $a_A(n)$ from the cycle-length recurrence ($a_A(0)=1$, $a_A(n)=\sum_{m\in A, m\le n}(n-1)_{m-1} a_A(n-m)$) for $0 \le n \le 120$:
    1. **Odd $p$, sign $+$ ($A=\{1,7\}, p=3, e=3$):** Type II ($1\in A, 3\notin A$), predicted least period $27$; proven $a(n) \equiv 1 - 9\binom{n}{7} \pmod{27}$ with repeating 9-term block `(1,1,1,1,1,1,1,19,10)` and exact least period $9 < 27$.
    2. **Odd $p$, sign $-$ ($A=\{5\}, p=5, e=2$):** Type II ($1\notin A, 5\in A$), predicted least period $50$; proven $a(5k) \equiv (-1)^k \pmod{25}$ and $0$ otherwise, repeating 10-term block `(1,0,0,0,0,24,0,0,0,0)` and exact least period $10 < 50$.
    3. **$p=2$, sign $+$ ($A=\{2,4\}, p=2, e=2$):** Type II ($1\notin A, 2\in A$), sign $(-1)^{[2\in A]+[4\in A]} = +1$, predicted least period $4$; proven $a(2m) \equiv 1 \pmod 4$ and $a(2m+1)=0$, repeating `(1,0)` with exact least period $2 < 4$.
    4. **Constant-residue families:** Checked $A=\{1\}$, $A=\{1,10\} \bmod 27$, $A=\{1,5\} \bmod 4$, $A=\{1,8\} \bmod 7$ all satisfy $a_A(n) \equiv 1 \pmod{p^e}$ (least period $1 < p^e$).
- **Script & Result:** `.venv/bin/python -u targets/kallat-2610.40342-ques14.8/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** Check board / ping `@watch-1` if not yet posted.

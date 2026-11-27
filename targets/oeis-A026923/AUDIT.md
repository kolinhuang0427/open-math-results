# Adversarial Audit — `targets/oeis-A026923/`

- **Auditor:** `@audit-2` (blind adversarial audit; did NOT read author `verify.py` or author scratch notes)
- **Date (UTC):** `2026-11-27T11:44Z`
- **Verdict:** **PASS** (`written proof, internally audited`)

---

## 1. Statement & Primary-Source Fidelity

Verified verbatim against the official OEIS data mirror (`gh api repos/oeis/oeisdata/contents/seq/A026/A026923.seq`, `%I A026923 #27 Feb 27 2026 15:18:34`, offset `1,7`, 55 listed terms):
- **`NAME`:** `Number of partitions of n into an odd number of parts, the greatest being 3; also, a(n+5) = number of partitions of n+2 into an even number of parts, each <= 3.` — matches `TARGET.md` L17 verbatim.
- **`FORMULA`:** `Conjectures from _Colin Barker_, Sep 01 2019: (Start)`
  - `G.f.: x^3*(1 - x + x^2 + x^4) / ((1 - x)^3*(1 + x)^2*(1 - x + x^2)*(1 + x^2)*(1 + x + x^2)).`
  - `a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11) for n>11.`
  - `(End)` — matches `TARGET.md` L19–23 and `PROOF.md` Theorem L5–9 verbatim.
- **`DATA`:** `0,0,1,0,1,1,3,2,4,3,6,5,8,7,11,9,13,12,17,15,20,18,24,22,28,26,33,30,37,35,43,40,48,45,54,51,60,57,67,63,73,70,81,77,88,84,96,92,104,100,113,108,121,117,131` (offset `1,7`).

---

## 2. Novelty & Compendia Cross-Check

- **Gate 2 receipts:** All three independent Gate 2 checks passed (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
- **OEIS compendia snapshots:** Independently checked all 7 OEIS compendia snapshots under `watch/snapshots/` (`zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`, `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, `zenodo-2026-oeis-compendia-ids.md`): **`0` hits** for `A026923`.
- **Official OEIS mirror status:** Barker's Sep 01 2019 G.f. and recurrence remain open conjectures in `A026923.seq` rev. 27.

---

## 3. Line-by-Line Proof Audit (`PROOF.md`)

1. **Bivariate generating function (§1, L19–22):**
   - Every partition of $n \ge 1$ into $m \ge 1$ parts with largest part $3$ decomposes uniquely as one mandatory part $3$ plus a multiset of $m-1$ parts in $\{1,2,3\}$ with multiplicities $(c_1,c_2,c_3) \in \mathbb{Z}_{\ge 0}^3$, giving $n = 3 + c_1 + 2c_2 + 3c_3$ and $m = 1 + c_1 + c_2 + c_3$.
   - Hence $F(x,y) = \sum_{n,m \ge 1} p_3(n,m) x^n y^m = \frac{x^3 y}{(1-xy)(1-x^2 y)(1-x^3 y)}$ holds identically in $\mathbb{Z}[y][[x]]$. Because $p_3(n,m)=0$ for $m>n$, each $[x^n]F(x,y)$ is a polynomial in $y$, so evaluating at $y = \pm 1$ is well-defined coefficientwise in $\mathbb{Z}[[x]]$.
   - The alternate-description remark (L11) is also exact: deleting one part of size $3$ bijects partitions of $n+5$ ($n \ge 1$) into an odd number of parts with largest part $3$ onto partitions of $n+2$ into an even number of parts each $\le 3$.
2. **Parity projection & algebraic simplification (§2, L26–40):**
   - $\frac{1 - (-1)^m}{2} = \mathbf{1}_{m\text{ odd}}$ gives $A(x) = \frac{F(x,1) - F(x,-1)}{2}$.
   - Denominator factorizations verified:
     - $F(x,1) = \frac{x^3}{(1-x)(1-x^2)(1-x^3)} = \frac{x^3}{(1-x)^3(1+x)(1+x+x^2)}$,
     - $F(x,-1) = \frac{-x^3}{(1+x)(1+x^2)(1+x^3)} = \frac{-x^3}{(1+x)^2(1+x^2)(1-x+x^2)}$.
   - Over common denominator $D(x) = (1-x)^3(1+x)^2(1-x+x^2)(1+x^2)(1+x+x^2)$:
     - $(1+x)(1-x+x^2)(1+x^2) = (1+x^3)(1+x^2) = 1 + x^2 + x^3 + x^5$,
     - $(1-x)^3(1+x+x^2) = (1-x)^2(1-x^3) = 1 - 2x + x^2 - x^3 + 2x^4 - x^5$.
   - Sign check: since $F(x,-1)$ carries a minus sign in the numerator, $F(x,1) - F(x,-1)$ adds the two numerator polynomials, yielding $2 - 2x + 2x^2 + 2x^4 = 2(1 - x + x^2 + x^4)$. Dividing by $2$ yields Barker's exact G.f.
3. **Linear recurrence (§3, L44–52):**
   - Exponent count in $D(x)$ verified: $(1-x) \cdot [(1-x)(1+x+x^2)] \cdot [(1+x)(1-x+x^2)] \cdot [(1-x)(1+x)] \cdot (1+x^2) = (1-x)(1-x^6)(1-x^4) = 1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}$.
   - Multiplying by $D(x)$ gives $D(x)A(x) = x^3 - x^4 + x^5 + x^7$ of degree $7$.
   - Extracting $[x^n]$ for all $n \ge 8$ (hence all $n > 11$, with $a(k)=0$ for $k \le 0$) yields $a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11)$.

No gaps, edge-case errors, or hidden assumptions found.

---

## 4. Independent Verifier Audit (`notes/check-check-1.py`)

- **AST float audit:** `FLOAT_CONSTANTS: 0 []` (strictly exact integer/polynomial arithmetic via `sympy`).
- **Execution:** Re-ran `.venv/bin/python -u targets/oeis-A026923/notes/check-check-1.py` -> exit code `0`, `OVERALL: PASS`.
- **Checks confirmed:** Exact symbolic equivalence of $F(x,1)$, $F(x,-1)$, $\frac{F(x,1)-F(x,-1)}{2}$, $D(x)$, $N(x)$; direct DP enumeration of partitions for $1 \le n \le 120$ matching Taylor coefficients of $A(x)$ and all 55 official OEIS `DATA` terms; alternate OEIS bijection $a(n+5)$ verified for $1 \le n \le 115$; 11-term recurrence verified for $8 \le n \le 120$ (including all $n > 11$).

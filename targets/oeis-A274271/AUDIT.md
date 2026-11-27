# Adversarial Audit — `targets/oeis-A274271/`

- **Auditor:** `@audit-2` (blind adversarial audit; did NOT read author `verify.py` or author scratch notes)
- **Date (UTC):** `2026-11-27T11:48Z`
- **Verdict:** **PASS** (`written proof, internally audited`)

---

## 1. Statement & Primary-Source Fidelity

Verified verbatim against the official OEIS data mirror (`gh api repos/oeis/oeisdata/contents/seq/A274/A274271.seq`, `%I A274271 #12 Jun 21 2016 09:29:05`, offset `0,2`, 19 listed terms):
- **`NAME`:** `Number of partitions of 3^n into at most four parts.` — matches `TARGET.md` L14 verbatim.
- **`FORMULA`:**
  - `Coefficient of x^(3^n) in 1/((1-x)*(1-x^2)*(1-x^3)*(1-x^4)).`
  - `Conjectures (Start)`
  - `a(n) = ((3+3^n)^2*(9+3^n))/144 for n>1.`
  - `a(n) = 40*a(n-1)-390*a(n-2)+1080*a(n-3)-729*a(n-4) for n>4.`
  - `G.f.: (1-37*x+288*x^2-405*x^3-81*x^4) / ((1-x)*(1-3*x)*(1-9*x)*(1-27*x)).`
  - `(End)`
  Matches `TARGET.md` L16–22 and `PROOF.md` L5–11 verbatim.
- **`DATA`:** `1,3,18,225,4410,105903,2746098,73140525,1965803130,52995903003,1430162760978,38607856205625,1042353276205050,28143008896575303,759856474192364658,20516081909157771525,553933825501236490170,14956209814120079146803,403817633711525094117138` (offset `0,2`).

---

## 2. Novelty & Compendia Cross-Check

- **Gate 2 receipts:** All three independent Gate 2 checks passed (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
- **OEIS compendia snapshots:** Independently checked all 7 OEIS compendia snapshots under `watch/snapshots/` (`zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, `cohen-zenodo-24384895-oeis-ids.md`, `mylesparslow-conjecture-ledger.md`, `su-zenodo-24366920-oeis-ids.md`, `su-zenodo-23760779-oeis-ids.md`, `zenodo-2026-oeis-compendia-ids.md`): **`0` hits** for `A274271`.
- **Official OEIS mirror status:** Barker's Jun 17 2016 closed form, recurrence, and rational G.f. remain inside `Conjectures (Start) ... (End)` in `A274271.seq` rev. 12.

---

## 3. Line-by-Line Proof Audit (`PROOF.md`)

1. **Generating function & partial fraction decomposition (§1, L19–31):**
   - By Ferrers conjugation, partitions of $m$ into $\le 4$ parts correspond bijectively to partitions of $m$ with parts in $\{1,2,3,4\}$, giving $a(n) = [x^{3^n}] F(x)$ with $F(x) = \frac{1}{(1-x)(1-x^2)(1-x^3)(1-x^4)}$ and $a(0) = [x^1]F(x) = 1$.
   - Denominator factorization $(1-x)(1-x^2)(1-x^3)(1-x^4) = (1-x)^4(1+x)^2(1+x^2)(1+x+x^2)$ and the exact partial fraction decomposition (L24) plus cleared-denominator polynomial identity (L26–30) verified symbolically over $\mathbb{Q}(x)$.
2. **Exact coefficient extraction at $m = 3^n$ for $n \ge 1$ (§2, L37–61):**
   - For every $n \ge 1$, $m = 3^n$ is odd and divisible by $3$.
   - Term-by-term extraction verified:
     - $x = 1$ poles: $\frac{2m^3 + 30m^2 + 135m + 175}{288}$;
     - $x = -1$ poles (since $(-1)^m = -1$): $-\frac{1}{8} - \frac{m+1}{32} = \frac{-9m - 45}{288}$;
     - $x = \pm i$ poles (since $m$ is odd): $0$;
     - primitive cube-root poles ($\frac{1+x}{9(1+x+x^2)} = \frac{1-x^2}{9(1-x^3)}$ and $3 \mid m$): $\frac{1}{9} = \frac{32}{288}$.
   - Summing yields $a(n) = \frac{2m^3 + 30m^2 + 126m + 162}{288} = \frac{m^3 + 15m^2 + 63m + 81}{144} = \frac{(3+m)^2(9+m)}{144} = \frac{(3+3^n)^2(9+3^n)}{144}$ for all $n \ge 1$ (hence all $n > 1$), proving Conjecture 1.
3. **Rational G.f. & 4-term linear recurrence (§3, L67–82):**
   - At $n=0$, the closed form evaluates to $\frac{160}{144} = \frac{10}{9}$ while $a(0)=1$, giving the exact correction $-\frac{1}{9}$.
   - Summing the four geometric series yields $G(x) = -\frac{1}{9} + \frac{1}{144}(\frac{81}{1-x} + \frac{63}{1-3x} + \frac{15}{1-9x} + \frac{1}{1-27x}) = \frac{1 - 37x + 288x^2 - 405x^3 - 81x^4}{(1-x)(1-3x)(1-9x)(1-27x)}$, proving Conjecture 3.
   - Expanding the denominator gives $1 - 40x + 390x^2 - 1080x^3 + 729x^4$; since the numerator has degree $4$, extracting $[x^n]$ for all $n > 4$ gives $a(n) = 40a(n-1) - 390a(n-2) + 1080a(n-3) - 729a(n-4)$, proving Conjecture 2.

No gaps, edge-case errors, or hidden assumptions found.

---

## 4. Independent Verifier Audit (`notes/check-check-2.py`)

- **AST float audit:** `FLOAT_CONSTANTS: 0 []`, `FLOAT_CALLS: 0 []`.
- **Execution:** Re-ran `.venv/bin/python -u targets/oeis-A274271/notes/check-check-2.py` -> exit code `0`, `PASS`.
- **Checks confirmed:** Direct DP partition counts $[x^{3^n}]F(x)$ for $0 \le n \le 8$ (up to $x^{6561}$) and all 19 official OEIS `DATA` terms ($n=0..18$); exact partial fraction & cleared-denominator polynomial identity in $\mathbb{Q}(x)$; pole-by-pole extraction for $n=1..25$; rational G.f., denominator expansion, and 4-term recurrence for $n=0..40$.

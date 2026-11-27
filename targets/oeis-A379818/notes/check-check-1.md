# Independent Check Report: `oeis-A379818` (`check-1`)

- **Checked at (UTC):** `2026-11-26T22:49:32Z`
- **Checker:** `check-1`
- **Verdict:** **PASS** (primary-source fidelity and independent exact verification of all definitions, lemma, induction identities, and 10,000 $(m, k)$ cases)

## 1. Primary-Source Fidelity Check

- **Primary sources fetched:**
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A379818&fmt=json`), revision `8` (`2026-02-26T16:45:49-05:00`).
  - Live OEIS JSON API (`https://oeis.org/search?q=id:A025480&fmt=json`), revision `235` (`2025-11-05T15:21:50-05:00`).
- **Exact fields checked in `A379818`:**
  - `name`: `a(2n+1) = a(n) for n >= 0, a(2n) = a(n) + a(n - 2^f(n)) + a(2n - 2^f(n)) + a(A025480(n-1)) for n > 0 with a(0) = 1 where f(n) = A007814(n).` (`offset: "0,3"`)
  - `formula`: `Conjecture: a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k) for m >= 0, k >= 0 with a(0) = 1.`
  - `data`: 62 terms (`1,1,4,1,10,...`).
- **Exact fields checked in `A025480`:**
  - `name`: `a(2n) = n, a(2n+1) = a(n).` (`offset: "0,5"`)
- **Word-for-word comparison against `TARGET.md` and `PROOF.md`:**
  - Exact recurrences, `a(0) = 1`, `A025480` recurrence, `f(n) = v_2(n)`, quantifiers `m >= 0, k >= 0`, and binomial sum match verbatim. Zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Check

- **Isolation:** Written strictly from the live OEIS `A379818` and `A025480` JSON records and the proof steps in `PROOF.md`, without reading `verify.py`.
- **Verifier script:** `targets/oeis-A379818/notes/check-check-1.py` (exact integer arithmetic).
- **Verified claims & lemmas:**
  1. **`A025480` & Shift Lemma:** Computed `A025480` from `b(2r)=r, b(2r+1)=b(r)` up to `10,000`, matched all 84 published OEIS `A025480` data terms, and verified `b(2^r(2k+1) - 1) == k` for 755 `(r, k)` pairs.
  2. **`A379818` & Conjecture Formula:** Computed `A379818` from its defining recurrence up to `10,000`, matched all 62 published OEIS `A379818` data terms, and verified Kurkov's conjecture formula for all `10,000` `(m, k)` pairs with `2^m(2k+1) <= 10,000` (including `m=0`, `m=1`, `k=0`, `k=1`).
  3. **Inductive Step Pascal Identities:** Verified `c(m,0) = m+1 = c(m-1,0) + 1`, `c(m,m) = m+1 = 1 + c(m-1,m-1)`, and `c(m-1,j) + c(m-1,j-1) = c(m,j)` for all `1 <= m <= 30` and `1 <= j < m`.

### Command & Raw Output

Command:
```bash
.venv/bin/python targets/oeis-A379818/notes/check-check-1.py
```

Raw output:
```text
A025480 data (84 terms) & Lemma (755 pairs): OK
A379818 data (62 terms) & Kurkov formula (10000 (m,k) pairs up to n=10000): OK
Pascal boundary & interior identities (1<=m<=30): OK
PASS
```

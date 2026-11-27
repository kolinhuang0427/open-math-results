# Adversarial Audit Report (`audit-1`): `targets/oeis-A132411/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A132411` — Peter Bala (May 10 2025) $q$-series expansion conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and live OEIS `A132411` (rev. 80, `2026-01-22T07:45:32-05:00`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Fidelity
- Verified verbatim against live OEIS `A132411` JSON (rev. 80, `2026-01-22T07:45:32-05:00`, offset `0,3`):
  - `NAME`: `a(0) = 0, a(1) = 1 and a(n) = n^2 - 1 with n >= 2.`
  - `COMMENTS`: `Conjecture: the sequence terms are the exponents in the expansion of the q-series Sum_{n >= 0} q^(2*n) * Product_{k >= 2*n+2} 1 - (-q)^k = 1 + q^3 + q^8 + q^15 + q^24 + .... - _Peter Bala_, May 10 2025`
- **Clarification on `a(1) = 1`:** Bala's displayed expansion `1 + q^3 + q^8 + q^15 + q^24 + ...` omits $q^1$, i.e., its exponents are $\{0\} \cup \{m^2 - 1 : m \ge 2\} = \{m^2 - 1 : m \ge 1\}$ (`A005563`, all terms of `A132411` except $a(1) = 1$). `PROOF.md` (lines 6–8) proves the exact displayed $q$-series identity $F(q) = 1 + \sum_{m \ge 2} q^{m^2 - 1}$ in $\mathbb{Z}[[q]]$ and explicitly notes that $a(1) = 1$ does not occur as an exponent ($[q^1]F(q) = 0$). Also checked live OEIS `A005563` (rev. 549) — no overlap with Bala's $q$-series identity.

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)
- **Step 1 (lines 12–32):** Substituting $x = -q$ gives $F(q) = (x; x)_\infty \sum_{n \ge 0} \frac{x^{2n}}{(x; x)_{2n+1}}$ in $\mathbb{Z}[[x]]$ (well-defined since each $1 - x^k$ is a unit and the $n$-th summand has valuation $2n$). For $E(t) = \sum_{r \ge 0} \frac{t^r}{(x; x)_r} \in \mathbb{Q}[[x]][[t]]$, the identity $E(t) - E(tx) = t E(t)$ yields $E(t) = E(tx^N)/(t; x)_N \to 1/(t; x)_\infty$ $(x, t)$-adically. Specializing $t = \pm x \in x\mathbb{Z}[[x]]$ and taking $(E(x) - E(-x))/2$ yields $x F(q) = \frac{1}{2}\bigl(1 - (x; x)_\infty/(-x; x)_\infty\bigr)$ in $\mathbb{Q}[[x]]$ (and $\mathbb{Z}[[x]]$). Airtight.
- **Step 2 (lines 34–62):** For $N \ge 1$, $P_N(z) = \prod_{k=1}^N (1 + z x^{2k-1})(1 + z^{-1} x^{2k-1}) = \sum_{m=-N}^N c_{N,m}(x) z^m$ satisfies $(x^{2N} + zx)P_N(zx^2) = (1 + zx^{2N+1})P_N(z)$ in $\mathbb{Z}[x, x^{-1}][z, z^{-1}]$ (verified via $(x^{2N}+zx)(1+z^{-1}x^{-1}) = (1+zx)(1+z^{-1}x^{2N-1})$). Equating $[z^m]$ for $-N < m \le N$ gives $(1 - x^{2N+2m}) c_{N,m} = x^{2m-1}(1 - x^{2N-2m+2}) c_{N,m-1}$ with both polynomial factors nonzero since $2N+2m \ge 2$ and $2N-2m+2 \ge 2$; backward induction from $c_{N,N} = x^{N^2}$ gives $c_{N,m} = \frac{(x^2;x^2)_{2N}}{(x^2;x^2)_{N+m}(x^2;x^2)_{N-m}} x^{m^2}$ for all $-N \le m \le N$. Multiplying $P_N(-1)$ by $(x^2;x^2)_N$, noting both quotients $\frac{(x^2;x^2)_{2N}}{(x^2;x^2)_{N+m}}$ and $\frac{(x^2;x^2)_N}{(x^2;x^2)_{N-m}}$ lie in $1 + x^{2(N-|m|+1)}\mathbb{Z}[[x]]$ for $N \ge |m|$ (both when $m \ge 0$ and when $m < 0$, since $2(N+1) \ge 2(N-|m|+1)$) while the $m$-th summand has $x$-adic valuation $\ge m^2$, and letting $N \to \infty$ gives $\prod_{k \ge 1}(1-x^{2k})(1-x^{2k-1})^2 = 1 + 2\sum_{m \ge 1}(-1)^m x^{m^2}$. Rewriting via $(x^2;x^2)_\infty = (x;x)_\infty(-x;x)_\infty$ yields $(x;x)_\infty/(-x;x)_\infty = 1 + 2\sum_{m \ge 1}(-1)^m x^{m^2}$. Airtight.
- **Step 3 (lines 64–73):** Substituting into Step 1 gives $x F(q) = \sum_{m \ge 1}(-1)^{m-1} x^{m^2}$; dividing by $x = -q$ in the integral domain $\mathbb{Z}[[x]]$ and noting $(-1)^{m-1}(-1)^{m^2-1} = (-1)^{m(m+1)} = +1$ yields $F(q) = \sum_{m \ge 1} q^{m^2 - 1} = 1 + \sum_{m \ge 2} q^{m^2 - 1}$ in $\mathbb{Z}[[q]]$. Airtight.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Executed `.venv/bin/python -u targets/oeis-A132411/notes/check-check-2.py` -> exit code `0`, `PASS` (pure exact integer and SymPy polynomial arithmetic; verified $F(q) \equiv 1 + \sum_{m \ge 2} q^{m^2-1} \pmod{q^{121}}$, Step 1 reduction and Gauss theta identity mod $x^{121}$, and Step 2 finite $P_N(z)$, $c_{N,m}$, and $P_N(-1)$ identities for $1 \le N \le 8$; minor dead-code initialization on L69–73 immediately overwritten on L75 does not affect the check).
- **Gate 2 novelty receipts:** `watch-6` (`#729`) and `watch-5` (`#753`) clear (absent from `zenodo-23112421-oeis-ids.md`); `@watch-1` will also verify at Gate 3.
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).

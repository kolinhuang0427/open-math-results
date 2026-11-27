# Blind Audit Report: `oeis-A121754`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:47Z` (initial FAIL) / `2026-11-27T09:59Z` (re-audit **PASS**)
**Verdict:** **PASS** (after author patch `#547` resolving the $n = 6$ boundary gap; Charter label: `"written proof, internally audited"`)

## 1. Primary-Source Fidelity (PASS)
Verified verbatim against live OEIS JSON API (`https://oeis.org/search?q=id:A121754&fmt=json`, revision `4`, `2022-07-26T11:32:34-04:00`, offset `1,3`):
- **NAME, FORMULA (established recurrence for $a(n)$), and Mathar's Jul 26 2022 conjectured recurrence ($C_0(n), \dots, C_5(n)$ for $n \ge 6$)** in `TARGET.md` and `PROOF.md` match the live OEIS record character-for-character.
- *Scope note:* `PROOF.md` establishes Mathar's conjectured recurrence directly from the established OEIS `FORMULA` recurrence $a(n) = (2n-3)a(n-1) - (n-1)(n-3)a(n-2) + (n-2)! f(n)$ ($n \ge 3$, $a(1) = 0, a(2) = 1$).

## 2. Line-by-Line Mathematical Audit of `PROOF.md`
1. **Step 1 (lines 17–32) — PASS:**
   - $D(k) := a(k) - k a(k-1)$ satisfies $D(k) - (k-3) D(k-1) = (k-2)! f(k)$ for $k \ge 3$, with $D(3) = 3 = 0!(3-2)f(3)$, telescoping to $D(k) = (k-3)! S(k)$ for all $k \ge 3$.
   - Induction for $S(2r) = (r-1)^2(4r-1)$ ($r \ge 2$) and $S(2r+1) = r^2(4r-1)$ ($r \ge 1$) is completely rigorous.
2. **Step 2 (lines 34–48) — PASS:**
   - The operator factorization $M(n) = \sum_{i=0}^4 e_i(n) D(n-i)$ holds identically in $\mathbb{Z}[n]$.
3. **Step 3 (lines 50–76) — FAIL at $n = 6$ (all $n \ge 7$ PASS):**
   - For odd $n = 2r + 1$ ($r \ge 3$, i.e., $n \ge 7$): all indices $n-i \ge 3$ stay inside the proved domains of $S(2r')$ ($r' \ge 2$) and $S(2r'+1)$ ($r' \ge 1$), and $M(2r+1) = (2r-6)! P_{\mathrm{odd}}(r) = 0$ is completely rigorous.
   - For even $n = 2r$ with $r \ge 4$ (i.e., $n \ge 8$): all indices $n-i \ge 4$ stay inside the proved domains, and $M(2r) = (2r-7)! P_{\mathrm{even}}(r) = 0$ is completely rigorous.
   - **BLOCKING PROOF GAP AT $n = 6$ ($r = 3$, lines 51–63):**
     Lines 54 and 59–61 assert `M(6) = P_even(3)`, where
     $$P_{\mathrm{even}}(r) = e_0(2r)(2r-3)(2r-4)(2r-5)(2r-6) S(2r) + \dots + e_3(2r)(2r-6) S(2r-3) + e_4(2r) S(2r-4).$$
     This identity does **not** follow from substituting $D(k) = (k-3)! S(k)$ into $M(6)$: at $r = 3$, **every** term of $P_{\mathrm{even}}(r)$ contains a factor of $(2r - 6) = 0$ (explicitly in the first four terms and inside $e_4(2r)$ in the fifth), so $P_{\mathrm{even}}(3) = 0$ trivially regardless of the value of $M(6)$, whereas substituting $D(k) = (k-3)! S(k)$ into $M(6)$ gives
     $$M(6) = e_0(6)\cdot 3!\,S(6) + e_1(6)\cdot 2!\,S(5) + e_2(6)\cdot 1!\,S(4) + e_3(6)\cdot 0!\,S(3),$$
     which has no $(2r-6)$ factor (it corresponds to $P_{\mathrm{even}}(r)/(2r-6)$ evaluated at $r = 3$, not $P_{\mathrm{even}}(3)$).
   - **EGF D-finiteness (line 76) — PASS:** Multiplying $M(n) = 0$ by $x^{n-5}/(n-5)!$ and summing over $n \ge 6$ yields $\sum_{j=0}^5 C_j(\theta+5) \hat{y}^{(5-j)}(x) = \text{poly}(x)$ with nonzero leading $\hat{y}^{(6)}$ coefficient $16x(1-x)^2(1+x)$, and differentiating eliminates the polynomial RHS.

## 3. Independent Mechanical Verification
Ran `.venv/bin/python targets/oeis-A121754/notes/check-check-1.py`: exit `0`, raw `PASS` (including direct check $M(6) = 0$, Steps 1–3 symbolic identities, and order-6 EGF ODE).

## 4. Action Required for Re-Audit
Fix the $n = 6$ case in `targets/oeis-A121754/PROOF.md` (lines 51–63): restrict the $(2r-7)! P_{\mathrm{even}}(r)$ formula strictly to even $n = 2r \ge 8$ ($r \ge 4$), and settle $n = 6$ cleanly (either by direct arithmetic verification of $M(6) = 0$ from $a(1),\dots,a(6)$ or $D(3),\dots,D(6)$, or by dividing out $(2r-6)$ from $P_{\mathrm{even}}(r)$ first), then re-ping `@audit-3`.

---

## 5. Re-Audit After Author Patch (`2026-11-27T09:59Z`) — **PASS**

Re-inspected patched `targets/oeis-A121754/PROOF.md` (lines 1–79) after `#547` and independently verified every patched number and differential-operator coefficient using exact SymPy arithmetic (zero floats) plus re-running `.venv/bin/python targets/oeis-A121754/notes/check-check-1.py`:

1. **$n = 6$ boundary fix (lines 51–54) — PASS:** Verified $e_4(6) = 0$, $(e_0(6), e_1(6), e_2(6), e_3(6)) = (112, -441, -2121, 3325)$, $(D(6), D(5), D(4), D(3)) = (264, 56, 7, 3)$, and $M(6) = 112 \cdot 264 - 441 \cdot 56 - 2121 \cdot 7 + 3325 \cdot 3 = 29568 - 24696 - 14847 + 9975 = 0$.
2. **Domain restriction for $n \ge 7$ (lines 55–79) — PASS:** $M(2r) = (2r-7)! P_{\mathrm{even}}(r)$ is now strictly restricted to $r \ge 4$ ($n \ge 8$), and $M(2r+1) = (2r-6)! P_{\mathrm{odd}}(r)$ to $r \ge 3$ ($n \ge 7$), so all factorials and $S(k)$ evaluations lie strictly inside their proved domains.
3. **EGF D-finiteness (line 79) — PASS:** Independently verified in SymPy with $a(0) := 0$ that $M(5) = \sum_{j=0}^5 C_j(5) a(5-j) = 339$, $L[\hat{y}](x) = \sum_{m \ge 0} M(m+5)\frac{x^m}{m!} = 339$ is an exact order-6 linear ODE with polynomial coefficients whose $\hat{y}^{(6)}(x)$ coefficient is $16x(x-1)^2(x+1) \not\equiv 0$ (its $x^1$ term $16x$ arises uniquely from $C_0(m+5) = 16m + 96$, and $j=0,\dots,3$ combine to $16x - 16x^2 - 16x^3 + 16x^4 = 16x(x-1)^2(x+1)$), and differentiating once yields a non-trivial homogeneous order-7 polynomial-coefficient ODE $\frac{d}{dx} L[\hat{y}](x) = 0$.
4. **Independent checker re-run:** `.venv/bin/python targets/oeis-A121754/notes/check-check-1.py` exited `0` with raw output `PASS`.

**Final Verdict:** **PASS** (`"written proof, internally audited"`). Handed off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`).

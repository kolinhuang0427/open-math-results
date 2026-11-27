# Adversarial Audit Report: `targets/oeis-A091524/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T09:04Z` (re-audit after L4–5 / §2 L27 fix)
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary sources:
  - OEIS `A091524` (`rev #27`, `2025-02-16`), `A028982` (`rev #156`), `A006337` (`rev #104`), `A001521` (`rev #105`);
  - Eric Weisstein's MathWorld page *Graham-Pollak Sequence* (`https://mathworld.wolfram.com/Graham-PollakSequence.html`, the sole reference linked on OEIS `A091524`).
- `targets/oeis-A091524/TARGET.md`
- `targets/oeis-A091524/PROOF.md` (post-patch)
- `targets/oeis-A091524/notes/check-check-3.md` and `targets/oeis-A091524/notes/check-check-3.py`
- Confirmed no `targets/oeis-A091524/CONTESTED.md` exists, and Gate 2 PASS receipts from `watch-1`, `watch-5` (`#51`), and `watch-6`.

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Verification of Prior FAIL Fix (Resolved)

- **`PROOF.md` lines 4–5 and Section 2 line 27:** The primary-source Graham–Pollak recurrence $u_{r+1}^{(m)} = \lfloor \sqrt{2 u_r^{(m)}(u_r^{(m)} + 1)} \rfloor$ (OEIS `A001521` / MathWorld *Graham–Pollak Sequence*) is now explicitly stated in the Theorem, and Section 2 line 27 proves rigorously for all integers $u \ge 0$ that $\lfloor \sqrt{2u(u+1)} \rfloor = \lfloor \sqrt{2}(u + \frac{1}{2}) \rfloor$ via $2(u + \frac{1}{2})^2 = 2u(u+1) + \frac{1}{2}$ and the absence of integer squares in $(2u(u+1),\, 2u(u+1) + \frac{1}{2}]$. Verified exact.

---

## 3. Full Independent Mathematical & Mechanical Verification (PASS)

1. **Primary-Source Fidelity (PASS):**
   - Live OEIS `A091524` (rev 27, `2025-02-16`) still marks Kurkov's Apr 25 2024 formula `a(n) = sqrt(A028982(n)/A006337(n))` as `Conjecture:`.
   - Indexing $d_j^{(m)} = u_{2j+2}^{(m)} - 2u_{2j}^{(m)}$ ($j \ge 1$) matches MathWorld's $0$-based $b_j = a_{2j+1} - 2a_{2j-1}$ (`a_0 = m`) and OEIS `A091524`'s examples verbatim; OEIS `A028982` and `A006337` match live OEIS verbatim.
2. **Sections 1–4 Mathematical Proof (PASS):**
   - **§1:** Beatty partition $B_1(k) = k + \lfloor k/\sqrt{2} \rfloor$, $B_2(k) = k + \lfloor k\sqrt{2} \rfloor$ and exact ranks $\tau_{B_1(k)} = k$, $\tau_{B_2(k)} = k\sqrt{2}$ in $S = \mathbb{Z}_{\ge 1} \cup \sqrt{2}\mathbb{Z}_{\ge 1}$ verified airtight.
   - **§2:** Equivalence $\lfloor \sqrt{2u(u+1)} \rfloor = \lfloor \sqrt{2}(u+\frac{1}{2}) \rfloor$, base case $r = 1$, exhaustive case split ($r \ge 2$ with $K \in \mathbb{Z}_{\ge 1}$; $r=1, \tau_m=k\sqrt{2}$ with $K=k$; $r=1, \tau_m=k$ with $K = k/2, 2K = k$), strict inequalities in Cases 1 and 2 ($\alpha < 1/2$ and $\alpha > 1/2$), integer cancellation in $d_j^{(m)} = \lfloor 2^j k\sqrt{2} \rfloor - 2\lfloor 2^{j-1} k\sqrt{2} \rfloor$, telescoping binary expansion $\alpha(m) = k\sqrt{2} - \lfloor k\sqrt{2} \rfloor$, and $a(B_1(k)) = a(B_2(k)) = k$ verified airtight.
   - **§3–4:** Evaluations $c(B_1(k)) = k^2$, $c(B_2(k)) = 2k^2$, $f(B_1(k)) = 1$, $f(B_2(k)) = 2$, and conclusion $a(n) = \sqrt{\mathrm{A028982}(n)/\mathrm{A006337}(n)}$ for all $n \ge 1$ verified airtight.
3. **Independent Verifier Execution (PASS):**
   - Re-executed `.venv/bin/python targets/oeis-A091524/notes/check-check-3.py`: exit code `0`, `PASS` (pure exact $\mathbb{Q}(\sqrt{2})$ arithmetic, zero floats, verifying Beatty partition, Graham–Pollak recurrence, all 75 OEIS `A091524` terms, 54 `A028982` terms, 105 `A006337` terms, and Kurkov's identity through $n \le 5{,}000$).

---

## 4. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python targets/oeis-A091524/notes/check-check-3.py` and paths `targets/oeis-A091524/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.

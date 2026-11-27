# Adversarial Audit Report: `targets/oeis-A286044/`

- **Auditor:** `audit-1`
- **Audited at (UTC):** `2026-11-27T08:50Z` (re-audit after L39 fix)
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`

---

## 1. Strict Isolation Record

Inspected ONLY:
- Live primary sources: OEIS `A286044` (`https://oeis.org/search?q=id:A286044&fmt=text`, rev `#8`, `2026-02-19`), `A003160` (rev `#61`, `2026-03-10`), and `A010060` (rev `#619`, `2026-10-18`).
- `targets/oeis-A286044/TARGET.md`
- `targets/oeis-A286044/PROOF.md`
- Prior `targets/oeis-A286044/AUDIT.md`
- `targets/oeis-A286044/notes/check-check-2.md` and `targets/oeis-A286044/notes/check-check-2.py`
- Confirmed no `targets/oeis-A286044/CONTESTED.md` exists.

Did **not** inspect `verify.py` or any author scratch `notes/`.

---

## 2. Verification of Prior FAIL Fix (Resolved)

- **`PROOF.md` L39:** The single prose error flagged by the prior audit is fixed. Line 39–40 now states accurately:
  > *"Starting from $t_0 = 0$, the sequence $t_0, t_1, \dots, t_{j_m}$ makes $j_m$ steps in $\{0, 1\}$, of which $\pi_{\bar{V}}(j_m) = m - 1$ steps stay unchanged and the remaining $\pi_V(j_m)$ steps change bit: $\pi_V(j_m) = j_m - (m - 1) = 2v(m) - m$."*
  Verified exact for all $m \ge 1$ (including boundary case $m = 1$, where $j_1 = 1$, $\pi_{\bar{V}}(1) = 0$, $\pi_V(1) = 1$).

---

## 3. Full Independent Mathematical & Mechanical Verification

1. **Primary-Source Fidelity (PASS):**
   - Live OEIS `A286044` (rev 8, offset `1`) matches `TARGET.md` and `PROOF.md` verbatim: Velin Yanev's Feb 16 2026 formula `a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160` remains explicitly marked `Conjecture:`.
   - Live OEIS `A003160` (rev 61, offset `1,4`) gives `a(1) = a(2) = 1, a(n) = n - a(a(n-1)) - a(a(n-2))` (note Yanev's Jan 27 2026 formula `a(n) = A003159(n+1) - (n+1)` is listed without proof on `A003160`, and `PROOF.md` §3 proves it cleanly from first principles).
   - Live OEIS `A010060` (offset `0,1`) matches $t_k = s_2(k) \bmod 2$.
2. **Line-by-Line Proof Verification (PASS):**
   - **§1 (Facts 1–2):** $\bar{V} = 2V$, $\pi_{\bar{V}}(N) = \pi_V(\lfloor N/2 \rfloor)$, $\pi_V(N) + \pi_V(\lfloor N/2 \rfloor) = N$, and $s_2(j) = s_2(j+1) - 1 + v_2(j+1) \implies (t_{j+1} \neq t_j \iff j+1 \in V)$ all verified exact for all $j \ge 0, N \ge 0$.
   - **§2 (Positions of `1`s in `A286044`):** Pairwise disjointness of all `011` blocks at even $2m$ with $(t_m, t_{m+1}) = (0,1)$ and $t_{2m+3} = 0$ makes `{011 -> 0}` unambiguous (no overlap and no newly created `011`). Surviving `1`s correspond bijectively and in strictly increasing order to $j_m = 2v(m)-1$ ($m \ge 1$); every deleted pair $(2i+1, 2i+2)$ lies strictly before ($i < j_m$) or strictly after ($i > j_m$) the surviving `1`; both parity cases yield 1-based position $2v(m) + m = \pi_V(4v(m))$, giving $a(n) = \mathbf{1}_{v(n)\text{ even}}$ for all $n \ge 1$.
   - **§3 (Closed form for `A003160`):** $g(0)=0$, $g(n) = v(n+1) - (n+1) = \pi_{\bar{V}}(v(n+1))$ satisfies $g(n)-g(n-1) \in \{0,1\}$ for all $n \ge 1$, contiguous level-set partition $I_y = [y+2g(y-1),\, y+2g(y)]$ of size $1$ or $3$ ($y \ge 1$), base cases $n=1,2,3$, and all three block-position cases for $n \ge 4$ ($y \ge 2$; $|I_1|=3$ guarantees $y \ge 3$ whenever $|I_{y-1}|=1$, so $y-2 \ge 1$ is always valid). Verified $1 \le g(k) < k$ for all $k \ge 2$, closing the strong induction for $b(n) = g(n)$.
   - **§4 (Double-difference identity):** Verified both directions of $b(b(m)) - b(b(m-1)) = 1 \iff v(m+2)\text{ even}$ for all $n > 3$ ($m = n-2 \ge 2$). In ($\Leftarrow$), confirmed $v(4)=5, v(5)=7, v(6)=9, v(7)=11, v(8)=12$, so $n \ge 8$, $k \ge 6$, $m \ge 6$, $y = b(m) \ge b(6) = 4 \ge 2$, and all index bounds $2k-3 \ge 9, k-1 \ge 5, y-1 \ge 3$ hold strictly.
3. **Independent Verifier Execution (PASS):**
   - Ran `.venv/bin/python -u targets/oeis-A286044/notes/check-check-2.py`: exit code `0`, `PASS` in `0.294s` (confirms all 86 OEIS prefix terms and every section identity through $n \le 120{,}000$).

---

## 4. Handoff

Handed off directly to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 novelty check (within 1 hour of reporting), with instructions to mention `@coordinator` once Gate 3 clears with verification command `.venv/bin/python -u targets/oeis-A286044/notes/check-check-2.py` and paths `targets/oeis-A286044/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

# Independent Verification Report: `targets/oeis-A286044/`

- **Reviewer:** `@check-2`
- **Primary Sources Verified (Live OEIS JSON, `https://oeis.org/search?q=id:...&fmt=json`):**
  - **OEIS `A286044`** (rev. `8`, `2026-02-19T22:02:10-05:00`, offset `1`):
    - Name: `{011->0}-transform of the Thue-Morse word A010060.`
    - Comment: `This is also the {110->1}-transform of A010060.`
    - Formula: `Conjecture: a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160. - _Velin Yanev_, Feb 16 2026`
    - Example: `As a word, A010060 = 0110100110010110100101100..., and replacing each 011 by 0 gives 00100001001001000010000100001...`
  - **OEIS `A003160`** (rev. `61`, `2026-03-10T09:26:09-04:00`, offset `1,4`): `a(1) = a(2) = 1, a(n) = n - a(a(n-1)) - a(a(n-2)).`
  - **OEIS `A010060`** (rev. `619`, `2026-10-18T01:10:44-04:00`, offset `0,1`): Thue–Morse sequence.
  - **OEIS `A003159`** (rev. `238`, `2026-05-30T16:39:44-04:00`, offset `1,2`): Numbers whose binary representation ends in an even number of zeros.
- **Primary-Source Fidelity:** **PASS (Verbatim Match, Zero Drift).**
  - `TARGET.md` and `PROOF.md` match the live OEIS definitions, offsets (`1`-indexed `a(n)` and `b(n)` vs `0`-indexed `t_k` for `A010060`), and Yanev's `n > 3` conjecture verbatim with zero quantifier, hypothesis, or edge-case drift.
- **Proof Audit (`PROOF.md`):** **PASS.**
  - **§1 (Facts 1–2):** $v_2(2k) = 1 + v_2(k)$ gives $\bar{V} = 2V$ and $\pi_V(N) + \pi_V(\lfloor N/2 \rfloor) = N$; $s_2(j) = s_2(j+1) - 1 + v_2(j+1)$ gives $t_{j+1} \ne t_j \iff j+1 \in V$. Exact.
  - **§2 (Positions of $1$s in `A286044`):** Disjointness of `011` occurrences at even indices $2m$ with $(t_m, t_{m+1})=(0,1)$ and $t_{2m+3}=0$ makes `{011 -> 0}` unambiguous; counting deleted pairs before surviving $1$s gives $1$-based index $2v(m)+m$ in both parity cases, matching the $m$-th even element $4v(m)$ of $V$ ($n = \pi_V(4v(m)) = 2v(m)+m$). Exact.
  - **§3 (Closed form for `A003160`):** $g(n) = v(n+1)-(n+1)$ has level sets $I_y = [y+2g(y-1), y+2g(y)]$ of size $1$ or $3$; all base cases ($n=1,2,3$) and block-position cases ($n \ge 4$) satisfy $b(n) = n - b(b(n-1)) - b(b(n-2))$, with $1 \le g(k) < k$ for $k \ge 2$ ensuring valid recursion. Exact.
  - **§4 (Double-difference identity):** Both directions $b(b(n-2)) - b(b(n-3)) = 1 \iff v(n)$ is even hold cleanly for all $n > 3$ ($m = n-2 \ge 2$). Exact.

## Independent Mechanical Check (`notes/check-check-2.py`)

- **Command Run:**
  ```
  .venv/bin/python -u targets/oeis-A286044/notes/check-check-2.py
  ```
- **Exit Code:** `0`
- **Raw Output:**
  ```
  [OEIS A286044 prefix + literal 011->0] PASS (86 OEIS terms, computed 160138 terms)
  [Section 1 Fact 1 & Fact 2] PASS up to 240200
  [Section 2 indicator & 2v(m)+m positions] PASS for 1<=n<=120000 (29999 surviving 1s)
  [Section 3 A003160 recurrence, prefix, closed form & I_y blocks] PASS for 1<=n<=120004
  [Main Theorem: a(n) = b(b(n-2)) - b(b(n-3))] PASS for ALL 4<=n<=120000
  PASS (all independent checks passed in 0.491s)
  ```

## Gate 2 / Contest Status & Handoff

- **Gate 2:** **PASS** (`targets/oeis-A286044/notes/novelty-gate2-watch-1.md`, `targets/oeis-A286044/notes/novelty-gate2-watch-5.md`; no `CONTESTED.md`).
- **Handoff:** Ready for `@audit-3`.

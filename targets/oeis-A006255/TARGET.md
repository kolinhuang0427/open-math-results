---
source: https://oeis.org/A006255 (OEIS A006255, revision 106, 2026-06-19)
status: reported
owner: attack-6
updated: 2026-11-26T23:54:00Z
identifiers: ["A006255", "Ron Graham", "Jaideep Padhi", "David A. Corneth", "b(n)^2 >= 2 * n", "171"]
---

# OEIS A006255 — Padhi (2026) Refinement of Graham Sequence Threshold

## Exact Statement
From OEIS **A006255** (Comments section, revision 106, 2026-06-19):
> "Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]"

where `a(n)` is R. L. Graham's sequence: "smallest m for which there is a sequence n = b_1 < b_2 < ... < b_t = m such that b_1*b_2*...*b_t is a perfect square", `A007913(n)` is the squarefree part of `n`, and `A006530(k)` is the greatest prime factor of `k` (`A006530(1) = 1`).

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-26T20:15:10Z – 2026-11-26T20:25:00Z
- **Sources Checked:**
  - `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A006255 "Ron Graham" "Graham's sequence"` -> 0 matches across 201 files.
  - Live OEIS entry `A006255` (rev 106, 2026-06-19) + `b006255.txt` (`n = 1..10000`).
  - `arXiv:2410.04728` (Kagey & Rajesh, 2024, `graham.tex`) — proves Wilson's conjecture `T(n) != 2` and `a(n) <= 2n`, does not address Padhi's `b(n)^2 >= 2n` threshold.
  - `arXiv:2504.19196` (Adenwalla, 2025, `main.tex`) — proves `a(n) = 2n <=> n prime or 6` and quotes Erdős–Selfridge (1992): `P(n) > sqrt(2n) + 1 => a(n) = n + P(n)`; does not close the `sqrt(2n) <= P(n) <= sqrt(2n) + 1` boundary case or mention `171`.
  - Web search: `"A006255" "Padhi" OR "b(n)^2 >= 2 * n" OR "171" "Graham"`.
- **Near Misses:** Erdős–Selfridge (Amer. Math. Monthly 99, 1992, Problem 6655, pp. 791–794) proves `P(n) > sqrt(2n) + 1 => a(n) = n + P(n)`, leaving open the boundary `sqrt(2n) <= P(n) <= sqrt(2n) + 1` (where `n = 171 = 9 * 19` sits!).
- **Not Covered:** Full text of Erdős–Selfridge (1992, JSTOR) not downloaded; quoted statement verified via `arXiv:2504.19196` (`main.tex` line 218).

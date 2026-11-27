---
source: https://oeis.org/A091524 (rev. 27, Feb 16 2025)
status: reported
owner: scout-6
updated: 2026-11-27T06:45:00Z
identifiers: [A091524, A028982, A006337, A003151, A003152, A001521, Graham-Pollak, Mikhail Kurkov]
---

# Target: OEIS A091524 (Kurkov 2024 Graham–Pollak / Beatty Ratio Conjecture)

## Verbatim Statement
From OEIS **A091524** (author: `_Eric W. Weisstein_`, Jan 18 2004; latest revision `#27`, `2025-02-16T08:32:52-05:00`), offset `1,3`:

- **Name:**
  > a(m) is the multiplier of sqrt(2) in the constant alpha(m) = a(m)*sqrt(2) - b(m), where alpha(m) is the value of the constant determined by the binary bits in the recurrence associated with the Graham-Pollak sequence.
- **Data (`offset 1`):**
  > 1,1,2,2,3,4,3,5,4,6,7,5,8,6,9,7,10,11,8,12,9,13,14,10,15,11,16,12,17,18,13,19,14,20,21,15,22,16,23,24,17,25,18,26,19,27,28,20,29,21,30,31,22,32,23,33,24,34,35,25,36,26,37,38,27,39,28,40,41,29,42,30,43,31,44
- **Formula (Conjecture):**
  > Conjecture: a(n) = sqrt(A028982(n)/A006337(n)). - _Mikhail Kurkov_, Apr 25 2024

## Gate 1 Novelty Receipt
- Checked at: `2026-11-27T06:00:23Z` – `06:44:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A091524 "Graham-Pollak" A028982 A006337`): 2 hits (`erdosproblems/problems.yaml` & `pulls.json`) discussing only Erdős Problem 482 (the binary digits of $\sqrt{2}$ from `u_1=1`); `0` hits on `A091524` or Kurkov's formula across all `522` files.
- `tools/arxiv_fetch.py query 'all:A091524 OR (all:"Graham-Pollak" AND all:"sqrt(2)")'`: 1 hit (`arXiv:0902.4168v2`, Thomas Stoll 2009), checked `gpseq.tex`: cites `A091524` as background only and studies $\varepsilon$-perturbations; does not state or prove Kurkov's 2024 formula.
- Zenodo API (`zenodo.org/api/records?q=A091524&size=5`): `0` hits.
- Crossref API (`api.crossref.org/works?query=A091524&rows=3`): `0` hits.
- GitHub (`gh search code A091524`): only `loda-lang/loda-programs` (`A091524.asm`), `archmageirvine/joeis` (`A091525.java`), `Anon52MI4/oeis-alien`, and unrelated repos; no proof of Kurkov's formula.
- Web search (`"A091524" "sqrt(A028982" OR "Mikhail Kurkov"`): only OEIS `A091524`, no proof found.
- Live OEIS `A091524` (rev 27, `2025-02-16`): formula remains marked `Conjecture:`.
- Not covered: closed-access venues or private repos.

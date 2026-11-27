# Gate 3 Novelty Receipt (`watch-1`): `targets/benfield-2407.20048-conj5.3/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Target:** Brennan Benfield and Oliver Lippard, *"Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers"*, `arXiv:2407.20048v2` (`2025-01-30`), Section 5, Conjecture 5.3 (`\label{finite-orders}`), **rescoped strictly to clause (vi)** (*"infinite in all other cases"*), per `CONTESTED.md` & `notes/contest-ruling-audit-1.md` (`partial-overlap-still-open`)
- **Audited Artifacts Verified:** `TARGET.md`, `COUNTEREXAMPLE.md`, `AUDIT.md` (`@audit-1` PASS), cmd `.venv/bin/python targets/benfield-2407.20048-conj5.3/notes/check-check-2.py`
- **Verdict:** **PASS for rescoped clause (vi) (Uncontested on clause (vi); prior `trureturing#9448` / PR `#9451` credit explicitly recorded for clause (v))**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2407.20048 ...` & `trureturing/files.txt`):** `0` matches in `1337isnot1337/solved-conjectures` (`08:49Z` rebuild) or any other repo except `the-omega-institute/trureturing` `Problems/pisano-order-range-refutation.md` (which addresses only clause (v) and explicitly leaves clause (vi) open).
2. **Live GitHub (`gh search issues "2407.20048"` & `gh search prs --repo the-omega-institute/trureturing "Benfield"`):** Only `trureturing#9448` / PR `#9451` (Conjecture 5.3(v)), `trureturing#23317` (open preregistration on Question 4.34, explicitly stating it does not settle Conjecture 5.3), and `trureturing#23099` / PR `#33413` (`2404.08193` Waring-gap Conjecture 10.4/10.5). No PR or issue addresses clause (vi) or $(a,b)=(3,4)$.
3. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2407.20048`):** `2407.20048v2` (`2025-01-30`) remains latest.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=10`):** `0` hits.

## Coverage Limits
- Journal publication *The Fibonacci Quarterly* 63(2) (2025), 240–258 (`doi:10.1080/00150517.2025.2460555`) is paywalled (`HTTP 403`) and unread beyond `arXiv:2407.20048v2`.

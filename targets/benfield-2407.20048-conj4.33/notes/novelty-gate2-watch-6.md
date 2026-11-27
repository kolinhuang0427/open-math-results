# Gate 2 Novelty Receipt (`watch-6`) — `targets/benfield-2407.20048-conj4.33/`

- **Checked UTC:** `2026-11-27T09:19:49Z`
- **Target:** Benfield–Lippard, `arXiv:2407.20048v2` Section 4.2, Conjecture 4.33 (`\label{even-K-exceptions}`), all even integers $K \in \mathbb{Z}$, all moduli $m > 3$
- **Verdict:** **PASS** (no settled or near-settled PR settles Conjecture 4.33; see near-miss disclosure below)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "even-K-exceptions" "4.33" "omega_K" "2407.20048"`
  - `"even-K-exceptions"`, `"omega_K"`, `"2407.20048"`: `0` hits across `608` snapshot files.
  - `"4.33"` hit only Lean toolchain `4.33.1` and unrelated files.
  - Note: in `watch/snapshots/discovered/the-omega-institute__trureturing.json`, `trureturing` has settled `D5/S1/Recurrence/LucasEvenDescent.lean` (Fiebig–Mbirika–Spilker Conj. 5.2), `D5/S1/Recurrence/LucasEvenPeriods.lean` (Fiebig–Mbirika–Spilker Q5.3–5.4), and `D5/S3/Arith/PisanoOrderRangeRefutation.lean` (Benfield–Lippard Conj. 5.3(v) only). None proves Conjecture 4.33.
- `gh search repos "2407.20048" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2407.20048" --limit 10 --json repository,number,title,state,url`:
  1. `the-omega-institute/trureturing#9448` (`closed`): Conjecture 5.3(v) only (`(a,b)=(3,2), m=13`). Unrelated.
  2. `the-omega-institute/trureturing#23099` (`open`): `arXiv:2404.08193` Conjecture 10.4. Unrelated.
  3. **Near-miss:** `the-omega-institute/trureturing#23317` (`open`, created `2026-10-28T20:05:07Z`): *"Open problem (preregistration): prove the complete dyadic-threshold answer to Benfield–Lippard Question 4.34 (arXiv:2407.20048) for positive even K"*.
     - Inspected full body via `gh api "repos/the-omega-institute/trureturing/issues/23317"`: `#23317` explicitly states *"neither the claim nor its negation has been proved in Lean"* / *"no Lean proof attempted"*, targets **Question 4.34** ($0 < K$, $4 \mid m$) rather than Conjecture 4.33 ($K \in \mathbb{Z}$, $m > 3$), and explicitly notes *"Conjecture 4.33 of the source is excluded as an already implied neighboring statement"*. Its 5-step prose outline combines Benfield–Lippard Theorem 4.28, Fiebig–Mbirika–Spilker (`arXiv:2408.14632v2`, Section 3 odd-modulus classification), and Renault's $\mathrm{lcm}$ laws to derive the dyadic threshold for Question 4.34, which together with the odd-modulus case mathematically implies Conjecture 4.33 for positive even $K$, though no proof of Conjecture 4.33 (nor odd $m$, $m = 2s$, or $K \le 0$) is given or checked there. Because `#23317` is an open unproved preregistration for a neighboring question rather than a settled result or near-settled PR for Conjecture 4.33, it does not trigger `CONTESTED.md`, and is logged here for `@audit-1` / `@triage`.
- `tools/arxiv_fetch.py query 'all:"2407.20048" OR (au:"Benfield" AND ti:"Pisano")'`: `1` entry (`2407.20048v2` itself, updated `2025-01-30`).
- Zenodo API (`https://zenodo.org/api/records?q=%222407.20048%22&size=5`): `0` records.
- `search_web` (`"2407.20048"`, `"even-K-exceptions"`): no published resolution of Conjecture 4.33 found.

## Coverage Limits
- `gh search code` returned HTTP 429 rate limit during check; GitHub coverage relies on `watch/snapshots/discovered/` (`608` total snapshot files, including full tree of `the-omega-institute/trureturing`), live `gh search repos`, and live `gh search issues`.
- Journal DOI `10.1080/00150517.2025.2460555` paywalled (`HTTP 403`), checked via `2407.20048v2` TeX source (`fiborder.tex`).

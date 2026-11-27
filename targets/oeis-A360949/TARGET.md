---
source: https://oeis.org/A360949 (OEIS A360949, rev. 2023-03-05), https://oeis.org/A161674
status: reported
owner: scout-6
updated: 2026-11-26T23:32:00Z
identifiers: [A360949, A325574, A161674, A010060, Paul D. Hanna, Thue-Morse]
---

# Target: OEIS A360949 (Paul D. Hanna 2023 Mod-4 Thue–Morse Conjecture)

## Verbatim Statement
From OEIS **A360949** (author: `_Paul D. Hanna_`, Mar 03 2023; latest revision `2023-03-05T12:37:19-05:00`):

- **Name:**
  > G.f. A(x) satisfies: 1 = Sum_{n>=0} (-x/2)^n * (A(x)^n + (-1)^n)^n.
- **Data (`offset 0`):**
  > 1,2,8,50,376,3124,27804,260496,2539616,25556330,263922884,2785341186,29948035032,327315887046,3630399545244,40813503158790,464662514679168,5354222585965310,62419468527625408,736098528973804246,8781173950238637928,105987886325647341056
- **Comment (Conjecture):**
  > Conjecture: a(0) = 1, a(2*A161674(k) + 1) == 2 (mod 4) for k >= 1, otherwise a(n) == 0 (mod 4). A161674 lists positions n such that A010060(n) + A010060(n+2) = 1, where A010060 is the Thue-Morse sequence.

Cross-referenced `A161674` (`offset 1`): `0,1,4,5,6,7,8,9,12,13,16,17,20,21,22,23,24,25,28,29,30,31,32,33,...` ("Positions n such that A010060(n) + A010060(n+2) = 1").

## Gate 1 Novelty Receipt
- Checked at: `2026-11-26T23:25:00Z` – `23:28:00Z`
- `watch/snapshots/` (`tools/novelty_grep.py A360949 A325574 A161674`): `0 lines across 0/356 files`.
- `tools/arxiv_fetch.py query "all:A360949 OR all:A325574"`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A360949+OR+A325574&size=5`): `0` hits.
- GitHub code search (`gh search code A360949` general + `aliromman/math`, `trureturing`, `joaquimmj/oeis-conjectures`, `1337isnot1337/solved-conjectures`): only PARI/GP entry `gfis/OEIS-prog/prog/gp/a360/A360949.gp` and unrelated hex strings; `0` matches in competing math repos (the single `trureturing` hit is a SHA-256 hash substring).
- Web search (`"A360949" OR ("A161674" "2*A161674") OR "Paul D. Hanna" "A360949"`): only OEIS `A360949`; no proof found.
- OEIS `A360949`, `A325574`, `A161674` inspected live: comment remains marked `Conjecture:`.
- Not covered: closed-access venues not indexed by arXiv/Zenodo/web.

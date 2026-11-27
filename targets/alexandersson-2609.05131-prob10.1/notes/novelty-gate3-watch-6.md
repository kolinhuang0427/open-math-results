# Gate 3 (<1h) Live Novelty Receipt (`watch-6`) — `targets/alexandersson-2609.05131-prob10.1/`

- **Checked UTC:** `2026-11-27T12:06:25Z`–`2026-11-27T12:06:43Z`
- **Target:** Per Alexandersson, *Real-rootedness and interlacing for parking functions and Chow polynomials*, `arXiv:2609.05131v2` (2026-09-23), Section 10, **Problem 10.1** (`\label{prob:consecutiveChowInterlacing}`).
- **Audit Status:** `@audit-1` Re-Audit #1 **PASS** (`AUDIT.md` §4, `#1388`, `notes/check-check-3.py` zero-float `PASS`).
- **Verdict:** **OPEN / CLEAR FOR GATE 5 REPORTING**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `709` post-Sweep-7 snapshot files):**
   - `consecutiveChowInterlacing` -> **`0` hits** (`0/709`).
   - `2609.05131` -> hits only `1337-solved-conjectures/closed_issues.md:246` (unrelated excedance issue) and `watch/snapshots/arxiv/citing_papers.{json,md}` (citing `arXiv:2611.07267`, parking permutation avoidance with fixed lucky sets — unrelated).
   - `Alexandersson` / `Chow polynomial` -> `1337-solved-conjectures` entries (`alexandersson-parking-excedance`, `alexandersson-graphical-dist`, `alexandersson-transportation`, `alexandersson-fuss-catalan`, `chow-conjecture`) and `byigitt__inverse-kl-first-index` (dual Chow polynomial for $q \ge 17$) — `0` overlaps with $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$.
2. **Live arXiv (`export.arxiv.org/api/query`):**
   - `id_list=2609.05131` -> sole version `http://arxiv.org/abs/2609.05131v2` (`2026-09-23T12:23:46Z`).
   - `au:Alexandersson+AND+all:Chow` -> `1` entry (`2609.05131v2`).
3. **GitHub Live Search (`gh` CLI):**
   - `gh search code '"consecutiveChowInterlacing"'` -> `[]`.
   - `gh search repos "2609.05131"` -> `[]`.
   - `gh search code 2609.05131` & `"Alexandersson" "Chow" "interlacing"` -> `1337isnot1337/solved-conjectures` (unrelated problems above), `the-omega-institute/trureturing` (`alexandersson2026parking.md`, `alexandersson-2026-parking-descent-refinement.md`, `DescentGapKernel.md`, `MaximumLetterGaps.md`, `PeakTieDescentRecurrence.md` — parking function descent/gap results, not Problem 10.1), `BrettRey/erdos-problem-993` (triage ID list).
   - `gh search issues "2609.05131"` -> solely `PerAlexandersson/RealRooted#665` (`state: closed`, Theorem 3.1 Smirnov transfer).
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` -> `AlexanderssonLeiteFundamentalLengthRefutation` and `SimplicialPosetChowRefutation` only (`0` hits for `2609.05131` / `prob:consecutiveChowInterlacing`).
4. **Live Zenodo & Web Search:**
   - `zenodo.org/api/records?q=2609.05131` -> `0` hits; `q=Alexandersson+Chow+interlacing` -> unrelated older repos (`grace-s-ko/interlacing-zeros`, `Pistrix/Zeros-of-Eisenstein-Series`).
   - `search_web` (`"2609.05131" OR ("Alexandersson" "Problem 10.1" "Chow" "interlacing")`) -> returns solely `arXiv:2609.05131`.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all checked public sources confirm Problem 10.1 (`\label{prob:consecutiveChowInterlacing}`) remains open.

---
source: Nikolay Vereshchagin, "How Much Randomness is Needed to Convert MA Protocols to AM Protocols?", arXiv:2611.30127v1 (2026-11-23), Section 6 (Open questions, items 2–3, main-eng.tex lines 774–780) and Section 1 (lines 151–154)
status: reported
owner: attack-6
started: 2026-11-27T18:58:25Z
attack_started_utc: 2026-11-27T19:17:00Z
updated: 2026-11-27T19:52:00Z
identifiers: ["arXiv:2611.30127v1", "Open Question 2", "Open Question 3", "Conjecture 1", "algebrization", "MA", "AM"]
---

# Target: vereshchagin-2611.30127-q2

- **Source:** Nikolay Vereshchagin, *How Much Randomness is Needed to Convert MA Protocols to AM Protocols?*, `arXiv:2611.30127v1` (2026-11-23), Section 6 (Open questions, items 2–3; see also Section 1 lines 153–154).
- **Status:** reported
- **Owner:** attack-6
- **Started (UTC):** 2026-11-27T18:58:25Z
- **Attack Started (UTC):** 2026-11-27T19:17:00Z
- **Updated (UTC):** 2026-11-27T19:52:00Z
- **Identifiers:** `arXiv:2611.30127v1`, Open Question 2 (and Open Question 3) on algebrization of $\mathrm{MA}[m,a]\subset\mathrm{AM}[*,p(a)]$.

## Exact Quoted Statement

From `2611.30127.src`, `main-eng.tex` (lines 774–780, and Section 1 lines 151–154):

> \section{Open questions}
> 1. Is it true that for some polynomial $p$ for all polynomials $m,a$ it holds $\mathrm{MA}[m,a]\subset\mathrm{AM}[*,p(a)]$?
> 2. Can we prove the inclusion $\mathrm{MA}[m,a]\subset\mathrm{AM}[*,p(a)]$ by algebrizing techniques (for some fixed polynomial $p$)?
> 3. Can we prove Conjecture 1 by algebrizing techniques?
>
> (Section 1: "It remains an open question whether we can resolve both questions using algebrizable techniques in the sense of Aaronson and Wigderson~\cite{AW}.")

## Gate 1 Novelty Receipt (`2026-11-27T18:58:22Z`, re-verified `2026-11-27T19:16:40Z`)

- `ls targets/`: no folder matching `vereshchagin`, `30127`, `algebriz`, or `knop`.
- `tools/novelty_grep.py`: only `watch/snapshots/arxiv/arxiv_submissions.{json,md}` listing `2611.30127v1` itself; 0 settlements across 790 files.
- `gh search code/issues/prs`: 0 PRs, 0 issues, 0 proof repos for `2611.30127`.
- `Zenodo`: `0` records; `Crossref`: `0` matching works; `arXiv:2611.30127v1` sole version.
- Live ECCC & web search: see `notes/novelty-attack.md`.

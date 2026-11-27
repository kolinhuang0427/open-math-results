---
source: arXiv:2603.19554v1 (Section 3.1, Conjecture 3.3 / conj:1)
status: reported
owner: scout2-4
updated: 2026-11-27T09:00:50Z
identifiers: ["2603.19554", "Hare", "Hichri", "Parry order", "x^d - x - 1"]
---

# Hare–Hichri (arXiv:2603.19554v1): Conjecture 3.3 (`conj:1`)

## Statement (verbatim, `tools/.arxiv_cache/eprint/2603.19554/v6.tex`, Section 3.1 `sec:beta, theta`, lines 489–493)

Context (lines 489):
> The two polynomial families $x^d - x - 1$ and $x^d - x^{d-1} - 1$ are often considered in many works to show important results on the dynamic properties of Perron numbers \cite{Akiyama2016,HichriSmyth2024,VergerGaugry2008}. For instance, Akiyama proved that all Perron numbers $\beta_d$ of minimal polynomial $x^d - x - 1 = 0$, with $d \ge 4$ are non-Parry numbers belonging to $\mathbb{P}_\Phi$.

Conjecture (`\label{conj:1}`, lines 490–493):
> `\begin{conj} {\ }`
> `\label{conj:1}`
> For all $d \geq 4$ and all $k \geq 1$ we have $\beta_d^k$ is non-Parry.
> `\end{conj}`

## Gate 1 Novelty Receipt

- Checked UTC: `2026-11-27T08:52:02Z`
- `tools/novelty_grep.py Hichri "Parry order" 2603.19554`: 1 hit across 586 files, only `watch/snapshots/discovered/AlexenderSokolov__cross-theory-formal-database.json` (license entry `arxiv-2603.19554-CC-BY-4.0.txt`).
- `gh search issues "2603.19554"` & `"Hare Hichri"`: 0 hits.
- `gh search code "2603.19554"`: 12 hits; only mathematical resolution found is `ArtificialZeng/AI-Has-Taste` (`BW2-B06-P08`), which proves **only the fixed $d=4$ case** ("*Every Power of the Perron Root of $X^4-X-1$ Is Non-Parry: An Exact Certificate*", 2026-08-30; its `CITATION_AUDIT.md` explicitly states it does not settle the full all-$d$ conjecture). Note: subsequent `gh search code` calls for `"Hichri"` / `"BW2-B06-P08"` hit GitHub code-search 403 rate limit; `gh search repos "2603.19554"` returned 0 hits.
- `search_web`: confirmed `arXiv:2603.19554v1` (2026-03-20) is latest version; no all-$d$ proof or counterexample found.
- Coverage limit: GitHub code search for `"Hichri"` rate-limited after `"2603.19554"` succeeded.

## Attack Start

- Attack started UTC: `2026-11-27T08:52:02Z` (deadline ~`2026-11-27T09:15Z`).

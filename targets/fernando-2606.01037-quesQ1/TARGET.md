---
source: Neranga Fernando, Bhitali Kousik, "A further study of polynomial $g_{n,q}$ over finite fields", arXiv:2606.01037v1 (31 May 2026), Section 6 (`draftMay31.tex`, lines 893–895, `\label{Q1}`; Question 6.1)
status: reported
owner: attack-6
started: 2026-11-27T16:05:49Z
attack_started_utc: 2026-11-27T17:17:00Z
updated: 2026-11-27T17:40:00Z
identifiers: ["2606.01037", "2606.01037v1", "Question 6.1", "Q1"]
---

# fernando-2606.01037-quesQ1

- Source: Neranga Fernando, Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, arXiv:2606.01037v1 (31 May 2026), Section 6 (`draftMay31.tex`, lines 893–895, `\label{Q1}`; Question 6.1).
- Status: reported
- Owner: attack-6
- Started: 2026-11-27T16:05:49Z
- Attack started: 2026-11-27T17:17:00Z
- Updated: 2026-11-27T17:40:00Z
- Identifiers: arXiv:2606.01037v1

## Gate 1 Novelty Receipt
- `ls targets/`: no `fernando-*` or `2606.01037*` directory present (`targets/fernando-2606.01037-quesQ1` claimed atomically).
- `tools/novelty_grep.py`: 0 hits for `2606.01037`, `Bhitali Kousik`, `Q1` / `S_{e/2}`; unrelated hits only on `Neranga Fernando` (`2611.12065` doubled-triangle minimum-fold) and generic numbers `307`.
- `gh search` on `the-omega-institute/trureturing`: `#8550` (`math: Fernando–Kousik permutation criterion, Conjecture 5.23`) covers ONLY Conjecture 5.23 via Matthews (1982); 0 issues/PRs/code for Section 6 open questions (`Q1`–`Q8` / `desirable triples`).
- Global `gh search` (`issues`, `prs`, `code`): only catalog listing `10m-u/open-problems-catalog` (`Q3704`, explicitly marked `Status: Open`, primary source `arXiv:2606.01037v1`) and RSS feed entry; 0 solutions or proofs.
- `arxiv_fetch.py abs 2606.01037`: v1 is the latest version (31 May 2026); Zenodo API returned 0 hits; `search_web` returned no follow-up resolutions.
- Re-verified live at `2026-11-27T17:16:39Z` by `@attack-6`: `notes/novelty-attack.md` (still OPEN).

## Statement (verbatim from `draftMay31.tex`, lines 893–895)

> **Question 6.1 (`\label{Q1}`):**
> Let $q>2$ be even, $e>0$ be even, and $n=(q-1)\cdot q^0+(q-1)\cdot q^{e/2}+1\cdot q^e$. Then $g_{n,q}=S_1+S_{e/2}^{q^{e/2}}+S_e\cdot S_{e/2}^{q-1}$. Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}.$

Here $S_k = \x + \x^q + \x^{q^2} + \cdots + \x^{q^{k-1}}$ ($S_0 = 0$) and $S_1 = \x$ (Section 2, line 119).

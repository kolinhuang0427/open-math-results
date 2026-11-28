---
source: arXiv:2606.01037v1 (Neranga Fernando and Bhitali Kousik, "A further study of polynomial $g_{n,q}$ over finite fields", 31 May 2026, Section 6, Question 6.4 / \label{Q4}, draftMay31.tex lines 923–926)
status: reported
owner: attack-1
created: 2026-11-27T17:31:00Z
updated: 2026-11-27T19:03:00Z
identifiers: ["arXiv:2606.01037v1", "Question 6.4", "Q4", "g_{n,q}", "Fernando", "Kousik"]
---

# Fernando & Kousik (2026), arXiv:2606.01037v1 — Question 6.4 (`\label{Q4}`)

## Primary Source & Verbatim Statement

From Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1` (31 May 2026), Section 6 (`draftMay31.tex` inside `tools/.arxiv_cache/eprint/2606.01037.src`, lines 923–926, `\label{Q4}`):

> **Question 6.4 (`\label{Q4}`).**
> Let $q > 2$ be even and $e > 2$ a positive integer. Let $n = (q - 1) \cdot q^0 + (q - 2) \cdot q^2 + 1 \cdot q^e + 1 \cdot q^{e+2}$. Find conditions on $q$ and $e$ for which
> $$g_{n,q} = X^q + S_e^2 \, S_2^{q - 2} + S_e S_2^{q - 1}$$
> is a PP of $\mathbb{F}_{q^e}$.

Here $q = 2^m$ ($m \ge 2$), $S_k(X) = X + X^q + \cdots + X^{q^{k-1}}$ ($S_0 = 0$, $S_2(X) = X + X^q$, Section 2 line 119), and $S_e = \mathrm{Tr}_{q^e/q}$ on $\mathbb{F}_{q^e}$. (Note the commented-out example in `draftMay31.tex` line 928: `$n = 4387, q = 4, e = 4$`.)

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T17:31:00Z` (corroborating `fernando-lit` `#1712` full live check at `16:57Z`).
- `targets/`: no existing `fernando-2606.01037-quesQ4` directory (`Q1` and `Q3` are separate questions).
- `tools/novelty_grep.py`: 0 settlement hits for `2606.01037`, `Question 6.4`, or `4387` across all `watch/snapshots/**` (incl. `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`, `1337-solved-conjectures`, `trureturing`).
- `the-omega-institute/trureturing#8550` covers ONLY Conjecture 5.23; `10m-u/open-problems-catalog` lists Question 6.4 as `Open`; `arXiv:2606.01037v1` is the sole version; Zenodo & live `hexagonmath.org` clear.

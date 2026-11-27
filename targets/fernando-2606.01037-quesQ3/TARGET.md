---
source: arXiv:2606.01037v1 (Neranga Fernando, Bhitali Kousik, "A further study of polynomial g_{n,q} over finite fields", 31 May 2026, Section 6, Question 6.3 `\label{Q3}`, `draftMay31.tex` lines 911–915)
status: reported
owner: attack-2
updated: 2026-11-27T17:55:00Z
start_utc: 2026-11-27T16:53:58Z
identifiers: ["2606.01037", "2606.01037v1", "Q3", "Question 6.3"]
---

# fernando-2606.01037-quesQ3

## Statement (verbatim from `draftMay31.tex`, lines 911–915)

> **Question 6.3 (`\label{Q3}`):**
> Let $q>2$ be even, $n=1\cdot q^0+(q-1)\cdot q^{e/2}+(q-1)\cdot q^e$, and $e>0$ be even. Then
> $$g_{1\cdot q^0+(q-1)\cdot q^{e/2}+(q-1)\cdot q^e}=S_{e/2+1}^{q^{e/2}}+S_e+S_e\,(S_{e/2}^{q^{e/2}})^{q-1}.$$
> Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}.$

Here $S_k = X + X^q + X^{q^2} + \cdots + X^{q^{k-1}}$ ($S_0 = 0$) and $S_e = \mathrm{Tr}_{q^e/q}$ on $\mathbb{F}_{q^e}$ (Section 2, line 119).

## Gate 1 Novelty Receipt (updated `2026-11-27T16:57Z`, full log in `notes/novelty-attack.md`)
- `ls targets/`: `targets/fernando-2606.01037-quesQ3` claimed atomically; no duplicate slug.
- Local watch snapshots (`watch/snapshots/**`, 743 files incl. `hexagonmath`, `papex`, `hwzw`, `raghav`, `1337`, `trureturing`): 0 hits for `2606.01037`, `Bhitali Kousik`, `Neranga Fernando`, `g_{n,q}`, `S_{e/2+1}`, or Question 6.3.
- Live GitHub & `the-omega-institute/trureturing`: `#8550` covers ONLY Conjecture 5.23 / Remark 5.24 via Matthews (1982); 0 issues/PRs/code for Section 6 (`Q1`–`Q8`). `10m-u/open-problems-catalog` only catalogs `Q1` and `Q4` as Open.
- Live arXiv (`2606.01037v2` HTTP 404; `v1` 31 May 2026 sole version), Zenodo API (0 hits), DataCite (0 hits), live `hexagonmath.org` (0/3,000 works), Crossref, and web search: **OPEN** — no follow-up or resolution of Question 6.3 found.

## Candidate Result
- **Classification (proved in `PROOF.md`, verified in `verify.py`):** For even $q = 2^m > 2$ ($m \ge 2$) and even $e > 0$, $g_{n,q}$ is a permutation polynomial of $\mathbb{F}_{q^e}$ **if and only if** $q = 4$ and $4 \mid e$.

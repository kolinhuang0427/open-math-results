---
source: arXiv:2401.09497v1 (Thomas Garrison, Chris Seiler, Andrew Knowles, "Weakly Consecutive Sequences", Section 5 "Conjectures and future work", Conjecture 5.2 / `\label{conj:1 at end}`)
status: reported
owner: attack-2
updated: 2026-11-27T09:10:16Z
identifiers: arXiv:2401.09497, arXiv:2401.09497v1, Garrison, Seiler, Knowles, weakly consecutive sequence, conj:1 at end, WeaklyConsecutiveOneAtEnd, IsWeaklyConsecutive
---

# Target: Garrison–Seiler–Knowles `arXiv:2401.09497v1` Conjecture 5.2 (`conj:1 at end`)

## Exact Verbatim Statement

From `tools/.arxiv_cache/eprint/2401.09497/WCS.tex` (arXiv:2401.09497v1):

**Definition 1.1 (`\label{def:weak_consec}`, Section 1, lines 83–85):**
> Let $\sigma : [k] \to [k]$ be a permutation for a natural number $k$. We say $\sigma$ is \emph{weakly consecutive} if, for all $i,j \in [k]$ and integers $m$, if $m \mid \sigma(i)$ and $m \mid (i - j)$, then $m \mid \sigma(j)$. Let $N(k)$ be the number of distinct weakly consecutive sequences of length $k$.

**Conjecture 5.2 (`\label{conj:1 at end}`, Section 5 "Conjectures and future work", lines 718–720):**
> Any WCS either begins or ends with the term $1$ (in other words, $\sigma(1) = 1$ or $\sigma(k) = 1$).

## Gate 1 Novelty Receipt

- **Checked UTC:** `2026-11-27T08:44:00Z`
- **Sources checked:**
  - `tools/novelty_grep.py 2401.09497` (0 matches across 0/54 snapshot files; watch snapshots are still rebuilding).
  - `tools/arxiv_fetch.py query 'all:"2401.09497" OR (all:"weakly consecutive" AND submittedDate:[202401010000 TO 202612312359])'` (1 result: `2401.09497v1` itself; no citing or follow-up arXiv preprints).
  - `gh search code "2401.09497"`: found `rainwangphy/aftd-platform` (`lean/AFTD/Kb/NumberTheory/`), which formalizes `is_weakly_consecutive`, `weakly_consecutive_first_dvd` ($\sigma(1) \mid k$), `weakly_consecutive_last_dvd` ($\sigma(k) \mid k$), `weakly_consecutive_ends_coprime` ($\gcd(\sigma(1),\sigma(k))=1$), `weakly_consecutive_rev`, and `weakly_consecutive_one_at_end_of_isPrimePow` (proving Conjecture 5.2 **only** when $k$ is a prime power `IsPrimePow k`). No general proof or counterexample for composite non-prime-power $k$ is present.
  - `1337isnot1337/solved-conjectures` (`CONTENTS.md`, `HISTORY.md`, `issues`, `pulls`) and `openai/math` tree: no matches for `2401.09497`, `weakly consecutive`, or `Garrison`.
  - `search_web` for `"Weakly Consecutive Sequences"` / `"2401.09497"` / `"conj:1 at end"`: no published proof or disproof found.
- **What was not covered:** Full sweep of all 642 `watch/snapshots/discovered/` repos (snapshots still rebuilding).
- **Updated Live Gate 1 Sweep (`garrison-lit`, `2026-11-27T09:03:27Z`, full receipt in `notes/novelty-garrison-lit.md`):**
  - `tools/novelty_grep.py` across all `601` rebuilt snapshot files (`watch/snapshots/**`, incl. all `the-omega-institute/trureturing*`, `1337isnot1337/solved-conjectures`, `openai/math`, `mathesis-papers`): 0 proofs for general $k$ (only `rainwangphy/aftd-platform` proving prime-power $k$ only).
  - Live GitHub (`gh search repos/issues`, `trureturing`, `1337isnot1337`): found `ndesmo/leaning` (`#21`, `#47`/PR `#57` proving $k \le 16$ in Lean, `#48`/PR `#61` proving prime-power $k$ in notes & checking $k \le 23$ in Python, open unmerged issue `#68` attacking 2-prime composite $k$); general $k$ (and even $k$ and general composite $k$) remains OPEN.
  - Live Zenodo (`0` hits), Crossref (`0`), OpenCitations (`0`), INSPIRE (`0`), live arXiv (`2401.09497v1` only), OEIS `A395372` (`2026-04-22`, no resolution), web/MO/MSE (Pillai–Brauer near-miss is non-bijection blocks only): 0 proofs or counterexamples for general $k$.
  - Not covered in live sweep: `gh search code` (HTTP 429), OpenAlex/Semantic Scholar (HTTP 429), zbMATH (SSL), DBLP/Google Scholar (anti-bot), unpushed local branches on `ndesmo/leaning#68`.
- **Conclusion:** Full statement (general $k$, including non-prime-power $k$) remains OPEN.

## Screening Log

- **Started UTC:** `2026-11-27T08:44:00Z`

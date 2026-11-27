# Gate 2 Novelty Check — `vasilyev-2611.20344-q7.10` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T16:52:21Z`–`2026-11-27T16:52:39Z`
- **Target:** `targets/vasilyev-2611.20344-q7.10/` — Oleg Vasilyev, *"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"* (`arXiv:2611.20344v2`, `2026-11-18`), Section 7 Question 7.10 (`q:supremum`: whether $\sup \pi_C(S) = \log_3 2$ over uniformly descending periodic sets $S$)
- **Claimed result:** **YES** ($\sup \pi_C(S) = \log_3 2$, proved in `PROOF.md`, zero-float `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.20344" "Vasilyev" "pi_C" "De Bruijn" "Collatz"`):**
   - `1337isnot1337/solved-conjectures` (`227` `results/`, `94` `research` at `16:49:39Z`): `0` Vasilyev/`2611.20344` hits; Collatz hits are solely `#220`/`#224` (Althöfer's stochastic / optimal-play Collatz games).
   - `ai-collections` / `discovered` / `arxiv`: only Q7.7 (`the-omega-institute/trureturing` `VasilyevForceDivergenceRefutation.*`), Q7.1 (`s66lem/conjectures`), Q7.12 (`Mira-Cult/math/notes/number-theory/collatz/density-zero-modification.md`), and `watch/snapshots/arxiv/*` tracking `2611.20344v2` itself (`citing_papers.json`: `openalex_cited_by=1`, `S2=0`, `citing_works: []`).
   - `0` hits on Question 7.10 (`q:supremum`, $\sup \pi_C(S) = \log_3 2$, `73/174`).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T16:52:21Z`):**
   - `main` = `236b4fc42c9b7bd1c6246039ff895e3ece0bc673` (`2026-11-27T16:49:19Z`, PR `#1060`, Stanley unlabelled leaf distances) — unrelated.
   - `research` = `5a78c3bf87679f70756d091587c8e97682f7c927` (`2026-11-27T16:52:08Z`, uniform odd-girth barrier) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.20344"` -> `0` hits (`[]`).
   - `gh search issues "2611.20344"` -> `1` hit: `the-omega-institute/trureturing#32194` (open, Q7.7 forcing divergence only — not Q7.10).
   - `gh search issues "q:supremum"` -> `0` hits (`[]`).
   - `gh search code "2611.20344"` -> `s66lem/conjectures` (Q7.1), `the-omega-institute/trureturing` (Q7.7), `Mira-Cult/math` (Q7.12), plus unrelated CSVs.
   - `gh search code "uniformly descending" "Vasilyev"` -> `Mira-Cult/math/notes/number-theory/collatz/density-zero-modification.md` (Q7.12 only).
   - `gh search code "73/174" "Vasilyev"` -> `1` unrelated Twitter CSV collision (`fin-vermehr/twitter-ideas-spread`).
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2611.20344`) -> `2611.20344v2` (`published: 2026-11-16T00:13:47Z`, `updated: 2026-11-18T03:50:40Z`), latest version.
   - Zenodo API (`q=2611.20344`) -> `0` hits.
   - Web search -> only Vasilyev's `arXiv:2611.20344` paper and index mirrors; no resolution of Question 7.10 (`q:supremum`).

## Coverage Limits
- Covers `watch/snapshots`, live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and public web search as of `2026-11-27T16:52:39Z`; private repositories and non-indexed preprints remain unobservable.

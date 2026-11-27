# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/caro-2312.08777-prob7/`

- **Target:** Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster & Christina Zarb, *Flip colouring of graphs*, `arXiv:2312.08777v1` (2023-12-14; *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 6 & Section 7 final Problem: for $t \in \mathbb{N}, t \ge 2$, determine $b(t)$ (**exact answer: $b(t) = 3$ for all $t \ge 1$**, proved).
- **Checked UTC:** `2026-11-27T18:06:49Z` – `2026-11-27T18:07:01Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior determination of $b(t)$ for $t \ge 2$ found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `760` files after Sweep 19) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2312.08777 "caro-2312.08777" "Mifsud" "Zarb" "flip colouring" "CayleyTFlip" "PackingTFlip" "s00373-024-02838-w" --max-per-file 0 --max-total 40` -> `# 0 lines across 0/760 files in 0.61s`.
   - `RESULTS.md` scan (`2312\.08777|caro|mifsud|lauri|zarb`) -> `[]`.
2. **Live GitHub (`2026-11-27T18:06:49Z`–`18:07:00Z`):**
   - `gh search code '"2312.08777"'`, `gh search code '"s00373-024-02838-w"'`, `gh search code '"CayleyTFlip"'`, `gh search repos "2312.08777"`, `gh search issues "2312.08777"`, `gh search prs "2312.08777"`, and `trureturing` `dev` tree -> `0` hits on all seven.
3. **Live arXiv, Semantic Scholar, OpenAlex, Crossref, Hexagon, Papex, Zenodo & Web (`2026-11-27T18:06:49Z`–`18:07:01Z`):**
   - `https://export.arxiv.org/api/query?id_list=2312.08777` -> `2312.08777v1` sole arXiv version.
   - `OpenAlex cited_by_count=4`, `Crossref is-referenced-by-count=0`, `S2 citationCount=5` unchanged (`2401.02315`, `2403.04401`, `2507.14473`, `2602.23517`, `2609.37978` all already verified unrelated to $b(t)$).
   - `hexagonmath.org` (`q=2312.08777`, `q=Zarb`, `q=Mifsud`) -> `total=0`; `papex.org` `0/20`; Zenodo `0` hits; `search_web` clear.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py` -> exit `0`, `PASS` (lower bound $b(t) \ge 3$, exact recurrence $1 \le s \le 200$, explicit `([1],(3,4))` 128v, `([2],(3,4))` 2048v, `([3],(3,4))` 34952v sampled 203v).

## Coverage Limits

- Paywalled journal issues beyond arXiv preprints and private/unindexed repositories are outside reach.

# Gate 2 Novelty Receipt — `caro-2312.08777-prob7` (`watch-5`)

- **Target:** `targets/caro-2312.08777-prob7/` — Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *"Flip colouring of graphs"*, `arXiv:2312.08777v1` / *Graphs and Combinatorics* 40 (106), 2024 (`DOI:10.1007/s00373-024-02838-w`), Section 7 Problem 7 (determine $b(t) = \min\{b : ([t], (b, r))\text{-flip graph exists}\}$ for $t \ge 2$).
- **Checked UTC:** `2026-11-27T17:58:15Z`–`2026-11-27T17:59:37Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no published or preprinted determination of $b(t)$ for $t$-neighbourhood flip graphs ($t \ge 2$) found.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 760 files):**
   - `.venv/bin/python tools/novelty_grep.py "2312.08777" "Mifsud" "Zarb" "flip graph" --max-per-file 10 --max-total 50`: `0` hits for `2312.08777` / `Mifsud` / `Zarb` (`3` unrelated `"flip graph"` hits).
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Citation Follow-Up & Direct Eprint Inspection (`arXiv` + `OpenAlex`):**
   - `arXiv:2312.08777v1` (`2023-12-14`) is sole arXiv version; published version is `DOI:10.1007/s00373-024-02838-w` (*Graphs and Combinatorics* 40, 2024).
   - `OpenAlex` (`W4403238211`, `doi.org/10.1007/s00373-024-02838-w` & `doi.org/10.48550/arXiv.2312.08777`): `cited_by_count: 4`. Verified all 4 citing works on arXiv via `referenced_works` + direct TeX eprint inspection (`tools/.arxiv_cache/eprint/`):
     1. `arXiv:2401.02315v3` (*Flip colouring of graphs II*) — covers $h(b,r)$, $q(k)$, $m(k)$, `(3,4)`-flip graph closed neighbourhood (`t=1`), zero results on $b(t)$ for $t \ge 2$.
     2. `arXiv:2403.04401v1` (*On $(r,c)$-constant, planar and circulant graphs*) — covers $(r,c)$-constant graphs only.
     3. `arXiv:2507.14473v1` (*Graphs With the Same Edge Count in Each Neighborhood*) — covers `2-FLIP` complexity and $(r,c)$-regularity only.
     4. `arXiv:2602.23517v2` (*Regular $K_3$-regular graphs*) — covers $K_3$-regular graph spectrum (`spec(r)`) only.
   - `arXiv` author search `all:"Xandru Mifsud"` (`11` papers through `2609.05268v1`) & `all:"flip colouring"` / `all:"flip coloring" AND all:"Caro"`: no other follow-up papers touch $b(t)$.
3. **Live GitHub, Zenodo, OpenCitations & Web:**
   - `gh search issues/prs/repos "2312.08777"`: `0` hits; `gh search code "2312.08777"` & `"10.1007/s00373-024-02838-w"`: only `xmif1/geng_rc_graphs` (citation in README), `10m-u/open-problems-catalog` (`Q4739`, unrelated `(r,c)`-regular spectrum problem), and numeric CSVs.
   - `the-omega-institute/trureturing` `dev` tree & PRs up to `#34939`: `0` hits.
   - `Zenodo` (`2312.08777`): `0` hits; `OpenCitations`: `[]`.
   - `search_web` (`"2312.08777" OR ("Caro" "Lauri" "Mifsud" "Yuster" "Zarb")`, `("b(t)" OR "b(2)" OR "b(t) = 3") ...`): returns only `2312.08777` / J. Graphs Combin. article.

## Near-Misses & Coverage Limits
- **Near-misses:** The 4 citing preprints (`2401.02315`, `2403.04401`, `2507.14473`, `2602.23517`) address $t=1$ flip colourings, $(r,c)$-regularity, and complexity, not $b(t)$ ($t \ge 2$).
- **Coverage limits:** Live Semantic Scholar endpoint returned `HTTP 429`; private/unindexed drafts posted after `2026-11-27T17:59:37Z` are not covered.

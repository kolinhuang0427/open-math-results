# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/vereshchagin-2611.30127-q2/`

- **Target:** Nikolay Vereshchagin, *How Much Randomness is Needed to Convert MA Protocols to AM Protocols?*, `arXiv:2611.30127v1` (`2026-11-23`; prior ECCC `TR22-060` 2022-04-27 & CSR 2022 `DOI:10.1007/978-3-031-09574-0_21`), **Section 6** (`main-eng.tex` L774–780) & Section 1 (L151–154), **Open Questions 2 & 3**: can $\mathrm{MA}[m,a] \subset \mathrm{AM}[*, p(a)]$ or Knop's Conjecture 1 ($\mathrm{Heur}\text{-}\mathrm{MA}[m,a] \subset \mathrm{Heur}\text{-}\mathrm{AM}[*, p(a)]$) be proved by algebrizing techniques? (**NO** to both, proved via single Boolean oracle $A$ with Aaronson–Wigderson canonical multilinear extension $\widetilde{A}$, additive query split, rectangle-shrinking & Ping-Pong block-min-entropy restoration; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T19:50:32Z` – `2026-11-27T19:51:10Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of Section 6 Open Questions 2 or 3 found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `826` indexed files across `907` cataloged repos, post-Sweep 22) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.30127" "vereshchagin-2611.30127" "TR22-060" "10.1007/978-3-031-09574-0_21" "Heur-AM" "Vereshchagin" "algebrization"` -> `19` lines across `9/826` files: only `2611.30127v1` itself (`watch/snapshots/arxiv/*`), `AlgebrizationWanted.lean` (`facebookresearch/atlas-lean`), `kaced_romashchenko_vereshchagin_2017` (`plasma-ai/erdos`), `qedavid/solverz/algorithms/barriers.md`, and `hty942/p-vs-np-barriers` intro (`0` settlements of Q2/Q3).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T19:50:36Z`–`19:50:54Z`):**
   - `gh search code` & `gh search repos` for `"2611.30127"`, `"TR22-060"`, and `"Vereshchagin" "algebrization"` -> `[]` (`0` hits on all six queries).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Crossref, Hexagon, Papex, Zenodo & Web (`2026-11-27T19:50:36Z`–`19:51:02Z`):**
   - `https://eccc.weizmann.ac.il/report/2022/060/` (`TR22-060`): Vereshchagin's own 2022 report; `https://eccc.weizmann.ac.il/` (`26` homepage reports, `2026/347` latest) & `/year/2026/` (`692` links) + `search_web` (`domain:eccc.weizmann.ac.il` and general web/venues) show no follow-up resolving Q2 or Q3.
   - `https://export.arxiv.org/api/query?id_list=2611.30127` -> `2611.30127v1` sole arXiv version.
   - `https://api.crossref.org/works/10.1007/978-3-031-09574-0_21` -> `is-referenced-by-count: 0`.
   - `https://hexagonmath.org/api/v1/works` (`1,656` total works; `q=2611.30127`, `q=Vereshchagin`, `q=TR22-060` -> `0`), `papex.org` (`20` records -> `0`), `Zenodo` (`0` hits).
4. **Independent Verifier Verification (`@audit-1` re-audit `#1944`):**
   - Executed `.venv/bin/python -u targets/vereshchagin-2611.30127-q2/notes/check-check-1.py` -> exited `0` (`PASS`, including `Primary source Section 6 citation check: PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled/unindexed proceedings remain outside public reach); Semantic Scholar returned `429` in earlier Sweep 22 checks, cross-covered via ECCC `TR22-060`, Crossref `0` citations, arXiv, and `search_web`.

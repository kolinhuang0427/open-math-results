# Gate 2 Novelty Receipt (`watch-6`) — `targets/vereshchagin-2611.30127-q2/`

- **Target:** Nikolay Vereshchagin, *How Much Randomness is Needed to Convert MA Protocols to AM Protocols?*, `arXiv:2611.30127v1` (`2026-11-23`; prior ECCC `TR22-060` 2022-04-27 & CSR 2022 `DOI:10.1007/978-3-031-09574-0_21`), Section 7 (`main-eng.tex` L774–780) & Section 1 (L151–154), **Open Questions 2 & 3**: can $\mathsf{MA}[m,a] \subset \mathsf{AM}[*, p(a)]$ or Knop's Conjecture 1 be proved by algebrizing techniques? (**NO** to both, proved via canonical multilinear extension $\widetilde{A}$ + 2-party additive query simulation + rectangle-shrinking & Ping-Pong block-min-entropy restoration).
- **Checked UTC:** `2026-11-27T19:32:38Z` – `2026-11-27T19:34:15Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of Open Questions 2 or 3 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `811` files across `892` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2611.30127 "vereshchagin-2611.30127" "Vereshchagin" "algebrization" "AM[" --max-per-file 0 --max-total 30` -> `17` lines across `7/811` files: `watch/snapshots/arxiv/` entries (`2611.30127v1` itself), `kaced_romashchenko_vereshchagin_2017_conditional_information_inequality` (`plasma-ai/erdos`), `AlgebrizationWanted.lean` (`facebookresearch/atlas-lean`), `qedavid/solverz` barriers overview; `0` hits settling Q2/Q3.
   - `RESULTS.md` scan -> `[]`.
2. **Live GitHub (`2026-11-27T19:32:38Z`–`19:34:15Z`):**
   - `gh search code '"2611.30127"'`, `gh search code '"vereshchagin-2611.30127"'`, `gh search code '"Vereshchagin" "algebrization"'`, `gh search code '"10.1007/978-3-031-09574-0_21"'`, `gh search code '"TR22-060"'`, `gh search repos/issues/prs "2611.30127"`, `trureturing` `dev` tree -> `0` hits on all nine.
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, OpenAlex, Crossref, Hexagon, Papex, Zenodo & Web (`2026-11-27T19:32:38Z`–`19:33:57Z`):**
   - `https://eccc.weizmann.ac.il/report/2022/060/` (`TR22-060`, 27 Apr 2022): Vereshchagin's own original report; `eccc.weizmann.ac.il/` and `/year/2026/` show `0` follow-up reports resolving Q2/Q3.
   - `https://export.arxiv.org/api/query?id_list=2611.30127` -> `2611.30127v1` sole arXiv version.
   - `OpenAlex` (`ids.arxiv:2611.30127` & title search) -> `0`; `Crossref` (`10.1007/978-3-031-09574-0_21`) -> `is-referenced-by-count=0`; `hexagonmath.org` (`q=2611.30127`, `q=Vereshchagin`, `q=algebrization`) -> `total=0`; `papex.org` `0`; Zenodo `0` hits; `search_web` (incl. `site:eccc.weizmann.ac.il` and `STOC`/`FOCS`/`CCC`/`ITCS`) returns only Vereshchagin (`TR22-060` / `2611.30127`) and Knop (CSR 2015).

## Coverage Limits

- Semantic Scholar API returned HTTP `429` (covered via ECCC `TR22-060`, OpenAlex, Crossref, and `search_web`); paywalled venues and private repositories are outside reach; independent Gate 3 (`<1h`) check remains required before `RESULTS.md` publication.

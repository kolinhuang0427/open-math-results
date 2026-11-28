# Gate 3 Novelty Check — `vereshchagin-2611.30127-q2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T19:50:33Z`–`2026-11-27T19:50:44Z`
- **Target:** `targets/vereshchagin-2611.30127-q2/` — Nikolay Vereshchagin, *"How Much Randomness is Needed to Convert MA Protocols to AM Protocols?"* (`arXiv:2611.30127v1`, `2026-11-23`; ECCC `TR22-060`; CSR 2022 LNCS 13296 pp. 338–349, `DOI:10.1007/978-3-031-09574-0_21`), **Section 6** Open Questions 2 & 3 (`main-eng.tex` L774–780)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**NO** to both Open Questions 2 & 3: algebrizing barriers via Boolean oracle $A$ with canonical multilinear extension $\widetilde{A}$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/vereshchagin-2611.30127-q2/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.30127" "Vereshchagin" "algebrization"`):**
   - `18` lines across `9/826` files (`watch/snapshots/arxiv/*` indexing `2611.30127v1` itself, `hty942/p-vs-np-barriers`, `AlgebrizationWanted.lean`, `qedavid/solverz`, `plasma-ai/erdos`); `0` settlement hits.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T19:50:33Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `58f6f3d40349dddb1086d3af2d1d48b4e883f2eb` (`2026-11-27T19:49:07Z`, ccc specialization quotient) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.30127"` -> `0` hits (`[]`).
   - `gh search issues "2611.30127"` -> `0` hits (`[]`).
   - `gh search code '"2611.30127" "algebrization"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / ECCC / Web:**
   - arXiv API (`id_list=2611.30127`) -> sole version `2611.30127v1` (`2026-11-23T06:37:19Z`).
   - Zenodo API (`q=2611.30127`) -> `0` hits.
   - Crossref (`10.1007/978-3-031-09574-0_21`) -> `is-referenced-by-count: 0`.
   - `search_web` (ECCC `TR22-060` / CSR 2022 `10.1007/978-3-031-09574-0_21` / `arXiv:2611.30127` / Aaronson–Wigderson) -> only primary report & Aaronson–Wigderson (`2009`); `0` resolutions of Section 6 Open Questions 2 & 3.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/vereshchagin-2611.30127-q2/notes/check-check-1.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`826` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and `search_web` (including indexed ECCC pages) as of `2026-11-27T19:50:44Z`; direct `curl` to `eccc.weizmann.ac.il` failed in earlier check (relying on `watch-5`/`watch-6` ECCC `/year/2026/` checks and `search_web`).

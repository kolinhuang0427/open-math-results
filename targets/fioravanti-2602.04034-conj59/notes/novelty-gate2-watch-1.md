# Novelty Gate 2 Receipt — `targets/fioravanti-2602.04034-conj59`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T13:42:05Z`
- **Verdict:** **PASS — OPEN (no competing settlement found)**

## Exact Queries & Results

1. **Snapshot Grep (`watch/snapshots/` across `717` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2602.04034" "Fioravanti" "Kompatscher" "clonoids" "uniformly generated" "conjecture:strong" "conjecture:main" --max-per-file 5 --max-total 60`
   - Result: `18` lines across `8/717` files — zero competing settlements for Conjecture 59 or Conjecture 1:
     - `watch/snapshots/arxiv/{citing_papers,last_sweep_report}`: only references our own `fioravanti-2602.04034-ques2` (`OpenAlex cited_by=0; S2=0`).
     - `watch/snapshots/discovered/AlexenderSokolov__cross-theory-formal-database.json`: `lemma:representation` license/proof mirror only.
     - `watch/snapshots/hwzw-algebra-number-theory-drafts.md` / `Hwzw__algebra-number-theory-drafts.json`: `papers/P32-mixed-exponent-clonoids/` (`2026-09-09`) settles Question 60 ($\mathbb{Z}/p^2\mathbb{Z}\oplus(\mathbb{Z}/p\mathbb{Z})^s$) only; verified verbatim via `gh api repos/Hwzw/algebra-number-theory-drafts/contents/papers/P32-mixed-exponent-clonoids/ASSESSMENT.md` that it explicitly states *"The result is not a solution of the full finite-module conjecture"* and does not solve multiple $\mathbb{Z}/p^2\mathbb{Z}$ factors or higher exponents.
     - `1337isnot1337/solved-conjectures` sweep hit on `id:Rossi` is solely unrelated `rossi-permutohedron-roots`.

2. **Live GitHub:**
   - `gh search prs "2602.04034"` -> `0` matches.
   - `gh search issues "2602.04034"` -> `0` matches.
   - `gh search code "2602.04034"` -> `21` results (`10m-u/open-problems-catalog` `Q2503` lists Conjecture 1 as **Open**; `Hwzw` `P32` covers Question 60 only; remaining hits are bibliographies/RSS/CC-BY mirror/unrelated CSVs).
   - `gh search code '"uniformly generated" clonoid'` -> `0` matches.
   - `gh search code 'repo:the-omega-institute/trureturing clonoid'` -> `0` matches.

3. **Live arXiv / Zenodo / Web:**
   - `export.arxiv.org/api/query?id_list=2602.04034` -> sole version `arXiv:2602.04034v1` (`2026-02-03T21:55:59Z`); no `v2`.
   - `export.arxiv.org/api/query?search_query=all:clonoid+OR+all:clonoids&sortBy=submittedDate&sortOrder=descending&max_results=10` -> latest entries `2611.33066v1` (Boolean $\pm$-preclones) and `2608.18917v1` (2-nilpotent Mal'cev algebras; cited by `10m-u` as leaving Conjecture 1 open).
   - Zenodo API (`2602.04034 OR (Fioravanti clonoids)`): `225` hits, all unrelated biological/software records matching surname `Fioravanti` (0 clonoid/math records).
   - `search_web` for `"2602.04034"`, `"Fioravanti" "Kompatscher" "clonoids"`, `"uniformly generated" "clonoid" "p-group"`, `"finitely many clonoids" "finite modules" "coprime"`: no later solution to Conjecture 59 or Conjecture 1 found.

## Coverage Limits

- Unauthenticated OpenAlex API daily-budget limit was previously noted in `notes/novelty-attack.md` (already mitigated by snapshot `citing_papers.md` showing `0` citations and live S2/arXiv/GitHub/web queries). Independent Gate 3 final check remains recommended before `RESULTS.md` publication.

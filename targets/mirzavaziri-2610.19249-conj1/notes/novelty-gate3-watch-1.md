# Gate 3 Novelty Receipt — `targets/mirzavaziri-2610.19249-conj1/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:48Z`
- **Target:** M. Mirzavaziri & D. Yaqubi, `arXiv:2610.19249v1` (`2026-10-13`), Section 4 **Conjecture 4.4** (`\label{conj:general}`) & Section 1 **Conjecture 1.1** (`\label{conj:GK}` = Guo–Krattenthaler `arXiv:1301.7651v3` Section 7 **Conjecture 7.4** `\label{conj:330n88n}`). (Conjecture 4.5 `conj:almost` / Problem 7.2 is NOT claimed.)
- **Verdict:** **PASS** (`0` competing proofs closing $[301, 10^{30})$)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.19249" "10n-1" "15n-1" "conj:330n88n" --max-per-file 0 --max-total 0` -> `45` lines across `4/658` files: only `arxiv/citing_papers.{json,md}`, `arxiv/last_sweep_report.json`, and `tamnd__arxiv.json` (arXiv bib/census index only).
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.19249" "1301.7651" "conj:GK" "conj:330n88n" "Mirzavaziri"` -> inspected all non-index hits:
     - `the-omega-institute/trureturing#21322` & `MirzavaziriYaqubiMonotonicityRefutation.lean` / `Library/Certificates/mirzavaziri2026gaussianquotient.md`: refutes **Problem 7.2** (whether weak increase after one division forces the two-exception sign pattern after a second division), separate from `conj:GK` / `conj:general`.
     - `arxiv/citing_papers.md` cites `arXiv:2610.26878v1` (T. Prellberg, *A positivity conjecture of Prellberg and Stanton*, `2026-10-08`), checked directly via `arxiv_fetch.py query --id-list 2610.26878`: resolves Prellberg–Stanton and Reiner–Stanton–White only, not `conj:330n88n`.
     - `OjasMor`, `andrheabacor`, `s66lem`, Zenodo `24552279` (`Mirzavaziri–Yaqubi Conj 8 / PDO / Conj 6.2`): unrelated conjectures by the same authors.
2. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2610.19249,1301.7651` -> `2610.19249v1` (`2026-10-13`) and `1301.7651v3` (`2013-10-15`, only Conjectures 7.2 & 7.3 noted proved) remain latest.
   - `curl -s "https://zenodo.org/api/records?q=2610.19249&size=3"` & `q=1301.7651` -> `0` hits each.
3. **Live GitHub & Web Search:**
   - `gh search issues '"2610.19249"'` -> `trureturing#21322` (Problem 7.2 only); `gh search issues/prs '"1301.7651"'` -> `trureturing#12062`/`#12071` (`arXiv:1503.08231`, unrelated) and unrelated CI PRs.
   - `search_web` -> returns only `1301.7651` and `2610.19249v1` (which proves $m \le 300$ and $m \ge 10^{30}$ only, leaving $[301, 10^{30})$ open).

## Near-Misses & Coverage Limits
- **Near-misses:** `trureturing#21322` (`MirzavaziriYaqubiMonotonicityRefutation.lean`, Problem 7.2 only); `arXiv:2610.26878v1` (Prellberg–Stanton positivity); `arXiv:2610.19249v1` Theorem `thm:computation` ($m \le 300$) and Theorem `thm:asymptotic` ($m \ge 10^{30}$).
- **Coverage limits:** Private repositories and works without `2610.19249`/`1301.7651` identifiers are not covered.

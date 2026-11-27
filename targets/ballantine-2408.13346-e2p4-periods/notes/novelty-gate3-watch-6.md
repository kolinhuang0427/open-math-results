# Gate 3 Novelty Receipt (`watch-6`) — `targets/ballantine-2408.13346-e2p4-periods/`

- **Checked UTC:** `2026-11-27T09:29:24Z` (`<1h` before submission)
- **Target:** Ballantine–Beck–Merca `arXiv:2408.13346v1` Section 1 conjectural table of minimal periods for $e_2 p_4(n) \pmod m$ ($m = 10$ gives `1200 != 1150`, $m = 18$ gives `1296 != 1246`)
- **Verdict:** **PASS** (note paywalled *Ramanujan J.* 66 (2025) version caveat logged in `AUDIT.md` §1)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2408.13346" "e2p4" "e_2p_4"`: `0` hits for `2408.13346` or `e_2p_4` across `608` snapshot files (`CuteSurtr` `scale2p40` false positive only).
- `gh search repos "2408.13346" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2408.13346" --limit 10 --json repository,number,title,state,url`: only unrelated `the-omega-institute/trureturing#8751` (`arXiv:2409.11268v3`).
- Zenodo API (`https://zenodo.org/api/records?q=%222408.13346%22&size=5`): `0` records.
- Semantic Scholar citations of *Ramanujan J.* 66 (2025) `DOI: 10.1007/s11139-024-01001-6` (`9` citing works; checked all 9 arXiv abstracts via `tools/arxiv_fetch.py`): all 9 concern $\mathrm{pre}_j$, $d$-ary partitions, or Taylor integrals (`0` address $e_2 p_4(n)$ periods).

## Coverage Limits
- Published journal version *The Ramanujan Journal* 66 (2025), Art. 34 (`DOI: 10.1007/s11139-024-01001-6`) is paywalled (unverified whether the journal table silently corrected `1150`/`1246` relative to `arXiv:2408.13346v1`); `gh search code` skipped due to secondary rate-limit cooldown.

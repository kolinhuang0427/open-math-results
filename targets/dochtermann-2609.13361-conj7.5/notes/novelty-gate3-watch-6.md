# Gate 3 (<1h) Live Novelty Receipt (`watch-6`) — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked UTC:** `2026-11-27T12:08:58Z`–`2026-11-27T12:09:03Z` (extending Gate 2 live check at `12:00:36Z`)
- **Target:** Dochtermann, Huang, Mawhinney, Oh, Xu, *Matroids with cycle systems are regular*, `arXiv:2609.13361v1` (2026-09-11), Section 7, **Conjecture 7.5** (`\label{conj:C>=3 ind}`, plus Corollary 1 `conj:unique` & Corollary 2 cographic vertex-star characterization).
- **Audit Status:** `@audit-3` Re-Audit #1 **PASS** (`AUDIT.md` §6, `#1396`, zero-float/zero-div `check-check-1.py` `PASS`).
- **Verdict:** **OPEN / CLEAR FOR GATE 5 REPORTING**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `709` post-Sweep-7 snapshot files):**
   - `2609.13361` -> `5` index paths in `watch/snapshots/discovered/tamnd__arxiv.json` (`0` proofs).
   - `Dochtermann` -> `1` path in `watch/snapshots/discovered/cmu-l3__reuF2F.json` (`lean/reuF2F/dochtermann2026matroids.lean`, verified verbatim at `230023d` / `2026-10-25T06:02:32Z` to be an open `theorem conjecture_7_5 ... := by sorry` stub only).
   - `conj:C>=3 ind` -> **`0` hits** (`0/709`).
2. **Live arXiv, GitHub & Zenodo:**
   - `export.arxiv.org/api/query?id_list=2609.13361` -> sole version `http://arxiv.org/abs/2609.13361v1` (`2026-09-11T17:52:05Z`).
   - `gh search repos "2609.13361"` -> `[]`; `gh search issues "2609.13361"` -> `[]`; `gh search code '"conj:C>=3 ind"'` -> `[]`.
   - `zenodo.org/api/records?q=2609.13361` -> `0` hits.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or unscraped author webpages remain out of live query scope; all public channels searched confirm `arXiv:2609.13361v1` Conjecture 7.5 (`\label{conj:C>=3 ind}`) remains open.

# Gate 3 Novelty Check — `gaevoy-2606.25895-src2-1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T19:48:51Z`–`2026-11-27T19:49:04Z`
- **Target:** `targets/gaevoy-2606.25895-src2-1/` — Nikita Gaevoy, *"The Power of Small Symmetries"* (`arXiv:2606.25895v1`, `2026-06-24`; MFCS 2026 LIPIcs Vol. 386, Art. 97, `DOI:10.4230/LIPIcs.MFCS.2026.97`), §§ 2 & 6 ($\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs Resolution)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**YES — exponential separation** of $1\text{-SRC-II}$ from $\mathrm{Res}$ and bounded-depth Frege)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.25895" "Gaevoy" "SRC-II"`):**
   - `0` lines across `0/826` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T19:48:51Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `16cc4674fed3a74a73ec1d999a38eb92e658d202` (`2026-11-27T19:47:19Z`, two-step Cohen forcing) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.25895"` -> `0` hits (`[]`).
   - `gh search issues "2606.25895"` -> `0` hits (`[]`).
   - `gh search code '"SRC-II" "Resolution"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Web / Venues:**
   - arXiv API (`id_list=2606.25895`) -> sole version `2606.25895v1` (`2026-06-24T14:41:30Z`).
   - Zenodo API (`q=2606.25895`) -> `0` hits.
   - `search_web` (arXiv / LIPIcs MFCS 2026 Dagstuhl / ECCC follow-up check) -> only Gaevoy's `arXiv:2606.25895` / `LIPIcs.MFCS.2026.97` paper (`0` resolutions of $\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs Resolution).
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`826` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and `search_web` (including Dagstuhl/LIPIcs MFCS 2026 & indexed ECCC) as of `2026-11-27T19:49:04Z`; Crossref has not indexed `10.4230/LIPIcs.MFCS.2026.97`, and direct `curl` to `eccc.weizmann.ac.il` failed in earlier check (relying on `watch-5`/`watch-6` ECCC `/year/2026/` checks and `search_web`).

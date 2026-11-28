# Gate 2 Novelty Check — `gaevoy-2606.25895-src2-1` (`watch-5`)

- **Timestamp:** `2026-11-27T19:35:42Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Nikita Gaevoy, *"The Power of Small Symmetries"*, `arXiv:2606.25895v1` (`2026-06-24T14:41:30Z`; MFCS 2026, LIPIcs Vol. 386, Art. 97, pp. 97:1–97:17, DOI `10.4230/LIPIcs.MFCS.2026.97`), §2 & §6 — whether $\mathrm{SRC}\text{-}\mathrm{II}[1]$ (Resolution with local $1$-symmetries) is strictly stronger than / exponentially separated from Resolution ($\mathrm{Res}$).

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py` across `811` files):**
   - `"2606.25895" "Gaevoy" "SRC-II" "symmetric resolution"`: `0 lines across 0/811 files`.
   - `"SRCII" "small symmetries" "MFCS.2026.97"`: `0 lines across 0/811 files`.
2. **Live GitHub (`gh search` & `the-omega-institute/trureturing`):**
   - `gh search issues/prs/repos "2606.25895"`: `0` hits each.
   - `gh search issues/prs "SRC-II[1]"`: unrelated hits only; `gh search code "LIPIcs.MFCS.2026.97"`, `gh search code "SRC-II[1]"`: `0` hits; `gh search code "1-SRC-II"`: `1` unrelated hit (`SRC-IISERM/SRC-IISERM.github.io`).
   - `the-omega-institute/trureturing` PRs up to `#34956`: `0` hits for `2606.25895` / `Gaevoy` / `SRC-II`.
3. **arXiv API (`export.arxiv.org`):**
   - `id_list=2606.25895`: `2606.25895v1` (`2026-06-24T14:41:30Z`) sole version.
   - `cat:cs.CC AND (all:"SRC-II" OR all:"SRCII" OR all:"small symmetries" OR (all:"symmetry rule" AND all:"resolution"))`: only `2606.25895v1` and `2101.05142v1` (Schweitzer–Seebach 2021, *Resolution with Symmetry Rule applied to Linear Equations*).
4. **Citations & Repositories (OpenAlex / OpenCitations / Zenodo / Crossref / S2):**
   - OpenAlex `W7166252852` (queried via both `10.48550/arXiv.2606.25895` and `10.4230/LIPIcs.MFCS.2026.97`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2606.25895` and `10.4230/LIPIcs.MFCS.2026.97`): `200 []`.
   - Zenodo: `q=2606.25895` `0` hits; `q='"The Power of Small Symmetries"'` `0` hits; `q='"LIPIcs.MFCS.2026.97"'` `0` hits (`4` unquoted hits are unrelated token matches).
   - Note: Crossref returned `404` for both DOIs; S2 returned `429` for `ARXIV:2606.25895`/search and `404` for `10.4230/LIPIcs.MFCS.2026.97`.
5. **ECCC & Conference Web Search (`search_web`):**
   - Three live web queries (`"2606.25895" OR "LIPIcs.MFCS.2026.97"`, `"SRC-II[1]"/"SRCII[1]"/"local 1-symmetries"`, and `("1-SRC-II" ...) (STOC OR FOCS OR CCC OR SAT OR ECCC OR ICALP OR STACS OR arxiv)`) surfaced only Gaevoy's `arXiv:2606.25895` / MFCS 2026 (`dagstuhl.de`) and background symmetry-resolution definitions — no follow-up resolving $\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs. $\mathrm{Res}$.

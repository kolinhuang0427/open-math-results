# Adversarial Audit Helper Report: `targets/ferrero-2511.16335-conj1.8/`

- **Helper:** `ferrero-audit-hlp` (for `@audit-1`)
- **Timestamp (UTC):** 2026-11-26T20:17:00Z
- **Overall Assessment:** **NO PRIOR RESOLUTION OR DRIFT FOUND** — Conjecture 1.8 remains open in both `arXiv:2511.16335v1` and the June 2026 revised *Australasian Journal of Combinatorics* published version; $C_6[2K_1] \cong \mathrm{Circ}(12, \{1,5\})$ is a genuine counterexample, and $k=6$ with $r_i \ge 2$ is sharp among $C_k[2K_1]$ ($4 \le k \le 8$) and $C_6[1,2,2,2,2,2]$.

---

## 1. arXiv Metadata & Published Journal Version (*Australasian Journal of Combinatorics*)

- **arXiv query (`.venv/bin/python tools/arxiv_fetch.py query --id-list 2511.16335`):**
  - Latest version is still **`2511.16335v1`** (`published`: `2025-11-20T13:15:25Z`, `updated`: `2025-11-20T13:15:25Z`), with empty `comment`, `journal_ref`, and `doi`.
- **Published journal version (`ajc.maths.uq.edu.au/v96.p374` & OpenAlex `W4416550551`):**
  - Published in *Australasian Journal of Combinatorics*, **Vol. 96(2) (2026), pp. 374–394** (`https://ajc.maths.uq.edu.au/download/96/ajc_v96_p374-394.pdf`), marked *Received 23 Nov 2025; revised 2 June 2026*. OpenAlex records `cited_by_count: 0`.
  - Direct text extraction from the AJC Vol. 96(2) PDF confirms that **Definition 1.5** (standard fast join), **Theorem 1.6**, **Conjecture 1.8** (*"Let $G$ be a connected graph. If $\overline{\mathrm{pt}}(G) = 1$, then $G$ is a standard fast join."*), and **Corollary 5.12** (concluding Section 5) appear verbatim unchanged in the revised June 2026 published article, with no erratum, remark, or refutation added.
  - Both Sage code URLs cited in Reference [8] (`https://aimath.org/~hogben/FixedPropTime.ipynb` and `https://aimath.org/~hogben/FixedPropTime_Sage.pdf`) return **HTTP 404**.

---

## 2. Literature, Citation, Web, and Snapshot Novelty Searches (2024–2026 & Earlier)

- **OpenAlex & Crossref:**
  - OpenAlex `W4416550551` (`arXiv:2511.16335` / AJC Vol. 96(2)): `cited_by_count: 0`.
  - OpenAlex 2024–2026 searches for `"zero forcing propagation time"`, `"fixed propagation time"`, `"standard fast join"`, and `"minimal zero forcing sets"` found no paper resolving Conjecture 1.8 or mentioning $C_6[2K_1]$ / $\mathrm{Circ}(12,\{1,5\})$. (Crossref returned HTTP 429 on the second query of our batch.)
  - OpenAlex citation checks for foundational earlier works:
    - Hogben et al. (2012), *"Propagation time for zero forcing on a graph"* (`arXiv:1410.4191`, DOI `10.1016/j.dam.2012.04.003`, 117 citations total, 28 in 2024–2026): checked TeX source `Proptime12.tex` of `arXiv:1410.4191`. Its $\mathrm{pt}(G)=1$ section treats *minimum* zero forcing sets ($\mathrm{pt}(G)$ and $\mathrm{PT}(G)$, e.g., $Q_s$ and universal-vertex attachments), not *minimal* zero forcing sets ($\overline{\mathrm{pt}}(G)$), and contains no mention of $C_6[2K_1]$ or $\mathrm{Circ}(12,\{1,5\})$.
    - Brimkov & Carlson (2024), *"Minimal zero forcing sets"* (`arXiv:2204.01810`, *Australas. J. Combin.* 90:363–377): 6 citing works in OpenAlex; checked abstracts of `2403.03921` (*Zero forcing irredundant sets*), `2509.18486` (*Universal perspectives on irredundance for X-set parameters*), `10.1007/s00373-024-02827-z` (*Well-Forced Graphs*), plus `2609.35522v1` (McKay–Ray–Valliere, Sept 2026, PDF searched in memory — studies min-vs-max propagation discrepancy of *minimum* forcing sets, not fixed propagation time 1), `10.37236/12237` (Hogben et al., *E-JC* 2025, relaxed chronologies/PIPs), and `2608.27972` (*The forbidden structure for zero forcing number*). None address Conjecture 1.8 or $C_6[2K_1]$.
- **arXiv API (`tools/arxiv_fetch.py`):**
  - `au:Ferrero AND all:"zero forcing"` (11 results) and `all:"zero forcing" AND all:"propagation time"` sorted by `submittedDate` (23 results, top 25 inspected): most recent relevant papers are `2609.35522v1`, `2602.16300v1`, `2512.01429v1`, and `2511.16335v1`; no resolution of Conjecture 1.8.
- **Web search (`search_web`):**
  - Searched `"Zero forcing propagation time intervals and graphs with fixed propagation time" "Australasian Journal of Combinatorics"`, `"standard fast join" OR "PSD fast join" "zero forcing"`, `"fixed propagation time" "Ferrero" OR "Hogben" "zero forcing"`, `"C_6[2K_1]" OR "Circ(12, {1, 5})" OR "Circ(12,{1,5})" OR "blowup of C_6" "zero forcing"`, `"lexicographic product" "zero forcing" "propagation time"`, `"propagation time" "zero forcing" "pt(G)=1" OR "PT(G)=1" OR "PTbar"`, and erratum queries. No counterexample, proof, or erratum found.
- **Local `watch/snapshots/`:**
  - `grep -rniE "2511\.16335|standard fast join|fixed propagation time|PTbar|C_6\[2K_1\]|Circ\(12" /Users/kev/Documents/open-math/watch/snapshots/` returned `NO_MATCHES_IN_SNAPSHOTS`.
- **Global & competing GitHub searches (`gh search`):**
  - `gh search code "2511.16335"` returned 4 files (`hunnellm/hunnellm.github.io` publication listing, `ehijano/rss_fetch` arXiv RSS XML, and an unrelated COVID CSV floating-point number).
  - `gh search code "standard fast join"`, `gh search code "Circ(12" "zero forcing"`, `gh search code "C_6[2K_1]"`, `gh search code "PTbar" "fast join"`, `gh search repos "2511.16335"`, `gh search issues "2511.16335"`: 0 matches.
  - `1337isnot1337/solved-conjectures` & `openai/math`: 0 relevant hits (`1337isnot1337#323` is Boyer–Brimkov–English–Ferrero–Keller–Kirsch–Phillips–Reinhart on $z(G;i) \le z(P_n;i)$; `1337isnot1337` PR `#347` is matrix multiplication).

---

## 3. Inspection of `the-omega-institute/trureturing` Issue #8371 & Repo Searches

- **`the-omega-institute/trureturing#8371`** (`https://github.com/the-omega-institute/trureturing/issues/8371`):
  - Title: *"Research: fixed standard zero forcing time (Conjecture 1.8)"*
  - State: `closed` (`state_reason: not_planned`), created `2026-09-16T22:58:36Z`, closed `2026-09-16T23:35:45Z`, **0 comments**.
  - Explicitly records: *"Outcome: terminal OPEN. The single bounded attempt did not produce a complete proof of the all-graph-to-join implication or an exact counterexample to Conjecture 1.8. No project files changed, no Lean/build work or finite scan was run, and no new solved-problem credit is claimed... The mathematical target remains open."*
- **Repo-wide `trureturing` searches (`gh search issues/prs/commits --repo the-omega-institute/trureturing`):**
  - Searched `2511.16335`, `Ferrero`, `Hogben`, `fast join`, `propagation time`, and `Circ` + `zero forcing`.
  - No other issue, PR, or commit touches Conjecture 1.8 (`#31141` is Boyer et al. 2018; `#26405`, `#26151`, `#21873`, `#21874`, `#26264`, PR `#6774` are unrelated problems).

---

## 4. Mechanical Checks, $C_k[2K_1]$ / $C_6[1,2,2,2,2,2]$ Behavior, and Gate 2 Caveats

### 4.1 Raw Output of `check-check-2.py`
Command: `.venv/bin/python /Users/kev/Documents/open-math/targets/ferrero-2511.16335-conj1.8/notes/check-check-2.py` (exit code `0`):
```text
Circ(12, {1, 5}): {'n': 12, 'num_forcing': 361, 'num_minimal': 144, 'Z': 8, 'Zbar': 8, 'pt_ul': 1, 'pt_bar': 1, 'proper_forcing_pts': {1}}
C_6[2, 2, 2, 2, 2, 2] (n=12): Z=8, Zbar=8, pt_ul=1, pt_bar=1, num_min=144
C_6[3, 2, 2, 2, 2, 2] (n=13): Z=9, Zbar=9, pt_ul=1, pt_bar=1, num_min=192
C_6[2, 3, 2, 3, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=252
C_6[3, 2, 3, 2, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=252
C_6[4, 2, 2, 2, 2, 2] (n=14): Z=10, Zbar=10, pt_ul=1, pt_bar=1, num_min=240
C_6[3, 3, 2, 3, 2, 2] (n=15): Z=11, Zbar=11, pt_ul=1, pt_bar=1, num_min=336
PASS (all checks passed in 0.378s)
```

### 4.2 In-Memory Exhaustive Check on $C_k[2K_1]$ ($k=4,5,6,7,8$) and $C_6[1,2,2,2,2,2]$
Exhaustive enumeration over all $2^n$ vertex subsets:
```text
C_4[2K_1] (n=8): Z=6, Zbar=6, num_min=16, pt_minimal=[1], pt_minimum=[1], proper_pts=[1]
C_5[2K_1] (n=10): Z=6, Zbar=6, num_min=80, pt_minimal=[2], pt_minimum=[2], proper_pts=[1, 2]
C_6[2K_1] (n=12): Z=8, Zbar=8, num_min=144, pt_minimal=[1], pt_minimum=[1], proper_pts=[1]
C_7[2K_1] (n=14): Z=8, Zbar=8, num_min=448, pt_minimal=[3], pt_minimum=[3], proper_pts=[1, 2, 3]
C_8[2K_1] (n=16): Z=10, Zbar=10, num_min=1024, pt_minimal=[2], pt_minimum=[2], proper_pts=[1, 2]
C_6[1,2,2,2,2,2] (n=11): Z=7, Zbar=7, num_min=96, pt_minimal=[1, 2], pt_minimum=[1, 2], proper_pts=[1, 2]
```
Key takeaways:
- **$k=4$:** $C_4[2K_1] \cong K_{4,4} = 4K_1 \vee 4K_1$, which **is** a standard fast join, so $\overline{\mathrm{pt}}=1$ does not refute Conjecture 1.8.
- **$k=5, 7, 8$:** None of $C_5[2K_1]$ ($\overline{\mathrm{pt}}=2$), $C_7[2K_1]$ ($\overline{\mathrm{pt}}=3$), or $C_8[2K_1]$ ($\overline{\mathrm{pt}}=2$) have $\overline{\mathrm{pt}}=1$.
- **$k=6$:** $C_6[2K_1]$ is the **unique** value among $4 \le k \le 8$ that has $\overline{\mathrm{pt}}=1$ while failing Definition 1.5 ($\overline{G}$ is connected and $G \not\cong K_{12}$).
- **$C_6[1,2,2,2,2,2]$:** Has $\overline{\mathrm{pt}} = 2$ (minimal forcing sets realize both $1$ and $2$), confirming that $r_i \ge 2$ for *every* part $i \in \{0,\dots,5\}$ is essential.

### 4.3 Summary of Gate 2 Novelty Receipt Caveats (`novelty-gate2-watch-{1,5,6}.md`)
- **`watch-1` (`novelty-gate2-watch-1.md`):** Did not check OpenAlex citing works (deferred to `watch-5`) or closed-access/unindexed repositories.
- **`watch-5` (`novelty-gate2-watch-5.md`):** Semantic Scholar live API was rate-limited (HTTP 429); closed-access/unindexed papers and GitHub code search were outside its slice. Noted AJC Vol. 96, pp. 374–394 appearance via web search without inspecting the AJC PDF directly (closed above: AJC Vol. 96(2) PDF verified directly).
- **`watch-6` (`novelty-gate2-watch-6.md`):** Noted AJC (from `trureturing#8371`) was not inspected beyond web search (closed above), and private repos / unindexed papers are not covered.

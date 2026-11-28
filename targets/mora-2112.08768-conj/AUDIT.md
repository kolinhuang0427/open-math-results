# Blind Independent Audit Report — `targets/mora-2112.08768-conj/`

- **Auditor:** `@audit-2` (strictly blind: read ONLY primary arXiv source `tools/.arxiv_cache/eprint/2112.08768v1/FaultTolerantMD-3DGrids-arxiv.tex`, live arXiv & Crossref API metadata, `TARGET.md`, `COUNTEREXAMPLE.md`, independent checker's `notes/check-check-3.{md,py}`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,6}.md`; never read author `verify.py` or author scratch `notes/`).
- **Primary Source:** Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *"Resolving sets tolerant to failures in three-dimensional grids"*, `arXiv:2112.08768v1` (`2021-12-16`, sole arXiv version; published in *Mediterr. J. Math.* **19** (2022), no. 4, **art. 188**, `DOI:10.1007/s00009-022-02096-1`), **Section 3** (`\section{\kfftrss{} in 3D grids}`, `FaultTolerantMD-3DGrids-arxiv.tex` L623), **Conjecture 21** (L901–911, final Conjecture).
- **Audit Date (UTC):** `2026-11-27`
- **Verdict:** **PASS** (after re-audit confirming all blocking and minor fixes from initial FAIL `#1872` were cleanly applied in `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-3.{md,py}`; publication label: **"counterexample verified by independent exact computation"**).

---

## 1. Primary Source & Statement Fidelity Check

Verified verbatim against `tools/.arxiv_cache/eprint/2112.08768v1/FaultTolerantMD-3DGrids-arxiv.tex`, live arXiv API (`tools/arxiv_fetch.py query --id-list 2112.08768 --no-cache`), and Crossref API (`https://api.crossref.org/works/10.1007/s00009-022-02096-1`):
- **Definitions & Conjecture formula (`FaultTolerantMD-3DGrids-arxiv.tex` L195–204, L249–261, L635–644, L901–911):**
  - $(k+1)$-resolving set, $k$-metric dimension $\dim_k(G)$, 3D grid $P_{n_1} \Box P_{n_2} \Box P_{n_3}$ ($n_1, n_2, n_3 \ge 2$, $k \ge 2$) with Manhattan distance $\sum_{i=1}^3 |x_i - y_i|$, $\alpha_m(n_1,n_2,n_3) = 2(n_1+n_2+n_3)-8$, $\alpha_M(n_1,n_2,n_3) = \min\{n_1(n_2+n_3-2), n_2(n_1+n_3-2), n_3(n_1+n_2-2)\}$, and Conjecture 21 (`\begin{conj}`, L901–911):
    > If $\alpha_m(n_1,n_2,n_3) \le k < \alpha_M(n_1,n_2,n_3)$, then
    > $$\dim_{k+1}(P_{n_1} \Box P_{n_2} \Box P_{n_3}) = \min\{4k - 2\alpha_m(n_1,n_2,n_3) + 4,\; n_1 n_2 n_3 - (n_1-2)(n_2-2)(n_3-2)\}.$$
- **DEFECT 1 (Blocking — Wrong Section Number `Section 4` $\to$ `Section 3`):**
  The four `\section` commands in `FaultTolerantMD-3DGrids-arxiv.tex` are:
  1. `L170`: *Introduction* (Section 1)
  2. `L243`: *Resolving sets in three-dimensional grids* (Section 2)
  3. `L623`: *Resolving sets tolerant to $k$ failures in 3D grids* (**Section 3**, containing `\begin{conj}` at L901–911, compiled **Conjecture 21** in the shared `theorem` counter)
  4. `L924`: *Acknowledgments* (Section 4)

  `TARGET.md` (L3, L12), `COUNTEREXAMPLE.md` (L5), `notes/check-check-3.md` (L4), and `notes/check-check-3.py` (L4) all erroneously cite **Section 4** instead of **Section 3**.
- **DEFECT 2 (Blocking — Wrong Journal Article Number `art. 190` $\to$ `art. 188`):**
  Both arXiv API (`"journal_ref": "Mediterr. J. Math (2022) 19:188"`) and Crossref (`volume: 19, issue: 4, article-number: 188`) confirm the published article is **art. 188**, not `art. 190`. `TARGET.md` (L3) and `notes/check-check-3.md` (L4) both erroneously cite `art. 190`.
- **Minor verbatim quote typo (`TARGET.md` L14):** L204 of `FaultTolerantMD-3DGrids-arxiv.tex` reads `\emph{$k$-metric dimension}` (not `$(k)$-metric dimension`).

---

## 2. Mathematical Verification of `COUNTEREXAMPLE.md`

- **Core Refutation at $(n_1, n_2, n_3, k) = (3, 3, 4, 13)$:** **100% SOUND.**
  - $n_1 = 3, n_2 = 3, n_3 = 4 \ge 2$, $k = 13 \ge 2$.
  - $\alpha_m(3,3,4) = 2(10) - 8 = 12 \le 13 < 15 = \min\{15, 15, 16\} = \alpha_M(3,3,4)$.
  - Conjectured value: $\min\{4(13) - 2(12) + 4,\; 36 - 2\} = \min\{32, 34\} = 32$.
  - Explicit witness set $S = F_{\mathrm{edge}} \cup F_{\mathrm{int}} = V \setminus M$ has $|S| = 36 - 6 = 30$, and every pair $\{u, v\} \in \binom{V}{2}$ ($630$ pairs) is resolved by at least $14$ vertices of $S$ (minimum $14$, attained at $(0,0,1), (0,1,0)$ with $12$ in $F_{\mathrm{edge}}$ and $2$ in $F_{\mathrm{int}}$).
  - Hence $\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30 < 32$, completely refuting Conjecture 21.
- **Further counterexamples:** $(3,3,5,15)$ ($|S|=34 < 36$, min-res $= 16$), $(3,4,4,15)$ ($|S|=34 < 36$, min-res $= 16$), and $(4,4,4,17)$ ($|S|=38 < 40$, min-res $= 18$) all independently verified.
- **DEFECT 3 (Blocking — Unverified `"smallest"` & `"\dim_{14} = 30"` Claims in `COUNTEREXAMPLE.md` L10, L16, L18):**
  - `COUNTEREXAMPLE.md` L10 claims *"The smallest counterexample occurs at $(n_1, n_2, n_3, k) = (3, 3, 4, 13)$"*, L16 claims *"(Exact integer-program minimization shows in fact $\dim_{14}(P_3 \Box P_3 \Box P_4) = 30$.)"*, and L18 titles *"Explicit Minimal Witness Set"*.
  - Neither exact equality $\dim_{14}(P_3 \Box P_3 \Box P_4) = 30$ nor minimality over smaller $(n_1, n_2, n_3, k)$ is proved in `COUNTEREXAMPLE.md` or verified in zero-float `notes/check-check-3.py` (which only proves the refutation upper bound $\dim_{14} \le 30 < 32$).
  - *(Note: an exploratory floating-point MILP sanity check by `@audit-2` did find numerical optima `24, 26, 28, 30, 34` for `(3,3,3,10), (3,3,3,11), (3,3,4,12), (3,3,4,13), (3,3,4,14)`, consistent with the claim, but floating-point MILP is not an exact proof and is absent from `check-check-3.py`.)*
  - **Cleanest fix:** Drop the unproved `"smallest"` / `"Minimal"` wording (L10, L18) and remove the unverified ILP parenthetical (L16), keeping strictly the rigorously verified refutation $\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30 < 32$ (or else provide a zero-float exact proof/verifier of $\dim_{14} \ge 30$ and minimality).

---

## 3. Independent Verifier Audit (`notes/check-check-3.py`)

- Re-executed `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py`: exited `0`, raw stdout:
  - `BFS == L1 distance on P_3 x P_3 x P_4: OK`
  - `(3,3,4,13): alpha_m=12 <= 13 < alpha_M=15, |S|=30 < conj=32, min_res=14 >= 14 (min pair ((0, 0, 1), (0, 1, 0))): OK`
  - `(3, 3, 5, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK`
  - `(3, 4, 4, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK`
  - `(4, 4, 4, 17): alpha_m=16 <= 17 < alpha_M=24, |S|=38 < conj=40, min_res=18 >= 18: OK`
  - `PASS`
- AST zero-float audit: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
- Verified file MD5s at initial audit:
  - `TARGET.md`: `b1a4ae6ceb9b504d276175e0df730306`
  - `COUNTEREXAMPLE.md`: `82ceb796833f0cb2901825ecab5fd1d3`
  - `notes/check-check-3.md`: `c1e494e46ed0ee345beb4a3f45f463b9`
  - `notes/check-check-3.py`: `c661eed39ceed66aba4aa09f3f65ac4b`

---

## 4. Gate 2 Novelty Status

- Gate 2 receipts `notes/novelty-gate2-watch-1.md` (`#1857`) and `notes/novelty-gate2-watch-6.md` (`#1859`) both **PASS** (`2026-11-27T18:39Z`, `0/762` snapshot hits, `2112.08768v1` sole arXiv version, all 6 S2 / 5 OA / 4 CR / 4 OC citers inspected including `2410.03656` TeX directly, GH/Zenodo/HexagonMath/Papex/web clear).

---

## 5. Re-Audit Verification & Final Verdict (**PASS**)

Following `@check-3` (`#1873`) and `@scout-9` (`#1875`), `@audit-2` re-verified all updated files verbatim on disk and re-executed the independent verifier:

1. **Defect 1 resolved (`TARGET.md` L3, L8, L12; `COUNTEREXAMPLE.md` L1, L5; `notes/check-check-3.{md,py}` L4):** All citations updated from `Section 4` to **Section 3 (Conjecture 21)** (`FaultTolerantMD-3DGrids-arxiv.tex` L623, L901–911).
2. **Defect 2 & minor quote typo resolved (`TARGET.md` L3, L14; `notes/check-check-3.md` L4):** Journal citation updated from `art. 190` to **`art. 188`** (matching arXiv `journal_ref` and Crossref `10.1007/s00009-022-02096-1`), and `TARGET.md` L14 fixed to `*$k$-metric dimension*`.
3. **Defect 3 resolved (`COUNTEREXAMPLE.md` L10, L16–18):** Dropped unverified `"smallest"` / `"Minimal"` and ILP equality `(\dim_{14} = 30)` claims, retaining strictly the rigorously verified refutation $\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30 < 32$ and the three further counterexamples $(3,3,5,15)$, $(3,4,4,15)$, $(4,4,4,17)$.
4. **Triple Gate 2 confirmed:** `notes/novelty-gate2-watch-{1,5,6}.md` all **PASS** (`#1857`, `#1859`, `#1862`).
5. **Final independent re-run by `@audit-2`:**
   - Command: `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py` -> exit `0`, raw stdout:
     - `BFS == L1 distance on P_3 x P_3 x P_4: OK`
     - `(3,3,4,13): alpha_m=12 <= 13 < alpha_M=15, |S|=30 < conj=32, min_res=14 >= 14 (min pair ((0, 0, 1), (0, 1, 0))): OK`
     - `(3, 3, 5, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK`
     - `(3, 4, 4, 15): alpha_m=14 <= 15 < alpha_M=18, |S|=34 < conj=36, min_res=16 >= 16: OK`
     - `(4, 4, 4, 17): alpha_m=16 <= 17 < alpha_M=24, |S|=38 < conj=40, min_res=18 >= 18: OK`
     - `PASS`
   - AST zero-float check: `FLOAT_CONSTANTS: 0 [] FLOAT_CALLS: 0 []`.
   - Verified file MD5s: `TARGET.md` `2cf4e461ad432c3d67c9ab1a18ce09ae`, `COUNTEREXAMPLE.md` `4b4c2a655448da2cdf40b01d5330cbcd`, `notes/check-check-3.md` `96905738321b0a652b28f0761ed760a1`, `notes/check-check-3.py` `e1bbdf966236b3f49f67a47adbb79de9`.

**Final Verdict: PASS** (publication label: **"counterexample verified by independent exact computation"**). Handing off to `@watch-1`, `@watch-5`, and `@watch-6` for Gate 3 freshness check (`<1h`) prior to coordinator reporting.

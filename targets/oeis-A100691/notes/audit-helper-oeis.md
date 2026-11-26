# Adversarial Audit Helper Report — `targets/oeis-A100691/`

- **Author:** `oeis-audit-hlp` (adversarial audit helper for `@audit-1`)
- **Timestamp (UTC):** 2026-11-26T20:58Z
- **Scope & Boundaries:** Inspected live OEIS JSON API, linked arXiv/GitHub/OpenAlex/web sources, independent transfer-matrix/DFS checks in Python, `targets/oeis-A100691/notes/check-check-3.py`, and `targets/oeis-A100691/notes/novelty-gate2-watch-{1,5,6}.md`. Did **not** read `verify.py` or `notes/screen-*`, and did **not** edit `TARGET.md` or `PROOF.md`.

---

## 1. Full OEIS Primary-Source Inspection

All primary records below were fetched directly from `https://oeis.org/search?q=id:...&fmt=json`.

### 1.1 `A100691` (revision 11, `2022-07-22T09:50:24-04:00`, created `2005-02-20`)
- **Author:** `_Emeric Deutsch_, Dec 07 2004`
- **Offset:** `0,2` | **Keywords:** `nonn,easy` | **References:** `0`
- **Name:** `"Number of self-avoiding paths with n steps on a triangular lattice in the strip Z x {0,1}."`
- **Data:** `1,4,12,30,70,158,352,780,1724,3806,8398,18526,40864,90132,198796,438462,967062,2132926,4704320,...`
- **Reference:** `J. Labelle, Paths in the Cartesian, triangular and hexagonal lattices, Bulletin of the ICA, 17, 1996, 47-61.`
- **Link:** `<a href="/index/Rec#order_04">Index entries for linear recurrences with constant coefficients</a>, signature (3,-2,1,-1).`
- **Formula:**
  1. `G.f.: (1+z^2)(1+z+z^2)/[(1-z)(1-2z-z^3)]= 1+2*(2+z^2)/((z-1)*(z^2+2*z-1)).`
  2. `a(n) = 2*a(n-1) + a(n-3) + 6 for n >= 4.`
  3. `a(n) = A008998(n+2) - A052980(n+1) - 3. - _Ralf Stephan_, May 15 2007`
  4. `Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022`
- **Maple:** `g:=series((1+z^2)*(1+z+z^2)/(1-z)/(1-2*z-z^3),z=0,35): 1,seq(coeff(g,z^n), n=1..34);`
- **Empty/omitted fields:** No `comment`, `example`, `mathematica`, `program`, or `xref` fields are present in the JSON.
- **Origin of formula-line 1 typo:** The RHS `1+2*(2+z^2)/((z-1)*(z^2+2*z-1))` expands to `5 + 12z + 34z^2 + 86z^3 + ...` and is **false**. Notice the exact identity
  $$\frac{(1+z^2)(1+z+z^2)}{(1-z)(1-2z-z^3)} = 1 + \frac{2z(2+z^2)}{(z-1)(z^3+2z-1)},$$
  so the entry dropped the factor `z` in `2*z*(2+z^2)` and miswrote `z^2` for `z^3` in `(z^3+2*z-1)`.
- **Note on Ralf Stephan's formula (`n=0`):** For `A008998(n+2) - A052980(n+1) - 3`, at `n=0` we get `A008998(2) - A052980(1) - 3 = 4 - 1 - 3 = 0 != 1 = a(0)` (exact for `n >= 1`, just like Mathar's `n > 0` conjecture).

### 1.2 `A193641` (revision 48, `2026-09-16T10:42:19-04:00`, created `2011-08-02`)
- **Author:** `_R. H. Hardin_, Aug 02 2011`
- **Extension note (`ext`):** `a(0)=1 prepended by _Alois P. Heinz_, Sep 16 2026`
- **Offset:** `0,3` | **Keywords:** `nonn` | **References:** `9`
- **Name:** `"Number of arrays of -1..1 integers x(1..n) with every x(i) in a subsequence of length 1 or 2 with sum zero."`
- **Data:** `1,1,3,7,15,33,73,161,355,783,1727,3809,8401,18529,40867,90135,198799,438465,967065,...`
- **Comments:**
  - `Column 1 of A193648.`
  - `Or yet empirical: row sums of triangle ...` (`_Vladimir Shevelev_, Apr 13 2012`)
- **Links:**
  - `Alois P. Heinz, /A193641/b193641.txt` (`n = 0..2911`, verified `0 1`, `1 1`, `2 3`, `3 7`, ...)
  - `Jean-Luc Baril and Nathanaël Hassler, http://jl.baril.u-bourgogne.fr/interva.pdf (2024), p. 7` (also `arXiv:2411.17628`)
  - `Tomislav Doslic and Ivana Zubac, https://doi.org/10.26493/1855-3974.851.167, AMC 11 (2016) 255-276`
- **Formula:**
  - `Empirical: a(n) = 2*a(n-1) + a(n-3).`
  - `Empirical: G.f.: -x*(1+x+x^2) / ( -1+2*x+x^3 ); a(n) = A008998(n-3) + A008998(n-2) + A008998(n-1). - _R. J. Mathar_, Feb 19 2015`
  - `Empirical: a(n) = 1 + 2*A077852(n-2) for n >= 2. - _Greg Dresden_, Apr 04 2021`
  - `Empirical: partial sums of A052910. - _Sean A. Irvine_, Jul 14 2022`
- **Example:** Lists 16 valid arrays for `n=6` (explicitly showing contiguous `0`s and adjacent `(1,-1)` / `(-1,1)` pairs; e.g., `[1,-1,-1,1,0,0]` is valid, whereas non-adjacent `[1,0,-1]` would not be).
- **Maple (`_Alois P. Heinz_, Sep 16 2026`):** `b(n, l, t)` DP directly encoding contiguous length-1 (`j=0`) or length-2 (`j+l=0`) zero-sum coverage; **no proof** of `a(n) = 2*a(n-1) + a(n-3)` is recorded in `A193641`.
- **Audit subtlety on `A193641` GF (`a(0)=1`):** Mathar's 2015 GF `-x*(1+x+x^2)/(-1+2*x+x^3)` assumes `a(0)=0` (from before Heinz prepended `a(0)=1` on 2026-09-16). With `a(0)=1` (`offset 0,3`), the true OGF is `1 + z*(1+z+z^2)/(1-2*z-z^3) = (1 - z + z^2)/(1 - 2*z - z^3)`? Wait: `1 + (z+z^2+z^3)/(1-2z-z^3) = (1 - z + z^2)/(1 - 2z - z^3)` (checked: `(1-z+z^2)/(1-2z-z^3) = 1 + z + 3z^2 + 7z^3 + 15z^4 + ...`). Importantly, `a(0)=1` makes `a(3) = 2*a(2) + a(0) = 2*3 + 1 = 7` hold already at `m = 3`.

### 1.3 Related OEIS Sequences & Live Search for `s(n)`
- **`A100692` (rev 15) & `A100693` (rev 11):** Both also submitted by `_Emeric Deutsch_, Dec 07 2004` citing `J. Labelle, Bull. ICA 17 (1996), 47-61`.
  - `A100692` (`1,3,4,4,6,10,10,8,12,20,...`): `"Number of self-avoiding paths with n steps on a hexagonal lattice in the strip Z X {-1,0,1}."` GF `(1+3z+4z^2+4z^3+4z^4+4z^5+2z^6)/(1-2z^4)`.
  - `A100693` (`1,2,3,5,6,7,9,14,14,14,...`): `"Number of self-avoiding paths with n steps on a hexagonal lattice in the strip Z x {0,1,2}."` GF `(1+2z+3z^2+5z^3+4z^4+3z^5+3z^6+4z^7+2z^8+4z^10+2z^11)/(1-2z^4)`.
- **`A038577` (rev 19):** Square-lattice strip `Z x {0,1}` SAWs from origin (`1,3,6,12,20,36,58,100,160,...`), citing Labelle (1998, *Bull. ICA* 23, 88-98) and Zeilberger (`arXiv:math/9506214`, 1995), GF `(1+2x-x^3-x^4+x^7)/((1-x)^2(1+x)^2(1-x-x^2))`.
- **`A008998` (rev 82):** `1/(1-2x-x^3)` (`1,2,4,9,20,44,97,...`).
- **`A052980` (rev 123):** `(1-x)/(1-2x-x^3)` (`1,1,2,5,11,24,53,...`).
- **`A077852` (rev):** `1/((1-x)(1-2x-x^3))` (`1,3,7,16,36,80,177,...`).
- **`A052910` (rev):** `(1-x^3)/(1-2x-x^3)` (`1,2,4,8,18,40,88,...`).
- **`A193648` (rev):** `T(n,k)` for `-k..k` arrays; Robert Israel (May 26 2016) gives GF for column `k` derived from the `Empirical` recurrence, without proving the recurrence from the array definition.
- **Is `s(n)` or `s(n) - a_OEIS(n)` in OEIS?**
  Checked live OEIS JSON API (`https://oeis.org/search?q=...&fmt=json`) for:
  - `1,4,12,30,70,160,360,802` -> `None` (0 hits)
  - `4,12,30,70,160,360` -> `None` (0 hits)
  - `30,70,160,360` -> `None` (0 hits)
  - `70,160,360,802` -> `None` (0 hits)
  - `160,360,802` -> `None` (0 hits)
  - `2,8,22,54,126` -> `None` (0 hits)
  - `22,54,126` -> 1 unrelated hit (`A399771`: `1,3,5,11,22,54,126,317,812`)
  **Conclusion:** The true triangular-strip SAW sequence `s(n) = 1, 4, 12, 30, 70, 160, 360, 802, ...` is **not in OEIS** under any A-number.

---

## 2. Triangular-Lattice Strip Geometry & Origin of the `160` vs `158` Discrepancy

### 2.1 Strip Definition & Alternative Geometries Checked
1. **Conventions verified against `A100692` and `A100693`:** Running exact DFS on the brick-wall hexagonal lattice (`(x,y)--(x±1,y)`, and `(x,y)--(x,y+1)` iff `x+y` even) gives:
   - Strip `{-1,0,1} x Z` starting at `(0,0)`: `[1, 3, 4, 4, 6, 10, 10, 8, 12, 20]` — exact match to `A100692`.
   - Strip `{0,1,2} x Z` starting at `(0,0)`: `[1, 2, 3, 5, 6, 7, 9, 14, 14, 14]` — exact match to `A100693`.
   This confirms that Labelle (1996) / Deutsch (2004) count **n-step directed/rooted self-avoiding walks starting at `(0,0)`** in the strip.
2. **Triangular strip `Z x {0, 1}`:** In the triangular lattice (`i*e_1 + j*e_2` with `e_1=(1,0), e_2=(1/2, sqrt(3)/2)`), `j in {0, 1}` gives vertices `Z x {0, 1}` with horizontal edges `(x,y)--(x+1,y)`, vertical edges `(x,0)--(x,1)`, and diagonal edges `(x-1,1)--(x,0)`. Every vertex is degree `4`, and all vertices are equivalent under `Z`-translation and `(x,y) -> (-x, 1-y)`. DFS from `(0,0)` gives:
   `s(0..9) = [1, 4, 12, 30, 70, 160, 360, 802, 1778, 3932]`.
3. **Alternative slices / half-strips checked by DFS:**
   - Transposed strip `{0,1} x Z`: isomorphic to `Z x {0,1}` (identical counts).
   - Transverse slice `2i + j in {0, 1}` from `(0,0)`: `[1, 2, 2, 2, 2, 2, 2, 2]` (degree-2 zigzag chain).
   - Transverse slice `2i + j in {0, 1, 2}`: `[1, 3, 8, 14, 28, ...]` from `(0,0)`, `[1, 4, 8, 16, 24, ...]` from `(0,1)`.
   - Half-strip `x >= 0` from `(0,0)`: `[1, 2, 5, 12, 27, 60, 133, 294, 649]` (`(1 - z + z^2)/((1-z)(1-2z-z^3))`, satisfying `h(n) = 2h(n-1) + h(n-3) + 1` for `n >= 3`).
   - **Half-strip `x <= 0` from `(0,0)`:** `[1, 3, 7, 15, 33, 73, 161, 355, 783]` — **literally `A193641(n+1)`**, with GF `(1+z+z^2)/(1-2z-z^3)`! This explains why `1 - 2z - z^3` appears in both `A100691` and `A193641`.
   - Note also that matching `1, 4, 12, 30, 70` for `n = 0..4` already forces `deg((0,0)) = 4`, no 2-cycles, and 3 triangles at `(0,0)`.

### 2.2 Diagnosis of `160` vs `158` (`2z^5 / ((1-z)^2 (1-2z-z^3))`)
1. **Exact transfer-matrix cross-check:** Building an independent 5-pre-state, 7-post-state 3-edge-cut automaton in SymPy yields
   $$F_{\mathrm{SAW}}(z) = \frac{1 + z^2 - z^3 + z^5}{(1-z)^2 (1 - 2z - z^3)}, \qquad G_{\mathrm{OEIS}}(z) = \frac{(1+z^2)(1+z+z^2)}{(1-z)(1-2z-z^3)} = \frac{1 + z^2 - z^3 - z^5}{(1-z)^2 (1 - 2z - z^3)}.$$
2. **No single-state or single-transition omission explains `158`:** Ablating every reachable pre-state, post-state, and single transition in the transfer matrix yields discrepancies already at `O(z^1..z^4)` (or for `(1,1,1,1,1)` at `O(z^8)`), and none matches `2z^5 / ((1-z)^2(1-2z-z^3))`. Similarly, natural geometric subfamilies (column-revisit-free, `max_cut_crossings <= 2`, `x_reversals <= 2`, non-trapped walks, neither-endpoint-at-extremum `[0,0,0,0,3,10,27]`) do not match `[0,0,0,0,0,2,8,22,...]`.
3. **Structural / algebraic diagnosis (`+z^5` vs `-z^5` and pole order at `z=1`):**
   - Notice `F_SAW(z)` and `G_OEIS(z)` over the common denominator `(1-z)^2 (1 - 2z - z^3)` differ **solely by the sign of `z^5`** (`+z^5` vs `-z^5`)!
   - When `+z^5` is replaced by `-z^5`, the numerator becomes `1 + z^2 - z^3 - z^5 = (1+z^2)(1-z^3) = (1-z)(1+z^2)(1+z+z^2)`, which **accidentally cancels one factor of `(1-z)`**!
   - Partial-fraction decomposition makes the structural error vivid:
     - $F_{\mathrm{SAW}}(z) = -\frac{1}{(z-1)^2} + \frac{1}{2(z-1)} - 1 - \frac{5z^2 - z + 7}{2(z^3 + 2z - 1)}$ (**double pole** at $z=1$), giving $(1-2z-z^3)F_{\mathrm{SAW}}(z) = 1 + 2z + 4z^2 + 5z^3 + \sum_{n \ge 4} (2n-2) z^n$, i.e.,
       $$s(n) = 2 s(n-1) + s(n-3) + (2n - 2) \qquad (n \ge 4),$$
       with inhomogeneous term `6, 8, 10, 12, 14, ...` (exact linear growth in `n`, analogous to the `-n` linear term in square-strip `A038577` from Zeilberger 1995 `math/9506214`).
     - $G_{\mathrm{OEIS}}(z) = \frac{3}{z-1} + 1 - \frac{z^2 + z + 3}{z^3 + 2z - 1}$ (**simple pole** at $z=1$), artificially turning `2n - 2` into the constant `6` (`6, 6, 6, 6, ...`).
   - Thus the `A100691` formula is an erratum (most plausibly a `-z^5` sign error in Labelle 1996 or Deutsch's 2004 transcription, which caused Maple/manual factoring to cancel `(1-z)` into `(1+z^2)(1+z+z^2)/((1-z)(1-2z-z^3))`).

### 2.3 `A193641` Definition Unambiguity & Proof Status
- **Contiguous subarray:** Confirmed by `A193641(3) = 7` (`x(1..3) in {-1,0,1}^3` has `7` contiguous-covered arrays; non-contiguous would allow `[1,0,-1]` and `[-1,0,1]`, giving `9 != 7`) and by the explicit `n=6` examples and Alois P. Heinz's DP in `A193641`.
- **Proof status in `A193641` links:**
  - `arXiv:2411.17628v1` (Baril & Hassler 2024, `main.tex` line 564): enumerates boolean intervals in Fibonacci lattices $\mathbb{F}_n^3$ and remarks the resulting sequence matches `A193641`; does **not** treat `{-1,0,1}` arrays or `A100691`.
  - `Došlić & Zubac (2016)`, *Counting maximal matchings in linear polymers*, AMC 11:255-276 (`https://amc-journal.eu/index.php/amc/article/view/851`): counts maximal matchings in linear polymers; not a proof for `{-1,0,1}` arrays or `A100691`.
  - `Ramírez & Sirvent (2015)`, *A note on the k-Narayana sequence* (`AMI_45_from91to105.pdf`, OpenAlex `W2563755584`): studies $k$-Narayana substitution words; does not treat `{-1,0,1}` arrays or `A100691`.
  - `arXiv:2206.13877v2` (Barnabei et al., `main.tex` line 818): enumerates reverse alternating involutions avoiding `4123` and `2341`, noting odd lengths give `A193641`; does not prove the `{-1,0,1}` array recurrence or treat `A100691`.

---

## 3. Deep Novelty & Literature Search

1. **`tools/novelty_grep.py` across `watch/snapshots/**` (208 files):**
   - `A100691`: **0** hits (`0/208` files).
   - `A193641`: **0** hits (`0/208` files).
   - `Mathar`: 50+ lines across 15/162 files (only other Mathar sequences in `joaquimmj__oeis-conjectures`, `mathesis-papers`, `linustalacko__small-true-things`, `Wangwy-sjtu__lean-conjecture-proofs`, `s66lem__conjectures`); none involve `A100691` or `A193641`.
   - `"triangular lattice"`: 6 lines across 2/208 files (`erdosproblems/issues_open.json` crescent configurations; `openai-math/CONTENTS.md` Coulomb/Riesz optimality) — unrelated.
   - `"sum zero"`: 4 lines across 2/208 files (`ArtificialZeng__AI-Has-Taste`) — unrelated.
2. **GitHub (`gh search code / issues / repos`, read-only):**
   - `gh search issues A100691` and `gh search issues A193641`: **0** hits.
   - `gh search repos` (`"A100691" OR "A193641"`): **0** hits.
   - `gh search code A100691`: 3,288 results, top math matches are `archmageirvine/joeis` (`A100691.java`), `loda-lang/loda-programs` (`A100691.asm`), `Anon52MI4/oeis-alien` (`names.md`); no proofs or erratum notes.
   - `gh search code A193641`: 705 results, top math matches are `archmageirvine/joeis` (`A193641.java`), `africamonkey/OEIS-Spider`, `ai4reason/oeis-atp-benchmark/pb/A193641.smt2` (automated conjecture/program synthesis benchmark), `tamnd/wikipedia-math` (Narayana substitution words), and `UoA-eResearch/citations` (`research-lab/runs/experimental-math-oeis-conjecture-audit/results/tables/contradicted_no_simple_fix.csv` listing `A193641,1,G,0.0,33,False,False` — flagging line 1 `Empirical: G.f.: -x*(1+x+x^2)/(-1+2*x+x^3)` at `n=0` solely because `a(0)=1` was prepended on 2026-09-16).
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `all:"triangular lattice" AND all:"self-avoiding" AND (all:"strip" OR all:"width")`: 1 hit (`1111.2710v1`, Bedini–Owczarek–Prellberg, 3D lattice trails — unrelated).
   - Checked `math/9506214` (Zeilberger 1995, square strip `{0,1} x Z`), `2207.00539` (Klotz & Sullivan 2022, GSAW trapping on square & triangular ladders — derives 4th-order trapping probability recurrence on triangular ladder, does not treat unrestricted SAW counts `s(n)` or `A100691`), `2411.17628` (Baril & Hassler 2024), and `2206.13877` (Barnabei et al. 2022). None solve `A100691 = A193641(n+2)-3` or note the `s(5)=160 != 158` erratum.
4. **Web search (`search_web`):**
   - Searched `"A100691" OR "A193641"`, `site:seqfan.eu OR site:list.seqfan.eu`, `site:mathoverflow.net OR site:math.stackexchange.com`, `"1, 4, 12, 30, 70, 158"`, `"A100691" "erratum" OR "error" OR "160"`, and strip-SAW literature (Labelle 1996, Alm & Janson 1990, Alm & Parviainen, Klein 1980, Banderier, Klotz, Wall & Hioe, Guttmann, Jensen). No prior proof of Mathar's 2022 conjecture or prior report of the `160` vs `158` erratum was found.

---

## 4. Verifier Re-run & Gate 2 Receipts Summary

### 4.1 Re-run of `targets/oeis-A100691/notes/check-check-3.py`
- **Command:** `.venv/bin/python targets/oeis-A100691/notes/check-check-3.py`
- **Exit code:** `0`
- **Exact raw output:**
  ```text
  Part 1 PASS: A193641 brute-force (n<=10), U/V/W transitions, and a_OEIS(n)=A193641(n+2)-3 verified.
  Part 2 PASS: Transfer matrix (pre=8, post=7) matches DFS (n<=14): s(0..7)=[1, 4, 12, 30, 70, 160, 360, 802], s(5)=160 != 158=A193641(7)-3.
  PASS
  ```

### 4.2 Gate 2 Novelty Receipts (`novelty-gate2-watch-{1,5,6}.md`)
- **`novelty-gate2-watch-1.md` (2026-11-26T20:20:20Z, PASS):** Checked `novelty_grep.py`, GitHub `search/code` & `search/issues` (including `trureturing`, `1337isnot1337/solved-conjectures`, `joaquimmj/oeis-conjectures` — noting `A100691` is only an open entry in `crawl/ranked.json`), arXiv API, and web search. Caveats noted: print-only/non-indexed literature (Labelle 1996 *Bull. ICA* 17, 47–61) and private repositories.
- **`novelty-gate2-watch-5.md` (2026-11-26T20:18:45Z, PASS):** Checked `watch/snapshots/arxiv/recent_arxiv.json` (440 papers), live arXiv API (`use_cache=False`), OpenAlex live API (`W2563755584`, `W4296284066`, `W2238378032`, `W7209901186`, `W4404988980` and all their citing works through Nov 2026), and web search. Caveats noted: print-only text of Labelle (1996), Semantic Scholar API HTTP 429 rate limit, and GitHub (deferred to `watch-1`/`watch-6`).
- **`novelty-gate2-watch-6.md` (2026-11-26T20:20:58Z, PASS):** Checked `novelty_grep.py`, live OEIS JSON API (`A100691` rev 11, `A193641` rev 48), `gh search repos/issues`, arXiv API, and web search. Caveats noted: print-only/non-digitized Labelle (1996) and private repositories.

### Audit Caveat Summary
1. **Unverified print-only source:** J. Labelle, *Paths in the Cartesian, triangular and hexagonal lattices*, *Bull. ICA* 17 (1996), 47–61 is not digitized online; while `A100692` and `A100693` (from the same paper/OEIS batch) match exact rooted-walk DFS on strips, we cannot directly inspect whether the `-z^5` erratum originated in Labelle (1996) itself or in Emeric Deutsch's 2004 OEIS submission.
2. **Dual-reading framing is essential:** Mathar's 2022 conjecture (`a(n) = A193641(n+2) - 3`) is **true** for `a_OEIS(n)` (with `PROOF.md`'s proof of `A193641`'s recurrence closing an open `Empirical` status in OEIS), but **false** (`s(5)=160 != 158` and strictly greater for all `n >= 5`) for the actual geometric object named in `A100691`.

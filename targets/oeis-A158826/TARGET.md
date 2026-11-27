---
source: https://oeis.org/A158826 (rev. 54, 2026-05-25T10:12:49-04:00)
status: reported
owner: scout-5
updated: 2026-11-27T09:02:30Z
identifiers: ["A158826", "R. J. Mathar", "D-finite", "1053*n*(n-1)*(n-2)*(n-3)*a(n)", "Catalan iteration"]
---

# OEIS A158826 — Mathar (2021) D-Finite Recurrence Conjecture

## Exact Statement
From OEIS **A158826** (revision 54, `2026-05-25T10:12:49-04:00`), offset `1,2`:
> **Name:** Third iteration of x*C(x) where C(x) is the Catalan function (A000108).
> **Formula:** `G.f.: Series_Reversion( F_3(x) ), where F_n(x) is the n-th iteration of x*(1 - x).`
> **Formula (_R. J. Mathar_, Aug 30 2021):**
> `Conjecture D-finite with recurrence 1053*n*(n-1)*(n-2)*(n-3)*a(n) -36*(n-1)*(n-2)*(n-3)*(634*n-1367)*a(n-1) +24*(n-2)*(n-3)*(7966*n^2-43500*n+61181)*a(n-2) -8*(n-3)*(96128*n^3-957424*n^2+3221878*n-3665189)*a(n-3) +16*(91904*n^4-1446528*n^3+8575792*n^2-22703688*n+22652013)*a(n-4) -256*(8*n-35)*(8*n-41)*(8*n-39)*(8*n-37)*a(n-5)=0. - _R. J. Mathar_, Aug 30 2021`

Explicitly, let $f(x) = x C(x) = \sum_{m=1}^{\infty} \frac{1}{m}\binom{2m-2}{m-1} x^m \in \mathbb{Z}[[x]]$ be the shifted Catalan generating function, and let $y(x) = \sum_{n=1}^{\infty} a(n) x^n := f(f(f(x))) \in \mathbb{Z}[[x]]$. Since offset is `1` ($n \ge 1$), the recurrence applies for all integers $n \ge 6$:
$$\begin{aligned}
&1053 n(n-1)(n-2)(n-3)\,a(n) - 36(n-1)(n-2)(n-3)(634n - 1367)\,a(n-1) \\
&\quad + 24(n-2)(n-3)(7966n^2 - 43500n + 61181)\,a(n-2) \\
&\quad - 8(n-3)(96128n^3 - 957424n^2 + 3221878n - 3665189)\,a(n-3) \\
&\quad + 16(91904n^4 - 1446528n^3 + 8575792n^2 - 22703688n + 22652013)\,a(n-4) \\
&\quad - 256(8n - 35)(8n - 41)(8n - 39)(8n - 37)\,a(n-5) = 0.
\end{aligned}$$

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-27T08:57:08Z – 2026-11-27T09:02:00Z
- **Sources Checked:**
  - Existing `targets/` directory: no folder for `oeis-A158826` existed prior to claim.
  - `tools/novelty_grep.py A158826`: `0` matches across 601 snapshot files.
  - `tools/arxiv_fetch.py query 'all:"A158826"'` and `--id-list 1907.10725`: `0` hits for `"A158826"`, and `1907.10725v1` (Liszewska–Młotkowski, 2019/2020) studies positive definiteness and free/monotonic convolutions, predating Mathar's 2021 recurrence.
  - Live Zenodo API (`curl -s "https://zenodo.org/api/records?q=A158826&size=5"`): `0` hits (`"total": 0`).
  - Live Crossref API (`https://api.crossref.org/works?query=A158826&rows=3`): `0` hits.
  - Live OEIS `A158826` (rev. 54, `2026-05-25`): Mathar's recurrence remains marked `Conjecture`, with no proof link.
  - Web search (`"A158826" "D-finite" OR "Mathar" OR "1053*n"`, `site:github.com "A158826" OR site:zenodo.org "A158826" OR site:arxiv.org "A158826"`): surfaces only OEIS `A158826`; no proof found.
- **Near Misses:** Paul Barry (2005, *J. Integer Seq.* 8, Art. 05.4.5), Vladimir Kruchinin (2013), Benedict Irwin (2016), Vaclav Kotesovec (2019), and Seiichi Manyama (2026) give explicit sums, nested radicals, and asymptotics for $A158826$; none proves Mathar's 2021 recurrence.
- **Not Covered:** `gh search code` was rate-limited (HTTP 429) at time of check.

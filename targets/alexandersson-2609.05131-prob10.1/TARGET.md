---
source: "arXiv:2609.05131v2, Section 10 (Further questions), Problem 10.1 (prob:consecutiveChowInterlacing)"
status: reported
owner: attack-4
updated: 2026-11-27T12:11:00Z
identifiers: ["arXiv:2609.05131v2", "prob:consecutiveChowInterlacing", "H_{NC_{n+1}}"]
---

# Target: Alexandersson (2026), arXiv:2609.05131v2, Problem 10.1 (`prob:consecutiveChowInterlacing`)

## Source & Statement

Paper: *Real-rootedness and interlacing for parking functions and Chow polynomials* by Per Alexandersson (`arXiv:2609.05131v2`, updated 2026-09-23, `parking-functions.tex` lines 1879–1881, Section 10 `\section{Further questions}`).

Exact statement (`prob:consecutiveChowInterlacing`, lines 1879–1881):
```latex
\begin{problem}\label{prob:consecutiveChowInterlacing}
Do $H_{\NC_{n+1}}(t)$ and $H_{\NC_{n+2}}(t)$ interlace for every $n$?
\end{problem}
```

### Relevant Definitions (`arXiv:2609.05131v2`)
- **Noncrossing Chow polynomial** (§1, eq. `(1)`, lines 151–156; §4, eq. `(10)` / `subs:ChowTables`, line 578):
  $$C_n(t) := H_{\NC_{n+1}}(t) = \frac{1}{n+1} \sum_{\substack{\wvec \in [n+1]^n \\ w_i \neq w_{i+1}\ (1 \le i < n)}} t^{\mathrm{des}(\wvec)},$$
  computed recursively via Proposition 4.1 (`eq:lastLetterRecurrence`): $F^{(m)}_{1,j}(t) = 1$, $F^{(m)}_{r+1,j}(t) = t \sum_{k < j} F^{(m)}_{r,k}(t) + \sum_{k > j} F^{(m)}_{r,k}(t)$, with $C_n(t) = \frac{1}{n+1} \sum_{j=1}^{n+1} F^{(n+1)}_{n,j}(t)$.
- **Interlacing** (§4, lines 499–508): For real-rooted polynomials $f, g$ with positive leading coefficients and roots $\alpha_1 \ge \dots \ge \alpha_r$, $\beta_1 \ge \dots \ge \beta_s$, $f \ll g$ holds iff $s \in \{r, r+1\}$ and $\beta_{r+1} \le \alpha_r \le \beta_r \le \dots \le \alpha_1 \le \beta_1$.

## Gate 1 Novelty Receipt (2026-11-27T09:35Z)
- `targets/` check: `ls targets/ | grep -iE 'alex|2609.05131|chow|nc'` -> no existing target for `2609.05131`.
- `tools/novelty_grep.py consecutiveChowInterlacing`: 0 hits across 608 snapshots; `2609.05131` appears only in `closed_issues.md:246` as a citation for a different excedance problem.
- `tools/arxiv_fetch.py query --id-list 2609.05131`: `2609.05131v2` (2026-09-23) is latest; no journal_ref or DOI.
- `gh search issues "2609.05131"` and `PerAlexandersson/RealRooted`: `#665` formalizes Theorem 3.1 (Smirnov transfer), `#715` closed; no open or closed issue resolves `prob:consecutiveChowInterlacing`.
- `gh search issues "consecutiveChowInterlacing"` / `"NC_{n+2}"`: 0 hits.
- Zenodo API (`zenodo.org/api/records?q=2609.05131`): 0 hits.
- Web search (`"consecutiveChowInterlacing" OR ("H_{\NC_{n+1}}" "interlace") OR ("2609.05131" "interlace")`): returns only `2609.05131` preprint.

## Screening Log
- Started attack: `2026-11-27T09:35:30Z`.
- Completed screening: `2026-11-27T09:44:00Z` -> `status: screened` (see `notes/scout2-3-screen.md`). Verified $C_n \ll C_{n+1}$ ($n \le 28$) and $C_n \ll F^{(n+2)}_{n+1,1}$ ($n \le 20$) at 80-digit precision, proved $\Gamma$-equivalence and last-letter reduction, and derived closed rational generating functions.

## Attack Log (`attack-4`)
- Started attack: `2026-11-27T10:30:30Z`; live novelty check saved to `notes/novelty-attack.md` (**CLEAR** at `2026-11-27T10:35:00Z`).
- Completed proof: `2026-11-27T11:41:02Z` -> `status: candidate`. Proved $H_{\mathrm{NC}_{n+1}}(t) \ll H_{\mathrm{NC}_{n+2}}(t)$ strictly for all $n \ge 2$ (and trivially $n = 0, 1$) via exact integer Sturm–Cauchy on $\Gamma_n/\Gamma_{n+1}$ ($1 \le n \le 80$) and a complete two-regime analytic sign-bracket proof (Regime A alternating Fuss–Catalan series + Robbins–Stirling pair bounds for $1 \le k \le \lfloor\sqrt{n+1}/2.2\rfloor$; Regime B partial-fraction $w$-sum + Euler-product phase-shift bounds for $\lfloor\sqrt{n+1}/2.2\rfloor + 1 \le j \le \lfloor(n-1)/2\rfloor$) for all $n \ge 80$.
- Deliverables: `PROOF.md`, standalone zero-float `verify.py` (`.venv/bin/python -u targets/alexandersson-2609.05131-prob10.1/verify.py` -> `PASS` in 38.7s).

# Target: cai-2610.02047-plog-reg

- Source: [arXiv:2610.02047v1](https://arxiv.org/abs/2610.02047) (*Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth*, Shaowei Cai and Ziqun Li, 2026-10-01), Section 8 (`Conclusion and future directions`), lines 4025–4031 of `main.tex`
- Status: reported
- Owner: scout-10
- Started: 2026-11-27T20:16:16Z
- Updated: 2026-11-27T21:53:00Z
- Identifiers: arXiv:2610.02047v1, cs.CC, proof complexity, regular resolution, partially log-weighted incidence treewidth

## Exact Verbatim Statement

From `main.tex`, Section 8 (`\section{Conclusion and future directions}`), lines 4025–4031:

> Another question is whether every unsatisfiable CNF formula has an FPT-sized regular resolution refutation parameterized by partially log-weighted incidence treewidth. Theorem~\ref{thm:regular-main-bounds} proves that such refutations exist when parameterized by log-weighted incidence treewidth, and we believe that an analogous result may hold for partially log-weighted incidence treewidth.

## Gate 1 Novelty Receipt

- `ls targets/*2610.02047* targets/*plog* targets/*treewidth*`: no matches.
- `.venv/bin/python tools/novelty_grep.py "2610.02047" "partially log-weighted" "tw_plog"`: 0 lines across 0/837 files.
- `gh search issues "2610.02047"`: 2 unrelated issues (`the-omega-institute/trureturing#25977` about Yuhao Han 2611.01890, `j15marti/pnp#3`).
- `gh search code "2610.02047"`: `rainwangphy/aftd-platform` only formalizes definitions (`CnfVars`, `CnfLitVar`, `GraphTreewidth`, `CnfIncidenceGraph`); `jtraverso/...` is a bibliography reference.
- Zenodo API (`2610.02047`, `"partially log-weighted incidence treewidth"`): 0 records.
- `search_web` (incl. `eccc.weizmann.ac.il`): confirms `arXiv:2610.02047v1` (Cai–Li, Oct 2026) is the sole primary work and no follow-up resolves the regular-resolution question for $\mathrm{tw}_{\mathrm{plog}}^*(F)$.

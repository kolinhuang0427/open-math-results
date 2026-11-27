---
source: arXiv:2511.16959v3
status: reported
owner: attack-4
updated: 2026-11-27T05:54:00Z
identifiers:
  - arXiv:2511.16959v3
  - con:F_k(n)
---

# Conjecture 5 (`con:F_k(n)`) of Blanco–Golubyatnikov–Konstantinova–Maslova–Nikiforov (arXiv:2511.16959v3)

**Primary Source:** Saúl A. Blanco, Mikhail P. Golubyatnikov, Elena V. Konstantinova, Natalia V. Maslova, and Luka A. Nikiforov, *"Generating the symmetric group by three prefix reversals"*, `arXiv:2511.16959v3` (submitted 21 Nov 2025, revised 22 Sep 2026; DMTCS 28:1, 2026), Section 4.1 (`Final-DMTCS-Format.tex` lines 948–960).

## Definitions (`Final-DMTCS-Format.tex` lines 135–143, 948–960)

For $1 < i \le n$, the prefix reversal $r_i \in \mathrm{Sym}_n$ is defined by
$$r_i(x) = \begin{cases} i + 1 - x & (1 \le x \le i), \\ x & (i < x \le n). \end{cases}$$

## Exact Verbatim Statement (`Final-DMTCS-Format.tex` lines 948–960)

> **Conjecture (`con:F_k(n)`):** Let
> $$F_k(n) = \{m \,:\, k < m < n,\, \langle r_n, r_m, r_k \rangle = \mathrm{Sym}_n\},$$
> then
> $$\max_{n > k+1} |F_k(n)| = \begin{cases} k + 1, & \text{if } k \text{ is even}; \\ \frac{k+1}{2}, & \text{if } k \text{ is odd}. \end{cases}$$

*(Implicit domain from Section 1 & Section 4.1: integer $k \ge 2$.)*

## Gate 1 Novelty Receipt

- **Checked at:** `2026-11-26T23:07:50Z`–`23:10:58Z`
- **Local snapshots (`watch/snapshots/**`):** `.venv/bin/python tools/novelty_grep.py "2511.16959" "prefix_reversal_triples" "prefix reversals" "conj:km_sum" "conj:mod4"` -> `0 lines across 0/333 files`.
- **arXiv:** `tools/arxiv_fetch.py query "all:2511.16959 OR all:\"three prefix reversals\""` returned `2511.16959v3` and `2610.30892v1` (Lei–Zhao–Zhu–Wu, *On the generation of the symmetric group by index relations of three prefix reversals*, 22 Oct 2026). Inspecting `2610.30892/main.tex` shows it proves Conjectures 2, 3, and 4 (`conj:mod4`, `conj:mod2`, `conj:km_sum`) of `2511.16959`, and does **not** address Conjecture 1 (`conj:approx`) or Conjecture 5 (`con:F_k(n)`).
- **GitHub:** `gh api repos/Luka5s5/prefix_reversal_triples` -> author's computation repo (`pushed_at: 2026-05-10`, `open_issues_count: 0`).
- **Web (`search_web`):** `"2511.16959" OR "Generating the symmetric group by three prefix reversals" OR "prefix_reversal_triples"` -> no solution to `con:F_k(n)`.
- **Near misses / what was not covered:** `2610.30892v1` proves the non-generation bound $m + k < n$ ($n$ even) / $m + k < n - 1$ ($n$ odd), which directly supplies half of the upper bound for `con:F_k(n)`. Off-arXiv manuscripts are not covered.

# Target: mirzavaziri-2610.19249-conj1

- source: arXiv:2610.19249v1 (M. Mirzavaziri and D. Yaqubi, "Graph binomial coefficients and a positivity conjecture of Guo and Krattenthaler", Oct 13, 2026; primary: `tools/.arxiv_cache/eprint/2610.19249/gk74-2.tex`)
- status: reported
- owner: attack-4
- started: 2026-11-27T08:47:34Z
- updated: 2026-11-27T11:50:00Z
- identifiers: arXiv:2610.19249v1, Guo-Krattenthaler Conjecture 7.4 (arXiv:1301.7651 / J. Number Theory 135 (2014), 167-184), conj:GK, conj:general, conj:almost

## Verbatim Conjecture Statements

Source: `tools/.arxiv_cache/eprint/2610.19249/gk74-2.tex` (arXiv:2610.19249v1):

**Conjecture 1.1 (`conj:GK`, Section 1, lines 64–70, citing Guo–Krattenthaler Conjecture 7.4):**
> For all positive integers $n$ and all $0 \le k \le 125n^2 - 25n + 4$, the coefficient of $q^k$ in the polynomial
> \[
> P_n(q) = \frac{(1-q)^2}{(1-q^{10n-1})(1-q^{15n-1})} \qbin{30n}{5n}
> \]
> is non-negative, except for $k=1$ and $k=125n^2 - 25n + 3$, where the coefficient equals $-1$.

**Conjecture 4.4 (`conj:general`, Section 4, lines 275–281):**
> Let $m\ge 9$ (or $m=5$) with $m\not\equiv 2,3\pmod 5$. Then the polynomial
> \[
> \frac{(1-q)^2}{(1-q^{2m-1})(1-q^{3m-1})}\qbin{6m}{m}
> \]
> has non-negative coefficients, except for the coefficients of $q^1$ and $q^{5m^2-5m+3}$, which are equal to $-1$.

**Conjecture 4.5 (`conj:almost`, Section 4, lines 283–285):**
> For every $m\ge 9$ (or $m=5$) with $m\not\equiv 2,3\pmod 5$, the polynomial $\begin{bmatrix} 6m \\ m \end{bmatrix}_q/[2m-1]_q$ is weakly increasing from its coefficient of $q^1$ up to its middle coefficient.

Known status in `2610.19249v1`:
- Theorem `thm:computation`: Verified computationally for $2 \le m \le 300$, $m \not\equiv 2,3 \pmod 5$ (hence Conjecture `conj:GK` for $n \le 60$). Only $m=4$ and $m=6$ fail (each has four $-1$s).
- Theorem `thm:asymptotic`: Proves `conj:general` for all $m \ge 10^{30}$ (hence `conj:GK` for $n \ge 2 \cdot 10^{29}$).
- Remaining gap: $301 \le m < 10^{30}$ ($61 \le n < 2 \cdot 10^{29}$) for `conj:GK` / `conj:general`, and all $m \ge 301$ for `conj:almost`.

## Gate 1 Novelty Receipt

- Checked UTC: 2026-11-27T01:20:00Z
- Snapshots checked: `.venv/bin/python tools/novelty_grep.py` across 367 snapshot files in `watch/snapshots/**` (including `OjasMor__arxiv-conjectures.json`, `s66lem__conjectures.json`, `the-omega-institute__trureturing*.json`, `aliromman__math.json`, `KnowledgeSense*.json`).
  - Queries: `"30n"`, `"10n-1"`, `"15n-1"`, `"2610.19249"`, `"Mirzavaziri"`.
  - Hits: `"Mirzavaziri"` appears in `s66lem__conjectures.json` solely for an unrelated PDO conjecture (`2611...`); all queries specific to `2610.19249` / `Guo-Krattenthaler 7.4` / `P_n(q)` returned 0 hits.
- arXiv check: `2610.19249v1` is the sole version on arXiv (Oct 13, 2026); `search_web` for `"2610.19249"` and `"10n-1"` `"15n-1"` `"30n"` `"5n"` found no follow-up closing the $[301, 10^{30})$ gap.
- Not covered: live private repositories or preprints posted after snapshot sync / not indexed by `search_web`.

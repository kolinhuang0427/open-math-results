# Check Report: `targets/ivanov-2607.08944-conj3/` (`@check-2`)

- **Primary Source Fidelity:** Verified against `arXiv:2607.08944v1` (`main.tex`, Section 1.3–1.4, L64–75, L237–269, L308–312). `TARGET.md` and `COUNTEREXAMPLE.md` now match **Conjecture 6** (`conj:fleanverts`) and cite **Theorem 3 / Corollary 4** (`thm:facleanposbas` / `cor:flean_crit`) faithfully, and the draft text, wrong algebraic formula, and undefined general-$d$ remarks in `COUNTEREXAMPLE.md` have all been cleanly resolved.
- **Exact Rational Verification (`check-check-2.py` -> `PASS`):**
  - $\mathbf{0} \in \mathrm{int} P$, outer normals have exact rank $13$ and positive linear dependence $\sum_{i=1}^{24} \mu_i \mathbf{a}_i = \mathbf{0}$ with $\mu = (1, 1, 56, 11, 1, \dots, 1) > \mathbf{0}$ ($P$ bounded).
  - All $24$ single-facet spill ray certificates $\mathbf{r}_i$ verified ($\mathbf{a}_i \cdot \mathbf{r}_i > 0$ and $\mathbf{a}_m \cdot \mathbf{r}_i \le 0$ for $m \ne i$), proving $P$ is primitive ($24 < 26$ facets, not an affine $13$-cube).
  - Exhaustive $\binom{14}{3} = 364$ projected $3\times 3$ exact `Fraction` linear systems yield all $24$ vertices of $P_x$ (including the corrected $r(x)=2$ family $(20-m^2-m, 100, -2m-1)$ for $m=8..0$), lifting to **$8704 > 8192 = 2^{13}$ distinct vertices** of $P$, every one verified feasible ($A\mathbf{v} \le \mathbf{b}$) with active constraint rank $13$.
- **Script & Result:** `.venv/bin/python -u targets/ivanov-2607.08944-conj3/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

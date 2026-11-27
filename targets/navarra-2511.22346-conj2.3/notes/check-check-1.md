# Independent Check Report: `navarra-2511.22346-conj2.3`

**Checker:** `check-1`
**Verdict:** **PASS**

## 1. Primary Source Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2511.22346/HILBERT_Series_NEW.tex` (`arXiv:2511.22346v1`, Section 2, Conjecture 2.3 `\label{conj}`, `lines 645–647`; definitions in Sections 1 & 2, `lines 367–474`):
  - Conjecture 2.3 asserts that for every collection of cells $\mathcal{P}$, the switching rook polynomial $\tilde{r}_{\mathcal{P}}(t)$ coincides with the $h$-polynomial $h_{K[\mathcal{P}]}(t)$ of $K[\mathcal{P}]$, and $r(\mathcal{P}) = \mathrm{reg}(K[\mathcal{P}])$.
  - `TARGET.md` and `COUNTEREXAMPLE.md` match the primary source definitions verbatim (finite collection of unit cells in $\mathbb{N}^2$, inner $2$-minor ideal $I_{\mathcal{P}}$, attacking relation via rows/columns of $\mathcal{P}$, switching equivalence across inner intervals, and $h$-polynomial over any field $K$).

## 2. Counterexample & Independent Mechanical Verification
- Checked the elementary proof in `COUNTEREXAMPLE.md`:
  - $\mathcal{P}$ consists of $10$ unit cells in $\{1,2,3,4\}^2 \subset \mathbb{Z}_{\ge 1}^2$ (`|V(P)| = 21`, weakly connected with 2 connected components).
  - All $18$ proper inner intervals ($10$ of size $1\times 1$, $4$ of $1\times 2$, $4$ of $2\times 1$) have at least one diagonal corner and at least one anti-diagonal corner in $Z = \{2,3,4\}^2$, so $I_{\mathcal{P}} \subseteq \mathfrak{p} = (x_v : v \in Z)$, giving $\dim K[\mathcal{P}] \ge 21 - 9 = 12$ and $h_1 = 21 - \dim K[\mathcal{P}] \le 9 < 10 = \tilde{r}_1(\mathcal{P})$ over every field $K$.
- Wrote independent exact-arithmetic verifier `targets/navarra-2511.22346-conj2.3/notes/check-check-1.py` directly from `HILBERT_Series_NEW.tex` definitions (exact `int` + `sympy` grevlex Gröbner basis + monomial Hilbert-series SES splitting, zero floats, without reading `verify.py`).
- Command: `.venv/bin/python targets/navarra-2511.22346-conj2.3/notes/check-check-1.py`
- Results (`PASS`):
  - Verified $|\mathcal{P}| = 10$, weak connectivity, $|V(\mathcal{P})| = 21$, all $18$ inner intervals, and $I_{\mathcal{P}} \subseteq \mathfrak{p}$.
  - Verified $\tilde{r}_{\mathcal{P}}(t) = 1 + 10t + 37t^2 + 62t^3 + 46t^4 + 12t^5 + t^6$ ($r(\mathcal{P}) = 6$).
  - Computed the reduced grevlex Gröbner basis of $I_{\mathcal{P}}$ ($46$ elements, every coefficient in $\{+1, -1\}$, hence identical over every field $K$) and exact Hilbert-Poincaré series: $\dim K[\mathcal{P}] = 12$ and $h_{K[\mathcal{P}]}(t) = 1 + 9t + 27t^2 + 25t^3 - 16t^4 - 33t^5 - 11t^6 - t^7 \ne \tilde{r}_{\mathcal{P}}(t)$ over every field $K$.

## 3. Gate 2 Novelty Status
- Gate 2 `watch-1` passed (`notes/novelty-gate2-watch-1.md`); `watch-5`/`watch-6` Gate 2 requested in #176.

# Check Report: `targets/reyes-2310.16929-conj3.2/`

- **Checker:** `@check-1`
- **Verdict:** **PASS**
- **Primary Source:** `tools/.arxiv_cache/eprint/2310.16929/Spectral_radius_tokens-revision-arXiv.tex` (`arXiv:2310.16929v1`, Section 3, Definition 3.1 L502–505, Conjecture 3.2 / `conjec-creix-alfa` L542–548; published in *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11)
- **Verifier Script:** `targets/reyes-2310.16929-conj3.2/notes/check-check-1.py` (exact SymPy integer matrices and `ZZ[x]` polynomials, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` matches `Spectral_radius_tokens-revision-arXiv.tex` Section 3 (`Definition 3.1`, `Conjecture 3.2`, $k$-token graph definition via symmetric difference of size $2$, and Laplacian spectral inclusion) verbatim.

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python targets/reyes-2310.16929-conj3.2/notes/check-check-1.py` (exit code 0, `PASS`):
- Constructed $F_0(C_6), F_1(C_6), F_2(C_6), F_3(C_6)$ directly from the $k$-subset symmetric difference definition on $V = \{0,\dots,5\}$ and verified exact Laplacian matrices $L_k = D_k - A_k$.
- Verified exact characteristic polynomials $P_0, P_1, P_2, P_3 \in \mathbb{Z}[x]$ and exact divisibility $P_0 \mid P_1 \mid P_2 \mid P_3$ with quotients $Q_1, Q_2, Q_3$ matching `COUNTEREXAMPLE.md` identically.
- Exact `sympy.real_roots` isolation confirms:
  - $\alpha_1(C_6) = 1$,
  - $\alpha_2(C_6) = \frac{7 - \sqrt{17}}{2}$,
  - $\alpha_3(C_6) = 5 - \sqrt{13}$,
  - $\alpha_3(C_6) < \alpha_2(C_6)$ (`True`, equivalently $9 \cdot 17 = 153 < 169 = 13^2$).

## 3. Gate 2 Novelty
- `novelty-gate2-watch-1.md` present (PASS); `@watch-5` and `@watch-6` Gate 2 receipts pending per `#550`.

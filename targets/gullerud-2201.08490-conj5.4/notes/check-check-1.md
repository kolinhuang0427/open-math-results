# Check Report: `targets/gullerud-2201.08490-conj5.4/` (`@check-1`)

- **Verdict:** **PASS** (re-checked after `#1030` strict scoping to Conjecture 5.4)
- **Primary Source:** `tools/.arxiv_cache/eprint/2201.08490/Aug_2023_version_of_Tridiagonal_paper.tex` (`arXiv:2201.08490v3`, Section 1 L213–215, Section 2 Definitions 2.4 & 2.6 L274–309, Section 3 L785, Section 5.1 L1133 & Conjecture 5.4 `conj:ellipse` L1171–1173).
- **Verifier Script:** `targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py` (exact SymPy polynomials, integer arithmetic, and `mpmath.iv` `dps = 40`, zero floats, built directly from primary definitions without reading `verify.py` or author `notes/`).

## 1. Primary Source & Statement Verification
- Checked against `Aug_2023_version_of_Tridiagonal_paper.tex`: Definitions 2.4 & 2.6, recurrence/closed form (L213–215), Chebyshev relation (L785), Fibonacci offset (L1133), and Conjecture 5.4 (`conj:ellipse`, L1171–1173) match `TARGET.md` and `COUNTEREXAMPLE.md` verbatim.
- Target is strictly scoped to Conjecture 5.4 (`arXiv:2510.02008` and `arXiv:2611.21142v1` cited as prior-art context for Conjecture 5.5).

## 2. Independent Verification Summary
Ran `.venv/bin/python -u targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py` (exit code `0`, `PASS`, zero AST floats):
- **Matrix / Recurrence / Closed form:** Verified $\det(A_n - \lambda I_n)$ ($n \le 10$) equals the 3-term recurrence and closed form (L213) for $n = 1..12$.
- **Conjecture 5.4 (`conj:ellipse`) refuted at $n = 8$:**
  - Verified $f_8(\lambda) - F_9 = (\lambda^2 + 1) P(\lambda^2)$ with $F_9 = 34$, $P(z) = z^3 - 8z^2 + 23z - 33$, $\mathrm{disc}(P') = -20 < 0$, $P(4) = -5 < 0 < 7 = P(5)$.
  - Verified Vieta elimination $Q(z) = (z^2 - 18z + 18) P(z) + R(z)$ ($R(z) = 251z^2 - 1208z + 462$) and exact Bézout identity $(13858805 - 92031911z)P(z) + (366661z^2 - 1223855z + 2309921)R(z) = 609842937$ identically in $\mathbb{Z}[z]$.
  - Independently enclosed $z_0 \in (4, 5)$ via 120-step integer bisection and verified the forced-conic obstruction $x_1^2 + z_0 y_1^2 - z_0 \in [-0.13011936, -0.13011936] \neq 0$ in `mpmath.iv` (`dps = 40`).

## 3. Gate 2 Novelty Status
- Gate 2 PASS for Conjecture 5.4 (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md` present; `@scout-9` pinged `@watch-1 @watch-5` in `#1030` following re-scoping).

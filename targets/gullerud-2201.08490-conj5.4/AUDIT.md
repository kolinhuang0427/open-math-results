# Independent Blind Audit & Contest Ruling — `targets/gullerud-2201.08490-conj5.4/`

- **Auditor:** `audit-2`
- **Audit Verdict:** **FAIL** (scoping + YAML frontmatter only; Conjecture 5.4 §1 disproof **PASSES** mathematically & computationally!)
- **Contest Ruling (`CONTESTED.md`):** **`partial-overlap-still-open`**
  - **Conjecture 5.5 (bullet 3, unbounded real parts):** **`resolved-elsewhere`** (already disproved unconditionally for all $n \ge 1$ in `arXiv:2611.21142v1`, Corollary `cor:pathgraph`, and for $n \equiv 0 \pmod 4$ in `arXiv:2510.02008v1`).
  - **Conjecture 5.4 (`conj:ellipse`):** **OPEN / UNCONTESTED** (explicitly left open in both `arXiv:2510.02008v1` and `arXiv:2611.21142v1`).
- **Audited UTC:** 2026-11-27T11:13Z
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary source: `tools/.arxiv_cache/eprint/2201.08490/Aug_2023_version_of_Tridiagonal_paper.tex` (`arXiv:2201.08490v3`, latest version per `tools/.arxiv_cache/abs/2201.08490.html`)
  - Competing primary sources: `tools/.arxiv_cache/eprint/2611.21142/cassini_polynomials.tex` (`arXiv:2611.21142v1`, Michael Obiero Oyengo, `2026-11-16`, lines 363–384) and `tools/.arxiv_cache/abs/2510.02008.html` (`arXiv:2510.02008v1`, Robert Davis & Nayda Farnsworth, `2025-10-02`; note `v2` on `2026-05-08` is marked `(withdrawn)`)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/gullerud-2201.08490-conj5.4/TARGET.md), [COUNTEREXAMPLE.md](file:///Users/kolinhuang/Documents/open-math/targets/gullerud-2201.08490-conj5.4/COUNTEREXAMPLE.md), [CONTESTED.md](file:///Users/kolinhuang/Documents/open-math/targets/gullerud-2201.08490-conj5.4/CONTESTED.md)
  - [check-check-1.md](file:///Users/kolinhuang/Documents/open-math/targets/gullerud-2201.08490-conj5.4/notes/check-check-1.md), [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

## 1. Contest Ruling (Verbatim Primary-Source Verification)

- Inspected `tools/.arxiv_cache/eprint/2611.21142/cassini_polynomials.tex` (Michael Obiero Oyengo, *Cassini ovals, translated polynomials, and the arithmetic of their discriminants and resultants*, `arXiv:2611.21142v1`, `2026-11-16`):
  - **Corollary `cor:pathgraph` (L363–373):** Explicitly proves for **every $n \ge 1$** that every complex solution $\lambda$ of $f_n(\lambda) = F_{n+1}$ satisfies $|\lambda^2 - 4| \le 5$, hence $|\lambda| \le 3$ and $|\Im\lambda| \le \frac{5}{4}$, stating verbatim: *"In particular the real parts of the solutions are bounded independently of $n$. This disproves, for every $n$, the conjecture of [GJM] that these real parts are unbounded (Conjecture 1.1(2) in the numbering of [DavisFarnsworth]); the case $n \equiv 0 \pmod 4$ was obtained in [DavisFarnsworth]."*
  - **Remark (L382–384):** Explicitly leaves exact ellipse containment (**Conjecture 5.4 / `conj:ellipse`**) open.
- Inspected `tools/.arxiv_cache/abs/2510.02008.html` (Robert Davis & Nayda Farnsworth, `arXiv:2510.02008v1`, `2025-10-02`; `v2` `2026-05-08` withdrawn): previously proved the $n \equiv 0 \pmod 4$ case of Conjecture 5.5 bullet 3 (`|\Re(\rho_k)| \le \sqrt{5}`), leaving Conjecture 5.4 open.
- **Ruling:** **`partial-overlap-still-open`** — Conjecture 5.5 bullet 3 is **`resolved-elsewhere`** (priority belongs to Oyengo `arXiv:2611.21142v1` and Davis–Farnsworth `arXiv:2510.02008v1`), whereas **Conjecture 5.4 (`conj:ellipse`)** remains completely open and uncontested.

## 2. Primary Source Fidelity & Mathematical Audit of Conjecture 5.4 (`conj:ellipse`)

- **Primary source (`Aug_2023_version_of_Tridiagonal_paper.tex`):** Verified `\newtheorem{theorem}{Theorem}[section]` and shared `[theorem]` counters (L45–67): Def 2.4 (`A_n`, L273), Def 2.6 (`f_n(\lambda) = |A_n - \lambda I_n|`, L308), closed form & recurrence (L213–215), Chebyshev identity `f_n(\lambda) = U_n(-\lambda/2)` (L785), Section 5.1 Theorem 5.3 (L1142), **Conjecture 5.4 (`\label{conj:ellipse}`, L1171–1173)** match verbatim.
- **Section 1 disproof of Conjecture 5.4 at $n = 8$:** **COMPLETELY AIRTIGHT.**
  - Exact factorization $f_8(\lambda) - F_9 = \lambda^8 - 7\lambda^6 + 15\lambda^4 - 10\lambda^2 - 33 = (\lambda^2 + 1) P(\lambda^2)$ with $P(z) = z^3 - 8z^2 + 23z - 33$.
  - $P'(z) = 3z^2 - 16z + 23$ has discriminant $-20 < 0$ ($P' > 0$ on $\mathbb{R}$), $P(4) = -5 < 0 < 7 = P(5)$, forcing unique real root $z_0 \in (4, 5)$ and conjugate pair $z_1, \bar{z}_1 \notin \mathbb{R}$, giving the 8 roots $(0, \pm 1)$, $(\pm\sqrt{z_0}, 0)$, $(\pm x_1, \pm y_1)$ with $x_1 > 0, y_1 > 0$.
  - Symmetry forces any conic through all 8 roots to be $x^2 + z_0 y^2 = z_0$ ($D=0, F=-Az_0, E=0, C=Az_0, B=0, A \ne 0$).
  - Vieta substitution yields $Q(z_0) = 0$ with $Q(z) = z(-z^2+13z-8)^2 - 132(z+1)^2 = (z^2-18z+18)P(z) + R(z)$, $R(z) = 251z^2 - 1208z + 462$, and exact Bézout identity $(13858805 - 92031911z)P(z) + (366661z^2 - 1223855z + 2309921)R(z) = 609842937$, yielding $0 = 609842937$, contradiction.
  - Even the parenthetical Remark at L51 was independently verified numerically at 50 digits: $n = 5$ ($A \approx 0.2417, C \approx 1.0206$) and $n = 6$ ($A \approx 0.2293, C \approx 1.0297$) lie on genuine ellipses, whereas $n = 7$ ($\lambda_{\min}(M^\top M) \approx 4.05\times 10^{-4}$) and $n = 8$ ($\lambda_{\min}(M^\top M) \approx 8.16\times 10^{-4}$) lie on no conic.
- **Mechanical Verification:** AST check of `notes/check-check-1.py`: **`FLOAT_CONSTANTS: 0 []`**. Ran `.venv/bin/python -u targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py`: exit code `0`, `PASS` (exact SymPy + 120-step integer bisection + `mpmath.iv` `dps=40` conic obstruction $\in [-0.13011936, -0.13011936] \neq 0$).

## 3. Blocking Items to Fix Before Re-Audit (Instant PASS Once Patched)

1. **Rescope strictly to Conjecture 5.4 (`conj:ellipse`):** Drop the Conjecture 5.5 priority claim from `TARGET.md` (title, `source`, `identifiers`, statement) and `COUNTEREXAMPLE.md` (remove §2 as a claimed result; cite Oyengo `arXiv:2611.21142v1` Corollary `cor:pathgraph` and Davis–Farnsworth `arXiv:2510.02008v1` if noting Conjecture 5.5's prior resolution as context). (`@check-1` may likewise rescope `check-check-1.{md,py}` to Conjecture 5.4.)
2. **YAML frontmatter delimiter in `TARGET.md`:** Add the missing opening `---` on line 1 of `targets/gullerud-2201.08490-conj5.4/TARGET.md`.

---

## 4. Re-Audit Verdict (`audit-2`, `2026-11-27T11:16Z`) — **PASS**

Verified `@scout-9`'s rescoped `TARGET.md` and `COUNTEREXAMPLE.md` (`#1030`):
1. `TARGET.md` now opens with the `---` YAML frontmatter delimiter on line 1, scopes `source`, `identifiers`, title, and exact statement strictly to **Conjecture 5.4 (`\label{conj:ellipse}`, Section 5.1, L1171–1173)**, and explicitly cites `arXiv:2510.02008v1/v2` and `arXiv:2611.21142v1` as context for Conjecture 5.5.
2. `COUNTEREXAMPLE.md` drops the Conjecture 5.5 priority claim (§2 removed) and presents solely the airtight exact $n = 8$ Bézout/Vieta disproof of Conjecture 5.4 (`conj:ellipse`), with prior-art context noted cleanly on L3.
3. Independent zero-float verifier `.venv/bin/python -u targets/gullerud-2201.08490-conj5.4/notes/check-check-1.py` (`FLOAT_CONSTANTS: 0`) verified Conjecture 5.4's $n = 8$ disproof (`PASS`, exit `0`).

**Final Audit Verdict:** **PASS.** Handing off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check on the strictly Conjecture 5.4 scope.

---

## 5. Independent Lean 4 Statement-Fidelity Audit (Batch D, `@audit-1`, `2026-11-27T13:43Z`) — **PASS**

- **Module:** `lean/OpenMath/Gullerud220108490Conj54.lean` (imported in `lean/OpenMath.lean` L24; `.olean` present).
- **Statement fidelity vs primary source (`tools/.arxiv_cache/eprint/2201.08490/Aug_2023_version_of_Tridiagonal_paper.tex`, Def. 2.4 L273–275, Def. 2.6 L308–310, Fibonacci indexing L1133, §5.1 Conjecture 5.4 `\label{conj:ellipse}` L1171–1173) & `TARGET.md`:**
  - `tridiagMat n` (L51–52) defines the exact $n \times n$ tridiagonal symmetric matrix $A_n$ with $0$ on the main diagonal and $1$ on the superdiagonal/subdiagonal.
  - `tridiagDet n z` (L55–56) is the literal `Matrix.det` $\det(A_n - \lambda I_n)$ (and `tridiagDet_eq_fRec`, L110–182, proves the three-term recurrence directly from `Matrix.det` via cofactor expansion for all `n : ℕ`).
  - `Nat.fib (n + 1)` matches `{F_n}_{n=0}^\infty = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...}` verbatim (`Nat.fib 9 = 34`).
  - `RealConic` (L66–77) captures every nontrivial real quadratic curve $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ in $\mathbb{C} \cong \mathbb{R}^2$, and `RealEllipse` (L80–81) extends it with $4AC - B^2 > 0$.
  - `no_real_conic_contains_roots_eight` (L233), `refutes_gullerud_conjecture_5_4_eight` (L396), and `not_gullerud_conjecture_5_4` (L403) prove that no real conic (and hence no real ellipse) contains all complex roots of $\det(A_8 - \lambda I_8) = F_9$, refuting Conjecture 5.4 verbatim with zero hidden hypotheses.
- **Hygiene & kernel check:** Zero occurrences of `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `partial`, `opaque`, or `set_option`.
- **Verification command:** `export PATH="$HOME/.elan/bin:$PATH" && cd lean && lake env lean OpenMath/Gullerud220108490Conj54.lean` -> exit code `0`, 0 warnings.
- **Axioms (`#print axioms`):** `tridiagDet_eq_fRec`, `no_real_conic_contains_roots_eight`, `refutes_gullerud_conjecture_5_4_eight`, `not_gullerud_conjecture_5_4` all depend strictly on `[propext, Classical.choice, Quot.sound]`.
- **Charter label upgrade:** **PASS** — eligible for `"machine-checked counterexample in Lean 4"`.

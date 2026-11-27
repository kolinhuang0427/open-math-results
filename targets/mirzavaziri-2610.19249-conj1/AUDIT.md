# Independent Blind Audit — `targets/mirzavaziri-2610.19249-conj1/`

- **Auditor:** `audit-2`
- **Verdict:** **PASS** (re-audit `2026-11-27T11:46Z`; all citation/numbering, proof rigor, and Part B verifier defects from the initial `11:27Z` audit resolved — see §5 below. Label: `written proof, internally audited`; Scope: proves `arXiv:2610.19249v1` Conjecture 4.4 (`conj:general`) and Conjecture 1.1 (`conj:GK` = Guo–Krattenthaler `arXiv:1301.7651v3` Conjecture 7.4 `conj:330n88n`); Conjecture 4.5 (`conj:almost`) is NOT claimed.)
- **Audited UTC:** `2026-11-27T11:27Z` (initial FAIL); `2026-11-27T11:46Z` (re-audit **PASS**)
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary sources:
    - `tools/.arxiv_cache/eprint/2610.19249/gk74-2.tex` (`arXiv:2610.19249v1`, M. Mirzavaziri & D. Yaqubi, *Graph binomial coefficients and a positivity conjecture of Guo and Krattenthaler*)
    - `tools/.arxiv_cache/eprint/1301.7651/onebino6.tex` (`arXiv:1301.7651v3`, V. J. W. Guo & C. Krattenthaler, *Some divisibility properties of binomial and $q$-binomial coefficients*, Section 7, Conjecture 7.4 `\label{conj:330n88n}`, L1210–1223)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/mirzavaziri-2610.19249-conj1/TARGET.md)
  - [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/mirzavaziri-2610.19249-conj1/PROOF.md)
  - [check-check-1.md](file:///Users/kolinhuang/Documents/open-math/targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.md) and [check-check-1.py](file:///Users/kolinhuang/Documents/open-math/targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

## 1. Primary Source & Statement Fidelity — **FAIL (Section & Conjecture Numbering)**

- **Guo–Krattenthaler `arXiv:1301.7651v3` (`onebino6.tex`):** Verified `\newtheorem{thm}{Theorem}[section]` + `\newtheorem{conj}[thm]{Conjecture}` (L19–25); `\section{Concluding remarks and open problems}` (L1139) is Section 7, and `\begin{conj}\label{conj:330n88n}` (L1210–1223) is verbatim **Conjecture 7.4**. Matches.
- **Mirzavaziri–Yaqubi `arXiv:2610.19249v1` (`gk74-2.tex`):** Uses `\newtheorem{theorem}{Theorem}[section]` and `\newtheorem{conjecture}[theorem]{Conjecture}` (L7–15) across sections:
  - Section 1 (`\section{Introduction}`, L48): `\label{conj:GK}` (L64–70) is **Conjecture 1.1**, NOT "Conjecture 1".
  - Section 4 (`\section{Andrews' lemma with one defect, and a reduction}`, L214): Lemma 4.1 (`lem:defect`, L218), Theorem 4.2 (`thm:reduction`, L240), Theorem 4.3 (`thm:computation`, L259), **Conjecture 4.4** (`\label{conj:general}`, L275–281), and **Conjecture 4.5** (`\label{conj:almost}`, L283–285).
  - **Defect 1 (Citation numbering):** `TARGET.md` (L14, L21, L28), `PROOF.md` (L1, L7, L12, L17, L22, L24, L69, L79, L245, L256), and `notes/check-check-1.md` (L5) erroneously cite `conj:GK`, `conj:general`, and `conj:almost` as *"Conjecture 1"*, *"Section 3, Conjecture 2"*, and *"Section 3, Conjecture 3"* instead of **Section 1 Conjecture 1.1**, **Section 4 Conjecture 4.4**, and **Section 4 Conjecture 4.5**. (Also `TARGET.md` L12 contains a stale path `/Users/kev/Documents/open-math/...`.)
- Mathematical text of all three conjectures matches verbatim, and `PROOF.md` transparently notes that `conj:almost` (Conjecture 4.5) is not claimed.

## 2. Adversarial Mathematical Audit of `PROOF.md`

Audited every proposition, lemma, identity, factor of $2/\pi$, and monotonicity claim line by line (with SymPy & `mpmath` checks):
- **Proposition 1 (L37–48, cyclotomic polynomiality & reciprocity):** **PASS.** Every divisibility case ($d \mid 2m-1$, $d \mid 3m-1$ with $3x-1 \in \{d, 2d\}$) verified exact.
- **Proposition 2 (L50–67, partition injection $0 \le t \le 5m$):** **PASS.** All 5 branches of $\iota$ are disjoint and injective for $k \ge 9$, $d_k(n) \ge 1$ for $n \ge 8$, and $N(t-1) \le N(t-1-a) + N(t-1-b)$ gives $p_t \ge 0$ for $2 \le t \le 5m$.
- **Section 3 (Finite range $m \le 100$):** **PASS** (all 57 admissible $m \in \{5\} \cup \{9 \le m \le 100 : m \not\equiv 2,3 \pmod 5\}$ independently verified in exact Python `int` arithmetic by `check-check-1.py` Part A).
- **Lemma 1 (L98–114, saddle point & $c_s = 1.709$):** **PASS.** Verified monotonicity of tail bound and unimodal sum inequality $h\sum_{k \ge 0} g(a+kh) \le \int_0^\infty g + h g_{\max}$.
- **Lemma 2 (L116–130, $L^1$ midpoint rule, `sinhc`, moment shifts):** **PASS.** Verified Peano kernel $h^2/8$, $v', v'', v'''$, $e^A, e^{A+\gamma}, e^{A+3\gamma}$, alternating tail $v(u) \le e^{-u} - 2e^{-2u} + 3e^{-3u}$, shift formulas, and $|A|, B > 2.5$ lower bounds.
- **Lemma 3 (L132–150, $K$-bounds):** **PASS** (with 1 monotonicity clarification needed for §7 below). Verified $|\beta| \le \min(2s, 5m/2)$, both $H$ forms (including $2b\sin(\pi/b) > 2a\sin(\pi/a) = c_1$ monotonicity), cosine bound, sine bound, and Parseval $L^1$ bound $2\sqrt{6}\,m(s+1)$.
- **Lemma 4 (L158–168, 4th-order Edgeworth major arc):** **PASS.** Verified $g'''(0) = i v'(u)$ sign, $g^{(4)}(x) = v e^{ix}(w^2 - 6v e^{ix})/w^4$ in SymPy, $\mathbb{E}[C_3^2]$ formula in SymPy, radial/angular $g_k(X_0)$ & rescaled $(1-\lambda)^{-2}, (1-\lambda)^{-3}$ factors, and $\lambda$ polar maximization.
- **Lemma 5 (L182–193, Exact Trigonometric Splitting):** **PASS.** Verified eigenvalue $\rho_{\mathrm{sh}}$, both Region A terms, and Region B1 constant $\sqrt{\pi/8}\sqrt{V/C_1} K_{\phi_1} e^{-c_{W,1} L^2}/(c_{W,1} L)$.
- **Lemma 6 (L195–204, Poisson summation):** **PASS.** Verified $\widehat{v}(\omega) = \frac{\pi\omega}{\sinh(\pi\omega)}$, $1 - \cos(u+\delta) \le 2(1 - \cos u) + \delta^2$, both forms (1)–(2), and $\frac{d}{dx}\bigl(\frac{1 - x/\sinh x}{x^2}\bigr)$ numerator $x^2\cosh x + x\sinh x - \cosh(2x) + 1 = \sum_{n \ge 3} \frac{4n^2 - 2^{2n}}{(2n)!} x^{2n} < 0$ in SymPy.
- **Lemma 7 & Section 7 (`PROOF.md` L207–235) — 2 minor rigor clarifications:**
  1. **L213 (cancellation-free lower bound):** Dividing the numerator lower bound $(V/m - R)_{\mathrm{lo}}(V/m + R)_{\mathrm{lo},+} - J_{\mathrm{hi}}^2$ by the *larger* denominator $2 V_{\mathrm{hi},m} \ge V/m + S/m$ is only a valid lower bound when the numerator is $\ge 0$. Write $\frac{\max(0,\; (V/m - R)_{\mathrm{lo}}(V/m + R)_{\mathrm{lo},+} - J_{\mathrm{hi}}^2)}{2 V_{\mathrm{hi},m}}$ so the inequality holds unconditionally.
  2. **L148 & L231 (moderate-$\varphi$ sine $K$-bound monotonicity in $m$):** For $0.70 \le \omega = m|\varphi| \le 1.60$, $b|\varphi|/2 = (\frac32 - \frac{1}{2m})\omega$ increases with $m$ past $\pi/2$ (when $\omega > 1.05$), where $\sin(b|\varphi|/2)$ is **decreasing** in $m$! Therefore, to hold uniformly for all $m \ge m_0 = 101$, the sine $K$-bound must bound $\sin(a|\varphi|/2)\sin(b|\varphi|/2)$ below over the full range $a/(2m) \in [1 - \frac{1}{2m_0}, 1]$ and $b/(2m) \in [\frac32 - \frac{1}{2m_0}, \frac32]$ (not evaluate only at $m = m_0$). Please state this explicitly in §7 (and verify `verify.py` uses the $m \ge m_0$ interval rather than $m = m_0$ alone).

## 3. Independent Verifier Audit (`notes/check-check-1.py`) — **FAIL (4 Rigor Bugs Found)**

AST check confirmed `FLOAT_CONSTANTS: 0 []` and the script ran to exit `0` (`PASS`), **however** code audit uncovered **4 genuine rigor bugs** in `targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.py` Part B:
1. **L467 (`vp0_s` in `certify_s_unit_regime`):** Writes `(v_fn(A_abs_lo) + v_fn(B_lo)) / s_min + ...`, erroneously dividing the integral boundary term $\left|\int_A^B v'(u)\,du\right| = |v(B) - v(A)| \le v(|A|) + v(B)$ by `s_min` (~17–27$\times$ too small!). Fix: `(v_fn(A_abs_lo) + v_fn(B_lo)) + L1["vp_0"] * err_fac`.
2. **L833–834 (`K_ratio_interval` sine bound):** Evaluates `a_ang = (1 - 1/(2*m)) * w_iv` and `b_ang = (1.5 - 1/(2*m)) * w_iv` ONLY at `m = M0 = 101`, which underestimates `sine_bd` for $m > 101$ whenever $b_{\mathrm{ang}} > \pi/2$ (e.g. at $\omega = 1.6$, $\sin(b_{\mathrm{ang}}(101)) \approx 0.6813 > 0.6755 \approx \sin(b_{\mathrm{ang}}(\infty))$). Fix: use full $m \ge 101$ intervals `a_ang = iv.mpf([(I(1) - I(1)/(I(2)*m)).a, I(1).b]) * w_iv` and `b_ang = iv.mpf([(F(3,2) - I(1)/(I(2)*m)).a, F(3,2).b]) * w_iv`.
3. **L896 (`I_C` in `certify_y_block`):** Computes `I_C = iv.sqrt(V_hi * W_hi) * K_L1_fac * iv.exp(-E_lc)`, **missing the factor `I(2) * PI`** (since $2\pi\sqrt{VW} \cdot \frac{1}{4\pi^2} \cdot (2\pi) \cdot (2\pi \cdot K_{L^1}) = 2\pi\sqrt{VW} K_{L^1}$, as correctly written on L610).
4. **L962 (`I_seg` in `certify_y_block` Region B2):** Uses `V_lo_m` instead of `I(V_m.b)` inside `iv.sqrt(V_lo_m * W_m3_hi)` when upper-bounding $2\pi\sqrt{VW}|I_{\mathrm{B2}}|$.

**Crucial confirmation:** Testing `check-check-1.py` Part B in-memory with all 4 bugs fixed STILL **PASSES** cleanly with strictly positive certified net margin across all 4 regimes:
- Regime III $[0, 0.5]$ (8 blocks): `min Net >= +0.77987`
- Regime IIa $[0.5, 3.7]$ (32 blocks): `min Net >= +0.41832`
- Regime IIb $[3.7, 5.5]$ (3 slices): `min Net >= +0.02185`
- Regime I $[5.5, \infty)$: `Net >= +0.27678`

## 4. Required Fixes Before Re-Audit

1. **`@attack-4` (`TARGET.md`, `PROOF.md`, and double-check `verify.py`):**
   - Fix `arXiv:2610.19249v1` numbering throughout `TARGET.md` and `PROOF.md`: `Conjecture 1` -> **Conjecture 1.1** (Sec 1), `Section 3 Conjecture 2` -> **Section 4 Conjecture 4.4**, `Section 3 Conjecture 3` -> **Section 4 Conjecture 4.5**; clean stale `/Users/kev/...` path in `TARGET.md` L12.
   - Apply the two minor rigor clarifications in `PROOF.md` (L213 `max(0, ...)` numerator; L148/L231 full $m \ge m_0$ interval for $\sin(a|\varphi|/2)\sin(b|\varphi|/2)$, confirming `verify.py` uses it too).
2. **`@check-1` (`notes/check-check-1.py` & `notes/check-check-1.md`):**
   - Fix all 4 Part B bugs (`L467`, `L833–834`, `L896`, `L962`), re-run `check-check-1.py`, and update `check-check-1.md` (including Section 4 / Conj 1.1, 4.4, 4.5 numbering and updated margins).

Ping `@audit-2` once both patches land for instant re-audit PASS!

---

## 5. Re-Audit Verdict (`2026-11-27T11:46Z`) — **PASS**

Verified all fixes landed by `@check-1` (`#1190`) and `@attack-4` (`#1314`) while maintaining strict blindness (author `verify.py` and author scratch `notes/` not read):

1. **Citation & primary-source numbering (`TARGET.md`, `PROOF.md`, `notes/check-check-1.md`):**
   - `TARGET.md` L12 cleaned stale `/Users/kev/...` path to `tools/.arxiv_cache/eprint/2610.19249/gk74-2.tex`.
   - `TARGET.md` L14/L21/L28, `PROOF.md` L1/L7/L12/L17/L22/L24/L69/L79/L246/L257, and `notes/check-check-1.md` L5/L10/L15 now consistently cite **Section 1 Conjecture 1.1** (`conj:GK` = Guo–Krattenthaler `arXiv:1301.7651v3` Section 7 Conjecture 7.4 `conj:330n88n`), **Section 4 Conjecture 4.4** (`conj:general`), and **Section 4 Conjecture 4.5** (`conj:almost`, explicitly noted as not claimed).
2. **Proof rigor clarifications (`PROOF.md`):**
   - L149 & L232: Explicitly states the uniform-in-$(m \ge m_0, \omega \in [0.70, \omega_b])$ concavity lower bounds $\sin(a|\varphi|/2) \ge \min(\sin((1-\frac{1}{2m_0})\cdot 0.70), \sin(\omega_b))$ and $\sin(b|\varphi|/2) \ge \min(\sin((\frac32-\frac{1}{2m_0})\cdot 0.70), \sin(\frac32\omega_b))$ covering the regime where $b|\varphi|/2 > \pi/2$.
   - L214: Adds the unconditional $\max(0, \dots)$ clamp on the cancellation-free lower bound numerator before dividing by $2 V_{\mathrm{hi},m}$.
3. **Independent verifier fixes & re-execution (`notes/check-check-1.py`):**
   - Inspected all 4 patched sites:
     - L467 (`vp0_s`): retains full integral boundary term `(v_fn(A_abs_lo) + v_fn(B_lo))` without dividing by `s_min` (plus conservative `(abs(vp_fn(A_abs_lo)) + abs(vp_fn(B_lo))) / s_min`).
     - L833–834 (`K_ratio_interval`): uses full $m \ge m_0$ intervals `a_ang = iv.mpf([(I(1) - I(1)/(I(2)*m)).a, I(1).b]) * w_iv` and `b_ang = iv.mpf([(F(3,2) - I(1)/(I(2)*m)).a, F(3,2).b]) * w_iv`.
     - L896 (`I_C`): includes the missing factor `I(2) * PI`.
     - L962 (`I_seg`): uses upper bound `I(V_m.b)` instead of `V_lo_m`.
   - AST float audit: `FLOAT_CONSTANTS: 0 []`, `FLOAT_CALLS: 0 []`.
   - Re-ran `.venv/bin/python -u targets/mirzavaziri-2610.19249-conj1/notes/check-check-1.py` -> exit code `0`, `PASS`:
     - Part A (`8s`): all `57` admissible $m \le 100$ verified in exact `int` arithmetic.
     - Part B (`39s`, `mpmath.iv` `dps=30`): Regime III $[0, 0.5]$ (8 blocks) `min Net >= +0.77987`; Regime IIa $[0.5, 3.7]$ (32 blocks) `min Net >= +0.4183219`; Regime IIb $[3.7, 5.5]$ (3 slices) `min Net >= +0.02184526`; Regime I $[5.5, \infty)$ `Net >= +0.2767805` (`Maj >= 0.5640574`, `Min <= 0.2872769`). Uniformly `min Net >= +0.02184526 > 0` for all $m \ge 101$.
4. **Gate 2 novelty:** Confirmed `notes/novelty-gate2-watch-{1,5,6}.md` all PASS (`arXiv:2610.19249v1` sole version, `0` competing proofs closing $[301, 10^{30})$).

**Final Verdict:** **PASS** — ready for Gate 3 freshness check (`<1h`) and reporting to `@coordinator`.

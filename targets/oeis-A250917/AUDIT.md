# Adversarial Audit Report: `oeis-A250917`

- **Auditor:** `audit-2`
- **Audited at (UTC):** `2026-11-26T21:27Z`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Independent Verifier:** `targets/oeis-A250917/notes/check-check-2.py` (report: `targets/oeis-A250917/notes/check-check-2.md`)

---

## 1. Isolation & Materials Inspected

In accordance with `CHARTER.md`, this audit was conducted without reading `verify.py`, `notes/screen-*`, `notes/attack-*`, or author scratch commentary. Inspected materials:
1. Primary source: Live OEIS JSON (`https://oeis.org/search?q=id:A250917&fmt=json`, revision 20, `2025-03-15`, extracted in `notes/audit-helper-a250917.md`).
2. `targets/oeis-A250917/TARGET.md`.
3. `targets/oeis-A250917/PROOF.md`.
4. `targets/oeis-A250917/notes/check-check-2.md` and `targets/oeis-A250917/notes/check-check-2.py`.
5. Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) and independent adversarial literature/OEIS/symbolic verification notes (`notes/audit-helper-a250917.md`, produced by Flash helper `oeis250917-hlp`).

---

## 2. Primary-Source Fidelity Audit

Verified directly against live OEIS **A250917** (revision 20, `2025-03-15`):
- **Name:** `"Expansion of e.g.f. exp( x*C(x)^3 ) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, A000108."` (offset `0,3`).
- **Conjectured Formula (R. J. Mathar, Jan 25 2020):**
  > `Conjecture D-finite with recurrence: +2*a(n) +(-11*n+20)*a(n-1) +(n^3+9*n^2-116*n+164)*a(n-2) +(-4*n^4+35*n^3+n^2-317*n+342)*a(n-3) -6*(n-3)*(6*n^3-50*n^2+147*n-176)*a(n-4) +12*(n-5)*(2*n-9)*(n-3)*(n-4)*a(n-5)=0.`
- **Fidelity Verdict:** Character-for-character match across `TARGET.md`, `PROOF.md`, and `notes/check-check-2.py`. Clarifying the natural domain of an order-5 recurrence on an offset-0 sequence ($n \ge 5$, and also $n = 3, 4$ where the coefficients of all negative-index terms vanish identically, while failing at $n = 0, 1, 2$ with LHS $= 2, 11, -12$) is accurate and transparent. Zero quantifier, sign, or definition drift.

---

## 3. Adversarial Mathematical & Symbolic Audit

Checked every analytic, algebraic, and computational step of `PROOF.md` and audited all 167 lines of `notes/check-check-2.py`:

1. **Differential field & analyticity:**
   - On $|x| < 1/4$, $\Delta(x) = 1 - 4x \neq 0$, so $S(x) = \sqrt{1 - 4x}$ (with $S(0) = 1$) is analytic and satisfies $S' = \frac{-2}{1-4x} S$.
   - Since $1 - 4x$ is not a square in $\mathbb{Q}(x)$, $\mathcal{A} = \mathbb{Q}(x)[S]/(S^2 - (1-4x))$ is a quadratic field extension of $\mathbb{Q}(x)$ equipped with the unique derivation extending $d/dx$, and sending $S \mapsto \sqrt{1-4x}$ embeds $\mathcal{A}$ injectively as a differential field into the field of meromorphic functions on $|x| < 1/4$.
   - $C(x) = \frac{1 - S}{2x}$ and $g(x) = x C(x)^3$ have removable singularities at $x = 0$ with $C(0) = 1$ and $g(0) = 0$; hence $F(x) = \exp(g(x))$ is analytic and nonvanishing on $|x| < 1/4$, and every $\theta^j F^{(r)}(x)$ is analytic on $|x| < 1/4$.
   - Independent pole verification (`notes/audit-helper-a250917.md` §3B) confirms every denominator of $F^{(r)}/F = A_r(x) + B_r(x) S$ ($r=0,\dots,5$) and of every operator summand $Q_r(\theta)[F^{(5-r)}]/F$ is of the form $2^\epsilon x^a (4x-1)^b$, so all rational coefficients are holomorphic on the punctured disk $0 < |x| < 1/4$.
2. **Recurrence-to-operator translation:**
   - Setting $m = n - 5 \ge 0$ and multiplying $\sum_{r=0}^5 P_r(m+5) a(m + 5 - r)$ by $\frac{x^m}{m!}$ and summing over $m \ge 0$ gives
     $$L[F](x) = \sum_{r=0}^5 Q_r(\theta)\bigl[F^{(5-r)}(x)\bigr], \qquad Q_r(m) = P_r(m + 5),$$
     since $F^{(s)}(x) = \sum_{m=0}^\infty a(m+s)\frac{x^m}{m!}$ and $\theta = x\frac{d}{dx}$ multiplies $[x^m]$ by $m$.
   - *(Minor non-fatal expository note: `PROOF.md` line 24 reuses the letter $r$ in $\sum P_r(m+5) a(m+r) x^m/m! = Q_r(\theta)[F^{(r)}(x)]$ right before defining $P_r(n)$ as the coefficient of $a(n-r) \leftrightarrow F^{(5-r)}$ on lines 26–27; line 27 has the exact correct formula $\sum_{r=0}^5 Q_r(\theta)[F^{(5-r)}(x)]$.)*
3. **Exact symbolic vanishing & small-$n$ boundary:**
   - Line-by-line audit of `notes/check-check-2.py` confirms exact rational/polynomial arithmetic in SymPy (`sp.Rational`, `sp.Integer`, `sp.cancel`, zero floats) computing $L[F](x)/F(x) = R(x, S) = (0, 0)$ identically in $\mathcal{A}$.
   - Hence $L[F](x) = R(x, \sqrt{1-4x}) F(x) = 0$ on $0 < |x| < 1/4$, and by continuity on all of $|x| < 1/4$, forcing $[x^m] L[F](x) = 0$ for every $m \ge 0$, i.e. Mathar's recurrence holds for all $n \ge 5$.
   - Direct hand arithmetic verified $n = 3, 4$: $P_4(3) = P_5(3) = P_5(4) = 0$ (no negative-index convention needed!), and at $n=3$: $2(73) - 13(7) - 76(1) + 21(1) = 0$; at $n=4$: $2(1033) - 24(73) - 92(7) + 306(1) + 24(1) = 0$.
   - Re-run of `.venv/bin/python -u targets/oeis-A250917/notes/check-check-2.py` (`notes/audit-helper-a250917.md` §3A) returned exit code `0` and `PASS` in `12.002s`, independently matching all 19 OEIS terms and checking the recurrence through $n = 25$.

---

## 4. Adversarial Novelty Audit & Caveats

Deep checks (`notes/audit-helper-a250917.md`, plus Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`) confirmed:
- **No prior proof found** on live OEIS `A250917` (rev 20) or any sibling/xref entry (`A250916`, `A250918`, `A251568`, `A080893`, `A091695`, `A380512`, `A380515`, `A001517`), in `watch/snapshots/**`, Zenodo (including Roberto Blanco Gómez's 37 Zenodo records), `joaquimmj/oeis-conjectures`, arXiv, Crossref, or web/SeqFan searches.
- **Documented Near-Miss (`gfis/OEIS-mat` & `archmageirvine/joeis`):** `holrec/rectopost.man` and `A250917.java` (Aug 2022) record an *unproved* Maple `sumrecursion` order-3 recurrence $Q(n)$ on the OEIS binomial sum formula (of which Mathar's order-5 recurrence $P(n)$ is a $\mathbb{Q}(n)$-left-multiple), with no proof, no creative-telescoping certificate, no equivalence proof with $\exp(x C(x)^3)$, and no derivation of Mathar's order-5 recurrence. This does not settle Mathar's conjecture.
- **What Is Not Established / Caveats:**
  - The algebraic cancellation $R(x, S) = (0, 0)$ in $\mathcal{A} = \mathbb{Q}(x)[S]/(S^2 - (1-4x))$ is a computer-verified exact symbolic computation (verified independently by `notes/check-check-2.py`), not expanded term-by-term by hand inside `PROOF.md`.
  - OpenAlex returned HTTP 429 during the helper's fresh check (though `watch-5` confirmed 0 OpenAlex hits for `A250917` at Gate 2, and Zenodo/arXiv/Crossref/GitHub/OEIS/web were all live-checked).
  - Internal audit and SymPy exact symbolic verification are not formal peer review or a Lean formalization.

---

## 5. Final Verdict

**PASS** — `"written proof, internally audited"`. Gate 3 novelty cleared (`notes/novelty-gate3-watch-1.md`, `notes/novelty-gate3-watch-5.md`, `notes/novelty-gate3-watch-6.md`, checked `2026-11-26T21:37–21:56Z`).

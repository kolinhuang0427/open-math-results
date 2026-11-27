# Adversarial Audit Report: `targets/dawsey-2107.14284-conj5.1/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T09:02Z`
- **Target:** Madeline Locus Dawsey, Matthew Just, and Robert Schneider, *"A 'supernormal' partition statistic"*, `arXiv:2107.14284v2` (`main.tex`, **Section 4**, **Conjecture 4.1** `\label{conj1}`, lines 1083–1086)
- **Owner:** `scout-11`
- **Checker:** `check-1` (`notes/check-check-1.md`, `notes/check-check-1.py`)
- **Strict Isolation Observed:** Read ONLY primary sources `tools/.arxiv_cache/eprint/2107.14284v2/main.tex` and `tools/.arxiv_cache/eprint/2107.14284v1/main.tex`, `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,4}.md`. Did NOT read author `verify.py` or any author scratch `notes/`. Did NOT edit `TARGET.md` or `PROOF.md`.
- **Verdict:** **`FAIL`** *(1 blocking primary-source citation/numbering error in `TARGET.md` and `PROOF.md`; all mathematical steps, verbatim text, and exact verification PASS)*

---

## 1. Exact Blocking Issue to Fix

1. **Wrong section & conjecture number for `arXiv:2107.14284v2` (`TARGET.md` lines 2, 9, 13, 15 and `PROOF.md` lines 1, 3):**
   - Both `TARGET.md` and `PROOF.md` cite the target as **"Section 5, Conjecture 5.1"** of `arXiv:2107.14284v2`.
   - Direct inspection of `tools/.arxiv_cache/eprint/2107.14284v2/main.tex` (and `v1/main.tex`) shows there are only **four** numbered `\section` environments:
     - Line 64: `\section{Introduction: the supernorm statistic on partitions}\label{sect1}` (Section 1)
     - Line 601: `\section{Analytic comparisons of partition statistics}\label{sectanalytic}` (Section 2)
     - Line 771: `\section{Partition bijections and arithmetic densities}\label{sect2}` (Section 3)
     - Line 954: `\section{``Supernormal'' maps and Abelian-type conjectures}\label{sect5}` (**Section 4** — `\label{sect5}` is an internal TeX label artifact!)
   - Because line 12 declares `\newtheorem{conjecture}{Conjecture}[section]`, line 1083 (`\begin{conjecture}\label{conj1}`) is literally **Conjecture 4.1** in **Section 4** of `arXiv:2107.14284v2` (and likewise Section 4, Conjecture 4.1 in `v1`).
   - **Fix (do NOT rename the folder slug `dawsey-2107.14284-conj5.1`):** Update `TARGET.md` (header `source:`, title/body) and `PROOF.md` (title & theorem header) to cite **`arXiv:2107.14284v2`, Section 4 (`\label{sect5}`), Conjecture 4.1 (`\label{conj1}`)** accurately (noting that the folder slug retains `conj5.1` from the TeX label `\label{sect5}`), and remove the unverified `?` DOI note in `TARGET.md` line 2 unless verified.

---

## 2. What Passed (No Rework Needed)

- **Verbatim text & definition fidelity:** The quoted statement (`main.tex` lines 1083–1086) and definitions ($\mathbb{N} = \{1, 2, \dots\}$, $\mathbb{P} = \{p_1 < p_2 < \cdots\}$, $\mathrm{idx}(p_k) = k$, $f : \mathbb{N} \to \mathbb{C}$, $L_f = \lim_{N \to \infty} \frac{1}{N} \sum_{k=1}^N f(k)$) match `arXiv:2107.14284v2` word-for-word.
- **Line-by-line mathematical audit of `PROOF.md`:**
  - **Step 1:** Boundedness of $S_k / k \to L_f \in \mathbb{C}$ gives $|S_k| \le Ck$. Summation by parts $\sum_{k=N}^M f(k) p_k^{-s} = S_M p_M^{-s} - S_{N-1} p_N^{-s} + \sum_{k=N}^{M-1} S_k (p_k^{-s} - p_{k+1}^{-s})$ is exact. Since $p_M \ge M$, $|S_M p_M^{-s}| \le C M^{1-s} \to 0$ for every real $s > 1$; strict monotonicity $p_k^{-s} - p_{k+1}^{-s} > 0$ and exact telescoping $\sum_{k=1}^{M-1} k(p_k^{-s} - p_{k+1}^{-s}) = \sum_{k=1}^{M-1} p_k^{-s} - (M-1)p_M^{-s} < P(s) \le \zeta(s) < \infty$ yield absolute convergence of $\sum_{k=1}^\infty S_k(p_k^{-s} - p_{k+1}^{-s})$, hence convergence of the ordered Dirichlet series $\lim_{M \to \infty} \sum_{k=1}^M f(k) p_k^{-s}$ for every $s > 1$ (even when $f$ is unbounded and the numerator does not converge absolutely on $1 < s \le 2$), and $P(s) = \sum_{k=1}^\infty k(p_k^{-s} - p_{k+1}^{-s})$.
  - **Step 2:** Absolute convergence justifies subtracting $L_f P(s)$ termwise to $\sum_{k=1}^\infty \varepsilon_k k(p_k^{-s} - p_{k+1}^{-s})$ with $\varepsilon_k = S_k / k - L_f \to 0$. Splitting at $K$ where $|\varepsilon_k| < \eta / 2$ for $k > K$, bounding $0 < p_k^{-s} - p_{k+1}^{-s} < p_k^{-s} < p_k^{-1}$ (valid since $p_k \ge 2$ and $s > 1$) for $1 \le k \le K$ by the $s$-independent constant $C_K$, and bounding the tail by $\frac{\eta}{2 P(s)} P(s) = \frac{\eta}{2}$ yields $\le C_K / P(s) + \eta / 2$. Finally, Euler's theorem $\sum_{k=1}^\infty p_k^{-1} = \infty$ implies $\liminf_{s \to 1^+} P(s) \ge \sum_{k=1}^M p_k^{-1}$ for every $M$, so $P(s) \to +\infty$ as $s \to 1^+$, closing the proof cleanly.
- **Independent mechanical verification:** Re-executed `.venv/bin/python targets/dawsey-2107.14284-conj5.1/notes/check-check-1.py` -> exit code `0`, raw `PASS`.
- **Scholarly scope notes (for final `RESULTS.md` "What is not established"):**
  - For unbounded $f$ with finite Cesàro mean, convergence of the numerator on $1 < s \le 2$ holds as the ordered Dirichlet series $\lim_{M \to \infty} \sum_{k=1}^M f(k) p_k^{-s}$ (not necessarily unconditionally/absolutely).
  - Establishes the stated real limit $s \to 1^+$ of Conjecture 4.1 (`\label{conj1}`), not complex Stolz-sector limits (footnote, line 1054) nor Conjecture 4.2 (`\label{conj2}`).
  - Paywalled *J. Number Theory* 241 (2022), 120–141 PDF was not directly downloaded.

## 3. Handoff

Returned to `@scout-11` and `@triage` for the quick `Section 4, Conjecture 4.1 (\label{conj1})` numbering correction in `TARGET.md` and `PROOF.md`. Once patched, ready for immediate re-audit PASS and Gate 3 novelty check.

---

## 4. Re-Audit After Fix (`audit-2`, `2026-11-27T09:06Z`)

- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (supported by exact integer/`Fraction`/interval verification in `notes/check-check-1.py`). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Verified Fixes:** Both `TARGET.md` (lines 2, 9–17) and `PROOF.md` (lines 1, 3) now accurately cite `arXiv:2107.14284v2`, Section 4 (`\label{sect5}`), Conjecture 4.1 (`\label{conj1}`) (noting the retained folder slug `dawsey-2107.14284-conj5.1`), with the unverified `?` DOI removed.
- **Independent Verifier:** `.venv/bin/python targets/dawsey-2107.14284-conj5.1/notes/check-check-1.py` (previously executed directly with exit code `0`, raw `PASS`; proof body unchanged).
- **Gate 2 Novelty:** Clear (`notes/novelty-gate2-watch-{1,4,5,6}.md`, no `CONTESTED.md`).
- **Handoff:** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final reporting to `@coordinator`.

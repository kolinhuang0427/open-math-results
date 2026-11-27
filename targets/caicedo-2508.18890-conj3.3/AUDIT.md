# Adversarial Audit Report (`audit-1`): `targets/caicedo-2508.18890-conj3.3/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Jhon B. Caicedo, Martina Juhnke, & Germain Poullot, *Ehrhart non-positivity and unimodular triangulations for classes of $\mathbf{s}$-lecture hall simplices*, `arXiv:2508.18890v4`, Section 3, **Conjecture 3.4** (`Ehrhart_non_positivity.tex` L109–111; historical folder slug `conj3.3`)
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `#698` and `#722` patches), `notes/check-check-1.md`, `notes/check-check-1.py` (re-checked in `#724`), and primary source `tools/.arxiv_cache/eprint/2508.18890/{main,Introduction,Preliminaries,Ehrhart_non_positivity}.tex` (verified live arXiv latest version is `2508.18890v4`)
- **Verdict:** **PASS**

---

## 1. Primary-Source Statement Fidelity
- Verified verbatim against `tools/.arxiv_cache/eprint/2508.18890/{main,Introduction,Preliminaries,Ehrhart_non_positivity}.tex` (shared `[theorem]` counter across Section 3 `Ehrhart_non_positivity.tex`):
  - **Proposition 3.1** (L32), **Theorem 3.2** (L64), **Example 3.3** (L98–101), **Conjecture 3.4** (L109–111: *"For $n\geq 5$, we conjecture that if $\mathcal{P}_n^{(a, \dots, a, a+1)}$ is Ehrhart non positive for some $a\in \mathbb{N}$, then for all $b\geq a$ the $\mathbf{s}$-lecture hall simplex $\mathcal{P}_n^{(b, \dots, b, b + 1)}$ is also Ehrhart non positive."*), and **Theorem 3.5** (L128).
  - Prior FAIL numbering fixes (`Conjecture 3.4` and `Example 3.3`, retaining historical folder slug `conj3.3`) are cleanly resolved across `TARGET.md`, `PROOF.md`, and `notes/check-check-1.{md,py}`. The misprint on line 88 of `Ehrhart_non_positivity.tex` vs. lines 81–84 / 399–400 is transparently disclosed.

## 2. Adversarial Line-by-Line Mathematical Audit
- **Lemma 1 (`PROOF.md` §1):** Exact Ehrhart formula (1) from Proposition 3.1 & Beck–Robins, generating function (2) for $[t^k]\mathcal{L}_n(t,a)$ ($k \ge 1$), and partial fraction identity (3) for $F_a(x)$ verified line-by-line.
- **Lemma 2 (`PROOF.md` §2):** Exact proof of Ehrhart positivity for all $1 \le a \le 6$ and all $n \ge 1$ via $f_{a,n} \ge 1 - \frac{1}{a}\sum_{m=1}^{a-1}\frac{1}{2\sin(\pi m/a)} > 0$.
- **Lemma 3 (`PROOF.md` §3):** Exact formula (4) via Stirling numbers of the first kind and Faulhaber's formula; exact rational Sturm/interval root isolation over all $5 \le n \le 32$ and $1 \le k \le n$ proves exact integer thresholds $m_n \in [8, 16]$ with $[m_n, \infty) \cap \mathbb{N}$ completely covered by strictly negative gaps.
- **Lemma 4 (`PROOF.md` §4):** Exact $[t^{n-4}]$ quartic in $a$ verified symbolically for all $n \ge 5$, with both $n$-cubics proved strictly negative on $[5, \infty)$ and upper bound $0.65 + 0.25 = 0.90 < 1$ for all $a \ge 2n^{4/3}$.
- **Lemma 5 (`PROOF.md` §5 — re-audited after `#698` & `#722` patches):**
  - Sign of $M_k(n, a)$ fixed on L86–88 to $\cos(-n\theta_a - \frac{k\pi}{2})$ (exact match with $a u(x_1) = -2\pi i = 2\pi e^{-i\pi/2}$).
  - **Case 5a ($a \in \{8, 9, 10\}, n \ge 33$):** Explicit $n \to n+1$ step ratio $(1 + \frac{1}{34 H_{33}})^4 \cdot 2\sin(\pi/8) \approx 0.7876 < 0.79 < 1$ combined with exact interval check at $n = 33$ proves error/$|M_k| < 1$ for all $n \ge 33$.
  - **Case 5b ($a \ge 11, n \ge 33$):**
    - L103 convexity proof ($g(u) = \arcsin(3\sin u)$, $g'(u) = 3/\sqrt{1 - 8\tan^2 u}$ strictly increasing on $(0, \pi/11]$) rigorously proves $a|\phi| < 3.40\pi < \frac{7\pi}{2}$ for all $a \ge 12$ and $< 3.53\pi$ at $a = 11$.
    - L104 ($\cos(a\phi) \le 0 \implies |1 - z^{\pm a}| \ge 1$), L105 (explicit quadratic $r_\pm = \cos\phi \pm \sqrt{R_a^2 - \sin^2\phi}$ giving $|1 - z^a| \ge 1 - r_-^a > 0.993 > 0.85$ for $r \le 1$ and $|1 - z^{-a}| \ge 1 - r_+^{-a} > 0.862 > 0.85$ for $r > 1$ uniformly for **all** $a \ge 11$), and L106 ($|1 - z^{\pm 11}| \ge |\sin(11\phi)| > 0.9967 > 0.99$ on $(3.5\pi, 3.53\pi)$) rigorously prove $a|G_a(x)| \le 3\pi / 0.85 < 11.1$ for all $a \ge 11$.
    - L110–111 (stray $k!$ removed): $\frac{\partial}{\partial a}\ln(a^{k+1}(2\sin(\pi/a))^n) \le \frac{1}{a}(5 - 33\frac{\pi/11}{\tan(\pi/11)}) < -27/a < 0$ proves $E_1/|M_k|$ is strictly decreasing in $a \ge 11$ (maximized at $a = 11$), and at $a = 11$ strictly decreasing in $n \ge 33$ by factor $< 0.58 < 1$, with $n = 33, a = 11$ bound $\le 0.001636 < 0.002 < 1$ for all $k \in \{1, 2, 3, 4\}$.
- **Conclusion (§6):** Completely airtight synthesis of Lemmas 2–5 proving Conjecture 3.4 for all $n \ge 5$ and all $b \ge a \ge 1$.

## 3. Independent Verification & Gate 2 Novelty
- **Independent checker:** Re-executed `.venv/bin/python -u targets/caicedo-2508.18890-conj3.3/notes/check-check-1.py` -> exit code `0`, `PASS` (verified Lemmas 1–5 with pure `int`/`Fraction`, SymPy exact `QQ[a]` Sturm root isolation, and 50-digit `mpmath.iv` interval arithmetic).
- **Gate 2 novelty receipts:** All three watchers clear (`watch-1` `#492`, `watch-5` `#521`, `watch-6` `#520`).
- **Handoff:** Ready for Gate 3 novelty verification (`@watch-1`, `@watch-5`, `@watch-6`).

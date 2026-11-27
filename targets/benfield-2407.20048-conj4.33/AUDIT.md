# Adversarial Audit Report (`audit-1`): `targets/benfield-2407.20048-conj4.33/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Benfield & Lippard, `arXiv:2407.20048v2` (*Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers*, updated `2025-01-30`), Section 4.2, Conjecture 4.33 (`\label{even-K-exceptions}`)
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after L46 patch per `#296`), `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2407.20048/fiborder.tex`
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Re-Audit Summary (`PROOF.md` L46 Patch)

The initial audit flagged a mislabeled parenthetical remark on `PROOF.md` L46 (`(Alternatively, if \omega = 1 and 4 \mid \pi = \alpha, ...)`), which proved the converse ($\omega = 1 \implies 4 \nmid \pi$) rather than Claim (3) ($4 \nmid \pi \implies \omega = 1$). `@scout-11` removed the parenthetical (`#296`), and `PROOF.md` L46 now reads cleanly:
> `- **Claim (3):** By contrapositive, we show that if $\omega \in \{2, 4\}$, then $4 \mid \pi$. If $\omega = 4$, then $4 \mid 4\alpha = \pi$. If $\omega = 2$, Claim (2) gives $4 \mid \pi$. Thus $4 \nmid \pi \implies \omega = 1$. $\square$`

No remaining issues.

---

## 2. Primary-Source Fidelity & Mathematical Verification

- **Primary-source fidelity (`fiborder.tex`):** Verified exact environment numbering in Section 4 (`\newtheorem{theorem}{Theorem}[section]`, shared counter): `\label{omega-odd-K}` = 4.26, `\label{omegaK(2)^x-even}` = 4.28, `\label{omega-even-K}` = 4.29, `\label{mainthm-even-K}` = 4.31, Question 4.32, **Conjecture 4.33** = `\label{even-K-exceptions}` (L675–682). Definitions (L84, L273, L310) and Conjecture 4.33 match `TARGET.md` verbatim. Passing note in `PROOF.md` L15 regarding the `lcm[1, ...]` typo in `fiborder.tex` L615 (`Theorem 4.29`, e.g., $K=2, m=10$) is accurate, and `PROOF.md` is completely self-contained.
- **Line-by-line proof check:**
  - **Setup & Lemma 1 (L9–31):** Matrix $U = \begin{pmatrix} K & 1 \\ 1 & 0 \end{pmatrix}$ ($\det U = -1$), pure periodicity mod $m \ge 2$, $\alpha_K(m) \mid n \iff m \mid F_{K,n}$, $\beta = F_{K,\alpha+1}$ with $\beta^2 \equiv (-1)^\alpha \pmod m$, $\omega_K(m) = \mathrm{ord}_m(\beta) \in \{1, 2, 4\}$, $\pi_K(m) = \alpha_K(m)\omega_K(m)$, and $\mathrm{lcm}$ relations for $\alpha_K$ and $\pi_K$. All exact for all $K \in \mathbb{Z}, m \ge 2$.
  - **Lemma 2 (L35–46):** For odd $n \ge 3$ ($-1 \not\equiv 1 \pmod n$), all three assertions hold cleanly.
  - **Lemma 3 (L50–71):** For even $K \in \mathbb{Z}$ (including $K = 0$ and negative even $K$) and all $x \ge 1$, $F_{K,2r} = F_{K,r} L_{K,r}$, $L_{K,2r} = L_{K,r}^2 - 2(-1)^r \equiv 2 \pmod 4$, and induction on $x$ establishes $\omega_K(2^x) = 1$ and $\pi_K(2^x) = \alpha_K(2^x) = 2^a$ ($a \ge 1$). Exact.
  - **Main Proof (L75–102):** Partitioning $m > 3$ as $m = 2^x n$ ($x \ge 0$, $n \ge 1$ odd) into Case 1 ($x=0, n>3$), Case 2 ($x \ge 2, n=1$), and Case 3 ($x \ge 1, n \ge 3$ odd; $\omega_K(m) = 2^{\max(a, v+\nu_2(\omega_K(n))) - \max(a, v)}$ since odd parts of $\pi_K(m)$ and $\alpha_K(m)$ coincide as $\omega_K(n) \in \{1,2,4\}$) exhaustively verifies all three claims across all 7 subcases. Exact.
- **Independent checker (`notes/check-check-2.py`):** Executed `.venv/bin/python targets/benfield-2407.20048-conj4.33/notes/check-check-2.py` -> exit code `0`, `PASS (Lemmas 1-3 + all 7 proof subcases verified across 6422 even-(K,m) pairs)`.
- **Gate 2 novelty:** All three watchers clear (`watch-1` `#267`, `watch-5` `#260`, `watch-6` `#281`).

---

## 3. Verdict

**PASS.** Ready for Gate 3 novelty verification (`<1h`).

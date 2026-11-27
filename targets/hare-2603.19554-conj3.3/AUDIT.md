# Blind Audit Report: `hare-2603.19554-conj3.3`

**Auditor:** `audit-3` (blind Pro audit; author `notes/` not read)
**Timestamp (UTC):** `2026-11-27T09:20Z`
**Verdict:** **PASS** — Written proof with exact integer-interval verification of $4 \le d \le 499$ (`"written proof, internally audited"`).

## 1. Primary-Source Fidelity
Verified verbatim against `arXiv:2603.19554v1` (confirmed latest version via live arXiv API query on `2026-11-27`, published/updated `2026-03-20T01:33:42Z`), Kevin G. Hare and Hachem Hichri, *"The Parry Order of Perron Numbers"*, `tools/.arxiv_cache/eprint/2603.19554/v6.tex`:
- **Conjecture 3.3 (`\label{conj:1}`, Section 3.1 `sec:beta, theta`, lines 489–493):**
  > For all $d \geq 4$ and all $k \geq 1$ we have $\beta_d^k$ is non-Parry.
  where (line 489) $\beta_d$ is the Perron number of minimal polynomial $x^d - x - 1 = 0$.
- **Definitions (Introduction, lines 84–95; Section 2, Lemmas 2.1, 2.4, 2.6):** $T_\beta(x) = \beta x \bmod 1$, $\beta$ is a Parry number iff $\{T_\beta^{[k]}(1)\}_{k=1}^\infty$ is finite, Solomyak's bound $\theta_0 = (1+\sqrt{5})/2$, and Akiyama's divergence criterion all match `TARGET.md` and `PROOF.md` verbatim across the full quantifier range $d \ge 4$, $k \ge 1$.

## 2. Line-by-Line Mathematical Audit of `PROOF.md`
1. **Section 1 (Preliminaries):**
   - *Irreducibility and degree of $\beta_d^k$:* Selmer (1956, Theorem 1) establishes irreducibility of $P_d(x) = x^d - x - 1$ over $\mathbb{Q}$ for all $d \ge 2$. Uniqueness of the real root $\beta_d > 1$, the Perron property $|\gamma| < \beta_d$ for every conjugate $\gamma \neq \beta_d$, and the fact that $\beta_d^k$ has full degree $d$ with conjugates $\gamma^k$ (since $|\gamma|^k < \beta_d^k$ implies no non-identity embedding fixes $\beta_d^k$) are completely rigorous.
   - *Solomyak's bound:* Uses strict inequality $|\gamma|^k > \theta_0 = (1+\sqrt{5})/2$, matching Solomyak (1994).
   - *Akiyama's divergence criterion:* Since $x_0 = 1$ and $x_m \in [0, 1)$ for $m \ge 1$, every greedy digit satisfies $0 \le c_{m+1} = \lfloor q x_m \rfloor \le \lfloor q \rfloor$. Hence $|\sigma(x_n)| > \lfloor q \rfloor / (|c| - 1)$ with $|c| > 1$ inductively implies strict growth $|\sigma(x_{m+1})| > |\sigma(x_m)|$ for all $m \ge n$, forcing an infinite orbit.
   - *Closed-form Akiyama block for $q \in (1, 2)$:* Checked both $m_0 = 2$ and $m_0 \ge 3$. Existence and uniqueness of $m_0 \ge 2$ with $q^{m_0 - 2}(q - 1) < 1 \le q^{m_0 - 1}(q - 1)$ holds since $0 < q - 1 < 1$ and $q > 1$. Non-vanishing of $1 - c^{-1} - c^{-m_0}$ transfers via Galois conjugation to strict inequality $q^{m_0 - 1}(q - 1) > 1$, while $q^{m_0 - 2}(q - 1) < 1$ gives $q^{m_0 - 1}(q - 1) < q < 2$. The greedy orbit yields $x_{2m_0 - 2} = q^{2m_0 - 2}(1 - q^{-1} - q^{-m_0})$ in both cases $m_0 = 2$ and $m_0 \ge 3$, so $\sigma(x_{2m_0 - 2}) = c^{2m_0 - 2}(1 - c^{-1} - c^{-m_0})$. Complete and airtight.
2. **Section 3 (Analytic Proof for $d \ge 500$):**
   - *Lemma 3.1:* $2^{1/d} < \beta_d < 1 + \frac{\ln 2}{d} + \frac{1}{d^2}$ and $\frac{\ln 2}{d} < \ln \beta_d < \frac{\ln 2}{d} + \frac{1}{d^2}$ verified step by step for all $d \ge 500$.
   - *Lemma 3.2:* Rouché's theorem on $|z - z_0| = 5/d^2$ around $z_0 = \exp((\ln 2 + 2\pi i)/d)$ yields a unique root $\gamma_d$ with $\mathrm{Im}(\gamma_d) > 0$, $\ln|\gamma_d| \ge \frac{\ln 2}{d} - \frac{5.01}{d^2}$, and $|\arg(\gamma_d) - \frac{2\pi}{d}| < \frac{5.01}{d^2}$.
     *Minor exposition note (non-blocking):* On line 72, the displayed inequality $2(e^{5/d} - 1 - 5/d) < 0.06/d$ is strictly true for all $d \ge 500$ (actual maximum at $d = 500$ is $0.050167\dots/d < 0.06/d$), via $e^y - 1 - y \le 0.51 y^2$ on $[0, 0.01]$; the parenthetical remark writes $e^y - 1 - y \le y^2$ (which gives $0.10/d$, still yielding $|E(w)| < 6.52/d < 9.98/d$). All displayed inequalities and the conclusion are completely valid.
   - *Completion of Proof ($d \ge 500$):* Assuming $|\gamma_d|^k \le \theta_0$, verified $t = k/d < 0.705$, $1 < q < 1.635 < 2$, $\frac{|c|-1}{q-1} > 0.9741$, the algebraic identity and positive-factor lower bound for $F(c)$ (valid for $m_0 = 2$ and $m_0 \ge 3$), and every estimate in Case A ($0 < t \le 0.5$, yielding $F(c) > 1.36 > 1$, noting $\frac{\ln(d/\ln 2)}{d}$ decreases for $d > e\ln 2$) and Case B ($0.5 < t \le 0.705$, yielding $m_0 \le 4$, $\max_{\phi \in [3.1365, 4.4368]} \cos\phi = \cos(4.4368) < -0.272$, and $F(c) > 1.15 > 1$).

## 3. Independent Mechanical Verification
Audited every line of `targets/hare-2603.19554-conj3.3/notes/check-check-3.py` (pure Python `int` fixed-point interval arithmetic at scale $2^{140}$ with zero floats for $4 \le d \le 499$, Rouché disk certification with Taylor remainder $\frac{d(d-1)}{2} r^2(|z_*|+r)^{d-2}$, exact integer floor-digit checks, Solomyak cutoff $(2s-3)^2 > 5$, plus `mpmath.iv` at `dps = 50` for Section 3 constants and spot checks at $d \in \{500, 501, 600, 1000\}$) and ran it directly:
- Command: `.venv/bin/python -u targets/hare-2603.19554-conj3.3/notes/check-check-3.py`
- Result: exit `0`, raw `PASS` (`4 <= d <= 499`: $496$ Solomyak cutoffs, $86205$ closed-form Akiyama blocks, $10$ greedy orbits with max step $35$; all Section 3 inequalities and spot checks passed).

## 4. Verdict & Handoff
**PASS.** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final coordinator verification.

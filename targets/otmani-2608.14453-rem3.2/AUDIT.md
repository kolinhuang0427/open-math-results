# Adversarial Audit Report (`audit-1`): `targets/otmani-2608.14453-rem3.2/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** Yassine Otmani, *New Congruences Involving $p$-adic dual sequences*, `arXiv:2608.14453v2`, Section 3, **Remark 3.1** (`Manuscript.tex` lines 471–477; historical directory slug `otmani-2608.14453-rem3.2`)
- **Audited Files:** `TARGET.md`, `PROOF.md` (re-audited after `Remark 3.2` $\to$ `Remark 3.1` fixes per `#403`), `notes/check-check-2.md`, `notes/check-check-2.py`, and primary source `tools/.arxiv_cache/eprint/2608.14453/Manuscript.tex`
- **Verdict:** **PASS** (Label: `"written proof, internally audited"`)

---

## 1. Re-Audit Summary (`Remark 3.1` Numbering Fix)

The initial audit confirmed zero mathematical gaps across Lemmas 1–6 and flagged that `Manuscript.tex` L20 defines `\newtheorem{remark}{Remark}[section]` on an independent counter from `\newtheorem{theorem}{Theorem}[section]` (L12–15), so the open problem at Section 3 `L471–477` compiles as **Remark 3.1** (not Remark 3.2, which is `L563`). `@scout-10` updated all text references in `TARGET.md` (L3, L11, L14, L19) and `PROOF.md` (L1, L22, L117, L128, L181) to **`Remark 3.1`** (`#403`) while preserving the folder slug.

All primary-source definitions, statements, and citations now match `Manuscript.tex` L198, L204, L463, L471–477 verbatim.

---

## 2. Full Mathematical Audit (Lemmas 1–6)

Every step of `PROOF.md` was verified line-by-line for all primes $p > 3$:

- **Lemma 1 (L19–32):** Exact reformulation $\mathcal{P}_k = 8^k \sum_{m=0}^{\lfloor k/2 \rfloor} \binom{k}{2m} c_m$, swap of summation giving $\sum_{k=0}^{p-1} \mathcal{P}_k^2 / 128^k = \sum_{m=0}^n c_m B_m$, mod-$p^4$ truncation of $\sum_{k=0}^{p-1} \binom{2k}{k}^4 / 256^k$ to $\sum_{m=0}^n c_m^2$, and $c_m \equiv \binom{n}{m}^2 \pmod p$ giving $c_m \equiv c_{n-m} \pmod p$ and $c_n \equiv 1 \pmod p$. Exact.
- **Lemma 2 (L36–53):** Self-contained proof of $H_n^{(2)} \equiv 0 \pmod p$ (using $p > 3 \implies 4 \not\equiv 1 \pmod p$) and Morley's congruence $\binom{p-1}{n} \equiv \varepsilon 4^{p-1} \pmod{p^3}$ via $X = pH_n$ and $Y = 2^{p-1}-1$. Exact.
- **Lemma 3 (L57–82):** $v_p \equiv \frac{1}{2} \pmod p$, $\frac{1}{p}\binom{2j}{j} \equiv -\frac{2}{r\binom{2r}{r}} \pmod p$ for $j = p - r$ ($1 \le r \le n$), decomposition $v_{p-1} = T_{\mathrm{mid}} + T_{\mathrm{tail}}$ with $c_n - \varepsilon T_{\mathrm{mid}} \equiv 0 \pmod{p^3}$ and $\frac{T_{\mathrm{tail}}}{p^2} \equiv \frac{1}{2}\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod p$, yielding $p^2 \mid E_p(n)$, $v_{p-1} \equiv \varepsilon \pmod p$, and $\tilde{E}_n \equiv -\frac{1}{2}\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod p$. Exact.
- **Lemma 4 (L86–111):** Exact polynomial ODE $\mathcal{L}_G(G)(x) = p^2 (1+x)^p (-2v_p + v_{p-1}(1+x))$ and exact operator identity $(1+x)\mathcal{L}_A = -x\mathcal{L}_G$ (independently verified symbolically), cancellation of monic $(1+x)$ mod $p^3$ in $\mathbb{Z}_{(p)}[x]$, $[x^{2m}]$ extraction giving $4m^2 B_m - (2m-1)^2 B_{m-1} \equiv -p^2 \pmod{p^3}$, and downward induction from $m = n$ to $m = 0$ proving $p^2 \mid E_p(m)$ and $4m^2 \tilde{E}_m - (2m-1)^2 \tilde{E}_{m-1} \equiv 1 \pmod p$. Exact.
- **Lemma 5 (L115–134):** Reflection $m' = n + 1 - m$ yields $4m^2 S_m \equiv (2m-1)^2 S_{m-1} \pmod p$ ($S_m = \tilde{E}_m + \tilde{E}_{n-m}$), reducing the theorem to $S_0 \equiv 0 \pmod p$; telescoping $\tilde{E}_m / c_m$ yields $S_0 \equiv 2\tilde{E}_n - T_{n-1} \pmod p$. Exact.
- **Lemma 6 (L138–181):** Self-contained telescoping proofs of Staver's identity (1) and Apéry's identity (3) (both polynomial/telescoping steps verified symbolically), mod-$p^2$ vanishing at $M = p-2$ and reflection giving $3\sum_{r=1}^n \frac{1}{r^2\binom{2r}{r}} \equiv -2\varepsilon T_{n-1} \pmod p$ (using $p > 3 \implies p \nmid 6$), and mod-$p$ reduction of Apéry's identity at $m = n$ giving $T_{n-1} \equiv -\varepsilon \sum_{t=1}^n \frac{(-1)^t}{t^2} \pmod p$, hence $S_0 \equiv 0 \pmod p$. Exact.

---

## 3. Independent Mechanical Verification & Gate 2 Status

- Executed `@check-2`'s independent exact-arithmetic verifier (zero floats):
  - Command: `.venv/bin/python targets/otmani-2608.14453-rem3.2/notes/check-check-2.py`
  - Raw output (exit code `0`): `PASS (CLF + Lemmas 1-6 verified for 5<=p<=73, Remark 3.2 verified for all 26 primes 5<=p<=107)` (note: print string in `check-check-2.py` uses the historical slug name; the mathematical statement checked is verbatim Remark 3.1, `Manuscript.tex` L471–477).
- Independently verified all symbolic operator identities (L98–100), Staver polynomial identity (L148, L151–152), and Apéry telescoping ratios (L169–173) via SymPy.
- Gate 2 novelty receipts from `watch-1` (`#350`) and `watch-6` (`#348`) are clear.

---

## 4. Verdict

**PASS.** Ready for Gate 3 novelty verification (`<1h`) — please note in `RESULTS.md` that the primary-source citation is **Section 3, Remark 3.1** (`Manuscript.tex` L471–477; folder slug `otmani-2608.14453-rem3.2`).

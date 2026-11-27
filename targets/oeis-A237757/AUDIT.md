# Blind Audit: `targets/oeis-A237757/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/oeis-A237757/TARGET.md`, `targets/oeis-A237757/PROOF.md`, `targets/oeis-A237757/notes/check-check-3.md`, `targets/oeis-A237757/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Source Checked:** Live OEIS JSON `https://oeis.org/search?q=id:A237757&fmt=json` (`rev. 17`, `2022-01-22T07:31:08-05:00`, offset `1,8`) and `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits).

---

## 1. Primary-Source Statement Fidelity

Verified verbatim against live OEIS **A237757** (`rev. 17`, `2022-01-22`, offset `1,8`):
- **Name (`%N`):** `Number of partitions of n such that 2*(least part) = (number of parts).`
- **Conjecture (`%F`):** `Conjectural g.f.: Sum_{n >= 0} q^(2*(n+1)^2)/Product_{k = 1..2*n+1} 1 - q^k. - _Peter Bala_, Feb 02 2021`
- **Data (`%S..%U`, 58 terms `a(1)..a(58)`):** `0,1,1,1,1,1,1,2,2,3,4,5,6,8,9,11,13,16,18,22,...,2703,3013`.
- **Minor cosmetic note (non-blocking):** `TARGET.md` L17 writes `for $n = 1,\dots,57$:` in the italicized data parenthetical before listing all 58 terms `a(1)..a(58)`; the verbatim conjecture statement and `PROOF.md` are unaffected.
- **Offset & Domain Check:** OEIS offset is `1,8` ($a(1)=0$, $a(2)=1$, first term $>1$ is $a(8)=2$). Both sides have zero $q^0$ term ($2(n+1)^2 \ge 2$ for all $n \ge 0$), so $\sum_{N \ge 1} a(N) q^N = \sum_{n \ge 0} q^{2(n+1)^2} / \prod_{k=1}^{2n+1}(1-q^k)$ matches OEIS `A237757` exactly.

---

## 2. Line-by-Line Mathematical Audit of `PROOF.md`

Audited every line (`L1–35`) of `PROOF.md`:
1. **Decomposition by least part (`L14–16`):** Every partition $\lambda$ of $N \ge 1$ is nonempty, so its least part $m = \lambda_\ell \ge 1$ is uniquely determined, and the condition $2m = \ell$ fixes the number of parts $\ell = 2m \ge 2$. Thus $\mathcal{P}(N) = \bigsqcup_{m \ge 1} \mathcal{P}_m(N)$ is an exact disjoint union.
2. **Bijection $\Phi_m : \mathcal{P}_m(N) \to \mathcal{Q}_{\le 2m-1}(N - 2m^2)$ (`L18–28`):**
   - For $\lambda = (\lambda_1 \ge \dots \ge \lambda_{2m}) \in \mathcal{P}_m(N)$ with $\lambda_{2m} = m$, subtracting $m$ from all $2m$ entries gives $\lambda_1 - m \ge \dots \ge \lambda_{2m-1} - m \ge 0$ and $\lambda_{2m} - m = 0$; dropping trailing zeros leaves a partition $\mu$ of $N - 2m^2$ with at most $2m - 1$ positive parts.
   - Edge cases verified: when $N < 2m^2$, both $\mathcal{P}_m(N)$ and $\mathcal{Q}_{\le 2m-1}(N - 2m^2)$ are empty; when $N = 2m^2$, the unique partition $(m,\dots,m) \in \mathcal{P}_m(2m^2)$ maps to the unique empty partition $\emptyset \in \mathcal{Q}_{\le 2m-1}(0)$.
   - Inverse $\Psi_m$: padding any $\mu = (\mu_1 \ge \dots \ge \mu_r > 0)$ ($0 \le r \le 2m-1$, $|\mu| = N - 2m^2$) with $2m - r \ge 1$ zeros gives $(\mu_1,\dots,\mu_{2m-1},0)$ with $\mu_{2m} = 0$; adding $m$ to every entry yields $(\mu_1+m,\dots,\mu_{2m-1}+m,m) \in \mathcal{P}_m(N)$. Clearly $\Phi_m \circ \Psi_m = \mathrm{id}$ and $\Psi_m \circ \Phi_m = \mathrm{id}$.
3. **Ferrers Conjugation & Formal Power Series Summation (`L30–35`):**
   - Ferrers conjugation ($\mu \mapsto \mu'$, with $\emptyset' = \emptyset$) gives $|\mathcal{Q}_{\le 2m-1}(M)| = \#\{\text{partitions of } M \text{ into parts } \le 2m-1\}$ for all $M \ge 0$, whose generating function in $\mathbb{Z}[[q]]$ is $\prod_{k=1}^{2m-1} (1 - q^k)^{-1}$.
   - Multiplying by $q^{2m^2}$ gives $\sum_{N \ge 1} |\mathcal{P}_m(N)| q^N = q^{2m^2} / \prod_{k=1}^{2m-1}(1 - q^k)$ for each $m \ge 1$.
   - Summing over $m = n + 1 \ge 1$ ($n \ge 0$) is a finite sum in every coefficient $[q^N]$ (since $2(n+1)^2 > N$ for all large $n$), rigorously establishing Peter Bala's conjectured generating function in $\mathbb{Z}[[q]]$.

Zero gaps, zero hidden hypotheses, zero edge-case failures.

---

## 3. Independent Verification & Novelty Status

- Re-ran independent checker script (pure Python `int` combinatorics and DP, zero floats, visually inspected all 85 lines):
  - Command: `.venv/bin/python -u targets/oeis-A237757/notes/check-check-3.py`
  - Result: exit code `0`, raw `PASS` (exact $q$-series expansion matches all 58 OEIS `A237757` `%S..%U` terms; exhaustive partition enumeration + explicit $\Phi_m \leftrightarrow \Psi_m$ bijection + Ferrers conjugation verified for $1 \le N \le 28$).
- Checked `watch/snapshots/zenodo-23112421-oeis-ids.md`: `0` hits for `A237757`.
- Gate 2 novelty PASS receipts present from `watch-1` (`#860`), `watch-5` (`#862`), and `watch-6` (`#863`).

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Handing off directly to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`).

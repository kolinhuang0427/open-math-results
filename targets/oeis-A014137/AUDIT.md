# Blind Audit: `targets/oeis-A014137/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (re-audit PASS after `#921` analytic convergence patch; Charter label: `"written proof, internally audited"`)
- **Audited Files:** `targets/oeis-A014137/TARGET.md`, `targets/oeis-A014137/PROOF.md`, `targets/oeis-A014137/notes/check-check-3.md`, `targets/oeis-A014137/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Source Checked:** Live OEIS JSON `https://oeis.org/search?q=id:A014137&fmt=json` (`rev. 180`, `2026-08-07`, offset `0,2`) and `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits).

---

## 1. Primary-Source Statement Fidelity & Formal Power Series Proof

- **Live OEIS `A014137`** (`rev. 180`, `2026-08-07T18:53:11-04:00`, offset `0,2`): Name (`Partial sums of Catalan numbers (A000108).`), 29 data terms (`a(0)..a(28)`), and Sergei N. Gladkovskii's May 14, 2013 `%F` continued fraction conjecture match `TARGET.md` verbatim. Zero hits in `watch/snapshots/zenodo-23112421-oeis-ids.md`.
- **Formal Power Series Proof (`PROOF.md` L5–48):**
  - Lemma 1 ($r_1(k) = (4k+1)/(k+1)$, $r_2(k) = 2(4k+3)/(2k+3)$) and Lemma 2 ($Q(k) = 1 + r_1(k)x + r_1(k)r_2(k)x^2 Q(k+1)$) are exact.
  - Bottom-up unit evaluation $D_2 = (2k+3)(1 + r_2 x q)/q \in \mathbb{Q}[[x]]^\times$, $D_1 = (k+1)/(1 + r_2 x q) \in \mathbb{Q}[[x]]^\times$, and $1 + (4k+1)x/D_1 = Q(k)$ are exact in $\mathbb{Q}[[x]]$.
  - Exact $x$-adic truncation discrepancy $Q^{(K)}(0) - Q(0) = C_{2K+2} x^{2K+2}(q_{K+1}^{(K)} - Q(K+1)) \in x^{2K+3}\mathbb{Q}[[x]]$ for any seed $q_{K+1}^{(K)} = 1 + O(x)$ is exact.
  - Independent verifier `.venv/bin/python -u targets/oeis-A014137/notes/check-check-3.py` ran cleanly (exit code `0`, raw `PASS`, zero floats).

---

## 2. Localized Analytic Convergence Gaps to Fix (`PROOF.md` L31, L47–49)

`PROOF.md` L3 and L31 claim analytic convergence of the finite continued-fraction truncations $Q^{(K)}(0)$ on $\{x \in \mathbb{C} : |x| < 1/4\}$, and L47–49 proves this via $Q^{(K)}(0) - Q(0) = C_{2K+2} x^{2K+2}(q_{K+1}^{(K)} - Q(K+1))$. Two concrete gaps remain in L47–49:
1. **Unbounded seeds (`PROOF.md` L47, L49):** L47 allows *any* seed $q_{K+1}^{(K)} = 1 + O(x)$ (which could grow faster than $(4\rho)^{-(2K+2)}$ in $K$, e.g. $q_{K+1}^{(K)} = 1 + 100^{2K} x$), yet L49 bounds only $|Q(K+1)| \le (1 - 4\rho)^{-1}$ without restricting the analytic convergence statement to the standard truncation $q_{K+1}^{(K)} = 1$ (or seeds uniformly bounded on compact subsets of $\{|x| < 1/4\}$), so that $|q_{K+1}^{(K)} - Q(K+1)|$ is uniformly bounded in $K$.
2. **Nonvanishing of analytic continued-fraction denominators (`PROOF.md` L45–49):** The rational simplification $T_k(q) = 1 + r_1(k)x + r_1(k)r_2(k)x^2 q$ requires that none of the intermediate analytic denominators $q_{k+1}^{(K)}(x)$, $D_2(x)$, or $D_1(x)$ vanish on $\{|x| < 1/4\}$ (so no $0/0$ removable singularity occurs when evaluating the continued fraction at $x \in \mathbb{C}$ with $|x| < 1/4$). For the standard truncation $q_{K+1}^{(K)} = 1$, this has a 2-line self-contained proof: every intermediate $q_{k+1}^{(K)}(x) = \sum_{n=0}^{2(K-k)} \frac{C_{n+2k+2}}{C_{2k+2}} x^n$ and $1 + r_2(k) x q_{k+1}^{(K)}(x) = \sum_{n=0}^{2(K-k)+1} \frac{C_{n+2k+1}}{C_{2k+1}} x^n$ has the form $p(x) = \sum_{n=0}^M b_n (4x)^n$ with $b_0 = 1 > b_1 > \dots > b_M > 0$ (since $\frac{C_{m+1}}{4 C_m} = \frac{2m+1}{2m+4} < 1$); hence for $|4x| < 1$,
   $$\bigl|(1 - 4x)p(x)\bigr| = \left|b_0 - \sum_{n=1}^{M}(b_{n-1}-b_n)(4x)^n - b_M(4x)^{M+1}\right| > b_0 - \sum_{n=1}^M (b_{n-1}-b_n) - b_M = 0,$$
   proving $q_{k+1}^{(K)}(x) \neq 0$ and $1 + r_2(k) x q_{k+1}^{(K)}(x) \neq 0$ (and likewise for the full series $Q(k+1)(x)$ and $1+r_2(k)x Q(k+1)(x)$ as $M\to\infty$), so $D_2(x), D_1(x) \neq 0$ throughout $\{|x| < 1/4\}$.

---

## 3. Handoff
Returned to `@scout-5` and `@triage` for this 2-sentence analytic precision patch in `PROOF.md` L31 & L47–49 (`check-check-3.py` already passes cleanly). Ping `@audit-3` once patched for instant PASS.

---

## 4. Re-Audit (`audit-3`, 2026-11-27, after `#921` patch) — **PASS**

Verified updated `targets/oeis-A014137/PROOF.md` (57 lines):
- **L31 & L51–57:** Both analytic convergence gaps from §2 are resolved cleanly and completely:
  1. Analytic uniform convergence on compact disks $|x| \le \rho < 1/4$ is explicitly stated for the standard truncation $q_{K+1}^{(K)} = 1$ (and uniformly bounded analytic seeds avoiding denominator zeros), yielding the explicit uniform bound $\frac{(4\rho)^{2K+2}}{2K+3}\bigl(1 + \frac{1}{1 - 4\rho}\bigr) \to 0$.
  2. Downward induction identifies $q_k^{(K)}(x) = \sum_{n=0}^{2(K-k+1)} \frac{C_{n+2k}}{C_{2k}} x^n$ and $1 + r_2(k)x\,q_{k+1}^{(K)}(x) = \sum_{n=0}^{2(K-k)+1} \frac{C_{n+2k+1}}{C_{2k+1}} x^n$, and the self-contained telescoping bound on $(1 - 4x) S_{m,M}(x)$ (with strictly decreasing $b_n = \frac{C_{n+m}}{4^n C_m}$, $b_{n+1}/b_n = \frac{4(n+m)+2}{4(n+m)+8} < 1$) proves $q_{k+1}^{(K)}(x) \ne 0$ and $1 + r_2(k)x\,q_{k+1}^{(K)}(x) \ne 0$, hence $D_2(x), D_1(x)$ are finite and nonzero everywhere on $\{|x| < 1/4\}$.
- **Independent Verifier (`check-check-3.py`):** Already executed on unmodified `check-check-3.py` (exit code `0`, raw `PASS`, zero floats).
- **Verdict:** **PASS** (`written proof, internally audited`). Handing off directly to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty verification (`<1h`).

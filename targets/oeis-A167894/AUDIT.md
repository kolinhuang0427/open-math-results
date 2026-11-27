# Blind Audit: `targets/oeis-A167894/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (re-audit PASS after `@scout-5` patched `PROOF.md` L27 per `#1046`; live OEIS `A167894` rev. 83 verbatim, `0` hits in Zenodo `23112421`/`23114921`, `check-check-3.py` zero-float `PASS`)
- **Audited Files:** `targets/oeis-A167894/TARGET.md`, `targets/oeis-A167894/PROOF.md`, `targets/oeis-A167894/notes/check-check-3.md`, `targets/oeis-A167894/notes/check-check-3.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON `https://oeis.org/search?q=id:A167894&fmt=json` (`rev. 83`, `2026-01-02`, offset `0,4`), `watch/snapshots/zenodo-23112421-oeis-ids.md` (`0` hits), and `zenodo-23114921-oeis-ids.md` (`0` hits).

---

## 1. Primary-Source Fidelity & Proof Verification

- Live OEIS `A167894` (`rev. 83`, offset `0,4`) matches `TARGET.md` verbatim (`Expansion of g.f.: 1/(Sum_{k >= 0} k!*x^k).`, Gladkovskii's Nov 19, 2013 `G.f.: conjecture: Q(0), where Q(k) = 1 + k*x - (k+1)*x/Q(k+1).`, 20 data terms).
- `PROOF.md` Lemma 1 ($P_{k-1}(x) = 1 + kx P_k(x)$), CF recurrence $Q(k) = P_{k-1}(x)/P_k(x) = 1 + kx - (k+1)x/Q(k+1)$ in $\mathbb{Z}[[x]]$, and contraction $T_k(q_1) - T_k(q_2) = (k+1)x(q_1-q_2)/(q_1 q_2)$ are all exact.
- `.venv/bin/python -u targets/oeis-A167894/notes/check-check-3.py` ran cleanly (exit code `0`, raw `PASS`, zero floats).

---

## 2. Required 1-Line Fix (`PROOF.md` L27)

- `PROOF.md` L27 writes: `if $q \in \mathbb{Z}[[x]]^\times$ (i.e., $q(0) \ne 0$)`.
- **Error:** Over $\mathbb{Z}$, a formal power series $q \in \mathbb{Z}[[x]]$ is a unit in $\mathbb{Z}[[x]]^\times$ if and only if **$q(0) = \pm 1$**, **not** $q(0) \ne 0$ (for example, $q = 2$ has $q(0) = 2 \ne 0$, yet $2 \notin \mathbb{Z}[[x]]^\times$ and $T_0(2) = 1 - x/2 \notin \mathbb{Z}[[x]]$).
- **Fix:** Replace `(i.e., $q(0) \ne 0$)` on L27 with `(i.e., $q(0) = \pm 1$)` (and optionally note that the same $x$-adic contraction holds in $\mathbb{Q}[[x]]^\times$ for any seed with $q(0) \ne 0$, matching `check-check-3.py`'s `q2 = 2 + x` check).

---

## 3. Handoff
Returned to `@scout-5` and `@triage` for this 1-line patch on `PROOF.md` L27 (`check-check-3.py` already passes). Ping `@audit-3` once patched for instant PASS.

---

## 4. Re-Audit After `#1046` Patch — **PASS**

- Verified patched `targets/oeis-A167894/PROOF.md` L27: now accurately states `if $q \in \mathbb{Z}[[x]]^\times$ (i.e., $q(0) = \pm 1$; more generally, over $\mathbb{Q}$, any $q \in \mathbb{Q}[[x]]^\times$ with $q(0) \ne 0$ also works), then $T_k(q)(0) = 1 \ne 0$, so $T_k(q) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ (respectively, $1 + x\mathbb{Q}[[x]] \subseteq \mathbb{Q}[[x]]^\times$) for every $k \ge 0$.`
- All mathematical claims, Lemma 1, CF recurrence, $x$-adic contraction, statement fidelity against live OEIS `A167894` (`rev. 83`), and `.venv/bin/python -u targets/oeis-A167894/notes/check-check-3.py` (exit `0`, raw `PASS`, zero floats) are verified.
- **Final Verdict: PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check.

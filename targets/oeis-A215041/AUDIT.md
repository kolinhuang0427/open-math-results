# Independent Blind Audit — `targets/oeis-A215041/`

- **Auditor:** `audit-2`
- **Verdict:** **FAIL** (1 localized sign error on `PROOF.md` L48; live OEIS verbatim fidelity, all core math, `check-check-2.py`, and Gate 2 novelty all **PASS** — instant PASS once L48 is patched!)
- **Audited UTC:** 2026-11-27T11:27Z
- **Files audited (blind — author `verify.py` and author scratch `notes/` not read):**
  - Primary source: Live OEIS JSON [A215041](https://oeis.org/A215041) (`rev. 10`, fetched directly `2026-11-27T11:26Z`) and `tools/.arxiv_cache/eprint/1210.1018.src` (`arXiv:1210.1018v2`)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A215041/TARGET.md)
  - [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A215041/PROOF.md)
  - [check-check-2.md](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A215041/notes/check-check-2.md) and [check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A215041/notes/check-check-2.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

## 1. Primary Source & Statement Fidelity — **PASS**

- Verified directly against live OEIS JSON `A215041` (`rev. 10`, `OFFSET: 1,2`, `55` terms): `NAME`, `DATA`, and `FORMULA` (`a(1) = 1. Conjectures for a(n), n>=2: i) a(2^k) = 2, k>=1; ii) a(p^k) = p^((p^(k-1)+1)/2), for odd prime p and k>=1; iii) a(n) = product(p^(delta(n)/(p-1)), odd p|n) otherwise.`) match `TARGET.md` and `PROOF.md` verbatim.
- Checked OEIS compendium/Lean snapshots: `0` matches in `watch/snapshots/zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, and `discovered/OtherMindset__congress-lean.json`; Gate 2 receipts `watch-{1,5,6}` all PASS.

## 2. Adversarial Mathematical Audit

- **Section 1 (L5–15, $\Phi_{2n}(z) = z^{\delta(n)} C(n, z+z^{-1})$):** **PASS.**
- **Section 2 (Lemma 1, L21–33, $|\mathrm{Disc}(\Phi_m)|$ via Möbius inversion + CRT surjectivity + $\Phi_k(1)$):** **PASS.** Completely self-contained and airtight.
- **Section 3 (Lemma 2, L39–52) — 1 LOCALIZED SIGN ERROR ON L48:**
  - **Defect (`PROOF.md` L48):** Writes
    $$\prod_{i=1}^d (\zeta_i - \zeta_i^{-1})(\zeta_i^{-1} - \zeta_i) = \prod_{i=1}^d -\bigl((\zeta_i + \zeta_i^{-1})^2 - 4\bigr) = (-1)^d \prod_{i=1}^d (4 - x_i^2) = \pm C(n, 2)\, C(n, -2).$$
  - The second equality is **literally false** for every odd $d$ (e.g., $n = 2, 3$ where $d = 1$): $-\bigl(x_i^2 - 4\bigr) = +(4 - x_i^2)$, NOT $-(4 - x_i^2)$, so there is **no** $(-1)^d$ factor in front of $\prod_{i=1}^d (4 - x_i^2)$! (The true equality is `= \prod_{i=1}^d (4 - x_i^2) = (-1)^d C(n, 2)\, C(n, -2)`.)
- **Section 3 (Lemma 3, L54–63) & Section 4 (L67–80):** **PASS.** Verified $\Phi_{2n}(-z) = \Phi_n(z)$ ($n$ odd $\ge 3$) and $\Phi_{2n}(-z) = \Phi_{2n}(z)$ ($4 \mid 2n$), cancellation of $2^{2d}$, $\mathrm{Disc}(C(n,x)) > 0$, and all three cases (i)–(iii).

## 3. Independent Mechanical Verification

- AST check of `targets/oeis-A215041/notes/check-check-2.py`: **`FLOAT_CONSTANTS: 0 []`**.
- Executed `.venv/bin/python -u targets/oeis-A215041/notes/check-check-2.py`: exit code `0`, `PASS` ($n = 1..60$, all 55 live OEIS terms, Lemmas 1–3).

## 4. Required Fix

Fix the sign on **`PROOF.md` L48** (`= \prod_{i=1}^d (4 - x_i^2) = (-1)^d C(n, 2)\, C(n, -2)`), then ping `@audit-2` for instant PASS!

---

## 5. Re-Audit Verdict (`audit-2`, `2026-11-27T11:29Z`) — **PASS**

Verified `@scout-6`'s fix on `targets/oeis-A215041/PROOF.md` L48 (`#1180`):
- L48 now reads `= \prod_{i=1}^d (4 - x_i^2) = (-1)^d C(n, 2)\, C(n, -2)` (exact since $C(n, 2) C(n, -2) = \prod_{i=1}^d (2 - x_i)(-2 - x_i) = (-1)^d \prod_{i=1}^d (4 - x_i^2)$).
- Also verified `0` matches for `A215041` in `watch/snapshots/cohen-zenodo-24384895-oeis-ids.md`, `zenodo-23112421-oeis-ids.md`, `zenodo-23114921-oeis-ids.md`, and `discovered/OtherMindset__congress-lean.json`, and verified verbatim match to `arXiv:1210.1018v2` (`ArXivngonGalois2017.tex` L540–555 & L928) as well as live OEIS `A215041` rev. 10.

**Final Audit Verdict:** **PASS.** Handing off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (including the newly discovered Zenodo `24366920` / `mylesparslow-collab` OEIS ledgers).

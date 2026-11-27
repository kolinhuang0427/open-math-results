# Contest Ruling (`audit-3`) — `targets/campbell-2509.16034-conj1/`

- **Ruling:** **PARTIALLY-RESOLVED-ELSEWHERE (RESCOPE REQUIRED)** — Three of Section 3's open problems (odd recurrence, eq. (11) `displayconjecture`, and non-$k$-automaticity) are already settled in `the-omega-institute/trureturing` (Sept 2026); the other **two** explicitly stated Section 3 open problems (explicit sign of $\rho(4n+2) - \rho(4n)$ when nonzero, and an explicit recursion for $\rho(4n)$ / full recursion) remain **genuinely open and uncontested**.
- **Auditor:** `audit-3` (strictly isolated; did not read `PROOF.md`, `verify.py`, or `notes/screen-*`)
- **Ruled at (UTC):** 2026-11-27 00:28 UTC
- **Sources inspected:** Primary source `arXiv:2509.16034v1` (`ReducedComplexityV85.tex` lines 655–700; *INTEGERS* 26 (2026), #A34), `TARGET.md`, `CONTESTED.md`, `notes/novelty-gate2-watch-6.md`, and `the-omega-institute/trureturing` files/commits via `notes/contest-helper-campbell.md`.

---

## 1. Item-by-Item Breakdown Against `arXiv:2509.16034v1` Section 3

| Section 3 Open Problem (`ReducedComplexityV85.tex` lines 676–699) | Status in `the-omega-institute/trureturing` (Sept 2026) | Ruling |
|---|---|---|
| (a) Odd recurrence $\rho(2n+1) = \rho(n+1)$ ($n \ge 0$) | **Settled & Lean 4 verified** (`ThueMorseReducedAbelianOdd.lean`, `sorry`-free, standard axioms) | **RESOLVED-ELSEWHERE** |
| (b) Eq. (11) `displayconjecture`: $\|\rho(4n+2) - \rho(4n)\| = 0$ if $\mathbf{t}_{n+1}=\mathbf{t}_{3n+1}$ else $1$ ($n > 0$) | **Settled & Lean 4 verified** (`ThueMorseReducedAbelianEven.lean`, commit `832f82f782`, 2026-09-08, `sorry`-free, standard axioms) | **RESOLVED-ELSEWHERE** |
| (d) Non-$k$-automaticity of $\rho(n)$ for all $k \ge 2$ | **Settled in prose** from frozen Lean lemmas via unboundedness $R(a_j+1) \ge j+1$ (commit `96baee8682`, 2026-09-14) | **RESOLVED-ELSEWHERE** |
| (c1) **Explicit sign** of $\rho(4n+2) - \rho(4n)$ in the nonzero case (lines 691–694) | **Explicitly unsettled / out of scope** (`Problems/campbell-currie-rampersad-eq-11.md`: *"The sign of `rho(4n+2) - rho(4n)` when nonzero, a recursion for `rho(4n)`, and the full recursion remain outside that result."*) | **OPEN / NOVEL** |
| (c2) **Explicit recursion for $\rho(4n)$** and full recursion for $\rho(n)$ (lines 680–682, 695–696) | **Explicitly unsettled / out of scope** (only coupled extrema recurrences `minAlt`/`maxAlt` are used internally; no recursion for $\rho(4n)$ or full recursion for $\rho(n)$) | **OPEN / NOVEL** |

*(No other competing proofs found across `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, arXiv, or web.)*

---

## 2. Required Action Before Audit

1. Under `CHARTER.md`, `targets/campbell-2509.16034-conj1/` **cannot** claim eq. (11) `displayconjecture`, the odd recurrence, or non-$k$-automaticity as new results.
2. `@scout2-4` (with `@triage` approval) should rescope `TARGET.md` and `PROOF.md` so the claimed new results are **strictly** the two open Section 3 problems — **(c1) explicit sign of $\rho(4n+2) - \rho(4n)$** and **(c2) explicit recursion for $\rho(4n)$ / full recursion for $\rho(n)$** — while explicitly crediting `the-omega-institute/trureturing` (Sept 2026, commits `832f82f782` & `96baee8682`) for prior settlement of (a), (b), and (d).
3. Once rescoped, `@check-1` should confirm the rescoped `PROOF.md` and verify exact formulas/recurrences before handing off to an auditor. (Note: `audit-3` remained strictly isolated from `PROOF.md`, `verify.py`, and `notes/screen-*`.)

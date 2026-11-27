# Adversarial Audit Report (`audit-3`) — `targets/daugherty-2610.29291-conj6.1/`

- **Verdict:** **PASS**
- **Charter label:** `"counterexample, verified by exact computation"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py` or author scratch `notes/screen-*` / `notes/search_box*.py`)
- **Audited at (UTC):** 2026-11-27 03:02 UTC (following re-audit verification of fixes to `COUNTEREXAMPLE.md` L24 & L36 and `TARGET.md` L25)
- **Files inspected:** `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, `notes/audit-helper-daugherty61.md`, and primary source `tools/.arxiv_cache/eprint/2610.29291/final.tex` + compiled `tools/.arxiv_cache/pdf/2610.29291.pdf` (`arXiv:2610.29291v1`).

---

## 1. Primary-Source Fidelity (`arXiv:2610.29291v1`, submitted 2026-10-21, sole/latest version)

- **Verbatim Conjecture 6.1 (`\label{conj:box}`, `final.tex` lines 717–719, PDF p. 12):**
  > If $\lambda$ and $\mu$ are wide partitions where $\lambda_i = \mu_i + 1$ for some $i \in [\ell(\lambda)-1]$ and $\lambda_j = \mu_j$ when $j \neq i$, then $LT(\lambda) \geq LT(\mu)$.
  Matches `TARGET.md` L20 and `COUNTEREXAMPLE.md` L9 verbatim.
- **Motivating pair in primary source:** `final.tex` line 721 explicitly cites adding a box to row $i = 5$ of $\mu = (6,5,5,3,2,1)$ to obtain the wide partition $\lambda = (6,5,5,3,3,1)$ ($n = 22 \to 23$, immediately beyond the authors' $n \le 22$ verification).
- **Definitions verified from `final.tex`:**
  - Definition 2.2 (lines 263–265): $\lambda$ is *wide* iff every subpartition $\nu \subseteq \lambda$ satisfies $\nu \succeq \nu'$.
  - Proposition 2.4 (lines 302–304): $\lambda$ is wide iff every lower subpartition (deleting rows $1, \dots, m$) satisfies $\nu \succeq \nu'$.
  - Definition 2.5 (lines 306–308): A Latin tableau of shape $\rho$ and type $\rho'$ has no repeated symbols in any row or column and multiplicity $\rho'_k$ of symbol $k$, which inductively forces row $r$ to be a permutation of $\{1, \dots, \rho_r\}$.
  - Compiled Section 5 numbering: `TARGET.md` L25 now accurately cites **Proposition 5.5** (`final.tex` lines 695–701) for top-row monotonicity ($i = 1$).

---

## 2. Adversarial Verification of `COUNTEREXAMPLE.md` & Independent Computation

1. **Line-by-line check of `COUNTEREXAMPLE.md` (after re-audit fixes):**
   - Main pair $\mu = (6,5,5,3,2,1) \to \lambda = (6,5,5,3,3,1)$: $\ell(\lambda) = 6$, $i = 5 \in \{1,2,3,4,5\} = [\ell(\lambda)-1]$, $\lambda_5 = \mu_5 + 1 = 3$, $\lambda_j = \mu_j$ for $j \neq 5$.
   - All lower-subpartition conjugates and partial sums in `COUNTEREXAMPLE.md` L19–27 verified exact (including patched L24: $(5,5,3,3,1)' = (5,4,4,2,2)$ with partial sums $(5,10,13,16,17) \ge (5,9,13,15,17)$). In addition, all $2^6 - 1 = 63$ nonempty subpartitions of both $\mu$ and $\lambda$ were directly checked to satisfy $\nu \succeq \nu'$.
   - Patched L36 intuition note accurately reflects $\lambda'_3 = 5$ vs $\mu'_3 = 4$ (all 32 valid tableaux of $\lambda$ have row 5 in $\{(2,1,3), (2,3,1), (3,1,2), (3,2,1)\}$, placing symbol $3$ in col 1 in 16 tableaux, col 2 in 8, and col 3 in 8).

2. **Independent Exact Computation (`notes/check-check-3.py` + `notes/audit-helper-daugherty61.md`):**
   - Independent verifier `targets/daugherty-2610.29291-conj6.1/notes/check-check-3.py` executed cleanly (`exit 0`, `28.83s`), verifying all paper sanity checks and all three counterexample pairs.
   - Independent cross-check via **both** direct Definition 2.5 tableau enumeration and Lemma 5.4 exact integer Ryser permanents ($r = 1$ and $r = 5$) confirmed:
     - **Main counterexample ($n = 22 \to 23$, $i = 5$):** $LT((6,5,5,3,2,1)) = 56 > 32 = LT((6,5,5,3,3,1))$.
     - **Additional counterexample 1 ($n = 22 \to 23$, $i = 5$):** $LT((6,6,4,3,2,1)) = 88 > 64 = LT((6,6,4,3,3,1))$ (both wide across all 63 subpartitions).
     - **Additional counterexample 2 ($n = 23 \to 24$, $i = 5$):** $LT((6,6,5,3,2,1)) = 2080 > 1984 = LT((6,6,5,3,3,1))$ (both wide across all 63 subpartitions).

---

## 3. Deep Novelty Check (Clear as of 2026-11-27 02:30 UTC; Pending Gate 3 Live Re-Check)

- No `CONTESTED.md`; `arXiv:2610.29291v1` is sole version; OpenAlex (`W7223232483`) has `cited_by_count = 0`; Zenodo & Crossref = 0 hits; web search = 0 refutations.
- Checked 413 local watch snapshots (`tools/novelty_grep.py`) and competing GitHub repositories (`the-omega-institute/trureturing*`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `aliromman/math`, `KnowledgeSense/math`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `1337isnot1337/solved-conjectures`, `openai/math`, plus global `gh search`):
  - `trureturing#20269/#20329`, `aftd-platform`, and `valyuAI/research` settle **Conjecture 6.3** only;
  - `trureturing#26377` tracks **Conjecture 6.2** only;
  - `aftd-platform`'s `LatinTableauxCountMonoThreeTwoOne.lean` proves only the positive $n = 6 \to 7$ case $LT((3,2,1)) \le LT((3,3,1))$.
  - Zero prior public refutations of Conjecture 6.1 (`conj:box`) or `(6,5,5,3,3,1)` found.

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (exact Charter label: `"counterexample, verified by exact computation"`).
- **Next step:** Requesting Gate 3 live pre-report novelty re-check before final report to `@coordinator`.

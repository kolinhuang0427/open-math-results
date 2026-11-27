# Contest Ruling: `targets/cassaigne-2602.21895-conjC4/`

- **Auditor:** `audit-2`
- **Ruled UTC:** `2026-11-27T08:09Z`
- **Target:** Dekking Conjecture $(C_4)$ as stated in Julien Cassaigne, Bastián Espinoza, Michel Rigo, and Manon Stipulanti, *"Symbols frequencies in the Thue--Morse word in base $3/2$ and related conjectures"*, `arXiv:2602.21895v1` (`2026-02-25`), Section 1.4 (`merge_version.tex` lines 493–495) and Section 7 (`lines 2090–2121`).
- **Contested By:** `CONTESTED.md` (`watch-3` Gate 3 check `#908`) citing `the-omega-institute/trureturing#24005` (`2026-10-30`, open) and `#29075` (`2026-11-11`, open).
- **Verdict:** **`STILL-OPEN`** *(for Conjecture $(C_4)$ as a whole — Part 2 reversal invariance $\mathrm{freq}(w) = \mathrm{freq}(w^R)$ [Dekking Journal Conjecture 9], complement invariance [Dekking Journal Conjecture 8], and explicit rationality $\mathrm{freq}(w) \in \mathbb{Q}$ are completely unaddressed by `trureturing#24005`/`#29075`; transparent credit required for `trureturing#24005`/`#29075`'s prior public 4-step Toeplitz-skeleton proof plan and unpushed/unmerged Lean 4 claim for Part 1 / Dekking Journal Conjecture 7 on $\mathbf{t}'$)*

---

## 1. Direct Inspection of Competing Sources

Directly inspected via read-only `gh api` (`repos/the-omega-institute/trureturing/issues/24005`, `/24005/comments`, `/24005/timeline`, `/29075`, `/29075/comments`, `/29075/timeline`, plus repo-wide issue/PR searches for `Dekking`, `2301.13563`, `A357448`, `2602.21895`, `ThueMorseBaseThreeHalvesFactorFrequency`, `op-dekking2301`):

1. **`the-omega-institute/trureturing#24005`** (`open`, created `2026-10-30T02:07:36Z`, `0` comments, no linked PR):
   - Targets **Dekking (2023, *JIS* 26, Art. 23.2.3, `arXiv:2301.13563v1`) Journal Conjecture 7** ONLY:
     > *"The frequencies $\mu[w]$ of the words $w$ occurring in $x_{3/2}$ exist. Two conjectured values: $\mu[00] = 1/10, \mu[01] = 4/10$."*
   - Its own Literature section explicitly distinguishes Dekking's Journal Conjecture 7 from Dekking's **Conjectures 8 and 9** (*"it labels the target Conjecture 7 on page 3 and labels the complement and reversal frequency corollaries Conjectures 8 and 9"*).
   - Its binding Lean `claim` proves ONLY: (i) canonical base-$3/2$ expansion uniqueness, (ii) existence of $\mu[w] \in \mathbb{R}$ for every nonempty finite binary word $w$ occurring in $x_{3/2} = \mathbf{t}'$, and (iii) $\mu[00] = 1/10$ and $\mu[01] = 4/10$.
   - The issue body publicly outlines a mathematically sound 4-step proof plan for that claim (using $3^k$-residue transfer + `2602.21895v1` Theorem 18 + Proposition 11's $(9,4)$-Toeplitz skeleton of $\Delta \mathbf{t}_{3/2}$ + safe-start cylinder approximation $|S_j|/(2p_j)$ with unsafe density $\beta_j \le (m-1)4^j/(3\cdot 9^j) \to 0$).
2. **`the-omega-institute/trureturing#29075`** (`open`, created `2026-11-11T00:58:12Z`, `0` comments):
   - Records that a Lean 4 formalization of `#24005`'s `result : claim` compiled cleanly with standard axioms on internal branch `lane/math/op-dekking2301` (`57dc5140f9b`), but explicitly states: *"The four-slot audit for this delivery is unfinished. The implementation stage does not produce a Lean report or push a head, so no DTR finding is claimed."*
   - Confirmed `lane/math/op-dekking2301` is NOT pushed publicly (HTTP 404), no PR exists, and `trureturing` has **zero** issues, PRs, or files targeting Dekking Journal Conjecture 8 (complement invariance), Dekking Journal Conjecture 9 (reversal invariance $\mu[w] = \mu[w^R]$), or rationality of factor frequencies.

---

## 2. Comparison Against Exact Statement of Conjecture $(C_4)$ (`arXiv:2602.21895v1`)

Conjecture $(C_4)$ of `arXiv:2602.21895v1` (`merge_version.tex` lines 493–495) states verbatim:
> $(C_4)$ *It is conjectured that frequencies of the words $w \in \mathcal{A}^*$ occurring in $\mathbf{t}'$ exist. It is also conjectured that $w$ and its reversal have the same frequency. Similar questions can also be asked for $\mathbf{t}_{3/2}$.*

| Component of Conjecture $(C_4)$ | Status in `trureturing#24005` / `#29075` | Status in `PROOF.md` |
|---|---|---|
| **Part 1 (Existence of $\mathrm{freq}_{\mathbf{t}'}(w)$ & `00`/`01` values; Dekking Conj 7)** | Public 4-step Toeplitz-skeleton proof outline in `#24005` (`2026-10-30`) + unpushed/unmerged Lean 4 completion announcement in `#29075` (`2026-11-11`); no public Lean code or merged PR. | Independently proved via direct desubstitution + diagonal contraction (Prop 1 + §4), giving explicit rational recursion for both $\mathbf{t}_{3/2}$ and $\mathbf{t}'$. |
| **Part 2 (Reversal invariance $\mathrm{freq}(w) = \mathrm{freq}(w^R)$ for all $w$; Dekking Conj 9)** | **NOT CLAIMED AND NOT PROVED** (explicitly excluded from `#24005` `claim`). | **Proved in full** for all $w \in \{0,1\}^*$ in both $\mathbf{t}_{3/2}$ and $\mathbf{t}'$ via involutions $\sigma(m)=3M+1-m$, $\tau(j)=2M-j$ (Prop 2 + §4). |
| **Complement invariance ($\mathrm{freq}(w) = \mathrm{freq}(\bar{w})$; Dekking Conj 8) & Rationality ($\mathrm{freq}(w) \in \mathbb{Q}$)** | **NOT CLAIMED AND NOT PROVED** (`#24005` Toeplitz skeleton gives $\mu[w] \in \mathbb{R}$ only, not rationality). | **Proved in full** for all $w \in \{0,1\}^*$ in both $\mathbf{t}_{3/2}$ and $\mathbf{t}'$. |

---

## 3. Ruling & Guidance for Reporting

- **Ruling:** **`STILL-OPEN`** for the exact statement of Conjecture $(C_4)$ of `arXiv:2602.21895v1`, because Part 2 (reversal symmetry $\mathrm{freq}(w) = \mathrm{freq}(w^R)$ for general finite words $w$, i.e. Dekking Conjecture 9) — as well as complement invariance (Dekking Conjecture 8) and rationality of all factor frequencies — has never been proved or claimed in `trureturing#24005`/`#29075` or anywhere else in public literature.
- **Required transparent attribution (if accepted into `RESULTS.md` upon resume):** Explicitly note that `the-omega-institute/trureturing#24005` (`2026-10-30`) publicly posted a 4-step Toeplitz-skeleton proof outline (and `#29075`, `2026-11-11`, announced an unpushed/unmerged Lean 4 proof) for Part 1 alone (existence of real factor frequencies in $\mathbf{t}'$ and $\mu[00]=1/10, \mu[01]=4/10$, i.e. Dekking Journal Conjecture 7), whereas `PROOF.md` settles the **full** Conjecture $(C_4)$ including Part 2 (reversal symmetry for all $w \in \{0,1\}^*$), complement symmetry, and explicit rationality for both $\mathbf{t}_{3/2}$ and $\mathbf{t}'$ via an independent desubstitution-contraction proof.

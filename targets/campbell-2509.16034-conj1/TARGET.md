# campbell-2509.16034-conj1

- **source**: arXiv:2509.16034v1 (John M. Campbell, James Currie, and Narad Rampersad, "Reduced complexities for sequences over finite alphabets", Section 3 Conclusion — rescoped per `notes/contest-ruling-audit-3.md` strictly to Open Problems (c1) explicit sign of $\rho(4n+2)-\rho(4n)$ and (c2) explicit recursion for $\rho(4n)$ / full recursion; published in *INTEGERS* 26 (2026), #A34)
- **status**: reported
- **owner**: scout2-4
- **updated**: 2026-11-27T05:52:00Z
- **identifiers**: 2509.16034, campbell-2509.16034-conj1, Campbell, Currie, Rampersad, reduced abelian complexity, Thue-Morse

## Exact Statement (Rescoped Scope per `notes/contest-ruling-audit-3.md`)

From `arXiv:2509.16034v1`, Section 3 ("Conclusion", lines 675–699 of `ReducedComplexityV85.tex`):

> Although it appears that
> $$\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(2n + 1) = \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(n + 1)$$
> for nonnegative integers $n$, the problem of determining a full recursion for $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(n)$ seems to be challenging.
> It appears that
> \begin{equation}\label{displayconjecture}
> \left| \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n+2) - \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n) \right| = \begin{cases} 0 & \text{if } \mathbf{t}_{n+1} = \mathbf{t}_{3n+1}, \\ 1 & \text{otherwise}, \end{cases}
> \end{equation}
> but it is unclear how the sign of $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n+2) - \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n)$ could be evaluated in an explicit way for the nonzero case, and we leave this as an open problem. Also, it is unclear as to how a suitable recursion could be determined for $\rho_{\mathbf{t}}^{\mathrm{ab},\mathrm{red}}(4n)$, and we leave this as an open problem. We also leave it as an open problem to prove \eqref{displayconjecture}. It also appears that the integer sequence in \eqref{numericalproblem} is not $k$-automatic, and we leave it as an open problem to prove this.

**Rescoped claimed problems (per `audit-3` contest ruling #515):**
- **(c1)** Explicit evaluation of the sign of $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n+2) - \rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n)$ in the nonzero case (lines 691–694).
- **(c2)** Explicit recursion for $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(4n)$ and full recursion for $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}(n)$ (lines 680–682, 695–696).

*(Prior-credit note: The odd recurrence, eq. (11) `displayconjecture`, and non-$k$-automaticity were previously settled in `the-omega-institute/trureturing` in Sept 2026 — commits `832f82f782` and `96baee8682` — and are NOT claimed as new results here.)*

Definitions from Section 1 (`arXiv:2509.16034v1`, lines 75–113):
- For a finite nonempty word $w$, $\mathrm{red}(w)$ replaces every maximal run $cc\cdots c$ of identical characters with $c$.
- $\rho_{\mathbf{x}}^{\mathrm{ab},\mathrm{red}}(n)$ counts the number of distinct length-$n$ factors of $\mathbf{x}$ up to the equivalence $v \sim w \iff \mathrm{red}(v)$ and $\mathrm{red}(w)$ have the same length and $\mathrm{red}(v)$ is a rearrangement of the characters of $\mathrm{red}(w)$.
- $\mathbf{t}$ is indexed starting at $n=1$: $\mathbf{t}_n$ is the number of $1$'s modulo $2$ in the base-$2$ expansion of $n-1$, so $\mathbf{t} = 0110100110010110\cdots$.

## Gate 1 Novelty Receipt

- **Checked UTC**: 2026-11-26T23:26:54Z
- **Local snapshot grep**: `.venv/bin/python tools/novelty_grep.py 2509.16034 "Reduced complexities" "ab, red" "ab,red"` -> 0 matches across `watch/snapshots/**`.
- **GitHub / live API checks**:
  - `1337isnot1337/solved-conjectures` `CONTENTS.md`: 0 matches for `campbell|currie|rampersad|2509.16034|reduced`.
  - `aliromman/math` tree: 0 matches.
  - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`): 0 matches.
- **Zenodo API (`zenodo.org/api/records`)**:
  - `"2509.16034"` -> 0 hits; `"reduced abelian complexity"` -> 0 hits; `"Reduced complexities for sequences"` -> 1 hit (the source paper itself).
- **Web search**: Confirms publication in *INTEGERS* 26 (2026), #A34; no subsequent paper found resolving the Section 3 open problems.
- **Not covered**: Private/unindexed repositories and papers published after Nov 2026.

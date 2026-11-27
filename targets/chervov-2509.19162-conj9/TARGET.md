# Target: chervov-2509.19162-conj9

- **source**: `arXiv:2509.19162v2` (*CayleyPy Growth: Efficient growth computations and hundreds of new conjectures on Cayley graphs (Brief version)*, A. Chervov, D. Fedoriaka, E. V. Konstantinova, A. Naumov, I. Kiselev, et al.), Subsection "Bounds on the diameters of unitriangular groups", Conjecture 9
- **status**: reported
- **owner**: `scout-12`
- **started**: `2026-11-27T01:31:37Z`
- **updated**: `2026-11-27T08:48:30Z`
- **identifiers**: `arXiv:2509.19162v2`, `Conjecture 9`, `OEIS A136184`, `U(n, Z/2Z)`

## Verbatim Conjecture Statement

From `tools/.arxiv_cache/eprint/2509.19162/mainv2.tex` (Subsection "Bounds on the diameters of unitriangular groups", lines 2203–2231):

Context (lines 2204–2206):
> J.~Ellenberg in \cite{ellenberg1993diameter}, and later jointly with J.~Tymoczko  \cite{ellenberg2005unipotent}, established that the diameters of $U(n,\mathbb{Z}/p\mathbb{Z})$, the unitriangular groups over prime fields, are within a constant factor of $np+n^2\log(p)$ ... Here the group is considered with respect to the generators $E\pm E_{i,i+1}$ (fundamental roots).

Conjecture 9 (lines 2229–2231, 9th `\begin{Conj}` environment in `mainv2.tex`):
> \begin{Conj}
> The diameter of $U(n,\mathbb{Z}/2\mathbb{Z})$ with respect to the fundamental root transvections is equal to the number of metacyclic groups of order $2^n$ (\href{https://oeis.org/A136184}{OEIS A136184}).  
> \end{Conj}

(Note: over $\mathbb{Z}/2\mathbb{Z}$, $E + E_{i,i+1} = E - E_{i,i+1}$ are involutions, so undirected and oriented Cayley graphs coincide.)

## Gate 1 Novelty Receipt

- **Checked at**: `2026-11-27T01:31:37Z` (initial check) and re-verified `2026-11-27T03:12:00Z`
- **Sources & snapshots checked**:
  1. Existing workspace `targets/`: no directory for `2509.19162-conj9` or `A136184` existed prior to claim.
  2. `tools/novelty_grep.py "2509.19162" "A136184" "metacyclic" "unitriangular"` across `watch/snapshots/**` (413/462 snapshot files at initial check; 462 files in swarm): 0 hits for `2509.19162`, `A136184`, or `metacyclic`; the 4 `unitriangular` hits (`1337-solved-conjectures` on `LOCAL_LAW.md` rank projection, `JamieLittle16__HessianConjecture4` on `UnitriangularBlock.lean`) are completely unrelated.
  3. `the-omega-institute/trureturing` repo tree (inspected prior to GitHub search 403 rate limit): `CayleyPyConjectureOneRefutation.lean` refutes Conjecture 1 (quasipolynomial diameter) and `NikolovSegal/TypeA/Unitriangular` addresses Nikolov–Segal width over large odd prime fields; 0 entries touching Conjecture 9, `U(n, Z/2Z)`, or `A136184`.
  4. `tools/arxiv_fetch.py abs 2509.19162` and `eprint 2509.19162`: latest version on arXiv is `[v2]`; `mainv2.tex` states Conjecture 9 without proof or disproof.
  5. `search_web` queries:
     - `"2509.19162" "A136184" OR "metacyclic" "unitriangular"` — returns `arXiv:2509.19162` and OEIS A136184/A007982; no refutation paper found.
     - `"diameter" "U(n, Z/2Z)" OR "U(n, F_2)" "metacyclic"` — no matching theorem or refutation found.
     - Ellenberg–Tymoczko (`arXiv:math/0510506`) proves `diam(U(n, F_p)) = Theta(n p + n^2 log p)` with an unspecified multiplicative constant and does not compare with `A136184`.
- **Not covered (flag for Gate 2)**:
  - Live `gh api "search/code..."` returned HTTP 403 rate-limit after `2026-11-26T23:30Z`; Gate 2 watchers should run live GitHub/competing-repo/OEIS checks.

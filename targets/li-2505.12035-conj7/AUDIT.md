# Adversarial Audit Report: `targets/li-2505.12035-conj7/`

- **Auditor:** `audit-1`
- **Date (UTC):** 2026-11-27T00:44Z
- **Verdict:** **`PASS`**
- **Charter Label:** `"counterexample, verified by exact computation"` (two explicit finite connected $3$-uniform hypergraphs on $n = 6$ and $n = 7$ vertices verified by exact integer computation and exhaustive Berge-cycle search). Note: per `CHARTER.md`, internal auditing and exact computation are not external peer review.
- **Independent Verifier:** `targets/li-2505.12035-conj7/notes/check-check-3.py` (authored by `check-3` strictly from `arXiv:2505.12035v1/main_arxiv.tex` and `COUNTEREXAMPLE.md`, independently audited and re-executed with exit code `0` and output `PASS`).

---

## 1. Isolation & Reviewed Inputs

Strictly following `CHARTER.md` isolation rules, this audit inspected **only**:
- Primary source (directly verified via `tools/arxiv_fetch.py` and `tools/.arxiv_cache/eprint/2505.12035/main_arxiv.tex`): `arXiv:2505.12035v1` (`2025-05-17T14:55:02Z`, sole version), Yupei Li, Linyuan Lu, Ruth Luo, *"An Ore-type theorem for $[3]$-graphs"*.
- `targets/li-2505.12035-conj7/TARGET.md`
- `targets/li-2505.12035-conj7/COUNTEREXAMPLE.md`
- `targets/li-2505.12035-conj7/notes/check-check-3.md` and `notes/check-check-3.py`
- Gate 2 novelty receipts (`notes/novelty-gate2-watch-{1,3,5,6}.md`), plus direct GitHub/web checks (including `rainwangphy/aftd-platform` and `valyuAI/research`).

The finder's `verify.py` was **not** read (and no author scratch notes exist in `notes/`).

---

## 2. Primary-Source Fidelity & Definition Audit

Verified word-for-word against `tools/.arxiv_cache/eprint/2505.12035/main_arxiv.tex` (Abstract lines 60–66, Section 1 lines 94–182, and end of paper lines 1100–1204):
- **Conjecture 7 (`\label{conj:ore}`, lines 155–156):**
  > Let $n \ge 6$, and let $\mathcal{H}$ be a $[3]$-graph on $n$ vertices such that every pair $u, v \in V(\mathcal{H})$ of non-adjacent vertices satisfies $d_{\partial\mathcal{H}}(u) + d_{\partial\mathcal{H}}(v) \ge n + 1$. Then $\mathcal{H}$ contains a Hamiltonian Berge cycle.
- **Definitions checked verbatim:**
  - $[3]$-graph: hypergraph whose edges are subsets of $V(\mathcal{H})$ of size in $\{1, 2, 3\}$ (lines 94–95, 153; line 153 notes focus is on $\{2,3\}$-uniform hypergraphs — both witnesses are simple, connected, $3$-uniform hypergraphs).
  - Adjacency and $2$-shadow $\partial\mathcal{H}$: $u, v$ are adjacent iff $d_{\mathcal{H}}(u, v) \ge 1$; $\partial\mathcal{H}$ is the simple $2$-uniform graph on $V(\mathcal{H})$ with $uv \in E(\partial\mathcal{H}) \iff d_{\mathcal{H}}(u, v) \ge 1$, and $d_{\partial\mathcal{H}}(u) = |N_{\mathcal{H}}(u)|$ (lines 101–103, 152, 206).
  - Hamiltonian Berge cycle: $n$ distinct vertices $v_1, \dots, v_n$ and $n$ distinct hyperedges $e_1, \dots, e_n \in E(\mathcal{H})$ with $\{v_i, v_{i+1}\} \subseteq e_i$ ($v_{n+1} \equiv v_1$) (lines 110–113).
- **No hidden hypotheses:** Checked the entire paper; Conjecture 7 carries no $|E(\mathcal{H})| \ge n$, covering, or large-$n$ assumption. Indeed, lines 166–168 explicitly justify the bound $n \ge 6$ via Lu–Wang's 5-vertex, 4-edge covering hypergraph (which fails precisely because $|E| = 4 < 5$), and lines 177–182 explain that for Theorem 8 ($d_0 = 65$), $6 \le n \le d_0 + 3$ forces $\mathcal{H}$ to be covering — an implication that breaks down at $n = 6, 7$ when $d_0$ is reduced to $1$ (or $2$).
- Zero quantifier, definition, or hypothesis drift between `main_arxiv.tex`, `TARGET.md`, `COUNTEREXAMPLE.md`, and `notes/check-check-3.py`.

---

## 3. Adversarial Audit of `COUNTEREXAMPLE.md`

### 3.1 Witness 1 ($n = 6$, $|E| = 5 < 6$)
- $V(\mathcal{H}_1) = \{0, 1, 2, 3, 4, 5\}$, $E(\mathcal{H}_1) = \{\{0,1,2\}, \{0,1,3\}, \{0,2,4\}, \{1,2,5\}, \{3,4,5\}\}$.
- **Admissibility:** $n = 6 \ge 6$; $5$ distinct $3$-element subsets of $V(\mathcal{H}_1)$; simple, connected, $3$-uniform (hence a $[3]$-graph with no singleton edges).
- **2-shadow & Ore condition:** The $5$ triples cover $12$ of the $\binom{6}{2} = 15$ pairs, missing exactly the perfect matching $\{05, 14, 23\}$. Hence $\partial\mathcal{H}_1 \cong K_{2,2,2}$ is $4$-regular, and every non-adjacent pair $(u, v) \in \{(0,5), (1,4), (2,3)\}$ satisfies
  $$d_{\partial\mathcal{H}_1}(u) + d_{\partial\mathcal{H}_1}(v) = 4 + 4 = 8 = n + 2 > n + 1 = 7.$$
  (This also refutes $d_0 = 2$ at $n = 6$.)
- **Non-Hamiltonicity:** A Hamiltonian Berge cycle on $6$ vertices requires $6$ pairwise distinct hyperedges, impossible since $|E(\mathcal{H}_1)| = 5 < 6$ (also verified by exhaustive search in `check-check-3.py`).

### 3.2 Witness 2 ($n = 7$, $|E| = 6 < 7$, linear $3$-uniform)
- $V(\mathcal{H}_2) = \{0, 1, 2, 3, 4, 5, 6\}$, $E(\mathcal{H}_2) = \{\{0,3,4\}, \{0,5,6\}, \{1,3,5\}, \{1,4,6\}, \{2,3,6\}, \{2,4,5\}\}$ (Fano plane $\mathrm{STS}(7)$ minus the line $\{0, 1, 2\}$).
- **Admissibility:** $n = 7 \ge 6$; $6$ distinct $3$-element edges; simple, connected, **linear** ($|e \cap e'| \le 1$ for all distinct $e, e'$), $3$-uniform.
- **2-shadow & Ore condition:** The $6$ triples cover $6 \times 3 = 18$ distinct pairs, missing precisely $\{01, 02, 12\}$. Thus $d_{\partial\mathcal{H}_2}(v) = 6$ for $v \in \{3,4,5,6\}$ and $d_{\partial\mathcal{H}_2}(v) = 4$ for $v \in \{0,1,2\}$. Every non-adjacent pair $(u, v) \in \{(0,1), (0,2), (1,2)\}$ satisfies
  $$d_{\partial\mathcal{H}_2}(u) + d_{\partial\mathcal{H}_2}(v) = 4 + 4 = 8 = n + 1.$$
- **Non-Hamiltonicity:** Requires $7$ pairwise distinct hyperedges, impossible since $|E(\mathcal{H}_2)| = 6 < 7$ (also verified by exhaustive search in `check-check-3.py`).

### 3.3 Independent Verifier Re-run
Re-executed `.venv/bin/python /Users/kev/Documents/open-math/targets/li-2505.12035-conj7/notes/check-check-3.py` (exit code `0`):
```text
Witness 1 PASS: n=6, |E|=5 < 6, shadow_degs=[4, 4, 4, 4, 4, 4], non_adj=[(0, 5), (1, 4), (2, 3)], min_non_adj_sum=8 >= 7, hamiltonian_berge_cycle=False
Witness 2 PASS: n=7, |E|=6 < 7, shadow_degs=[4, 4, 4, 6, 6, 6, 6], non_adj=[(0, 1), (0, 2), (1, 2)], min_non_adj_sum=8 >= 8, hamiltonian_berge_cycle=False
PASS
```

---

## 4. Novelty Assessment (Gate 3 Clear)

- `arXiv:2505.12035v1` (`2025-05-17`) remains the sole version on arXiv.
- Gate 2 receipts (`notes/novelty-gate2-watch-{1,3,5,6}.md`) all passed with no `CONTESTED.md`.
- Direct auditor GitHub checks confirmed 0 refutation hits in `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `facebookresearch/atlas-lean`, global GitHub PRs, and global GitHub code (`2505.12035`, `conj:ore`).
- **Gate 3 live pre-report re-check (all PASS, no `CONTESTED.md`; `watch-3` co-covered `watch-6` per board #644):**
  - `targets/li-2505.12035-conj7/notes/novelty-gate3-watch-1.md` (`2026-11-27T01:35:00Z`, PASS)
  - `targets/li-2505.12035-conj7/notes/novelty-gate3-watch-3.md` (`2026-11-27T02:34:54Z`, PASS — fresh live check across 413 snapshots, `1337`, `trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `aftd-platform`, `valyuAI/research`, `atlas-lean`, `JENW1N/complete-math-solutions`, and Zenodo)
  - `targets/li-2505.12035-conj7/notes/novelty-gate3-watch-5.md` (`2026-11-27T01:26:04Z`, PASS)

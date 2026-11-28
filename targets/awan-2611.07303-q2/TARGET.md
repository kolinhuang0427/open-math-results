---
source: https://arxiv.org/abs/2611.07303v2 (Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, "Gaps in the Most Frequent Sizes of Integer Sumsets", Section 5 "Additional Results and Future Work", Subsection 5.2 "Questions", Question 2 `\label{q:rate}`, lines 556–578)
status: reported
owner: scout-10
created: 2026-11-27T18:30:39Z
updated: 2026-11-27T18:43:00Z
identifiers: ["2611.07303", "2611.07303v2", "Awan", "Miller", "Senger", "q:rate", "B_h-set"]
---

# Awan et al. (2026) — Convergence, Limit $c_{h,k}$, and Monotonicity of Non-$B_h$ Density (`q:rate`)

- **Started:** 2026-11-27T18:30:39Z

## Exact Quoted Statement

From `sections/additional-results.tex` (`arXiv:2611.07303v2`), Section 5 (`Additional Results and Future Work`), Subsection 5.2 (`Questions`), Question 2 (`\label{q:rate}`, lines 556–578), with definitions from `sections/introduction.tex`, `sections/preliminary-lemmas.tex`, and `sections/additional-results.tex`:

- For $q \ge k \ge 3$ and $h \ge 2$, $\mathcal{B}_{h,k}(q) = \bigl\{A \in \binom{[q]}{k} : A \text{ is a } B_h\text{-set}\bigr\}$, where $A$ is a $B_h$-set if $|hA| = M_{h,k} = \binom{h+k-1}{k-1}$.
- $\mathcal{R}_{h,k} = \bigl\{\mathbf{d} \in \mathbb{Z}^k \setminus \{\mathbf{0}\} : \sum_{i=1}^k d_i = 0,\ w(\mathbf{d}) \le h,\ \gcd(|d_1|, \dots, |d_k|) = 1,\ d_{j(\mathbf{d})} > 0\bigr\}$, where $w(\mathbf{d}) = \sum_{i=1}^k \max\{d_i, 0\}$ and $j(\mathbf{d}) = \min\{i : d_i \neq 0\}$.

> **Question 2 (`\label{q:rate}`).**
> By Corollary~\ref{cor:proportion},
> \[
> q\left(1-\frac{\abs{\Bcal_{h,k}(q)}}{\binom qk}\right)
> \]
> is bounded above and below by positive constants. For $k=3$, it converges to $3\sum_{w=2}^h\varphi(w)/w$ by Remark~\ref{rem:k3-limit}. Does it converge for every $k\geq4$? If so, what is its limit $c_{h,k}$? Is it eventually monotone in $q$?
>
> For $(h,k)=(2,4)$, the only relations of weight at most $2$ that can hold when $a_1<a_2<a_3<a_4$ are
> \[
> 2a_2=a_1+a_3,\qquad 2a_3=a_2+a_4,\qquad 2a_2=a_1+a_4,\qquad 2a_3=a_1+a_4,\qquad a_1+a_4=a_2+a_3.
> \]
> The numbers of sets in $\binom{[q]}4$ satisfying them are asymptotic to $q^3/12$, $q^3/12$, $q^3/24$, $q^3/24$ and $q^3/12$, respectively, and only $O(q^2)$ sets satisfy two of them. Hence $c_{2,4}=24\cdot\frac13=8$.
>
> Can $c_{h,k}$ be expressed in general as a sum of normalized $(k-1)$-dimensional volumes of the sections
> \[
> \left\{
> \mathbf v\in\R^k:
> 0<v_1<\cdots<v_k<1,\
> \mathbf d\cdot\mathbf v=0
> \right\},
> \qquad \mathbf d\in\Rcal_{h,k}?
> \]

## Gate 1 Novelty Receipt

- **Checked UTC:** 2026-11-27T18:29:49Z
- `ls -d targets/*07303*`: no existing targets.
- `.venv/bin/python tools/novelty_grep.py "2611.07303" "q:rate" "Bcal_" "Gaps in the Most Frequent"`: `0` lines across `0/760` snapshot files.
- `gh search issues --repo the-omega-institute/trureturing "07303"` and `gh search issues "Gaps in the Most Frequent Sizes of Integer Sumsets"`: `0` relevant hits (`#29874` unrelated).
- `gh search code "2611.07303"`: returned `richfrem/Project_Sanctuary` (targeting `q:threshold` only) and `rainwangphy/aftd-platform` (formalizing Proposition 5.7, Definition 2.2, and Definition 3.1 of `2611.07303`); `0` code hits addressing `q:rate`.
- `gh search code "c_{h,k}"`: `0` relevant hits.
- Zenodo API (`https://zenodo.org/api/records?q=2611.07303&size=5`): `0` hits.
- `arXiv` API (`id_list=2611.07303`): `2611.07303v2` (`2026-11-09T14:48:06Z`) is the latest version.
- `search_web`: returned only `arXiv:2611.07303`.
- **Verdict:** Open (passes Gate 1).

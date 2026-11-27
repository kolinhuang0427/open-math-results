# yasutomi-2609.32450-conj6.1

- source: arXiv:2609.32450v2 (Shin-ichi Yasutomi, "On the Ordering and Injectivity of Lagrange Constants Associated with Certain Substitutions", Section 5, Conjecture 5.1)
- status: reported
- owner: scout2-4
- updated: 2026-11-27T09:44:40Z
- attack_started_utc: 2026-11-27T09:14:45Z
- identifiers: ["2609.32450", "Yasutomi", "Lagrange constants", "phi_{a,b}"]

## Exact Statement (from `lagrangev2.tex`, `arXiv:2609.32450v2`)

Lemma `l1` (Section 1, Lemma 1.4; proved in Section 2):
```latex
\begin{lem}\label{l1}
Let $x, y \in \mathbb{Q}$ such that $0 \le x < y \le 1$.
Let $\mathrm{den}(u)$ denote the denominator of a rational number $u$.
Then, the relation between $x$ and $y$ is classified into the following three types:
\begin{enumerate}
\item[\rm (1)] There exists a natural number $n$ such that $n < \min(\mathrm{den}(x), \mathrm{den}(y))$ and $\lfloor nx \rfloor < \lfloor ny \rfloor$.
\item[\rm (2)] $(x, y) = (0, 1)$, or $\mathrm{den}(x) < \mathrm{den}(y)$, and $\lfloor jx \rfloor = \lfloor jy \rfloor$ for all $1 \le j \le \mathrm{den}(x)$.
\item[\rm (3)] $\mathrm{den}(x) > \mathrm{den}(y)$, $\lfloor jx \rfloor = \lfloor jy \rfloor$ for all $1 \le j < \mathrm{den}(y)$, and $\lfloor jx \rfloor < \lfloor jy \rfloor$ for $j = \mathrm{den}(y)$.
\end{enumerate}
\end{lem}
```

Conjecture (Section 5, Conjecture 5.1):
```latex
\begin{con}
Let $a, b \in \mathbb{Z}_{>0}$ satisfy $1 \le a < b$, and let $x, y \in \mathbb{Q} \cap [0, 1]$ with $x < y$.

\begin{enumerate}
\item[\rm (I)] Suppose that $b < a^2 + 2$. Then the following hold:
\begin{enumerate}
\item[\rm (1)] If $(x, y)$ is of type (1) and $a \ge 2$, then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) < \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\item[\rm (2)] If $(x, y)$ is of type (2), then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) < \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\item[\rm (3)] If $(x, y)$ is of type (3) and $a \ge 2$, then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) > \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\end{enumerate}

\item[\rm (II)] Suppose that $b \ge a^2 + 2$. Then the following hold:
\begin{enumerate}
\item[\rm (1)] If $(x, y)$ is of type (1), then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) > \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\item[\rm (2)] If $(x, y)$ is of type (2), then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) < \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\item[\rm (3)] If $(x, y)$ is of type (3), then
\[
\mathcal{L}([\phi_{a,b}(G(x))]) > \mathcal{L}([\phi_{a,b}(G(y))]).
\]
\end{enumerate}
\end{enumerate}
\end{con}
```

## Gate 1 Novelty Receipt (2026-11-27T09:14:45Z)
- `tools/novelty_grep.py 2609.32450 Yasutomi "Lagrange constants"` -> 0 lines across 0/608 files.
- `gh search issues "2609.32450"` -> no issues matched; `gh search repos "2609.32450"` -> no repositories matched.
- `tools/arxiv_fetch.py query --id-list 2609.32450` -> `2609.32450v2` (published 2026-09-26, updated 2026-10-14).
- Web search for `"2609.32450" Yasutomi Lagrange constants` -> arXiv:2609.32450 primary paper only, no resolution or counterexample found.

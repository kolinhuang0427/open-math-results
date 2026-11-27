# Target: Ackelsberg--Richter (2026), Question 16.3 ("Finitary form of Kneser's theorem")

- **source**: Ethan Ackelsberg and Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*, arXiv:2604.12864v1 (`2026-04-14`, `math.NT`), Section 16.1 ("More on direct theorems for sumsets in the integers"), Question 16.3.
- **status**: reported
- **owner**: scout-10
- **created**: 2026-11-27T11:06:51Z
- **updated**: 2026-11-27T11:28:00Z
- **identifiers**: arXiv:2604.12864v1, Question 16.3

## Exact Quoted Statement

From `InverseProblemDensity_arXiv_v1.tex`, Section 1 (definitions) and Section 16.1 (Question 16.3, lines 5747--5757):

- Notation: $\mathbb{N} = \{1, 2, 3, \ldots\}$, $[N] = \{1, \ldots, N\}$, and $A + B = \{a + b : a \in A,\, b \in B\}$.

> **Question 16.3 (Finitary form of Kneser's theorem).** Is it true that for every $\varepsilon > 0$ and $N_0 \in \mathbb{N}$ there exist $D = D(\varepsilon, N_0) > 0$ and $N_1 = N_1(\varepsilon, N_0) \in \mathbb{N}$ such that the following holds: For any $\alpha, \beta > 0$, any $N \geq N_1$, and any sets $A, B \subset [N]$ such that
> \[
> \min_{N_0 < n \leq N} \frac{|A \cap [n]|}{n} \geq \alpha \qquad \text{and} \qquad \min_{N_0 < n \leq N} \frac{|B \cap [n]|}{n} \geq \beta,
> \]
> and $B$ intersects every residue class mod $D$, we have
> \[
> \frac{|(A + B) \cap [N]|}{N} \geq \alpha + \beta - \varepsilon.
> \]

## Gate 1 Novelty Receipt

- Checked at `2026-11-27T11:05:45Z`:
  - `ls -d targets/*2604.12864*`: only `targets/ackelsberg-2604.12864-ques16.4` existed (`ackelsberg-2604.12864-ques16.3` was unoccupied).
  - `.venv/bin/python tools/novelty_grep.py "Finitary form of Kneser" "Question 16.3" "2604.12864"`: 3 lines in `watch/snapshots/formal/formal-conjectures-prs.{json,tsv}` only for Question 16.9 (`EssentialComponent.lean`, PR #8236); zero hits for Question 16.3.
  - `gh search issues '"2604.12864" OR "Finitary form of Kneser"' --limit 15` and `gh search code '"2604.12864" OR "Finitary form of Kneser"' --limit 15`: no issues or code matched.
  - Zenodo API (`https://zenodo.org/api/records?q=2604.12864&size=5`): `0` hits.
  - arXiv API (`id_list=2604.12864`): latest version is `arXiv:2604.12864v1` (`2026-04-14T15:15:46Z`).
  - Web search (`"2604.12864" "Finitary form of Kneser" OR "Question 16.3" Ackelsberg Richter`): returned only the original preprint.

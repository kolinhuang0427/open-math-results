source: arXiv:2309.10950v2 (Theorem 1.7 / thm:VLM & Section 3.2 Remark 3.3; Canad. J. Math. 78 (2026), 594–618)
status: reported
owner: attack-4
updated: 2026-11-26T23:52:00Z
identifiers: 2309.10950, Yip, van Lint-MacWilliams, restricted sumsets, GPS(q,2), Paley sum graph

# Exact Statement (Primary Source)

From Chi Hoi Yip, *"Restricted sumsets in multiplicative subgroups"*, arXiv:2309.10950v2 [math.NT] (published in *Canad. J. Math.* 78 (2026), 594–618), Section 1 (`thm:VLM`) and Section 3.2 (Remark after `Proof of Theorem~\ref{thm:VLM}`, lines 405–407 of `main.tex`):

Context (`thm:VLM`, lines 105–107 of `main.tex`):
> **Theorem 1.7** (`thm:VLM`). Let $d \geq 3$. Let $q \equiv 1 \pmod d$ be an odd prime power and a square. If $A \subset \mathbb{F}_q$ such that $A\hat{+}A \subset S_d \cup \{0\}$, then $|A| \leq \sqrt{q}$, with the equality holds if and only if $d \mid (\sqrt{q}+1)$ and $A=\alpha \mathbb{F}_{\sqrt{q}}$, where $\alpha \in S_d$.

Here $S_d = \{x^d : x \in \mathbb{F}_q^*\}$ and $A \hat{+} A = \{a + b : a, b \in A, a \neq b\}$.

Verbatim Conjecture (Section 3.2, Remark, lines 405–407 of `main.tex`):
> **Remark.** Our analysis cannot handle the case $d=2$. In fact, there is $A \subset \mathbb{F}_9$ with size $4$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_9) \cup \{0\}$, and there are $15$ different $A \subset \mathbb{F}_{25}$ with size $5$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_{25}) \cup \{0\}$. Nevertheless, we conjecture that when $q$ is an odd square and $q \geq 49$, the statement of Theorem~\ref{thm:VLM} also extends to the case $d=2$.

(That is: for every odd prime power $q \ge 49$ that is a square, if $A \subset \mathbb{F}_q$ satisfies $A \hat{+} A \subset S_2 \cup \{0\}$, then $|A| \le \sqrt{q}$, with equality if and only if $A = \alpha \mathbb{F}_{\sqrt{q}}$ for some $\alpha \in S_2$ — note $2 \mid (\sqrt{q}+1)$ always holds for odd $\sqrt{q}$.)

# Gate 1 Novelty Receipt

- **Checked UTC:** 2026-11-26T20:37:20Z
- **Snapshots checked:** `tools/novelty_grep.py` across `watch/snapshots/**` (208 files) for `"2309.10950"`, `"Yip"`, `"Paley sum"`, `"GPS(q"`, `"van Lint"` — 28 lines across 11 files (Asgarli–Ghioca–Yip blocking-pencil, Yip on Erdős–Ingham, Yip's Cayley graph paper; 0 hits on `2309.10950` or van Lint–MacWilliams for $GPS(q, 2)$).
- **Exact arXiv query:** `.venv/bin/python tools/arxiv_fetch.py query 'au:Yip AND (all:"Paley" OR all:"van Lint" OR all:"restricted sumset") AND submittedDate:[202301010000 TO 202612312359]' --max-results 15` (13 hits, including `2608.02568v3`, `2607.25711v2`, `2503.19603v3`, `2405.09319v2`).
- **Inspected eprint:** `2608.02568v3` (Cochrane–Yip–Yoo, *Additive decompositions of multiplicative subgroups via differential identities*) — works strictly over **prime fields** $\mathbb{F}_p$ (not odd squares $\mathbb{F}_{p^{2r}}$) and has 0 hits for `van Lint`, `Paley sum`, or `GPS`.
- **Exact web search queries:**
  - `"2309.10950" OR ("Restricted sumsets in multiplicative subgroups" "Yip") OR ("Paley sum graph" "GPS(q,2)" OR "d=2")`
  - `"van Lint" "Paley sum" OR ("GPS(q,2)" OR "GPS(q, 2)" "clique") OR ("Yip" "Yoo" "restricted sumsets")`
- **Near misses:**
  - `arXiv:2608.02568v3` & `arXiv:2607.25711v2` classify $H = A \hat{+} A$ and $H \cup \{0\} = A \hat{+} A$ over prime fields $\mathbb{F}_p$ (not cliques of $GPS(q,2)$ for square $q$).
  - `arXiv:2503.19603v3` & `arXiv:2405.09319v2` study $f$-Diophantine sets and Paley-like quasi-random graphs, not equality cases $|A| = \sqrt{q}$ of $A \hat{+} A \subset S_2 \cup \{0\}$.
- **Not covered:** Unpublished works or papers not mentioning Yip, van Lint–MacWilliams, or Paley sum graphs.

# Adversarial Audit Report (`audit-3`) — `targets/biswas-2603.04876-conj5.5/`

- **Verdict:** **PASS**
- **Charter label:** `"written proof, internally audited"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py` or author scratch `notes/screen-*` / `notes/attack-*` / `notes/triage-brief.md`)
- **Audited at (UTC):** 2026-11-27 04:03 UTC
- **Files inspected:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, `notes/audit-helper-biswas.md`, and primary source `tools/.arxiv_cache/eprint/2603.04876/Arxiv.tex` (`arXiv:2603.04876v1`).

---

## 1. Primary-Source Fidelity (`arXiv:2603.04876v1`, 2026-03-05, sole/latest version)

Directly checked `tools/.arxiv_cache/eprint/2603.04876/Arxiv.tex`:
- **Conjecture 5.5 (`Arxiv.tex` L980–983, Section 5 *Future Directions*):**
  > For the class of connected chordal graphs on $n\geq 3$ vertices, we have
  > $$\mathcal{RV}_{\mathrm{chordal}}(n)=\left\{(r,v)\in \mathbb{N}^{2} \mid 1\leq r<\frac{n}{2}, 1\leq v\leq r-\left\lceil\frac{r}{n-2r}\right\rceil+1\right\}.$$
  Matches `TARGET.md` and `PROOF.md` verbatim.
- **Definitions & cited results verified 100% accurate:**
  - $\mathrm{reg}(G) := \mathrm{reg}(R/I(G))$ and $\mathrm{v}(G) := \mathrm{v}(I(G))$ (`Arxiv.tex` L249); $\mathbb{N} = \{1, 2, 3, \dots\}$ (and explicit $1 \le r, 1 \le v$ inequalities).
  - **Definition 2.4 (`Arxiv.tex` L303–307, citing Jaramillo–Villarreal 2021 Lemma 3.4 & Theorem 3.5):** $\mathrm{v}(G) = \min\{|A| : A \text{ independent and } N_G(A) \text{ is a vertex cover of } G\}$. *(Confirmed directly that whenever $A$ is independent and $N_G(A)$ is a vertex cover, $N_G(A)$ is automatically a **minimal** vertex cover — every $w \in N_G(A)$ has a neighbor $a \in A \subseteq V \setminus N_G(A)$, so $\{a, w\}$ is uncovered without $w$ — hence $(I(G):x_A) = \langle N_G(A) \rangle \in \mathrm{Ass}(R/I(G))$ with zero hidden caveats.)*
  - **Proposition 2.9 (`Arxiv.tex` L333–335):** $\mathrm{reg}(G) < n/2$ for connected $G$ on $n \ge 3$ vertices.
  - **Theorem 2.11 (`Arxiv.tex` L344–346, citing Hà–Van Tuyl 2008 Cor. 6.9):** $\mathrm{reg}(G) = \mathrm{im}(G)$ for every chordal graph $G$.
  - **Lemma 3.4 (`Arxiv.tex` L371–376)** and **Theorem 3.5 (`Arxiv.tex` L380–383, L975–978):** $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$.

---

## 2. Adversarial Line-by-Line Audit of `PROOF.md`

Every lemma, base case, boundary case, and algebraic step was audited independently:

1. **Lemma 1 (Dirac 1961, L35–42):** Checked disconnected $H$ ($S = \emptyset$ is vacuously a clique; $H_a = H[C_a]$ has $< n$ vertices) and connected non-complete $H$ (minimal separator $S$ is a clique; IH yields simplicial vertices in $C_a$ and $C_b$ which are nonadjacent). *(Non-blocking editorial remark: in L39, asserting $P_a, P_b$ are induced paths implicitly assumes $\{x, y\} \notin E(H)$, since if $\{x, y\} \in E(H)$ the claim $\{x, y\} \in E(H)$ already holds.)*
2. **Lemma 2 ($\mathrm{v}(H) \le \mathrm{im}(H)$ for arbitrary chordal $H$, L45–56):** Handles disconnected and edgeless graphs ($E(H) = \emptyset \implies A = \emptyset$, $|A| = 0 = \mathrm{im}(H)$); deleting isolated vertices yields nonempty $H_0$ with $\delta(H_0) \ge 1$; simplicial $s$ and neighbor $u \in N_H(s)$ satisfy $N_H[s] \subseteq N_H[u]$, so $M' \cup \{\{s, u\}\}$ is an induced matching of $H$, giving $\mathrm{im}(H - N_H[u]) \le \mathrm{im}(H) - 1$; $A = \{u\} \cup A'$ is independent and $N_H(A)$ covers all edges of $H$. **Airtight.**
3. **Lemma 3 (Clique tree of connected chordal $G$, L59–71):** Checked $n = 1$, connectedness of $G - s$ via shortcutting through simplicial $s$, exact characterization of $\mathcal{K}(G)$ in Case 1 ($N_G(s) = B_0$) and Case 2 ($N_G(s) \subsetneq B_0$), subtree connectivity (1), and nonempty edge intersection (2). **Airtight.**
4. **Lemma 4 (Greedy bottom-up clique cover & max induced matching, L74–93):** Checked $T_e = T_u \cup T_v$ nonempty connected subtree, unique $\mathrm{top}(T_e)$, termination (each $B_i$ deletes $\ge 1$ vertex of $e_i \in E(G_i)$), monotone depths $\mathrm{depth}(B_i) \ge \mathrm{depth}(B_j)$ ($i < j$), induced matching proof via ancestor path $B \to B_i \to B_j \implies B_i \in T_{e_j}$ contradicting $e_j \in E(G_j)$, converse $|M^*| \le k$ via clique-cover bound, and property (4) ($B_i = R \implies E(G_{i+1}) = \emptyset \implies i = r$). **Airtight.**
5. **Lemma 5 (Clique cover intersecting $X = V(G) \setminus V(M)$, L96–117):**
   - Root $R := N_G[s]$ is inclusion-maximal since $s$ is simplicial.
   - **Step A ($B_i \neq R$):** $z \in B_i \cap P(B_i)$ cannot lie in $e_i$ (else $P(B_i) \in T_{e_i}$ has smaller depth than $\mathrm{top}(T_{e_i})$) and cannot lie in $e_j$ ($j \neq i$) because $z$ is adjacent in clique $B_i$ to some $w \in e_i \cap B_i$ ($z \neq w$), violating induced matching of $M$. Thus $z \in B_i \cap X$. **Airtight.**
   - **Step B ($B_r = R$):** Subcase B1 ($R \cap X \neq \emptyset$) sets $C_r := R$. Subcase B2 ($R \cap X = \emptyset$) forces $R \subseteq V(M)$, hence $R \subseteq e_r$ (clique meets at most one edge of $M$), and $|R| = |N_G[s]| \ge 2$ (connected, $n \ge 3$) forces $R = e_r = \{u_r, v_r\}$ with $v_r = s$ a leaf ($\deg_G(v_r) = 1$), so every edge hitting $R$ contains $u_r$; connectedness and $n \ge 3$ give a neighbor $x \in N_G(u_r) \setminus \{v_r\}$, which cannot lie in any $e_j$ ($j \neq r$) by induced matching, hence $x \in X$, and $C_r := \{u_r, x\}$ is a clique hitting $X$ while preserving the vertex cover property. **Airtight.**
6. **Theorem 1 Part 1 (L122–145):** Checked $1 \le r < n/2$ ($m = n - 2r \ge 1$), pigeonhole over pairs $(i, x)$ with $1 \le i \le r, x \in C_i \cap X$ giving $x^* \in X$ in $t \ge \lceil r/m \rceil$ cliques $C_1, \dots, C_t \subseteq N_G[x^*]$, residual chordal graph $G' = G - N_G[x^*]$ covered by the $r - t$ cliques $C_{t+1} \cap V(G'), \dots, C_r \cap V(G')$ (including boundary $t = r \implies E(G') = \emptyset$, $\mathrm{im}(G') = 0$), yielding $\mathrm{im}(G') \le r - t \le r - \lceil r/(n-2r) \rceil$; applying Lemma 2 to (possibly disconnected/edgeless) $G'$ yields independent $A := \{x^*\} \cup A'$ with $N_G(A)$ a vertex cover and $\mathrm{v}(G) \le |A| \le r - \lceil r/(n-2r) \rceil + 1$. **Airtight.**
7. **Theorem 1 Part 2 (Reverse inclusion $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$, L148–168):** Checked all indices, edge counts, connectedness, chordality, $\mathrm{im}(G) = r$, and $\mathrm{v}(G) = v$ for both Case I ($m \ge r$) and Case II ($m < r$), including all boundary cases ($v = 1$, $v = r$, $m = 1$, $m = r$, $q = 1$, $q = m$). **Airtight.**
8. *(Minor non-blocking editorial remark on L174: "Saha–Sengupta witnesses $A$" echoes `Arxiv.tex` `[ss22]` without introducing the term in §§1–3; does not affect the self-contained proof.)*

---

## 3. Independent Computation & Deep Novelty Check

- **Independent verifier rerun (`notes/check-check-3.py`):** Exited `0` in `0.44s` (`real 0.44s`), confirming all 352 non-isomorphic connected chordal graphs on $n = 3..7$ ($\mathcal{RV}_{\mathrm{chordal}}(n) = A(n)$ exact), all 42 lattice points of $A(3..11)$, and 84 stress graphs on $n = 8..14$.
- **Independent adversarial script (`notes/audit-helper-biswas.md` §3.2):** Confirmed Lemma 5 Subcase B2 genuinely occurs **97 times across 78** of the 352 atlas graphs ($n = 3..7$) and **46 times** across 118 structured families ($n = 3..16$), passing every single Subcase B2 assertion in all 143 occurrences, plus 14 explicit Part 2 boundary points up to $n = 16$.
- **Deep novelty check (`notes/audit-helper-biswas.md` §2):** `2603.04876v1` is sole version; OpenAlex (`W7134037417`) has `cited_by_count = 0`; checked all 2025–2026 works of Biswas, Mandal, and Saha, arXiv (`"v-number"`, `"chordal"`, `"regularity"`, `"induced matching"`), Crossref, Zenodo, web search, 470 local watch snapshots, all 19 `the-omega-institute` repos, `1337isnot1337/solved-conjectures`, and 14 other competing GitHub repos (`aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `openai/math`). **Zero prior proofs or settlements found.**

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (exact Charter label: `"written proof, internally audited"`).
- **Next step:** Requesting Gate 3 live pre-report novelty re-check before final report to `@coordinator`.

# Independent Blind Audit — `targets/teheux-2611.12469-q3/`

- **Auditor:** `@audit-2` (blind Pro adversarial audit; author `verify.py` and author scratch `notes/` not read)
- **Audited UTC:** `2026-11-27T14:22Z`
- **Verdict:** **PASS** (`written proof, internally audited`)
- **Files audited:**
  - Primary source: `tools/.arxiv_cache/eprint/2611.12469v1/Notes_definability_pocset.tex` (`arXiv:2611.12469v1`, Bruno Teheux, *Dualities and completions of median algebras and semilattices: a universal-algebraic approach*, 2026-11-09)
  - [TARGET.md](file:///Users/kolinhuang/Documents/open-math/targets/teheux-2611.12469-q3/TARGET.md)
  - [PROOF.md](file:///Users/kolinhuang/Documents/open-math/targets/teheux-2611.12469-q3/PROOF.md)
  - [check-check-3.md](file:///Users/kolinhuang/Documents/open-math/targets/teheux-2611.12469-q3/notes/check-check-3.md) and [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/teheux-2611.12469-q3/notes/check-check-3.py)
  - Gate 2 receipts: `notes/novelty-gate2-watch-{1,5,6}.md`

---

## 1. Statement & Primary-Source Fidelity

Verified verbatim against `tools/.arxiv_cache/eprint/2611.12469v1/Notes_definability_pocset.tex` (shared counter `\newtheorem{theorem}{Theorem}[section]` L8–20 across 8 numbered sections):
- **Section 8, Question 8.4 (`\label{q:correspondence}`, L3066–3085), item (3) (L3077–3079):**
  > *Does every universal sentence that holds in a median algebra $\mathbf{A}$ hold in $\hat{\mathbf{A}}$, that is, does every finite subalgebra of $\hat{\mathbf{A}}$ embed into $\mathbf{A}$?*
  Matches `TARGET.md` and `PROOF.md` verbatim.
- **All internal citations verified exact:**
  - `Definition 2.1` (`def:median`, L231), `Definition 2.2` (`def:convex`, L264), `Theorem 2.4` (`prop:med-axioms`, L314 + local finiteness L323–330), `Definition 2.5` (`def:poc`, L344) & bounded strongly complemented Priestley spaces (L651–654), `Theorem 3.4(1)` (`thm:dualities`, L777 strong duality $\mathsf{M} \leftrightarrow \mathsf{Poc}_\tau$), `Corollary 4.6` (`prop:profinite`, L1395 $\hat{\mathbf{A}} \cong (\mathbf{A}^+)_+$), `Section 7` rank definition (L2609–2612), `Lemma 7.1` (`lem:cube-lift`, L2618), `Example 7.2` (`ex:rho-k`, L2681), `Corollary 7.6` (`cor:rank-transfer`, L2799), and `Example 8.1` (`ex:rho-k-correspondent`, L2930).
- **Gate 2 novelty receipts (`watch-1`, `watch-5`, `watch-6`):** All three **PASS** (`arXiv:2611.12469v1` sole version, `0/721` snapshot settlement hits, `trureturing#29092` verified explicitly scoped to Question 8.4(2) `ST(\sigma)` only, `dev` tree/Zenodo/GitHub/web clear).

---

## 2. Adversarial Line-by-Line Mathematical Audit (`PROOF.md`)

Checked every definition, quantifier, topological closure/compactness argument, and edge case:
1. **Equivalence (L42):** Local finiteness of $\mathsf{M}$ (`Theorem 2.4`, L323–330) ensures any refuting tuple $(u_1, \dots, u_n)$ of a universal $L_{\mathsf{M}}$-sentence generates a finite subalgebra $\mathbf{B} \le \hat{\mathbf{A}}$ (and for $n = 0$, $L_{\mathsf{M}} = \{m\}$ has no closed terms so quantifier-free sentences are trivial); conversely, applying transfer to the universal sentences $\varphi_{\mathbf{B}}$ (`Example 7.2`) yields finite-subalgebra embeddability. Exact.
2. **Base case & Case 1 ($\mathrm{rank}(\mathbf{A}) = \infty$, L48–51):** $|A| = 1 \implies \hat{\mathbf{A}} \cong \mathbf{A}$. For $\mathrm{rank}(\mathbf{A}) = \infty$, `Theorem 2.4` gives $\mathbf{B} \hookrightarrow \mathbf{2}^d$ ($d = |\mathsf{M}(\mathbf{B}, \mathbf{2})| < \infty$), $0$-padding embeds $\mathbf{2}^d \hookrightarrow \mathbf{2}^n$ ($n \ge d$) preserving coordinatewise median ($m(0,0,0)=0$), and infinite rank embeds $\mathbf{2}^n \hookrightarrow \mathbf{A}$. Airtight.
3. **Lemma 1 (Transversality bound, L56–62):** Pairwise transversality of $x_1, \dots, x_k \in \mathbf{X} \setminus \{0, 1\}$ is equivalent to all four intersections $x_i^{\pm} \cap x_j^{\pm}$ being nonempty. Helly's property for convex sets in a median algebra (proved by clean induction using $m(a,b,c)$) makes $\psi(a) = (x_1(a), \dots, x_k(a)) \colon \mathbf{A} \to \mathbf{2}^k$ surjective (checked for $k = 1$ as well), so `Lemma 7.1` gives $k \le r$. Airtight.
4. **Lemma 2 (Finite boundary $|A_U \setminus \{0\}| \le r$, L68–92):** Verified $(A_U)^\bullet = B_U$ via homeomorphism ${}^\bullet$ and $U^\bullet = U^c$. In the contradiction proof from $z_1, \dots, z_{r+1} \in A_U \setminus \{0\} \subseteq X \setminus \{0, 1\}$ ordered by linear extension ($h < i \implies z_i \not\le z_h$), every factor of $O_i$ is open ($X$ is compact Hausdorff with closed order $\le$ and homeomorphism ${}^\bullet$, and $y \in (X \setminus z_j^\downarrow)^\bullet \iff y^\bullet \not\le z_j$), every membership condition for $z_i \in O_i$ is verified, and picking $x_i \in O_i \cap U$ preserves all inductive hypotheses and forces all four transversality conditions $x_h \not\le x_i$, $x_i \not\le x_h$, $x_h^\bullet \not\le x_i$, $x_h \not\le x_i^\bullet$ for $h < i$, contradicting Lemma 1. Airtight.
5. **Lemma 3 (Local upward cone at boundary points, L96–112):** $t = 0$ is trivial ($W_{0, U} = X$). For $t \in A_U \setminus \{0\}$, assuming every open neighborhood of $t$ meets $U \setminus t^\uparrow$ builds $y_1, \dots, y_{r+1} \in (U \setminus t^\uparrow) \setminus \{0, 1\}$ via open $O_k \ni t$ (using $t^\bullet \in U \implies t^\bullet \not\le t$, $y_i \in U \implies y_i \not\le t$, IH $y_i^\bullet \not\le t$, and $y_i \notin t^\uparrow \implies t \not\le y_i$), yielding $r + 1$ pairwise transverse elements in $X \setminus \{0, 1\}$, contradicting Lemma 1. Airtight.
6. **Step 0 (Symmetric initial separation, L120–131):** $T = \{0, 1\} \cup W \cup \bigcup_{U \in \mathbf{B}} (A_U \cup B_U)$ is finite and ${}^\bullet$-closed. The symmetric definition of $D_t^{(0)}$ (intersecting over both $s \not\le t$ and $t^\bullet \not\le u$) guarantees $t \in D_t^{(0)}$, $s \in E_s^{(0)}$, and $E_s^{(0)} \cap D_t^{(0)} \subseteq C_{s, t} \cap C_{s, t}^c = \emptyset$ whenever $s \not\le t$, giving pairwise disjoint $N_t^{(0)} = D_t^{(0)} \cap E_t^{(0)}$ and $D_1^{(0)} = E_0^{(0)} = X$. Airtight.
7. **Step 1 (Inductive bottom-up $D_t$, L135–146):** Along a linear extension $t_1, \dots, t_m$ of $(T, \le)$, for every $U \in \mathbf{B}$ with $t \notin U$, any $z \in t^\downarrow \cap \overline{U}$ satisfies $z \notin U$ (since $U$ is an up-set), hence $z \in A_U \subseteq T$, placing $z$ in $W_{t, U}$ if $z = t$ or $D_z \cap W_{z, U}$ if $z < t$, so $t^\downarrow \cap \overline{U} \subseteq \Omega_{t, U}$ (verified at $t = 0$ both when $0 \in A_U$ and $0 \notin A_U$, and at $t = 1$ where $F_1 = \emptyset$). Compactness of $F_t$ plus pointwise clopen separation ($t^\downarrow = \bigcap \{H \ni t \text{ clopen down-set}\}$) yields clopen down-set $D_t \subseteq D_t^{(0)}$ with $t \in D_t$ and $D_t \cap F_t = \emptyset$. Airtight.
8. **Step 2 (Claims (I) & (II), L150–167):** Putting $E_s := (D_{s^\bullet})^\bullet$ and $N_s := D_s \cap E_s$ gives $(N_s)^\bullet = N_{s^\bullet}$ and pairwise disjointness. For $x \in D_t \cap U$ ($t \notin U$), $D_t \cap F_t = \emptyset$ forces $x \in \Omega_{t, U} \cap U$; Lemma 3 gives $x \in t^\uparrow \subseteq E_t$ (so $x \in N_t$) or $x \in D_r \cap r^\uparrow \subseteq D_r \cap E_r = N_r$ for some $r < t$ in $A_U$ (Claim (I)). Involution immediately yields Claim (II) ($E_s \cap U^c \subseteq \bigcup_{q \in T} N_q$ for $s \in U$). Airtight.
9. **Step 3 (Clopen retraction $\pi$ and embedding $\mathbf{B} \hookrightarrow \mathbf{A}$, L170–188):** $\pi$ commutes with ${}^\bullet$ and fixes $T$. For each $U \in \mathbf{B}$, $\widetilde{U} = \pi^{-1}(U) = (U \cap K) \cup \bigcup_{t \in T \cap U} N_t$ is clopen (since $A_U, B_U \subseteq T \subseteq X \setminus K$ implies $\overline{U \cap K} = U \cap K = \mathrm{int}(U) \cap K$), satisfies $0 \notin \widetilde{U}$, $1 \in \widetilde{U}$, $\widetilde{U}^\bullet = \widetilde{U}^c$, and all four up-set cases $(K,K), (N_s,N_t), (N_s,K), (K,N_t)$ hold via Step 0(2) and Claims (I)–(II). Strong duality (`Theorem 3.4(1)`) maps $\widetilde{U} \mapsto a_U \in \mathbf{A}$; set-theoretic preimage preserves the median operation, and witness points $W \subseteq T$ guarantee injectivity. Airtight.
10. **Remark (L192–194):** Verified the infinite zig-zag Priestley space $P = (\mathbb{N} \cup \{\infty\}) \times \{0, 1\}$ has a nontrivial complemented pair in $\mathcal{U}(P)$ but none in $\mathrm{ClopUp}(P)$.

Zero gaps, edge-case errors, or hidden assumptions found.

---

## 3. Independent Verifier Audit (`notes/check-check-3.py`)

- **AST float audit:** `FLOAT_CONSTANTS: 0 []`, `FLOAT_CALLS: 0 []`.
- **Execution:** Re-ran `.venv/bin/python -u targets/teheux-2611.12469-q3/notes/check-check-3.py` -> exit code `0`, `PASS`:
  - Part 1: Finite median/poc duality, Helly property, Lemma 1, and Remark 7.5 verified.
  - Part 2: Constructive execution of Lemmas 2–3 and Steps 0–3 on the infinite rank-2 Stone poc set $X_2 = A_2^*$ with comparable boundary points $r < t$ in $A_U$ ($|A_U \setminus \{0\}| = 2 = \mathrm{rank}(A_2)$) and explicit median embeddings $\mathbf{B} \hookrightarrow A_2$ (`|B| = 1, 2, 5`).
  - Part 3: Explicit $0 \in A_U$ boundary test on $\omega^*$.
  - Part 4: Remark Priestley space counterexample verified.

---

## 4. Verdict

**PASS** (`written proof, internally audited`). Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

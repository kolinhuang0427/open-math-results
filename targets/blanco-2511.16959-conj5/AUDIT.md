# Adversarial Audit Report: `targets/blanco-2511.16959-conj5/`

- **Auditor:** `audit-1`
- **Verdict:** **PASS**
- **Charter Label:** `"written proof, internally audited"`
- **Gate 3 Status:** Gate 3 Clear (`notes/novelty-gate3-watch-{1,5,6}.md`, all PASS; no `CONTESTED.md`)

---

## 1. Strict Isolation Record

Inspected ONLY:
- Primary source: `arXiv:2511.16959v3` (Saúl A. Blanco, Mikhail P. Golubyatnikov, Elena V. Konstantinova, Natalia V. Maslova, and Luka A. Nikiforov, *"Generating the symmetric group by three prefix reversals"*, *Discrete Mathematics & Theoretical Computer Science* **28:1**, Permutation Patterns 2025 (2026), Paper #7, DOI `10.46298/dmtcs.16975`), verified directly in `tools/.arxiv_cache/eprint/2511.16959/Final-DMTCS-Format.tex` (lines 133–164, 240–265, 835–1010) and confirmed latest (`v3`, `2026-09-22`) via `tools/arxiv_fetch.py`.
- Follow-up citation: `arXiv:2610.30892v1` (Yexiao Lei, Jinxing Zhao, Ziyu Zhu, and Yang Wu, *"On the generation of the symmetric group by index relations of three prefix reversals"*, `2026-10-22`), inspected directly in `tools/.arxiv_cache/eprint/2610.30892/main.tex` (lines 1–275, 730–850).
- `targets/blanco-2511.16959-conj5/TARGET.md`
- `targets/blanco-2511.16959-conj5/PROOF.md`
- `targets/blanco-2511.16959-conj5/notes/check-check-2.md`
- `targets/blanco-2511.16959-conj5/notes/check-check-2.py`
- Novelty receipts: `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-2.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md` (and confirmed absence of `CONTESTED.md`).

Did **not** inspect `verify.py` or any author scratch `notes/` (`notes/screen-*`, `notes/attack-*`, `notes/triage-brief.md`, etc.).

---

## 2. Primary-Source Statement Fidelity

- **Prefix reversal definition (`Final-DMTCS-Format.tex` lines 135–143, 250):** On $\Omega = \{1, \ldots, n\}$ with right-to-left composition $(\sigma\pi)(x) = \sigma(\pi(x))$, prefix reversals are the $n-1$ involutions $r_i$ for $1 < i \le n$ reversing $\{1, \ldots, i\}$ and fixing $\{i+1, \ldots, n\}$, decomposing as $\lfloor i/2 \rfloor$ disjoint transpositions. Hence the parameter domain of $k$ in $F_k(n)$ is all integers $k \ge 2$.
- **Conjecture numbering & exact text (`Final-DMTCS-Format.tex` lines 948–960):** Four conjectures precede `\begin{conjecture}\label{con:F_k(n)}`, confirming Conjecture 5 verbatim:
  $$F_k(n) = \{m : k < m < n,\ \langle r_n, r_m, r_k \rangle = \mathrm{Sym}_n\}, \qquad \max_{n > k+1} |F_k(n)| = \begin{cases} k + 1, & k \text{ even}, \\ \frac{k + 1}{2}, & k \text{ odd}. \end{cases}$$
- **Match:** `TARGET.md` and `PROOF.md` match the primary source verbatim with zero quantifier, domain, or convention drift.

---

## 3. Adversarial Line-by-Line Mathematical Audit

### Section 1: Upper Bound (Propositions 1.1 & 1.2)
- **Proposition 1.1 (self-contained proof of Conjecture 4):**
  - The $2$-cycle matchings $E_m, E_k$ on $\Omega$ are disjoint because equal pairs would force $m + 1 = k + 1$, contradicting $k < m$.
  - Acyclicity of $H = (\Omega, E_m \cup E_k)$: any simple cycle must have even length $2\ell \ge 4$ alternating $E_k, E_m$, giving $v_{2j+2} = m + 1 - (k + 1 - v_{2j}) = v_{2j} + (m - k)$, hence $v_{2\ell} = v_0 + \ell(m - k) > v_0$, contradiction. Thus $H$ is a forest with $c(H) = n - \lfloor m/2 \rfloor - \lfloor k/2 \rfloor$ components.
  - Quotient multigraph $Q$ on $\pi_0(H)$ with $|E(Q)| = \lfloor n/2 \rfloor$ edges from $E_n$: $r_m, r_k$ preserve each component of $H$, and $r_n$ moves elements only along $E_n$, so transitivity of $G$ requires $Q$ to be connected.
  - **Case 1 ($n = 2t + 1$ odd, $m + k < n - 1$):** Since $2 \le k < m < n$, odd $n \ge 5$ so $t \ge 2$. Also $\lfloor m/2 \rfloor + \lfloor k/2 \rfloor \le \lfloor (m+k)/2 \rfloor \le t - 1$, giving $|V(Q)| \ge t + 2 = |E(Q)| + 2$, so $Q$ is disconnected and $G$ is intransitive.
  - **Case 2 ($n = 2t$ even, $m + k < n$):** $n \ge 4$ so $t \ge 2$. Either $|V(Q)| \ge t + 2$ or $Q$ is disconnected (intransitive), or $Q$ is a connected multigraph with $|V(Q)| = t + 1 = |E(Q)| + 1$, hence a simple tree and bipartite with nonempty parts $\mathcal{A} \sqcup \mathcal{B}$. Lifting to $A \sqcup B = \Omega$, $r_m, r_k$ stabilize $A, B$ while fixed-point-free $r_n$ swaps $A \leftrightarrow B$, forcing $|A| = |B| = t$ and $|G| \le 2(t!)^2 < (2t)!$ since $\binom{2t}{t} \ge \binom{4}{2} = 6 > 2$ for all $t \ge 2$.
- **Proposition 1.2:**
  - Even $k$: Prop 1.1 bounds $m \in [n-k, n-1]$ ($k$ values) for even $n$ and $m \in [n-k-1, n-1]$ ($k+1$ values) for odd $n$, so $|F_k(n)| \le k + 1$ for all $n > k + 1$.
  - Odd $k \ge 3$: If $m \in F_k(n)$ were odd, $r_k$ and $r_m$ preserve odd/even positions $O \sqcup E$; for odd $n \ge 5$, $r_n$ also preserves $O, E$ (intransitive); for even $n \ge 6$, $r_n$ swaps $O \leftrightarrow E$ with $|O|=|E|=n/2 \ge 3$, giving $|G| \le 2((n/2)!)^2 < n!$. Thus every $m \in F_k(n)$ is even. Intersecting with Prop 1.1 gives at most $(k+1)/2$ even values in $[n-k-1, n-1]$ for odd $n$ ($n-k, n-k+2, \ldots, n-1$) and at most $(k-1)/2$ even values in $[n-k, n-1]$ for even $n$ ($n-k+1, \ldots, n-2$). **No gaps.**

### Section 2: Permutation-Group Lemmas (Lemmas 2.1–2.3)
All compositions verified explicitly under the stated right-to-left convention $(\sigma\pi)(x) = \sigma(\pi(x))$:
- **Lemma 2.1:** With $\mathrm{supp}(g) \cap \mathrm{supp}(g') = \{a\}$, direct evaluation of $c = g g' g^{-1} (g')^{-1}$ on all six partition classes of $\Omega$ verifies $c(a) = g(a)$, $c(g(a)) = g'(a)$, $c(g'(a)) = a$, and $c(x) = x$ elsewhere, so $[g, g'] = (a\ g(a)\ g'(a))$.
- **Lemma 2.2:** Verified all three $3$-cycle generation identities right-to-left:
  - $(a\ b\ z_1)(a\ b\ z_2)^{-1} = (a\ b\ z_1)(a\ z_2\ b) = (a\ z_2\ z_1)$,
  - $(a\ b\ z_1)^{-1}(a\ b\ z_2) = (a\ z_1\ b)(a\ b\ z_2) = (b\ z_2\ z_1)$,
  - $(a\ x\ y)^{-1}(a\ y\ z)(a\ x\ y) = (a\ y\ x)(a\ y\ z)(a\ x\ y) = (x\ z\ y)$.
  Maximal $M \subseteq \Omega$ with $\mathrm{Alt}(M) \le G$ has $|M| \ge 3$; if $|M| < n$, $2$-transitivity maps distinct $(a, d) \in M^2$ to $(a, c)$ ($c \notin M$), giving $M' = g(M)$ with $\mathrm{Alt}(M') = g\mathrm{Alt}(M)g^{-1} \le G$. Both $|M \cap M'| \ge 2$ (direct merge) and $|M \cap M'| = 1$ (Lemma 2.1 produces $(a\ x\ y) \in G$, then merge $M$ with $\{a, x, y\}$ along $\{a, x\}$) contradict maximality.
- **Lemma 2.3:** For $g \in G \setminus \{1\}$ ($s = |\Delta| \ge 2$) and $2$-transitive $G$ with $\mathrm{Alt}_n \not\le G$, Lemmas 2.1–2.2 imply $X(h) = |\Delta \cap h(\Delta)| \in \mathbb{Z}_{\ge 0} \setminus \{1\}$, so $X(X-2) \ge 0$. Orbit-stabilizer over $1$- and $2$-transitive actions gives $\mathbb{E}[X] = s^2/n$ and $\mathbb{E}[X(X-1)] = s^2(s-1)^2/(n(n-1))$, forcing $(s-1)^2 \ge n-1$, contradicting $(s-1)^2 + 1 < n$. **No gaps.**

### Section 3: Lower Bound Attainment (Proposition 3.1 & Theorem 3.2)
- **Arithmetic setup:** $Q = 4 \prod_{3 \le q \le k+1,\, q \text{ prime}} q$. For each odd prime $q \le k+1$, $q \ge 3$ guarantees a residue $r_q \not\equiv 0, k \pmod q$. CRT produces $R \equiv 3 \pmod 4$ and $R \equiv r_q \pmod q$ with $\gcd(R, Q) = 1$. Dirichlet's theorem yields a prime $n \equiv R \pmod Q$ with $n > k^2 + 2$. For all $k \ge 2$, $k^2 + 2 - (2k+1) = (k-1)^2 \ge 1$, so $n - (k+1) > k$, ensuring every $m = n - a \in M_k(n)$ satisfies $k < m < n$.
- **Coprimality $\gcd(a, b) = 1$ ($b = n - k$):** Every odd prime $q \le k + 1$ satisfies $b \equiv r_q - k \not\equiv 0 \pmod q$; when $k$ is even, $b$ is also odd, while when $k$ is odd, every $a \in \{1, 3, \ldots, k\}$ is odd. Thus $\gcd(a, b) = 1$ for all $m = n - a \in M_k(n)$.
- **Proposition 3.1 (Transitivity):** Verified right-to-left:
  - For $y \in \{a+1, \ldots, n\}$, $(r_m r_n)(y) = r_m(n+1-y) = m + 1 - (n+1-y) = y - a$, so repeated application maps every $y \in \Omega$ to its unique representative in $\{1, \ldots, a\} \subseteq \Omega$; every $G$-orbit is a union of residue classes mod $a$.
  - For $x \in \{1, \ldots, k\}$, $(r_n r_k)(x) = r_n(k+1-x) = n + 1 - (k+1-x) = x + b \in \Omega$, so $\overline{x} \sim_G \overline{x + b}$ for all $x \in \{1, \ldots, k\}$.
  - Both $1 \le a \le k$ (all classes represented) and $a = k + 1$ ($k$ even; all nonzero classes represented, chaining $\overline{b} \sim_G \overline{2b} \sim_G \cdots \sim_G \overline{(a-1)b} \sim_G \overline{ab} = \overline{0}$ using $\gcd(a, b) = 1$) merge all $a$ classes into one orbit.
- **Theorem 3.2:**
  - $G$ is transitive of prime degree $n$, so Burnside's theorem (1901; Dixon–Mortimer GTM 163 Thm 3.5B; Wielandt Thm 11.7) implies $G$ is $2$-transitive or permutation-isomorphic to a subgroup of $\mathrm{AGL}_1(n)$.
  - Non-identity elements of $\mathrm{AGL}_1(n)$ fix at most $1$ point, whereas $r_k \neq 1$ fixes all $n - k > k^2 - k + 2 \ge 4 > 2$ points in $\{k+1, \ldots, n\}$, forcing $G$ to be $2$-transitive.
  - $s = |\mathrm{supp}(r_k)| = 2\lfloor k/2 \rfloor \le k$ satisfies $(s-1)^2 + 1 \le (k-1)^2 + 1 < k^2 + 2 < n$ for all $k \ge 2$ (and $n \ge 7 \ge 4$), so Lemma 2.3 gives $\mathrm{Alt}_n \le G$.
  - Finally, $n \equiv 3 \pmod 4 \implies \lfloor n/2 \rfloor = (n-1)/2$ is odd $\implies r_n \in G \setminus \mathrm{Alt}_n \implies G = \mathrm{Sym}_n$. Thus $M_k(n) \subseteq F_k(n)$, attaining equality with Proposition 1.2. **No gaps.**

---

## 4. Independent Mechanical Verification & Novelty Status

- **Independent script re-execution:** Re-ran `.venv/bin/python -u /Users/kev/Documents/open-math/targets/blanco-2511.16959-conj5/notes/check-check-2.py`: exited with status `0`, outputting `PASS (all checks passed in 1.602s)` (exhaustive Schreier–Sims $F_k(n)$ for $4 \le n \le 10$, Section 2 commutator & $\mathrm{AGL}_1(p)$ checks, and Section 3 CRT/Dirichlet construction verification for $k = 2, \ldots, 12$).
- **Primary-source & prior-work checks performed directly:**
  - `arXiv:2610.30892v1` (Lei–Zhao–Zhu–Wu) `main.tex`: proves Conjectures 2, 3, and 4 only; does not address Conjecture 5.
  - `the-omega-institute/trureturing`: `#20814` (preregistration for Conjecture 5) is `open`, `0` comments, no solution/PR; `#22875` is Conjecture 1; `#7577` and `#7558` are Conjecture 4 even/odd only.
  - Author repo `Luka5s5/prefix_reversal_triples` (last pushed `2026-05-10`): computational data/plots only.
  - Newly indexed competing repos (`GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `linustalacko/small-true-things`, `chy4pro/automath`, `CrocSwap/integer-mult-bounds`, `JENW1N/complete-math-solutions`) + Gate 2 receipts (`notes/novelty-gate2-watch-{1,2,5,6}.md`): clear; no `CONTESTED.md`.
- **Gate 3 receipts (all PASS, no `CONTESTED.md`):**
  - `targets/blanco-2511.16959-conj5/notes/novelty-gate3-watch-1.md` (`2026-11-27T04:10:00Z`, PASS): Sweep 14 snapshots, live arXiv `2511.16959v3`, Zenodo, and 15 competing GitHub repos (`trureturing*`, `aftd-platform` Conj 1–4 only, `atlas-lean`, `open-math-agents`, `ProofPlaygrond`, `CrocSwap`, `small-true-things`, `automath`, etc.) clear.
  - `targets/blanco-2511.16959-conj5/notes/novelty-gate3-watch-5.md` (`2026-11-27T03:40:57Z`, PASS): live arXiv `2511.16959v3`, OpenAlex citing works (`2610.30892v1` Conj 2–4 only; `2603.22195v1` bib-only), `aftd-platform` (`PrefixReversal*` Conj 1–4 only), `trureturing#20814` open/no PR, Zenodo, 470 snapshots, and 15 competing repos clear.
  - `targets/blanco-2511.16959-conj5/notes/novelty-gate3-watch-6.md` (`2026-11-27T03:50:17Z`, PASS): 596 discovered repo snapshots, live `trureturing`, and live arXiv `2511.16959v3` clear.
- Ready for final report to `@coordinator` with label `"written proof, internally audited"`.

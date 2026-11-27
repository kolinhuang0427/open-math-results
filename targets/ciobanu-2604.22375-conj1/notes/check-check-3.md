# Independent Check Report: `ciobanu-2604.22375-conj1`

- **Checker:** `@check-3`
- **Verdict:** **PASS**
- **Primary Source:** `tools/.arxiv_cache/eprint/2604.22375v1/Arxiv_version.tex` (`arXiv:2604.22375v1`, Section 3.1, Conjecture 1 `\label{conjecture1}`, L370–372).
- **Gate 2 Watch Status:** PASS (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

## 1. Primary-Source Fidelity Check

- **Verbatim match:** `TARGET.md` L11–17 reproduces the definitions of $\Sigma = X \cup X^{-1}$, $\pi : \Sigma^\star \to G$, $\mathbf{VPL}^\forall$, $\mathbf{REG}^\forall$ (recognisable), and the verbatim text of `\begin{conj}\label{conjecture1}` from `Arxiv_version.tex` L204–215 and L370–372.
- **Numbering:** `\subsection{$\mathbf{VPL}^\forall$ sets in groups}` (L366) is **Section 3.1** inside Section 3 (`\section{Types of \vpl ~sets in groups}`, L305; the Introduction is unnumbered, making `Preliminaries` Section 1 at L68 and `The Word Problem` Section 2 at L242), and `\begin{conj}\label{conjecture1}` (L370–372) is the unique conjecture environment in the paper (Conjecture 1).

## 2. Proof Audit & Independent Mechanical Verification

- Checked `PROOF.md` L1–89 against `Arxiv_version.tex` §1.1 (`\ref{prop:CongsVPLs}`, `\ref{prop:recsetsareficosets}`, VPA conventions L78–100):
  - **Case 1 ($\Sigma_r = \emptyset$):** Projecting stack push labels yields an NFA $M'$ accepting $L = \pi^{-1}(S)$; reachable-state-set congruence $R(u_1) = R(u_2)$ gives $H \pi(u_1) = H \pi(u_2)$ for $H = \mathrm{Stab}_L(S)$, bounding $[G : H] \le 2^{|Q|} < \infty$. (Trivially handles empty $\Sigma$ for $G = \{1\}$ too.)
  - **Case 2 ($\Sigma_r \neq \emptyset$):**
    - Lemma 1: $\mathit{MC}(\Sigma)$ is a submonoid containing $\Sigma_r \cup \Sigma_i \cup (\Sigma_c \Sigma_r)$, so picking $y_0 \in \Sigma_r$ gives $\pi(x) = \pi(x y_0)\pi(y_0)^{-1} \in \langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}}$ for all $x \in \Sigma_c$, hence $\langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}} = G$.
    - Lemma 2: Every run of $M$ on $u \in \mathit{MC}(\Sigma)$ from empty stack $\bot$ ends with $\bot$ (maximizing index $j$ with $h_j = 0$ would force $\#_c(s) > \#_r(s)$ on the suffix $s = a_{j+1}\dots a_m$), hence $|\mathit{MC}(\Sigma) / {\sim_0}| \le 2^{|Q|} < \infty$, and $u_1 \sim_0 u_2 \implies H\pi(u_1) = H\pi(u_2)$.
    - Lemma 3: Right multiplication $\rho_m$ maps finite $\Omega = \{Hm : m \in M_{\mathrm{mc}}\}$ into itself injectively, forcing $\rho_m(\Omega) = \Omega$ and $\rho_{m^{-1}}(\Omega) = \Omega$, so $K = \{g \in G : \rho_g(\Omega) = \Omega\} = G$ and $\Omega = H \backslash G$.
  - **Conclusion:** Normal core $N = \bigcap_{g \in G} g H g^{-1}$ satisfies $[G:N] \le [G:H]! < \infty$ and $S = \bigcup_{s \in S} N s$, so $S \in \mathbf{REG}^\forall(G)$.
- Wrote and executed independent verifier [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/ciobanu-2604.22375-conj1/notes/check-check-3.py) (AST `FLOAT_COUNT: 0`):
  1. `[1/3]` Lemma 1 & Lemma 2(1) tested on all $\mathit{MC}(\Sigma)$ words up to length 5 across 20 random nondeterministic VPAs.
  2. `[2/3]` Case 1 and two Case 2 VPA partitions over $G = (\mathbb{Z}/6\mathbb{Z}) \times S_3$ with non-normal stabilizer subgroup $H_{\mathrm{true}}$ of index 9 and normal core $N$ of index 18 (verified VPA acceptance up to length 4, $\mathit{MC}(\Sigma)$ generation, $\Omega = H \backslash G$, and $S = \bigcup_{s \in S} N s$).
  3. `[3/3]` Negative sanity check on $G = \mathbb{Z}$, $S = \{0\}$ verifying unbounded ${\sim_0}$-classes on $\{A^k\}_{k=0}^{12} \subset \mathit{MC}(\Sigma)$.

### Raw Verifier Output

Command: `.venv/bin/python -u targets/ciobanu-2604.22375-conj1/notes/check-check-3.py` (exit code `0`):
```text
[1/3] Checking Lemma 1 (MC submonoid & generation) & Lemma 2(1) (empty stack) on random VPAs...
[2/3] Checking Case 1, Case 2 (Lemma 2, Lemma 3, normal core N) on finite & infinite groups...
[3/3] Checking negative sanity on G = Z, S = {0} (infinite ~_0 index for symmetric partition)...
PASS
```

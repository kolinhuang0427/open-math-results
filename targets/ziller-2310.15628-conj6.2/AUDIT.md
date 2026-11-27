# Adversarial Audit Report (`audit-3`) — `targets/ziller-2310.15628-conj6.2/`

- **Verdict:** **PASS**
- **Charter label:** `"written proof, internally audited"`
- **Auditor:** `audit-3` (isolated audit; did not read `verify.py` or author scratch `notes/screen-*` / `notes/attack-*` / `notes/triage-brief.md`)
- **Audited at (UTC):** 2026-11-27 06:22 UTC
- **Files inspected:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, `notes/audit-helper-ziller.md`, and primary source `tools/.arxiv_cache/eprint/2310.15628/` (`Ziller_2023_v2.tex`, `Examples.tex`, `Conclusions.tex`, plus `2310.15628v1` and `2604.19646v1`).

---

## 1. Primary-Source Fidelity (`arXiv:2310.15628v2`, 2026-04-15, latest version)

Directly checked `tools/.arxiv_cache/eprint/2310.15628/`:
- **Conjecture 6.2 (`Conclusions.tex` L89–91; numbered 6.2 via `\stepcounter{section}` at `Conclusions.tex` L4 and shared `defi` counter in `Ziller_2023_v2.tex` L28–30; previously numbered Conjecture 5.10 in v1):**
  > All function values of $\dfrac{\varphi(x)}{x^2}$ for $x \in \mathbb{N}$ are pairwise distinct.
  Matches `TARGET.md` and `PROOF.md` verbatim.
- **Definitions verified:** `Ziller_2023_v2.tex` L116 defines $\mathbb{N} = \{1, 2, 3, \dots\}$; `Examples.tex` L296 defines Euler's totient $\varphi(x) = |\{k \in \mathbb{N} \le x : k \perp x\}| = x \prod_{p \mid x} (1 - 1/p)$; `Conclusions.tex` L98 notes the equivalent reciprocal claim for $x^2/\varphi(x)$; `Examples.tex` L337–349 proves only the distinct-coprime special case (Lemma 5.8) and leaves the general conjecture explicitly open in v2 (`2026-04-15`). Ziller's follow-up `arXiv:2604.19646v1` (`2026-04-21`) cites `2310.15628` without resolving Conjecture 6.2.

---

## 2. Adversarial Line-by-Line Audit of `PROOF.md`

Every step of `PROOF.md` (lines 1–52) was audited independently:
1. **Product formula (L10–21):** For any $n = \prod_{q \mid n} q^{e_q} \in \mathbb{N}$ (empty product $= 1$ when $n = 1$), $\varphi(n)/n^2 = \prod_{q \mid n} (q-1)/q^{e_q+1}$, and $v_p(f(n)) = \sum_{q \mid n} (v_p(q-1) - (e_q + 1) v_p(q))$ since $v_p \colon \mathbb{Q}_{>0} \to \mathbb{Z}$ is a homomorphism. **Exact.**
2. **Minimal-product setup & largest prime factor (L23–36):** For a pair $x \neq y \in \mathbb{N}$ with $f(x) = f(y)$ minimizing $xy$, $\max(x, y) \ge 2$ implies $xy > 1$, so $xy$ has a largest prime factor $p$. For every prime $q \mid xy$, $1 \le q - 1 < p$ gives $v_p(q - 1) = 0$. Hence $v_p(f(x)) = 0$ if $v_p(x) = 0$ and $-(v_p(x) + 1) \le -2$ if $v_p(x) \ge 1$ (and identically for $y$). Handles $x = 1$ or $y = 1$ seamlessly. **Exact.**
3. **Descent & contradiction (L38–52):** Since $p \mid xy$ and $v_p(f(x)) = v_p(f(y))$, both $e := v_p(x)$ and $f' := v_p(y)$ are $\ge 1$ and satisfy $-(e+1) = -(f'+1) \implies e = f' \ge 1$. Factoring $x = p^e x_0, y = p^e y_0$ with $p \nmid x_0, p \nmid y_0$, multiplicativity of $f$ on coprime arguments and $f(p^e) = (p-1)/p^{e+1} > 0$ yield $f(x_0) = f(y_0)$ with $x_0 \neq y_0$ and $x_0 y_0 = xy / p^{2e} < xy$, contradicting minimality of $xy$. **100% airtight; zero gaps.**

---

## 3. Independent Computation & Deep Classical/Modern Novelty Check

- **Independent verifier rerun (`notes/check-check-3.py`):** Exited `0` in `0.93s` (`real 0.93s`), verifying exact injectivity of $\varphi(x)/x^2$ for all $1 \le x \le 200{,}000$, product & $p$-adic valuation identities for $1 \le n \le 10{,}000$, and $p^e$-descent for $2 \le x < y \le 200$.
- **Deep novelty & classical-literature check (`notes/audit-helper-ziller.md` §2):**
  - No `CONTESTED.md`; 17 targeted web search queries, StackExchange API (MSE & MO), live OEIS (`A373318`, `A373319`, `A373320`, `A002618`, and cross-references), arXiv, Crossref, Zenodo, Mathlib4 v4.36.0, 522 local watch snapshots, and 32 competing GitHub repos (`the-omega-institute/*`, `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `openai/math`) returned **0 prior proofs or statements** of injectivity of $\varphi(x)/x^2$, $x^2/\varphi(x)$, $m^2\varphi(n) = n^2\varphi(m)$, or general $n^\alpha\varphi(n)$ ($\alpha \le -2$ / $\alpha \notin \{0,-1\}$).
  - **Scholarly disclosure (sibling exponent $\alpha = 1$):** The exact same largest-prime $p$-adic valuation descent is well known in the literature for the sibling integer-valued function $n \mapsto n\varphi(n) = \varphi(n^2)$ (e.g., P. Giblin, *Primes and Programming*, CUP 1993, p. 116 Ex. 1.10; OEIS `A002618` F. Vrabec 2012; MSE `#68120` & `#539558`; Gabdullin–Iudelevich–Luca, `arXiv:2201.09287v2` / *Int. J. Number Theory* 19(5), 2023, §4). None of those sources state or prove injectivity of $\varphi(x)/x^2$ (or general $n^\alpha \varphi(n)$), and Ziller explicitly left $\varphi(x)/x^2$ open as Conjecture 6.2 in April 2026 (`2310.15628v2`).
  - **Coverage caveat:** OpenAlex (`W4387947328`, `cited_by_count: 1`) `cites:` endpoint and Semantic Scholar hit HTTP 429 daily quota; however, Ziller's own `arXiv:2604.19646v1` (2026-04-21) cites `2310.15628` 6 times (accounting for the 1 citation) and was directly inspected and confirmed not to resolve Conjecture 6.2.

---

## 4. Verdict & Handoff

- **Verdict:** **PASS** (exact Charter label: `"written proof, internally audited"`).
- **Next step:** Requesting Gate 3 live pre-report novelty re-check before final report to `@coordinator`.

---

## 5. Lean 4 Statement-Fidelity Audit (`@audit-2`, `2026-11-27T09:18Z`) — **PASS**

- **Lean module:** `lean/OpenMath/Ziller231015628Conj62.lean` (306 lines; imported in `lean/OpenMath.lean` line 11)
- **Primary source verified verbatim (`tools/.arxiv_cache/eprint/2310.15628v2/`):**
  - `Ziller_2023_v2.tex` line 116: $\mathbb{N} = \{1, 2, 3, \dots\}$ (positive integers).
  - `Examples.tex` line 296: Euler's totient $\varphi(x) = |\{k \in \mathbb{N} \le x : k \perp x\}| = x \prod_{p \mid x} (1 - 1/p)$.
  - `Conclusions.tex` lines 89–91 (Section 6, Conjecture 6.2): *"All function values of $\frac{\varphi(x)}{x^2}$ for $x \in \mathbb{N}$ are pairwise distinct."* (Line 98 notes the equivalent reciprocal statement for $x^2/\varphi(x)$.)
- **Statement-fidelity verification:**
  - `Nat.totient` (Mathlib) agrees identically with Ziller's $\varphi(x)$ on all $x > 0$ (for $x = 1$, $\varphi(1) = 1$; for $x \ge 2$, $\gcd(0, x) = x \neq 1$ and $\gcd(x, x) = x \neq 1$, so $\{k < x : k \perp x\} = \{1 \le k \le x : k \perp x\}$).
  - `ziller_conjecture_6_2` (`{x y : ℕ} (hx : 0 < x) (hy : 0 < y) : (Nat.totient x : ℚ) / (x : ℚ) ^ 2 = (Nat.totient y : ℚ) / (y : ℚ) ^ 2 → x = y`), `ziller_conjecture_6_2_pnat` (`Function.Injective (fun x : ℕ+ => (Nat.totient x : ℚ) / (x : ℚ) ^ 2)`), `ziller_conjecture_6_2_reciprocal` (for $x^2/\varphi(x)$), and `totient_mul_sq_inj` match Conjecture 6.2 verbatim (since $\mathbb{Q} \hookrightarrow \mathbb{R}$ is injective, equality in $\mathbb{Q}$ is equivalent to equality in $\mathbb{R}$).
- **Hygiene audit:** `grep -nE 'sorry|admit|axiom |native_decide|unsafe|implemented_by|extern |partial '` matched only the module docstring on line 18 (zero `sorry`, zero `admit`, zero custom `axiom`, zero `native_decide`, zero `unsafe`). All 4 main theorems have `#print axioms` checks on lines 301–304.
- **Verdict:** **PASS** (statement fidelity & Lean hygiene verified; handed off directly to `@coordinator` for final `lake build` + `lake env lean` verification).

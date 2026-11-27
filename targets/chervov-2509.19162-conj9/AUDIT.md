# Adversarial Audit Report: `targets/chervov-2509.19162-conj9/`

- **Auditor:** `audit-2`
- **Audited UTC:** `2026-11-27T06:28Z`
- **Target:** A. Chervov et al., *"CayleyPy Growth: Efficient growth computations and hundreds of new conjectures on Cayley graphs (Brief version)"*, `arXiv:2509.19162v2` (`2026-04-01`), Subsection *"Bounds on the diameters of unitriangular groups"*, Conjecture 9 (`mainv2.tex` lines 2229–2231)
- **Owner:** `scout-12`
- **Checker:** `check-3` (`notes/check-check-3.md`, `notes/check-check-3.py`)
- **Audit Helper:** `chervov-audit-hlp` (`notes/audit-helper-chervov.md`, killed)
- **Strict Isolation Observed:** Read ONLY the primary source (`tools/.arxiv_cache/eprint/2509.19162/mainv2.tex` via `notes/audit-helper-chervov.md`), `TARGET.md`, `COUNTEREXAMPLE.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, and `notes/audit-helper-chervov.md`. Did NOT read author `verify.py` or any author scratch notes. Did NOT edit `TARGET.md` or `COUNTEREXAMPLE.md`.
- **Verdict:** **FAIL** *(2 small fixable proof/wording errors in `COUNTEREXAMPLE.md` L73 & L21; all core math, primary source, novelty, and computations PASS)*

---

## 1. Exact Blocking Errors to Fix in `COUNTEREXAMPLE.md`

1. **`COUNTEREXAMPLE.md` line 73 (Claim 1 — false group-axiom justification):**
   States: *"Hence multiplication is associative, $(0,0)$ is the identity, and $G$ is finite with $|G| = AB = 2^{a+b} = 2^n$ (so inverses exist automatically)."*
   - **False reasoning:** A finite associative monoid does **not** automatically have inverses (e.g., $(\{0, 1\}, \times)$); finiteness implies inverses only together with cancellation (injectivity of left/right translations), or by exhibiting the inverse directly.
   - **Fix:** Replace `"(so inverses exist automatically)"` with either the explicit 1-line right/left inverse
     $$(i, j)^{-1} = \Bigl(\bigl(-i - C\mathbf{1}_{j > 0}\bigr) r^{-j} \bmod A,\; (-j) \bmod B\Bigr)$$
     (valid since $r = 1 + 2^s$ is odd, hence invertible modulo $A = 2^a$) or the 1-line verification that left- and right-multiplication by any $(i_1, j_1)$ are injective (hence bijective on finite $G$) because $r$ is invertible mod $A$.

2. **`COUNTEREXAMPLE.md` line 21 (ambiguous scope & unverified $n = 7$ claim):**
   States: *"(in fact, exhaustive BFS for $2 \le n \le 7$ gives diameters $1, 4, 8, 12, 19, 26$, matching $M(n)$ only on $3 \le n \le 7$ and failing at $n = 2$ and for all $n \ge 178$ as well as $n = 176$)."*
   - **Two issues:** (a) `"matching M(n) only on 3 <= n <= 7"` reads as claiming equality fails for $8 \le n \le 175$, which is not proved here (only $n = 2$, $n = 176$, and $n \ge 178$ are proved to fail); (b) the independent checker `notes/check-check-3.py` verifies exact BFS for $2 \le n \le 5$ (and our helper verified $2 \le n \le 6$ giving `1, 4, 8, 12, 19`), whereas $n = 7$ (`diam = 26`) is neither tabulated in `mainv2.tex` nor independently verified by `check-check-3.py`.
   - **Fix:** Tighten the parenthetical to state accurately only what is verified and proved — e.g., *"among $2 \le n \le 6$, exact BFS gives diameters $1, 4, 8, 12, 19$, already failing at $n = 2$ ($1 < 2$) and matching $M(n)$ on $3 \le n \le 6$, while Parts 1–3 prove failure at $n = 176$ and for all $n \ge 178$."*

*(Optional minor clarity note on line 88: when $c = d$, $c - d = 0$ so $Z(G) \cong C_{2^{n-2d}}$ is cyclic; the sentence "the smaller invariant factor exponent of $Z(G)$ equals $c - d$" is valid under the 2-component convention $C_{2^{e_1}} \times C_{2^{e_2}}$ with $e_1 \ge e_2 \ge 0$, which could be stated in 4 words for extra clarity.)*

---

## 2. What Passed (No Rework Needed)

- **Primary-source fidelity (`notes/audit-helper-chervov.md` §1):** Confirmed `arXiv:2509.19162v2` (`mainv2.tex` lines 2229–2231, 9th `\begin{Conj}`, $n$ unqualified) and OEIS `A136184` (rev. 31, `2026-09-17`) match `TARGET.md` verbatim. Even if Conjecture 9 were read charitably as $n \ge 3$, Parts 1–3 unconditionally refute it for $n = 176$ and all $n \ge 178$.
- **Mathematical audit of Parts 1–3 (modulo the 2 fixes above):**
  - **Part 1:** Row-by-row decomposition $M = U_{n-2}\cdots U_0$, block conjugation $W^{-1} s_{i+1} W = I + e_i^T \mathrm{row}_{i+1}(W)$, two-pass construction of $W$ of length $\le 2(n-i) - 5$, final $(i, i+1)$ flip, and total sum $1 + 2(n-2)(n-1) = 2n^2 - 6n + 5$ are 100% airtight for all $n \ge 2$.
  - **Part 2:** LTE for $p = 2$ ($s \ge 2 \implies \nu_2(r^j - 1) = s + \nu_2(j)$), carry associativity, $G' = \langle x^{2^s} \rangle$ of order $2^d$, $G^{\mathrm{ab}} \cong C_{2^s} \times C_{2^{n-a}}$ with $s < n - a$, $Z(G) = \langle x^{2^d}, y^{2^d} \rangle \cong C_{2^{n-c-d}} \times C_{2^{c-d}}$ with $c - d \le n - c - d$ (recovering $(a, c, s)$ uniquely) are completely airtight once the inverse justification in Claim 1 line 73 is fixed.
  - **Part 3:** Exact counting identity $\sum_{s=2}^{a-1}(\min(s,a-s)+1) = \lfloor a^2/4 \rfloor + a - 3 \ge (a^2 + 4a - 13)/4$, exact closed-form cubic sum $(2m^3 + 15m^2 - 65m + 54)/24 > m^3/12 \ge (n-1)^3/96$, and $(n-1)^3 - 96(2n^2 - 6n + 5) = n^3 - 195n^2 + 579n - 481 > 0$ for $n \ge 195$ (plus exact integer evaluation for $n = 176$ and $178 \le n \le 195$) are 100% exact.
- **Independent mechanical verification (`notes/check-check-3.py` & `notes/audit-helper-chervov.md` §3):** `check-check-3.py` passed (`exit 0`, `1.72s`), and independent bitmask BFS confirmed $\mathrm{diam}(U(n, \mathbb{F}_2)) = 1, 4, 8, 12, 19$ for $n = 2..6$, along with exact $|\mathcal{F}_n|$ and OEIS `A136184` GF values.
- **Deep novelty check (`notes/audit-helper-chervov.md` §2):** Clear across arXiv (`2509.19162v2`, `2603.22195v1`, `2610.08385`, `2610.14373`, `au:Chervov`), OEIS `A136184` rev. 31, `cayleypy/*` (incl. PR #213), `the-omega-institute/trureturing*`, 17+ competing GitHub repos, `522` local snapshots, Crossref, Zenodo, and web search.

---

## 3. Handoff

Returned to `@scout-12` for the quick 2-line fix (`COUNTEREXAMPLE.md` L73 & L21). Upon fix, ready for immediate re-audit PASS and Gate 3 novelty check.

---

## 4. Re-Audit After Fixes (`audit-2`, `2026-11-27T09:02Z`)

- **Verdict:** **`PASS`**
- **Charter Label:** `"written proof, internally audited"` (with exact-arithmetic verification of BFS diameters $n = 2..5$ [and $n=6$], word factorizations up to $n = 176$, metacyclic group laws/invariants $n = 6, 7, 8$, and cubic/quadratic threshold inequality through $n = 500$ in `notes/check-check-3.py`).
- **Verified Fixes in `COUNTEREXAMPLE.md`:**
  1. **Line 73 (Claim 1 inverse):** Replaced the invalid finiteness-only claim with the explicit two-sided inverse $\bigl((-i - C\mathbf{1}_{j > 0}) r^{-j} \bmod A,\; (-j) \bmod B\bigr)$ ($r = 1 + 2^s$ odd, invertible mod $A = 2^a$). Auditor verified both products directly: for $j = 0$, trivial; for $1 \le j < B$ ($j' = B - j$), right product first coordinate is $i + (-i - C) r^{-j} r^j + C \equiv 0 \pmod A$, and left product first coordinate is $(-i - C) r^{-j} + i r^{B-j} + C \equiv -i r^{-j} - C + i r^{-j} + C = 0 \pmod A$ using $r^B \equiv 1 \pmod A$ and $C r^{-j} \equiv C \pmod A$.
  2. **Line 21 (scope wording):** Tightened accurately to state only the verified $2 \le n \le 6$ BFS diameters (`1, 4, 8, 12, 19`, failing at $n = 2$ and matching $M(n)$ on $3 \le n \le 6$) plus proved failure at $n = 176$ and all $n \ge 178$.
  3. **Line 88 (clarity):** Explicitly states the 2-component convention $C_{2^{e_1}} \times C_{2^{e_2}}$ ($e_1 \ge e_2 \ge 0$, $C_1$ trivial when $c = d$).
- **Independent Verifier Re-run:** Re-executed `.venv/bin/python targets/chervov-2509.19162-conj9/notes/check-check-3.py` -> exit code `0`, raw output `PASS`.
- **Handoff:** Ready for Gate 3 novelty check (`@watch-1`, `@watch-5`, `@watch-6`) and final reporting to `@coordinator`.

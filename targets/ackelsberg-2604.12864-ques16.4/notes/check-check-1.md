# Independent Check Report — `ackelsberg-2604.12864-ques16.4`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Ethan Ackelsberg and Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*, `arXiv:2604.12864v1` (`tools/.arxiv_cache/eprint/2604.12864.src`, `InverseProblemDensity_arXiv_v1.tex`).
- **Exact numbering & location:** Section 16 (`\section{Further explorations}`, L5712), Subsection 16.1 (`\subsection{More on direct theorems for sumsets in the integers}`, L5716), Question 16.4 (`\begin{Question}[Kneser's theorem in $\N^2$]`, L5771–5777; preceded by `\N=\{1,2,3,\ldots\}` at L398, `[N]=\{1,\ldots,N\}` at L405, and $\liminf_{n,m\to\infty}$, $\underline{d}(A)$, $H_{a,b,c}$ definitions at L5760–5768).
- **Verbatim match:** `TARGET.md` matches the primary definitions, quantifiers (`\N`, `[N]`, $\underline{d}$ via rectangular $\liminf_{n,m\to\infty}$, $H = H_{a,b,c} \cap (\mathbb{N} \times \mathbb{N})$ with $a,c \in \mathbb{N}$, $b \in \{0,\ldots,a-1\}$), and statement verbatim, including noting the primary-paper typo `d(A+H)+d(A+H)-d(H)` at L5776 (matching Theorem 1.2 at L421). Since $A = B$ in `COUNTEREXAMPLE.md`, the typo does not affect anything, and `COUNTEREXAMPLE.md` refutes the structural conclusion ($A+B$ equals, up to finitely many elements, a finite union of translates of $H$).

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python targets/ackelsberg-2604.12864-ques16.4/notes/check-check-1.py` using exact `int` and `fractions.Fraction` arithmetic (`AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Sumset & slice structure:** Exhaustive brute-force computation of $A + B$ for $A = B = (2\mathbb{N} \times \N_{\ge 3}) \cup \{(2^j, 1) : j \in \mathbb{N}\}$ on $[1..150] \times [1..40]$ (`2763` points) matches the slice description in `COUNTEREXAMPLE.md` (`\varnothing` for $y \in \{1,3\}$, $\{(2^j+2^{j'},2) : j,j'\ge 1\}$ for $y=2$, $2\N_{\ge 2} \times \{y\}$ for $y \ge 4$) at every lattice point.
2. **Exact rational density bounds:** Exact counts $|A \cap ([n]\times[m])| = \lfloor n/2 \rfloor (m-2) + (\lfloor \log_2 n \rfloor)$ and $|(A+B)\cap([n]\times[m])| = (m-3)(\lfloor n/2 \rfloor - 1) + s_2(n)$ (`s_2(n) <= (\lfloor \log_2 n \rfloor)^2`) verified for all $4 \le n, m \le 64$, together with exact sandwich bounds giving $\underline{d}(A) = \underline{d}(B) = d(A) = 1/2$ and $\underline{d}(A+B) = d(A+B) = 1/2 < 1 = \underline{d}(A) + \underline{d}(B)$ (explicit separation at $N = 2^{20}$: $\le 34359738393/68719476736 < 1048573/1048576$).
3. **Failure of finite union of translates of $H = H_{a,b,c} \cap \mathbb{N}^2$:** Exhaustively verified across `21,675` tuples $(a,b,c,v_1,v_2)$ (`1 <= a,c <= 5`, `0 <= b < a`, `v in [-8,8]^2` in $\mathbb{Z}^2$) on $x \in [1, 128]$ that $(v + H) \cap (\mathbb{N} \times \{2\})$ is empty iff $(2 - v_2)/c \notin \mathbb{N}$ and otherwise equals $\{x \in \mathbb{N} : x \equiv v_1 + b m_i \pmod a,\ x \ge \max(1, v_1+1)\} \times \{2\}$; verified the Case 2 lower bound $\lfloor (2^K - X_0)/a \rfloor > (K-1)^2 \ge |(A+B) \cap ([2^K]\times\{2\})|$ as $K \to \infty$.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).

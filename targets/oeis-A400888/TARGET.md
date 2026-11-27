---
source: https://oeis.org/A400888 (created 2026-10-15), https://oeis.org/A000361
status: reported
owner: attack-2
updated: 2026-11-27T08:04:00Z
identifiers: [A400888, A000360, A000361, A284556, A002487, Gosper-Lafitte triangle, M. Jeremie Lafitte (Levitas)]
---

# Target: OEIS A400888 (Gosper–Lafitte Quarter-Turn Stern Content Surjectivity)

## Verbatim Statement
From OEIS **A400888** (author: `_M. Jeremie Lafitte (Levitas)_`, Oct 08 2026; created/modified `2026-10-15T16:25:59-04:00`):

- **Name:**
  > Contents of the quarter-turn corrected Stern vectors associated with the column words of the Gosper-Lafitte triangle.
- **Definition (`Comment`):**
  > Let V(n) be the filled-empty word in column n of the fractal set described in A000360, considered from the narrow top downward, with filled=1 and empty=0. V(n) is A000361's W(n) read in reverse order. Let f_n=A000360(n) and e_n=A284556(n+1) be its numbers of 1s and 0s. Starting with (p,q)=(1,1), read V(n), replacing (p,q) by (p+q,q) after a 1 and by (p,p+q) after a 0. Let (p_n, q_n) be the resulting Stern vector.
  > With v_n=(p_n,q_n)^T, c_n=(f_n,e_n)^T, J={{0,-1},{1,0}}, and u_n=v_n + J*c_n, we have a(n) = max {m >= 1 : u_n == (0,0)^T (mod m)}.
  > ...
  > Every positive integer divides some term of this unbounded sequence. Every positive even integer occurs infinitely often as a term. It is conjectured that the sequence is surjective onto the positive integers.

## Gate 1 Novelty Receipt
- Checked at: `2026-11-26T23:42:00Z` – `23:46:01Z`
- `watch/snapshots/` (`tools/novelty_grep.py A400888 "Gosper-Lafitte"`): `0` hits across `356` files.
- `tools/arxiv_fetch.py query "all:A400888 OR all:\"Gosper-Lafitte\""`: `0` results.
- Zenodo API (`zenodo.org/api/records?q=A400888+OR+%22Gosper-Lafitte%22&size=3`): `0` hits.
- GitHub code search (`gh search code A400888`): only `archmageirvine/joeis` (`A400888.java`, `A400889.java`); `0` matches in `aliromman/math`, `trureturing`, `joaquimmj/oeis-conjectures`, `1337isnot1337/solved-conjectures`.
- Web search (`"A400888" OR "Gosper-Lafitte triangle" "surjective"`): only OEIS `A400888`; no proof or disproof found.
- OEIS `A400888` and `A000361` (rev `2026-10-21`) inspected live: surjectivity remains marked conjectured.
- Not covered: closed-access venues not indexed by arXiv/Zenodo/web.

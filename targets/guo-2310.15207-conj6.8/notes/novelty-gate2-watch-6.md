# Gate 2 Novelty Check — targets/guo-2310.15207-conj6.8/ (watch-6)

- **UTC Timestamp:** `2026-11-27T11:01:23Z`
- **Target:** `targets/guo-2310.15207-conj6.8/` (`status: candidate`, `owner: scout-11`) — Victor J. W. Guo (`arXiv:2310.15207v1`, §6) Conjecture 6.8 (`conj:8`) modulo $\Phi_n(q)^2$ for $m \ge 1$, odd $n \ge 3$ (and boundary $n=1$).
- **Verdict:** **PASS** (no settled proof or counterexample found).

## Exact Queries & Results

1. **Local Snapshot Index (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python -u tools/novelty_grep.py "2310.15207" "conj:8" "Conjecture 6.8"`
   - Result: `# 0 lines across 0/636 files in 0.79s` (incl. Sweep 4 `discovered/`).
2. **Live arXiv (`all:2310.15207`):**
   - Sole version remains `http://arxiv.org/abs/2310.15207v1` (`2023-10-23T12:51:42Z`, *"Dwork-type $q$-congruences through the $q$-Lucas theorem"*).
3. **Citation & Related-Paper Checks:**
   - OpenAlex (`doi:10.1007/s13398-025-01762-9`): `cited_by_count: 2` (`cited_by_api_url` returned HTTP 429; S2 returned `None`).
   - Checked citing arXiv preprint `arXiv:2608.13818` (*"Some Dwork-type $q$-supercongruences from a $_6\phi_5$ summation formula"*): addresses $(6k-1)(-1/3)_k^3/(1)_k^3$ mod $p^{3s}$, completely distinct from Conjecture 6.8's `[4k+1](q;q^2)_k^3/(q^2;q^2)_k^3 q^{k^2}` mod $\Phi_n(q)^2$. (`watch-5` `#953` also confirmed all S2 citing papers incl. `2608.13818` `.tex` do not cover `conj:8`.)
4. **Zenodo API (`https://zenodo.org/api/records?q=%222310.15207%22&size=5`):** `zenodo_hits: 0`.
5. **GitHub Search (`gh search repos "2310.15207"`, `gh search issues "2310.15207"`):** Both returned `[]`.
6. **Web Search (`search_web`):** Clear; no resolution of Conjecture 6.8 located.

## Coverage Limits
- OpenAlex `cited_by_api_url` hit HTTP 429 and Semantic Scholar returned `None` during this turn (`watch-5` verified S2 citing set in `#953`); `gh search code` skipped after `0` repo/issue/snapshot hits.

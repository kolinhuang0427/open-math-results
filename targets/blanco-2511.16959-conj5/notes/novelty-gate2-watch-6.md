# Gate 2 Novelty Receipt — `targets/blanco-2511.16959-conj5/` (`watch-6`)

- **UTC Checked:** `2026-11-27T02:00:53Z`
- **Target:** Blanco–Golubyatnikov–Konstantinova–Maslova–Nikiforov, `arXiv:2511.16959v3` (DMTCS 28:1, 2026), Section 4.1 Conjecture 5 (`con:F_k(n)`).
- **Verdict:** **PASS**
- **Sources & Exact Queries Checked:**
  1. **Live arXiv API (`tools/arxiv_fetch.py query --id-list 2511.16959` + `all:"three prefix reversals"`):** Latest is `2511.16959v3` (`2026-09-22T12:44:56Z`). Near miss `2610.30892v1` (Lei–Zhao–Zhu–Wu, `2026-10-22`) settles Conjectures 2–4 only (`conj:mod4`, `conj:mod2`, `conj:km_sum`), not Conjecture 5 (`con:F_k(n)`).
  2. **Live `the-omega-institute/trureturing` (`search/issues?q=repo:the-omega-institute/trureturing 2511.16959`):** `total_count: 4` — issue `#20814` (`open`, `0` comments, preregistration for Conjecture 5 with no solution/PR), issue `#22875` (`closed`, Conjecture 1), and merged PRs `#7577` & `#7558` (Conjecture 4 even/odd only).
  3. **Competing repo snapshots (11 snapshots incl. `JENW1N`, `TheJustinSunPrize/awards`, `aftd-platform`, `valyuAI/research`, `atlas-lean`, `aliromman/math`, `KnowledgeSense/math`, `trureturing*`) + `tools/novelty_grep.py`:** `0` hits for `2511.16959`, `con:F_k`, `three prefix reversals`, or `golubyatnikov`.
  4. **Live Zenodo API (`q=2511.16959`):** `0` hits.
- **Not Covered:** Off-arXiv manuscripts not indexed by Zenodo/GitHub and private repositories.

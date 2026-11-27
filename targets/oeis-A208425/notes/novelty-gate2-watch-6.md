# Gate 2 Novelty Receipt — `targets/oeis-A208425/` (`watch-6`)

- **UTC Checked:** `2026-11-27T01:49:16Z`–`02:00:53Z`
- **Target:** OEIS `A208425` rev 60 — Zhi-Wei Sun (Nov 12 2016) Conjecture (ii), $p \equiv 1 \pmod 3$ case ($\sum_{k=0}^{p-1} a(k) \equiv \binom{2(p-1)/3}{(p-1)/3} \pmod{p^2}$).
- **Verdict:** **PASS**
- **Sources & Exact Queries Checked:**
  1. **Live OEIS (`https://oeis.org/search?q=id:A208425&fmt=json`):** `rev 60` (`2025-11-05T15:22:21-05:00`) unchanged; Conjecture (ii) remains unmarked as proved.
  2. **Competing repo snapshots (11 snapshots incl. `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `aliromman/math`, `KnowledgeSense/math`, `trureturing*`) + `tools/novelty_grep.py`:** `0` competing solution hits for `A208425`.
  3. **Direct inspection of `Varun-Dudipala/sun-conjectures-lean` (`SunConjectures/A208425/README.md` via `gh api`):** Formalizes only `OeisA189286.conjecture_3` and `OeisA208425.conjecture_3` ($p \equiv 2 \pmod 3$), explicitly stating: *"The companion statements, part (i) and the case $p \equiv 1 \pmod 3$, are not proved here."*
  4. **arXiv near miss:** Hao Pan & Zhi-Wei Sun, `arXiv:2012.05121v3` (`2026-03-13`, *Frontiers in Combinatorics and Number Theory* 2 (2026), 55–62) proves Conjecture (i) for central trinomial coefficients / related congruence only, not Conjecture (ii) ($p \equiv 1 \pmod 3$).
  5. **Live Zenodo API (`q=A208425`):** `0` hits.
- **Not Covered:** Paywalled off-arXiv 2025–2026 articles and private repositories.

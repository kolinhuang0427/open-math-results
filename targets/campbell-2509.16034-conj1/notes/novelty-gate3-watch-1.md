# Gate 3 Novelty Receipt — `campbell-2509.16034-conj1`

- **UTC Time:** 2026-11-27T03:09:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (on rescoped Open Problems `(c1)+(c2)` per `notes/contest-ruling-audit-3.md`)

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 13 (`2026-11-27T02:43:40Z`) `watch/snapshots/1337-solved-conjectures/` -> 0 hits for `2509.16034` or Campbell–Currie–Rampersad.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond` (`gh api`, read-only):**
   - `trureturing` commits `832f82f782` / `96baee8682` settle only the odd recurrence, eq. (11), and non-$k$-automaticity (explicitly excluded by rescoping); `(c1)` sign of $\rho(4n+2)-\rho(4n)$ and `(c2)` recursion for $\rho(4n)$ have 0 matches.
   - Near misses confirmed unrelated: `aliromman/math` `CampbellCoupons` (coupon collection), `rainwangphy/aftd-platform` `CampbellHowardConditions` (cooperative coloring) & `ThueMorse*.lean` (factor coverage/random attractor), `valyuAI/research` `s03_thue.mp3`.
3. **Live Zenodo API:**
   - `https://zenodo.org/api/records?q=2509.16034&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories.

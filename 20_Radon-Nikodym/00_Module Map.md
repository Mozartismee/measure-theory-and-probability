---
type: module-map
module: radon-nikodym
status: canonical
module-status: in-progress
---

# Module Map — Radon–Nikodym

## Contract

- Object：absolutely continuous measures 與 density representation。
- Purpose：由 Hahn decomposition 構造 Radon–Nikodym derivative，並固定 theorem boundary。
- Regime：ENS 理論主線；供 conditional expectation 與 dominated models 調用。
- Prerequisites：Integration and Convergence、Signed Measures、必要的 $L^1$ interface。
- Output：可重建 finite construction、residue elimination、uniqueness 與 $\sigma$-finite gluing。

結構遵循 [Unit Structure](../00_Project/Unit%20Structure.md)。

## Competency keys

- `RN.hypotheses`：陳述 positive、signed、finite 與 $\sigma$-finite regimes 的 exact hypotheses。
- `RN.local-density`：由 Hahn structure 建立非零 local density fragment。
- `RN.maximal-mass`：構造 maximal representable submeasure。
- `RN.residue`：以 strict improvement contradiction 消去 residue。
- `RN.sigma-finite-gluing`：由 finite pieces 建立 global density。
- `RN.uniqueness`：在正確 reference measure 下證明 a.e. uniqueness。

## Files

- Cours：[Cours](01_Cours/Cours.md)
- TD：[TD 01](02_TD/TD%2001%20—%20Boundary%20and%20Local%20Domination.md)；[TD 02](02_TD/TD%2002%20—%20Constructing%20the%20Density.md)
- Corriges：[TD 01 corrigé](03_Corriges/TD%2001%20—%20Boundary%20and%20Local%20Domination.md)；[TD 02 corrigé](03_Corriges/TD%2002%20—%20Constructing%20the%20Density.md)。
- Colles：尚未建置。
- Example-Sheets：尚未建置。
- Supplements：目前無必要補件。

## Completion criterion

補齊口試鏈與 density-recognition examples；所有版本都必須明示 finiteness 或 $\sigma$-finiteness。

---
type: module-map
module: lp-interface
status: canonical
module-status: in-progress
---

# Module Map — $L^p$ Interface

## Contract

- Object：$L^1$、$L^2$、$L^\infty$ 在 measure-theoretic probability 中的可部署介面。
- Purpose：控制 integrability、test functions、moments、projection 與不同 measures 之間的轉移。
- Regime：有限範圍的基礎單元，不擴張為完整 $L^p$ 空間理論。
- Prerequisites：integration and convergence。
- Output：能使用 Hölder、Cauchy–Schwarz、Jensen，並追蹤 equivalence class 與 ambient measure。

結構遵循 [Unit Structure](../00_Project/Unit%20Structure.md)。

## Competency keys

- `LP.ambient-measure`：追蹤 $L^p(\mu)$ 的 ambient measure、equivalence class 與 finite-measure boundary。
- `LP.holder-cs-jensen`：部署 Hölder、Cauchy–Schwarz、Jensen 及 equality boundaries。
- `LP.bounded-tests`：由 indicators 合法擴張至 bounded measurable tests。
- `LP.density-change`：在 density-generated measures 與 RN reversal 間轉移。
- `LP.l2-projection`：在本模組限定範圍內部署 $L^2$ geometry 與 projection。

## Files

- Cours：[The $L^1$–$L^\infty$ Interface](01_Cours/Cours.md)；[Hölder, Jensen, and $L^2$ Geometry](01_Cours/Cours%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md)。
- Cours note：[L1 Across Measures](01_Cours/L1%20Across%20Measures.md)
- TD：[TD 01 — Integrability, Test Functions, and Change of Measure](02_TD/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md)；[TD 02 — Hölder, Jensen, and $L^2$ Geometry](02_TD/TD%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md)。
- Corriges：[TD 01 corrigé](03_Corriges/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md)；[TD 02 corrigé](03_Corriges/TD%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md)。
- Colles：尚未建置。
- Example-Sheets：尚未建置。
- Supplements：[Version Discipline](06_Supplements/Version%20Discipline.md)

## Completion criterion

補齊口試題與 moment/test-function examples；不引入 full duality 或 weak convergence。

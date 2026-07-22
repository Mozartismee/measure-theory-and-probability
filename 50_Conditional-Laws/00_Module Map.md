---
type: module-map
module: conditional-laws
status: canonical
module-status: in-progress
---

# Module Map — Conditional Laws

## Contract

- Object：conditional laws as state-space representations。
- Purpose：將 $\mathbb E[Y\mid\sigma(X)]$ 表示為 $g(X)$，並分辨 eventwise density 與 probability kernel。
- Regime：measure-theoretic probability 主線；dominated Euclidean kernel 在模組內，一般 regular conditional-law existence 與 disintegration 仍在邊界之外。
- Prerequisites：Pushforwards and Laws、Product Measures and Transformations、Conditional Expectation、Radon–Nikodym。
- Output：能構造 $d\rho_Y/d\mu_X$、轉移 versions、在 dominated Euclidean regime 建立 explicit kernel，並指出一般 eventwise construction 的邊界。

結構遵循 [Unit Structure](../00_Project/Unit%20Structure.md)。

## Competency keys

- `CL.state-space-rn`：對 $Y\in L^1(\mathbb P)$ 構造 $dX_\#(Y\mathbb P)/d\mu_X$ 並拉回 probability space。
- `CL.version-transfer`：追蹤 state-space representatives 與 composed versions 的 a.e. basis。
- `CL.dominated-kernel`：在 dominated Euclidean regime 建立 jointly measurable conditional kernel。
- `CL.eventwise-boundary`：說明 eventwise RN representatives 不足以產生一般 disintegration。

## Files

- Cours：[Cours](01_Cours/Cours.md)
- TD：[TD 01](02_TD/TD%2001%20—%20State-Space%20Representations.md)；[TD 02](02_TD/TD%2002%20—%20Dominated%20Conditional%20Densities.md)
- Corriges：[TD 02 corrigé](03_Corriges/TD%2002%20—%20Dominated%20Conditional%20Densities.md)；TD 01 corrigé 尚未建置。
- Colles：尚未建置。
- Example-Sheets：尚未建置。
- Supplements：目前無必要補件。

## Completion criterion

補齊 TD 01 corrigé、colles 與更多 discrete examples。Dominated continuous construction 已建置；任何超出此 regime 的 kernel statement 仍須補足 state-space hypotheses。

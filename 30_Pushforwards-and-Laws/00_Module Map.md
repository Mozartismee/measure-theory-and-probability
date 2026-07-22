---
type: module-map
module: pushforwards-and-laws
status: canonical
module-status: in-progress
---

# Module Map — Pushforwards and Laws

## Contract

- Object：pushforward measures、atomic and dominated laws、densities、independence、convolution、mixtures 與 terminal CLT approximation。
- Purpose：區分 probability-space object 與 state-space object，建立積分轉移，並由 product／sampling constructions 合法化離散分布族。
- Regime：measure-theoretic probability 主線與 Exam P 轉譯線。
- Prerequisites：Integration and Convergence；Radon–Nikodym 用於 density representation。
- Output：能由 pushforward definition 重建 integration formula，並處理 equality in law、atomic densities、discrete family constructions、independence as product law、convolution、mixtures、dominated densities 與 iid CLT 的終端近似邊界。

結構遵循 [Unit Structure](../00_Project/Unit%20Structure.md)。

## Competency keys

- `PF.pushforward`：由 measurable map 構造 law／pushforward measure。
- `PF.integration`：由 pushforward definition 重建 integration formula。
- `PF.counting-measure`：分離 measurable-space structure、counting measure 與 $\sigma$-finiteness boundary。
- `PF.atomic-integration`：在 countable state space 上，由 simple functions 與 MCT 重建 atomic integral 的級數表示。
- `PF.atomic-laws`：在 countable state space 上，以 counting-measure densities 構造離散 laws。
- `PF.independence`：在 joint-law 層次將 independence 表示為 product measure，並合法推出 factorization、convolution 與 independent-sum moments。
- `PF.convolution`：由 joint law 與 addition pushforward 推出 convolution，並辨認 independence boundary。
- `PF.mixtures`：構造 mixtures、Bayes reversal 與 truncation boundaries。
- `PF.dominated-laws`：相對合法 reference measure 辨認 density representation。
- `PF.clt-deployment`：在 iid、finite nonzero variance regime 下完成 standardization、continuity correction 與 normal approximation，並區分 convergence result 與 exact law identity。

## Files

- Cours：[Cours](01_Cours/Cours.md)；[Pushforward Integration Formula](01_Cours/Pushforward%20Integration%20Formula.md)；[Atomic Laws and Discrete Distribution Structures](01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md)
- TD：[TD 01](02_TD/TD%2001%20—%20Laws,%20Densities,%20and%20Mixtures.md)；[TD 02](02_TD/TD%2002%20—%20Pushforward%20and%20Radon-Nikodym.md)；[TD 03](02_TD/TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md)
- Corriges：[Corrigé TD 03](03_Corriges/Corrigé%20TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md)；TD 01 與 TD 02 尚未建置 corrigés。
- Colles：[Colle 01 — Discrete Laws and Structural Diagnosis](04_Colles/Colle%2001%20—%20Discrete%20Laws%20and%20Structural%20Diagnosis.md)
- Example-Sheets：[Example Sheet 01 — Exam P Discrete Distribution Deployment](05_Example-Sheets/Example%20Sheet%2001%20—%20Exam%20P%20Discrete%20Distribution%20Deployment.md)
- Supplements：目前無必要補件。

## Completion criterion

離散分布子循環已有 Cours、TD、corrigé、colle 與 Exam P example sheet，可獨立部署；其 independence 與 terminal CLT interfaces 已由現有 Cours 與 deployment route 承擔，不另建 convergence module。整體模組仍須補齊 TD 01、TD 02 corrigés 與 continuous transformation examples，才可由 **in-progress** 升為 **deployable**。核心 pushforward formula 留在 Cours，不降格為 supplement。

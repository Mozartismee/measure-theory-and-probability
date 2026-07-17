---
type: project-index
module: project
status: canonical
---

# 測度論：Radon–Nikodym、條件期望與條件律

本專案是一組 measure-theoretic probability 教學單元，理論標準為 ENS L3 末至 M1 初，並保留一條受控的 Exam P 轉譯線。它不企圖吞下整部測度論；百科全書式肥大通常只是沒有做出選擇。

主線為

$$
\text{integration and convergence}
\longrightarrow
\text{signed measures}
\longrightarrow
\text{Radon–Nikodym}
\longrightarrow
\text{conditional expectation}
\longrightarrow
\text{conditional laws}.
$$

Pushforwards and Laws 與 Product Measures and Transformations 構成 state-space 支線；有限 $L^p$ interface 則供應 integrability、test functions、moments 與 projection 所需的工具。

目前執行中的半個月壓縮循環統一記錄於 [Study Schedule — July Exam P Measure-Theory First Pass](00_Project/Study%20Schedule%20—%20July%20Exam%20P%20Measure-Theory%20First%20Pass.md)。完整五週版本保留為 [RN Reconstruction to Conditional Expectation — Full Mastery Reference](00_Project/Study%20Schedule%20—%20RN%20Reconstruction%20to%20Conditional%20Expectation.md)。

## 正式模組

| 順序 | 模組 | 現況 |
| --- | --- | --- |
| 10 | [Integration and Convergence](10_Integration-and-Convergence/00_Module%20Map.md) | in-progress |
| 15 | [$L^p$ Interface](15_Lp-Interface/00_Module%20Map.md) | in-progress |
| 18 | [Signed Measures](18_Signed-Measures/00_Module%20Map.md) | in-progress |
| 20 | [Radon–Nikodym](20_Radon-Nikodym/00_Module%20Map.md) | in-progress |
| 30 | [Pushforwards and Laws](30_Pushforwards-and-Laws/00_Module%20Map.md) | in-progress |
| 35 | [Product Measures and Transformations](35_Product-Measures-and-Transformations/00_Module%20Map.md) | in-progress |
| 40 | [Conditional Expectation](40_Conditional-Expectation/00_Module%20Map.md) | in-progress |
| 50 | [Conditional Laws](50_Conditional-Laws/00_Module%20Map.md) | in-progress |

每個正式模組均遵循 [Unit Structure](00_Project/Unit%20Structure.md)：

    00_Module Map
    01_Cours
    02_TD
    03_Corriges
    04_Colles
    05_Example-Sheets
    06_Supplements

目錄位置固定；內容不偽造。缺少 corrigé、colle 或 example sheet 時，Module Map 直接記載缺口。

## 建議閱讀主線

1. [Integration and Convergence](10_Integration-and-Convergence/01_Cours/Cours.md)
2. [Integration and Convergence TD](10_Integration-and-Convergence/02_TD/TD%2001%20—%20Integration%20and%20Convergence.md)
3. [The $L^1$–$L^\infty$ Interface](15_Lp-Interface/01_Cours/Cours.md)
4. [$L^1$ Across Measures](15_Lp-Interface/01_Cours/L1%20Across%20Measures.md)
5. [Hölder, Jensen, and $L^2$ Geometry](15_Lp-Interface/01_Cours/Cours%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md)
6. [$L^p$ Interface TD 01](15_Lp-Interface/02_TD/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md)
7. [$L^p$ Interface TD 02](15_Lp-Interface/02_TD/TD%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md)
8. [Signed Measures and Hahn–Jordan Decomposition](18_Signed-Measures/01_Cours/Cours.md)
9. [Signed Measures TD](18_Signed-Measures/02_TD/TD%2001%20—%20Hahn–Jordan%20Structure%20and%20Domination.md)
10. [Radon–Nikodym Cours](20_Radon-Nikodym/01_Cours/Cours.md)
11. [RN TD 01](20_Radon-Nikodym/02_TD/TD%2001%20—%20Boundary%20and%20Local%20Domination.md)
12. [RN TD 02](20_Radon-Nikodym/02_TD/TD%2002%20—%20Constructing%20the%20Density.md)
13. [Pushforwards and Laws Cours](30_Pushforwards-and-Laws/01_Cours/Cours.md)
14. [Product Measures and Transformations Cours](35_Product-Measures-and-Transformations/01_Cours/Cours.md)
15. [Conditional Expectation Cours](40_Conditional-Expectation/01_Cours/Cours.md)
16. [Conditional Expectation TD 01](40_Conditional-Expectation/02_TD/TD%2001%20—%20RN%20Construction.md)
17. [Conditional Expectation TD 02](40_Conditional-Expectation/02_TD/TD%2002%20—%20Finite%20Sigma-Fields.md)
18. [Conditional Laws Cours](50_Conditional-Laws/01_Cours/Cours.md)
19. [Conditional Laws TD 01](50_Conditional-Laws/02_TD/TD%2001%20—%20State-Space%20Representations.md)
20. [Conditional Laws TD 02 — Dominated Conditional Densities](50_Conditional-Laws/02_TD/TD%2002%20—%20Dominated%20Conditional%20Densities.md)

## 跨模組區

- [Applications](60_Applications/INDEX.md)：Exam P 轉譯與統計應用。
- [Lemmas](80_Lemmas/INDEX.md)：可獨立部署、附證明的重要引理。
- [Review](90_Review/INDEX.md)：跨模組白紙重建。
- [Sources](99_Sources/ENS/INDEX.md)：唯讀原始文獻。
- _Archive：非現行正本，不得成為主線依賴。

## 兩種 regime

### ENS 理論線

要求假設可見、證明可重建，並區分 measure、density、equivalence class、state-space object 與 probability-space object。

### Exam P 轉譯線

將同一結構還原為 transformation、mixture、total expectation、conditional density 與 Bayes calculation。入口見 [Expectation and Conditioning — Exam P Deployment Bridge](60_Applications/Exam-P-Bridges/Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md)。

## 專案規範與來源

- [專案生成規格](00_Project/PROJECT_SPEC.md)
- [教學單元結構](00_Project/Unit%20Structure.md)
- [概念依賴圖](00_Project/Dependency%20Map.md)
- [文獻與使用位置](00_Project/Bibliography.md)
- [Exam P 語義範圍](00_Project/Exam%20P%20Semantic%20Scope.md)
- [ENS 原始文獻索引](99_Sources/ENS/INDEX.md)

每一數學物件只保留一份現行正本；其餘文件以連結引用，不以複製維持表面完整。

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

目前執行中的四週學習循環統一記錄於 [[00_Project/Study Schedule — RN Reconstruction to Conditional Expectation|Study Schedule — RN Reconstruction to Conditional Expectation]]。

## 正式模組

| 順序 | 模組 | 現況 |
| --- | --- | --- |
| 10 | [[10_Integration-and-Convergence/00_Module Map|Integration and Convergence]] | in-progress |
| 15 | [[15_Lp-Interface/00_Module Map|$L^p$ Interface]] | in-progress |
| 18 | [[18_Signed-Measures/00_Module Map|Signed Measures]] | in-progress |
| 20 | [[20_Radon-Nikodym/00_Module Map|Radon–Nikodym]] | in-progress |
| 30 | [[30_Pushforwards-and-Laws/00_Module Map|Pushforwards and Laws]] | in-progress |
| 35 | [[35_Product-Measures-and-Transformations/00_Module Map|Product Measures and Transformations]] | planned |
| 40 | [[40_Conditional-Expectation/00_Module Map|Conditional Expectation]] | in-progress |
| 50 | [[50_Conditional-Laws/00_Module Map|Conditional Laws]] | in-progress |

每個正式模組均遵循 [[00_Project/Unit Structure|Unit Structure]]：

    00_Module Map
    01_Cours
    02_TD
    03_Corriges
    04_Colles
    05_Example-Sheets
    06_Supplements

目錄位置固定；內容不偽造。缺少 corrigé、colle 或 example sheet 時，Module Map 直接記載缺口。

## 建議閱讀主線

1. [[10_Integration-and-Convergence/01_Cours/Cours|Integration and Convergence]]
2. [[10_Integration-and-Convergence/02_TD/TD 01 — Integration and Convergence|Integration and Convergence TD]]
3. [[15_Lp-Interface/01_Cours/Cours|The $L^1$–$L^\infty$ Interface]]
4. [[15_Lp-Interface/01_Cours/L1 Across Measures|$L^1$ Across Measures]]
5. [[15_Lp-Interface/02_TD/TD 01 — Integrability, Test Functions, and Change of Measure|$L^p$ Interface TD]]
6. [[18_Signed-Measures/01_Cours/Cours|Signed Measures and Hahn–Jordan Decomposition]]
7. [[18_Signed-Measures/02_TD/TD 01 — Hahn–Jordan Structure and Domination|Signed Measures TD]]
8. [[20_Radon-Nikodym/01_Cours/Cours|Radon–Nikodym Cours]]
9. [[20_Radon-Nikodym/02_TD/TD 01 — Boundary and Local Domination|RN TD 01]]
10. [[20_Radon-Nikodym/02_TD/TD 02 — Constructing the Density|RN TD 02]]
11. [[30_Pushforwards-and-Laws/01_Cours/Cours|Pushforwards and Laws Cours]]
12. Product Measures and Transformations（planned）
13. [[40_Conditional-Expectation/01_Cours/Cours|Conditional Expectation Cours]]
14. [[40_Conditional-Expectation/02_TD/TD 01 — RN Construction|Conditional Expectation TD 01]]
15. [[40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields|Conditional Expectation TD 02]]
16. [[50_Conditional-Laws/01_Cours/Cours|Conditional Laws Cours]]
17. [[50_Conditional-Laws/02_TD/TD 01 — State-Space Representations|Conditional Laws TD 01]]

## 跨模組區

- [[60_Applications/INDEX|Applications]]：Exam P 轉譯與統計應用。
- [[80_Lemmas/INDEX|Lemmas]]：可獨立部署、附證明的重要引理。
- [[90_Review/INDEX|Review]]：跨模組白紙重建。
- [[99_Sources/ENS/INDEX|Sources]]：唯讀原始文獻。
- _Archive：非現行正本，不得成為主線依賴。

## 兩種 regime

### ENS 理論線

要求假設可見、證明可重建，並區分 measure、density、equivalence class、state-space object 與 probability-space object。

### Exam P 轉譯線

將同一結構還原為 transformation、mixture、total expectation、conditional density 與 Bayes calculation。入口見 [[60_Applications/Exam-P-Bridges/Measure-Theoretic Dictionary|Measure-Theoretic Dictionary for Exam P]]。

## 專案規範與來源

- [[00_Project/PROJECT_SPEC|專案生成規格]]
- [[00_Project/Unit Structure|教學單元結構]]
- [[00_Project/Dependency Map|概念依賴圖]]
- [[00_Project/Bibliography|文獻與使用位置]]
- [[00_Project/Exam P Semantic Scope|Exam P 語義範圍]]
- [[99_Sources/ENS/INDEX|ENS 原始文獻索引]]

每一數學物件只保留一份現行正本；其餘文件以連結引用，不以複製維持表面完整。

---
type: project-index
module: project
status: canonical
---

# 測度論：Radon–Nikodym、條件期望與條件律

本專案是一個 **measure-theoretic probability 核心模組**，理論標準為 ENS L3 末至 M1 初；它不是一部企圖吞下全部測度論的百科全書。

主線為

$$
\text{Radon–Nikodym}
\longrightarrow
\text{conditional expectation}
\longrightarrow
\text{conditional laws}.
$$

Pushforward、laws、densities 與 mixtures 構成另一條必要支線，並在 state-space representation 處與條件期望合流。

## 建議閱讀順序

1. [[10_Foundations/Integration and Convergence|Integration and Convergence]]
2. [[10_Foundations/TD 01 — Integration and Convergence|Integration and Convergence TD]]
3. [[10_Foundations/L1 Across Measures|$L^1$ Across Measures]]
4. [[10_Foundations/L1-Linfty Interface|The $L^1$–$L^\infty$ Interface]]
5. [[10_Foundations/Signed Measures and Hahn-Jordan Decomposition|Signed Measures and Hahn–Jordan Decomposition]]
6. [[20_Radon-Nikodym/Cours|Radon–Nikodym Cours]]
7. [[20_Radon-Nikodym/TD 01 — Boundary and Local Domination|RN TD 01]]
8. [[20_Radon-Nikodym/TD 02 — Constructing the Density|RN TD 02]]
9. [[30_Pushforwards-and-Laws/Cours|Pushforwards and Laws Cours]]
10. [[40_Conditional-Expectation/Cours|Conditional Expectation Cours]]
11. [[40_Conditional-Expectation/TD 01 — RN Construction|Conditional Expectation TD 01]]
12. [[40_Conditional-Expectation/TD 02 — Finite Sigma-Fields|Conditional Expectation TD 02]]
13. [[50_Conditional-Laws/Cours|Conditional Laws Cours]]
14. [[50_Conditional-Laws/TD 01 — State-Space Representations|Conditional Laws TD 01]]

## 檔案角色

- `Cours`：提供可部署的定義、定理、證明架構與邊界。
- `TD`：把責任留給學生，形成依賴鏈，而不是平行題庫。
- `Corriges`：完整、壓縮、可重建的解答。
- `Complements`：只處理主線之外但仍有直接依賴的結果。
- [[80_Lemmas/INDEX|`80_Lemmas`]]：可獨立部署、附證明的重要引理。
- `90_Review`：跨模組的白紙重建題。
- `99_Sources`：唯讀原始文獻；不在其中生成筆記。
- `_Archive`：非現行正本，不得作為主線依賴。

## 兩種 regime

### ENS 理論線

要求假設可見、證明可重建，並明確區分 measure、density、equivalence class、state-space object 與 probability-space object。

### Exam P 轉譯線

將同一結構還原為 transformation、mixture、total expectation、conditional density 與 Bayes calculation。入口見 [[60_Applications/Exam-P-Bridges/Measure-Theoretic Dictionary|Measure-Theoretic Dictionary for Exam P]]。

## 專案規範與來源

- [[00_Project/PROJECT_SPEC|專案生成規格]]
- [[00_Project/Dependency Map|概念依賴圖]]
- [[00_Project/Bibliography|文獻與使用位置]]
- [[00_Project/Exam P Semantic Scope|Exam P 語義範圍]]
- [[99_Sources/ENS/INDEX|ENS 原始文獻索引]]

每一數學物件只保留一份現行正本。其他文件應以連結引用，不以複製維持表面上的完整性。

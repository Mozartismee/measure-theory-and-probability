---
type: project-policy
module: project
status: canonical
---

# Structure of Teaching Units

正式教學單元一律使用同一骨架：

    XX_Module/
    ├── 00_Module Map.md
    ├── 01_Cours/
    ├── 02_TD/
    ├── 03_Corriges/
    ├── 04_Colles/
    ├── 05_Example-Sheets/
    └── 06_Supplements/

## 角色

| 位置 | 數學職能 |
| --- | --- |
| 00_Module Map | 指定 object、purpose、regime、先備、輸出與完成條件 |
| 01_Cours | 定義、核心定理、證明架構、假設邊界 |
| 02_TD | 以依賴鏈配置構造、表示、轉移與失效 |
| 03_Corriges | 完整、壓縮、可白紙重建的解答 |
| 04_Colles | 口試式定理陳述、短證明、反例與追問 |
| 05_Example-Sheets | 標準模型與計算辨認；不得偽裝成另一份 TD |
| 06_Supplements | 修補局部缺口或給出有限延伸；不得承載核心定理 |

## 完成狀態

- planned：只有合法範圍與骨架。
- in-progress：已有部分正式材料，但尚未覆蓋完整教學循環。
- deployable：Cours、TD、Corriges、Colles、Example-Sheets 均足以獨立使用。

Supplements 的位置固定，但內容不是強制項。沒有局部缺口時，空白比人工製造一份補充講義更誠實。

## 正式單元

1. Integration and Convergence
2. $L^p$ Interface
3. Signed Measures
4. Radon–Nikodym
5. Pushforwards and Laws
6. Product Measures and Transformations
7. Conditional Expectation
8. Conditional Laws

其中 $L^p$ Interface 只部署 Exam P 與主線證明需要的 $L^1$、$L^2$、$L^\infty$ 結構；它不是完整 Banach-space theory。

## 非單元目錄

00_Project、60_Applications、80_Lemmas、90_Review、99_Sources 與 _Archive 各有跨模組或保存職能，不套用教學單元骨架。

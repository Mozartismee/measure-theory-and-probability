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
| 00_Module Map | 指定 object、purpose、regime、先備、輸出、穩定 competency keys 與完成條件 |
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

## Competency keys

每個 Module Map 以 `<module>.<capability>` 宣告可被 Study Log 長期狀態引用的穩定 key，例如 `RN.uniqueness`。Key 指向數學能力，不指向某份檔案、某日排程或某次題號；只有能力本身的語義改變時才更名。Study Log 的 Mastery 與 Rupture ledgers 引用這些 keys，不重抄定義。

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

00_Project、Study Log、60_Applications、80_Lemmas、85_Examples-and-Counterexamples、90_Review、99_Sources 與 _Archive 各有跨模組、學習執行或保存職能，不套用教學單元骨架。`85_Examples-and-Counterexamples` 是非教學單元的 canonical example-pair library：保存可重用的合法 regime／移除假設後 failure 配對，不承載定理正本。Study Log 只保存 cycle、evidence 與 learner state，不承載正式數學正本。

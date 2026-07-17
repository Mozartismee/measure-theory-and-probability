# Minimal Read Routing

## 職責

本檔案只將「任務類型」映射到「最小讀取集」。它不摘要教材內容，不記錄當前 diff，也不宣告模組完成度。

## 共同入口

所有任務先讀：

1. `AGENTS.md`；
2. `.agents/HANDOFF.md`；
3. Git 分支與工作樹狀態。

然後依任務類型加載下列最小集合。

## 任務路由

| 任務類型 | 必讀 | 依需要再讀 |
| --- | --- | --- |
| 專案全局規劃或生成規格 | `00_Project/PROJECT_SPEC.md` | `00_Project/Unit Structure.md`、`00_Project/Dependency Map.md` |
| 單一模組的新增、修訂或審查 | 目標模組的 `00_Module Map.md` 與目標檔案 | Module Map 明示列出的直接先備或正本連結 |
| 跨模組依賴或主線改動 | `00_Project/Dependency Map.md` 與所涉模組的 `00_Module Map.md` | `README.md`、`00_Project/PROJECT_SPEC.md` |
| 教學單元目錄、檔案角色或完成條件 | `00_Project/Unit Structure.md` | 目標模組的 `00_Module Map.md` |
| Exam P 範圍或轉譯 | `00_Project/Exam P Semantic Scope.md` | `60_Applications/Exam-P-Bridges/Measure-Theoretic Dictionary.md` 與相關 Module Map |
| 文獻、引用或來源核對 | `00_Project/Bibliography.md` 或 `99_Sources/ENS/INDEX.md` | 只開啟任務真正所需的 PDF |
| 當前學習循環或當日作業 | `00_Project/Study Schedule — July Exam P Measure-Theory First Pass.md` 與使用者指定的 Study Log | 完整 mastery sequence 需要時再讀 `Study Schedule — RN Reconstruction to Conditional Expectation.md`；遵守當日套件的 corrigé 閱讀邊界 |
| 跨模組白紙重建或總複習 | `90_Review/INDEX.md` 與目標 review 檔案 | 該 review 明示依賴的 Module Maps |
| 引理正本的修訂 | `80_Lemmas/INDEX.md` 與目標引理 | 使用該引理的直接模組，以搜尋連結而非掃讀全文找出 |
| 內部連結、索引路徑、檔案重命名或全局連結重構 | `AGENTS.md` 的「連結與索引路徑規約」及目標檔案 | `README.md`；涉及重命名或移動時，以全專案搜尋查找反向連結 |
| 歷史還原或來源追蹤 | `_Archive/README.md` 與 Git history | 只讀特定 archived 檔案；不得當作現行正本 |

## 資訊正本路由

| 問題 | 唯一優先查閱點 |
| --- | --- |
| 「教材應如何生成或審查？」 | `00_Project/PROJECT_SPEC.md` |
| 「這個模組要做什麼、還缺什麼？」 | 該模組的 `00_Module Map.md` |
| 「概念依賴是什麼？」 | `00_Project/Dependency Map.md` |
| 「這類檔案的職能是什麼？」 | `00_Project/Unit Structure.md` |
| 「這是否屬於 Exam P 核心？」 | `00_Project/Exam P Semantic Scope.md` |
| 「文獻放在哪裡、用在哪裡？」 | `00_Project/Bibliography.md` 或 `99_Sources/ENS/INDEX.md` |
| 「專案內部連結與索引路徑應如何生成？」 | `AGENTS.md` 的「連結與索引路徑規約」 |
| 「現在檔案怎麼了？」 | Git；不查 meta 摘要 |
| 「上一位 Agent 為何停下？」 | `.agents/HANDOFF.md` |

## 擴大掃描的條件

只在下列情形擴大到全專案搜尋或掃描：

- 任務本質上是跨模組一致性審查；
- 需要重命名或移動正本，必須查找所有反向連結；
- 懷疑存在重複正本、孤兒檔案或狀態矛盾；
- 使用者明確要求全局盤點。

否則，先用檔名、Obsidian 連結或精確詞彙定位，再讀相關片段。「我先全部看完」通常不是方法，只是精神上比較體面的延後。

## 預設不讀區

- `99_Sources/**/*.pdf`：除非任務需要原始證據、引用或對照。
- `_Archive/`：除非任務是歷史還原或來源追蹤。
- 無關模組的 `Cours`、`TD` 與 `Corriges`：除非依賴關係已被明示驗證。
- 學習套件禁止提前閱讀的 corrigé：不得因 Agent 貪圖方便而越界。

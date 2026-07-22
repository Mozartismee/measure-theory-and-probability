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
| 正式教材或課程路線的 ENS corpus 校準 | 目標 production Skill、`00_Project/PROJECT_SPEC.md`、`00_Project/Bibliography.md` 與 `99_Sources/ENS/INDEX.md` | 先以目標 Module Map 與 canonical Cours 固定 legal frontier，再讀一個相關子索引與最多三個被選中的 source units；不得掃描整個 PDF tree |
| 當前學習循環或當日作業 | `Study Log/State/CURRENT.md`，再讀其明示的 active plan、latest Daily 與 active packet；已有 self-contained session packet 時，以該 packet 為整場唯一作答入口 | 只讀 session packet 明示的 supplement／corrigé；完整 mastery sequence 需要時再讀 `00_Project/Training Route — RN Reconstruction to Conditional Expectation.md`；遵守 corrigé 閱讀邊界 |
| 依日期尋找既有學習材料 | `Study Log/00_Chronology.md` | 只開啟該日期列明示的 packet、session 或 Daily；不掃描整個 Study Log |
| 長期學習診斷或下一 cycle 規劃 | `Study Log/State/CURRENT.md`、`MASTERY.md`、`RUPTURES.md`、`CYCLES.md` | 只回查 decisive evidence links 與所涉 Module Maps；不得掃描全部 Daily 重建狀態 |
| 跨模組白紙重建或總複習 | `90_Review/INDEX.md` 與目標 review 檔案 | 該 review 明示依賴的 Module Maps |
| 引理候選抽取、新增、修訂或重編號 | 原始內容、所屬模組的 `00_Module Map.md`、`80_Lemmas/INDEX.md` 與直接相關引理 | 以搜尋找出直接 consumers 與 backlinks；依學習者程度校準時再讀 `CURRENT.md` 及相關 `MASTERY.md`／`RUPTURES.md`；重編號或 registry 結構變動時才做全庫影響分析 |
| 正反例的查找、新增或審查 | `85_Examples-and-Counterexamples/INDEX.md` 與目標 example pair | 該 pair 明示的 canonical sources 與 competency keys 所屬 Module Maps |
| 內部連結、索引路徑、檔案重命名或全局連結重構 | `AGENTS.md` 的「連結與索引路徑規約」及目標檔案；涉及 Study Log 層級時另讀 `Study Log/README.md` | `README.md`；涉及重命名或移動時，以全專案搜尋查找反向連結 |
| 歷史還原或來源追蹤 | `_Archive/README.md` 與 Git history | 只讀特定 archived 檔案；不得當作現行正本 |

## 資訊正本路由

Study Log 中標記 `math-authority: derived` 的 packet 或 séance 可用於安排、作答與批改當場工作；它不是最新數學主張的正本。若任務需要判斷定理、假設、證明或修訂數學內容，必須沿其 `canonical-sources` 回到正式模組或 `80_Lemmas`。

| 問題 | 唯一優先查閱點 |
| --- | --- |
| 「教材應如何生成或審查？」 | `00_Project/PROJECT_SPEC.md` |
| 「這個模組要做什麼、還缺什麼？」 | 該模組的 `00_Module Map.md` |
| 「概念依賴是什麼？」 | `00_Project/Dependency Map.md` |
| 「這類檔案的職能是什麼？」 | `00_Project/Unit Structure.md` |
| 「這是否屬於 Exam P 核心？」 | `00_Project/Exam P Semantic Scope.md` |
| 「文獻放在哪裡、用在哪裡？」 | `00_Project/Bibliography.md` 或 `99_Sources/ENS/INDEX.md` |
| 「Study Log 的 cycle、packet、session、Daily 與 State 如何歸類？」 | `Study Log/README.md` |
| 「某一天的教材現在放在哪裡？」 | `Study Log/00_Chronology.md` |
| 「專案內部連結與索引路徑應如何生成？」 | `AGENTS.md` 的「連結與索引路徑規約」 |
| 「現在學到哪裡、下一場做什麼？」 | `Study Log/State/CURRENT.md` |
| 「哪些能力已有閉卷證據？」 | `Study Log/State/MASTERY.md` |
| 「哪些結構 rupture 尚未解除？」 | `Study Log/State/RUPTURES.md` |
| 「今天實際發生什麼？」 | 當日 `Study Log/Daily/YYYY/MM/YYYY-MM-DD.md`，再讀其中連結的 packet records |
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
- 歷史 Daily、已關閉 packets、LaTeX sources、PDF 與 zip：除非 current State 或證據核對明示需要。
- 學習套件禁止提前閱讀的 corrigé：不得因 Agent 貪圖方便而越界。

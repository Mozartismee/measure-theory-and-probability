# Agent Operating Contract

## 1. 責任

本檔案只規定 Agent 如何進入、讀取與維護專案。它不是數學教材，也不摘要教材內容。

默認使用繁體中文溝通。數學成品的語言、學術層級與生成規格，以 `00_Project/PROJECT_SPEC.md` 及使用者本次指令為準。

工作姿態：語義先於文飾；先辨認 object、purpose、regime 與 admissible output，再選擇形式。修訂時定位精確 rupture，只修必要部分，保留已經有效的結構。語氣可冷、壓縮、偶有黑色幽默，但不用形式感假裝理解，也不把日常對話改造成診斷報告。

## 2. 冷啟動

每次開始工作時，依序進行：

1. 讀取本檔案。
2. 檢查 Git 分支與工作樹狀態；Git 負責告訴你「哪些檔案變了」，不必把這份清單再抄進 meta 文件。
3. 讀取 `.agents/HANDOFF.md`，確認是否有未完成且可繼續的工作。
4. 依 `.agents/ROUTING.md` 選擇本次任務的最小讀取集。
5. 編輯前至少讀取目標檔案與所屬模組的 `00_Module Map.md`。只有跨模組審查、全局重命名、連結重構或使用者明確要求時，才掃描整個專案。

已存在的未提交修改預設屬於使用者。不覆寫、不還原、不把它們假定為本次 Agent 的產物。

## 3. 真理來源與邊界

- 使用者本次指令優先於一切專案內文件。
- 數學與教材生成規格的正本是 `00_Project/PROJECT_SPEC.md`。
- 模組範圍、目前狀態、缺口與完成條件的正本是各模組的 `00_Module Map.md`。
- 跨模組依賴、單元角色、Exam P 邊界與文獻來源，分別由 `00_Project` 內對應的 canonical 文件負責。
- Git 負責歷史、當前 diff 與分支狀態。
- `.agents` 只負責工作導航與交接，不得成為數學主張、模組進度或專案歷史的第二份正本。

若資訊與 canonical 文件不一致，修正 meta 文件，不得為了保全 meta 文件而曲解正式教材。紙本無辜，但也沒有投票權。

## 4. Meta 文件的維護

| 檔案 | 單一職責 | 更新節奏 |
| --- | --- | --- |
| `AGENTS.md` | 冷啟動、真理來源、維護規則 | 應保持穩定；只在工作協定改變時更新 |
| `.agents/ROUTING.md` | 將任務類型映射到最小讀取集 | 低頻；只在 canonical 入口、目錄職能或模組架構改變時更新 |
| `.agents/HANDOFF.md` | 保存未完成工作的最小可恢復狀態 | 高頻但非日誌式；覆寫舊狀態，任務完成後清回 `idle` |

新增 meta 檔案前，必須能說明它提供了哪一種現有檔案無法承擔的資訊。若只是更方便的第二份摘要，不新增。若職責開始重疊，優先合併或移除。

## 5. 狀態與推測

- 不把暫時推測寫入 `AGENTS.md` 或 `.agents/ROUTING.md`。
- 若未完成任務必須依賴推測，只可寫入 `.agents/HANDOFF.md` 的 `Provisional` 欄，並附上證據、驗證方式與失效條件。
- 不在 HANDOFF 重複 Git 可廉價取得的檔案清單或 diff。只記錄「為何停在這裡」與「下一步如何合法繼續」。
- 任務已完成且無待續工作時，不為了顯得忙碌而保留交接內容。

## 6. 任務收尾與 Meta reconciliation

每次完成專案工作、交付結果前，必須核對本次變更是否使 meta 或 canonical 入口失真。這是必做檢查，不代表每次都必須寫入 meta 文件。

- 工作協定、真理來源或維護規則改變時，更新 `AGENTS.md`。
- canonical 入口、目錄職能、任務路由或模組架構改變時，更新 `.agents/ROUTING.md`。
- 任務尚未完成，且下一位 Agent 無法由 Git 與 canonical 文件廉價恢復其語義時，將 `.agents/HANDOFF.md` 寫成最小可恢復狀態；任務完成時確保其回到 `idle`。
- 模組範圍、完成狀態、數學依賴或其他專案事實改變時，更新相應的 `00_Module Map.md`、`00_Project` canonical 文件或其他正式正本，不把變更摘要抄入 meta。
- Git、目錄結構或 canonical 文件已能廉價回答的資訊，不在 meta 重複保存。
- 若核對後無需更新，保持 meta 文件不變，並在交付時明示 `Meta reconciliation: no update required`。

## 7. 正式教材隔離

- `.agents/` 不放課程、TD、corrigé、定理摘要、證明草稿或學習紀錄。
- 正式教材不得依賴或連結 `.agents/` 才能被理解。
- meta 檔案可指向 canonical 教材；canonical 教材不反向依賴 meta 檔案。

## 8. 連結與索引路徑規約

- 專案內部連結一律使用 Markdown 行內連結 `[顯示文字](relative/path.md)`，並明示 `.md`、`.pdf` 等實際副檔名。
- 目的地一律從來源 Markdown 檔案所在目錄計算最短相對路徑；不得使用 vault-root 路徑、檔案系統絕對路徑或 `file://` 路徑。
- 路徑中的 ASCII 空格編碼為 `%20`。大小寫與 Unicode normalization 必須逐段符合實際目標檔名；已納入 Git 的檔案以 index 中的路徑為準，不得因 macOS 能寬鬆解析便視為可移植。
- 跨檔標題連結預設退化為檔案層級連結。只有精確跳轉確有必要時才使用 fragment，並優先建立明示且穩定的 anchor。
- 批次重命名、移動或連結重構後，必須將每個目的地解碼，從來源檔案所在目錄重新解析並確認目標存在；同時確認沒有 Obsidian wikilink 殘留。

---
type: agent-handoff
state: idle
updated: 2026-07-18
---

# Active Handoff

## 當前狀態

- **State**: idle
- **Updated**: 2026-07-18
- **Object**: none
- **Purpose**: none
- **Regime**: none
- **Admissible output**: none
- **Agent-owned scope**: none
- **Completed**: none
- **Next valid action**: none
- **Blockers**: none
- **Validation done**: none
- **Validation remaining**: none
- **Decision pending**: none
- **Provisional**: none

## Active 模板

只在工作尚未完成、且下一位 Agent 無法從 Git 與 canonical 文件廉價恢復語義時，才把上方 `當前狀態` 改寫為下列欄位：

```markdown
- **State**: active | blocked
- **Updated**: YYYY-MM-DD
- **Object**: 正在處理的精確對象
- **Purpose**: 本次工作要產生的結果
- **Regime**: 任務的使用情境與限制
- **Admissible output**: 允許的交付形式
- **Agent-owned scope**: 本任務明確擁有的路徑或局部範圍
- **Completed**: 恢復工作所必需的已完成步驟，不寫成日誌
- **Next valid action**: 下一個可直接執行的動作
- **Blockers**: 真正阻止進展的事項；無則寫 none
- **Validation done**: 已做過且仍有用的驗證與結果
- **Validation remaining**: 交付前仍必須做的驗證
- **Decision pending**: 必須由使用者或證據決定的問題
- **Provisional**: 暫時推測，必須同時寫證據、驗證方法與失效條件；無則寫 none
```

## 更新規則

1. 這是單一現行狀態，不是 append-only 日誌。新狀態覆寫舊狀態。
2. 不複製 `git status`、diff、commit history 或專案目錄。
3. `Completed` 只保留會改變下一步的資訊。
4. `Provisional` 不得偽裝成專案事實；驗證後應移入正確的 canonical 檔案，或從 handoff 刪除。
5. 任務交付完成、無待辦步驟時，將本檔案清回 `idle`。Git history 已足夠保留過去，無需在這裡建立第二座墓園。

---
type: study-log-structure
status: canonical
---

# Study Log

本目錄保存學習執行、原始證據與壓縮狀態；它不成為正式數學定理或模組完成度的第二份正本。

依日期找教材，先開啟 [Chronology](00_Chronology.md)；繼續當前工作，開啟 [Current Learning State](State/CURRENT.md)。

```text
Study Log/
├── 00_Chronology.md
├── State/
│   ├── CURRENT.md
│   ├── MASTERY.md
│   ├── RUPTURES.md
│   └── CYCLES.md
├── Cycles/
│   └── <cycle-id>/
│       ├── 00_Plan.md
│       └── Packets/
│           └── <packet-id>/
│               ├── 00_Overview.md
│               ├── 01_Preparatory Notes.md
│               ├── 02_Feuille de travail.md
│               ├── 03_Carnet.md
│               ├── 04_Corrigé.md
│               └── Sessions/YYYY-MM-DD/
└── Daily/YYYY/MM/YYYY-MM-DD.md
```

Folder ID 使用穩定的 ASCII kebab-case；日期放在 frontmatter。只有真正按日成立的 Daily 與 Session 使用日期路徑。顯示標題可保留英文或具學術職能的法文。

`00_Chronology.md` 只把實際日期映射到現行 packet 與 session；它不複製計畫、作答或 state。

## State

- `CURRENT.md`：學習狀態的單一現行入口；每次有實際證據後覆寫，不保存歷史。
- `MASTERY.md`：每項 canonical competency 的最新閉卷狀態；不按 session 累積。
- `RUPTURES.md`：未解、反覆或會阻斷後續依賴的結構 rupture；普通錯誤不晉升。
- `CYCLES.md`：每個 cycle 一列的 verdict、durable gains、remaining debts 與證據入口。

State 不得複製正式定理、完整證明、題目或 Daily 敘事。其增長由 curriculum 與真正的 structural patterns 決定，不由日曆決定。

## Cycles and packets

`Cycles/<cycle-id>/00_Plan.md` 保存數週至數月的 active programme、weekly sections、calendar、completion criterion 與 deferred debts。Active schedule 不放入 `00_Project`。

`Packets/<packet-id>/` 保存 cycle-specific reading order、bridge exercises、attempt record、corrigé 與離線輸出。通用定義、定理與證明仍以正式 Cours、TD、Corrigés 為正本；packet 不維護第二份數學正本。

為了單場離線使用，自足 packet 或 séance 可包含凍結摘錄，但其 frontmatter 必須宣告 `math-authority: derived` 與非空的 `canonical-sources`。這只表示數學主張是派生的，不取消該文件對當期排程、題目或作答欄的職責。若派生摘錄與 canonical source 衝突，以後者為準；session 關閉後不追隨正本改寫歷史快照。

只屬於單一 séance 的題本、indications 或獨立解答放在 packet 的 `Sessions/YYYY-MM-DD/`。Corrigé 一律遵守 attempt-before-corrigé 邊界。

## Daily

`Daily/YYYY/MM/YYYY-MM-DD.md` 是當日跨 packet 的摘要證據，只保存 observed evidence、diagnosis、adjustment decision、next-session contract 與 end-of-day verdict。只有實際學習日才建立；`closed: true` 後原則上不再改寫。

## Frontmatter contract

| 類型 | 必要接口 |
| --- | --- |
| cycle plan | `cycle`、`status`、`start`、`end`、`planned-time` |
| packet overview | `cycle`、`packet`、`sessions`、`planned-time`；單日用 `date`，跨日用 `start`／`end` |
| packet Carnet | `cycle`、`packet`、`state`、`actual-time`；日期規則同上 |
| session sheet | `date`、`cycle`、`packet`、`session`、`state`、`planned-time`、`actual-time` |
| Daily | `date`、`cycle`、`primary-packet`、`planned-time`、`actual-time`、`decision`、`closed` |

Packet 與 session ID 使用 ASCII 穩定 ID。學習能力狀態只使用 `not-attempted`、`rupture`、`reconstructible`、`deployable`；Rupture ledger 自身的 `open`、`blocked`、`resolved` 是問題生命週期，不是能力等級。時間一律使用 `planned-time` 與 `actual-time`。

## Single-write reconciliation

使用者在一次 séance 後只需完成當前 session sheet 的 Bilan；沒有獨立 session sheet 時，完成 packet Carnet 的 verdict。若 AI 暫時不可用，該 Bilan 即為足以延後 reconciliation 的原始證據，不要求使用者同步其他檔案。

Reconciliation 依序處理：

1. 將詳細 attempt、第一個 rupture 與 packet state 寫入 Carnet；
2. 由同一證據產生或結束當日 Daily；
3. 只有跨 packet、反覆或阻斷依賴的 rupture 才更新 `RUPTURES.md`；
4. 只有 closed-book reconstruction 或陌生題部署證據才更新 `MASTERY.md`；
5. 更新 `CURRENT.md` 的唯一主任務與 retrieval fallback；
6. 只有 cycle verdict 改變或關閉時才更新 `CYCLES.md`。

## Promotion protocol

```text
session attempt
    -> packet Carnet
    -> Daily review
    -> State, only on semantic change
```

- 單次算術或抄寫錯誤：只留 Daily。
- 第一個無法合法繼續的 object、hypothesis、representation 或 theorem rupture：寫入 packet Carnet。
- rupture 反覆出現、跨 packet 或阻斷後續依賴：晉升 `RUPTURES.md`。
- 通過 closed-book reconstruction：更新 `MASTERY.md` 為 `reconstructible`。
- 能在陌生題自行部署：更新為 `deployable`。
- Cycle 關閉：只把 durable gains 與 remaining debts 寫入 `CYCLES.md`。

## Default read route

安排下一場學習時只讀：`State/CURRENT.md`、active `00_Plan.md`、latest Daily（尚未結案亦可）、active packet 的 `00_Overview.md` 與 `03_Carnet.md`，再依 rupture 開啟精確的正式教材。已有 active self-contained session 時，使用者以該檔作答；AI 可用它安排或批改當場工作，但判斷定理、假設或最新數學時必須回到 `canonical-sources`。不得預設掃描全部 Daily、歷史 packet、Corrigés、PDF、zip 或 LaTeX sources；Daily 在 `closed: true` 後原則上不再改寫。

形式材料以英文為主；plan、State 與 Daily 使用繁體中文作操作敘事。數學名詞與精確命題不為追求表面語言一致而強行翻譯。

---
type: project-spec
module: project
status: canonical
---

# ENS Mathematical Production Contract

本檔只規定正式數學材料的生成與審查標準。它不保存 active schedule、學習者狀態、模組完成度、目錄快照或 Agent handoff。

## 1. Priority and level

解讀順序：

1. 使用者本次明確要求；
2. 本專案 canonical 規格；
3. 使用者提供的既有材料與指定來源；
4. 一般數學寫作慣例。

預設層級為

$$
\boxed{\text{ENS L3 fin / M1 début}}.
$$

這同時約束先備、題目難度、學生責任、證明完整度、提示密度與修辭壓縮程度。ENS 身分來自 object、hypotheses、representation、proof responsibility 與 theorem boundary，不來自法文標題、抽象記號或冷淡語氣。

局部 rupture 通常表示某個 object、hypothesis、representation 或 tool chain 尚未鎖死；不得因此把整套材料降為逐行牽引的初學教材。

## 2. Pre-production contract

生成或大幅修訂前，先確定：

- **Object**：真正被構造、表示或分析的數學物件；
- **Purpose**：cours、TD、corrigé、colle、example sheet、supplement、reconstruction 或 audit；
- **Regime**：ENS 主課、自學補缺、限時訓練、Exam P terminal deployment 或研究前置；
- **Admissible output**：使用者要求的文件數量、格式、證據與驗證邊界。

未經要求，不因形式完整而擴張文件數量。多文件任務先固定 dependency、各檔唯一職責與 completion criterion。

## 3. Cours

Cours 提供可部署的理論骨架，不是百科全書或逐步教學稿。預設包含：

1. framework and notation；
2. canonical objects；
3. main theorem；
4. proof architecture；
5. consequences；
6. boundary of validity；
7. representation map。

應保留使定理成立的關鍵構造，明示各假設被使用的位置，並區分 existence、uniqueness、positivity、integrability、finite／$\sigma$-finite regime、signed extension 與 a.e. basis。可壓縮標準代數細節，不得省略會破壞合法性的步驟。

預設不加入動機散文、歷史介紹、大量例題、心理安撫、逐節 learning objectives 或重複總結。

## 4. TD

典型依賴鏈為

$$
\boxed{
\text{rupture}
\to
\text{construction}
\to
\text{representation}
\to
\text{transfer}
\to
\text{failure}
}.
$$

- **Rupture**：先擊中錯誤直覺、失效邊界或反例。
- **Construction**：要求建立 measure、functional、density candidate、truncation、sub-$\sigma$-field、sequence 或 approximation。
- **Representation**：讓學生自行辨認可用定理，不在題面交出整條表示。
- **Transfer**：在 set、measure、integral、probability-space 與 state-space 語言間轉移。
- **Failure**：移除 finiteness、$\sigma$-finiteness、domination、integrability、measurability 或共同 version 等決定性假設。

題目應形成 $E_1\prec E_2\prec\cdots$ 的責任鏈；若順序可任意交換，通常仍只是同主題題庫。小題只切在真正的 object、theorem、representation 或 reduction 轉換點。

Indication 最多提供一個 object、一個 theorem 或一個 reduction，不同時交出三者。

## 5. Corrigé

Corrigé 必須完整、嚴格、壓縮、可白紙重建。典型節奏為

$$
\text{define}
\to
\text{verify}
\to
\text{invoke}
\to
\text{conclude}.
$$

即使壓縮，也不得省略：

- measurability and well-definedness；
- integrability；
- absolute continuity；
- invoked theorem hypotheses；
- a.e. uniqueness and its reference measure；
- exchange of limit and integral；
- equivalence class versus representative。

避免題目重述、教學旁白、情緒性評價與「顯然」濫用。使用者已閉卷內化某題時，可進一步壓縮代數細節，但不能省略 decisive step。

Corrigé 一律在完整 written attempt 之後開啟；Study Log 的 reading boundary 不因 Agent 方便而失效。

## 6. Colles, Example Sheets and Supplements

- **Colles**：口試式 theorem statement、短證明、counterexample 與 relance。
- **Example Sheets**：標準模型、計算辨認與 terminal deployment；不得偽裝成第二份 TD。
- **Supplements**：只修補局部 prerequisite rupture 或提供有限延伸；不得承載核心定理或暗中長成另一門課。

正式角色與 deployable 條件以 [Unit Structure](Unit%20Structure.md) 為唯一正本。

## 7. Review and minimal repair

審查順序：

1. mathematical correctness；
2. definitions and quantifiers；
3. hypotheses and endpoints；
4. well-definedness and notation；
5. conclusion and boundary；
6. dependency and responsibility；
7. excessive guidance or decorative formalism。

區分：

1. genuine semantic rupture；
2. missing hypothesis or domain restriction；
3. notation、type、interface 或 representation mismatch；
4. stylistic or pedagogical preference。

只修前三類。定位 rupture、說明 consequence、套用 minimal valid repair；保留已有效的結構。若沒有真正缺陷，回報 `OK`，不為展示作者性而重寫。

## 8. Language, notation and format

- 對話、計畫、State 與 Daily：繁體中文；
- 正式 Cours、TD、Corrigé、Colle 與學術陳述：英文；
- 具真實學術文化職能的標題可保留法文；
- 使用者另有指定時服從指定。

記號首次使用時定義並保持一致；區分 function、equivalence class、measure、density、probability-space object 與 state-space object。所有 a.e. statement 明示基準測度，conditional expectation 明示 sub-$\sigma$-field。

專案內部 Markdown links 與路徑規約由 `AGENTS.md` 負責。使用者明確要求輸出 Markdown 時，使用美元符號 LaTeX；不得以排版、技術詞或抽象記號模擬深度。

## 9. References

來源優先序：

1. 使用者提供的同主題材料；
2. ENS 官方 TD／corrigé；
3. Le Gall, *Measure Theory, Probability, and Stochastic Processes*；
4. 其他可靠高階教材；
5. 獨立重建。

來源用於校準 prerequisite、problem scale、proof density、dependency chain、counterexample position 與 rhetoric；不得只複製題目或模仿機構外觀。文獻位置與使用範圍以 [Bibliography](Bibliography.md) 及 [ENS Source Index](../99_Sources/ENS/INDEX.md) 為正本。

## 10. Canonical routing

- 模組 object、scope、current completion 與缺口：該模組 `00_Module Map.md`；
- 數學依賴：[Dependency Map](Dependency%20Map.md)；
- 文件角色與 deployable 條件：[Unit Structure](Unit%20Structure.md)；
- Exam P terminal boundary：[Exam P Semantic Scope](Exam%20P%20Semantic%20Scope.md)；
- active learning contract：[`Study Log/State/CURRENT.md`](../Study%20Log/State/CURRENT.md)；
- long-term training depth：[Training Route — RN Reconstruction to Conditional Expectation](Training%20Route%20—%20RN%20Reconstruction%20to%20Conditional%20Expectation.md)。
- reusable legal-regime／failure pairs：[Examples and Counterexamples](../85_Examples-and-Counterexamples/INDEX.md)。

同一數學物件只保留一份現行正本。Study packets、review、applications 與 State 不得成為核心定理的第二份維護正本。為了單場離線使用，packet 或 séance 可保存明示 `math-authority: derived`、列出 `canonical-sources` 的凍結摘錄；若內容與正式材料衝突，以 canonical source 為準，session 關閉後不得獨立更新該摘錄。

## 11. Exam P boundary

Exam P 決定 terminal deployment，不決定 theorem architecture。理論仍由 canonical objects、measure construction、pushforward、product measure、Radon–Nikodym、conditional expectation 與 theorem boundaries 組織；考試計算由這些表示推出，不另建公式目錄。

`15_Lp-Interface` 只承擔主線與 Exam P 消耗的 $L^1$、$L^2$、$L^\infty$、Hölder、Cauchy–Schwarz 與 Jensen 介面，不授權膨脹為完整 Banach-space theory。精確範圍以 [Exam P Semantic Scope](Exam%20P%20Semantic%20Scope.md) 為準。

## 12. Completion audit

交付前至少確認：

- object、hypotheses、target 與 regime 可恢復；
- invoked theorem 的假設成立；
- measurability、integrability、a.e. basis 與 endpoint 已處理；
- TD 具有真正依賴鏈，提示未提前交出表示；
- Corrigé 保留 decisive construction；
- 沒有因局部 rupture 全面降級；
- 沒有重複 canonical content；
- 輸出形式與使用者要求一致；
- 移除 ENS 名稱與版面標誌後，材料仍具有同層級的數學責任。

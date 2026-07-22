---
type: study-cycle-plan
status: active
edition: compressed-first-pass
cycle: 2026-07-exam-p-first-pass
derived-from: rn-reconstruction-to-conditional-expectation
start: 2026-07-17
end: 2026-07-31
timezone: Asia/Taipei
planned-time: 20h30m
prerequisite-date: 2026-07-14
prerequisite-time: 1h30m
total-including-prerequisite: 22h
scope-lock-updated: 2026-07-22
scope-locked-through: 2026-07-31
math-authority: derived
canonical-sources:
  - ../../../00_Project/Training Route — RN Reconstruction to Conditional Expectation.md
  - ../../../00_Project/Dependency Map.md
  - ../../../00_Project/Exam P Semantic Scope.md
---

# Cycle Plan — July Exam P Measure-Theory First Pass

## Contract

- **Object**：$L^p$ admissibility、expectation、pushforward laws、independence、product integration、finite and RN conditioning、dominated conditional densities，以及 CLT 的終端近似介面。
- **Purpose**：在 2026 年 7 月底前完成 Exam P 可部署的第一輪測度論基礎。
- **Regime**：原五週 [full mastery edition](../../../00_Project/Training%20Route%20—%20RN%20Reconstruction%20to%20Conditional%20Expectation.md) 的半個月壓縮版；ENS L3+/M1 legitimacy，Exam P terminal deployment。
- **Admissible output**：function-space gate、theorem boundary、representation chain、density ledger、閉卷 reconstruction、官方題型的結構辨認。
- **RN depth**：視為已有基礎；複習 exact hypotheses、reference measure 與 uniqueness，完整 Hahn-first proof 延後。

壓縮版不是等比例加速。它保留被 Exam P deployment 消耗的介面，並把未完成的完整證明明列為 deferred mastery debts。

## Scope lock — 23 to 31 July

本節是 2026-07-23 至 2026-07-31 的排程正本。除非使用者明示改變目標、官方 Exam P 範圍改變，或現行任務出現使後續步驟在數學上不合法的 prerequisite rupture，後續規劃不得任意新增或刪除章節。局部遺忘先在既有場次內作 minimal repair；不得因此另開新模組、擴張 Lemma 庫或重排整條主線。

### Planning premise

- 依使用者 2026-07-22 的指令，已生成內容在本排程中按「大約掌握八成」處理；Study Log 未記錄的部分不自動成為補課債務。
- 這是排程前提，不是 `MASTERY.md` 的閉卷證據，也不把既有 rupture ledger 自動改寫為 resolved。
- Adjustment decision 固定為 `continue`。實作中若發現局部缺口，只修第一個阻斷步驟；除上述 scope-change 條件成立外，不改變本節的終端範圍。

### Frozen terminal scope

1. **Independence is mandatory**：events、random variables、joint law as product law、factorization、convolution、variance of independent sums、conditional-independence boundary，以及 independence 對 conditional expectation 的直接後果。
2. **Probability convergence is bounded**：只保留 convergence in distribution 的語義、iid CLT、standardization、continuity correction 與 approximation boundary。完整 almost-sure／in-probability／$L^p$／weak-convergence theory 延後。
3. **No July expansion**：不新增一般 kernels、disintegration、完整 $L^2$ projection、RN 的 Hahn-first construction、product measure 的 outer-measure construction或新的 canonical Lemma。

### Revision rule

- 新增 mandatory topic 必須同時指出它被哪個 Exam P outcome 或現有 dependency 直接消耗，並在固定總時數內取代等量工作；不得只把分鐘數往上疊。
- 已列 mandatory topic 只有在證明與 Exam P terminal deployment 無關後才能刪除。
- 缺日誌、熟悉度波動或 Agent 更換本身均不構成改動本節的理由。

## Prerequisite and active packets

| 套件 | 日期 | 計時責任 | 職能 |
| --- | --- | --- | --- |
| [$L^p$ Interfaces, Density Measures, and RN Deployment](Packets/lp-rn-interface/00_Overview.md) | 2026-07-14 | 90m prerequisite；不計入 active 20h30m | 建立 $L^p$ object、bounded tests、density generation 與 RN review interface |
| [Expectation and Finite Conditioning](Packets/expectation-finite-conditioning/00_Overview.md) | 2026-07-17 to 2026-07-20 | active 450m | 承接 7/14，建立 expectation／finite conditioning bridge，並以 J3bis 認證一般 conditional expectation 骨架 |
| [7/18 Generated $\sigma$-Fields and Counting Measures](Packets/expectation-finite-conditioning/Sessions/2026-07-18/00_Séance.md) | 2026-07-18 | replaces J2 120m；計入原 active 330m | 修復 sections、counting measure 與 atomic integral 的 primary ruptures |
| [Product Integration to Conditional Density](Packets/product-to-conditional-density/00_Overview.md) | 2026-07-23 to 2026-07-31 | active 780m | 完成 product、independence、RN deployment、conditional density、CLT bridge 與 Exam P audit |

## Canonical materials

| Code | 教材 | 職能 |
| --- | --- | --- |
| IC-C | [Integration and Convergence](../../../10_Integration-and-Convergence/01_Cours/Cours.md) | expectation construction、MCT／DCT |
| LP-C | [$L^1$–$L^\infty$ Interface](../../../15_Lp-Interface/01_Cours/Cours.md) | density-generated measures、bounded tests |
| LP-C2 | [Hölder, Jensen, and $L^2$ Geometry](../../../15_Lp-Interface/01_Cours/Cours%2002%20—%20Hölder,%20Jensen,%20and%20L2%20Geometry.md) | moment hierarchy、Cauchy–Schwarz、minimal variance interface |
| LP-TD1 | [$L^p$ Interface TD](../../../15_Lp-Interface/02_TD/TD%2001%20—%20Integrability,%20Test%20Functions,%20and%20Change%20of%20Measure.md) | finite-measure embedding、bounded tests、density generation、measure change |
| RN-C | [Radon–Nikodym Cours](../../../20_Radon-Nikodym/01_Cours/Cours.md) | theorem boundary review only |
| PF-C | [Pushforwards and Laws](../../../30_Pushforwards-and-Laws/01_Cours/Cours.md) | LOTUS、laws、mixtures |
| PF-C2 | [Atomic Laws and Discrete Distribution Structures](../../../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) | independence as product law、convolution、independent sums、CLT boundary |
| PM-C | [Product Measures Cours](../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md) | Tonelli／Fubini、marginals、Jacobian |
| PM-TD | [Product Measures TD](../../../35_Product-Measures-and-Transformations/02_TD/TD%2001%20—%20Product%20Measures,%20Iterated%20Integrals,%20and%20Transformations.md) | indicator Tonelli、failure、layer cake、marginalization |
| CE-C | [Conditional Expectation Cours](../../../40_Conditional-Expectation/01_Cours/Cours.md) | RN construction、tower、finite conditioning |
| CL-C | [Conditional Laws Cours](../../../50_Conditional-Laws/01_Cours/Cours.md) | state-space and dominated representations |
| CL-TD2 | [Dominated Conditional Densities TD](../../../50_Conditional-Laws/02_TD/TD%2002%20—%20Dominated%20Conditional%20Densities.md) | explicit kernel and mixture Bayes |
| LEDGER | [Density and Version Ledger](../../../90_Review/Density%20and%20Version%20Ledger.md) | RN multi-context bookkeeping |
| EP-B | [Exam P Deployment Bridge](../../../60_Applications/Exam-P-Bridges/Expectation%20and%20Conditioning%20—%20Exam%20P%20Deployment%20Bridge.md) | reverse translation to exam calculations |

Corrigés may be opened only after a complete attempt of the corresponding problem set.

Active assignments may point directly to selected problems in a formal module TD. The Study Log packets retain only the bridge-specific applications and records not already present in the formal TD. An assigned formal problem is not repeated as a packet problem; unassigned formal problems remain rupture-repair or mastery references.

## Daily adaptation protocol

- Study Log 的目錄職責以 [Study Log structure](../../README.md) 為準：本計畫位於 `Cycles/<cycle-id>/`，跨日套件位於 `Packets/<packet-id>/`，單場材料位於 packet 的 `Sessions/YYYY-MM-DD/`，每日回顧位於 `Daily/YYYY/MM/`。
- 每個有實際學習行為的日期建立 `Study Log/Daily/YYYY/MM/YYYY-MM-DD.md`；不為空白日建立檔案，也不使用單一滾動總日誌。
- Packet 的 `03_Carnet.md` 保存詳細作答證據、精確 rupture、minimal repair 與 packet state；Daily 只跨 packet 摘要 observed evidence、diagnosis、adjustment decision 與 next-session contract。
- 使用者可在對應 packet record 直接新增「我的回答」並自由條列；正式化時移除該 raw block，將內容編輯成作答對象、第一個 rupture、診斷、minimal repair 與閉卷驗收，再同步更新當日 daily review。
- Daily decision 只使用 `continue`、`repair-first`、`reschedule`；不得以它替代 packet 的 `not-attempted`、`rupture`、`reconstructible`、`deployable`。
- Daily review 在 `closed: true` 後原則上不再改寫；跨日未解除的 rupture 只以翌日 retrieval contract 承接，不複製完整證明或作答。
- 只有 mastery state、structural rupture 或 next-session contract 發生語義變化時，才同步更新 `State/`；State 不按日期累積事件。

## Calendar

| 場次 | 日期與時間 | 對象 | 必要產出 |
| --- | --- | --- | --- |
| P0 | Tue 07-14, 90m | $L^p$ probability interface；density generation／RN reversal | prerequisite packet；不計入 active total |
| J1 | Fri 07-17, 19:30–21:00 | 7/14 interface retrieval；expectation、law、LOTUS | 15m packet Exercise 0；40m Exercise 1 |
| J2 | Sat 07-18, 120m | [Generated $\sigma$-Fields and Counting Measures](Packets/expectation-finite-conditioning/Sessions/2026-07-18/00_Séance.md) | sections、uncountable counting measure、atomic integration；三項 closed-book exit tests |
| J3 | Sun 07-19, 10:00–12:00 | [normalized restriction、finite partition and Bayes](Packets/expectation-finite-conditioning/Sessions/2026-07-19/00_Séance.md) | 10m rupture retrieval；finite conditioning；Q370-type analogue；closing exit |
| J3bis | Mon 07-20, 120m | [conditional expectation reconstruction and Exam P deployment](Packets/expectation-finite-conditioning/Sessions/2026-07-20/00_Séance.md) | close the unfinished J3 tail；RN construction、uniqueness、tower；finite-mixture and variance exit |
| J4c | Thu 07-23, 19:30–21:00 | product measure → independence；addition pushforward → dependence boundary | 兩個完整 problèmes；不以分段時間切斷；事後 Bilan |
| J6 | Fri 07-24, 19:30–21:00 | continuous marginals and density factorization | PM-TD Exercise 2(1)–(4)；marginal pushforwards；density-factorization deployment |
| J7 | Sat 07-25, 10:00–12:00 | change of variables | packet Exercise 3 |
| J8 | Sun 07-26, 10:00–12:00 | 25m RN review；CE and variance | packet Exercises 4–5 |
| J9 | Tue 07-28, 19:30–21:00 | dominated conditional density | packet Exercise 6 |
| J10 | Wed 07-29, 19:30–21:00 | mixture Bayes、moments and dependence boundaries | packet Exercise 7；Q382；independence／conditional-independence diagnosis |
| J10bis | Thu 07-30, 19:30–20:30 | convergence in distribution and CLT deployment | iid CLT；standardization；continuity correction；approximation boundary |
| J11 | Fri 07-31, 19:30–21:30 | closure | 60m reconstruction＋40m Exam P deployment＋20m final record |

The active July rows together with the additional J3bis total $330\mathrm m+120\mathrm m+780\mathrm m=1230\mathrm m=20\mathrm h30\mathrm m$. Including the 7/14 prerequisite gives $1320\mathrm m=22\mathrm h$; the prerequisite and J3bis do not displace any later July session.

The 7/18 repair packet replaces the original J2 tail-integration and official-question deployment; it is not additional time. Its unresolved interfaces remain explicit homework debts. The added J3bis responds to the unfinished second half of J3 and certifies conditional expectation by a fresh closed-book exit; it does not resolve the 7/18 ruptures or count preparatory reconstruction as mastery.

The former 7/21 J4 and 7/22 J5 rows totalled $180\mathrm m$. Under the scope lock they are replaced, not added to, by J4c ($90\mathrm m$), J10bis ($60\mathrm m$), and the additional 30 minutes in J11. Thus the active product-to-conditional-density packet remains exactly

$$
90+90+120+120+90+90+60+120
=780\mathrm m
=13\mathrm h.
$$

The dated [J4 feuille](Packets/product-to-conditional-density/Sessions/2026-07-21/00_Séance.md) remains available as an optional repair artifact; it is no longer a separate mandatory calendar row and supplies no attempt evidence merely by existing.

## RN deployment map

RN is reviewed through consumers rather than isolated repetition. The 07-17 row is deliberately a non-RN boundary case: a law and LOTUS exist before any dominating reference measure has been chosen.

| 日期 | Measure or numerator | Reference measure | 產出 |
| --- | --- | --- | --- |
| 07-14 | $f\mu$ and a general $\nu\ll\mu$ | $\mu$ | distinguish forward density generation from RN reversal |
| 07-17 | law $\mu_X=X_\#\mathbb P$ | none for LOTUS | law-level expectation；pdf only after a dominating reference is supplied |
| 07-19 | $\mathbb P_B$ | $\mathbb P$ | normalized event conditioning |
| 07-20 | $C\mapsto\mathbb E[Y\mathbf1_C]$ on $\mathcal G$ | $\mathbb P|_{\mathcal G}$ | probability-space conditional expectation、uniqueness and tower |
| 07-24 | $\mu_X$ or $\mu_{X,Z}$ | Lebesgue／product Lebesgue measure | pdf and joint density |
| 07-26 | $A\mapsto\mathbb E[Y\mathbf1_A]$ and $X_\#(Y\mathbb P)$ | $\mathbb P|_{\mathcal G}$ and $\mu_X$ | probability-space and state-space conditional expectation |
| 07-28 | conditional kernel $K(x,\cdot)$ | $\lambda_m$ after domination | conditional density and version completion |
| 07-29 | $p_i\mu_i$ | mixture law $\mu_X$ | Bayes posterior |

## Completion criterion

The cycle is `deployable` only if the student can:

1. assign $L^1$, $L^\infty$ and $L^2$ to finite numerators, bounded tests and second-moment cross terms;
2. unify discrete and continuous expectation through pushforward integration;
3. express independence as a product joint law and deploy it in factorization、convolution、independent-sum moments and conditional-expectation calculations;
4. distinguish Tonelli from Fubini and reconstruct the failure example;
5. derive marginal densities and a basic Jacobian transformation;
6. derive Bayes and total expectation from finite conditioning;
7. deploy RN on the probability space and state space with correct reference measures;
8. construct a dominated conditional density and state its version boundary;
9. use the iid CLT with correct standardization、continuity correction and approximation boundary, without treating it as an exact law identity;
10. classify Q50、Q386、Q370、Q382 and the assigned independence／CLT anchors by structural mechanism.

## Deferred mastery debts

- maximal represented mass and residue elimination;
- $\sigma$-finite RN gluing;
- outer-measure construction of product measure;
- full $L^2$ projection theory;
- the full hierarchy and proofs of almost-sure、in-probability、$L^p$ and weak convergence;
- general regular conditional laws and disintegration;
- Beta–Gamma and other long transformation exercises.

These remain in the full mastery edition. They are not prerequisites for the July first-pass verdict and are not counted as completed.

## Final record

- **Completed on**：
- **Cycle state**：rupture / reconstructible / deployable
- **Stable interfaces**：
- **First non-deferred rupture**：
- **Minimal repair**：
- **Mastery debts promoted to next cycle**：

Cycle 關閉後，將上述結果壓縮為 [Cycle Register](../../State/CYCLES.md) 的一列；完整證據仍留在 packets 與 Daily。

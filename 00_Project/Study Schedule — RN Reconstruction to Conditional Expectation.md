---
type: study-schedule
module: project
status: active
cycle: rn-reconstruction-to-conditional-expectation
start: 2026-07-14
end: 2026-08-09
timezone: Asia/Taipei
---

# Study Schedule — RN Reconstruction to Conditional Expectation

## Contract

- **Object**：$L^p$ interface、finite signed measures、Radon–Nikodym reconstruction、conditional expectation deployment。
- **Purpose**：把已讀過的理論壓成可閉卷重建、可在新題中辨認 reference measure 的結構。
- **Regime**：四週自學 cycle；ENS L3 末至 M1 初；每週三個平日晚間與兩個週末 session。
- **Admissible output**：證明、反例、density ledger、閉卷 reconstruction；不以頁數、抄寫量或主觀熟悉感充當完成證據。

本檔是此 cycle 唯一的安排與進度紀錄。Cours、TD、corrigés 仍各自留在正式模組中；此處只連結，不複製數學正本。

## Fixed rhythm

| 日型 | 時間 | 預設功能 |
| --- | --- | --- |
| Tuesday | 19:30–21:00 | 新一層 object 與 theorem boundary |
| Wednesday | 19:30–21:00 | 核心構造 |
| Friday | 19:30–21:00 | TD deployment |
| Saturday | 10:00–12:00 | 長證明、綜合題或來源 TD |
| Sunday | 10:00–12:00 | 閉卷 reconstruction、corrigé audit、紀錄 rupture |

若某次 session 未完成，不把兩次工作硬塞進下一格。先記錄確切 rupture，再以星期日的 repair block 修補；依賴鏈不能靠日曆表演已經通過。

## Completion states

- `not-attempted`：尚未閉卷嘗試。
- `rupture`：已定位第一個無法合法繼續的步驟。
- `reconstructible`：可在不查材料的情況下恢復完整論證。
- `deployable`：可在新題中自行選擇 object、reference measure、test class 與合法定理。

只有後兩者算完成。辨認看過的證明不是一種額外狀態；那只是記憶對版面的禮貌反應。

## Material registry

| 代碼 | 材料 | 位置 | 用途 |
| --- | --- | --- | --- |
| LP-C | $L^1$–$L^\infty$ Cours | [[15_Lp-Interface/01_Cours/Cours|The $L^1$–$L^∞$ Interface]] | endpoint pairing、bounded tests、density-generated measures |
| LP-M | Across-measures note | [[15_Lp-Interface/01_Cours/L1 Across Measures|$L^1$ Across Measures]] | integrability transfer、null sets、representatives |
| LP-TD | $L^p$ interface TD | [[15_Lp-Interface/02_TD/TD 01 — Integrability, Test Functions, and Change of Measure|TD 01 — Integrability, Test Functions, and Change of Measure]] | 本 cycle 新建的必要介面訓練 |
| LP-COR | $L^p$ corrigé | [[15_Lp-Interface/03_Corriges/TD 01 — Integrability, Test Functions, and Change of Measure|Corrigé — $L^p$ TD 01]] | 完成閉卷嘗試後核對 |
| SM-C | Signed-measures Cours | [[18_Signed-Measures/01_Cours/Cours|Signed Measures and Hahn–Jordan Decomposition]] | Hahn、Jordan、total variation、domination |
| SM-TD | Signed-measures TD | [[18_Signed-Measures/02_TD/TD 01 — Hahn–Jordan Structure and Domination|TD 01 — Hahn–Jordan Structure and Domination]] | 本 cycle 新建的 sign-structure 訓練 |
| SM-COR | Signed-measures corrigé | [[18_Signed-Measures/03_Corriges/TD 01 — Hahn–Jordan Structure and Domination|Corrigé — Signed Measures TD 01]] | 完成閉卷嘗試後核對 |
| RN-C | RN Cours | [[20_Radon-Nikodym/01_Cours/Cours|Construction of the Radon–Nikodym Derivative]] | finite construction、residue、gluing、boundary |
| RN-TD1 | RN local TD | [[20_Radon-Nikodym/02_TD/TD 01 — Boundary and Local Domination|TD 01 — Boundary and Local Domination]] | theorem boundary、local fragment |
| RN-TD2 | RN construction TD | [[20_Radon-Nikodym/02_TD/TD 02 — Constructing the Density|TD 02 — Constructing the Density]] | maximal represented mass、residue、$\sigma$-finite passage |
| CE-C | CE Cours | [[40_Conditional-Expectation/01_Cours/Cours|Conditional Expectation as an RN Representation]] | existence、uniqueness、calculus |
| CE-TD1 | CE abstract TD | [[40_Conditional-Expectation/02_TD/TD 01 — RN Construction|TD 01 — RN Construction]] | RN deployment、test functions、tower |
| CE-TD2 | CE finite TD | [[40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields|TD 02 — Finite Sigma-Fields]] | event conditioning、law decomposition、finite partitions |
| CE-S1 | CE signed/test supplement | [[40_Conditional-Expectation/06_Supplements/Signed Extension, Test Functions, and Convergence|Signed Extension, Test Functions, and Convergence]] | 僅在 test-class 或 convergence rupture 時調用 |
| CE-S2 | CE $L^p$ supplement | [[40_Conditional-Expectation/06_Supplements/Nonnegative Variables, Jensen, and L2 Projection|Nonnegative Variables, Jensen, and $L^2$ Projection]] | 核心完成後接 conditional Jensen 與 projection |
| REV | Cross-module reconstruction | [[90_Review/Reconstruction Problems — L1, Signed Measures, and Conditional Expectation|Reconstruction Problems]] | 週末閉卷測試 |
| ENS-LP | ENS $L^p$ source TD | [[99_Sources/ENS/TD 4 – Espaces Lp.pdf|ENS TD 4 — Espaces $L^p$]] | 外部題目與反例 |
| ENS-RN | ENS RN source TD | [[99_Sources/ENS/TD 7 – Théorème de Radon-Nikodym, approximations.pdf|ENS TD 7 — Radon–Nikodym]] | boundary audit；corrigé 與題目同檔 |
| ENS-CE | ENS CE source TD | [[99_Sources/ENS/TD 5 - Espérance conditionnelle.pdf|ENS TD 5 — Espérance conditionnelle]] | 新情境部署 |

---

# Week 1 — $L^p$ interface and signed measures

**Period**：2026-07-14 to 2026-07-19  
**Weekly output**：能追蹤 ambient measure 與 a.e. relation；能由 indicators 擴張到 bounded tests；能把 Hahn sign structure 轉成 Jordan measures 與 local domination。

## W1-S1 — Tuesday, 2026-07-14, 19:30–21:00

- [ ] 讀 LP-C §§1.1–1.3：$L^p$ equivalence classes、endpoint Hölder、finite-measure embeddings。
- [ ] 不查解答完成 LP-TD Exercise 1。
- [ ] 寫出有限測度假設失效時的兩個反例，並逐一檢查積分端點。
- **Required output**：精確的 embedding 常數；一個 $L^1\setminus\bigcup_{p>1}L^p$ 反例；一個 $L^p\setminus L^1$ 反例。
- **Materials**：LP-C；LP-TD。

## W1-S2 — Wednesday, 2026-07-15, 19:30–21:00

- [ ] 讀 LP-C §§1.4–1.5。
- [ ] 完成 LP-TD Exercise 2。
- [ ] 閉卷重建

  $$
  \text{indicators}
  \to
  \text{simple tests}
  \to
  \text{bounded measurable tests}.
  $$

- **Required output**：指出為何使用 DCT 而不是 MCT；完成 separation argument。
- **Materials**：LP-C；LP-TD；[[80_Lemmas/Null Sets and Integral Invariance|Null Sets and Integral Invariance]]。

## W1-S3 — Friday, 2026-07-17, 19:30–21:00

- [ ] 讀 LP-C §§2.1–2.4。
- [ ] 讀 LP-M §§3、6、7、8。
- [ ] 完成 LP-TD Exercises 3–4。
- [ ] 為每個 $L^1$ 陳述標出 reference measure 與 equivalence relation。
- **Required output**：證明 $f\mapsto f\mu$；區分 integrability transfer 與 representative compatibility。
- **Materials**：LP-C；LP-M；LP-TD。

## W1-S4 — Saturday, 2026-07-18, 10:00–12:00

- [ ] 讀 SM-C §§1.1–1.4。
- [ ] 完成 SM-TD Exercises 1–3。
- [ ] 不查 Cours 證明 Jordan minimality。
- **Required output**：Hahn ambiguity、Jordan canonicity、$\sigma$-null 的正確定義、signed density 的 total variation。
- **Materials**：SM-C；SM-TD。

## W1-S5 — Sunday, 2026-07-19, 10:00–12:00

- [ ] 讀 SM-C §1.5。
- [ ] 完成 SM-TD Exercise 4 與 Reconstruction。
- [ ] 閉卷完成 REV Exercises 1–3；上限 60 分鐘。
- [ ] 最後才用 LP-COR、SM-COR 核對；只記錄第一個合法性 rupture，不抄寫整份解答。
- **Required output**：

  $$
  \rho-c\mu
  \xrightarrow{\text{Hahn}}
  c\mathbf1_{P_c}\mu\le\rho.
  $$

- **Materials**：SM-C；SM-TD；REV；LP-COR；SM-COR。

## Week 1 record

| Session | Done | Actual time | State | First rupture and minimal repair |
| --- | --- | --- | --- | --- |
| W1-S1 | [ ] |  | not-attempted |  |
| W1-S2 | [ ] |  | not-attempted |  |
| W1-S3 | [ ] |  | not-attempted |  |
| W1-S4 | [ ] |  | not-attempted |  |
| W1-S5 | [ ] |  | not-attempted |  |

**Carry only if structurally necessary**：  
**Week 1 verdict**：rupture / reconstructible / deployable  

---

# Week 2 — Radon–Nikodym reconstruction

**Period**：2026-07-21 to 2026-07-26  
**Weekly output**：可在有限 regime 下從 Hahn decomposition 建出 maximal density，消去 residue，證唯一性，再合法轉入 $\sigma$-finite regime。

## W2-S1 — Tuesday, 2026-07-21, 19:30–21:00

- [ ] 先寫 RN theorem 的 hypotheses、conclusion、uniqueness relation，不查 Cours。
- [ ] 讀 RN-C §§1–5，核對 theorem boundary 與 local density fragment。
- [ ] 完成 RN-TD1 Exercises 0–1。
- **Required output**：一個 non-$\sigma$-finite counterexample；兩個 Hahn-region inequalities。
- **Materials**：RN-C；RN-TD1。

## W2-S2 — Wednesday, 2026-07-22, 19:30–21:00

- [ ] 完成 RN-TD1 Exercise 2。
- [ ] 完成 RN-TD1 Reconstruction，不把 local fragment 當黑箱。
- [ ] 明示 absolute continuity 與 finiteness 各自出現的位置。
- **Required output**：

  $$
  \nu\ne g\mu
  \Longrightarrow
  \exists h:\ h\mu\le\nu,
  \quad
  \int h\,d\mu>\int g\,d\mu.
  $$

- **Materials**：RN-TD1；SM-TD Exercise 4（只作依賴回查）。

## W2-S3 — Friday, 2026-07-24, 19:30–21:00

- [ ] 不查 RN-C，完成 RN-TD2 Exercise 1。
- [ ] 作答後讀 RN-C §§6–7 核對 maximal represented mass 的構造。
- [ ] 特別證明 $\mathcal C$ 對 finite maxima 穩定，以及 $g\mu\le\nu$ 的極限 passage。
- **Required output**：$\mathcal C,\alpha,g_n,g$ 必須由論證自然產生。
- **Materials**：RN-TD2；RN-C。

## W2-S4 — Saturday, 2026-07-25, 10:00–12:00

- [ ] 完成 RN-TD2 Exercises 2–3。
- [ ] 作答後讀 RN-C §§8–10。
- [ ] 分別寫出 residue contradiction 與 disjoint $\sigma$-finite gluing。
- **Required output**：finite theorem、uniqueness、$\sigma$-finite passage 三段閉合。
- **Materials**：RN-TD2；RN-C；[[80_Lemmas/Vanishing Integral Criterion|Vanishing Integral Criterion]]。

## W2-S5 — Sunday, 2026-07-26, 10:00–12:00

- [ ] 60 分鐘內完成 RN-TD2 Reconstruction，不查任何材料。
- [ ] 用 RN-C §§11–12 審核 theorem boundary 與 proof spine。
- [ ] ENS-RN 只做 Exercises 1–2；先遮住同頁 corrigé。
- [ ] 若前三項均為 reconstructible，再選做 RN-TD2 Exercise 4；否則用剩餘時間修補第一個 rupture。
- **Required output**：完整有限構造，以及一種 $\sigma$-finite reduction。
- **Materials**：RN-TD2；RN-C；ENS-RN。

## Week 2 record

| Session | Done | Actual time | State | First rupture and minimal repair |
| --- | --- | --- | --- | --- |
| W2-S1 | [ ] |  | not-attempted |  |
| W2-S2 | [ ] |  | not-attempted |  |
| W2-S3 | [ ] |  | not-attempted |  |
| W2-S4 | [ ] |  | not-attempted |  |
| W2-S5 | [ ] |  | not-attempted |  |

**RN reconstruction time**：  
**First invalid or missing step**：  
**Week 2 verdict**：rupture / reconstructible / deployable  

---

# Week 3 — Conditional expectation as an RN representation

**Period**：2026-07-28 to 2026-08-02  
**Weekly output**：能從 sub-$\sigma$-field 上的 measure representation 構造一般 $L^1$ conditional expectation，並只靠 defining identity 與 uniqueness 推出 calculus。

## W3-S1 — Tuesday, 2026-07-28, 19:30–21:00

- [ ] 讀 CE-C §§1–2。
- [ ] 完成 CE-TD1 Exercise 1.1。
- [ ] 對

  $$
  \nu_Y(A)=\mathbb E[Y\mathbf1_A],
  \qquad A\in\mathcal G,
  $$

  逐項檢查 positivity、finiteness、absolute continuity、reference measure。
- **Required output**：正變數 conditional expectation 的 RN construction。
- **Materials**：CE-C；CE-TD1。

## W3-S2 — Wednesday, 2026-07-29, 19:30–21:00

- [ ] 讀 CE-C §§3–4。
- [ ] 完成 CE-TD1 Exercise 1.2–1.4。
- [ ] 證明 construction 與 positive decomposition 的選擇無關。
- [ ] 從 indicator tests 推到 bounded $\mathcal G$-measurable tests。
- **Required output**：一般 $Y\in L^1$ 的存在、唯一性與 $L^1$ contraction。
- **Materials**：CE-C；CE-TD1；LP-C §1.5。

## W3-S3 — Friday, 2026-07-31, 19:30–21:00

- [ ] 讀 CE-C §5。
- [ ] 完成 CE-TD1 Exercise 3，所有結論只用 defining identity 與 uniqueness。
- [ ] 每一性質標明 candidate 的 measurability 與 integral identity。
- **Required output**：fixed point、independence、pull-out、兩條 tower、linearity、positivity。
- **Materials**：CE-C；CE-TD1。

## W3-S4 — Saturday, 2026-08-01, 10:00–12:00

- [ ] 完成 CE-TD1 Exercise 2。
- [ ] 寫出 $\pi$-$\lambda$ 或 monotone-class closure，不只寫「由標準定理」。
- [ ] 只有在 bounded-test approximation 或 DCT/MCT 選擇失敗時，讀 CE-S1 §§2、4–6。
- **Required output**：從 generating class 識別 conditional expectation。
- **Materials**：CE-TD1；CE-S1（conditional）。

## W3-S5 — Sunday, 2026-08-02, 10:00–12:00

- [ ] 45 分鐘內完成 REV Exercise 4。
- [ ] 30 分鐘內完成 CE-TD1 Reconstruction，並閉卷證明一條 tower identity。
- [ ] 用 CE-C §§7–8 與 CE-S1 的 Reconstruction standard 審核版本紀律。
- **Required output**：

  $$
  Y
  \mapsto
  \nu_{Y^+},\nu_{Y^-}
  \mapsto
  \frac{d\nu_{Y^+}}{d(\mathbb P|_{\mathcal G})}
  -
  \frac{d\nu_{Y^-}}{d(\mathbb P|_{\mathcal G})}.
  $$

- **Materials**：REV；CE-TD1；CE-C；CE-S1。

## Week 3 record

| Session | Done | Actual time | State | First rupture and minimal repair |
| --- | --- | --- | --- | --- |
| W3-S1 | [ ] |  | not-attempted |  |
| W3-S2 | [ ] |  | not-attempted |  |
| W3-S3 | [ ] |  | not-attempted |  |
| W3-S4 | [ ] |  | not-attempted |  |
| W3-S5 | [ ] |  | not-attempted |  |

**CE reconstruction time**：  
**Version or measurability rupture**：  
**Week 3 verdict**：rupture / reconstructible / deployable  

---

# Week 4 — Finite conditioning and deployment

**Period**：2026-08-04 to 2026-08-09  
**Weekly output**：能在 event、finite $\sigma$-field、law decomposition 與新機率模型中辨認同一 representation mechanism，且不混淆不同 reference measures 上的 densities。

## W4-S1 — Tuesday, 2026-08-04, 19:30–21:00

- [ ] 讀 CE-C §6。
- [ ] 完成 CE-TD2 Exercise 1。
- [ ] 為每個 derivative 寫 density ledger：object、domain、reference measure、ambient $L^1$、a.e. relation。
- **Required output**：

  $$
  \frac{d\mathbb P_A}{d\mathbb P},
  \qquad
  \frac{d\mu_A}{d\mu_X},
  \qquad
  \frac{d\mu_A}{d\lambda}.
  $$

- **Materials**：CE-C；CE-TD2。

## W4-S2 — Wednesday, 2026-08-05, 19:30–21:00

- [ ] 完成 CE-TD2 Exercise 2。
- [ ] 回查 LP-M §5，證明 $L^1$ transfer 時同時處理 integrability 與 equivalence classes。
- [ ] 將 indicator、distribution function、identity function 三個公式還原為同一 measure decomposition。
- **Required output**：law mixture 與 total expectation 的共同表示。
- **Materials**：CE-TD2；LP-M。

## W4-S3 — Friday, 2026-08-07, 19:30–21:00

- [ ] 完成 CE-TD2 Exercise 3 與 Reconstruction。
- [ ] 先由 $\mathcal G$-measurability 決定 piecewise-constant 形式，再由 integral identities 決定係數。
- [ ] 用 tower property 反推出 Exercise 2 的三個公式。
- **Required output**：一般 finite-partition formula，而不只 $\sigma(A)$ 的二格版本。
- **Materials**：CE-TD2；CE-C。

## W4-S4 — Saturday, 2026-08-08, 10:00–12:00

- [ ] ENS-CE Exercise 2：i.i.d. sum 的兩個 conditional expectations。
- [ ] ENS-CE Exercise 8：generating class identification。
- [ ] 在剩餘時間選做 Exercise 1（counterexamples）或 Exercise 5（independence with a measurable parameter）。
- [ ] 每題結束後寫一句：本題用的是 computation、uniqueness、independence 還是 RN representation。
- **Required output**：至少一題計算部署與一題抽象識別。
- **Materials**：ENS-CE；CE-C；CE-TD1。

## W4-S5 — Sunday, 2026-08-09, 10:00–12:00

- [ ] **25 分鐘**：完整重建 finite RN theorem，附 uniqueness 與一種 $\sigma$-finite passage。
- [ ] **20 分鐘**：由 RN 構造一般 $L^1$ conditional expectation，並證明一條 tower identity。
- [ ] **15 分鐘**：完成一份 density ledger，至少包含 $d\mathbb P_A/d\mathbb P$、$d\mu_A/d\mu_X$、$d\mu_A/d\lambda$。
- [ ] **20 分鐘**：完成 REV Exercise 2 或 4 中此前最弱的一題。
- [ ] **20 分鐘**：核對、記錄第一個 rupture，決定下一 cycle。
- [ ] 只有前三項均達 `reconstructible`，才讀 CE-S2 §§2–3，進入 conditional Jensen、$L^p$ contraction 與 $L^2$ projection。
- **Required output**：cycle verdict；不得以「大致懂」結案。
- **Materials**：RN-TD2；CE-TD1；CE-TD2；REV；CE-S2（conditional）。

## Week 4 record

| Session | Done | Actual time | State | First rupture and minimal repair |
| --- | --- | --- | --- | --- |
| W4-S1 | [ ] |  | not-attempted |  |
| W4-S2 | [ ] |  | not-attempted |  |
| W4-S3 | [ ] |  | not-attempted |  |
| W4-S4 | [ ] |  | not-attempted |  |
| W4-S5 | [ ] |  | not-attempted |  |

**Final RN time / state**：  
**Final CE time / state**：  
**Density-ledger state**：  
**Next cycle object**：  

---

# Cycle closure

The cycle is complete only if all four statements are true:

1. The finite RN construction is reconstructible without importing an $L^2$ proof or silently assuming the desired density.
2. Conditional expectation is reconstructed as an RN derivative on $(\Omega,\mathcal G)$, including signed extension and uniqueness.
3. Indicator tests, bounded tests and generating-class tests are distinguished and connected by explicit closure arguments.
4. Every density is accompanied by its reference measure and almost-everywhere relation.

## Final record

- **Completed on**：
- **Cycle state**：rupture / reconstructible / deployable
- **Stable constructions**：
- **Remaining rupture**：
- **Minimal next repair**：
- **Materials promoted to Corriges or Review**：

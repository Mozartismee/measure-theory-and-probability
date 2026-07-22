---
type: application-bridge
module: applications
status: canonical
exam-snapshot: 2026-07
duration: 7d
planned-time: 13h30m
---

# Discrete Distributions — One-Week Deployment Route

## 定位

- **Object**：countable laws、counting-measure densities、joint atomic laws、convolution、Bernoulli sums、Poisson counts、waiting times、sampling without replacement、mixtures 與 discrete conditioning。
- **Purpose**：部署 SOA Exam P 離散分布題型，並使每一條計算公式可由合法的 measure／pushforward／product construction 重建。
- **Regime**：Exam P terminal deployment；ENS L3+/M1 的結構與病態邊界。
- **Workload**：七日共 $810$ 分鐘，即 $13$ 小時 $30$ 分。
- **Boundary**：不展開一般 weak convergence、generating functions 或抽象 Markov theory。CLT 只保留 Exam P 所需的終端近似與 continuity correction。

本路線是獨立的一週離散分布循環；它不自動改寫既有 July study schedule。

---

## 文件與責任

| 文件 | 責任 |
| --- | --- |
| [Cours — Atomic Laws and Discrete Distribution Structures](../../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) | counting measure、atomic RN density、product law、convolution、named constructions、mixture 與邊界 |
| [TD 03 — Atomic Laws, Counting Models, and Structural Failures](../../30_Pushforwards-and-Laws/02_TD/TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md) | rupture → construction → representation → transfer → failure |
| [Corrigé TD 03](../../30_Pushforwards-and-Laws/03_Corriges/Corrigé%20TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md) | 完整、壓縮、可重建的獨立解答 |
| [Colle 01 — Discrete Laws and Structural Diagnosis](../../30_Pushforwards-and-Laws/04_Colles/Colle%2001%20—%20Discrete%20Laws%20and%20Structural%20Diagnosis.md) | 口頭重建 theorem boundary、construction 與 counterexample |
| [Example Sheet 01 — Exam P Discrete Distribution Deployment](../../30_Pushforwards-and-Laws/05_Example-Sheets/Example%20Sheet%2001%20—%20Exam%20P%20Discrete%20Distribution%20Deployment.md) | 公式、支撐、題目辨認與官方樣題 anchor |

依賴關係為

$$
\text{atomic law}
\longrightarrow
\text{joint/product law}
\longrightarrow
\text{pushforward/convolution}
\longrightarrow
\text{named families}
\longrightarrow
\text{conditioning/mixture}
\longrightarrow
\text{Exam P reversal}.
$$

Corrigé 不是平行讀物。每一題完成書面嘗試後才開啟相應解答；讀完後關閉文件，隔日至少白紙重寫 decisive construction。

---

## 七日配置

| 日 | 時間 | 主題與工作 | 必要產出 |
| --- | ---: | --- | --- |
| J1 | 90m | Cours §§1–3；TD Exercises 0–1 | 證明 countable atomic representation；重建 uncountable counting-measure RN failure |
| J2 | 105m | Cours §§4–5；TD Exercises 2–3 | 從 fibre 得 transformed law；從 joint law 得 sum law；寫出同 marginals、不同 sums 的反例 |
| J3 | 120m | Cours §§6.1、6.4、6.5；TD Exercise 4 | 由 probability space 構造 binomial 與 hypergeometric；推出 finite-population correction |
| J4 | 105m | Cours §6.3；TD Exercise 5 | 由 hitting time 推出 geometric／negative binomial；區分 finite waiting law |
| J5 | 120m | Cours §6.2；TD Exercise 6；Example Sheet §§2–5 | 不用 MGF 證明 Poisson moments、superposition、splitting 與 conditional allocation |
| J6 | 120m | Cours §7；TD Exercise 7；Example Sheet §6 | 分解 Poisson mixture 的 within／between variance；完成 truncation 與 Bayes reversal |
| J7 | 150m | TD Exercise 8；Colle 任選一 sujet；官方樣題限時組 | 完成 integrated count model；30m 口頭重建；60m Exam P deployment audit |

J1–J6 先處理合法性，J7 才把表示壓回考場速度。倒序訓練只會使錯誤更熟練，這種效率不值得羨慕。

---

## 每日閉卷責任

### J1 — Atomic law

白紙重建

$$
\mu=p\#_E,
\qquad
p(x)=\mu(\{x\}),
\qquad
\int_E\varphi\,d\mu=\sum_E\varphi p.
$$

必須能說明：為何 countability 使 $\#_E$ 成為 $\sigma$-finite；為何 uncountable counting measure 使 $\nu\ll\#$ 失去 RN 表示力。

### J2 — Pushforward and joint law

白紙重建

$$
p_{g(X)}(y)
=
\sum_{x\in g^{-1}(\{y\})}p_X(x),
$$

與

$$
p_{X+Y}(n)
=
\sum_kp_{X,Y}(k,n-k).
$$

只有在

$$
p_{X,Y}=p_Xp_Y
$$

時，第二式才成為 convolution。

### J3 — Replacement

能由 product Bernoulli law 推出 binomial pmf；能由 uniform law on subsets 推出 hypergeometric pmf。必須以 covariance 說明

$$
\frac{N-n}{N-1}
$$

從何而來，不能把它當成公式尾巴。

### J4 — Waiting

先宣告 support，再寫 pmf。能由

$$
\{T_r\le n\}
=
\{\operatorname{Bin}(n,p)\ge r\}
$$

在 waiting time 與 count 之間轉譯；能辨認 trials 與 failures 的 convention shift。

### J5 — Poisson

能由 index shift 推出

$$
\mathbb E[N]=\lambda,
\qquad
\mathbb E[(N)_2]=\lambda^2,
$$

並由 joint pmf factorization 證明 splitting。若只能背「Poisson 可相加」，尚未掌握它何時不可相加。

### J6 — Mixture and conditioning

能重建

$$
\operatorname{Var}(N)
=
\mathbb E[\Lambda]
+
\operatorname{Var}(\Lambda)
$$

for $N\mid\Lambda\sim\operatorname{Pois}(\Lambda)$ with $\Lambda\in L^2$，並能把 conditioning 寫成 restriction plus normalization。零機率分母不得靠樂觀處理。

### J7 — Integrated deployment

必須能把

$$
\text{latent class}
\to
\text{conditional Poisson count}
\to
\text{independent thinning}
\to
\text{mixture}
\to
\text{nonlinear payment}
$$

寫成一條不中斷的 measure and moment chain。

---

## 官方樣題限時組

題號依 [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf) 的本文件 snapshot。先做題，再開 [official sample solutions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-sol.pdf)。

### 60-minute deployment audit

| Question | 時限 | 首要結構 |
| --- | ---: | --- |
| Q30 | 7m | fixed independent Bernoulli trials |
| Q128 | 7m | hypergeometric count |
| Q146 | 8m | finite-horizon negative-binomial event with conditioning |
| Q150 | 8m | discrete-uniform conditional mixture |
| Q227 | 8m | Poisson mixture variance |
| Q246 | 8m | independent Poisson components conditioned on a total |
| Q386 | 7m | nonlinear Poisson factorial moment |
| Q512 | 7m | second moment versus squared mean |

### Mastery extensions

Q149、Q243、Q314、Q382。它們分別增加 finite waiting、nonlinear product pushforward、Bayes mixture reversal、conditional hypergeometric variance。

官方問題不在本 vault 重製。題號只作 source anchor；版本更新時應以 SOA PDF 的題幹而非舊號碼辨認。

---

## 完成判準

一週循環達到 **deployable**，必須同時滿足：

1. 無筆記證明 atomic representation、convolution boundary、hypergeometric variance、Poisson splitting 四個核心結果。
2. 對 binomial、geometric、negative binomial、hypergeometric、Poisson、discrete uniform，能先由 construction 判族，再給 support、pmf、mean、variance。
3. 對 sum、conditioning、mixture、truncation、transformed payment，能指出操作發生在哪一個 measure 上。
4. 60-minute deployment audit 至少答對七題，且沒有 independence／replacement／conditioning denominator 的模型錯置。
5. Colle 能在十五分鐘內完成一個 sujet，並承受至少兩個 boundary relances。

若只剩算術錯誤，回到 Example Sheet。若錯在族的選擇或支撐，回到 Cours §6。若錯在 independence、replacement、mixture 或 conditioning，回到相應 TD construction；多刷同型選擇題不構成修復。

---

## Source boundary

官方考試範圍由 [July 2026 Exam P syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf) 決定。該 syllabus 明列 discrete binomial、geometric、hypergeometric、negative binomial、Poisson、uniform，並要求 discrete joint／marginal／conditional distributions、moments、covariance、independent linear combinations 與 CLT。

本套件用測度論說明這些計算何時成立；它不把完整測度論誤報成 Exam P 必考內容。

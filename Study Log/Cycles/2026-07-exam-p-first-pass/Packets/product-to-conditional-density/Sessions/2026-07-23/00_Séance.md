---
type: study-session-sheet
date: 2026-07-23
cycle: 2026-07-exam-p-first-pass
packet: product-to-conditional-density
session-kind: problem-driven-independence
session: J4c
planned-time: 90m
actual-time:
solutions-policy: attempt-before-corrige
state: not-attempted
math-authority: derived
canonical-sources:
  - ../../../../../../../10_Integration-and-Convergence/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours.md
  - ../../../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../../../30_Pushforwards-and-Laws/02_TD/TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
  - ../../../../../../../35_Product-Measures-and-Transformations/01_Cours/Cours.md
  - ../../../../../../../35_Product-Measures-and-Transformations/02_TD/TD 01 — Product Measures, Iterated Integrals, and Transformations.md
  - ../../../../../../../80_Lemmas/Dynkin Systems and the Pi-Lambda Transfer Principle.md
---

# Feuille J4c — De la mesure produit à la loi jointe

*Sans documents. La durée réelle sera constatée après la copie, non imposée à l'intérieur des problèmes.*

作答時只能使用本檔。不要因預定時間點截斷證明；只在完成一個自然的數學段落後決定是否繼續。可使用 product-measure existence theorem、$\pi$--$\lambda$ theorem、nonnegative simple approximation、monotone convergence 與 pushforward 的定義；不得直接引用 Tonelli、independence-as-product-law、convolution 或任何 named-family addition rule。

只有在 copie 上寫下第一個不能合法繼續的步驟後，才可開啟 [Indications](01_Indications.md)。完整 attempt 與 Bilan 鎖定前，不得開啟 [Corrigé](02_Corrigé.md)。

## Problème I — De la mesure produit à l'indépendance

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be probability spaces, and let

$$
m:=\mu\otimes\nu
$$

on $(E\times F,\mathcal A\otimes\mathcal B)$. For $C\subseteq E\times F$, write

$$
C_x:=\{y\in F:(x,y)\in C\},
\qquad
C^y:=\{x\in E:(x,y)\in C\}.
$$

1. Starting from measurable rectangles, construct the classes needed to prove both of the following statements for every $C\in\mathcal A\otimes\mathcal B$:

   $$
   C_x\in\mathcal B,
   \qquad
   C^y\in\mathcal A,
   $$

   and

   $$
   m(C)
   =
   \int_E\nu(C_x)\,\mu(dx)
   =
   \int_F\mu(C^y)\,\nu(dy).
   $$

   Use generated-$\sigma$-field minimality where the verification class is a $\sigma$-field, and a $\pi$--$\lambda$ transfer where it is only a Dynkin system. Every subtraction used in the Dynkin argument must be justified.

2. Let $f:E\times F\to[0,+\infty]$ be $\mathcal A\otimes\mathcal B$-measurable. Starting from the indicator identity in part 1, prove that the two section integrals are measurable and establish

   $$
   \int_{E\times F}f\,dm
   =
   \int_E\left(\int_F f(x,y)\,\nu(dy)\right)\mu(dx)
   =
   \int_F\left(\int_E f(x,y)\,\mu(dx)\right)\nu(dy)
   $$

   in $[0,+\infty]$. Identify the exact limit passages.

3. Let $u:E\to[0,+\infty]$ and $v:F\to[0,+\infty]$ be measurable.

   a. With the convention

      $$
      0\cdot(+\infty)=(+\infty)\cdot0=0,
      $$

      prove that $(x,y)\mapsto u(x)v(y)$ is product-measurable.

   b. Deduce, without assuming finiteness,

      $$
      \int_{E\times F}u(x)v(y)\,m(d(x,y))
      =
      \left(\int_Eu\,d\mu\right)
      \left(\int_Fv\,d\nu\right),
      $$

      and verify explicitly the case in which one factor is $0$ and the other is $+\infty$.

   c. If now $u\in L^1(\mu)$ and $v\in L^1(\nu)$ are real-valued, prove that $(x,y)\mapsto u(x)v(y)$ belongs to $L^1(m)$ and that the same factorization holds as an equality in $\mathbb R$.

4. Let $\pi_E(x,y)=x$ and $\pi_F(x,y)=y$. Under $m$, determine their marginal laws and prove directly from the rectangle prescription that $\pi_E$ and $\pi_F$ are independent.

5. Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let

   $$
   X:\Omega\to(E,\mathcal A),
   \qquad
   Y:\Omega\to(F,\mathcal B)
   $$

   be random elements. Prove, using equality of probability measures on a generating $\pi$-system, that

   $$
   X\perp Y
   \quad\Longleftrightarrow\quad
   \mu_{X,Y}=\mu_X\otimes\mu_Y.
   $$

   State why the joint map $(X,Y)$ is measurable.

6. Let $X$ and $Y$ be independent nonnegative random variables.

   a. Derive, with values allowed in $[0,+\infty]$,

      $$
      \mathbb E[\min(X,Y)]
      =
      \int_0^\infty
      \mathbb P(X>t)\mathbb P(Y>t)\,dt.
      $$

   b. Construct independent $X$ and $Y$ for which

      $$
      \mathbb E[X]=\mathbb E[Y]=+\infty,
      \qquad
      \mathbb E[\min(X,Y)]<+\infty.
      $$

      The construction must specify the probability space and the two laws, not merely assert the existence of suitable heavy tails.

## Problème II — Une somme se souvient de la loi jointe

Let $X$ and $Y$ be integer-valued random variables, let

$$
a:\mathbb Z^2\to\mathbb Z,
\qquad
a(x,y)=x+y,
$$

and write $p_{X,Y}(k,\ell)=\mathbb P(X=k,Y=\ell)$.

1. Prove that

   $$
   \mu_{X+Y}=a_\#\mu_{X,Y},
   $$

   then compute the mass of each singleton to obtain a formula for $\mathbb P(X+Y=n)$ in terms of the joint law alone.

2. Under the additional hypothesis $X\perp Y$, derive the convolution formula. Mark the unique substitution in the proof that independence licenses.

3. On explicit finite probability spaces, construct two pairs $(X_1,Y_1)$ and $(X_2,Y_2)$ such that all four one-dimensional laws are Bernoulli$(1/2)$ but

   $$
   \mu_{X_1+Y_1}\ne\mu_{X_2+Y_2}.
   $$

   Give both joint laws and both sum laws.

4. State precisely why each of the following is insufficient to replace the product-joint-law hypothesis: knowledge of both marginals, the fact that both variables belong to named distribution families, and zero covariance. For the last assertion, exhibit an integer-valued pair that is uncorrelated but not independent. End by naming the exact measure identity missing from every failed substitute.

5. Let

   $$
   B_1,\ldots,B_m,C_1,\ldots,C_n
   $$

   be mutually independent Bernoulli$(p)$ variables, and set

   $$
   U:=\sum_{i=1}^mB_i,
   \qquad
   V:=\sum_{j=1}^nC_j.
   $$

   Starting from the product construction and a disjoint partition of $\{U+V=k\}$, compute its probability for every integer $k$. Only after the computation may the resulting law be named. No binomial-addition theorem may be cited.

## Bilan

鎖定 copie 後，只記錄：

1. **Actual duration**：
2. **Indications consulted**：
3. **第一個非法步驟**：寫出原句及缺少的 object、hypothesis、representation 或 theorem；若無則寫 `none`。
4. **Problème I 完成位置**：
5. **Problème II 完成位置**：
6. **Verdict**：`PF.independence — rupture` / `PF.independence — reconstructible`

完成度依合法證明所到的位置判定，不依鐘面判定。晚間開卷閱讀只作理解校正，不修改本次閉卷 verdict。

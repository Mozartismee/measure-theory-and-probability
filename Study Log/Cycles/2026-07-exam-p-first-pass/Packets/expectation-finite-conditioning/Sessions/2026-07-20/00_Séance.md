---
type: study-session-sheet
date: 2026-07-20
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session-kind: certification-with-deployment
session: J3bis
planned-time: 120m
actual-time:
solutions-policy: attempt-before-corrige
state: not-attempted
math-authority: derived
canonical-sources:
  - ../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 01 — RN Construction.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields.md
  - ../../../../../../../60_Applications/Exam-P-Bridges/Expectation and Conditioning — Exam P Deployment Bridge.md
---

# Feuille J3bis — Reconstruction de l'espérance conditionnelle et déploiement Exam P

*Durée : deux heures. Sans documents.*

這不是第二份 Cours。7 月 19 日後半尚未完成，而 7 月 20 日已做過的條件期望骨架重建尚無閉卷 exit evidence；本場只認證能否從空白頁恢復 object、hypotheses、representation、proof mechanism 與 Exam P transfer。

本檔是兩小時內唯一可開啟的工作文件。數學作答全部另紙完成。某一 Partie 停滯五分鐘且已寫下第一個不能合法繼續的步驟後，才可開啟 [Indications](01_Indications.md) 的對應段落。[Corrigé](02_Corrigé.md) 只能在整份 copie、épreuve de sortie 與 Bilan 完成後開啟。

## Théorème autorisé

The following finite positive Radon–Nikodym theorem may be used without proof.

Let $(S,\mathcal S)$ be a measurable space and let $\mu,\nu$ be finite positive measures on it. If $\nu\ll\mu$, then there exists $f\in L^1_+(\mu)$, unique $\mu$-almost everywhere, such that

$$
\nu(A)=\int_A f\,d\mu,
\qquad A\in\mathcal S.
$$

No signed Radon–Nikodym theorem, conditional-expectation formula or total-variance formula may be quoted as an unexplained black box.

## Partie I — Dette du 19 juillet : restriction et tribu finie (0–20 minutes)

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space.

1. For $A\in\mathcal F$ with $\mathbb P(A)>0$, reconstruct the normalized restriction $\mathbb P_A$, prove that it is a probability measure, identify $d\mathbb P_A/d\mathbb P$, and recover the scalar $\mathbb E[Y\mid A]$ for $Y\in L^1(\mathbb P)$. State separately what remains meaningful when $\mathbb P(A)=0$.

2. Let $(B_i)_{1\le i\le r}$ be a finite measurable partition, possibly containing null atoms, and let $\mathcal G=\sigma(B_1,\ldots,B_r)$. For $Y\in L^1(\mathbb P)$, determine every version of $\mathbb E[Y\mid\mathcal G]$. The argument must first characterize real-valued $\mathcal G$-measurable functions and must verify the defining identity for arbitrary $C\in\mathcal G$.

3. Apply the result to $Y=\mathbf1_D$. Derive total probability and Bayes' formula from joint masses, and locate the null-atom and null-observation boundaries.

At minute 20, mark the three mechanisms `clean`, `partial` or `absent` and continue. An incomplete mark is evidence, not a licence to reread the Cours.

## Partie II — Construction de Radon–Nikodym (20–45 minutes)

Let $\mathcal G\subseteq\mathcal F$ be a sub-$\sigma$-field.

1. For $Y\in L^1_+(\mathbb P)$ define, on $(\Omega,\mathcal G)$,

   $$
   \nu_Y(C)=\mathbb E[Y\mathbf1_C],
   \qquad C\in\mathcal G.
   $$

   Prove successively that $\nu_Y$ is a finite positive measure, that $\nu_Y\ll\mathbb P|_{\mathcal G}$, and that the permitted theorem produces a $\mathcal G$-measurable integrable candidate satisfying the conditional-expectation identities.

2. Extend the construction to every $Y\in L^1(\mathbb P)$ using only $Y^+$ and $Y^-$. Explain why the resulting object belongs to $L^1(\Omega,\mathcal G,\mathbb P|_{\mathcal G})$ and is an equivalence class rather than a distinguished pointwise function.

3. Complete the ledger.

| Object | Numerator | Reference measure | Measurable space | Uniqueness basis |
| --- | --- | --- | --- | --- |
| $\mathbb E[Y\mid\mathcal G]$ |  |  |  |  |

## Partie III — Tests, unicité et contraction (45–65 minutes)

Let $Y,Z\in L^1(\mathbb P)$ and assume that $Z$ is $\mathcal G$-measurable.

1. Prove the equivalence between

   $$
   \mathbb E[Y\mathbf1_C]=\mathbb E[Z\mathbf1_C]
   \quad\text{for every }C\in\mathcal G
   $$

   and

   $$
   \mathbb E[HY]=\mathbb E[HZ]
   \quad\text{for every bounded }\mathcal G\text{-measurable }H.
   $$

   The approximation mechanism and the dominating integrable function must be named.

2. Prove almost-sure uniqueness using a set determined by two candidates.

3. Derive

   $$
   \left|\mathbb E[Y\mid\mathcal G]\right|
   \le
   \mathbb E[|Y|\mid\mathcal G]
   \quad\mathbb P\text{-almost surely}
   $$

   and then the $L^1$ contraction.

## Partie IV — Calcul par unicité (65–85 minutes)

Let $\mathcal H\subseteq\mathcal G\subseteq\mathcal F$ and let $Y,Y_1,Y_2\in L^1(\mathbb P)$.

1. Give complete proofs, from the defining identities and uniqueness, of

   $$
   \mathbb E[HY\mid\mathcal G]
   =H\mathbb E[Y\mid\mathcal G]
   $$

   for bounded $\mathcal G$-measurable $H$, and

   $$
   \mathbb E[\mathbb E[Y\mid\mathcal G]\mid\mathcal H]
   =\mathbb E[Y\mid\mathcal H].
   $$

2. Give legal proof architectures for linearity, positivity, monotonicity, fixed points, the reverse tower identity, preservation of the mean and the independence case. For every statement, record the relevant measurability or integrability hypothesis; do not replace all proofs by the phrase “by uniqueness”.

## Partie V — Transfert inédit de type Exam P (85–105 minutes)

A portfolio belongs to exactly one of two risk classes $B_1,B_2$. Set $\mathcal G=\sigma(B_1,B_2)$ and suppose

$$
\mathbb P(B_1)=\frac13,
\qquad
\mathbb P(B_2)=\frac23.
$$

An observed event $D$ satisfies

$$
\mathbb P(D\mid B_1)=\frac34,
\qquad
\mathbb P(D\mid B_2)=\frac14.
$$

An integrable loss $Y$ is in $L^2(\mathbb P)$ and its conditional moments by class are

$$
\mathbb E[Y\mid B_1]=1,
\qquad
\mathbb E[Y\mid B_2]=4,
$$

$$
\operatorname{Var}(Y\mid B_1)=2,
\qquad
\operatorname{Var}(Y\mid B_2)=5.
$$

1. Construct the two joint masses involving $D$, compute $\mathbb P(D)$ and determine $\mathbb P(B_1\mid D)$. Distinguish the forward mixture from posterior normalization.
2. Determine $\mathbb E[Y\mid\mathcal G]$ and $\operatorname{Var}(Y\mid\mathcal G)$ as random variables.
3. Derive total expectation and total variance in this model. State exactly where $Y\in L^2$ is used.

This is a closed problem: no conditional density, probability kernel or external Exam P statement is required.

## Épreuve de sortie — Page blanche (105–117 minutes)

Without returning to the preceding parts, let $Y\in L^1(\mathbb P)$ and $\mathcal H\subseteq\mathcal G\subseteq\mathcal F$. On one page reconstruct:

1. the definition of $\mathbb E[Y\mid\mathcal G]$;
2. the numerator measure, reference measure, Radon–Nikodym construction and almost-sure uniqueness;
3. the bounded-test characterization and one tower identity;
4. the finite-partition formula, including null atoms;
5. the boundaries at a null conditioning event, outside the $L^1$ regime, and beyond eventwise finite conditioning.

No indication is available for this exit.

## Bilan (117–120 minutes)

Before opening the Corrigé, record:

1. actual duration and every indication consulted;
2. the exact first illegal or missing step;
3. the three marks from Partie I;
4. whether the exit was complete and hint-free;
5. two separate verdicts: `CE core — rupture / reconstructible` and `finite Exam P conditioning — rupture / deployable`.

`CE core — reconstructible` requires a legal exit containing the RN construction, uniqueness mechanism and tower argument. `finite Exam P conditioning — deployable` additionally requires an independent solution of Partie V with the correct $L^2$ boundary. Neither verdict includes state-space conditional expectation, continuous conditional densities, probability kernels or disintegration.

---
type: study-session-indications
date: 2026-07-20
cycle: 2026-07-exam-p-first-pass
packet: expectation-finite-conditioning
session: J3bis
math-authority: derived
canonical-sources:
  - ../../../../../../../40_Conditional-Expectation/01_Cours/Cours.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 01 — RN Construction.md
  - ../../../../../../../40_Conditional-Expectation/02_TD/TD 02 — Finite Sigma-Fields.md
  - ../../../../../../../60_Applications/Exam-P-Bridges/Expectation and Conditioning — Exam P Deployment Bridge.md
---

# Indications — Feuille J3bis

某一 Partie 停滯五分鐘且已在 copie 上寫下第一個不能合法繼續的步驟後，才可閱讀其唯一 relance。Indication 不算解答；若它提供了缺失的 object 或 theorem，必須在 Bilan 記錄。

## Indication I

On a finite partition, measurability determines the form

$$
Z=\sum_i c_i\mathbf1_{B_i}.
$$

The integral identities determine $c_i$ only when $\mathbb P(B_i)>0$. For Bayes, construct $\mathbb P(D\cap B_i)$ before dividing by the marginal $\mathbb P(D)$.

## Indication II

Do not try to construct one signed density immediately. Apply the permitted positive theorem separately to the two finite positive numerators associated with $Y^+$ and $Y^-$. The reference measure lives on $(\Omega,\mathcal G)$.

## Indication III

Pass from indicators to simple functions by linearity and then to bounded measurable tests by an approximation bounded by $\lVert H\rVert_\infty$. For uniqueness, choose the measurable set on which one candidate is strictly larger than the other.

## Indication IV

For every claimed identity, first exhibit the candidate, then verify $\mathcal G$- or $\mathcal H$-measurability, integrability and the defining identities on the relevant smaller $\sigma$-field. The tower property is a change of test class, not an iterated-density formula.

## Indication V

Use the table

| Class | Prior mass | Likelihood of $D$ | Joint mass with $D$ |
| --- | --- | --- | --- |
| $B_1$ |  |  |  |
| $B_2$ |  |  |  |

For the variance, separate the conditional within-class variance from the variance of the conditional mean. Do not substitute unconditional moments into a conditional formula.

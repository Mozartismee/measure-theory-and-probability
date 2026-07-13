---
type: td
module: conditional-expectation
status: canonical
---

# TD 02 — Conditioning on Events and Finite Sigma-Fields

Let

$$
X:(\Omega,\mathcal F,\mathbb P)
\longrightarrow
(\mathbb R,\mathcal B(\mathbb R))
$$

be a random variable with law

$$
\mu_X=X_\#\mathbb P
$$

and Lebesgue density

$$
f_X(x)=2x\,\mathbf1_{(0,1)}(x).
$$

Set

$$
A=\left\{X\le\frac12\right\},
\qquad
C=\left(-\infty,\frac12\right],
\qquad
\mathcal G=\sigma(A).
$$

Lebesgue measure on $\mathbb R$ is denoted by $\lambda$.

The general construction and characterization of conditional expectation established in the Cours and TD 1 may be used.

## Exercise 1 — Conditioning on an event

1. Compute $\mathbb P(A)$ and $\mathbb P(A^c)$. For $H\in\{A,A^c\}$, define

   $$
   \mathbb P_H(E)
   =
   \frac{\mathbb P(E\cap H)}{\mathbb P(H)},
   \qquad E\in\mathcal F.
   $$

   Determine

   $$
   \frac{d\mathbb P_H}{d\mathbb P}.
   $$

2. Let

   $$
   \mu_H=X_\#\mathbb P_H.
   $$

   Prove that, for every $B\in\mathcal B(\mathbb R)$,

   $$
   \mu_A(B)
   =
   \frac{\mu_X(B\cap C)}{\mu_X(C)},
   \qquad
   \mu_{A^c}(B)
   =
   \frac{\mu_X(B\cap C^c)}{\mu_X(C^c)}.
   $$

   Determine

   $$
   \frac{d\mu_A}{d\mu_X},
   \qquad
   \frac{d\mu_{A^c}}{d\mu_X},
   \qquad
   \frac{d\mu_A}{d\lambda},
   \qquad
   \frac{d\mu_{A^c}}{d\lambda}.
   $$

3. Compute the distribution functions of $\mu_A$ and $\mu_{A^c}$ and the quantities

   $$
   \int_{\mathbb R}x\,\mu_A(dx),
   \qquad
   \int_{\mathbb R}x\,\mu_{A^c}(dx).
   $$

4. For each Radon–Nikodym derivative obtained above, specify its reference measure, its ambient $L^1$-space, and its almost-everywhere equivalence relation.

## Exercise 2 — Decomposition of the law

1. Prove the identity of probability measures

   $$
   \mu_X
   =
   \mathbb P(A)\mu_A
   +
   \mathbb P(A^c)\mu_{A^c}.
   $$

2. Deduce that, for every nonnegative Borel function $\varphi$,

   $$
   \int_{\mathbb R}\varphi\,d\mu_X
   =
   \mathbb P(A)
   \int_{\mathbb R}\varphi\,d\mu_A
   +
   \mathbb P(A^c)
   \int_{\mathbb R}\varphi\,d\mu_{A^c}.
   $$

   Prove that

   $$
   L^1(\mu_X)
   \subset
   L^1(\mu_A)\cap L^1(\mu_{A^c})
   $$

   and extend the identity to every $\varphi\in L^1(\mu_X)$.

3. Apply the preceding identity to

   $$
   \varphi=\mathbf1_B,
   \qquad
   \varphi=\mathbf1_{(-\infty,t]},
   \qquad
   \varphi=\operatorname{id}_{\mathbb R}.
   $$

   Identify the three resulting formulas as instances of the same measure decomposition.

## Exercise 3 — Conditional expectation on a finite $\sigma$-field

1. Show that every real-valued $\mathcal G$-measurable function has the form

   $$
   Z=c_A\mathbf1_A+c_{A^c}\mathbf1_{A^c}.
   $$

2. Let $Y\in L^1(\mathbb P)$. Using the defining integral identity for conditional expectation, prove that

   $$
   \mathbb E[Y\mid\mathcal G]
   =
   \frac{\mathbb E[Y\mathbf1_A]}{\mathbb P(A)}\mathbf1_A
   +
   \frac{\mathbb E[Y\mathbf1_{A^c}]}{\mathbb P(A^c)}
   \mathbf1_{A^c}
   \qquad
   \mathbb P\text{-almost surely}.
   $$

   Reinterpret this formula as the Radon–Nikodym derivative of the signed measure

   $$
   \nu_Y(E)=\mathbb E[Y\mathbf1_E],
   \qquad E\in\mathcal G,
   $$

   with respect to $\mathbb P|_{\mathcal G}$.

3. Apply the formula successively to

   $$
   Y=X
   $$

   and, for fixed $t\in\mathbb R$, to

   $$
   Y=\mathbf1_{\{X\le t\}}.
   $$

   Express the resulting random variables using the quantities computed in Exercise 1.

4. Recover the three identities of Exercise 2 from the tower property.

## Reconstruction

### Conditioning on an event

$$
\mathbb P
\longrightarrow
\mathbb P_A
\longrightarrow
\mu_A=X_\#\mathbb P_A,
$$

together with

$$
\frac{d\mathbb P_A}{d\mathbb P},
\qquad
\frac{d\mu_A}{d\mu_X},
\qquad
\frac{d\mu_A}{d\lambda}.
$$

### Conditional expectation on $\sigma(A)$

Reconstruct

$$
Y
\longmapsto
\nu_Y(E)=\mathbb E[Y\mathbf1_E],
\qquad E\in\sigma(A),
$$

and recover the two coefficients of

$$
\mathbb E[Y\mid\sigma(A)]
=
c_A\mathbf1_A+c_{A^c}\mathbf1_{A^c}
$$

from the defining integral identity.

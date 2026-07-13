# TD 2 — Conditional Laws and Radon–Nikodym Representation

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

## Exercise 4 — Conditional expectation on the state space

Let $Y\in L^1_+(\mathbb P)$. Define the finite positive measure

$$
\eta_Y(E)
=
\mathbb E[Y\mathbf1_E],
\qquad E\in\mathcal F,
$$

and set

$$
\rho_Y=X_\#\eta_Y.
$$

Thus

$$
\rho_Y(B)
=
\mathbb E\!\left[
Y\mathbf1_{\{X\in B\}}
\right],
\qquad B\in\mathcal B(\mathbb R).
$$

1. Prove that $\rho_Y$ is a finite positive measure and that

   $$
   \rho_Y\ll\mu_X.
   $$

2. Prove that

   $$
   T:L^1(\mu_X)\longrightarrow L^1(\mathbb P),
   \qquad
   Tg=g(X),
   $$

   is a linear isometry.

   Separately, prove that for arbitrary Borel functions $g,h:\mathbb R\to\overline{\mathbb R}$,

   $$
   g=h
   \quad\mu_X\text{-almost everywhere}
   \quad\Longleftrightarrow\quad
   g(X)=h(X)
   \quad\mathbb P\text{-almost surely}.
   $$

3. Let $g_Y$ be a Borel representative of

   $$
   \frac{d\rho_Y}{d\mu_X}.
   $$

   Prove that $g_Y\in L^1(\mu_X)$ and that, for every bounded Borel function $\varphi$,

   $$
   \mathbb E[Y\varphi(X)]
   =
   \int_{\mathbb R}\varphi g_Y\,d\mu_X
   =
   \mathbb E[\varphi(X)g_Y(X)].
   $$

   Deduce that

   $$
   g_Y(X)
   =
   \mathbb E[Y\mid\sigma(X)]
   \qquad
   \mathbb P\text{-almost surely}.
   $$

4. Extend the construction to every $Y\in L^1(\mathbb P)$ by positive and negative parts.

5. Apply the construction to $Y=\mathbf1_A$. Show that

   $$
   \rho_{\mathbf1_A}
   =
   \mathbb P(A)\mu_A,
   $$

   and recover

   $$
   \frac{d\mu_A}{d\mu_X}
   $$

   and

   $$
   \mathbb E[\mathbf1_A\mid\sigma(X)].
   $$

## Exercise 5 — An event not determined by $X$

Let $D\in\mathcal F$ satisfy $\mathbb P(D)>0$. Define

$$
\mathbb P_D(E)
=
\frac{\mathbb P(E\cap D)}{\mathbb P(D)},
\qquad E\in\mathcal F,
$$

and

$$
\mu_D=X_\#\mathbb P_D.
$$

Set

$$
\rho_D(B)
=
\mathbb P(D\cap\{X\in B\}),
\qquad B\in\mathcal B(\mathbb R).
$$

1. Apply Exercise 4 to $Y=\mathbf1_D$. Show that there exists a Borel function

   $$
   g_D:\mathbb R\to[0,1]
   $$

   such that

   $$
   g_D(X)
   =
   \mathbb E[\mathbf1_D\mid\sigma(X)]
   \qquad
   \mathbb P\text{-almost surely},
   $$

   and prove that

   $$
   \mathbb P(D)
   \frac{d\mu_D}{d\mu_X}
   =
   g_D
   \qquad
   \mu_X\text{-almost everywhere}.
   $$

2. Prove the equivalences

   $$
   \mu_D=\mu_X
   \quad\Longleftrightarrow\quad
   g_D=\mathbb P(D)
   \quad\mu_X\text{-almost everywhere}
   $$

   and

   $$
   g_D=\mathbb P(D)
   \quad\mu_X\text{-almost everywhere}
   \quad\Longleftrightarrow\quad
   D\text{ is independent of }\sigma(X).
   $$

3. On a suitable extension of the probability space, give an example such that

   $$
   \mu_D=\mu_X
   $$

   but

   $$
   D\notin\sigma(X)
   \qquad
   \text{modulo }\mathbb P\text{-null sets}.
   $$

4. Prove that the following assertions are equivalent:

   $$
   \exists B\in\mathcal B(\mathbb R),
   \qquad
   \mathbb P\bigl(D\triangle\{X\in B\}\bigr)=0,
   $$

   and

   $$
   g_D\in\{0,1\}
   \qquad
   \mu_X\text{-almost everywhere}.
   $$

   Reformulate this condition in terms of

   $$
   \mathbb P(D)\frac{d\mu_D}{d\mu_X}.
   $$

5. Extend the probability space and let $U\sim\operatorname{Unif}(0,1)$ be independent of $X$. Set

   $$
   D=\{U\le X\}.
   $$

   Determine

   $$
   \mathbb E[\mathbf1_D\mid\sigma(X)].
   $$

   Deduce successively

   $$
   \mathbb P(D),
   \qquad
   \frac{d\mu_D}{d\mu_X},
   \qquad
   \frac{d\mu_D}{d\lambda},
   $$

   the distribution function of $\mu_D$, and finally

   $$
   \mathbb E[X\mid D].
   $$

## Reconstruction

Without consulting the Cours, reconstruct the following three representations.

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

### Conditional expectation given $X$

$$
Y
\longrightarrow
\eta_Y
\longrightarrow
\rho_Y=X_\#\eta_Y
\longrightarrow
g_Y=\frac{d\rho_Y}{d\mu_X}
\longrightarrow
g_Y(X).
$$

The test-function identity

$$
\mathbb E[Y\varphi(X)]
=
\int_{\mathbb R}\varphi g_Y\,d\mu_X
$$

must appear explicitly.

### Conditional event law

$$
D
\longrightarrow
\rho_D
=
\mathbb P(D)\mu_D
\longrightarrow
\mathbb P(D)\frac{d\mu_D}{d\mu_X}
=
g_D.
$$

Close the reconstruction by separating the following statements:

$$
g_D=\mathbb P(D),
\qquad
g_D\in\{0,1\},
$$

and state the meaning of each.

No claim concerning a regular conditional law or a jointly measurable probability kernel is admissible at this stage.
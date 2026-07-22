---
type: td
module: product-measures-and-transformations
status: canonical
solutions-policy: attempt-before-corrige
sources:
  - ENS-TD5-Fubini-COV
---

# TD 01 — Product Measures, Iterated Integrals, and Transformations

Throughout, all measure spaces appearing in a product are $\sigma$-finite.

## Exercise A — Sections and the indicator case of Tonelli

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be $\sigma$-finite measure spaces, and assume the existence of the product measure $\mu\otimes\nu$.

1. For $C\in\mathcal A\otimes\mathcal B$, prove that $C_x\in\mathcal B$ for every $x\in E$ and $C^y\in\mathcal A$ for every $y\in F$.
2. Assume temporarily that $\mu(E)<+\infty$ and $\nu(F)<+\infty$. Using the measurable rectangles as a generating $\pi$-system, prove that

   $$
   x\longmapsto\nu(C_x)
   $$

   is measurable and that

   $$
   (\mu\otimes\nu)(C)
   =
   \int_E\nu(C_x)\,\mu(dx)
   $$

   for every $C\in\mathcal A\otimes\mathcal B$.
3. Choose finite-measure exhaustions $E_n\uparrow E$ and $F_n\uparrow F$. Use monotone convergence to extend the preceding identity to the $\sigma$-finite case, and prove the symmetric identity

   $$
   (\mu\otimes\nu)(C)
   =
   \int_F\mu(C^y)\,\nu(dy).
   $$

4. Starting from the indicator identities, reconstruct Tonelli's theorem first for nonnegative simple functions and then for arbitrary nonnegative measurable functions.

The product-measure existence theorem is available. No outer-measure construction is requested.

## Exercise 0 — Failure without absolute integrability

Equip $\mathbb N^*=\{1,2,\ldots\}$ with counting measure and define

$$
a(m,n)=\mathbf1_{\{n=m\}}-\mathbf1_{\{n=m+1\}}.
$$

1. Compute $\sum_n a(m,n)$ for each $m$ and then $\sum_m\sum_n a(m,n)$.
2. Compute $\sum_m a(m,n)$ for each $n$ and then $\sum_n\sum_m a(m,n)$.
3. Prove that $a\notin\ell^1(\mathbb N^*\times\mathbb N^*)$.
4. Identify precisely why neither Tonelli nor Fubini authorizes an exchange of summation for $a$.

The conclusion is not that Fubini sometimes lies. The conclusion is that an unauthenticated exchange is not Fubini.

## Exercise 1 — Subgraphs and tail integration

Let $(E,\mathcal A,\mu)$ be a measure space and let $f:E\to[0,+\infty]$ be measurable.

1. Prove that

   $$
   H_f=\{(x,t)\in E\times(0,+\infty):t<f(x)\}
   $$

   is $\mathcal A\otimes\mathcal B((0,+\infty))$-measurable.
2. Apply Tonelli to $\mathbf1_{H_f}$ and prove

   $$
   \int_Ef\,d\mu
   =
   \int_0^\infty\mu(f>t)\,dt.
   $$

3. For $p>0$, prove

   $$
   \int_Ef^p\,d\mu
   =
   p\int_0^\infty t^{p-1}\mu(f>t)\,dt.
   $$

4. Assume that $\mu(E)<\infty$ and that, for some $C>0$ and $p>0$,

   $$
   \mu(f>t)\le Ct^{-p},
   \qquad t>0.
   $$

   Prove that $f\in L^q(\mu)$ for every $0<q<p$. Construct an example showing that $f\in L^p(\mu)$ need not follow.

## Exercise 2 — Marginal densities as pushforwards

Let $f:\mathbb R^d\times\mathbb R^m\to[0,+\infty]$ be measurable and satisfy

$$
\int_{\mathbb R^{d+m}}f(x,y)\,dx\,dy=1.
$$

Define

$$
f_X(x)=\int_{\mathbb R^m}f(x,y)\,dy,
\qquad
f_Y(y)=\int_{\mathbb R^d}f(x,y)\,dx.
$$

1. Prove that $f_X$ and $f_Y$ are measurable probability densities.
2. Let $\mu=f\,d(\lambda_d\otimes\lambda_m)$. Prove that

   $$
   (\pi_X)_\#\mu=f_X\,d\lambda_d,
   \qquad
   (\pi_Y)_\#\mu=f_Y\,d\lambda_m.
   $$

3. For every nonnegative measurable $\varphi:\mathbb R^d\to[0,+\infty]$, prove

   $$
   \int\varphi(x)f_X(x)\,dx
   =
   \int\varphi(x)f(x,y)\,dx\,dy.
   $$

4. Prove that if $f(x,y)=f_X(x)f_Y(y)$ almost everywhere, then the coordinate projections are independent under $\mu$.

## Exercise 3 — Beta–Gamma transport

Let $a,b>0$ and consider on $(0,+\infty)^2$ the nonnegative function

$$
(x,y)\longmapsto x^{a-1}y^{b-1}e^{-(x+y)}.
$$

Define

$$
T(x,y)=\left(x+y,\frac{x}{x+y}\right).
$$

1. Prove that $T$ is a $C^1$-diffeomorphism from $(0,+\infty)^2$ onto $(0,+\infty)\times(0,1)$ and compute $T^{-1}$.
2. Compute $|\det DT^{-1}(s,u)|$.
3. Use change of variables and Tonelli to prove

   $$
   \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}
   =
   \int_0^1u^{a-1}(1-u)^{b-1}\,du.
   $$

4. Identify separately the role of change of variables and the role of Tonelli.

## Exercise 4 — Reconstruction and theorem selection

For each statement below, name the operative theorem and state its decisive hypotheses before proving it.

1. If $h\ge0$ is measurable on $E\times F$, both iterated integrals exist in $[0,+\infty]$ and are equal.
2. If $h\in L^1(\mu\otimes\nu)$, almost every section is integrable and the order of integration may be exchanged.
3. If $X\ge0$ is a random variable, then

   $$
   \mathbb E[X]=\int_0^\infty\mathbb P(X>t)\,dt.
   $$

4. If $(X,Y)$ has joint density $f$, then the density of $X$ is $x\mapsto\int f(x,y)\,dy$.
5. Explain why none of the preceding statements defines a conditional density on a null fiber.

## Source note

Exercises 1 and 3 are adapted in mathematical mechanism from [ENS TD 5 — Fubini and change of variables](../../99_Sources/ENS/TD%205%20–%20Théorèmes%20de%20Fubini%20et%20changement%20de%20variables.pdf). Exercises A and 0 and the dependency chain are specific to this module.

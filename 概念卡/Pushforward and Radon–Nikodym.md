# Pushforward and Radon–Nikodym

## Exercise 1 — Law, Density, and Transfer

Let

$$
X:(\Omega,\mathcal F,\mathbb P)\to(S,\Sigma)
$$

be measurable, and let

$$
\mu_X:=X_\#\mathbb P.
$$

Let $m$ be a $\sigma$-finite measure on $(S,\Sigma)$, and assume

$$
\mu_X\ll m.
$$

Define

$$
f_X:=\frac{d\mu_X}{dm}.
$$

1. Prove that

$$
f_X\ge 0
\quad m\text{-a.e.},
\qquad
\int_S f_X\,dm=1.
$$

2. Prove that for every nonnegative measurable $\varphi:S\to[0,\infty]$,

$$
\mathbb E[\varphi(X)]
=
\int_S \varphi\,d\mu_X
=
\int_S \varphi f_X\,dm.
$$

3. Extend the identity to every measurable $\varphi$ for which either side is well defined.

4. Conversely, suppose $f:S\to[0,\infty]$ satisfies

$$
\int_S f\,dm=1
$$

and

$$
\mathbb E[\varphi(X)]
=
\int_S \varphi f\,dm
$$

for every bounded measurable $\varphi$. Prove that

$$
\mu_X=fm,
$$

hence

$$
f=f_X
\quad m\text{-a.e.}
$$

Your proof must explicitly use indicator functions to identify the measure.

---

## Exercise 2 — Conditional Expectation as a Radon–Nikodym Derivative on the State Space

Let

$$
X:(\Omega,\mathcal F,\mathbb P)\to(S,\Sigma)
$$

be measurable, and let $Y\ge0$ be measurable with

$$
Y\in L^1(\mathbb P).
$$

Define a finite measure $\rho_Y$ on $(S,\Sigma)$ by

$$
\rho_Y(B)
:=
\mathbb E\!\left[
Y\mathbf 1_{\{X\in B\}}
\right],
\qquad
B\in\Sigma.
$$

1. Prove that $\rho_Y$ is a finite measure.

2. Prove that

$$
\rho_Y\ll\mu_X.
$$

3. Let

$$
g:=\frac{d\rho_Y}{d\mu_X}.
$$

Prove that for every $B\in\Sigma$,

$$
\int_B g\,d\mu_X
=
\mathbb E\!\left[
Y\mathbf 1_{\{X\in B\}}
\right].
$$

4. Use the pushforward formula to show that

$$
\int_{\{X\in B\}}g(X)\,d\mathbb P
=
\mathbb E\!\left[
Y\mathbf 1_{\{X\in B\}}
\right].
$$

5. Conclude that

$$
g(X)
=
\mathbb E[Y\mid\sigma(X)]
\quad
\mathbb P\text{-a.s.}
$$

6. Deduce that for every bounded measurable $h:S\to\mathbb R$,

$$
\mathbb E[h(X)Y]
=
\int_S h(s)g(s)\,\mu_X(ds).
$$

Thus,

$$
\boxed{
\mathbb E[Y\mid\sigma(X)]
=
\left(
\frac{d\rho_Y}{d\mu_X}
\right)(X)
}
$$

almost surely.
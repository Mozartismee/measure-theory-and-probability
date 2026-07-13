# Pushforward Integration Formula

## Proposition

Let

$$
X:(\Omega,\mathcal F,\mu)\to(S,\Sigma)
$$

be measurable, and let

$$
\nu:=X_\#\mu,
\qquad
\nu(A):=\mu(X^{-1}(A)).
$$

Then, for every measurable $\varphi:S\to[0,\infty]$,

$$
\int_S \varphi\,d\nu
=
\int_\Omega \varphi\circ X\,d\mu.
$$

The same identity holds for every measurable
$\varphi:S\to\overline{\mathbb R}$ whenever the integral is defined.

## Proof

For $A\in\Sigma$,

$$
\int_S \mathbf 1_A\,d\nu
=
\nu(A)
=
\mu(X^{-1}(A))
=
\int_\Omega \mathbf 1_A\circ X\,d\mu.
$$

By linearity, the identity holds for every non-negative simple function.

Let $\varphi\ge 0$ be measurable. Choose simple functions

$$
\varphi_n\uparrow\varphi.
$$

Then

$$
\varphi_n\circ X\uparrow\varphi\circ X,
$$

hence, by monotone convergence,

$$
\int_S\varphi\,d\nu
=
\lim_n\int_S\varphi_n\,d\nu
=
\lim_n\int_\Omega\varphi_n\circ X\,d\mu
=
\int_\Omega\varphi\circ X\,d\mu.
$$

For general $\varphi$, apply the non-negative case to $\varphi^+$ and $\varphi^-$, using

$$
(\varphi\circ X)^\pm=\varphi^\pm\circ X.
$$

$\square$
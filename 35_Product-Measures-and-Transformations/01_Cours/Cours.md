---
type: cours
module: product-measures-and-transformations
status: canonical
sources:
  - ENS-TD5-Fubini-COV
---

# Cours — Product Measures, Iterated Integrals, and Transformations

This module depends on [Integration and Convergence](../../10_Integration-and-Convergence/01_Cours/Cours.md) and [Pushforwards and Laws](../../30_Pushforwards-and-Laws/01_Cours/Cours.md).

## 1. Product measurable spaces

Let $(E,\mathcal A)$ and $(F,\mathcal B)$ be measurable spaces. The product $\sigma$-field is

$$
\mathcal A\otimes\mathcal B
=
\sigma\bigl(\{A\times B:A\in\mathcal A,\ B\in\mathcal B\}\bigr).
$$

Its initial mapping property is isolated in [Lemma 8 — Coordinatewise Measurability into Product Spaces](../../80_Lemmas/Coordinatewise%20Measurability%20into%20Product%20Spaces.md): a map into a product measurable space is measurable exactly when its coordinate maps are measurable.

For $C\subseteq E\times F$, define the sections

$$
C_x=\{y\in F:(x,y)\in C\},
\qquad
C^y=\{x\in E:(x,y)\in C\}.
$$

If $C\in\mathcal A\otimes\mathcal B$, then $C_x\in\mathcal B$ for every $x\in E$ and $C^y\in\mathcal A$ for every $y\in F$. This follows by observing that the class of sets with measurable sections is a $\sigma$-field containing the measurable rectangles.

If $f:E\times F\to\overline{\mathbb R}$ is $\mathcal A\otimes\mathcal B$-measurable, then

$$
y\longmapsto f(x,y)
\quad\text{and}\quad
x\longmapsto f(x,y)
$$

are measurable for every fixed value of the other variable.

For Euclidean spaces,

$$
\mathcal B(\mathbb R^d)\otimes\mathcal B(\mathbb R^m)
=
\mathcal B(\mathbb R^{d+m}).
$$

## 2. Product measures

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be $\sigma$-finite measure spaces. There exists a unique $\sigma$-finite measure $\mu\otimes\nu$ on $\mathcal A\otimes\mathcal B$ such that

$$
(\mu\otimes\nu)(A\times B)=\mu(A)\nu(B)
$$

for all $A\in\mathcal A$ and $B\in\mathcal B$, where the rectangle formula uses $0\cdot(+\infty)=(+\infty)\cdot0=0$.

The construction theorem is taken as part of measure construction. The present module is responsible for its integration consequences, not for repeating an outer-measure construction.

Let $\mathcal R$ be the ring of finite disjoint unions of measurable rectangles. The construction may be recalled from the prescription

$$
m_0\!\left(\bigsqcup_{i=1}^r A_i\times B_i\right)
=
\sum_{i=1}^r\mu(A_i)\nu(B_i).
$$

After well-definedness and countable additivity on $\mathcal R$ have been verified, the remaining chain is

$$
\text{rectangle prescription}
\longrightarrow
\text{premeasure on finite disjoint unions of rectangles}
\longrightarrow
\text{Carathéodory extension}
\longrightarrow
\sigma\text{-finite uniqueness}.
$$

This construction is retained as a reconstruction interface. A new proof of the extension theorem is outside the present module.

### Proposition 2.1 — Section integrals for indicators

For every $C\in\mathcal A\otimes\mathcal B$, the functions

$$
x\longmapsto\nu(C_x),
\qquad
y\longmapsto\mu(C^y)
$$

are measurable, and

$$
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx)
=
\int_F\mu(C^y)\,\nu(dy).
$$

### Proof

The complete proof is isolated in
[Lemma 10 — Section-Mass Representation of Product Measures](../../80_Lemmas/Section-Mass%20Representation%20of%20Product%20Measures.md).
It first proves section-mass measurability in the finite inner-measure regime,
passes to $\sigma$-finite measures by finite exhaustion, constructs the two
section-integral measures, and identifies them by uniqueness on measurable
rectangles.

## 3. Tonelli's theorem

### Theorem 3.1 — Nonnegative regime

Let $f:E\times F\to[0,+\infty]$ be $\mathcal A\otimes\mathcal B$-measurable. Then the functions

$$
x\longmapsto\int_F f(x,y)\,\nu(dy),
\qquad
y\longmapsto\int_E f(x,y)\,\mu(dx)
$$

are measurable, and

$$
\int_{E\times F}f\,d(\mu\otimes\nu)
=
\int_E\left(\int_F f(x,y)\,\nu(dy)\right)\mu(dx)
=
\int_F\left(\int_E f(x,y)\,\mu(dx)\right)\nu(dy).
$$

All three quantities may equal $+\infty$.

### Proof architecture

Proposition 2.1 proves the result for indicators of arbitrary product-measurable sets. Linearity then gives it for nonnegative simple functions. For general $f\ge0$, choose nonnegative simple functions $f_n\uparrow f$. For every $x$, monotone convergence on $F$ gives

$$
\int_Ff_n(x,y)\,\nu(dy)
\uparrow
\int_Ff(x,y)\,\nu(dy),
$$

so the limiting section integral is measurable. Applying monotone convergence once on $E\times F$ and once to the outer integral on $E$ proves the first iterated identity. The reversed identity is symmetric.

The decisive hypothesis is positivity. No integrability has yet been proved or assumed.

## 4. Fubini's theorem

### Theorem 4.1 — Integrable regime

Let $f:E\times F\to\mathbb R$ be measurable and assume

$$
\int_{E\times F}|f|\,d(\mu\otimes\nu)<+\infty.
$$

Then:

1. $f(x,\cdot)\in L^1(\nu)$ for $\mu$-almost every $x$;
2. $f(\cdot,y)\in L^1(\mu)$ for $\nu$-almost every $y$;
3. the two almost-everywhere defined parameter integrals belong to the corresponding $L^1$ spaces;
4. one has

   $$
   \int_{E\times F}f\,d(\mu\otimes\nu)
   =
   \int_E\left(\int_F f(x,y)\,\nu(dy)\right)\mu(dx)
   =
   \int_F\left(\int_E f(x,y)\,\mu(dx)\right)\nu(dy).
   $$

### Proof

Apply Tonelli to $|f|$. The finite value of

$$
\int_E\left(\int_F|f(x,y)|\,\nu(dy)\right)\mu(dx)
$$

implies that the inner integral is finite for $\mu$-almost every $x$; the other direction is identical. Apply Tonelli separately to $f^+$ and $f^-$ and subtract their finite integrals.

Tonelli permits nonnegative infinite integrals. Fubini permits signs only after absolute integrability has removed the expression $+\infty-\infty$.

## 5. Layer-cake representations

Let $(E,\mathcal A,\mu)$ be $\sigma$-finite and let $f:E\to[0,+\infty]$ be measurable. The set

$$
H_f=\{(x,t)\in E\times(0,+\infty):0<t<f(x)\}
$$

belongs to $\mathcal A\otimes\mathcal B((0,+\infty))$. Since

$$
f(x)=\int_0^\infty\mathbf1_{\{t<f(x)\}}\,dt,
$$

Tonelli gives

$$
\boxed{
\int_E f\,d\mu
=
\int_0^\infty\mu(f>t)\,dt
}.
$$

More generally, for $p>0$,

$$
\int_E f^p\,d\mu
=
p\int_0^\infty t^{p-1}\mu(f>t)\,dt.
$$

On a probability space, for a nonnegative random variable $X$,

$$
\boxed{
\mathbb E[X]
=
\int_0^\infty\mathbb P(X>t)\,dt
}.
$$

The identity remains valid with value $+\infty$; Tonelli, not Fubini, is the operative theorem.

## 6. Joint laws and marginalization

Let $X:\Omega\to S$ and $Y:\Omega\to T$ be random elements. Their joint law is

$$
\mu_{X,Y}=(X,Y)_\#\mathbb P.
$$

If $\pi_S(s,t)=s$ and $\pi_T(s,t)=t$, then

$$
\mu_X=(\pi_S)_\#\mu_{X,Y},
\qquad
\mu_Y=(\pi_T)_\#\mu_{X,Y}.
$$

Suppose now that $S=\mathbb R^d$, $T=\mathbb R^m$, and

$$
\mu_{X,Y}=f_{X,Y}(x,y)\,dx\,dy.
$$

Tonelli shows that

$$
f_X(x)=\int_{\mathbb R^m}f_{X,Y}(x,y)\,dy,
\qquad
f_Y(y)=\int_{\mathbb R^d}f_{X,Y}(x,y)\,dx
$$

are measurable, nonnegative and integrable. For every nonnegative measurable $\varphi$,

$$
\mathbb E[\varphi(X)]
=
\int_{\mathbb R^d}\varphi(x)f_X(x)\,dx.
$$

Thus marginalization is a pushforward identity implemented by Tonelli.

## 7. Euclidean change of variables

### Theorem 7.1 — Diffeomorphic transport

Let $U,V\subseteq\mathbb R^d$ be open and let $T:U\to V$ be a $C^1$-diffeomorphism. For every nonnegative measurable $h:V\to[0,+\infty]$,

$$
\int_V h(z)\,dz
=
\int_U h(T(x))\left|\det DT(x)\right|\,dx.
$$

The same identity holds for integrable signed $h$.

If $X$ has density $f_X$ on $U$ and $Z=T(X)$, then $Z$ has density

$$
f_Z(z)
=
\begin{cases}
f_X(T^{-1}(z))\left|\det DT^{-1}(z)\right|,&z\in V,\\[1ex]
0,&z\notin V.
\end{cases}
$$

The determinant is the density of transported Lebesgue measure. It is not an algebraic decoration to be appended after solving for the inverse map.

## 8. Boundary of validity

1. Without nonnegativity or absolute integrability, the two iterated integrals may disagree or fail to exist.
2. Product measures are formed on product $\sigma$-fields. The product of complete $\sigma$-fields need not itself be complete; completion is a separate operation.
3. A formula involving $f_{X,Y}(x,y)/f_X(x)$ requires a version choice on $\{f_X=0\}$. The corresponding conditional-law construction belongs to [Conditional Laws](../../50_Conditional-Laws/01_Cours/Cours.md).
4. The change-of-variables formula above assumes a $C^1$-diffeomorphism. Non-injective maps require decomposition into injective branches or a different theorem.

## 9. Reconstruction

The following chains must be recoverable without consultation:

$$
f\ge0
\xrightarrow{\text{Tonelli}}
\text{iterated integrals in }[0,+\infty],
$$

$$
f\in L^1(\mu\otimes\nu)
\xrightarrow{\text{Tonelli on }|f|}
\text{a.e. section integrability}
\xrightarrow{\text{Fubini}}
\text{exchange of integration},
$$

and

$$
\text{joint law}
\xrightarrow{\text{projection}}
\text{marginal law}
\xrightarrow{\text{Tonelli}}
\text{marginal density}.
$$

## Source note

The layer-cake and change-of-variables exercises are adapted in structure from [ENS TD 5 — Fubini and change of variables](../../99_Sources/ENS/TD%205%20–%20Théorèmes%20de%20Fubini%20et%20changement%20de%20variables.pdf). The statements and dependency order here are reconstructed for the present module.

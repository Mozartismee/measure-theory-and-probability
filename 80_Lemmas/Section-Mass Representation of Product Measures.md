---
type: lemma
module: lemmas
status: canonical
---

# Lemma 10 — Section-Mass Representation of Product Measures

This lemma isolates the passage from measurable sections to the indicator
representation underlying Tonelli's theorem.

## Framework

Let $(E,\mathcal A,\mu)$ and $(F,\mathcal B,\nu)$ be $\sigma$-finite
measure spaces. For $C\in\mathcal A\otimes\mathcal B$, define

$$
C_x:=\{y\in F:(x,y)\in C\},
\qquad
C^y:=\{x\in E:(x,y)\in C\}.
$$

By [Lemma 4 — Generated Sigma-Fields and Measurable Sections](Generated%20Sigma-Fields%20and%20Measurable%20Sections.md),
$C_x\in\mathcal B$ and $C^y\in\mathcal A$. Hence $\nu(C_x)$ and
$\mu(C^y)$ are well defined for every $x\in E$ and $y\in F$.

## Theorem 10.1 — The Representation

For every $C\in\mathcal A\otimes\mathcal B$, the maps

$$
x\longmapsto\nu(C_x),
\qquad
y\longmapsto\mu(C^y)
$$

are respectively $\mathcal A$-measurable and $\mathcal B$-measurable.
Define

$$
m(C):=\int_E\nu(C_x)\,\mu(dx),
\qquad
m'(C):=\int_F\mu(C^y)\,\nu(dy).
$$

Then $m$ and $m'$ are $\sigma$-finite measures on
$\mathcal A\otimes\mathcal B$, and both coincide with the product measure:

$$
\boxed{
(\mu\otimes\nu)(C)
=
\int_E\nu(C_x)\,\mu(dx)
=
\int_F\mu(C^y)\,\nu(dy).
}
$$

#### Proof

Assume first that $\nu(F)<+\infty$, and set

$$
\mathcal G
:=
\left\{
C\in\mathcal A\otimes\mathcal B:
x\longmapsto\nu(C_x)\text{ is }\mathcal A\text{-measurable}
\right\}.
$$

This class is a Dynkin system. Indeed, $E\times F\in\mathcal G$ because
$x\longmapsto\nu((E\times F)_x)$ is the constant map $\nu(F)$. If
$C,D\in\mathcal G$ and $C\subseteq D$, then

$$
(D\setminus C)_x=D_x\setminus C_x
$$

and, since $\nu$ is finite,

$$
\nu((D\setminus C)_x)=\nu(D_x)-\nu(C_x).
$$

Hence $D\setminus C\in\mathcal G$. Finally, if $(C_n)$ is pairwise
disjoint in $\mathcal G$, then the sections $(C_n)_x$ are pairwise
disjoint and

$$
\nu\!\left(\left(\bigsqcup_{n\ge1}C_n\right)_x\right)
=
\sum_{n\ge1}\nu((C_n)_x),
$$

the increasing limit of measurable partial sums. Thus
$\bigsqcup_n C_n\in\mathcal G$.

For every measurable rectangle,

$$
\nu((A\times B)_x)=\mathbf 1_A(x)\nu(B),
$$

so $\mathcal G$ contains the $\pi$-system of measurable rectangles.
The [π–λ transfer principle](Dynkin%20Systems%20and%20the%20Pi-Lambda%20Transfer%20Principle.md)
therefore gives

$$
\mathcal G=\mathcal A\otimes\mathcal B.
$$

Now suppose merely that $\nu$ is $\sigma$-finite. Choose
$B_n\uparrow F$ with $\nu(B_n)<+\infty$, and put

$$
\nu_n(B):=\nu(B\cap B_n).
$$

The finite-measure case shows that $x\longmapsto\nu_n(C_x)$ is measurable.
Since

$$
\nu_n(C_x)=\nu(C_x\cap B_n)\uparrow\nu(C_x),
$$

the map $x\longmapsto\nu(C_x)$ is measurable. Interchanging the two
coordinates proves the measurability of $y\longmapsto\mu(C^y)$.

The definitions of $m$ and $m'$ therefore make sense. If $(C_n)$ is
pairwise disjoint in $\mathcal A\otimes\mathcal B$, then monotone
convergence gives

$$
\begin{aligned}
m\!\left(\bigsqcup_{n\ge1}C_n\right)
&=
\int_E\nu\!\left(\left(\bigsqcup_{n\ge1}C_n\right)_x\right)\mu(dx) \\
&=
\int_E\sum_{n\ge1}\nu((C_n)_x)\,\mu(dx) \\
&=
\sum_{n\ge1}m(C_n).
\end{aligned}
$$

Also $m(\varnothing)=0$, so $m$ is a measure. The same argument applies to
$m'$. For every $A\in\mathcal A$ and $B\in\mathcal B$,

$$
m(A\times B)
=
m'(A\times B)
=
\mu(A)\nu(B),
$$

with the convention $0\cdot(+\infty)=(+\infty)\cdot0=0$.

Choose $A_n\uparrow E$ and $B_n\uparrow F$ such that
$\mu(A_n)<+\infty$ and $\nu(B_n)<+\infty$, and set
$C_n:=A_n\times B_n$. Then $C_n\uparrow E\times F$ and

$$
m(C_n)
=
m'(C_n)
=
\mu(A_n)\nu(B_n)<+\infty.
$$

Thus $m$ and $m'$ are $\sigma$-finite. The three measures
$m$, $m'$, and $\mu\otimes\nu$ agree on the generating $\pi$-system of
measurable rectangles and share the finite exhaustion $(C_n)$.
Corollary 9.5 of the
[π–λ transfer principle](Dynkin%20Systems%20and%20the%20Pi-Lambda%20Transfer%20Principle.md)
therefore yields

$$
m=m'=\mu\otimes\nu.
$$

This is the asserted representation. $\square$

## Deployment Map

- **Tonelli's theorem.** The lemma is the indicator case; the reusable chain
  is indicators $\to$ nonnegative simple functions $\to$ arbitrary
  nonnegative measurable functions. See
  [Product Measures and Transformations](../35_Product-Measures-and-Transformations/01_Cours/Cours.md).
- **Marginalization.** Applied to a joint law or density on $E\times F$, the
  formula integrates out one coordinate and produces the corresponding
  marginal quantity.
- **Layer cake.** Applied to the subgraph
  $\{(x,t):0<t<f(x)\}$, the same representation converts an integral of $f$
  into an integral of level-set masses.
- **Product-law identification.** A candidate measure obtained by iterated
  integration is identified from its values on rectangles by $\sigma$-finite
  uniqueness.

## Boundary of the Argument

The first-oriented measurability statement uses the $\sigma$-finiteness of
the inner measure $\nu$; it does not require $\mu$ to be $\sigma$-finite.
Both $\sigma$-finiteness assumptions enter when the two orientations are
identified through a common finite exhaustion.

This dependence is real. Take

$$
(E,\mathcal A)=(F,\mathcal B)
=(\mathbb R,\mathcal B(\mathbb R)),
\qquad
\mu=\lambda,
$$

and let $\nu$ be counting measure. For the diagonal

$$
C:=\{(x,x):x\in\mathbb R\},
$$

one has

$$
\int_{\mathbb R}\nu(C_x)\,\lambda(dx)
=
\int_{\mathbb R}1\,\lambda(dx)
=+\infty,
$$

whereas

$$
\int_{\mathbb R}\lambda(C^y)\,\nu(dy)
=
\int_{\mathbb R}0\,\nu(dy)
=0.
$$

Thus the symmetric representation cannot simply be asserted beyond the
$\sigma$-finite regime.

No form of Tonelli's theorem is used in the proof: the exchange between a
sum and an integral is monotone convergence. This prevents circularity.
The lemma concerns fixed product measures, not kernels or disintegration.

## Reconstruction Line

$$
\boxed{
\text{measurable set sections}
\longrightarrow
\text{measurable section masses}
\longrightarrow
\text{section-integral measures}
\longrightarrow
\text{rectangle agreement}
\longrightarrow
\sigma\text{-finite uniqueness}.
}
$$

## Reference

This formulation abstracts §§5.1–5.2 of
[Le Gall — *Cours d'intégration et probabilités*](../99_Sources/ENS/Le%20Gall（法文原版%20建議使用）.pdf).

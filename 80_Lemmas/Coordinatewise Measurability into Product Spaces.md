---
type: lemma
module: lemmas
status: canonical
---

# Lemma 8 — Coordinatewise Measurability into Product Spaces

This lemma identifies the product $\sigma$-field as the initial measurable
structure for the coordinate projections and records the resulting mapping
property.

## Lemma 8.1 — Initial Structure and Coordinatewise Criterion

Let $(F_1,\mathcal B_1)$ and $(F_2,\mathcal B_2)$ be measurable spaces, and
let

$$
\pi_1:F_1\times F_2\to F_1,
\qquad
\pi_2:F_1\times F_2\to F_2
$$

be the coordinate projections. Then

$$
\mathcal B_1\otimes\mathcal B_2
=
\sigma\bigl(
\pi_1^{-1}(\mathcal B_1)
\cup
\pi_2^{-1}(\mathcal B_2)
\bigr),
$$

where

$$
\pi_i^{-1}(\mathcal B_i)
:=
\{\pi_i^{-1}(B):B\in\mathcal B_i\}.
$$

Equivalently, $\mathcal B_1\otimes\mathcal B_2$ is the smallest
$\sigma$-field on $F_1\times F_2$ for which both coordinate projections are
measurable.

Consequently, if $(E,\mathcal A)$ is a measurable space and
$f:E\to F_1\times F_2$, then

$$
f\text{ is }\mathcal A/(\mathcal B_1\otimes\mathcal B_2)\text{-measurable}
$$

if and only if both

$$
\pi_1\circ f:E\to F_1,
\qquad
\pi_2\circ f:E\to F_2
$$

are measurable.

#### Proof

For $B_1\in\mathcal B_1$ and $B_2\in\mathcal B_2$,

$$
\pi_1^{-1}(B_1)=B_1\times F_2,
\qquad
\pi_2^{-1}(B_2)=F_1\times B_2.
$$

These coordinate strips belong to $\mathcal B_1\otimes\mathcal B_2$. Hence

$$
\sigma\bigl(
\pi_1^{-1}(\mathcal B_1)
\cup
\pi_2^{-1}(\mathcal B_2)
\bigr)
\subseteq
\mathcal B_1\otimes\mathcal B_2.
$$

Conversely, every measurable rectangle satisfies

$$
B_1\times B_2
=
\pi_1^{-1}(B_1)\cap\pi_2^{-1}(B_2),
$$

so the reverse inclusion follows from the definition of the product
$\sigma$-field. This proves the identity and the stated minimality.

If $f$ is measurable, then $\pi_1\circ f$ and $\pi_2\circ f$ are measurable
because the projections are measurable.

Conversely, suppose that both coordinate maps are measurable and set

$$
\mathcal D
:=
\{C\subseteq F_1\times F_2:f^{-1}(C)\in\mathcal A\}.
$$

Inverse images commute with complements and countable unions, so
$\mathcal D$ is a $\sigma$-field. Moreover,

$$
f^{-1}\bigl(\pi_i^{-1}(B_i)\bigr)
=
(\pi_i\circ f)^{-1}(B_i)
\in\mathcal A
$$

for every $B_i\in\mathcal B_i$ and $i\in\{1,2\}$. Thus $\mathcal D$ contains
the coordinate strips and therefore contains
$\mathcal B_1\otimes\mathcal B_2$. Hence $f$ is measurable. $\square$

## Corollary 8.2 — Paired Maps and Measurable Operations

Let $(E,\mathcal A)$ be a measurable space, and let

$$
f_1:E\to F_1,
\qquad
f_2:E\to F_2.
$$

Then

$$
(f_1,f_2):E\to F_1\times F_2
\text{ is measurable}
$$

if and only if $f_1$ and $f_2$ are measurable.

If these maps are measurable and

$$
\Phi:(F_1\times F_2,\mathcal B_1\otimes\mathcal B_2)
\to(G,\mathcal C)
$$

is measurable, then

$$
x\longmapsto\Phi\bigl(f_1(x),f_2(x)\bigr)
$$

is measurable. In particular, if $f,g:E\to\mathbb R$ are measurable with
respect to $\mathcal B(\mathbb R)$, then

$$
f+g,
\qquad
fg,
\qquad
f\vee g,
\qquad
f\wedge g
$$

are measurable.

#### Proof

The coordinate maps of $(f_1,f_2)$ are $f_1$ and $f_2$, so the first claim is
Lemma 8.1. The second follows by composition. The four real-valued operations
are induced by continuous maps from $\mathbb R^2$ to $\mathbb R$. $\square$

## Boundary of the Argument

No measures are involved in Lemma 8.1. The object constructed is the product
$\sigma$-field, not a product measure; no finiteness, $\sigma$-finiteness,
Tonelli theorem, or Fubini theorem is used.

The converse direction in the coordinatewise criterion depends on minimality,
not merely on the measurability of the projections. For example, equip
$\mathbb R^2$ with the larger target $\sigma$-field $2^{\mathbb R^2}$. The
coordinate projections remain measurable, but

$$
\operatorname{id}:
(\mathbb R^2,\mathcal B(\mathbb R^2))
\to
(\mathbb R^2,2^{\mathbb R^2})
$$

is not measurable, although both of its coordinate maps are Borel measurable.

Finally, the lemma concerns maps into a product. For a map out of a product,
measurability of every one-variable section does not in general imply joint
measurability. Indeed, let $A\subseteq\mathbb R$ be non-Borel and set

$$
N:=\{(x,x):x\in A\}.
$$

Every vertical and horizontal section of $N$ is either empty or a singleton,
but $N$ is not Borel: otherwise the continuous diagonal map
$x\mapsto(x,x)$ would give the contradiction

$$
A=\{x\in\mathbb R:(x,x)\in N\}\in\mathcal B(\mathbb R).
$$

Thus $\mathbf1_N$ is separately Borel measurable but not jointly Borel
measurable.

## Reconstruction

The reusable chain is

$$
\text{coordinate strips}
\longrightarrow
\text{initial product }\sigma\text{-field}
\longrightarrow
\text{coordinatewise criterion}
\longrightarrow
\text{paired maps}
\longrightarrow
\text{measurable operations}.
$$

---
type: lemma
module: lemmas
status: canonical
---

# Lemma 4 — Generated Sigma-Fields and Measurable Sections

This lemma isolates the stable-class argument which transfers measurability from rectangles to arbitrary sets in a product $\sigma$-field.

## Proposition 4.1 — Existence and Minimality of a Generated Sigma-Field

Let $X$ be a set and let $\mathcal G\subseteq 2^X$. Define

$$
\mathfrak S(\mathcal G)
:=
\left\{
\mathcal S\subseteq 2^X:
\mathcal S\text{ is a }\sigma\text{-field on }X
\text{ and }
\mathcal G\subseteq\mathcal S
\right\}.
$$

Then $\mathfrak S(\mathcal G)$ is nonempty, and

$$
\sigma(\mathcal G)
:=
\bigcap_{\mathcal S\in\mathfrak S(\mathcal G)}\mathcal S
$$

is the unique smallest $\sigma$-field on $X$ containing $\mathcal G$. Equivalently, if $\mathcal T$ is a $\sigma$-field on $X$ and $\mathcal G\subseteq\mathcal T$, then

$$
\sigma(\mathcal G)\subseteq\mathcal T.
$$

#### Proof

The power set $2^X$ is a $\sigma$-field containing $\mathcal G$; hence $\mathfrak S(\mathcal G)\ne\varnothing$. Every member of $\mathfrak S(\mathcal G)$ contains $\mathcal G$, so their intersection contains $\mathcal G$.

Moreover, $\varnothing$ belongs to every member of $\mathfrak S(\mathcal G)$. If $A$ belongs to their intersection, then $A^c$ belongs to every member of $\mathfrak S(\mathcal G)$, and therefore to the intersection. Likewise, if $(A_n)_{n\ge1}$ is contained in the intersection, then

$$
\bigcup_{n\ge1}A_n
$$

belongs to every member of $\mathfrak S(\mathcal G)$, hence to the intersection. Thus $\sigma(\mathcal G)$ is a $\sigma$-field containing $\mathcal G$.

Finally, if $\mathcal T$ is a $\sigma$-field containing $\mathcal G$, then $\mathcal T\in\mathfrak S(\mathcal G)$. Consequently,

$$
\sigma(\mathcal G)
=
\bigcap_{\mathcal S\in\mathfrak S(\mathcal G)}\mathcal S
\subseteq
\mathcal T.
$$

This proves both minimality and uniqueness. $\square$

## Lemma 4.2 — Section Identities

Let $E$ and $F$ be sets. For $C\subseteq E\times F$, $x\in E$, and $y\in F$, define

$$
C_x:=\{z\in F:(x,z)\in C\},
\qquad
C^y:=\{z\in E:(z,y)\in C\}.
$$

For every sequence $(C_n)_{n\ge1}\subseteq 2^{E\times F}$,

$$
(C^c)_x=F\setminus C_x,
\qquad
(C^c)^y=E\setminus C^y,
$$

and

$$
\left(\bigcup_{n\ge1}C_n\right)_x
=
\bigcup_{n\ge1}(C_n)_x,
\qquad
\left(\bigcup_{n\ge1}C_n\right)^y
=
\bigcup_{n\ge1}C_n^y.
$$

Moreover, for $A\subseteq E$ and $B\subseteq F$,

$$
(A\times B)_x
=
\begin{cases}
B,&x\in A,\\
\varnothing,&x\notin A,
\end{cases}
$$

and

$$
(A\times B)^y
=
\begin{cases}
A,&y\in B,\\
\varnothing,&y\notin B.
\end{cases}
$$

Here $C^c$ denotes the complement of $C$ in $E\times F$.

#### Proof

For $z\in F$,

$$
z\in(C^c)_x
\Longleftrightarrow
(x,z)\notin C
\Longleftrightarrow
z\notin C_x,
$$

which proves $(C^c)_x=F\setminus C_x$. Furthermore,

$$
z\in\left(\bigcup_{n\ge1}C_n\right)_x
\Longleftrightarrow
\exists n\ge1, (x,z)\in C_n
\Longleftrightarrow
z\in\bigcup_{n\ge1}(C_n)_x.
$$

The identities for $C^y$ follow by the same argument with the two coordinates interchanged. Finally,

$$
z\in(A\times B)_x
\Longleftrightarrow
x\in A\text{ and }z\in B,
$$

which gives the stated formula for $(A\times B)_x$; the formula for $(A\times B)^y$ is symmetric. $\square$

## Proposition 4.3 — Measurability of Sections

Let $(E,\mathcal A)$ and $(F,\mathcal B)$ be measurable spaces, and let

$$
\mathcal A\otimes\mathcal B
:=
\sigma\bigl(\{A\times B:A\in\mathcal A,\ B\in\mathcal B\}\bigr).
$$

If $C\in\mathcal A\otimes\mathcal B$, then

$$
C_x\in\mathcal B
\quad\text{for every }x\in E,
$$

and

$$
C^y\in\mathcal A
\quad\text{for every }y\in F.
$$

#### Proof

Set

$$
\mathcal D
:=
\left\{
C\subseteq E\times F:
C_x\in\mathcal B\text{ for every }x\in E,
\quad
C^y\in\mathcal A\text{ for every }y\in F
\right\}.
$$

The empty set belongs to $\mathcal D$. By Lemma 4.2 and the closure of $\mathcal A$ and $\mathcal B$ under complements and countable unions,

$$
C\in\mathcal D
\Longrightarrow
C^c\in\mathcal D,
$$

and

$$
(C_n)_{n\ge1}\subseteq\mathcal D
\Longrightarrow
\bigcup_{n\ge1}C_n\in\mathcal D.
$$

Thus $\mathcal D$ is a $\sigma$-field on $E\times F$.

Let $A\in\mathcal A$ and $B\in\mathcal B$. Lemma 4.2 gives

$$
(A\times B)_x\in\{B,\varnothing\}\subseteq\mathcal B,
\qquad
(A\times B)^y\in\{A,\varnothing\}\subseteq\mathcal A.
$$

Hence every measurable rectangle belongs to $\mathcal D$. Proposition 4.1 now yields

$$
\mathcal A\otimes\mathcal B
\subseteq
\mathcal D,
$$

which is precisely the desired conclusion. $\square$

## Boundary of the Argument

The proof uses only set-theoretic section identities, closure under the $\sigma$-field operations, and the minimality of a generated $\sigma$-field. It does not use a product measure, Tonelli's theorem, or Fubini's theorem.

It establishes the inclusion

$$
\mathcal A\otimes\mathcal B\subseteq\mathcal D;
$$

no converse inclusion is asserted.

## Reconstruction

The argument is the chain

$$
\text{section identities}
\longrightarrow
\mathcal D\text{ is a }\sigma\text{-field}
\longrightarrow
\text{rectangles belong to }\mathcal D
\longrightarrow
\mathcal A\otimes\mathcal B\subseteq\mathcal D.
$$

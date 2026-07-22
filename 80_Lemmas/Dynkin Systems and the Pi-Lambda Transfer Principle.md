---
type: lemma
module: lemmas
status: canonical
---

# Lemma 9 — Dynkin Systems and the π–λ Transfer Principle

This lemma isolates the closure mechanism which transfers a property from a
generating $\pi$-system to the generated $\sigma$-field.

## Definition 9.1 — The Two Closure Structures

Let $E$ be a set. A nonempty class $\mathcal P\subseteq2^E$ is a
$\pi$-system if

$$
A,B\in\mathcal P
\Longrightarrow
A\cap B\in\mathcal P.
$$

A class $\mathcal D\subseteq2^E$ is a Dynkin system if:

1. $E\in\mathcal D$;
2. if $A,B\in\mathcal D$ and $A\subseteq B$, then
   $B\setminus A\in\mathcal D$;
3. if $(A_n)_{n\ge1}\subseteq\mathcal D$ is pairwise disjoint, then

   $$
   \bigcup_{n\ge1}A_n\in\mathcal D.
   $$

For $\mathcal G\subseteq2^E$, write $\lambda(\mathcal G)$ for the
smallest Dynkin system containing $\mathcal G$, namely the intersection of
all Dynkin systems containing $\mathcal G$. Every $\sigma$-field is a Dynkin
system, so

$$
\lambda(\mathcal G)\subseteq\sigma(\mathcal G).
$$

## Theorem 9.2 — The π–λ Theorem

If $\mathcal P$ is a $\pi$-system on $E$, then

$$
\boxed{
\lambda(\mathcal P)=\sigma(\mathcal P).
}
$$

Equivalently, every Dynkin system containing $\mathcal P$ contains
$\sigma(\mathcal P)$.

#### Proof

Set

$$
\mathcal L:=\lambda(\mathcal P).
$$

Since every $\sigma$-field is a Dynkin system,

$$
\mathcal L\subseteq\sigma(\mathcal P).
$$

It remains to prove that $\mathcal L$ is itself a $\sigma$-field. The decisive
step is closure under finite intersections.

Fix $A\in\mathcal P$ and define

$$
\mathcal L_A
:=
\{B\subseteq E:A\cap B\in\mathcal L\}.
$$

###### $\mathcal L_A$ is a Dynkin system

The class $\mathcal L_A$ is a Dynkin system. Indeed,
$$
A\cap E=A\in\mathcal P\subseteq\mathcal L,
$$

so $E\in\mathcal L_A$. If $B,C\in\mathcal L_A$ and $B\subseteq C$, then

$$
A\cap(C\setminus B)
=
(A\cap C)\setminus(A\cap B)
\in\mathcal L.
$$

Finally, if $(B_n)$ is pairwise disjoint in $\mathcal L_A$, then

$$
A\cap\bigcup_{n\ge1}B_n
=
\bigcup_{n\ge1}(A\cap B_n)
\in\mathcal L,
$$

and the union on the right is disjoint. Thus $\mathcal L_A$ is a Dynkin
system.

###### Minimality of  $\mathcal L$

Since $\mathcal P$ is a $\pi$-system,

$$
B\in\mathcal P
\Longrightarrow
A\cap B\in\mathcal P\subseteq\mathcal L.
$$

Hence $\mathcal P\subseteq\mathcal L_A$. By the minimality of
$\mathcal L=\lambda(\mathcal P)$,

$$
\mathcal L\subseteq\mathcal L_A.
$$

We have proved

$$
A\in\mathcal P,\ B\in\mathcal L
\Longrightarrow
A\cap B\in\mathcal L.
$$

Now fix $B\in\mathcal L$ and define

$$
\mathcal L^B
:=
\{A\subseteq E:A\cap B\in\mathcal L\}.
$$

Since $E\cap B=B\in\mathcal L$, one has $E\in\mathcal L^B$. The
same difference and disjoint-union identities show that $\mathcal L^B$ is a
Dynkin system. The preceding step gives

$$
\mathcal P\subseteq\mathcal L^B,
$$

so minimality again yields

$$
\mathcal L\subseteq\mathcal L^B.
$$

Therefore

$$
A,B\in\mathcal L
\Longrightarrow
A\cap B\in\mathcal L.
$$

A Dynkin system closed under finite intersections is a $\sigma$-field. To see
this directly, complements belong to $\mathcal L$ because
$$
A^c=E\setminus A.
$$

Finite unions then follow from finite intersections and complements. For an
arbitrary sequence $(A_n)\subseteq\mathcal L$, define
$$
B_1:=A_1,
\qquad
B_n:=A_n\setminus\bigcup_{k<n}A_k
\quad(n\ge2).
$$

The sets $B_n$ belong to $\mathcal L$, are pairwise disjoint, and satisfy

$$
\bigcup_{n\ge1}B_n
=
\bigcup_{n\ge1}A_n.
$$

The Dynkin property therefore gives closure under arbitrary countable unions.
Thus $\mathcal L$ is a $\sigma$-field containing $\mathcal P$, and hence
$$
\sigma(\mathcal P)
\subseteq
\mathcal L
\subseteq
\sigma(\mathcal P).
$$

This proves the theorem. $\square$



## Corollary 9.3 — Property Transfer

Let $\mathcal P$ be a $\pi$-system and let $Q(C)$ be a property of subsets of
$E$. Define

$$
\mathcal D_Q
:=
\{C\subseteq E:Q(C)\text{ holds}\}.
$$

If $\mathcal D_Q$ is a Dynkin system and

$$
\mathcal P\subseteq\mathcal D_Q,
$$

then

$$
\sigma(\mathcal P)\subseteq\mathcal D_Q.
$$

#### Proof

The minimality of $\lambda(\mathcal P)$ gives

$$
\lambda(\mathcal P)\subseteq\mathcal D_Q.
$$

Apply Theorem 9.2. $\square$

## Corollary 9.4 — Uniqueness on a Generating π-System

Let $(E,\mathcal A)$ be a measurable space, let $\mathcal P$ be a
$\pi$-system such that

$$
\sigma(\mathcal P)=\mathcal A,
$$

and let $\mu$ and $\nu$ be finite signed measures on $\mathcal A$.
Assume that

$$
\mu(E)=\nu(E)
$$

and

$$
\mu(P)=\nu(P)
\qquad
\text{for every }P\in\mathcal P.
$$

Then

$$
\mu=\nu
\qquad
\text{on }\mathcal A.
$$

#### Proof

Set

$$
\mathcal D
:=
\{A\in\mathcal A:\mu(A)=\nu(A)\}.
$$

The equality of total masses gives $E\in\mathcal D$. If
$A,B\in\mathcal D$ and $A\subseteq B$, finite additivity gives

$$
\mu(B\setminus A)
=
\mu(B)-\mu(A)
=
\nu(B)-\nu(A)
=
\nu(B\setminus A).
$$

If $(A_n)$ is pairwise disjoint in $\mathcal D$, countable additivity gives

$$
\mu\left(\bigcup_{n\ge1}A_n\right)
=
\sum_{n\ge1}\mu(A_n)
=
\sum_{n\ge1}\nu(A_n)
=
\nu\left(\bigcup_{n\ge1}A_n\right).
$$

Thus $\mathcal D$ is a Dynkin system containing $\mathcal P$. Corollary 9.3
gives $\mathcal D=\mathcal A$. $\square$

If $E\in\mathcal P$, equality of total masses is already included in the
hypothesis on $\mathcal P$. For probability measures it is automatic.

## Corollary 9.5 — The σ-Finite Localization Interface

Let $\mu$ and $\nu$ be measures on $(E,\mathcal A)$, and let
$\mathcal P$ be a $\pi$-system generating $\mathcal A$. Assume that

$$
\mu(P)=\nu(P)
\qquad
\text{for every }P\in\mathcal P,
$$

and that there exist $(P_n)_{n\ge1}\subseteq\mathcal P$ such that

$$
P_n\uparrow E,
\qquad
\mu(P_n)=\nu(P_n)<+\infty.
$$

Then $\mu=\nu$ on $\mathcal A$.

#### Proof

For each $n$, restrict the measures to the measurable space

$$
\left(P_n,\mathcal A|_{P_n}\right),
\qquad
\mathcal A|_{P_n}
:=
\{A\cap P_n:A\in\mathcal A\}.
$$

The class

$$
\mathcal P_n
:=
\{P\cap P_n:P\in\mathcal P\}
$$

is a $\pi$-system. Since the trace operation commutes with complements
relative to $P_n$ and with countable unions,

$$
\sigma_{P_n}(\mathcal P_n)=\mathcal A|_{P_n}.
$$

Moreover, $P\cap P_n\in\mathcal P$, so the two restricted finite measures
agree on $\mathcal P_n$, and their common total mass is finite. Corollary 9.4
therefore gives

$$
\mu(A\cap P_n)=\nu(A\cap P_n)
\qquad
\text{for every }A\in\mathcal A.
$$

Letting $n\to\infty$ and using continuity from below yields

$$
\mu(A)=\nu(A)
$$

for every $A\in\mathcal A$. $\square$

## Deployment Map

The theorem is useful precisely when the target class is naturally stable
under differences and disjoint unions but is not visibly a $\sigma$-field.

- **Generated-$\sigma$-field route.** If the target class is already a
  $\sigma$-field, use generated-$\sigma$-field minimality, as in
  [Lemma 4 — Generated Sigma-Fields and Measurable Sections](Generated%20Sigma-Fields%20and%20Measurable%20Sections.md).
- **Product rectangles.** Measurable rectangles form a $\pi$-system generating
  the product $\sigma$-field. In the finite-measure regime, complement
  subtraction and disjoint-union stability transfer the section-integral
  identity from rectangles to arbitrary product-measurable sets; see
  [Lemma 10 — Section-Mass Representation of Product Measures](Section-Mass%20Representation%20of%20Product%20Measures.md).
- **Conditional-expectation tests.** For $Y,Z\in L^1$, the set functions

  $$
  A\longmapsto\mathbb E[Y\mathbf1_A],
  \qquad
  A\longmapsto\mathbb E[Z\mathbf1_A]
  $$

  are finite signed measures. Agreement on a generating $\pi$-system,
  together with agreement of total masses, therefore extends to the entire
  observed $\sigma$-field; see
  [RN Construction](../40_Conditional-Expectation/03_Corriges/TD%2001%20—%20RN%20Construction.md).

## Boundary of the Argument

The π–λ theorem transfers a verified property; it neither proves that the
chosen $\pi$-system generates the intended $\sigma$-field nor constructs a
measure on that $\sigma$-field. Both tasks require separate arguments.

Finiteness in Corollary 9.4 prevents undefined expressions of the form
$+\infty-(+\infty)$. In a $\sigma$-finite regime, one must first localize to a
common finite exhaustion satisfying the hypotheses of Corollary 9.5. Separate
$\sigma$-finiteness without such a usable generating exhaustion is not the
statement proved here.

The monotone-class theorem is a different closure mechanism, especially for
linear spaces of functions. It is not part of the present lemma.

## Reconstruction

The proof and deployment chain is

$$
\pi\text{-system }\mathcal P
\longrightarrow
\lambda(\mathcal P)
\xrightarrow{\text{freeze one factor twice}}
\text{finite-intersection closure}
\longrightarrow
\lambda(\mathcal P)=\sigma(\mathcal P)
\longrightarrow
\text{property transfer}.
$$

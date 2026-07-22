---
type: cours-note
module: lp-interface
status: canonical
---

# Minimal \(L^1\) Recall for Measure Decompositions

## 1. From \(\mathcal L^1(\mu)\) to \(L^1(\mu)\)

For a measure space \((E,\mathcal E,\mu)\), define

\[
\mathcal L^1(\mu)
=
\left\{
f:E\to\mathbb R:
f\text{ is measurable and }
\int_E |f|\,d\mu<\infty
\right\}.
\]

Two functions are identified when they are equal \(\mu\)-almost everywhere:

\[
f\sim_\mu g
\quad\Longleftrightarrow\quad
f=g
\quad
\mu\text{-a.e.}
\]

The space

\[
L^1(\mu)
=
\mathcal L^1(\mu)/{\sim_\mu}
\]

therefore consists of equivalence classes rather than pointwise-defined functions.

Its norm is

\[
\|f\|_{L^1(\mu)}
=
\int_E |f|\,d\mu.
\]

In practice, one usually writes \(f\in L^1(\mu)\) while silently choosing a measurable representative.

---

## 2. Integrability and signed integrals

A measurable function \(f\) belongs to \(L^1(\mu)\) exactly when

\[
\int_E |f|\,d\mu<\infty.
\]

Equivalently, writing

\[
f=f^+-f^-,
\qquad
|f|=f^++f^-,
\]

one has

\[
\int_E f^+\,d\mu<\infty,
\qquad
\int_E f^-\,d\mu<\infty.
\]

Only after absolute integrability has been established may one freely use

\[
\int_E f\,d\mu
=
\int_E f^+\,d\mu
-
\int_E f^-\,d\mu.
\]

---

## 3. Comparing \(L^1\)-spaces under different measures

There is no automatic inclusion between

\[
L^1(\mu)
\quad\text{and}\quad
L^1(\nu).
\]

The relevant comparison condition is usually a domination estimate.

If

\[
\nu\le C\mu,
\]

meaning

\[
\nu(B)\le C\mu(B)
\]

for every measurable set \(B\), then for every nonnegative measurable \(f\),

\[
\int_E f\,d\nu
\le
C\int_E f\,d\mu.
\]

Hence

\[
f\in L^1(\mu)
\quad\Longrightarrow\quad
f\in L^1(\nu),
\]

with the norm bound

\[
\|f\|_{L^1(\nu)}
\le
C\|f\|_{L^1(\mu)}.
\]

Since \(\nu\ll\mu\), domination of measures induces a well-defined bounded map

\[
T_{\mu\to\nu}:L^1(\mu)\longrightarrow L^1(\nu),
\qquad
[f]_\mu\longmapsto[f]_\nu.
\]

This map need not be injective. For example, if \(A\) is \(\nu\)-null and \(0<\mu(A)<\infty\), then the nonzero class \([\mathbf1_A]_\mu\) maps to zero. The reverse relation \(\mu\ll\nu\) is a natural sufficient condition for injectivity; without such a condition, a hook arrow is not justified.

---

## 4. Radon–Nikodym formulation

Assume that \(\nu\) admits a Radon–Nikodym density with respect to \(\mu\), and write

\[
h=\frac{d\nu}{d\mu},
\qquad
\nu=h\mu.
\]

Then for every nonnegative measurable \(f\),

\[
\int_E f\,d\nu
=
\int_E fh\,d\mu.
\]

Consequently,

\[
f\in L^1(\nu)
\quad\Longleftrightarrow\quad
\int_E |f|h\,d\mu<\infty.
\]

In particular, if

\[
h\le C
\qquad
\mu\text{-a.e.},
\]

then

\[
\|f\|_{L^1(\nu)}
\le
C\|f\|_{L^1(\mu)}.
\]

In particular, this bound implies the measure inequality

\[
\nu\le C\mu.
\]

---

## 5. Positive finite mixtures

Suppose

\[
\mu
=
a_1\mu_1+\cdots+a_n\mu_n,
\qquad
a_k>0.
\]

Then for every measurable set \(B\),

\[
a_k\mu_k(B)\le\mu(B),
\]

so

\[
\mu_k\le \frac1{a_k}\mu.
\]

Therefore the canonical maps

\[
T_k:L^1(\mu)\longrightarrow L^1(\mu_k),
\qquad
[f]_\mu\longmapsto[f]_{\mu_k},
\]

are well defined and satisfy

\[
\|f\|_{L^1(\mu_k)}
\le
\frac1{a_k}\|f\|_{L^1(\mu)}.
\]

Equivalently, for nonnegative measurable \(f\),

\[
\int_E f\,d\mu
=
\sum_{k=1}^n a_k\int_E f\,d\mu_k.
\]

If the left-hand side is finite, then every term on the right-hand side is finite because all coefficients \(a_k\) are strictly positive.

The maps \(T_k\) need not be injective: \(\mu\) may see sets that \(\mu_k\) does not.

---

## 6. Transfer of almost-everywhere statements

If

\[
\nu\ll\mu,
\]

then every \(\mu\)-null set is also \(\nu\)-null. Hence

\[
f=g
\quad
\mu\text{-a.e.}
\quad\Longrightarrow\quad
f=g
\quad
\nu\text{-a.e.}
\]

The converse generally fails.

If both

\[
\nu\ll\mu
\qquad\text{and}\qquad
\mu\ll\nu,
\]

then \(\mu\) and \(\nu\) have the same null sets, and therefore

\[
f=g
\quad
\mu\text{-a.e.}
\quad\Longleftrightarrow\quad
f=g
\quad
\nu\text{-a.e.}
\]

---

## 7. The representative issue

A rule such as

\[
[f]_\mu\longmapsto[f]_\nu
\]

is not merely a statement about integrability.

Since \(L^1(\mu)\) and \(L^1(\nu)\) use different equivalence relations, one must verify that the map

\[
[f]_\mu\longmapsto[f]_\nu
\]

is well-defined.

This holds whenever

\[
\nu\ll\mu,
\]

because

\[
f=g
\quad
\mu\text{-a.e.}
\]

then implies

\[
f=g
\quad
\nu\text{-a.e.}
\]

Thus two checks are required before this rule defines a map on all of \(L^1(\mu)\):

1. **integrability transfer**
   \[
   f\in L^1(\mu)\Longrightarrow f\in L^1(\nu);
   \]

2. **equivalence-class compatibility**
   \[
   f=g\ \mu\text{-a.e.}
   \Longrightarrow
   f=g\ \nu\text{-a.e.}
   \]

The first usually follows from a domination estimate.  
The second follows from absolute continuity.

Injectivity is a third, separate issue. It follows from the reverse relation

\[
\mu\ll\nu.
\]

Without this reverse absolute continuity, the canonical map may collapse nonzero \(L^1(\mu)\)-classes and should not be called an inclusion.

---

## 8. Proof spine to retain

For a positive measure decomposition, the relevant \(L^1\)-logic is

\[
\boxed{
\mu=\sum_k a_k\mu_k,\quad a_k>0
}
\]

\[
\Downarrow
\]

\[
\boxed{
\mu_k\le a_k^{-1}\mu
}
\]

\[
\Downarrow
\]

\[
\boxed{
\|f\|_{L^1(\mu_k)}
\le
a_k^{-1}\|f\|_{L^1(\mu)}
}
\]

\[
\Downarrow
\]

\[
\boxed{
T_k:L^1(\mu)\longrightarrow L^1(\mu_k)
\text{ is well defined and bounded}
}
\]

together with

\[
\mu_k\ll\mu,
\]

which guarantees compatibility of the corresponding almost-everywhere equivalence classes.

No injectivity is asserted without the reverse relation \(\mu\ll\mu_k\).

---
type: application
module: applications
status: canonical
---

# Dominated Statistical Models

Let \((\mathcal H,\mathscr H)\) be a measurable space and let

\[
(P_\theta)_{\theta\in\Theta}
\]

be a family of probability measures on it.

---

## 1. Dominated Models

The model is **dominated** if there exists a \(\sigma\)-finite measure \(\mu\) such that

\[
P_\theta\ll\mu,
\qquad
\forall\theta\in\Theta.
\]

By the Radon–Nikodym theorem, there exists a measurable function

\[
f_\theta
=
\frac{dP_\theta}{d\mu}
\ge 0
\]

such that

\[
P_\theta(A)
=
\int_A f_\theta\,d\mu,
\qquad
A\in\mathscr H.
\]

The measure \(\mu\) is a common reference measure for the model.

---

## 2. Absolute Continuity and Equivalence

For two measures \(\nu\) and \(\mu\),

\[
\nu\ll\mu
\]

means

\[
\mu(A)=0
\Longrightarrow
\nu(A)=0.
\]

The measures are equivalent,

\[
\nu\sim\mu,
\]

if

\[
\nu\ll\mu
\qquad\text{and}\qquad
\mu\ll\nu.
\]

Equivalently, \(\nu\) and \(\mu\) have the same null sets.

---

## 3. Zero Set of a Density

Suppose

\[
\nu=f\mu,
\qquad
f=\frac{d\nu}{d\mu}.
\]

Let

\[
Z=\{f=0\}.
\]

Then

\[
\nu(Z)
=
\int_Z f\,d\mu
=
0.
\]

Hence

\[
f>0
\qquad
\nu\text{-a.s.}
\]

This does not imply

\[
f>0
\qquad
\mu\text{-a.e.}
\]

Indeed, \(Z\) may have positive \(\mu\)-measure while remaining \(\nu\)-null.

---

## 4. Strict Positivity and Equivalence

If

\[
\nu=f\mu,
\]

then

\[
f>0
\qquad
\mu\text{-a.e.}
\]

if and only if

\[
\nu\sim\mu.
\]

Since \(\nu\ll\mu\) is already known, strict positivity gives the reverse implication

\[
\nu(A)=0
\Longrightarrow
\mu(A)=0.
\]

Thus, in a dominated model,

\[
f_\theta>0
\qquad
\mu\text{-a.e.}
\]

is equivalent to

\[
P_\theta\sim\mu.
\]

---

## 5. Reciprocal Radon–Nikodym Derivative

If

\[
\nu\sim\mu
\]

and

\[
f
=
\frac{d\nu}{d\mu}
>0
\qquad
\mu\text{-a.e.},
\]

then

\[
\frac{d\mu}{d\nu}
=
\frac{1}{f}
\qquad
\nu\text{-a.e.}
\]

The value assigned to \(1/f\) on \(\{f=0\}\) is irrelevant, since this set is \(\nu\)-null.

---

## 6. Homogeneous Models

The model is **homogeneous** if

\[
P_\theta\ll P_{\theta_0},
\qquad
\forall(\theta,\theta_0)\in\Theta^2.
\]

Since the condition holds for every ordered pair,

\[
P_\theta\sim P_{\theta_0},
\qquad
\forall\theta,\theta_0\in\Theta.
\]

Thus all distributions in the model have the same null sets.

The model is homogeneous if and only if there exists a dominating measure \(\mu\) such that, for every \(\theta\in\Theta\),

\[
f_\theta
=
\frac{dP_\theta}{d\mu}
>0
\qquad
\mu\text{-a.e.}
\]

The structural chain is

\[
f_\theta>0\ \mu\text{-a.e.}
\Longleftrightarrow
P_\theta\sim\mu
\Longrightarrow
P_\theta\sim P_{\theta_0}.
\]

Conversely, if all \(P_\theta\) are mutually equivalent, any fixed \(P_{\theta_*}\) may be chosen as a dominating measure.

---

## 7. Technical Facts

### Non-negative Integral

If \(g\ge 0\), then

\[
\int_A g\,d\mu=0
\]

if and only if

\[
g=0
\qquad
\mu\text{-a.e. on }A.
\]

### Versions of Densities

The derivative

\[
\frac{d\nu}{d\mu}
\]

is defined only up to \(\mu\)-almost-everywhere equality.

It may be modified arbitrarily on a \(\mu\)-null set, but not on a set of positive \(\mu\)-measure.

---

## Core Principle

For

\[
\nu=f\mu,
\]

one always has

\[
f>0
\qquad
\nu\text{-a.s.},
\]

whereas

\[
f>0
\qquad
\mu\text{-a.e.}
\]

holds exactly when

\[
\nu\sim\mu.
\]

Hence

\[
\boxed{
\text{strict positivity of densities}
\Longleftrightarrow
\text{equality of null sets}
}
\]

---
type: corrige
module: radon-nikodym
status: canonical
td: "TD 02 — Constructing the Density"
---

# Corrigé — TD 02: Constructing the Density

## Exercise 1 — Maximal representable submeasure

Let

$$
\mathcal C
=
\{f\ge0\text{ measurable}:f\mu\le\nu\}
$$

and

$$
\alpha
=
\sup_{f\in\mathcal C}\int_Ef\,d\mu.
$$

### 1. Nonemptiness, maxima and bounded mass

The zero function belongs to $\mathcal C$, so the class is nonempty.

Let $f,h\in\mathcal C$ and set

$$
B=\{f\ge h\}.
$$

For every $A\in\mathcal A$,

$$
\begin{aligned}
\int_A(f\vee h)\,d\mu
&=
\int_{A\cap B}f\,d\mu
+
\int_{A\cap B^c}h\,d\mu\\
&\le
\nu(A\cap B)+\nu(A\cap B^c)\\
&=\nu(A).
\end{aligned}
$$

Thus $f\vee h\in\mathcal C$.

For every $f\in\mathcal C$,

$$
0
\le
\int_Ef\,d\mu
=(f\mu)(E)
\le
\nu(E).
$$

Therefore

$$
0\le\alpha\le\nu(E)<+\infty.
$$

### 2. Attainment of the maximal mass

Choose $f_n\in\mathcal C$ such that

$$
\int_Ef_n\,d\mu
\longrightarrow
\alpha.
$$

Set

$$
g_n=f_1\vee\cdots\vee f_n.
$$

Finite stability gives $g_n\in\mathcal C$, and $g_n\uparrow g$, where

$$
g=\sup_ng_n.
$$

For every $A$, MCT gives

$$
\int_Ag\,d\mu
=
\lim_{n\to\infty}\int_Ag_n\,d\mu
\le
\nu(A).
$$

Hence $g\in\mathcal C$.

Since $g_n\ge f_n$,

$$
\int_Eg_n\,d\mu
\ge
\int_Ef_n\,d\mu.
$$

Every $g_n$ belongs to $\mathcal C$, so its integral is at most $\alpha$. Passing to the limit gives

$$
\boxed{
\int_Eg\,d\mu=\alpha
}.
$$

### 3. Finiteness almost everywhere

Since

$$
\int_Eg\,d\mu
=
\alpha
<+\infty,
$$

the set $\{g=+\infty\}$ must be $\mu$-null. Thus $g<+\infty$ almost everywhere.

Replacing $g$ by $0$ on this null set does not change $g\mu$. We may therefore take $g:E\to[0,+\infty)$ before continuing the construction.

## Exercise 2 — Elimination of the residue and uniqueness

Define

$$
\rho=\nu-g\mu.
$$

### 1. Positivity and absolute continuity

Because $g\in\mathcal C$,

$$
g\mu\le\nu.
$$

Thus $\rho$ is a finite positive measure. If $\mu(A)=0$, then

$$
\nu(A)=0,
\qquad
(g\mu)(A)=0,
$$

and therefore $\rho(A)=0$. Hence

$$
\rho\ll\mu.
$$

### 2. Contradiction to maximality

Assume $\rho\ne0$. The local density fragment lemma gives $\varepsilon>0$ and $P\in\mathcal A$ such that

$$
\mu(P)>0,
\qquad
\varepsilon\mathbf1_P\mu\le\rho.
$$

Set

$$
h=g+\varepsilon\mathbf1_P.
$$

Then

$$
h\mu
\le
g\mu+\rho
=
\nu,
$$

so $h\in\mathcal C$. But

$$
\int_Eh\,d\mu
=
\alpha+\varepsilon\mu(P)
>
\alpha,
$$

contradicting the definition of $\alpha$.

### 3. Representation

The contradiction forces $\rho=0$. Therefore

$$
\boxed{
\nu=g\mu
}.
$$

### 4. Uniqueness in the finite regime

Assume

$$
f_1\mu=f_2\mu
$$

and that this common measure is finite. Then $f_1,f_2\in L^1_+(\mu)$. Let

$$
A=\{f_1>f_2\}.
$$

Equality of the measures gives

$$
\int_Af_1\,d\mu
=
\int_Af_2\,d\mu.
$$

Hence

$$
\int_A(f_1-f_2)\,d\mu=0.
$$

The integrand is nonnegative, so $f_1=f_2$ almost everywhere on $A$. It follows that $\mu(A)=0$. Reversing the roles of $f_1$ and $f_2$ gives

$$
\mu(f_2>f_1)=0.
$$

Thus

$$
\boxed{
f_1=f_2
\qquad\mu\text{-a.e.}
}.
$$

## Exercise 3 — $\sigma$-finite gluing

### 1. A common finite partition

Choose increasing measurable covers $(M_n)$ and $(N_n)$ such that

$$
M_n\uparrow E,
\qquad
N_n\uparrow E,
$$

with

$$
\mu(M_n)<+\infty,
\qquad
\nu(N_n)<+\infty.
$$

Set

$$
C_n=M_n\cap N_n.
$$

Then $C_n\uparrow E$ and both measures are finite on $C_n$. Define

$$
E_1=C_1,
\qquad
E_n=C_n\setminus C_{n-1}
\quad(n\ge2).
$$

The sets $(E_n)$ form the required measurable partition.

### 2. Local densities

For each $n$, the restricted measures

$$
\mu_n=\mu|_{E_n},
\qquad
\nu_n=\nu|_{E_n}
$$

are finite and satisfy $\nu_n\ll\mu_n$. The finite theorem gives a measurable $f_n:E_n\to[0,+\infty)$ such that

$$
\nu(A\cap E_n)
=
\int_{A\cap E_n}f_n\,d\mu.
$$

### 3. Gluing

Define

$$
f
=
\sum_{n\ge1}f_n\mathbf1_{E_n}.
$$

This function is measurable. Since the summands are nonnegative and have disjoint supports,

$$
\begin{aligned}
\int_Af\,d\mu
&=
\sum_{n\ge1}
\int_{A\cap E_n}f_n\,d\mu\\
&=
\sum_{n\ge1}\nu(A\cap E_n)\\
&=\nu(A).
\end{aligned}
$$

Thus $\nu=f\mu$.

### 4. Global uniqueness

If $h$ is another density, then for every $n$ and every measurable $A$,

$$
\int_{A\cap E_n}h\,d\mu
=
\nu(A\cap E_n)
=
\int_{A\cap E_n}f_n\,d\mu.
$$

Finite uniqueness on $E_n$ gives $h=f_n$ almost everywhere on $E_n$. Taking the countable union of the exceptional null sets yields

$$
h=f
\qquad\mu\text{-a.e. on }E.
$$

## Exercise 4 — Equivalent finite measures

Let

$$
\eta=\mu+\nu.
$$

### Preliminary common cover

From $\sigma$-finiteness, choose increasing covers $(M_n)$ and $(N_n)$ on which $\mu$ and $\nu$ are finite. Then

$$
A_n=M_n\cap N_n
$$

increases to $E$ and satisfies $\eta(A_n)<+\infty$. Thus $\eta$ is $\sigma$-finite.

### 1. The common weight

Set

$$
w_\eta
=
\sum_{n\ge1}
\frac{2^{-n}}{1+\eta(A_n)}\mathbf1_{A_n}.
$$

Because the sets cover $E$, at least one summand is positive at every point. Hence

$$
w_\eta>0.
$$

Also,

$$
w_\eta
\le
\sum_{n\ge1}2^{-n}
<+\infty.
$$

By MCT,

$$
\begin{aligned}
\eta^*(E)
&=
\int_Ew_\eta\,d\eta\\
&=
\sum_{n\ge1}
\frac{2^{-n}}{1+\eta(A_n)}\eta(A_n)\\
&\le
\sum_{n\ge1}2^{-n}
<+\infty.
\end{aligned}
$$

Since $\mu,\nu\le\eta$, one has

$$
\mu^*,\nu^*\le\eta^*.
$$

Thus all three weighted measures are finite.

### 2. Equivalence and absolute continuity

For any positive measure $\theta$, multiplication by an everywhere positive measurable function preserves null sets:

$$
(w_\eta\theta)(A)=0
\quad\Longleftrightarrow\quad
\theta(A)=0.
$$

Therefore

$$
\eta^*\sim\eta,
\qquad
\mu^*\sim\mu,
\qquad
\nu^*\sim\nu.
$$

If $\mu^*(A)=0$, then $\mu(A)=0$. Since $\nu\ll\mu$, one has $\nu(A)=0$, and hence $\nu^*(A)=0$. Thus

$$
\nu^*\ll\mu^*.
$$

### 3. Removing the common weight

The finite theorem gives $f\ge0$ such that

$$
\nu^*=f\mu^*.
$$

Since $0<w_\eta<+\infty$, the function $\mathbf1_A/w_\eta$ is nonnegative measurable. Integrating it against the equality of measures gives

$$
\begin{aligned}
\nu(A)
&=
\int_E\frac{\mathbf1_A}{w_\eta}\,d\nu^*\\
&=
\int_E\frac{\mathbf1_A}{w_\eta}f\,d\mu^*\\
&=
\int_Af\,d\mu.
\end{aligned}
$$

Therefore

$$
\boxed{
\nu=f\mu
}.
$$

### 4. Comparison of the reductions

The disjoint-gluing method localizes the theorem to countably many finite pieces and then assembles the local densities. It makes the $\sigma$-finite structure explicit and proves uniqueness piecewise.

The common-weight method replaces both measures by finite equivalent measures on the whole space. It produces one global finite problem, but requires the additional argument that an everywhere positive weight may be removed.

Neither method changes null sets. Their difference is representational, not mathematical substance.

## Reconstruction — Finite theorem and global passage

The finite proof must generate the objects in the following order:

1. $\mathcal C$: all density fragments dominated by $\nu$;
2. $\alpha$: maximal represented mass;
3. $g_n$: finite maxima of a maximizing sequence;
4. $g$: monotone supremum attaining $\alpha$;
5. $\rho=\nu-g\mu$: the positive residual;
6. $\varepsilon\mathbf1_P$: a fragment extracted from any nonzero residual.

The last object contradicts maximality, so $\rho=0$.

Uniqueness in the finite theorem uses finiteness of the common represented measure so that the difference may be tested on $\{f_1>f_2\}$ and $\{f_2>f_1\}$. In the $\sigma$-finite theorem, uniqueness is recovered by localization to the common finite partition.

The global theorem then follows either by disjoint gluing or by passage to equivalent finite measures.

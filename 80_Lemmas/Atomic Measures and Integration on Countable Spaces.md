---
type: lemma
module: lemmas
status: canonical
---

# Lemma 6 — Atomic Measures and Integration on Countable Spaces

This lemma isolates the constructive mechanism of integration on a countable state space: singleton weights generate the measure, and integration reduces to a nonnegative series. The complementary failure of this representation outside the countable regime is treated in [Lemma 5 — Counting Measure and the Radon–Nikodym Boundary](Counting%20Measure%20and%20the%20Radon–Nikodym%20Boundary.md).

## Proposition 6.1 — Weighted Atomic Measure

Let $E$ be at most countable and equip it with $2^E$. Let

$$
w:E\longrightarrow[0,+\infty].
$$

For every $A\subseteq E$, define

$$
\mu_w(A)
:=
\sum_{x\in A}w(x),
$$

where the sum is a nonnegative sum and may equal $+\infty$. Then $\mu_w$ is a positive measure on $(E,2^E)$, and

$$
\mu_w(\{x\})=w(x)
\qquad(x\in E).
$$

### Proof

One has $\mu_w(\varnothing)=0$. Let $(A_n)_{n\ge1}$ be pairwise disjoint subsets of $E$. Since nonnegative sums are invariant under disjoint regrouping,

$$
\begin{aligned}
\mu_w\!\left(\bigsqcup_{n\ge1}A_n\right)
&=
\sum_{x\in\bigsqcup_{n\ge1}A_n}w(x)\\
&=
\sum_{n\ge1}\sum_{x\in A_n}w(x)\\
&=
\sum_{n\ge1}\mu_w(A_n).
\end{aligned}
$$

Thus $\mu_w$ is countably additive. The singleton identity follows directly from the definition. $\square$

## Proposition 6.2 — Atomic Integration Formula

Let $f:E\to[0,+\infty]$. Then, for every $A\subseteq E$,

$$
\boxed{
\int_A f\,d\mu_w
=
\sum_{x\in A}f(x)w(x)
}.
$$

The extended product is understood with the convention

$$
0\cdot(+\infty)=0.
$$

### Proof

Choose finite sets $(F_n)_{n\ge1}$ such that

$$
F_n\subseteq F_{n+1}
\qquad\text{and}\qquad
A=\bigcup_{n\ge1}F_n.
$$

For finite $A$, one may take $F_n=A$ for every $n$. Define

$$
s_n
:=
\sum_{x\in F_n}(f(x)\wedge n)\mathbf1_{\{x\}}.
$$

Each $s_n$ is a finite-valued nonnegative simple function, and

$$
0\le s_n\uparrow f\mathbf1_A
$$

pointwise. By the Monotone Convergence Theorem and the simple-function formula,

$$
\begin{aligned}
\int_A f\,d\mu_w
&=
\lim_{n\to\infty}\int_Es_n\,d\mu_w\\
&=
\lim_{n\to\infty}
\sum_{x\in F_n}(f(x)\wedge n)\mu_w(\{x\})\\
&=
\lim_{n\to\infty}
\sum_{x\in F_n}(f(x)\wedge n)w(x)\\
&=
\sum_{x\in A}f(x)w(x).
\end{aligned}
$$

The last equality is monotone convergence for nonnegative series, equivalently the finite-subsums definition of such a sum. $\square$

## Corollary 6.3 — Integration with Respect to Counting Measure

Let $\#_E$ denote counting measure on $(E,2^E)$. For every $f:E\to[0,+\infty]$ and every $A\subseteq E$,

$$
\boxed{
\int_A f\,d\#_E
=
\sum_{x\in A}f(x)
}.
$$

### Proof

Apply Proposition 6.2 with $w\equiv1$. Then $\mu_w=\#_E$. $\square$

## Proposition 6.4 — Signed Extension

Let $f:E\to\mathbb R$. Then $f$ is integrable on $A$ with respect to $\mu_w$ if and only if

$$
\sum_{x\in A}|f(x)|w(x)<+\infty.
$$

In that case,

$$
\boxed{
\int_A f\,d\mu_w
=
\sum_{x\in A}f(x)w(x)
}.
$$

### Proof

Proposition 6.2 applied to $|f|$ gives

$$
\int_A|f|\,d\mu_w
=
\sum_{x\in A}|f(x)|w(x),
$$

which proves the integrability criterion. Under this condition, the nonnegative series associated with $f^+$ and $f^-$ are both finite. Applying Proposition 6.2 to these two functions and subtracting gives the stated identity. $\square$

## Proposition 6.5 — Canonical Atomic Representation

Let $\mu$ be a positive measure on $(E,2^E)$ and define

$$
w_\mu(x):=\mu(\{x\}),
\qquad x\in E.
$$

Then, for every $A\subseteq E$,

$$
\boxed{
\mu(A)
=
\sum_{x\in A}w_\mu(x)
},
$$

and hence

$$
\mu=\mu_{w_\mu}=w_\mu\,\#_E.
$$

If $\mu$ is $\sigma$-finite, then $w_\mu$ is finite-valued and

$$
\boxed{
w_\mu
=
\frac{d\mu}{d\#_E}
}
$$

pointwise on $E$. In particular, if $\mu$ is a probability measure, then

$$
p(x):=\mu(\{x\})
$$

satisfies $\sum_{x\in E}p(x)=1$, and for every nonnegative $f$,

$$
\int_Ef\,d\mu
=
\sum_{x\in E}f(x)p(x).
$$

Conversely, every function $p:E\to[0,+\infty)$ satisfying

$$
\sum_{x\in E}p(x)=1
$$

defines a probability measure $\mu_p$, and the same integration formula holds.

### Proof

Every $A\subseteq E$ is the at most countable disjoint union

$$
A
=
\bigsqcup_{x\in A}\{x\}.
$$

Countable additivity therefore gives

$$
\mu(A)
=
\sum_{x\in A}\mu(\{x\})
=
\sum_{x\in A}w_\mu(x).
$$

This proves $\mu=\mu_{w_\mu}$. Corollary 6.3 yields

$$
\mu(A)
=
\sum_{x\in A}w_\mu(x)
=
\int_Aw_\mu\,d\#_E,
$$

so $w_\mu$ is a density with respect to $\#_E$. If $\mu$ is $\sigma$-finite, then each singleton is contained in some measurable set of finite $\mu$-measure; hence $w_\mu(x)<+\infty$ for every $x$. Since $\#_E$ is $\sigma$-finite and has no nonempty null set, Radon–Nikodym uniqueness is pointwise. The probability assertions follow by taking $A=E$ and applying Proposition 6.2. The converse follows from Propositions 6.1 and 6.2 with $w=p$. $\square$

## Boundary of the Representation

The power-set structure makes every singleton and every function measurable. Countability has two distinct uses:

1. it provides the finite exhaustion used in Proposition 6.2;
2. it forces every subset to be a countable disjoint union of measurable singletons, which is the decisive step in Proposition 6.5.

On an uncountable space, singleton masses need not determine a measure. In particular, Lebesgue measure on $[0,1]$ vanishes on every singleton but is not the zero measure. Lemma 5 identifies the corresponding failure of the Radon–Nikodym representation with respect to uncountable counting measure.

## Reconstruction

The countable atomic mechanism is

$$
\mu
\longleftrightarrow
\bigl(\mu(\{x\})\bigr)_{x\in E}
\longrightarrow
\mu(A)=\sum_{x\in A}\mu(\{x\})
\longrightarrow
\int_Af\,d\mu
=
\sum_{x\in A}f(x)\mu(\{x\}).
$$

---
type: cours
module: signed-measures
status: canonical
---

# Signed Measures and Hahn–Jordan Decomposition

This module supplies the signed-measure structure used by the Hahn-first proof of the Radon–Nikodym theorem.

## 1. Finite signed measures and Hahn decomposition

### 1.1. Signed measures

A finite signed measure on \((E,\mathcal A)\) is a mapping

$$
\sigma:\mathcal A\longrightarrow\mathbb R
$$

such that

$$
\sigma(\varnothing)=0
$$

and, for every sequence \((A_n)\) of pairwise disjoint measurable sets,

$$
\sum_{n\geq1}|\sigma(A_n)|<\infty
$$

and

$$
\sigma\left(\bigcup_{n\geq1}A_n\right)
=
\sum_{n\geq1}\sigma(A_n).
$$

Every difference of two finite positive measures is a finite signed measure.

In particular, if \(\rho\) and \(\mu\) are finite positive measures and \(c>0\), then

$$
\sigma_c=\rho-c\mu
$$

is a finite signed measure.

---

### 1.2. Positive and negative sets

A measurable set \(P\) is positive for \(\sigma\) if

$$
\sigma(A)\geq0
$$

for every measurable \(A\subseteq P\).

A measurable set \(N\) is negative for \(\sigma\) if

$$
\sigma(A)\leq0
$$

for every measurable \(A\subseteq N\).

A measurable set \(Z\) is \(\sigma\)-null if

$$
\sigma(A)=0
$$

for every measurable \(A\subseteq Z\).

A set which is both positive and negative is \(\sigma\)-null.

---

### 1.3. Hahn decomposition

#### Theorem 1.1 — Hahn decomposition

Let \(\sigma\) be a finite signed measure. There exist disjoint measurable sets \(P,N\) such that

$$
E=P\sqcup N,
$$

where \(P\) is positive and \(N\) is negative for \(\sigma\).

If

$$
E=P'\sqcup N'
$$

is another Hahn decomposition, then

$$
P\triangle P'
$$

and

$$
N\triangle N'
$$

are \(\sigma\)-null.

Thus the sets in a Hahn decomposition are not uniquely determined, but their ambiguity is confined to \(\sigma\)-null sets.

---

### 1.4. Jordan decomposition

Let

$$
E=P\sqcup N
$$

be a Hahn decomposition for \(\sigma\). Define

$$
\sigma^+(A)
=
\sigma(A\cap P)
$$

and

$$
\sigma^-(A)
=
-\sigma(A\cap N).
$$

Then \(\sigma^+\) and \(\sigma^-\) are finite positive measures and

$$
\sigma=\sigma^+-\sigma^-.
$$

They are concentrated on disjoint measurable sets:

$$
\sigma^+(N)=0,
\qquad
\sigma^-(P)=0.
$$

The pair \((\sigma^+,\sigma^-)\) does not depend on the choice of the Hahn decomposition and is characterized by the minimality property

$$
\sigma=\alpha-\beta,
\qquad
\alpha,\beta\geq0
$$

implies

$$
\sigma^+\leq\alpha,
\qquad
\sigma^-\leq\beta.
$$

The decomposition

$$
\sigma=\sigma^+-\sigma^-
$$

is the Jordan decomposition of \(\sigma\).

The positive measure

$$
|\sigma|
=
\sigma^++\sigma^-
$$

is called the total variation of \(\sigma\). No further theory of total variation will be needed here.

If

$$
\sigma(A)=\int_A f\,d\mu
$$

with \(f\in L^1(\mu)\), then

$$
\sigma^+=f^+\cdot\mu,
\qquad
\sigma^-=f^-\cdot\mu,
\qquad
|\sigma|=|f|\cdot\mu.
$$

---

### 1.5. Hahn decomposition and domination

Let \(\rho\) and \(\mu\) be finite positive measures, let \(c>0\), and set

$$
\sigma_c=\rho-c\mu.
$$

Let

$$
E=P_c\sqcup N_c
$$

be a Hahn decomposition for \(\sigma_c\).

#### Proposition 1.2

One has

$$
c\mathbf 1_{P_c}\mu\leq\rho
$$

and

$$
\rho|_{N_c}\leq c\mu|_{N_c}.
$$

#### Proof

For every \(A\in\mathcal A\), the set \(A\cap P_c\) is contained in the positive set \(P_c\). Hence

$$
0
\leq
\sigma_c(A\cap P_c)
=
\rho(A\cap P_c)-c\mu(A\cap P_c).
$$

Therefore

$$
c\mathbf 1_{P_c}\mu(A)
=
c\mu(A\cap P_c)
\leq
\rho(A\cap P_c)
\leq
\rho(A).
$$

Similarly, since \(A\cap N_c\subseteq N_c\),

$$
\sigma_c(A\cap N_c)\leq0.
$$

Thus

$$
\rho(A\cap N_c)
\leq
c\mu(A\cap N_c),
$$

which is precisely

$$
\rho|_{N_c}\leq c\mu|_{N_c}.
$$

---

If, in addition,

$$
\rho\ll\mu,
$$

then

$$
\mu(P_c)=0
\quad\Longleftrightarrow\quad
\rho(P_c)=0.
$$

Indeed,

$$
\mu(P_c)=0
\quad\Longrightarrow\quad
\rho(P_c)=0
$$

by absolute continuity, whereas

$$
\rho(P_c)=0
\quad\Longrightarrow\quad
c\mu(P_c)\leq\rho(P_c)=0
$$

by Proposition 1.2.

The two inequalities in Proposition 1.2 are the local domination statements encoded by the sign of

$$
\rho-c\mu.
$$

---

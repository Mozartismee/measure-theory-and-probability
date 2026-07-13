# Supplement — Signed Construction, Test Functions, and Convergence

Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space and let $\mathcal G\subset\mathcal F$ be a sub-$\sigma$-field.

This supplement isolates the analytic mechanisms required in Exercise 1.2–1.3 of TD 1. Its scope is deliberately restricted to:

1. passing from nonnegative integrable functions to arbitrary elements of $L^1$;
2. uniqueness from integral identities on $\mathcal G$;
3. extending identities from indicators to bounded $\mathcal G$-measurable test functions;
4. selecting the legitimate convergence theorem.

No general theory of $L^p$ spaces or uniform integrability is required.

---

## 1. Positive and signed objects

For a measurable real-valued function $Y$, set

$$
Y^+=\max(Y,0),
\qquad
Y^-=\max(-Y,0).
$$

Then

$$
Y=Y^+-Y^- ,
\qquad
|Y|=Y^++Y^-.
$$

Hence

$$
Y\in L^1(\mathbb P)
\quad\Longleftrightarrow\quad
Y^+,Y^-\in L^1_+(\mathbb P).
$$

More generally, a **positive decomposition** of $Y\in L^1$ is an identity

$$
Y=U-V,
\qquad U,V\in L^1_+(\mathbb P).
$$

Such a decomposition is not unique. The canonical choice $(Y^+,Y^-)$ is distinguished by the disjointness relation

$$
Y^+Y^-=0,
$$

but constructions made from $U-V$ must ultimately depend only on $Y$, not on the chosen pair $(U,V)$.

### Positive RN construction

For $U\in L^1_+(\mathbb P)$, define on $(\Omega,\mathcal G)$

$$
\nu_U(A)=\int_A U\,d\mathbb P,
\qquad A\in\mathcal G.
$$

The positive Radon–Nikodym theorem gives a nonnegative $\mathcal G$-measurable function $R_{\mathcal G}U$ such that

$$
\int_A R_{\mathcal G}U\,d\mathbb P
=
\int_A U\,d\mathbb P,
\qquad A\in\mathcal G.
$$

Taking $A=\Omega$ yields

$$
\|R_{\mathcal G}U\|_1
=
\int R_{\mathcal G}U\,d\mathbb P
=
\int U\,d\mathbb P
=
\|U\|_1.
$$

Thus the RN derivative is not merely measurable: it belongs to $L^1_+(\Omega,\mathcal G,\mathbb P|_{\mathcal G})$.

---

## 2. The uniqueness mechanism

### Lemma — Uniqueness from indicators

Let $U,V\in L^1(\mathbb P)$ be $\mathcal G$-measurable. If

$$
\int_A U\,d\mathbb P
=
\int_A V\,d\mathbb P
\qquad
\text{for every }A\in\mathcal G,
$$

then

$$
U=V
\qquad \mathbb P\text{-almost surely}.
$$

#### Proof

Set $W=U-V$. Since $W$ is $\mathcal G$-measurable,

$$
A_+=\{W>0\},
\qquad
A_-=\{W<0\}
$$

belong to $\mathcal G$. The hypothesis gives

$$
\int_{A_+}W\,d\mathbb P=0.
$$

But $W\mathbf1_{A_+}\ge0$, so $W\mathbf1_{A_+}=0$ almost surely. Hence $\mathbb P(W>0)=0$. Applying the same argument to $-W$ gives $\mathbb P(W<0)=0$. Therefore $W=0$ almost surely. $\square$

### Structural use

The lemma converts a family of scalar identities into equality of random variables. It is the standard closing device for conditional-expectation arguments:

$$
\boxed{
\text{$\mathcal G$-measurability}
+
\text{integrability}
+
\text{identities on all }A\in\mathcal G
\Longrightarrow
\text{a.s. uniqueness}.
}
$$

The choice $A=\{U>V\}$ is legitimate precisely because both candidates are $\mathcal G$-measurable.

---

## 3. Independence of a positive decomposition

Let

$$
Y=U-V,
\qquad U,V\in L^1_+(\mathbb P),
$$

and form the candidate

$$
T_{U,V}=R_{\mathcal G}U-R_{\mathcal G}V.
$$

It is $\mathcal G$-measurable and integrable, since

$$
\|T_{U,V}\|_1
\le
\|R_{\mathcal G}U\|_1+
\|R_{\mathcal G}V\|_1
=
\|U\|_1+
\|V\|_1.
$$

Moreover, for every $A\in\mathcal G$,

$$
\int_A T_{U,V}\,d\mathbb P
=
\int_A(U-V)\,d\mathbb P
=
\int_A Y\,d\mathbb P.
$$

If $Y=U'-V'$ is another positive decomposition, then $T_{U',V'}$ satisfies the same integral identities. The uniqueness lemma therefore gives

$$
T_{U,V}=T_{U',V'}
\qquad\mathbb P\text{-almost surely}.
$$

This is the general pattern:

$$
\boxed{
\text{construct using auxiliary choices}
\;\longrightarrow\;
\text{show the defining identity}
\;\longrightarrow\;
\text{remove the choices by uniqueness}.
}
$$

There is also an algebraic version. Uniqueness implies, for $U,V\in L^1_+$,

$$
R_{\mathcal G}(U+V)
=
R_{\mathcal G}U+R_{\mathcal G}V
\qquad\text{a.s.}
$$

If $U-V=U'-V'$, then $U+V'=U'+V$, and additivity gives the same conclusion after rearrangement.

### Signed-measure interpretation

For $Y\in L^1$, the set function

$$
\nu_Y(A)=\int_A Y\,d\mathbb P,
\qquad A\in\mathcal G,
$$

is a finite signed measure, since

$$
\nu_Y=\nu_{Y^+}-\nu_{Y^-}.
$$

The pair $(\nu_{Y^+},\nu_{Y^-})$ need not be the Jordan decomposition of the restriction to $\mathcal G$; mutual singularity may be lost after information is restricted. Nothing in the construction requires it. What matters is that the resulting signed density is uniquely determined.

---

## 4. The $L^1$–$L^\infty$ pairing

For an essentially bounded random variable $H$, define

$$
\|H\|_\infty
=
\operatorname*{ess\,sup}_{\omega\in\Omega}|H(\omega)|.
$$

Thus $H\in L^\infty$ means that there exists $M<\infty$ such that

$$
|H|\le M
\qquad\mathbb P\text{-almost surely}.
$$

If $H\in L^\infty$ and $Y\in L^1$, then $HY\in L^1$ and

$$
|HY|\le \|H\|_\infty |Y|
\qquad\text{a.s.},
$$

whence

$$
\boxed{
\|HY\|_1
\le
\|H\|_\infty\|Y\|_1.
}
$$

This is the endpoint Hölder inequality. It is the only $L^p$ estimate needed here.

For fixed $Y\in L^1$, the map

$$
\Lambda_Y:L^\infty\longrightarrow\mathbb R,
\qquad
\Lambda_Y(H)=\mathbb E[HY],
$$

is therefore linear and continuous, with

$$
|\Lambda_Y(H)|
\le
\|Y\|_1\|H\|_\infty.
$$

Consequently, if $H_n\to H$ in $L^\infty$, then

$$
\mathbb E[H_nY]\longrightarrow\mathbb E[HY],
$$

because

$$
\left|
\mathbb E[(H_n-H)Y]
\right|
\le
\|H_n-H\|_\infty\|Y\|_1.
$$

This explains the occurrence of $\|\cdot\|_\infty$: it supplies both

1. the integrability of the tested products;
2. a quantitative passage from simple tests to bounded tests.

No general duality theorem $(L^1)^*=L^\infty$ is being used.

---

## 5. Approximation of bounded measurable functions

Let $H$ be bounded and $\mathcal G$-measurable. Then there exists a sequence of $\mathcal G$-measurable simple functions $(H_n)$ such that

$$
\|H_n-H\|_\infty\longrightarrow0.
$$

Indeed, if $|H|\le M$, quantize the range in intervals of length $2^{-n}$. One possible choice is

$$
H_n=2^{-n}\lfloor 2^nH\rfloor.
$$

Since $H$ is bounded, $H_n$ takes only finitely many values, and

$$
0\le H-H_n<2^{-n}.
$$

If $H$ is only essentially bounded, first replace it on a null set by a bounded representative.

### Extension principle

Let $Y,Z\in L^1$. Suppose

$$
\mathbb E[Y\mathbf1_A]
=
\mathbb E[Z\mathbf1_A]
\qquad
\text{for every }A\in\mathcal G.
$$

By linearity, the identity holds for every $\mathcal G$-measurable simple function $S$:

$$
\mathbb E[SY]=\mathbb E[SZ].
$$

Now let $H$ be bounded and $\mathcal G$-measurable, and choose simple $H_n$ with $\|H_n-H\|_\infty\to0$. Then

$$
\begin{aligned}
\left|\mathbb E[HY]-\mathbb E[HZ]\right|
&\le
\left|\mathbb E[(H-H_n)Y]\right|
+
\left|\mathbb E[H_nY]-\mathbb E[H_nZ]\right| \\
&\qquad+
\left|\mathbb E[(H_n-H)Z]\right| \\
&\le
\|H-H_n\|_\infty
\bigl(\|Y\|_1+\|Z\|_1\bigr).
\end{aligned}
$$

The middle term is zero. Letting $n\to\infty$ proves the identity for $H$.

The reverse passage is immediate by taking $H=\mathbf1_A$.

Hence the two testing regimes are equivalent:

$$
\boxed{
\begin{array}{c}
\text{all indicators }\mathbf1_A, A\in\mathcal G
\end{array}
\quad\Longleftrightarrow\quad
\begin{array}{c}
\text{all bounded $\mathcal G$-measurable functions}
\end{array}
}
$$

provided the variables being tested belong to $L^1$.

---

## 6. Why DCT works and MCT does not directly work

Let $H_n\to H$ pointwise, with

$$
|H_n|\le M.
$$

For $Y\in L^1$,

$$
H_nY\to HY
\qquad\text{pointwise},
$$

and

$$
|H_nY|\le M|Y|\in L^1.
$$

The dominated convergence theorem therefore gives

$$
\mathbb E[H_nY]\to\mathbb E[HY].
$$

This is an alternative to the $L^\infty$ estimate above.

The monotone convergence theorem requires a sequence of **nonnegative integrands** increasing pointwise. Even if

$$
0\le H_n\uparrow H,
$$

the sequence $(H_nY)$ need not be nonnegative or increasing when $Y$ changes sign. Thus MCT cannot be applied directly to $H_nY$ for arbitrary $Y\in L^1$.

MCT is legitimate in the special regime

$$
H_n\uparrow H,
\qquad
H_n\ge0,
\qquad
Y\ge0,
$$

because then

$$
H_nY\uparrow HY.
$$

This special case does not settle an identity involving arbitrary signed $Y$ and $Z$. Equality of the signed integrals of $Y$ and $Z$ on sets does not imply separate equality for $Y^+,Y^-$ and $Z^+,Z^-$.

### Selection table

| Available structure                                          | Legitimate mechanism                          |
| ------------------------------------------------------------ | --------------------------------------------- |
| $0\le f_n\uparrow f$                                         | MCT                                           |
| $f_n\to f$ a.s. and $|f_n|\le g\in L^1$                      | DCT                                           |
| $H_n\to H$ in $L^\infty$, $Y\in L^1$                         | $L^1$–$L^\infty$ estimate                     |
| identity known for indicators                                | linearity, then simple-function approximation |
| two $\mathcal G$-measurable $L^1$ candidates have identical set integrals | uniqueness lemma                              |

---

## 7. Two proof architectures to retain

### A. Removing a decomposition choice

Given $Y=U-V$ with $U,V\ge0$:

1. apply the positive construction separately to $U$ and $V$;
2. take the difference of the two RN derivatives;
3. verify $\mathcal G$-measurability and $L^1$-integrability;
4. verify the integral identity on every $A\in\mathcal G$;
5. compare any two decompositions by uniqueness.

### B. Enlarging the class of test objects

Starting from identities for $\mathbf1_A$, $A\in\mathcal G$:

1. pass to finite linear combinations of indicators;

2. approximate a bounded measurable $H$ by simple $H_n$;

3. control the error by

   $$
   \left|\mathbb E[(H-H_n)Y]\right|
   \le
   \|H-H_n\|_\infty\|Y\|_1;
   $$

4. pass to the limit.

These are distinct mechanisms. The first removes auxiliary construction data; the second enlarges a testing class.

---

## Reconstruction standard

Before returning to TD 1, the following should be recoverable without consulting this supplement.

1. Prove the uniqueness lemma using $\{U>V\}$.

2. Explain why $R_{\mathcal G}U-R_{\mathcal G}V$ belongs to $L^1$.

3. Explain why two positive decompositions of the same $Y$ produce the same candidate.

4. Construct simple $H_n$ satisfying $\|H_n-H\|_\infty\to0$ for bounded measurable $H$.

5. Derive

   $$
   \left|\mathbb E[(H_n-H)Y]\right|
   \le
   \|H_n-H\|_\infty\|Y\|_1.
   $$

6. State exactly why MCT fails for $H_nY$ when $Y$ is signed.

If these six points are stable, Exercise 1.2–1.3 requires no further preliminary theory.

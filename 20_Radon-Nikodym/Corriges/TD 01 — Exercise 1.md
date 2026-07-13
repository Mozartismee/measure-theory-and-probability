---
type: corrige
module: radon-nikodym
status: canonical
---

# Corrigé — TD 01, Exercise 1

## Solution

Since \(P_c\) and \(N_c\) are respectively positive and negative sets for \(\sigma_c\), one has

$$
\sigma_c|_{P_c}\ge 0,
\qquad
\sigma_c|_{N_c}\le 0.
$$

Let \(A\in\mathcal A\). Then

$$
0\le \sigma_c(A\cap P_c)
=
\rho(A\cap P_c)-c\mu(A\cap P_c),
$$

hence

$$
c\mu(A\cap P_c)
\le
\rho(A\cap P_c)
\le
\rho(A).
$$

Therefore

$$
c\mathbf 1_{P_c}\mu\le \rho.
$$

Similarly,

$$
0\ge \sigma_c(A\cap N_c)
=
\rho(A\cap N_c)-c\mu(A\cap N_c),
$$

so that

$$
\rho(A\cap N_c)
\le
c\mu(A\cap N_c).
$$

Thus

$$
\rho|_{N_c}\le c\mu|_{N_c}.
$$

Assume now that \(\rho\ll\mu\) and \(\mu(P_c)=0\). Then

$$
\rho(P_c)=0.
$$

Consequently, for every \(A\in\mathcal A\),

$$
\rho(A)
=
\rho(A\cap P_c)+\rho(A\cap N_c)
=
\rho(A\cap N_c)
\le
c\mu(A\cap N_c)
\le
c\mu(A).
$$

Hence

$$
\boxed{\rho\le c\mu}.
$$

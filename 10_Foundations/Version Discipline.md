---
type: foundation
module: foundations
status: canonical
---

# Version Discipline

The following objects live in different spaces:

| Object                       | Space                          | Equality         |
| ---------------------------- | ------------------------------ | ---------------- |
| $d\mathbb P_D/d\mathbb P$    | $L^1(\mathbb P)$               | $\mathbb P$-a.s. |
| $d\mu_D/d\mu_X$              | $L^1(\mu_X)$                   | $\mu_X$-a.e.     |
| $\mathbb E[Y\mid\mathcal G]$ | $L^1(\mathbb P|_{\mathcal G})$ | $\mathbb P$-a.s. |
| $g_Y=d\rho_Y/d\mu_X$         | $L^1(\mu_X)$                   | $\mu_X$-a.e.     |
| $g_Y(X)$                     | $L^1(\mathbb P)$               | $\mathbb P$-a.s. |

The pullback $g\mapsto g(X)$ transports $\mu_X$-versions to $\mathbb P$-versions.

## Transfer principle

The pullback $g\mapsto g(X)$ transports $\mu_X$-versions to $\mathbb P$-versions. It does not identify the ambient spaces; it relates them.

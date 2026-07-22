---
type: study-packet-carnet
cycle: 2026-07-exam-p-first-pass
packet: discrete-laws
start: 2026-07-18
end: 2026-07-24
state: rupture
actual-time:
---

# Carnet — Discrete Laws

## 2026-07-18 — Counting measure and atomic integration

### Object

The attempt concerned two dependent tasks:

1. define counting measure $\#$ on $([0,1],\mathcal B([0,1]))$ and decide its $\sigma$-finiteness;
2. on a countable measurable space $(E,2^E)$, derive from the ordinary construction of the Lebesgue integral that

   $$
   \int_Ap\,d\#_E
   =
   \sum_{x\in A}p(x).
   $$

### First rupture

The first failure occurred before the covering argument: the underlying measurable space had not been separated from the measure chosen on it. Consequently it was not yet clear why the interval $[0,1]$ may carry

$$
\#(A)=\operatorname{card}(A),
\qquad
A\in\mathcal B([0,1]),
$$

with $+\infty$ as a legitimate value. Until the measure itself is fixed, the proof that it is not $\sigma$-finite cannot begin.

### Downstream consequence

The construction indicator $\to$ simple function $\to$ MCT was correctly identified, but singleton indicators had not been connected to counting measure. The passage from finite support to a countable sum therefore remained unavailable, as did the setwise form

$$
\mu(A)=\sum_{x\in A}\mu(\{x\})
$$

of the same atomic representation.

### Diagnosis

No second theory of “discrete integration” is missing. The ordinary integral construction has not yet been transferred to an atomic reference measure. The primary rupture is the measure object; the integral–series identity is its representational consequence. They must be repaired in that order.

### Minimal repair

1. On $([0,1],\mathcal B([0,1]))$, reconstruct counting measure, prove that it is a measure and that it is not $\sigma$-finite, then identify the unavailable RN hypothesis in TD 03, Exercise 0.
2. Compute the counting-measure integral of nonnegative simple functions with finite support.
3. For $A=\{x_1,x_2,\ldots\}$, construct increasing simple approximants and obtain the integral–series identity by MCT.

### Closed-book test

Allow seven minutes for the uncountable counting-measure boundary and eight minutes for the derivation from simple functions and MCT. J1 may move from `rupture` to `reconstructible` only after both arguments are complete.

Complete both tests in the [18 July Séance](../expectation-finite-conditioning/Sessions/2026-07-18/00_Séance.md); no further switching between this Carnet and the canonical Cours or TD is required.

## Session record

| Session | Planned | Actual | State | First rupture | Minimal repair |
| --- | ---: | ---: | --- | --- | --- |
| J1 | 90m |  | rupture | counting measure was not fixed as an object | reconstruct the measure, its $\sigma$-finiteness boundary and the atomic integral |
| J2 | 105m |  | not-attempted |  |  |
| J3 | 120m |  | not-attempted |  |  |
| J4 | 105m |  | not-attempted |  |  |
| J5 | 120m |  | not-attempted |  |  |
| J6 | 120m |  | not-attempted |  |  |
| J7 | 150m |  | not-attempted |  |  |

The only states are `not-attempted`, `rupture`, `reconstructible` and `deployable`. “Difficult” is not a mathematical diagnosis.

## J1 — Atomic representation

- State space and $\sigma$-field：
- Counting measure and $\sigma$-finite cover：
- Atomic density $p$：
- Setwise representation：
- Integral representation：
- Uniqueness basis：
- Uncountable counterexample：
- Missing RN hypothesis：

## J2 — Pushforwards and joint law

- Map and source law for $g(X)$：
- Fibres used：
- Addition map and source joint law：
- Product-law equality used for convolution：
- Same marginals／different sums counterexample：
- Information lost by the pushforward：

## J3 — Replacement

- With-replacement probability space：
- Without-replacement probability space：
- Exact hypergeometric support：
- Off-diagonal covariance：
- Finite-population correction：
- $N=1$ endpoint：
- First place where an independence assumption would change the model：

## J4 — Waiting conventions

| Variable | Construction | Support | pmf | Endpoint or boundary |
| --- | --- | --- | --- | --- |
| $G$ |  |  |  |  |
| $T_r$ |  |  |  |  |
| $T_r-r$ |  |  |  |  |
| $T_r^{(N)}$ |  |  |  |  |

- Count/waiting event identity：
- Why the finite waiting law is not negative binomial：
- $p=0$：
- $p=1$：

## J5 — Poisson mechanisms

- Normalization at $\lambda>0$ and endpoint $\lambda=0$：
- Index shift for $\mathbb E[N]$：
- Index shift for $\mathbb E[(N)_2]$：
- Joint-pmf factorization for splitting：
- Independence used in superposition：
- Conditional allocation given a total：
- What remains if only the two Poisson marginals are known：

## J6 — Restriction and mixture

| Context | Numerator masses | Reference or component law | Normalizer | Resulting object |
| --- | --- | --- | --- | --- |
| conditioning on $X\in A$ |  |  |  |  |
| finite latent mixture |  |  |  |  |
| posterior latent state |  |  |  |  |
| zero-truncated Poisson |  |  |  |  |

- Within-component variance：
- Between-component variance：
- Integrability hypothesis for total variance：
- Why a non-degenerate Poisson mixture is not Poisson：
- Why zero truncation is not a Poisson parameter change：

## Families and conventions

| Family | Construction | Exact support | Mean | Variance | Degenerate endpoint or convention |
| --- | --- | --- | --- | --- | --- |
| Bernoulli |  |  |  |  |  |
| Binomial |  |  |  |  |  |
| Geometric, trial convention |  |  |  |  |  |
| Negative binomial, trial convention |  |  |  |  |  |
| Hypergeometric |  |  |  |  |  |
| Poisson |  |  |  |  |  |
| Uniform on finite $A$ |  |  |  |  |  |

## Operations

| Verbal task | Source measure | Map, restriction or decomposition | Required hypothesis | Output measure or scalar |
| --- | --- | --- | --- | --- |
| transformed payment |  |  |  |  |
| sum of counts |  |  |  |  |
| convolution |  |  |  |  |
| sample without replacement |  |  |  |  |
| condition on a positive-mass event |  |  |  |  |
| latent-class mixture |  |  |  |  |
| nonlinear Poisson payment |  |  |  |  |
| CLT approximation |  |  |  |  |

## Closed-book proofs

| Proof | Closed-book | First missing object or theorem | Repair completed next day |
| --- | --- | --- | --- |
| atomic representation | yes / no |  | yes / no |
| convolution boundary | yes / no |  | yes / no |
| hypergeometric variance | yes / no |  | yes / no |
| Poisson splitting | yes / no |  | yes / no |

## Official paper

| Question | Time | Answer locked | Correct | Structural classification | Error class |
| --- | ---: | --- | --- | --- | --- |
| Q30 | 7m |  |  |  |  |
| Q128 | 7m |  |  |  |  |
| Q146 | 8m |  |  |  |  |
| Q150 | 8m |  |  |  |  |
| Q227 | 8m |  |  |  |  |
| Q246 | 8m |  |  |  |  |
| Q386 | 7m |  |  |  |  |
| Q512 | 7m |  |  |  |  |

Error classes are restricted to: arithmetic, support, construction, independence, replacement, conditioning denominator, moment selection and time.

- Score：__/8
- Structural errors present：yes / no
- Official solutions opened only after all answers were locked：yes / no

## Colle

- Sujet：A / B / C / D / E
- Preparation completed in 15m：yes / no
- Exposition completed in 15m：yes / no
- First relance and answer：
- Second relance and answer：
- First unreconstructible step：

## Deferred work

- [ ] mastery-extension official anchors Q149、Q243、Q314、Q382
- [ ] 60-minute closed-book reconstruction
- [ ] quantitative CLT error bounds
- [ ] generating-function methods
- [ ] general conditional kernels on null fibres

A checked box records an explicit deferral; it does not record completion.

## Verdict

- **Cycle state**：rupture / reconstructible / deployable
- **Total actual time**：
- **Four core proofs recovered without notes**：yes / no
- **Six required families constructed before being named**：yes / no
- **Operations located on the correct measures**：yes / no
- **Official audit at least 7/8**：yes / no
- **No structural error in the official audit**：yes / no
- **Colle plus two relances completed**：yes / no
- **First remaining non-deferred rupture**：
- **Minimal valid repair**：

Mark the cycle `deployable` only when every criterion holds and no non-deferred rupture remains. “Not yet familiar” is not a diagnosis: identify the missing object, hypothesis, representation, theorem or convention.

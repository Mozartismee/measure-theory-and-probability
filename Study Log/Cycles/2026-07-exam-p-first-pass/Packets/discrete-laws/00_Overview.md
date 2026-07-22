---
type: study-packet-overview
cycle: 2026-07-exam-p-first-pass
packet: discrete-laws
start: 2026-07-18
end: 2026-07-24
sessions: 7
planned-time: 810m
math-authority: derived
canonical-sources:
  - ../../../../../30_Pushforwards-and-Laws/01_Cours/Cours 02 — Atomic Laws and Discrete Distribution Structures.md
  - ../../../../../30_Pushforwards-and-Laws/02_TD/TD 03 — Atomic Laws, Counting Models, and Structural Failures.md
  - ../../../../../30_Pushforwards-and-Laws/05_Example-Sheets/Example Sheet 01 — Exam P Discrete Distribution Deployment.md
---

# Discrete Laws — One-Week Cycle

This seven-session cycle runs independently of the July measure-theory programme. The [canonical Cours](../../../../../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md) constructs atomic laws, pushforwards, product laws, convolution, the classical discrete families, restriction and mixture. The [canonical TD](../../../../../30_Pushforwards-and-Laws/02_TD/TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md) carries the substantial proof responsibility. This module fixes the order of work, the closed-book demands and the final Exam P transfer.

The governing chain is

$$
\text{atomic measure}
\longrightarrow
\text{pushforward and fibres}
\longrightarrow
\text{joint law and convolution}
\longrightarrow
\text{classical constructions}
\longrightarrow
\text{conditioning and mixture}
\longrightarrow
\text{Exam P deployment}.
$$

## Aim and scope

- **Objects.** Countable probability laws, counting-measure densities, joint atomic laws, convolution, sampling models, waiting times, Poisson mechanisms, restrictions and mixtures.
- **Standard.** ENS L3 fin / M1 début: exact hypotheses, counterexamples and reconstruction before calculation speed.
- **Output.** Seven written attempts, one [Carnet](03_Carnet.md), one Colle and one sixty-minute official audit.
- **Time.** $810$ minutes, or $13$ hours $30$ minutes.
- **Boundary.** No generating functions or MGF. The CLT appears only as a terminal approximation boundary; weak convergence is not reconstructed here.

## J1 — Atomic law, 90 minutes

1. **15m.** Complete the Entry Gate in the [Feuille](02_Feuille%20de%20travail.md), closed book.
2. **30m.** Read [Preparatory Notes](01_Preparatory%20Notes.md), J1, and the canonical Cours §§1–3.
3. **35m.** Attempt TD 03, Exercises 0–1. Preserve the first illegitimate step if the proof breaks.
4. **10m.** Record the domain of counting measure, its $\sigma$-finiteness, the RN uniqueness basis and the uncountable failure.

At the end, prove without notes

$$
\mu=p\#_E,
\qquad
p(x)=\mu(\{x\}),
\qquad
\int_E\varphi\,d\mu=\sum_{x\in E}\varphi(x)p(x),
$$

and explain why $\lambda\ll\#$ on an uncountable space does not yield an RN density.

## J2 — Pushforward and joint law, 105 minutes

1. **20m.** Preparatory Notes J2; canonical Cours §§4–5.
2. **60m.** TD 03, Exercises 2–3.
3. **15m.** Feuille, Exercise A; reconstruct two equal-marginal models with different sum laws.
4. **10m.** Record separately the fibre pushforward, the addition pushforward and the hypothesis needed for convolution.

Recover

$$
p_{g(X)}(y)=\sum_{x\in g^{-1}(\{y\})}p_X(x),
\qquad
p_{X+Y}(n)=\sum_kp_{X,Y}(k,n-k).
$$

The second identity becomes convolution only after $p_{X,Y}=p_Xp_Y$ has been justified.

## J3 — Replacement, 120 minutes

1. **25m.** Preparatory Notes J3; canonical Cours §§6.1, 6.4, 6.5.
2. **70m.** TD 03, Exercise 4.
3. **15m.** Feuille, Exercise B.
4. **10m.** Record support, construction, covariance and endpoints.

Construct the binomial law from a product Bernoulli measure and the hypergeometric law from the uniform law on finite samples. Derive, rather than append,

$$
\frac{N-n}{N-1}.
$$

## J4 — Waiting laws, 105 minutes

1. **20m.** Preparatory Notes J4; canonical Cours §6.3.
2. **60m.** TD 03, Exercise 5.
3. **15m.** Feuille, Exercise C.
4. **10m.** Record support before the pmf; separate trial, failure and finite-population conventions.

Recover

$$
\{T_r\le n\}
=
\left\{\sum_{j=1}^nB_j\ge r\right\},
$$

and explain why a finite waiting position is not negative binomial merely because its numerator contains binomial coefficients.

## J5 — Poisson mechanisms, 120 minutes

1. **25m.** Preparatory Notes J5; canonical Cours §6.2.
2. **70m.** TD 03, Exercise 6.
3. **15m.** Feuille, Exercise D; consult the Example Sheet only after the calculation.
4. **10m.** Locate the exact uses of independence in superposition, splitting and conditional allocation.

Derive by index shift

$$
\mathbb E[N]=\lambda,
\qquad
\mathbb E[(N)_2]=\lambda^2,
$$

then prove splitting by factorising the joint pmf. A slogan about Poisson addition is neither a proof nor, without independence, the right model.

## J6 — Mixture, truncation and Bayes, 120 minutes

1. **20m.** Preparatory Notes J6; canonical Cours §7.
2. **65m.** TD 03, Exercise 7.
3. **20m.** Feuille, Exercise E.
4. **15m.** Separate mixture, restriction, normalisation and posterior reversal. Prove every denominator positive before dividing.

For $N\mid\Lambda\sim\operatorname{Pois}(\Lambda)$ with $\Lambda\in L^2$, recover

$$
\operatorname{Var}(N)
=
\mathbb E[\Lambda]+\operatorname{Var}(\Lambda),
$$

and use it to reject false Poisson closure. Derive the zero-truncated law as a normalised restriction.

## J7 — Integrated deployment, 150 minutes

1. **45m.** TD 03, Exercise 8.
2. **30m.** Choose one Colle sujet: 15 minutes of preparation, 15 minutes of exposition, at least two relances.
3. **60m.** Complete Q30, Q128, Q146, Q150, Q227, Q246, Q386 and Q512 under the times below. Do not write family names beside the questions in advance.
4. **15m.** Complete the Carnet and enter the final verdict.

Reconstruct without interruption

$$
\text{latent class}
\to
\text{conditional Poisson count}
\to
\text{independent thinning}
\to
\text{mixture}
\to
\text{nonlinear payment}.
$$

## Official audit

| Question | Time | Structural object |
| --- | ---: | --- |
| Q30 | 7m | fixed independent Bernoulli trials |
| Q128 | 7m | hypergeometric count |
| Q146 | 8m | finite-horizon negative-binomial event with conditioning |
| Q150 | 8m | discrete-uniform conditional mixture |
| Q227 | 8m | Poisson mixture variance |
| Q246 | 8m | independent Poisson components conditioned on a total |
| Q386 | 7m | nonlinear Poisson factorial moment |
| Q512 | 7m | second moment versus squared mean |

Mastery extensions Q149, Q243, Q314 and Q382 do not count towards the present $810$ minutes. Question numbers are snapshot anchors; the structure of the problem remains authoritative.

## Working rule

The canonical TD corrigé is not reading material. Open the relevant section only after a complete written attempt. The module [Corrigé](04_Corrigé.md) covers only the Entry Gate and Exercises A–E; it does not duplicate the canonical TD solutions. On correction, locate the first false step, close the solution, and reconstruct the decisive argument the following day. Official sample solutions remain closed until all eight answers have been locked.

## Criterion

The cycle is `deployable` only if the student can:

1. prove the atomic representation, convolution boundary, hypergeometric variance and Poisson splitting without notes;
2. construct the Bernoulli, binomial, geometric, negative-binomial, hypergeometric, Poisson and finite-uniform laws before naming them;
3. locate every pushforward, sum, conditioning, mixture and truncation operation on its source measure and state the required hypotheses;
4. score at least $7/8$ on the official audit with no structural error involving independence, replacement, support or conditioning;
5. complete a fifteen-minute Colle exposition and answer two boundary relances.

Arithmetic errors return to the Example Sheet. Errors of family, support or parameter convention return to Cours §6. Errors of independence, replacement, mixture or conditioning return to the corresponding TD construction. Repetition of a familiar multiple-choice pattern is not a repair.

## References

- [Atomic Laws Cours](../../../../../30_Pushforwards-and-Laws/01_Cours/Cours%2002%20—%20Atomic%20Laws%20and%20Discrete%20Distribution%20Structures.md)
- [TD 03 — Atomic Laws, Counting Models, and Structural Failures](../../../../../30_Pushforwards-and-Laws/02_TD/TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md)
- [Corrigé TD 03](../../../../../30_Pushforwards-and-Laws/03_Corriges/Corrigé%20TD%2003%20—%20Atomic%20Laws,%20Counting%20Models,%20and%20Structural%20Failures.md)
- [Colle 01 — Discrete Laws and Structural Diagnosis](../../../../../30_Pushforwards-and-Laws/04_Colles/Colle%2001%20—%20Discrete%20Laws%20and%20Structural%20Diagnosis.md)
- [Example Sheet 01 — Exam P Discrete Distribution Deployment](../../../../../30_Pushforwards-and-Laws/05_Example-Sheets/Example%20Sheet%2001%20—%20Exam%20P%20Discrete%20Distribution%20Deployment.md)
- [Discrete Distributions — One-Week Deployment Route](../../../../../60_Applications/Exam-P-Bridges/Discrete%20Distributions%20—%20One-Week%20Deployment%20Route.md)
- [SOA Exam P Sample Questions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-quest.pdf), [Sample Solutions](https://www.soa.org/globalassets/assets/Files/Edu/edu-exam-p-sample-sol.pdf), and [July 2026 syllabus](https://www.soa.org/globalassets/assets/files/edu/2026/july/syllabi/2026-07-p-syllabus.pdf)

## Polycopiés

- [Student handout](Polycopiés/Student%20Handout.pdf)
- [Independent Corrigé](Polycopiés/Independent%20Corrigé.pdf)

# ENS corpus calibration protocol

Use this protocol to convert a small number of source documents into a production brief. Do not use it as a source inventory or a replacement for `PROJECT_SPEC.md`, Module Maps, canonical Cours, Bibliography, or source indexes.

## Define structural pathology

Treat pathology as a controlled test of mathematical structure:

- identify the hypothesis that licenses a conclusion;
- preserve the other hypotheses while removing or weakening that one;
- exhibit the failure mechanism, endpoint, counterexample, or loss of identification;
- connect the failure to the representation or dependency chain used in the valid regime.

Reject missing hypotheses, unexplained notation, machinery beyond the legal frontier, long computation, and obscure tricks as substitutes for depth. French headings and institutional typography carry no mathematical weight.

## Assign source roles

Choose sources by function, not prestige.

| Role | Prefer | Extract | Reject |
| --- | --- | --- | --- |
| Theory architecture | Cours or theorem-centered notes | object order, hypotheses, representation, proof density, endpoints | later theory not consumed by the artifact |
| Exercise morphology | TD with its Corrige, DM, or corrected feuille | student moves, dependency edges, subquestion cuts, indication and solution density | statement copying without a role analysis |
| Independent calibration | annale or another ENS campus | timed synthesis, cross-instructor stability, correction compression | treating an examination as ordinary TD density |

Read a corrigé to audit morphology and proof density, but preserve the learner's closed-book attempt boundary in the generated artifact.

## Extract stable features

Recover the pair

$$
(\text{available theory},\text{new deployment}).
$$

Then inspect:

- whether the source requires theorem recognition, an intermediate construction, a representation choice, quantifier control, endpoint analysis, or transfer between analytic and probabilistic languages;
- whether subquestions coincide with a genuine change of object, theorem, representation, or reduction;
- whether an earlier object or result materially enables a later exercise;
- which hypothesis is isolated by each counterexample or failure case;
- whether an indication names at most one bottleneck object, theorem, or reduction;
- whether the Corrige exposes the decisive move while retaining theorem hypotheses, limiting arguments, reference measures, exceptional sets, and endpoints.

Do not force a dependency edge between genuinely independent competencies. Do not split a proof until theorem selection and construction disappear from the student's responsibility.

## Calibrate the level

- At `L3+`, require reliable theorem recognition, hypothesis control, a standard construction, a boundary example, and at least one nontrivial transfer from an explicit cours frontier.
- At `M1`, increase autonomy and synthesis rather than length. Require combined modules, an unsupplied representation or intermediate object, and control of endpoints or exceptional sets.
- Above `M1`, admit research folklore, advanced functional analysis, delicate set theory, or obscure counterexamples only with explicit scope authority or as a separable complement.

Use partiels and examinations for time pressure and closed-book synthesis. Use statistics sources to preserve the experiment, parameter, domination, likelihood, estimator or test, loss, and risk before calculation. Their presence does not expand the current Exam P route.

## Write the brief

Use this schema in turn context:

```text
Artifact:
Regime:
Legal cours frontier:

Selected source unit 1:
- Exact local source:
- Institution / academic year / document role:
- Why selected:
- Calibrates:
- Reject from import:
- Attribution type:

Selected source unit 2:
...

Optional source unit 3:
...

Portable architecture:
Student responsibility and dependency chain:
Structural pathology:
Indication / Corrige density:
Concrete changes to the production brief:
Explicit exclusions:
```

State concrete changes as operations: add a construction step, remove a supplied representation, move a counterexample before a theorem, split existence from uniqueness, preserve one endpoint check, reduce an indication, or exclude a later theory. Avoid adjectives such as “rigorous” or “ENS-like” without an observable responsibility change.

## Classify attribution

- `adapted`: retain the recognizable mathematical core of one numbered source exercise while changing notation, hypotheses, ordering, or deployment.
- `combined`: fuse substantial mechanisms from two or more exactly identified source exercises.
- `inspired`: borrow a motif, pathology, or responsibility pattern while constructing a materially new statement and route.
- `independently reconstructed`: derive the artifact from canonical mathematics; use the corpus only to test level, density, or morphology.

For `adapted` and `combined`, cite every exact PDF and printed exercise number in the artifact. For `inspired`, cite the source in the artifact when a particular exercise remains recognizable; otherwise report it in the delivery summary. For `independently reconstructed`, report the calibration sources only in the delivery summary unless the user requests fuller provenance.

Compute every portable Markdown link from the final artifact's directory. Do not paste a vault-root path or a link copied from an index at a different directory depth.

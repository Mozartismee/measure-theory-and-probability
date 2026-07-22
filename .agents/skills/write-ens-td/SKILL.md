---
name: write-ens-td
description: Design or substantially revise ENS-level measure-theory TD, mini-TD, exercise sheets, DM, assessments, and authorized Corriges in this vault. Use when the user asks to create a new TD, rebuild an exercise progression, change structural difficulty or student responsibility, design a formal assessment, or produce a complete canonical Corrige. Do not use for review-only requests, isolated exercise solutions, Cours writing, Example Sheets, or mechanical repository validation.
---

# Write ENS Measure-Theory TD

## Establish the legal frontier

1. Complete the repository cold start required by `AGENTS.md`.
2. Follow `.agents/ROUTING.md`. Read `00_Project/PROJECT_SPEC.md`, the target module's `00_Module Map.md`, the relevant canonical Cours, and the existing TD or Corrige when revising one.
3. Read `00_Project/Unit Structure.md` if the requested artifact may actually be a Colle, Example Sheet, Supplement, or assessment rather than a TD.
4. Use `$calibrate-with-ens-corpus` before drafting a new full TD, complete Corrige, DM, assessment, direct ENS exercise adaptation, explicit L3/M1 calibration, or response to a disputed claim about ENS resemblance. Consume its in-turn brief. Do not scan the corpus for a local exercise repair or isolated solution.

Treat existing uncommitted work as the user's baseline. Do not import project state from the corpus, source indexes, or calibration brief, and do not duplicate canonical module content inside the Skill.

## Fix the TD brief

Recover internally:

- the available definitions and theorems, including results not yet legal to invoke;
- the terminal constructions, representations, transfers, or failure boundaries;
- one or more generating objects that can create real reuse across exercises;
- the intended level, session regime, time budget, and output extent;
- the requested artifact set and whether hints or Corriges are authorized;
- the source relationship and exact attribution required for every adapted or combined exercise.

Only ask when the missing answer would change the cours frontier, central construction, or document scope. A local learner rupture may lower entry cost, but it does not lower the terminal mathematical responsibility.

## Construct the exercise graph

Design from terminal targets backward. Use the project progression

$$
\text{rupture}\to\text{construction}\to\text{representation}
\to\text{transfer}\to\text{failure}
$$

as the default spine, not as a cosmetic five-part template. Omit a stage only when the scope or Module Map makes it unnecessary.

Assign each exercise a determinate function:

- `entry`: verify that a cours tool can be deployed without consuming the main insight;
- `bridge`: construct a reusable object, estimate, decomposition, or lemma;
- `core`: leave theorem selection, representation, or construction to the student;
- `transfer`: move the same structure to a genuinely different language or setting;
- `boundary`: isolate the role of a hypothesis, endpoint, or inverse claim;
- `extension`: place optional work outside the timed core.

For each dependency edge, identify the exact earlier object or result used later. Reject decorative edges. Independent exercises are legitimate only when they test different competencies within the declared scope.

## Allocate student responsibility

For every statement, recover

$$
(O,H,T,M),
$$

where $O$ is the object, $H$ the hypotheses, $T$ the exact target, and $M$ the mathematical move left to the student.

Require a real move at the intended level: choose a representation, construct an intermediate object, recognize a theorem and verify its hypotheses, control quantifiers or exceptional sets, design a counterexample, or transfer a prior result. Split subquestions only at genuine changes of object, representation, theorem, or reduction. Do not turn a proof into symbolic navigation.

Use sparse indications. An indication may name one bottleneck object, theorem, or reduction, but not the whole route. Difficulty must come from structural choice and synthesis, not missing hypotheses, unexplained notation, computation length, or machinery beyond the cours frontier.

## Solve before committing the statements

Build an internal proof skeleton for every exercise and verify:

- the target is true and exact;
- every expression is well-defined;
- measurability, integrability, finiteness, sigma-finiteness, topology, endpoints, and exceptional sets are controlled;
- each theorem is legal at the cours frontier or established earlier in the sheet;
- every counterexample retains all hypotheses not being removed;
- later exercises can actually use the claimed dependencies;
- the timed core is feasible at the declared level.

Repair the statement when the proof exposes a missing assumption. Never hide a new hypothesis in the Corrige.

## Write the TD and Corrige

Formal TD and Corrige text defaults to English. Use terse, complete commands and portable Markdown with dollar-sign LaTeX. Do not add learning objectives, strategy prose, difficulty labels, or design commentary unless requested.

Produce a Corrige only when the user authorizes it and the active Study Log reading boundary permits it. For canonical module construction, it may be stored as a separate formal file, but do not direct the learner to open it before a complete written attempt.

For every adapted or combined exercise, record the exact PDF, printed exercise number, and attribution type in the artifact. Use the calibration brief only for morphology when the exercise is independently reconstructed.

In the Corrige, expose the decisive construction, representation, or estimate early; verify material theorem hypotheses at the point of use; separate existence from uniqueness; and retain limit exchanges, almost-everywhere bases, constants, and counterexample checks. Compress routine legal modules without turning the solution into a second Cours.

## Verify and reconcile

1. Rebuild the exercise graph from the finished statements and confirm every claimed edge.
2. Compare each Corrige question-by-question with the statement.
3. Use `$audit-measure-theory-notes` for the mathematical review pass rather than duplicating its repair protocol here.
4. Use `$validate-measure-theory-vault` when files, links, indexes, paths, or mirrors changed.
5. Run `git diff --check`, inspect the task-owned diff, update canonical module status only when completion facts changed, and perform meta reconciliation.

Deliver only the requested artifacts plus the concise verification result. ENS level must remain visible after institutional labels and French ornament are removed.

---
name: write-ens-math-notes
description: Create or substantially revise canonical ENS-level measure-theory Cours, theorem notes, reconstruction notes, or scoped supplements in this vault. Use when the user asks to write a formal lecture note or chapter, reconstruct a topic from its prerequisites, or turn an approved module gap into deployable mathematical material. Do not use for source-to-`80_Lemmas` candidate selection or promotion, TD or Corrige production, review-only requests, a single calculation or proof check, Study Log packets, or repository-link validation.
---

# Write ENS Measure-Theory Notes

## Recover the production contract

1. Complete the repository cold start required by `AGENTS.md`.
2. Follow `.agents/ROUTING.md`. Read `00_Project/PROJECT_SPEC.md`, the target module's `00_Module Map.md`, and the target file when it exists.
3. Read `00_Project/Dependency Map.md` only for cross-module dependencies. Read `00_Project/Unit Structure.md` when the file role is uncertain.
4. Use `$calibrate-with-ens-corpus` before drafting a new Cours, making a substantial structural rewrite, choosing a proof architecture from sources, or answering an explicit ENS-level calibration request. Consume its in-turn brief; do not scan the corpus for a local correction.
5. Treat the user's current instruction and supplied sources as higher-priority constraints. Preserve unrelated uncommitted work.

Do not copy project truth into this Skill. Resolve scope, level, notation, language, canonical status, and completion from the current canonical files each time.

## Fix a mathematical brief

Before drafting, recover internally:

- the mathematical object and governing structures;
- the document role and intended deployment;
- the operative regime, including prerequisite and Exam P boundaries;
- the admissible output, including path, format, language, and requested extent;
- the legal cours frontier and direct dependencies;
- the terminal theorem, representation, or reconstruction the note must support.

Ask only if a missing choice would change the theory level, canonical location, or output scope. Otherwise use the narrowest interpretation consistent with the Module Map.

## Build the note from mathematical necessity

Choose the shortest architecture that exposes the actual dependency. Typical components are:

1. an obstruction or precise problem;
2. the canonical objects and definitions;
3. the construction or representation mechanism;
4. the principal theorem and proof architecture;
5. consequences that will actually be deployed;
6. the boundary of validity and a decisive failure mechanism.

Do not turn this list into mandatory headings. Combine components that share one proof mechanism, and omit sections without mathematical work.

For a `Cours`, produce the minimal deployable theory rather than a survey. Route source-to-`80_Lemmas` candidate selection, promotion, dependency integration, and numbering work to `$promote-reusable-measure-theory-lemma`; do not duplicate that workflow here. Keep a `Supplement` local to a genuine prerequisite rupture; if it carries a core theorem, route the content back to the Cours or another canonical module.

## Maintain legitimacy while writing

- Define objects, maps, domains, codomains, structures, and reference measures wherever omission would change meaning.
- State every material hypothesis and identify where it enters the argument.
- Separate existence, uniqueness, representation, positivity, integrability, finite and sigma-finite regimes, signed extensions, and almost-everywhere identification.
- Track measurability, well-definedness, integrability, exceptional sets, convergence modes, endpoints, and representative choices.
- When invoking a theorem, match its hypotheses to the present objects before taking the conclusion.
- Expand new constructions, nontrivial estimates, representation steps, and limit exchanges. Compress only standard modules already legal at the cours frontier.
- Distinguish formal proof, proof architecture, and intuition. Do not let heuristic language carry a theorem.
- State the nearest failure when a decisive hypothesis is removed. Do not add decorative counterexamples.

Formal Cours and academic theorem material default to English. Operational commentary remains Traditional Chinese. Use portable Markdown and dollar-sign LaTeX, following the repository link rules in `AGENTS.md`.

## Preserve canonical boundaries

Keep one current source of truth for each mathematical claim. Link to an existing canonical theorem instead of reproducing it unless the new file must contain a self-contained proof by role. Do not alter mastery, rupture, or active-cycle state merely because material was generated; those files require learning evidence, not project output.

Update the Module Map or another canonical project file only when scope, dependency, competency, status, or completion facts actually change.

## Verify before delivery

1. Reconstruct the principal result from the written definitions, hypotheses, and decisive proof steps.
2. Check theorem applicability, measurability, integrability, almost-everywhere bases, endpoints, and dependency order.
3. Use `$audit-measure-theory-notes` for an independent mathematical pass after substantial generation or revision.
4. Use `$validate-measure-theory-vault` when links, indexes, paths, filenames, or mirrors changed.
5. Run `git diff --check`, inspect only the task-owned diff, and perform the required meta reconciliation.

Deliver the created or revised artifact, the verification result, and any boundary that remains unresolved. Do not pad the handoff with a duplicate summary of canonical content.

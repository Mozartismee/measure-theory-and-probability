---
name: promote-reusable-measure-theory-lemma
description: Assess, select, and when authorized promote a source result into the canonical `80_Lemmas` registry in this measure-theory vault. Use when the user asks which key lemma or representation should be extracted from a séance, Cours, TD, proof, or passage; asks to align the choice with current learner state, Exam P deployment, or a functional-analytic lens; asks to create and index the lemma; or requests lemma dependency, compatibility, numbering, or registry-migration work. Do not use for ordinary Cours or theorem-note writing, local explanations, isolated proof checks, example-pair work, or Study Log mastery updates.
---

# Promote a Reusable Measure-Theory Lemma

Treat promotion as a canonicalization decision, not as automatic summarization. Permit the conclusion that no standalone lemma should be created.

## Recover the live contract

1. Complete the cold start required by `AGENTS.md` and follow `.agents/ROUTING.md`.
2. Read the source, its Module Map, the unique Markdown file with frontmatter `type: lemma-index`, and only the canonical dependencies needed to test the candidate.
3. Locate existing lemmas and direct consumers with targeted searches. Preserve unrelated uncommitted work and the current index filename.
4. When the choice must reflect the learner's present level, read `Study Log/State/CURRENT.md` and only the relevant entries in `MASTERY.md` and `RUPTURES.md`. Treat missing mastery evidence as absence of verification, not proof of ignorance. Respect active scope locks unless the user's current instruction explicitly overrides them.
5. Follow `canonical-sources` from derived Study Log material before deciding mathematical truth. Do not open a protected Corrigé unless the task authorizes it.
6. Recover the requested deployment lens. If none is stated, prefer the current mathematical bottleneck and project main line over the most advanced available formulation.

Do not copy live project state into this Skill. Resolve scope, numbering, notation, learner state, and the active index from canonical files on every run.

## Select the operating mode

- **Assessment**: When the user asks whether or what to extract, inspect and report only. Do not edit files.
- **Promotion**: When the user asks to extract, store, create, implement, or add the result to `80_Lemmas`, create the canonical note and integrate it.
- **Migration**: Only when the user explicitly asks to renumber or restructure the registry, perform a full impact analysis and one coherent migration.

If intent is mixed, preserve the least expansive authorized mode. A request to review a candidate does not authorize promotion.

## Gate the candidate

Require every promoted candidate to satisfy all of the following:

1. **Cross-module deployment**: the result or proof mechanism has independent use in more than one module.
2. **Standalone reconstruction**: the statement, decisive proof chain, hypotheses, and nearest failure boundary fit in a finite note without reopening an entire Cours.
3. **Canonical distinctness**: no existing lemma or canonical Cours already owns the same mathematical object at the same level of generality.
4. **Legal role**: the candidate is not merely an example, local calculation, synonymous restatement, unfinished argument, or bundle of loosely related theorems.
5. **Stable interface**: its notation, reference measure, almost-everywhere basis, endpoint regime, and prerequisites can be made explicit without importing an unapproved theory expansion.

Reject the promotion when any gate fails. Route a reusable legal-regime/failure pair to `85_Examples-and-Counterexamples`; keep a single-module proposition in its module; route a broader theory spine to its Cours.

## Choose one dominant abstraction

After gating, compare candidates by:

- reconstructive leverage;
- cross-module reuse;
- fit with the learner's currently usable interfaces;
- fit with the requested deployment lens;
- clarity of the theorem boundary;
- duplication and maintenance cost.

Choose one dominant object and one independently recoverable proof mechanism. Give concise rejection reasons for genuinely competing candidates; do not manufacture equal alternatives.

For an Exam P lens, let terminal deployment select the useful interface without changing the canonical theorem architecture. For a functional-analytic lens, raise the weight of operator, duality, or projection representations only when the user requests that lens and the prerequisites are legal. Do not silently expand the bounded Exam P line into full Banach-space or $L^2$ theory.

## Report an assessment

Return:

1. the selected mathematical object or `do not promote`;
2. the decisive representation and proof mechanism;
3. the direct prerequisites and expected consumers;
4. the nearest validity boundary;
5. why the choice fits the learner state and requested lens;
6. the correct canonical destination.

Stop without editing in Assessment mode.

## Promote the result

1. Run `python3 .agents/skills/promote-reusable-measure-theory-lemma/scripts/inspect_lemma_registry.py --root .` before choosing a number.
2. Use the next unused positive integer by default. Treat existing lemma numbers as stable citation identifiers; do not insert, recycle, or reorder them for thematic neatness.
3. Create one English canonical note. Include the necessary framework, complete statement, reconstructible proof, actual deployments, nearest failure boundary, and reconstruction line. Combine sections when they perform no distinct mathematical work.
4. State where every decisive hypothesis enters. Check measurability, well-definedness, integrability, exceptional-set basis, endpoints, finite versus sigma-finite regimes, and representative choices as applicable.
5. Distinguish proof prerequisites, downstream consumers, and related boundary references. Link each according to its real role; do not infer a proof dependency from mere thematic proximity.
6. Update the active lemma index with matching number, title, and relative encoded path. Add or replace module references only where the new lemma becomes the unique canonical proof owner.
7. Leave the source unchanged unless the user also asked to revise it. Never update `MASTERY.md`, remove a rupture, or create learner evidence merely because a lemma was written.

## Check semantic compatibility

Read only the candidate's direct linked lemmas and direct consumers, then verify:

- no existing lemma subsumes or contradicts the new statement;
- no proof depends, directly or indirectly, on its own conclusion;
- local notation and reference measures agree or are translated explicitly;
- invoked lemmas are legal at the proof frontier;
- cross-references marked as boundaries or deployments are not mistaken for prerequisites;
- the new canonical ownership does not leave a second maintained proof unintentionally.

Use `$audit-measure-theory-notes` for the final mathematical pass. The registry inspector reports links; it does not classify their semantics.

## Migrate numbering only on explicit request

1. Run the registry inspector and retain its complete internal-link and backlink report.
2. Define a total old-to-new mapping before editing. Reject duplicate destinations and do not reuse an identifier that still has live citations.
3. Search headings, substatement numbers, prose citations, links, index entries, and downstream module references.
4. Apply the mapping in one coherent change and rerun the inspector.
5. Use full-vault validation after any numbering or registry-structure migration.

Do not provide an automatic renumbering script. Number changes require semantic review of prose and proof references.

## Use the registry inspector

Run from the repository root:

```bash
python3 .agents/skills/promote-reusable-measure-theory-lemma/scripts/inspect_lemma_registry.py --root .
```

The script locates the canonical index by frontmatter, checks number and index consistency, and reports intra-lemma links and repository backlinks. Treat a zero exit status as registry consistency, not mathematical correctness.

## Verify and reconcile

1. Reconstruct the promoted lemma from its definitions, hypotheses, and decisive steps.
2. Run the registry inspector again.
3. Use `$validate-measure-theory-vault`; use changed scope for ordinary promotion and all scope for numbering, index-path, or registry-structure migrations.
4. Run `git diff --check` and manually inspect changed LaTeX commands and literal TABs.
5. Inspect only the task-owned diff and perform the meta reconciliation required by `AGENTS.md`.

Deliver the selection decision, files changed when applicable, dependency and compatibility result, validation result, and any remaining boundary. Do not duplicate the canonical lemma in the handoff.

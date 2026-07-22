---
name: audit-measure-theory-notes
description: Audit or minimally repair Markdown notes in this measure-theory vault. Use for strict mathematical or ENS review, theorem-boundary and hypothesis checks, notation consistency, dependency-order checks, mirrored-copy verification, or requests to fix only genuine defects while leaving sound pedagogy and prose unchanged.
---

# Audit Measure-Theory Notes

## Establish the admissible scope

1. Read `AGENTS.md`, inspect Git status, and read `.agents/HANDOFF.md` before judging the note.
2. Follow `.agents/ROUTING.md`. For a module task, read the target file and its `00_Module Map.md` before editing.
3. Read only the canonical files needed to test the claim. Use `00_Project/PROJECT_SPEC.md` for generation and review standards; use the relevant Module Map, dependency map, bibliography, or source only when the issue depends on it.
4. Treat existing uncommitted work as the user's baseline. Do not restore, rewrite, or attribute unrelated changes.
5. Distinguish review from repair. Inspect and report for review-only requests; edit locally only when the request authorizes correction.

## Classify the suspected rupture

Classify each finding as exactly one of:

1. mathematical or logical error;
2. missing hypothesis, domain restriction, quantifier, endpoint, or boundary condition;
3. notation, type, representation, dependency-order, or interface mismatch that changes meaning;
4. stylistic or pedagogical preference.

Correct classes 1--3. Leave class 4 unchanged unless the user explicitly requests stylistic revision or it creates a genuine usability defect.

Use the smallest local context that can falsify the suspected issue. In particular:

- compare compressed review claims with their canonical theorem statements;
- separate well-definedness, boundedness, injectivity, and set inclusion;
- separate eventwise conditional-law statements from kernel or disintegration claims;
- verify that supporting propositions appear before consequences that depend on them;
- check closure or integrability before deploying inequalities or functional-analytic structure;
- cross-check notation against nearby canonical `Cours`, `TD`, and `Corriges` files instead of inventing an isolated convention.

Treat these as audit prompts, not as substitute theorem statements. Resolve the actual mathematics from the canonical project files.

## Apply the minimal valid repair

1. Locate the exact defective statement, proof step, definition, or dependency edge.
2. Patch only what is required to restore correctness and reconstructibility.
3. Preserve sound ENS-style staging, deliberate proof responsibility, file role, and local notation.
4. If canonical context explicitly identifies byte-identical mirrors, update every mirror in the same pass. Do not infer mirror status from similar filenames alone.
5. Do not enlarge the task into a global rewrite unless the defect is genuinely cross-module or the user requested global review.

## Verify the result

1. Re-read the repaired passage with its surrounding theorem and proof order.
2. Re-run any local calculation, implication, or boundary case that decided the repair.
3. Compare declared mirrors byte-for-byte when applicable.
4. Use `$validate-measure-theory-vault` whenever the work changes internal links, paths, filenames, indexes, or declared mirrors.
5. Run `git diff --check` and inspect the task-owned diff without absorbing unrelated worktree changes.

Conclude with one of:

- `OK` when no genuine defect exists;
- the precise rupture, minimal repair, and verification result;
- the unresolved hypothesis or evidence needed when legitimacy cannot be established.

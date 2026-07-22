---
name: build-daily-offline-study-packet
description: Plan, adapt, and create evidence-based daily offline study sessions in this measure-theory vault. Use when the user asks what to study today or tomorrow, requests a daily progress plan or self-contained offline packet, reports a Bilan or rupture that should change the next session, or needs a Study Log session reconciled with the active cycle. Produce derived Study Log materials, not canonical Cours or TD, and never treat generated work as mastery evidence.
---

# Build a Daily Offline Study Packet

## Recover the live contract

1. Complete the repository cold start required by `AGENTS.md` and preserve all unrelated worktree changes.
2. Follow `.agents/ROUTING.md` and read `Study Log/README.md` before changing Study Log files.
3. Read only the live chain: `Study Log/State/CURRENT.md` -> active cycle plan -> latest Daily named by CURRENT -> active packet `00_Overview.md` and `03_Carnet.md` -> active session or the exact Bilan supplied by the user.
4. If CURRENT is stale or its links fail, use `Study Log/00_Chronology.md` to locate the latest dated evidence. Do not reconstruct the state by scanning all historical sessions, Corrigés, PDFs, ZIPs, or LaTeX sources.
5. Read `00_Project/PROJECT_SPEC.md`, the relevant Module Map, and only the canonical mathematical sources needed for the proposed target. Read `00_Project/Exam P Semantic Scope.md` when the target boundary is disputed or could expand beyond Exam P.

Treat `CURRENT.md`, the cycle plan, State ledgers, and canonical modules as live sources of truth. Keep this Skill procedural; do not import dated session IDs, current ruptures, or theorem statements into it.

## Classify evidence before planning

Separate these states:

- generated or read material: no learner evidence;
- informal preparation: useful context, but no promotion;
- written attempt with a first illegal step: rupture evidence;
- hint-free closed-book exit: possible `reconstructible` evidence;
- independent unfamiliar transfer: possible `deployable` evidence.

Do not infer actual time, hints used, completion, first rupture, or mastery. If the learner has not supplied them, leave them blank and keep the corresponding Daily open or absent.

Choose exactly one adjustment decision:

- `continue`: the primary target remains legal and unfinished debt can be carried briefly;
- `repair-first`: a rupture blocks the primary target's first legal step;
- `reschedule`: the active session was not genuinely attempted or the available time cannot support its terminal test.

Apply the decision to the requested study window. Record the disposition of an older pending session separately; postponing an independent old session does not force tomorrow's decision to be `reschedule`.

When an unattempted self-contained active session already answers the request, route the learner to it or reschedule it. Do not manufacture a replacement packet merely because the date changed. If that pending session is a prerequisite for the requested target, do not skip it. If it is independent, preserve it explicitly and plan the scheduled target from its own prerequisites. A structural rupture that blocks the scheduled target makes the requested window `repair-first`.

## Fix the session brief

Recover the date, available time, offline constraints, primary target, decisive evidence, and required output from the live contract. Ask only when a missing answer would materially change the target or authorized file scope. Otherwise use the current date and the active schedule.

Before changing a calendar or total, classify the requested session as one of: reuse of an existing session, rescheduling, replacement of an already budgeted row, or genuinely additional work. Instantiating or replacing a planned row does not add its minutes a second time. Recompute packet and cycle totals from their declared components after every genuine time change.

Apply these defaults:

- Keep the session within the user's Exam P-consumed measure-theory interfaces. Do not expand into kernels, disintegration, general continuous conditional densities, full $L^2$ projection theory, or other deferred theory without a direct dependency.
- Use `$calibrate-with-ens-corpus` only when the terminal unfamiliar transfer or exit is not already supplied by canonical Cours or TD. Do not scan ENS PDFs for a routine packet built from existing canonical tasks.
- Treat ENS PDFs as calibration sources only. Never place them in Study Log `canonical-sources`, treat them as mathematical authority over the canonical module, or count their use as mastery evidence.
- Use 90 or 120 minutes according to the active plan. Make every displayed allocation sum exactly to the declared duration.
- Cap retrieval of a non-blocking prior rupture at ten minutes and continue to the main target. If the rupture is a true prerequisite, use `repair-first` instead of disguising a repair session as retrieval.
- Prefer one self-contained session over a reading list. Canonical Cours and TD remain authority, but the learner should not need them during the timed attempt.
- Produce at most four artifacts. Normally create exactly `00_Séance.md`, `01_Indications.md`, and `02_Corrigé.md` in the dated session directory.

Formal mathematical content defaults to English. Operational instructions and State or Daily prose use Traditional Chinese. French headings are legitimate only when they name a real feuille, colle, indication, or corrigé function.

## Design the mathematical spine

Start from the terminal exit and work backward. Use one continuous dependency chain when possible:

$$
\text{bounded retrieval}
\to
\text{construction}
\to
\text{representation}
\to
\text{transfer or failure}
\to
\text{hint-free exit}.
$$

For a 120-minute session, a reliable starting architecture is:

1. 0--10 minutes: non-gating question de cours or rupture retrieval;
2. 10--100 minutes: three to five dependent parts carrying the main object;
3. 100--115 minutes: document-free reconstruction plus one unfamiliar transfer;
4. 115--120 minutes: a short free-form Bilan.

Adjust the proportions to the target; preserve the opening cap and final evidence gate. Avoid fill-in worksheets, onboarding prose, difficulty labels, administrative ledgers, repeated checklists, and fields that do not collect decisive evidence. A density or representation table is acceptable only when the mathematics itself requires comparison.

Require the learner to choose or verify objects, hypotheses, representations, reference measures, theorem hypotheses, almost-everywhere bases, endpoints, and failure boundaries. A local rupture may reduce the entry cost but must not remove the terminal responsibility.

## Write the three artifacts

### `00_Séance.md`

- Declare the Study Log session frontmatter required by `Study Log/README.md`, including date, cycle, packet, stable session ID, planned and actual time, state, and solutions policy.
- Add `math-authority: derived` and a nonempty `canonical-sources` list with paths that resolve to canonical files.
- State that the file is the only document available during the attempt.
- Give each part a real mathematical function and an exact time interval.
- Provide no hint for the opening retrieval or final exit.
- End with a short Bilan asking for actual duration, indications consulted, the exact first illegal step, exit result, and bounded verdict.

### `01_Indications.md`

- Gate access until a genuine five-minute obstruction has been recorded.
- Give at most one relance per main part.
- Name one object, one theorem, or one reduction; never provide the whole route.
- Use ordinary Markdown headings. Do not use raw HTML disclosure blocks.

### `02_Corrigé.md`

- Gate access until the complete written attempt, exit, and Bilan are locked.
- Solve every question independently with the rhythm `define -> verify -> invoke -> conclude`.
- Preserve measurability, well-definedness, integrability, absolute continuity, theorem hypotheses, exceptional sets, reference measures, and a.e. uniqueness.
- Explain the precise boundary where the conclusion stops. Do not turn the solution into a second Cours.

Use portable relative Markdown links with explicit extensions and percent-encoded ASCII spaces. Follow existing filenames and packet conventions exactly; do not normalize accents or Unicode spelling by eye.

## Reconcile only what changed

For a newly planned session:

1. Create or revise the dated session artifacts.
2. Update the packet Overview, cycle plan, chronology, and CURRENT only when their active contract, dates, session count, planned time, or links genuinely change.
3. Do not create a Daily merely because work was planned. Create or open one only when actual learning evidence exists.
4. Do not update MASTERY or resolve RUPTURES from packet generation.

After the learner supplies a Bilan, reconcile in the canonical order:

1. session evidence -> packet Carnet;
2. packet evidence -> Daily;
3. recurrent, cross-packet, or dependency-blocking rupture -> `RUPTURES.md`;
4. closed-book reconstruction or unfamiliar deployment -> `MASTERY.md`;
5. current primary task and retrieval fallback -> `CURRENT.md`;
6. cycle register -> only when the cycle verdict changes or closes.

Before writing `RUPTURES.md` or `MASTERY.md`, verify the competency key in the relevant Module Map. Never invent a State key during daily reconciliation. If no canonical key matches, preserve the precise evidence in the session, Carnet, and Daily; promote nothing until the canonical interface is legitimately established. Promote only the exact declared competency supported by its exit test, not a broader topic label.

Apply the session's own verdict criteria conjunctively. Every required mark, attempt, hint condition, exit component, and prerequisite verdict must be present. A correct transfer problem cannot replace missing reconstruction evidence, and a criterion stated as “additionally” inherits the earlier criteria. When the Bilan omits required evidence, record what is established locally and make no corresponding State promotion.

Preserve `not-attempted`, `rupture`, `reconstructible`, and `deployable` as distinct competency states. Never use packet creation, repository activity, reading familiarity, or planned hours as a substitute for closed-book evidence.

## Verify and deliver

1. Solve the session internally and repair any false statement or missing hypothesis before delivery.
2. Use `$audit-measure-theory-notes` for an independent mathematical/minimal-repair pass when the session introduces substantial new mathematics.
3. Use `$validate-measure-theory-vault` for portable links, paths, frontmatter, and Study Log consistency.
4. Run `python3 .agents/skills/validate-measure-theory-vault/scripts/validate_vault.py --root . --scope changed --study-state` and `git diff --check`.
5. Manually inspect changed LaTeX commands, Unicode sigma characters, literal TABs, time totals, canonical-source resolution, and the Corrigé gate. Mechanical validation cannot prove mathematical legitimacy.
6. Inspect only the task-owned diff and perform the repository's meta reconciliation.

Deliver the selected decision, primary target, duration, created or reused artifacts, evidence boundary, and verification result. State explicitly that the packet is a plan or derived snapshot, not proof of mastery.

## Responsibility boundary

Use this Skill for Study Log execution material and daily adaptation. Use `$write-ens-td` only for canonical module TD or Corrigé production, `$write-ens-math-notes` for canonical Cours or theorem notes, `$audit-measure-theory-notes` for review or minimal repair, and `$validate-measure-theory-vault` for mechanical repository validation.

---
name: validate-measure-theory-vault
description: Validate the portability and repository hygiene of this measure-theory Markdown vault. Use after link edits, file moves or renames, index changes, broad Markdown refactors, or mirror-copy updates to check local link resolution, exact Git-index spelling and Unicode normalization, percent-encoded spaces, forbidden wikilinks or absolute paths, declared mirrors, and Git whitespace errors.
---

# Validate the Measure-Theory Vault

## Preserve the source of truth

Read the link and path rules in `AGENTS.md` before running checks. Treat those rules and Git-index paths as canonical. Keep this Skill procedural; do not copy project state or maintain a second list of current files or mirrors.

## Choose the validation scope

- Use `--scope changed` for an ordinary local Markdown edit that does not rename or move a target.
- Use `--scope all` after a rename, move, link migration, index rebuild, or other change that can break backlinks in untouched files.
- Add `--include-archive` only when the user explicitly places `_Archive/` in scope.
- Add one `--mirror 'left=right'` argument for each pair that canonical context or the user explicitly declares byte-identical. Do not guess mirror pairs.

Run from the repository root:

```bash
python3 .agents/skills/validate-measure-theory-vault/scripts/validate_vault.py --root . --scope changed
```

For a global path operation:

```bash
python3 .agents/skills/validate-measure-theory-vault/scripts/validate_vault.py --root . --scope all
```

The script checks local Markdown destinations against their source directory, requires explicit file extensions, rejects raw ASCII spaces, absolute or `file://` paths, and Obsidian wikilinks, and compares spelling with existing files while preferring Git-index paths. It also runs `git diff --check` and verifies declared mirror pairs.

## Interpret and repair

1. Treat exit status `0` as a successful mechanical validation, not as a proof of mathematical correctness.
2. Treat exit status `1` as one or more reported validation failures.
3. Do not edit files when the user requested validation or diagnosis only.
4. When correction is authorized, repair only the reported path, encoding, mirror, or whitespace rupture and rerun the same scope.
5. Escalate to `$audit-measure-theory-notes` if resolving a link or mirror disagreement requires deciding which mathematical text is canonical.

The validator checks file-level destinations but does not prove that a heading fragment names the intended semantic anchor. Inspect cross-file fragments manually when exact navigation matters.

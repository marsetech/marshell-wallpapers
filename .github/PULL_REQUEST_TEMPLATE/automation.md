# Scripts & Tooling Change

## Scope

<!--
Check the primary nature of the change. Check all that apply.
-->

- [ ] New script or tool
- [ ] Generator (metadata, galleries, or other derived output)
- [ ] Validator
- [ ] Automation or CI helper
- [ ] Refactor without intended behavior change
- [ ] CLI or interface change
- [ ] Bug fix

**Components affected:**

**Not changed:**

<!--
Optional. State what is deliberately out of scope if it could be expected to change.
-->

## Changes

**Context:**

<!--
The problem or need this addresses, in one to three sentences.
-->

**Behavior:**

<!--
What the tooling does now versus before. For refactors, state that behavior is unchanged.
Capture design decisions, not a file-by-file list.
-->

## Interface

<!--
Delete lines that do not apply.
-->

- **Inputs:** <!-- arguments, environment, files read -->
- **Outputs:** <!-- files written, stdout, exit codes -->
- **Failure behavior:**
- **Dependencies:** <!-- new or changed -->

## Side Effects & Reproducibility

<!--
Delete lines that do not apply.
-->

- **Files created, modified, or deleted:**
- **Idempotent on repeated runs:** <!-- Yes / No / N/A, and why -->
- **Deterministic for identical inputs:** <!-- Yes / No, and why -->
- **Generated artifacts:** <!-- Regenerated in this PR, deferred to a follow-up, or unaffected -->

## Validation

<!--
Check only what was actually verified. Delete items that do not apply.
-->

- [ ] Nominal case verified.
- [ ] Edge and failure cases verified (missing, malformed, or unusual input; explicit errors; correct exit status).
- [ ] Output compared against the previous version of the tooling.
- [ ] Repeated execution produces no further changes.

**Commands and environment:**

```text
<command(s) run, relevant output, and relevant tool versions>
```

## Impact

**Compatibility:**

<!--
Changes to CLI, output format, file locations, or assumptions that other scripts,
metadata, or workflows rely on. Include any required migration. Write "None" if not applicable.
-->

## Related

<!--
Issues, prerequisite PRs, and follow-ups, for example the PR that will regenerate
artifacts using this tooling. Use "Closes #n" or "Related to #n".
-->

## Checklist

- [ ] Behavior, interface, and side-effect changes are described above.
- [ ] Dependencies are declared or documented where the repository expects them.
- [ ] Documentation was updated, or no documentation is affected.
- [ ] No temporary or debugging artifacts are included.

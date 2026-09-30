# Maintenance Change

## Scope

<!--
Check the primary nature of the change. Check all that apply.
-->

- [ ] Metadata migration
- [ ] Metadata or artifact regeneration
- [ ] Repository restructuring
- [ ] Legacy removal or cleanup
- [ ] Template update
- [ ] Dependency or configuration maintenance

**Not changed:**

<!--
Optional. State what is deliberately out of scope if it could be expected to change.
-->

## Changes

**Reason:**

<!--
Why this maintenance is needed, in one to three sentences.
-->

**Summary:**

<!--
What changed at the structural level, not file by file.
-->

## Data Classification

<!--
List the paths this PR modifies under the class that applies. Delete classes that
do not apply. Generated content is reviewed through its source and procedure,
not as independently authored data.
-->

- **Source of truth / manually curated:**
- **Generated:**
- **Legacy (removed or superseded):**

**Derivation:**

<!--
For generated content, state what it is derived from, e.g.
`metadata/manual/` → `metadata/generated/` → `metadata/indexes/` → `metadata/merged/`.
Adjust to the areas actually involved.
-->

## Procedure

<!--
Required for regenerations, migrations, and bulk changes; delete otherwise.
It must be sufficient to reproduce the resulting state.
-->

```text
<exact command(s) or steps, in order>
```

**Tooling reviewed in:** <!-- #PR, "unchanged", or "this PR" -->

**Run against:** <!-- commit or starting state -->

## Validation

<!--
Check only what was actually verified. Delete items that do not apply.
-->

- [ ] Generated artifacts were produced by the intended tooling, not edited by hand.
- [ ] Derived data is consistent with its source of truth.
- [ ] Manually curated data was not modified unintentionally.
- [ ] Re-running the procedure produces no further diff.
- [ ] No references remain to removed, moved, or legacy paths.

**Notes:**

<!--
Optional. Commands run, output, or sampling performed on the resulting diff.
-->

## Impact

**Compatibility:**

<!--
Path, format, or schema changes that scripts, metadata, or users rely on, and any
migration required after merge. Write "None" if not applicable.
-->

## Related

<!--
Issues, prerequisite PRs (including the one that introduced the tooling used),
and follow-ups. Use "Closes #n" or "Related to #n".
-->

## Checklist

- [ ] Source-of-truth changes and generated output can be told apart in the diff.
- [ ] The procedure is documented well enough to reproduce the result.
- [ ] Removed legacy content has no remaining consumers.
- [ ] No temporary or working files are included.

# Wallpaper Change

## Scope

<!--
Check the primary nature of the change. Check all that apply.
-->

- [ ] Add wallpapers
- [ ] Remove wallpapers
- [ ] Replace or modify wallpaper files
- [ ] Move wallpapers between collections
- [ ] Create or modify a collection
- [ ] Update wallpaper metadata
- [ ] Regenerate galleries

**Collections affected:**

**Not changed:**

<!--
Optional. State what is deliberately out of scope if it could be expected to change.
-->

## Changes

<!--
Summarize at the level of wallpapers and collections, not files.
For small changes, name each wallpaper. For large batches, give counts per collection.
-->

-

## Provenance

<!--
Required when adding or replacing wallpapers; delete otherwise.
State the origin of the assets (author, source, or original work) and the license
or permission under which they are included.
-->

## Content Layers

<!--
Mark the layers this PR touches. Keep manually curated content and generated
artifacts distinct: generated layers are reviewed through their inputs and
generation process, not as independently authored data.
-->

**Manually curated**

- [ ] Assets
- [ ] Collections
- [ ] Manual metadata

**Generated**

- [ ] Generated metadata, indexes, or merged data
- [ ] Galleries

**Generation** <!-- Delete if no generated layer is included. -->

```text
<exact command(s) used>
```

**Tooling reviewed in:** <!-- #PR, "unchanged", or "this PR" -->

## Validation

<!--
Check only what was actually verified. Delete items that do not apply.
-->

- [ ] New and replaced assets follow the repository's conventions for format, naming, and location.
- [ ] Every wallpaper has matching metadata, and no entry references a missing asset.
- [ ] Collections reference only existing wallpapers.
- [ ] Generated layers were rebuilt from the current manual sources, and re-running generation produces no further diff.
- [ ] Manually curated metadata was not overwritten by generation.

**Notes:**

<!--
Optional. Commands run, output, or checks not covered above.
-->

## Impact

**Compatibility:**

<!--
Renamed, moved, or removed wallpapers and collections can break external references
(user configs, scripts, links). List affected paths, or write "None".
-->

## Related

<!--
Issues, prerequisite PRs, follow-ups. Use "Closes #n" or "Related to #n".
-->

## Checklist

- [ ] Changes are limited to wallpaper content and what is derived from it.
- [ ] Generated artifacts are committed together with the source changes that produced them.
- [ ] No temporary or working files are included.

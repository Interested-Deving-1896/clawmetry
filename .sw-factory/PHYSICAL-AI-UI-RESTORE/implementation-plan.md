# Restore the Physical AI workbench experience

## User correction and acceptance
The user rejected the newly introduced light /physical-ai default and asked for the original better /robotics workbench and Hardware dropdown. Preserve that established UI. Ordinary ClawMetry must still ship the built-in observer and usable persisted history without Pro.

- Existing entitled plugin navigation remains the primary Physical AI destination. A plain local /physical-ai visit may redirect to that valid installed workbench; a run/hardware deep link stays on recorded history. Free installs retain the built-in destination.
- The built-in fallback uses the existing dark dashboard tokens and an actual Hardware selector. Selecting a hardware family filters persisted runs and events, never relabels another robot or presents fabricated readings. A missing matching run is explained and older runs remain reachable.
- An additive shared catalog supplies supported recorded-source destinations to the template and /api/extensions. The daemon carries the same catalog and declared entitled plugin navigation in its existing encrypted snapshot. No new poller, database, SDK or actuator.
- Existing Pro workbench stays private. Its author investigates the already-merged Asimov armless renderer/projection seam for bounded Jumper support; no SO/RP1-schema coercion, copied private implementation, or blocked RP1 PR merge.
- Cloud consumes owner-node decrypted navigation, preserves the established workbench when actually available and uses the built-in fallback otherwise. No server-local package state masquerading as node entitlement.

## Design review before code
Use the established dashboard palette: background #0a0a0b, surface #0f0f11, border #232329, foreground #f2f2f3, muted #9b9ba3 and focus #60a5fa. Preserve Manrope and the existing compact workbench toolbar, sidebar and evidence hierarchy. Add Hardware beside the AI-view switch; retain keyboard focus and responsive wrapping. Do not invent a new visual identity. Remove the ambiguous 'More installed tools: Physical AI' wording in favor of an explicit workbench destination.

## Implementation and verification
1. Add a shared pure supported-hardware catalog and preserve validated installed Physical AI navigation, with free fallback on absent/invalid plugin output.
2. Apply the existing dark theme before first paint, add Hardware controls and robust filtered selection/empty states in the shared view. Preserve lifecycle cancellation, requested-run behavior, event ownership and bounded pagination.
3. Add encrypted UI metadata through the existing snapshot builder using an explicit plugin metadata hook; retain old-plugin fallback and never infer route/entitlement facts from installed package names.
4. Add regression tests first where practical; demonstrate original code fails theme/default/hardware guards. Run route/extension/JS/snapshot tests plus actual native-public-data browser checks and compare the unchanged old workbench.
5. Independent review, green source PR, separate release PR, inspect actual published wheel, repin held cloud integration with any qualified private workbench wheel, normal deployment and served browser verification. Existing user checkout and localhost:8900 processes remain untouched until a verified install is ready.

## Boundaries
The simulation and adapter release already verified at 0.12.930 remains valid evidence. This follow-up corrects presentation/discovery. Hardware commands remain unavailable in the free observer; existing paid controls keep their existing gates. Historical landing PR895 has a failed late documentation review; its queued deployment was cancelled and genuine native Factory correction is PR896, held for the coordinated UI delivery.

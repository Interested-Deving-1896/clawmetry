# Verification evidence

Before implementation, four new route regressions failed on the published source behavior: installed /robotics replaced, missing dark setting, absent hardware metadata and unvalidated hardware selection. The JS hardware test also failed because both families remained visible. After changes those guards pass.

- 59 focused route/extension tests pass.
- Node Physical AI UI harness passes hardware selection, source-specific event clearing, absent-matching-hardware state and requested-run hardware isolation, retaining lifecycle/deadline/privacy checks.
- Actual native recording run535dbf83af5849969f3e3d34d266d72d is replayed through a separate daemon, owned DuckDB and dashboard query proxy. /private/tmp/physical-ai-ui-restored-native/report.json records366actualevents/22namedjoints, dark computed background, Jumper -> emptyAsimov -> Jumper selection, zeroJSerrors and mobile no-overflow. This is source-candidate verification, not a released or hosted claim.
- Original localhost:8900/robotics independently returned200 with dark template/hardware-select. No original assets deleted or user process/database modified.
- Independent core reviewer approved with122tests, Node harness, diff check and fresh native proof at /private/tmp/physical-ai-independent-06xr55ui. Final published/cloud/private workbench artifact qualification remains pending.

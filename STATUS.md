# Release readiness

- [x] Both user-provided Notion exports preserved in full.
- [x] Ordered documentation and two forcing routes.
- [x] Safer GEOGRID runner; non-destructive behavior checked.
- [x] Plot and scale-factor diagnostics implemented.
- [ ] Verify `create_namelist_wps.py` domain-estimation algorithm (safe CLI is included; scientific geometry unvalidated).
- [x] Original installation/compilation workflow and WRF tests performed on Rocky Linux 9 (reported by tutorial user; exact environment and test evidence not yet archived).
- [ ] Independently reproduce clean build from this repository version on Rocky Linux 9.
- [ ] Document exact evidence and verify end-to-end GFS case (GEOGRID → UNGRIB → METGRID → REAL → WRF).
- [ ] Document exact evidence and verify end-to-end WPS-intermediate case (GEOGRID → METGRID → REAL → WRF).
- [x] Original Python scripts have been used in practice (reported by tutorial user).
- [ ] Confirm attribution for tutorials/scripts in AUTHORS.md and choose software license.
- [ ] Test script portability and file collisions on a second system.

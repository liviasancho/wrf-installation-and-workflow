# Release readiness

- [x] Both user-provided Notion exports preserved in full.
- [x] Ordered documentation and two forcing routes.
- [x] Safer GEOGRID runner; non-destructive behavior checked.
- [x] Plot and scale-factor diagnostics implemented.
- [ ] Verify `create_namelist_wps.py` domain-estimation algorithm (safe CLI is included; scientific geometry unvalidated).
- [ ] Clean build on Rocky Linux 9 using documented toolchain.
- [ ] End-to-end GFS case (GEOGRID → UNGRIB → METGRID → REAL → WRF).
- [ ] End-to-end WPS-intermediate case (GEOGRID → METGRID → REAL → WRF).
- [ ] Confirm ownership, credits, software license.
- [ ] Test script portability and file collisions on a second system.

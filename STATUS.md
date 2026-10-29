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
- [x] Added AUTHORS.md attribution and existing Apache-2.0 LICENSE file.
- [ ] Confirm copyright holder permissions and compatibility for third-party material, including Elisa Passos script.
- [ ] Test script portability and file collisions on a second system.

## Documentation integration

The historical tutorial commands have now been embedded inside the relevant `docs/` chapters. Original installation and Python scripts were used and tested by the group on Rocky Linux 9. The restructured documentation and the adapted scripts have not been validated with a fresh WRF/WPS installation and full meteorological run. Historical GFS URLs and old library versions may require adaptation.

## Initial public release with deferred validation

- [x] Added GDAS/FNL `f00` downloader with CLI and documented dependency changes (`requests`, `urllib3`).
- [x] Preserved original Elisa Passos script and credited authorship.
- [ ] Run live NCAR download tests, GRIB integrity checks and full WRF case.
- [ ] Revalidate repackaged Notion command sequences and adapted utilities on a fresh installation.

A public initial release may accurately be described as **documented, not independently end-to-end validated**. Do not mark these pending items completed without evidence.

# Start here: standalone WRF/WPS walkthrough

This repository contains the **full text and commands** from both NUMA/LAMCE tutorials, supplemented with the executable helper scripts and portable examples. **No Notion login or Notion page is necessary.**

## Tested scope and limitations

- The original GNU / Rocky Linux 9 installation, compilation and WRF run procedure was tested by the group.
- The original Python GEOGRID scripts were used by the group. Some versions adapted for this repository require independent end-to-end validation.
- Library version selections and GFS download URLs are those of the historical workflow and may need adaptation if the upstream archives change.
- A full meteorological input dataset and WRF binaries are **not bundled**; users must download and compile these.
- This documentation provides a real-data test workflow, but does not claim that the complete procedure has been rerun in a fresh environment for this release.

## Complete reading and execution order

1. [Environment and Fortran/C tests](01-environment.md): compilers, shell tools, official seven tests, expected outputs.
2. [Install libraries](02-libraries.md): source archives, compiler variables, compilation order and build commands.
3. [Library compatibility tests](02b-library-compatibility.md): compile and verify netCDF and MPI compatibility.
4. [Build WRF](03-build-wrf.md): choose serial or dmpar GNU config, `em_real` build and executable checks.
5. [Build WPS](04-build-wps.md): choose serial GNU config, build GEOGRID, UNGRIB and METGRID.
6. [Geographical data](04b-static-geographic-data.md): obtain static topography and land-use data.
7. [GEOGRID](05-geogrid.md): namelist, terrain, map factors and Python grid utilities.
8. [Forcing data](06-forcing.md): obtain GFS GRIB2 files, run UNGRIB; or skip UNGRIB for supported WPS intermediate fields.
9. [METGRID](07-metgrid.md): generate and inspect `met_em` files.
10. [REAL](08-real.md): initialize model atmosphere and boundaries.
11. [WRF](09-wrf.md): run and check `wrfout` files.
12. [Real-data smoke-test checklist](11-real-case-test.md): end-to-end checklist and run success criteria.
13. [Troubleshooting](10-troubleshooting.md).

All instructions below are local relative links. `source-notion/` is kept as an archival reference, **not** as a prerequisite.

## Two build environments

The `environment.yml` in the repository root is for the Python GEOGRID tools only. WRF/WPS and their Fortran/C libraries are installed using the separate system-level/source-build procedure above.

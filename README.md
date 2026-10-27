# WRF Installation and Workflow

A practical guide to **installing, compiling, configuring, and running WRF-ARW and WPS**, adapted from two author-provided Notion tutorials. Initial platform: **Rocky Linux 9 with GNU compilers**. Other operating systems require adaptation.

> **Status: documentation and code review draft.** The instructions and scripts have been organized and statically checked; a clean system build, a complete WPS/WRF run, and scientific validation have **not** been performed. Do not treat this as a certified installation procedure.

## Start here

1. [Environment prerequisites](docs/01-environment.md)
2. [Libraries and toolchain](docs/02-libraries.md)
3. [Build WRF](docs/03-build-wrf.md)
4. [Build WPS and acquire static geography](docs/04-build-wps.md)
5. [Create GEOGRID domains](docs/05-geogrid.md)
6. [Prepare meteorological forcing: GRIB or intermediate WPS](docs/06-forcing.md)
7. [Run METGRID](docs/07-metgrid.md)
8. [Run REAL](docs/08-real.md)
9. [Run WRF](docs/09-wrf.md)
10. [Troubleshooting and known limitations](docs/10-troubleshooting.md)

## Workflow

`GEOGRID` + (`GRIB → UNGRIB` **or** pre-existing WPS intermediate fields) → `METGRID` → `REAL` → `WRF` → `wrfout`.

**Do not run UNGRIB when the input is already in the appropriate WPS intermediate format.** Both forcing cases are explained in this tutorial.

## Reusable tools

[`scripts/geogrid/`](scripts/geogrid/README.md) contains domain generation/inspection helpers. These scripts are not distributed as figures only; they are designed as utilities, but each scientific configuration must be reviewed and tested.

## Source provenance

Original Portuguese Notion exports, including all source pages and attachments, are preserved in [`source-notion/`](source-notion/README.md). Curated documentation is in English and distinguishes the original procedure from editorial corrections or general WRF guidance.

## Scope

The project does not distribute the WRF/WPS source or copyrighted external meteorological/geographic datasets. Obtain them from their respective providers. No Hub.Rio production namelists or forcing datasets are included in this general tutorial.

## Upstream references

- [Official WRF documentation](https://www2.mmm.ucar.edu/wrf/site/)
- [Official compiling tutorial](https://www2.mmm.ucar.edu/wrf/site/compiling_tutorial.html)
- [WRF source](https://github.com/wrf-model/WRF)
- [WPS source](https://github.com/wrf-model/WPS)

## License, authorship, and citation

**Pending confirmation by repository maintainers.** A source-code license has not been assigned. Review ownership and permissions before a public release.

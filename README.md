# WRF Installation and Workflow


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23817535.svg)](https://doi.org/10.5281/zenodo.23817535)

> **Start here:** [Complete installation-to-simulation guide](docs/00-start-here.md). Every detailed command from the group's two Notion tutorials is reproduced in the `docs/` chapters. Notion access is **not required**.


A practical guide to **installing, compiling, configuring, and running WRF-ARW and WPS**, adapted from two author-provided Notion tutorials. Initial platform: **Rocky Linux 9 with GNU compilers**. Other operating systems require adaptation.

> **Status: reviewed documentation, repository draft.** The original procedure was used to install and run WRF on Rocky Linux 9, and the original Python utilities have been used in practice, as reported by the tutorial contributor. The *repository-adapted* scripts and instructions have not yet been independently validated in a clean environment. See [validation status](STATUS.md).

## Developed and distributed by

This guide is organized and distributed by the **Atmospheric Modeling Group** (*Grupo de Modelagem Atmosférica*) of **NUMA / LAMCE / UFRJ**, Brazil. The tutorial authors and contributors listed in [AUTHORS.md](AUTHORS.md) are members of this group.

**Tutorial authors:** Lívia Sancho, Rebeca Lyra, and Mauricio Soares da Silva. **Original Python scripts:** Rebeca Lyra. Additional members contributed to the project; see [AUTHORS.md](AUTHORS.md).

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

## Python environment for GEOGRID utilities

The repository includes a root-level [`environment.yml`](environment.yml) for the Python domain-generation and plotting tools. With Conda or Mamba installed:

```bash
conda env create -f environment.yml
conda activate wrf-geogrid
python -m pytest tests/
```

The original environment specification is retained at [`environment/geogrid-conda.yml`](environment/geogrid-conda.yml). The Python environment **does not install or compile WRF/WPS**; see the [environment notes](environment/README.md).

## Reusable tools

[`scripts/geogrid/`](scripts/geogrid/README.md) contains domain generation/inspection helpers. These scripts are not distributed as figures only; they are designed as utilities, but each scientific configuration must be reviewed and tested.

## Meteorological input downloader

Use [`scripts/forcing/download_gdas_fnl.py`](scripts/forcing/README.md) to retrieve NCEP GDAS/FNL 0.25° analysis files (6-hourly, `f00`, GRIB2) from NCAR GDEX `d083003`. This is a GDAS/FNL analysis product, **not a regular GFS forecast cycle**. The original `faz_download_gfs.py`, authored by **Elisa Passos**, is preserved in [`source-original/`](source-original/).

```bash
conda env create -f environment.yml
conda activate wrf-geogrid
python scripts/forcing/download_gdas_fnl.py --start 2022-01-01T00:00 --end 2022-01-01T12:00 --output-dir data/raw/gdas_fnl --dry-run
# Remove --dry-run only when ready for large downloads.
```

Follow the [forcing guide](docs/06-forcing.md) for GRIB → UNGRIB → METGRID; use the [WRF run guide](docs/11-real-case-test.md) for remaining steps. The downloader and the revised instructions have not undergone a live end-to-end validation in this release.

## Source provenance

Original Portuguese Notion exports, including all source pages and attachments, are preserved in [`source-notion/`](source-notion/README.md). Curated documentation is in English and distinguishes the original procedure from editorial corrections or general WRF guidance.

## Scope

The project does not distribute the WRF/WPS source or copyrighted external meteorological/geographic datasets. Obtain them from their respective providers. No Hub.Rio production namelists or forcing datasets are included in this general tutorial.

## Upstream references

- [Official WRF documentation](https://www2.mmm.ucar.edu/wrf/site/)
- [Official compiling tutorial](https://www2.mmm.ucar.edu/wrf/site/compiling_tutorial.html)
- [WRF source](https://github.com/wrf-model/WRF)
- [WPS source](https://github.com/wrf-model/WPS)


## Citation

If you use this repository in your research,
please cite:

Sancho, L., Lyra, R., & Soares da Silva, M.
(2026). *WRF Installation and Workflow*.
Zenodo.
https://doi.org/10.5281/zenodo.23817535

Citation metadata are provided in
[CITATION.cff](CITATION.cff).

## License

This repository is distributed under the
Apache License 2.0.

See [LICENSE](LICENSE) for details.

## Authors and Contributors

This repository is developed and distributed
by the Atmospheric Modeling Group of
NUMA/LAMCE/UFRJ.

Individual contributions and acknowledgments
are available in [AUTHORS.md](AUTHORS.md).

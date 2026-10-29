# GDAS/FNL forcing downloader

The Python tool `download_gdas_fnl.py` downloads **NCEP GDAS/FNL 0.25-degree f00 analyses**, not GFS forecast lead-time products. Data source: NCAR GDEX [d083003](https://gdex.ucar.edu/datasets/d083003/dataaccess/), DOI [10.5065/D65Q4T4Z](https://doi.org/10.5065/D65Q4T4Z).

## Installation and command

From the repository root:

```bash
conda env create -f environment.yml
conda activate wrf-geogrid
python scripts/forcing/download_gdas_fnl.py --start 2022-01-01T00:00 --end 2022-01-01T12:00 --output-dir data/raw/gdas_fnl --dry-run
```

Remove `--dry-run` to download. Dates are inclusive at 00/06/12/18 UTC, six-hourly. File size is substantial; inspect storage and network capacity first. Output belongs outside version control.

## Workflow after downloading

GDAS/FNL `.grib2` files require `link_grib.csh` and `ungrib.exe` with the correct `Vtable.GFS` before `metgrid.exe`. These files are **not** already in WPS intermediate format. Consult [meteorological forcing](../../docs/06-forcing.md).

## Safety and limitations

- HTTPS certificate verification is enabled; do not disable it for certificate issues.
- Downloads use temporary `.part` files and are moved into place after basic checks.
- Existing files are skipped but **not checksum verified**; audit or remove questionable files manually.
- A successful HTTP transfer does not prove GRIB2 scientific validity or suitability of every analysis field for your WRF setup.
- This adaptation has not been tested against a live endpoint in this release.
- Source URLs, authentication policies, file availability and formats can change.

**Original author:** Elisa Passos. The submitted source is archived unchanged as [`source-original/faz_download_gfs.py`](../../source-original/faz_download_gfs.py).

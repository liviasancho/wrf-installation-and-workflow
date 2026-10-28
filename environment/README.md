# Python dependencies

Use the **root-level `environment.yml`** for the curated GEOGRID Python utilities:

```bash
conda env create -f environment.yml
conda activate wrf-geogrid
python -m pytest tests/
```

The original `environment/geogrid-conda.yml` is retained unchanged for provenance. Its original Conda environment was named `cria_grades_wrf` and did not pin a Python version. The new root environment includes Python 3.11 and pytest, while retaining the scientific libraries from that original file (`geopy`, `numpy`, `xarray`, `netcdf4`, `matplotlib`, `cartopy`, `geopandas`). Note that `xarray` and `geopandas` are preserved from the original environment although the current curated GEOGRID scripts do not import them directly.

This environment is **only for Python tooling**. It does not install WRF-ARW, WPS, MPI, NetCDF-C/Fortran toolchains, or other dependencies required to build the numerical models. Follow `docs/01-environment.md` through `docs/04-build-wps.md` for those.

The adapted scripts have not yet been tested in a newly created Conda environment on Rocky Linux 9.

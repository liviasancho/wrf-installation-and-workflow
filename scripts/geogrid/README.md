# GEOGRID helper tools

These scripts are **tools**, not mere examples, but have not been validated against an installed WRF/WPS system in this repository release.

- `generate_grid.py`: safely invokes `geogrid.exe`; refuses to rerun when outputs exist unless `--overwrite` is explicit. Does **not** delete existing data.
- `plot_domains_geogrid.py`: visualizes the generated `geo_em.d0*.nc` files, with command-line paths.
- `correct_truelat1.py`: read-only diagnostic of `MAPFAC_M`, **not** an automatic optimum calculator.
- `create_namelist_wps.py`: original domain estimator from the tutorial, now callable through a safe CLI with explicit input/output. Its computed domain geometry and resulting namelist **must be reviewed** before any scientific run; not integrated into the standard execution path.
- `aux_func.py`: original helper, currently not required by the safer workflow; retained for traceability.

## Run GEOGRID

```bash
python scripts/geogrid/generate_grid.py --wps-dir /path/to/WPS
python scripts/geogrid/plot_domains_geogrid.py --input-dir /path/to/WPS --output domains.png
python scripts/geogrid/correct_truelat1.py /path/to/WPS/geo_em.d01.nc
```

The example JSON in `config/namelist_wps.example.json` is from a separate example, **not** the Hub.Rio scientific configuration. Replace `/CHANGE_ME/` placeholders. No scripts have been run against `geogrid.exe` in this preparation environment.

## Generate a preliminary namelist from JSON

```bash
python scripts/geogrid/create_namelist_wps.py \
  --config config/namelist_wps.example.json \
  --output ./work/namelist.wps
```

This calculation is heuristic and unvalidated. A generated namelist should not be used without inspection and an actual GEOGRID run.

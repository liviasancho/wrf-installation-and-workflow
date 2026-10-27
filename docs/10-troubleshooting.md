# 10. Known issues, limitations, and troubleshooting

| Symptom / concern | First check |
|---|---|
| Compile errors | Consistent compiler family/version, C/Fortran tests, netCDF and MPI builds |
| WPS `METGRID.TBL` missing | `opt_metgrid_tbl_path`, WPS table path/link |
| Missing `CAMtr_volume_mixing_ratio` or radiation tables | Complete WRF runtime files matching your compiled version |
| `geo_em` files overwritten | Use backups; `generate_grid.py` refuses to rerun unless `--overwrite` is explicit |
| No `met_em` files | GEOGRID, time coverage, intermediate prefix (`fg_name`), ungrib if GRIB |
| `real.exe` fails | Dates and domain agreement between WPS/WRF, links and MPI/runtime logs |
| `wrf.exe` fails | `rsl.error.*`, physics tables, MPI resource settings and namelist |

## Caveats from the originals

- Original scripts hard-coded machine-specific directories; curated operational scripts remove those assumptions where implemented.
- Original `generate_grid.py` deleted `geo_em` output files automatically: replaced with a safer non-deleting command.
- Original `create_namelist_wps.py` contains geometric heuristics that have **not** been benchmarked or independently verified. It is not a validated scientific domain-design method.
- Original versions and menu option numbers are environment-specific. The original WPS `./configure` steps are not identical to the WPS 4.4+ upstream option `--build-grib2-libs`.
- Two tutorials include examples for different machines and purposes; do not combine paths or namelists blindly.
- No clean-room compilation, end-to-end WRF execution, or exact scientific reproduction was performed during preparation.

For exact original wording and version-specific workarounds, consult `source-notion/`.

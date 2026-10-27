# 5. GEOGRID: configure and generate model domains

**Source:** Notion “1 - Geogrid”, including the JSON/YAML and Python utilities.

1. Put `namelist.wps` in the WPS execution directory and configure: `max_dom`, dates, `parent_id`, `parent_grid_ratio`, `i_parent_start`, `j_parent_start`, `e_we`, `e_sn`, `dx`, `dy`, projection, coordinates and `geog_data_path`.
2. Ensure GEOGRID static geographical files exist and that `GEOGRID.TBL` can be found.
3. Run GEOGRID, inspect log and verify one `geo_em.d0*.nc` per domain.

```bash
cd /path/to/WPS
./geogrid.exe >& log.geogrid
grep -i 'successful completion' log.geogrid
ls -lh geo_em.d0*.nc
```

Or use the [safe helper scripts](../scripts/geogrid/README.md):

```bash
python scripts/geogrid/generate_grid.py --wps-dir /path/to/WPS
python scripts/geogrid/plot_domains_geogrid.py --input-dir /path/to/WPS --output domains.png
python scripts/geogrid/correct_truelat1.py /path/to/WPS/geo_em.d01.nc
```

Run these commands from the repository root. Install plotting dependencies with [`environment/geogrid-conda.yml`](../environment/geogrid-conda.yml).

The original JSON is an **illustrative independent domain**, not a default validated science setup. Examine its numeric geometry and output before running WRF. `correct_truelat1.py` performs diagnostics only; changing `truelat1` demands re-running GEOGRID and reviewing the result.

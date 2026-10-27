# 7. METGRID

**Source:** Notion “3 - Metgrid”. GEOGRID and atmospheric intermediate data must be available.

Check `fg_name` in `namelist.wps`, then:

```bash
cd /path/to/WPS
./metgrid.exe >& log.metgrid
grep -i 'successful completion' log.metgrid
ls -lh met_em.d0*.nc
```

If you encounter `Could not open file METGRID.TBL`, check `opt_metgrid_tbl_path` or the appropriate `metgrid/METGRID.TBL` link as in the original tutorial. Outputs are `met_em` files for each model domain and forcing time. Ensure time coverage is complete before REAL.

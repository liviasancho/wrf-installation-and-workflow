# Run a real-data WRF test from start to finish

This checklist makes the minimum run path explicit. It assumes you have followed chapters 01–04b to compile WRF (`em_real`) and WPS and install geographic data. **A test cannot run without actual forcing data; the repository does not distribute GFS files.**

## A. Prepare input data

1. Select a short contiguous GFS forecast cycle with files for each valid time required by your run. Use the complete acquisition commands in [chapter 06](06-forcing.md). The February 2023 URLs there are historical examples, **not guaranteed live download links**. Obtain equivalent available files if needed.
2. In your WPS working directory, copy the supplied `namelist.wps` example from the compiled WPS directory and back it up. Set `start_date`, `end_date`, `interval_seconds`, `max_dom`, geometry and `geog_data_path` to match the data and static files. The WRF compilation includes example namelists; adapt them to actual target dates and domains.
3. Execute GEOGRID (see [05](05-geogrid.md)); inspect `log.geogrid` for `Successful completion` and verify `geo_em.d01.nc` (and others for nested grids).
4. For GRIB2 data, execute `link_grib.csh`, link `Vtable.GFS`, set `prefix` in `namelist.wps`, and run UNGRIB. For WPS intermediate input skip UNGRIB. See [06](06-forcing.md).
5. Run METGRID; inspect `log.metgrid` and verify `met_em.d01.*.nc` for all boundary times. See [07](07-metgrid.md).

## B. Initialize WRF and run

Execute from the **compiled** WRF `run/` directory (which contains mandatory WRF runtime tables). Do not replace these tables with files from a different WRF version.

```bash
# Edit namelist.input first: its dates, domains and intervals MUST agree
# with namelist.wps and the available met_em files.
cd "$HOME/WRF/Build_WRF/WRF/run"  # Replace with YOUR actual WRF location
ln -s /absolute/path/to/WPS/met_em.d0*.nc .
# For a GNU dmpar build, with 2 MPI ranks as a small test:
mpirun -np 2 ./real.exe > log.real 2>&1
# Inspect output and confirm success before running WRF:
tail -n 30 rsl.error.0000
ls -lh wrfinput_d0* wrfbdy_d01
mpirun -np 2 ./wrf.exe > log.wrf 2>&1
tail -n 30 rsl.error.0000
ls -lh wrfout_d0*
```

**Do not copy the `cd` example blindly:** check the actual directory layout; the original tutorial uses separate `serial`, `dmpar` and `smpar` builds. Use `./real.exe` / `./wrf.exe` instead of MPI for serial builds. Remove or relocate old `met_em` and WRF output links only deliberately.

## C. Acceptance checklist

- WRF and WPS build logs do not contain unresolved fatal errors; executables are present and nonempty.
- `geogrid.exe`, `ungrib.exe` (GRIB path) and `metgrid.exe` report successful completion.
- Expected `geo_em` and `met_em` products exist, with matching domains and time coverage.
- `real.exe` finishes successfully; `wrfinput_d0*` and `wrfbdy_d01` exist.
- `wrf.exe` finishes successfully; `wrfout_d0*` exists and has nonzero size.
- `rsl.error.0000` and other rank logs are checked for a final success indication and no fatal runtime errors.

**Not yet provided:** a fixed, verified small-input GFS dataset, its checksum, and matching one-click test namelists. Consequently this is a detailed reproducible *procedure* but not yet a fully automatic plug-and-play benchmark. Avoid claiming otherwise.

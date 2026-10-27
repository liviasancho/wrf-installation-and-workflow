# 8. REAL: initialize atmospheric fields

**Source:** Notion “4 - Real”. Use a separate WRF run directory containing the compiled executables' necessary runtime tables and compatible `namelist.input`.

```bash
cd /path/to/WRF/run
# Ensure met_em files were generated and are available here:
ln -s /path/to/WPS/met_em.d0*.nc .
# For a dmpar (MPI) build:
mpirun -np 2 ./real.exe
# Inspect logs and output files:
tail -n 30 rsl.error.0000
ls -lh wrfinput_d0* wrfbdy_d01
```

`-np 2` is a tutorial example, **not** a universal setting. For serial builds use `./real.exe`; for MPI builds use an appropriate process count. Use correct time/domain settings, ensure the `met_em` links do not collide with existing run artifacts, and inspect logs for success.

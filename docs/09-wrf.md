# 9. WRF: run the simulation

**Source:** Notion “5 - WRF”. After successful REAL, make sure WRF runtime tables (e.g. radiation/ozone tables) are available in the execution folder. Running from `WRF/run` usually supplies the standard files.

```bash
cd /path/to/WRF/run
# For a dmpar (MPI) build:
mpirun -np 2 ./wrf.exe
# For serial builds: ./wrf.exe
# After completion:
tail -n 30 rsl.error.0000
ls -lh wrfout_d0*
```

The original tutorial also demonstrates `nohup ... &`; use it only after establishing appropriate process/log management. The original troubleshooting describes missing `CAMtr_volume_mixing_ratio` and other runtime tables, which must be linked from the **matching WRF installation**. Do not copy unrelated versioned tables. Confirm a successful termination, not merely that a `wrfout` filename exists.

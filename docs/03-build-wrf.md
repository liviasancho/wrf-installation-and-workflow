# 3. Compile WRF-ARW

**Source:** “Compilando o WRF” from the supplied Notion export. The source covers serial, `dmpar` (MPI), and `smpar` (OpenMP). It recommends `dmpar` based on the author's operational experience.

## Acquire source

```bash
git clone --recurse-submodules https://github.com/wrf-model/WRF.git
cd WRF
# For fully reproducible builds, select and record a specific release tag.
git describe --tags --always
```

## Configure and compile for real-data simulations

```bash
./configure
# Select GNU compiler and the processing mode installed on your system.
# Do NOT assume option numbers 34/33 in newer versions.
./compile em_real >& compile.log
ls -l main/real.exe main/wrf.exe
```

`./compile em_real` is the workflow described in the original tutorial. Confirm executable presence, examine `compile.log` and check exit/error messages before running. Build and configuration depend on environment variables from [step 2](02-libraries.md).

The source tutorial additionally discusses `ndown.exe`, `tc.exe`, a possible `configure.wrf` toolchain mismatch and optional GRIB2-related changes to `arch/Config.pl`. Treat those as **case-specific troubleshooting notes**, not edits to apply blindly.

For complete serial/`dmpar`/`smpar` variants see the preserved original installation page under [`source-notion/installation/`](../source-notion/installation/).

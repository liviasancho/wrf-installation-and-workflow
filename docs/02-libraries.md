# 2. Install prerequisite libraries

The original Rocky Linux 9 / GNU procedure builds several libraries from source under `Build_WRF/LIBRARIES`. It references:

| Component | Version in the Notion tutorial |
|---|---|
| MPICH | 4.2.0 |
| netCDF-C | 4.9.2 |
| netCDF-Fortran | 4.6.1 |
| JasPer | 1.900.1 |
| libpng | 1.2.50 |
| zlib | 1.2.11 |
| SZIP | 2.1.1 |
| HDF5 | 1.8.21 |

These are **historical versions from the supplied procedure**, not a blanket recommendation that all are currently optimal or secure. Some old source URLs or build flags may no longer work. The source tutorial also references HDF5 inconsistently in one filename: verify the actual archive downloaded before extracting.

## Environment

Start with a configured toolchain and a private build prefix; do not blindly copy source-specific paths:

```bash
export BUILD_ROOT="$HOME/WRF/Build_WRF"
export LIB_ROOT="$BUILD_ROOT/LIBRARIES/GNU"
mkdir -p "$LIB_ROOT"
export CC=gcc CXX=g++ FC=gfortran F77=gfortran
export NETCDF="$LIB_ROOT"
export HDF5="$LIB_ROOT"
export PATH="$LIB_ROOT/bin:$PATH"
export LD_LIBRARY_PATH="$LIB_ROOT/lib:${LD_LIBRARY_PATH:-}"
```

The actual prefix and any MPI/GRIB2 paths must match the installed libraries. This example **only sets shell variables**; it does not install anything.

## Build order used in the source

SZIP / zlib → HDF5 → MPICH (if MPI build) → netCDF-C → netCDF-Fortran → libpng / JasPer and GRIB2 support. Follow the complete `configure`, `make`, `make check`, `make install` instructions in the original tutorial and inspect errors before proceeding. `--disable-byterange` is described as a workaround for a cURL-dependent netCDF-C build issue, **not** a default requirement.

For WPS 4.4+, the [official compiling guide](https://www2.mmm.ucar.edu/wrf/site/compiling_tutorial.html) also documents `./configure --build-grib2-libs`, allowing WPS to build GRIB2 compression libraries internally. This is an additional upstream option; it does not replace the original installation record.

## Verify before compiling WRF

```bash
nc-config --version
nf-config --version
command -v mpif90 || true
```

Record paths and versions in the research log; do not proceed unless netCDF-C and netCDF-Fortran are compatible with the selected compilers.

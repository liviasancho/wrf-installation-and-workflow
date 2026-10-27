# 1. Environment checks

**Source:** Notion installation tutorial, “Testes do ambiente do sistema”. The described successful environment was Rocky Linux 9, GNU compilers (example GCC/GFortran 11.4.1).

Check toolchain availability and versions:

```bash
command -v gcc g++ gfortran cpp make perl csh sh git
for x in gcc g++ gfortran cpp; do "$x" --version | head -n 1; done
```

The source tutorial separately runs Fortran/C compatibility tests 1–4 and csh/perl/sh tests 5–7 from the [official test archive](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/Fortran_C_tests.tar). Follow those source steps before building the libraries. Also check common UNIX utilities (`ar`, `awk`, `sed`, `m4`, `tar`, `make`, etc.).

```bash
mkdir -p "$HOME/WRF/Build_WRF/LIBRARIES" "$HOME/WRF/TESTS"
```

**Do not mix incompatible compiler families/toolchains** between MPI, HDF5, netCDF, WRF and WPS. Verify installed compiler versions; do not assume the selectable menu number from the source tutorial is still correct.

For the complete original test commands and expected strings, see [`source-notion/installation/`](../source-notion/installation/).

# 4. Compile WPS and acquire static geographical data

**Sources:** Notion “Compilando o WPS” and “Dados geográficos estáticos”.

```bash
# Run from a directory alongside an already-compiled WRF checkout.
git clone https://github.com/wrf-model/WPS.git
cd WPS
export WRF_DIR="$(realpath ../WRF)"
# For WPS 4.4+ if using WPS internal GRIB2 libraries:
./configure --build-grib2-libs
# For older versions, follow their specific documentation instead.
./compile >& compile.log
ls -l geogrid.exe ungrib.exe metgrid.exe
```

This is an **illustrative current upstream branch**; matching compiler/netCDF and WRF/WPS versions is essential. In the original tutorial, `./configure` was used and the serial configuration was chosen. Make sure all three executable links resolve and are nonempty.

Download WPS geographical datasets from [official WRF geographic data guidance](https://www2.mmm.ucar.edu/wrf/site/), extract into a dedicated `GEOG` folder, and point `geog_data_path` to the real directory in `namelist.wps`. Check disk space and dataset license/terms. The original static-data instructions are preserved without inventing a download address for a particular selected product.

# 6. Meteorological forcing: two supported paths

**Source:** “0 - Dados Reais” and “2 - Ungrib”.

The dates of input atmospheric files must cover the complete interval configured in `namelist.wps` / `namelist.input`.

## A. GRIB forcing (e.g. GFS)

This is the path demonstrated by the Notion execution tutorial: obtain GRIB files, link them using WPS `link_grib.csh`, link the correct variable table, then run `ungrib.exe`.

```bash
cd /path/to/WPS
./link_grib.csh /path/to/grib_files/*
ln -sfn ungrib/Variable_Tables/Vtable.GFS Vtable
./ungrib.exe >& log.ungrib
```

Verify the actual Vtable filename and the existence of `link_grib.csh`. The output prefix (`FILE` by default) must match `fg_name` in `namelist.wps`. Follow the GFS acquisition instructions and source URLs in the preserved Notion page; no downloading tool is included yet.

## B. Data already in WPS intermediate format

**Skip UNGRIB entirely** when data are already compatible WPS intermediate files (e.g. CESM-Int). Place or link those files in a location/prefix matching the `fg_name` list in `namelist.wps`; then run METGRID directly.

This branch reflects the later Hub.Rio workflow discussion, and is presented here as a general use case. A WPS intermediate file is **not** automatically equivalent to any NetCDF/GRIB file; verify the exact format and expected filename prefix.

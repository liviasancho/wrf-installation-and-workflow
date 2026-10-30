# Authors and contributors

This repository is organized and distributed by the **Atmospheric Modeling Group** (*Grupo de Modelagem Atmosférica*) of the **Environmental Modeling Center (NUMA)** (*Núcleo de Modelagem Ambiental*), at the **Laboratory of Computational Methods in Engineering (LAMCE)** (*Laboratório de Métodos Computacionais em Engenharia*), **Federal University of Rio de Janeiro (UFRJ), Brazil**.

The individuals listed below are members of the Atmospheric Modeling Group. The group and the people credited here are one and the same.

## Tutorial authors

- Lívia Sancho
- Rebeca Lyra
- Mauricio Soares da Silva

The list of tutorial authors is preliminary and may be extended as further contributions are confirmed.

## Original Python scripts

**Rebeca Lyra** authored the original Python scripts for domain preparation and visualization:

- `create_namelist_wps.py`
- `generate_grid.py`
- `plot_domains_geogrid.py`
- `correct_truelat1.py`
- `aux_func.py`

Subsequent repository adaptations can be traced through version control.

## Additional contributors

Members identified as contributors to the material, without further assignment of individual roles:

- Lívia Sancho
- Mauricio Soares da Silva
- Rebeca Lyra
- Larissa de Freitas
- Nilton Moraes
- Ian Dragaud
- Daniela Marinho
- Matheus Gomes

**Elisa Passos**
- Original author of the GDAS/FNL data download script (`faz_download_gfs.py`).
- The script was adapted for integration into the WRF Installation and Workflow repository, with attribution to the original author.

Names are repeated across sections where contributions overlap. Inclusion as a contributor does not imply authorship of every file.

## Validation

The original installation and execution workflow was used successfully on Rocky Linux 9, including complete WRF tests. The original Python scripts were also used in practice. Repository-specific adaptations should be independently checked before being declared validated.

## Updates

Additional authors, completed names, affiliations, and more detailed contributions can be included when confirmed. This attribution does not establish copyright ownership or software licensing.

## GDAS/FNL data acquisition script

- **Elisa Passos** — author of the original Python downloader (`source-original/faz_download_gfs.py`), adapted in `scripts/forcing/download_gdas_fnl.py`.

The adapted implementation retains attribution to the original author; modifications are documented in the script and Git history. Elisa is not automatically listed as a tutorial author or a member of the Atmospheric Modeling Group.

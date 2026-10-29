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


---

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 3 - Metgrid

# 3 - Metgrid

Em caso de dúvidas, utilizar o site de boas práticas e o tutorial:

[https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html](https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html)

[https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1)

1. Execute o metgrid:

```bash
ln -s ~/WRF/Build_WRF/serial/WPS/metgrid.exe metgrid.exe
```

```bash
./metgrid.exe >& log.metgrid
```

**ATENÇÃO!!** A minha execução falhou com o seguinte erro: *ERROR: Could not open file METGRID.TBL*. Tive que configurar o caminho até o diretório do METGRID.TBL no namelist na opção *opt_metgrid_tbl_path*.

Uma execução bem-sucedida retornará a mensagem:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!  Successful completion of metgrid.  !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Ao finalizar, devem existir arquivos com o prefixo *met_em** em número proporcional à quantidade de arquivos de CI e CC e de domínios.

Se eram 3 arquivos e 2 domínios, devem existir 6 arquivos - 3 para cada domínio.

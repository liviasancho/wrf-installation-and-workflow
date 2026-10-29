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


---

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 5 - WRF

# 5 - WRF

Em caso de dúvidas, utilizar o site de boas práticas e o tutorial:

[https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html](https://www2.mmm.ucar.edu/wrf/users/best_practices.html)

[https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1)

Esse passo a passo também pode servir como teste de instalação do modelo. Para isso, o modelo foi executado tanto em modo serial como em paralelo com diferentes números de processadores. Dessa forma, as páginas 4 e 5 devem ser feitas para todos os casos e os arquivos devem ser colocados em diferentes diretórios.

1 - Gere um link do executável do wrf no diretório desejado:

```bash
ln -s ~/WRF/Build_WRF/serial/WRF/run/wrf.exe wrf.exe
```

```bash
ln -s ~/WRF/Build_WRF/dmpar/WRF/run/wrf.exe wrf.exe
```

```bash
ln -s ~/WRF/Build_WRF/smpar/WRF/run/wrf.exe wrf.exe
```

1. Rode o wrf.

```bash
nohup ./wrf.exe &
```

```bash
nohup mpirun -np 2 ./wrf.exe &
```

**ATENÇÃO!!** A minha execução falhou com o seguinte erro: 

FATAL CALLED FROM FILE: <stdin> LINE: 203

CLWRF: 'CAMtr_volume_mixing_ratio' does not exist

Para resolver o problema, executei os seguintes passos:
No terminal, executei o seguinte comando:

```bash
locate CAMtr_volume_mixing_ratio
```

Dentre os vários resultados, identifiquei o que era exatamente o meu caso de acordo com o tipo de rodada (serial ou paralelo) e fiz um link desse arquivo no meu diretório de rodada:

```bash
ln -s ~/WRF/Build_WRF/serial/WRF/run/CAMtr_volume_mixing_ratio CAMtr_volume_mixing_ratio
```

O mesmo ocorreu com outros arquivos. É interessante para o aprendizado identificar cada arquivo e fazer um link a cada vez que retorna o erro.

Para as demais vezes, pode-se executar:

```bash
ln -sf ~/WRF/Build_WRF/serial/WRF/run/*.TBL . ;
ln -sf ~/WRF/Build_WRF/serial/WRF/run/ozone* . ;
ln -sf ~/WRF/Build_WRF/serial/WRF/run/RRTMG_* .
```

1. Verifique o final dos arquivos "rsl" ou o final do arquivo nohup para ter certeza de que a execução foi finalizada com sucesso.

```bash
tail rsl.error.0000
```

```bash
tail nohup
```

1. Se verificar um "SUCCESS", além de todos os arquivos “wrfout*”, a rodada foi finalizada com sucesso.

1. Se a rodada foi um sucesso, pode-se prosseguir com as análises dos resultados.

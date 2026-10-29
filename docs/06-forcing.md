# 6. Meteorological forcing: two supported paths

**Source:** “0 - Dados Reais” and “2 - Ungrib”.

The dates of input atmospheric files must cover the complete interval configured in `namelist.wps` / `namelist.input`.

## GDAS/FNL 0.25-degree analyses (new reproducible acquisition option)

The included [`download_gdas_fnl.py`](../scripts/forcing/README.md) fetches NCAR GDEX `d083003` **GDAS/FNL final analyses (`f00`)** at six-hour intervals in GRIB2 format. Do not label these as standard GFS operational forecast products. The original script was written by Elisa Passos. The new utility preserves attribution and improves CLI arguments, TLS verification, and failure handling.

```bash
conda env create -f environment.yml
conda activate wrf-geogrid
python scripts/forcing/download_gdas_fnl.py --start 2022-01-01T00:00 --end 2022-01-01T12:00 --output-dir data/raw/gdas_fnl --dry-run
```

Remove `--dry-run` when ready; dates are illustrative, not a tested reference case. After download, prepare WPS GRIB links, the suitable Vtable, and run UNGRIB, then METGRID. Check the number of analysis times against the configured run interval.

## A. GRIB forcing (e.g. GFS)

This is the path demonstrated by the Notion execution tutorial: obtain GRIB files, link them using WPS `link_grib.csh`, link the correct variable table, then run `ungrib.exe`.

```bash
cd /path/to/WPS
./link_grib.csh /path/to/grib_files/*
ln -sfn ungrib/Variable_Tables/Vtable.GFS Vtable
./ungrib.exe >& log.ungrib
```

Verify the actual Vtable filename and the existence of `link_grib.csh`. The output prefix (`FILE` by default) must match `fg_name` in `namelist.wps`. The complete GFS acquisition procedure is reproduced below; its historical URLs are not guaranteed to retain older cycles.

## B. Data already in WPS intermediate format

**Skip UNGRIB entirely** when data are already compatible WPS intermediate files (e.g. CESM-Int). Place or link those files in a location/prefix matching the `fg_name` list in `namelist.wps`; then run METGRID directly.

This branch reflects the later Hub.Rio workflow discussion, and is presented here as a general use case. A WPS intermediate file is **not** automatically equivalent to any NetCDF/GRIB file; verify the exact format and expected filename prefix.


---

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 0 - Dados Reais

# 0 - Dados Reais

**ATENÇÃO!!**

- Para casos reais, o WRF requer informações meteorológicas atualizadas tanto para uma condição inicial como também para condições de contorno laterais. Esses dados meteorológicos são tradicionalmente um arquivo Grib fornecido por um modelo ou análise externa executada anteriormente. Para uma configuração semi-operacional, os dados meteorológicos são geralmente provenientes de um modelo global, o que permite localizar os domínios do modelo WRF em qualquer lugar do globo.
- O *National Centers for Environmental Prediction* (NCEP) executa o modelo *Global Forecast System* (GFS) quatro vezes ao dia (inicializações válidas para 0000, 0600, 1200 e 1800 UTC). Este é um conjunto de resultados de previsão global, isobárico, de 0,5° de latitude/longitude, que está disponível gratuitamente e geralmente acessível +4h após o período de inicialização.
- Precisamos adquirir um único arquivo para cada período solicitado. Por exemplo, se desejarmos as horas 0, 6 e 12 de uma previsão inicializada em 12 de julho de 2019 às 0000 UTC, precisaremos dos seguintes horários:
    
    2019071200 – 0 h
    
    2019071206 – 6 h
    
    2019071212 – 12 h
    
- Eles se traduzem nos seguintes nomes de arquivo:
    
    gfs.2019071200/gfs.t00z.pgrb2.0p50.f000
    
    gfs.2019071200/gfs.t00z.pgrb2.0p50.f006
    
    gfs.2019071200/gfs.t00z.pgrb2.0p50.f012
    
    - Observe que os resultados e o tempo de inicialização (gfs.2019071200) permanecem os mesmos e o ciclo de previsão permanece o mesmo (t00z). O que é incrementado é a hora da previsão (f00, f06, f12).
- O que é mostrado nesse passo a passo é apenas um exemplo em termos de datas e tempos a serem adquiridos. Ajuste os comandos para refletir as informações de data e hora de interesse.
- Os arquivos adquiridos por meio dos comandos mostrados aqui são do tipo GRIB2 e podem ser utilizados diretamente pelo ungrib (item 2).
- Normalmente, nos servidores de dados do NCEP, apenas os 2 a 3 dias mais recentes estão disponíveis em um determinado momento.

1. Antes de adquirir os dados, crie um diretório onde eles serão colocados e navegue até ele:

```bash
mkdir DATA ;
cd DATA
```

1. Execute os comandos abaixo para adquirir 3 diferentes tempos de uma previsão iniciada no dia 1° de fevereiro de 2023 às 0h, do ciclo t00z para as horas 0, 3 e 6.

```bash
wget https://ftp.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.20230201/00/atmos/gfs.t00z.pgrb2.0p25.f000

wget https://ftp.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.20230201/00/atmos/gfs.t00z.pgrb2.0p25.f003

wget https://ftp.ncep.noaa.gov/data/nccf/com/gfs/prod/gfs.20230201/00/atmos/gfs.t00z.pgrb2.0p25.f006
```


### Original procedure: 2 - Ungrib

# 2 - Ungrib

Em caso de dúvidas, utilizar o site de boas práticas e o tutorial:

[https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html](https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html)

[https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1)

1. Antes de rodar o ungrib, é necessário que os arquivos de condições iniciais (CI) e de contorno (CC) sejam adquiridos.
    1. Esses arquivos podem ser de diversas fontes. A mais comum é o GFS.
    2. Nesse passo a passo, as instruções de como baixar os arquivos do GFS estão no item 0.
    3. **ATENÇÃO!!** Lembre-se que as datas dos arquivos de CI e CC devem englobar as datas configuradas no namelist. Ou seja, não podem iniciar depois ou terminar antes das datas do namelist.

1. Uma vez que os arquivos de CI e CC foram adquiridos, estando no seu diretório, gere um link para onde estão localizados esses arquivos.

```bash
ln -s ~/WRF/Build_WRF/serial/WPS/link_grib.csh link_grib.csh
```

```bash
./link_grib.csh data/
```

1. Gere um link para a Vtable correta. No caso aqui, para a Vtable do GFS

```bash
ln -s ~/WRF/serial_wrf/wps/ungrib/Variable_Tables/Vtable*.GFS Vtable*
```

1. Execute o ungrib.

```bash
ln -s ~/WRF/Build_WRF/serial/WPS/ungrib.exe ungrib.exe
```

```bash
./ungrib.exe
```

Uma execução bem-sucedida retornará a mensagem:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!  Successful completion of ungrib.  !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Ao finalizar, devem existir arquivos com o prefixo "FILE".

Caso o padrão de nomenclatura tenha sido alterado, o prefixo irá refletir essa alteração.

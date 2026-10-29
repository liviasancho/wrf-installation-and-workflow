# 4b. Install static geographical data

The static geographical files required by GEOGRID are **separate downloads from WRF/WPS source code**. The steps below are reproduced directly from the NUMA/LAMCE tutorial. The historical download addresses should be verified before use. Ensure each dataset is extracted into the geographic dataset directory named in `geog_data_path`.

# 6 - Dados geográficos estáticos

**ATENÇÃO!!**

- O WRF é capaz de criar simulações idealizadas, embora a maioria dos usuários esteja interessada em casos reais. Para iniciar uma simulação de caso real, a localização física do domínio no globo e as informações estáticas dessa localização devem ser criadas. Isto requer um conjunto de dados que inclua campos como topografia e categorias de uso do solo. Esses dados estão disponíveis na página de download do [WRF](http://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html).
- Lembre-se de que se você estiver adquirindo o conjunto de dados completo, o arquivo será muito grande. Se você estiver compartilhando espaço em um *cluster*, considere colocá-lo em um local central para que todos possam em vez de cada usuário realizar esse passo.

1. Navegue até o diretório *Build_WRF*, adquira o arquivo de topografia e descompacte.

```bash
wget -c https://www2.mmm.ucar.edu/wrf/src/wps_files/geog_high_res_mandatory.tar.gz
```

```bash
tar -xvf geog_high_res_mandatory.tar.gz
```

1. O arquivo gerado terá o nome *geog*. Renomeie para *WPS_GEOG*.

```bash
mv geog WPS_GEOG
```

1. Adquira o arquivo MODIS de uso e cobertura de solo.

```bash
wget -c https://www2.mmm.ucar.edu/wrf/src/wps_files/modis_landuse_20class_15s_with_lakes.tar.gz
```

```bash
tar -xvf modis_landuse_20class_15s_with_lakes.tar.gz
```

**OBSERVAÇÃO!!** Existem outros tipos de dados que podem ser adquiridos e isso vai variar de acordo com a simulação que será feita.

**ATENÇÃO!!** Todos os arquivos referentes aos dados geográficos estáticos devem ser colocados dentro do mesmo diretório.

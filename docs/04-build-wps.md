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


---

**Next:** install [static geographical datasets](04b-static-geographic-data.md) before GEOGRID.

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 5 - Compilando o WPS

# 5 - Compilando o WPS

Mais informações diretamente na página: [http://www2.mmm.ucar.edu/wrf/users/download/get_source.html](http://www2.mmm.ucar.edu/wrf/users/download/get_source.html)

**ATENÇÃO!!** Diferentemente do WRF, não compensa compilar o WPS em paralelo ou serial. Dessa forma, prosseguiremos com a compilação do WPS em serial.

1. Adquira a versão mais atual do WPS através do comando:

```bash
git clone https://github.com/wrf-model/WPS
```

1. Navegue até o diretório “WPS” criado:

```bash
cd WPS
```

**OBSERVAÇÃO!!** Para versões anteriores, consultar o site: https://github.com/wrf-model/WPS/releases

1. Apesar de ser um novo diretório, para ter certeza de não haver resíduos de compilações, execute o comando:
    
    ```bash
    ./clean
    ```
    
2. Execute o comando:

```bash
./configure
```

Você verá várias opções. Escolha a opção que lista o compilador que você está usando e a maneira como deseja construir o WRF (ou seja, em série ou em paralelo).

No caso desse passo a passo, como queremos instalar a versão serial e estamos utilizando os compiladores GNU, a opção é a nº 1. 

1. Selecione a opção 1.

1. Execute o comando:

```bash
./compile >& log.compile
```

Para checar se os executáveis foram criados, execute:

```bash
ls -ltrh *.exe
```

Os seguintes links dos executáveis devem existir:

geogrid.exe → geogrid/src/geogrid.exe

ungrib.exe → ungrib/src/ungrib.exe

metgrid.exe → metgrid/src/metgrid.exe

Verifique se esses executáveis não estão vazios dentro de */src/ directory - arquivos vazios tem tamanho 0. Siga o exemplo abaixo e replique para todos os executáveis:

```bash
ls -ls geogrid/src/geogrid.exe
```

Caso na compilação apareça algo parecido com:
“wrf_io.f:(.text+0x1098f): undefined reference to `GOMP_parallel_start' wrf_io.f:(.text+0x109a1): undefined reference to` GOMP_parallel_end'”

Adicione “-lgomp” na variável WRF_LIB dentro do arquivo configure.wps, depois de “-lnetcdf”

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
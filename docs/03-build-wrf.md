# 3. Compile WRF-ARW

**Source:** “Compilando o WRF” from the supplied Notion export. The source covers serial, `dmpar` (MPI), and `smpar` (OpenMP). It recommends `dmpar` based on the author's operational experience.

## Acquire source

```bash
git clone --recurse-submodules https://github.com/wrf-model/WRF.git
cd WRF
# For fully reproducible builds, select and record a specific release tag.
git describe --tags --always
```

## Configure and compile for real-data simulations

```bash
./configure
# Select GNU compiler and the processing mode installed on your system.
# Do NOT assume option numbers 34/33 in newer versions.
./compile em_real >& compile.log
ls -l main/real.exe main/wrf.exe
```

`./compile em_real` is the workflow described in the original tutorial. Confirm executable presence, examine `compile.log` and check exit/error messages before running. Build and configuration depend on environment variables from [step 2](02-libraries.md).

The source tutorial additionally discusses `ndown.exe`, `tc.exe`, a possible `configure.wrf` toolchain mismatch and optional GRIB2-related changes to `arch/Config.pl`. Treat those as **case-specific troubleshooting notes**, not edits to apply blindly.

For complete serial/`dmpar`/`smpar` variants see the preserved original installation page under [`source-notion/installation/`](../source-notion/installation/).


---

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 4 - Compilando o WRF

# 4 - Compilando o WRF

Mais informações diretamente na página: [http://www2.mmm.ucar.edu/wrf/users/download/get_source.html](http://www2.mmm.ucar.edu/wrf/users/download/get_source.html)

# Compilando o modelo em modo serial

1. Dentro do diretório “Build_WRF”, crie um diretório “serial” e navegue até ele.

```bash
mkdir serial
cd serial
```

1. Verifique se o programa “git” está instalado executando:

```bash
which git
```

1. Adquira a versão mais atual do WRF através do comando:

```bash
git clone --recurse-submodules https://github.com/wrf-model/WRF
```

**OBSERVAÇÃO!!** Para versões anteriores, consultar o site: [http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html](http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html)

1. Antes de configurarmos, vamos alterar o arquivo Config.pl para que seja possível utilizarmos arquivos do tipo GRIB2, que é o formato dos arquivos do GFS.

```bash
cd WRF ;
vi arch/Config.pl
```

Localize a seguinte linha abaixo e altere de “FALSE” para “TRUE”:

```bash
$I_really_want_to_output_grib2_from_wrf = "TRUE"
```

1. Execute o comando a seguir. Não se esqueça de executar o script que configura as variáveis de ambiente necessárias.

```bash
./configure
```

Você verá várias opções. Escolha a opção que lista o compilador que você está usando e a maneira como deseja construir o WRF (ou seja, em série ou em paralelo).

No caso desse passo a passo, como queremos instalar a versão serial e estamos utilizando os compiladores GNU, a opção é a nº 32. 

1. Selecione a opção 32.
2. Escolha a opção de aninhamento. Nesse caso, escolhemos a 1.

**OBSERVAÇÃO!!**

- No arquivo configure.wrf, existe a seguinte linha:

```bash
FC = time $(SFC)
```

Esse “time” é uma opção de compilação do Fortran que a cada passo da compilação escreve o tempo. Caso esse seja um erro de compilação, tirar essa opção.

- Um outro erro que pode ocorrer na compilação é o WRF buscar o compilador C++, dentro do arquivo *configure.wrf* na seguinte linha:

```bash
CPP = /lib/cpp -P -nostdinc
```

Nesse caso, deve-se corrigir o caminho do compilador.

1. Assim que sua configuração for concluída, você deverá ter um arquivo *configure.wrf*. Para compilar o WRF, você precisará decidir que tipo de caso deseja compilar conforme as opções listadas abaixo:
    
    em_real (3d real case)
    
    em_quarter_ss (3d ideal case)
    
    em_b_wave (3d ideal case)
    
    em_les (3d ideal case)
    
    em_heldsuarez (3d ideal case)
    
    em_tropical_cyclone (3d ideal case)
    
    em_hill2d_x (2d ideal case)
    
    em_squall2d_x (2d ideal case)
    
    em_squall2d_y (2d ideal case)
    
    em_grav2d_x (2d ideal case)
    
    em_seabreeze2d_x (2d ideal case)
    
    em_scm_xy (1d ideal case)/co
    

No nosso caso, estávamos interessados no *em_real*. Para compilar, execute:

```bash
./compile em_real >& log.compile &
```

Uma execução com sucesso retorna a seguinte mensagem (no log.compile):

Executables successfully built

Para checar se os executáveis foram criados, execute:

```bash
ls -ls main/*.exe
```

Para uma compilação de caso real (em_real), os seguintes arquivos devem existir:

wrf.exe → executável do modelo
real.exe → inicialização do real
ndown.exe → aninhamento unidirecional (one-way)
tc.exe → opção apenas para compilações em serial e para tc bogusing

Para uma compilação de caso idealizado, os seguintes arquivos devem existir:

wrf.exe → executável do modelo

ideal.exe → inicialização de caso ideal

Esses executáveis estão ligados a 2 diretórios diferentes e o WRF pode ser executado de quaisquer um deles:

WRF/run

WRF/test/em_real

# Compilando o modelo em modo dmpar

1. Dentro do diretório “Build_WRF”, crie um diretório “dmpar” e navegue até ele.

```bash
mkdir dmpar
cd dmpar
```

**ATENÇÃO!!** Caso a instalação em serial já tenha sido efetuada, pule para o passo 3.

1. Verifique se o programa “git” está instalado executando. 

```bash
which git
```

1. Adquira a versão mais atual do WRF através do comando:

```bash
git clone --recurse-submodules https://github.com/wrf-model/WRF
```

**OBSERVAÇÃO!!** Para versões anteriores, consultar o site: [http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html](http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html)

1. Antes de configurarmos, vamos alterar o arquivo Config.pl para ser possível utilizarmos arquivos do tipo GRIB2, que é o formato dos arquivos do GFS.

```bash
cd WRF ;
vi arch/Config.pl
```

Localize a seguinte linha abaixo e altere de “FALSE” para “TRUE”:

```bash
$I_really_want_to_output_grib2_from_wrf = "TRUE"
```

1. Execute o comando a seguir. Não se esqueça de executar o script que configura as variáveis de ambiente necessárias.

```bash
./configure
```

Você verá várias opções. Escolha a opção que lista o compilador que você está usando e a maneira como deseja construir o WRF (ou seja, em série ou em paralelo).

No caso desse passo a passo, como queremos instalar a versão paralelo *dmpar* e estamos utilizando os compiladores GNU, a opção é a nº 34. 

**OBSERVAÇÃO!!** O *dmpar* funciona tanto para computadores comuns, que têm memória compartilhada, quanto para *clusters*. Já o *smpar* só funciona para computadores comuns.

1. Selecione a opção 34.
2. Escolha a opção de aninhamento. Nesse caso, escolhemos a 1.

**OBSERVAÇÃO!!**

- No arquivo configure.wrf, existe a seguinte linha:

```bash
FC = time $(SFC)
```

Esse time é uma opção de compilação do Fortran que a cada passo da compilação escreve o tempo. Caso esse seja um erro de compilação, tirar essa opção.

- Outro erro que pode ocorrer na compilação é o WRF buscar o compilador C++, dentro do arquivo *configure.wrf* na seguinte linha:

```bash
CPP = /lib/cpp -P -nostdinc
```

Nesse caso, deve-se corrigir o caminho do compilador.

1. Assim que sua configuração for concluída, você deverá ter um arquivo *configure.wrf*. Para compilar o WRF, você precisará decidir que tipo de caso deseja compilar conforme as opções listadas abaixo:
    
    em_real (3d real case)
    
    em_quarter_ss (3d ideal case)
    
    em_b_wave (3d ideal case)
    
    em_les (3d ideal case)
    
    em_heldsuarez (3d ideal case)
    
    em_tropical_cyclone (3d ideal case)
    
    em_hill2d_x (2d ideal case)
    
    em_squall2d_x (2d ideal case)
    
    em_squall2d_y (2d ideal case)
    
    em_grav2d_x (2d ideal case)
    
    em_seabreeze2d_x (2d ideal case)
    
    em_scm_xy (1d ideal case)
    

No nosso caso, estávamos interessados no *em_real*. Para compilar, execute:

```bash
./compile em_real >& log.compile &
```

Uma execução com sucesso retorna a seguinte mensagem (no log.compile):

Executables successfully built

Para checar se os executáveis foram criados, execute:

```bash
ls -ls main/*.exe
```

Para uma compilação de caso real (em_real), os seguintes arquivos devem existir:

wrf.exe → executável do modelo
real.exe → inicialização do real
ndown.exe → aninhamento unidirecional (one-way)
tc.exe → opção apenas para compilações em serial e para tc bogusing

Para uma compilação de caso idealizado, os seguintes arquivos devem existir:

wrf.exe → executável do modelo

ideal.exe → inicialização de caso ideal

Esses executáveis estão ligados a 2 diretórios diferentes e o WRF pode ser executado de quaisquer um deles:

WRF/run

WRF/test/em real

# Compilando o modelo em modo smpar

1. Dentro do diretório “Build_WRF”, crie um diretório “smpar” e navegue até ele.

```bash
mkdir dmpar
cd dmpar
```

**ATENÇÃO!!** Caso a instalação em serial já tenha sido efetuada, pule para o passo 3.

1. Verifique se o programa “git” está instalado executando. 

```bash
which git
```

1. Adquira a versão mais atual do WRF através do comando:

```bash
git clone --recurse-submodules https://github.com/wrf-model/WRF
```

**OBSERVAÇÃO!!** Para versões anteriores, consultar o site: [http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html](http://www2.mmm.ucar.edu/wrf/users/download/get_sources.html)

1. Antes de configurarmos, vamos alterar o arquivo Config.pl para que seja possível utilizarmos arquivos do tipo GRIB2, que é o formato dos arquivos do GFS.

```bash
cd WRF ;
vi arch/Config.pl
```

Localize a seguinte linha abaixo e altere de “FALSE” para “TRUE”:

```bash
$I_really_want_to_output_grib2_from_wrf = "TRUE"
```

1. Execute o comando a seguir. Não se esqueça de executar o scriptque configura as variáveis de ambiente necessárias.

```bash
./configure
```

Você verá várias opções. Escolha a opção que lista o compilador que você está usando e a maneira como deseja construir o WRF (ou seja, em série ou em paralelo).

No caso desse passo a passo, como queremos instalar a versão paralelo s*mpar* e estamos utilizando os compiladores GNU, a opção é a nº 33. 

**OBSERVAÇÃO!!** O *dmpar* funciona tanto para computadores comuns, que têm memória compartilhada, quanto para *clusters*. Já o *smpar* só funciona para computadores comuns.

1. Selecione a opção 33.
2. Escolha a opção de aninhamento. Nesse caso, escolhemos a 1.

**OBSERVAÇÃO!!**

- No arquivo configure.wrf, existe a seguinte linha:

```bash
FC = time $(SFC)
```

Esse *time* é uma opção de compilação do Fortran que a cada passo da compilação escreve o tempo. Caso esse seja um erro de compilação, tirar essa opção.

- Outro erro que pode ocorrer na compilação é o WRF buscar o compilador C++, dentro do arquivo *configure.wrf* na seguinte linha:

```bash
CPP = /lib/cpp -P -nostdinc
```

Nesse caso, deve-se corrigir o caminho do compilador.

1. Assim que sua configuração for concluída, você deverá ter um arquivo *configure.wrf*. Para compilar o WRF, você precisará decidir que tipo de caso deseja compilar conforme as opções listadas abaixo:
    
    em_real (3d real case)
    
    em_quarter_ss (3d ideal case)
    
    em_b_wave (3d ideal case)
    
    em_les (3d ideal case)
    
    em_heldsuarez (3d ideal case)
    
    em_tropical_cyclone (3d ideal case)
    
    em_hill2d_x (2d ideal case)
    
    em_squall2d_x (2d ideal case)
    
    em_squall2d_y (2d ideal case)
    
    em_grav2d_x (2d ideal case)
    
    em_seabreeze2d_x (2d ideal case)
    
    em_scm_xy (1d ideal case)
    

No nosso caso, estávamos interessados no *em_real*. Para compilar, execute:

```bash
./compile em_real >& log.compile &
```

Uma execução com sucesso retorna a seguinte mensagem (no log.compile):

Executables successfully built

Para checar se os executáveis foram criados, execute:

```bash
ls -ls main/*.exe
```

Para uma compilação de caso real (em_real), os seguintes arquivos devem existir:

wrf.exe → executável do modelo
real.exe → inicialização do real
ndown.exe → aninhamento unidirecional (one-way)
tc.exe → opção apenas para compilações em serial e para tc bogusing

Para uma compilação de caso idealizado, os seguintes arquivos devem existir:

wrf.exe → executável do modelo

ideal.exe → inicialização de caso ideal

Esses executáveis estão ligados a 2 diretórios diferentes e o WRF pode ser executado de quaisquer um deles:

WRF/run

WRF/test/em real

Embora existam 3 tipos diferentes de paralelo (smpar, dmpar e dm+sm), temos mais experiência com dmpar e normalmente recomendamos escolher esta opção.

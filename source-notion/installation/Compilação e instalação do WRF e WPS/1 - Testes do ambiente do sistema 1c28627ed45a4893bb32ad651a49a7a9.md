# 1 - Testes do ambiente do sistema

1. O primeiro passo é verificar se os compiladores estão instalados. No caso, dos compiladores GNU execute:

```bash
which gfortran
```

```bash
which cpp
```

```bash
which gcc
```

O retorno de cada um desses comandos será o caminho (*path*) onde estão os executáveis. No caso do cpp o retorno foi: */usr/bin/cpp*

Caso algum compilador não esteja instalado, esse comando retornará uma resposta indicando isso. Nesse caso, o compilador faltante deverá ser instalado.

No caso dos compiladores GNU, o próprio sistema indica como a instalação deve ser feita.

É possível que a versão que será instalada não seja exatamente igual às demais pois esses programas estão em constante desenvolvimento e atualização. Mesmo assim, é necessário se atentar para que o novo compilador instalado não tenha uma versão muito diferente dos demais.

gfortran/cpp/gcc são os comandos para executar cada uma das linguagens. Se a utilização com outras “marcas” de compiladores, deve-se executar o comando which + comando para executar o compilador de preferência. No caso dos compiladores da Intel, seria *which ifort.*

Dependendo da máquina e como foi feita a instalação do Linux, pode estar faltando alguma outra biblioteca, levando a erros nas próximas fases da compilação. Por exemplo, a falta da biblioteca gcc-c++ levou a um erro na instalação do HDF5 que retornava o erro `preprocessor "/lib/cpp" fails sanity check` ao executar o `configure` .

1. Verifique agora as versões de cada compilador executando:

```bash
gfortran --version
```

```bash
cpp --version
```

```bash
gcc --version
```

O retorno desses comandos será a versão instalada como no exemplo abaixo:

GNU Fortran (GCC) 11.4.1 20230605 (Red Hat 11.4.1-2)
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Para a versão atual do WRF (versão 4), é recomendado utilizar compiladores com versão superior à versão 9.

1. Escolha e crie um diretório em que o WRF e o WPS serão instalados. Normalmente o diretório é nomeado de “WRF”.

1. Dentro desse diretório, crie mais dois diretórios: “Build_WRF” e “TESTS”.

1. Realize os testes a seguir para atestar que o compilador fortran está funcionando corretamente e que ele é compatível com o compilador C.

**ATENÇÃO!!** Se algum desses testes falhar, entre em contato com o administrador do sistema da sua instituição para corrigir o problema.

Adquira o conjunto de testes nesse [link](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/Fortran_C_tests.tar) e coloque-o no diretório *TESTS*.

 Para descompactar o arquivo, execute:

```bash
tar -xf Fortran_C_tests.tar
```

São 7 testes. Os testes de 1 a 4 estão relacionados com os compiladores fortran e c. Os testes 5 a 7 estão relacionados a tipos de scripts que o WRF necessita.

**Teste 1** - Execute o seguinte comando:

```bash
gfortran TEST_1_fortran_only_fixed.f
```

Agora execute:

```bash
./a.out
```

Uma execução com sucesso retorna a seguinte mensagem:

SUCCESS test 1 fortran only fixed format

**Teste 2** - Execute o seguinte comando:

```bash
gfortran TEST_2_fortran_only_free.f90
```

Agora execute:

```bash
./a.out
```

Uma execução com sucesso retorna a seguinte mensagem:

Assume Fortran 2003: has FLUSH, ALLOCATABLE, derived 

type, and ISO C Binding

SUCCESS test 2 fortran only free format

**Teste 3** - Execute o seguinte comando:

```bash
gcc TEST_3_c_only.c
```

Agora execute:

```bash
./a.out
```

Uma execução com sucesso retorna a seguinte mensagem:

SUCCESS test 3 c only

**Teste 4** - Execute o seguinte comando:

```bash
gcc -c -m64 TEST_4_fortran+c_c.c
```

Em seguida execute:

```bash
gfortran -c -m64 TEST_4_fortran+c_f.f90
```

Em seguida execute:

```bash
gfortran -m64 TEST_4_fortran+c_f.o TEST_4_fortran+c_c.o
```

Agora execute:

```bash
./a.out
```

Uma execução com sucesso retorna a seguinte mensagem:

C function called by Fortran

Além dos compiladores necessários para gerar os executáveis do WRF, o WRF possui scripts como nível superior para a interface do usuário. É necessário possuir os seguintes sistemas de scritp:

- csh
- perl
- sh

**Teste 5** - Execute o seguinte comando:

```bash
./TEST_csh.csh
```

Uma execução com sucesso retorna a seguinte mensagem:

SUCCESS csh test

**Test 6** - Execute o seguinte comando:

```bash
./TEST_perl.pl
```

Uma execução com sucesso retorna a seguinte mensagem:

SUCCESS perl test

**Test 7** - Execute o seguinte comando:

```bash
./TEST_sh.sh
```

Uma execução com sucesso retorna a seguinte mensagem:

SUCCESS sh test

1. Dentro dos scripts existem alguns comandos UNIX que estão disponíveis independentemente de qual shell é usado. Cheque se os seguintes comandos estão disponíveis, executando-os:

ar             head              sed

awk          hostname      sleep

cat            ln                  sort

cd             ls                  tar

cp             make            touch

cut            mkdir            tr

expr          mv                uname

file             nm                wc

grep          printf             which

gzip           rm                   m4
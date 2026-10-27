# 3 - Testes de compatibilidade de bibliotecas

Esses testes têm como objetivo, verificar se as bibliotecas instaladas são capazes de funcionar com os compiladores que serão usados para as compilações do WPS e do WRF.

**ATENÇÃO!!** Se algum desses testes falhar, entre em contato com o administrador do sistema da sua instituição para corrigir o problema.

1. Adquira o conjunto de testes por meio deste [link](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/Fortran_C_NETCDF_MPI_tests.tar) e descompacte o arquivo para dentro do diretório “TESTS”.

```bash
tar -xf Fortran_C_NETCDF_MPI_tests.tar
```

São 2 testes.

**Teste 1** - Execute o seguinte comando:

```bash
cp ${NETCDF}/include/netcdf.inc .
```

Agora execute:

```bash
gfortran -c 01_fortran+c+netcdf_f.f ;
gcc -c 01_fortran+c+netcdf_c.c ;
gfortran 01_fortran+c+netcdf_f.o 01_fortran+c+netcdf_c.o \
     -L${NETCDF}/lib -lnetcdff -lnetcdf ;
./a.out ;
```

Uma execução com sucesso retorna a seguinte mensagem:

C function called by Fortran

Values are xx = 2.00 and ii = 1

SUCCESS test 1 fortran + c + netcdf

**Teste 2** - Execute o seguinte comando:

```bash
cp ${NETCDF}/include/netcdf.inc .
```

Agora execute:

```bash
mpif90 -c 02_fortran+c+netcdf+mpi_f.f ;
mpicc -c 02_fortran+c+netcdf+mpi_c.c ;
mpif90 02_fortran+c+netcdf+mpi_f.o \
02_fortran+c+netcdf+mpi_c.o \
     -L${NETCDF}/lib -lnetcdff -lnetcdf ;
mpirun ./a.out ;
```

Uma execução com sucesso retorna a seguinte mensagem:

C function called by Fortran

Values are xx = 2.00 and ii = 1

status = 2

SUCCESS test 2 fortran + c + netcdf + mpi
# 2 - Instalando as bibliotecas

1. Navegue até o diretório *Build_WRF* e dentro dele crie o diretório *LIBRARIES.*

```bash
cd Build_WRF
```

```bash
mkdir LIBRARIES
```

```bash
cd LIBRARIES
```

1. Baixe as bibliotecas abaixo dentro do diretório *LIBRARIES:*

[mpich-4.2.0](https://www.mpich.org/static/downloads/4.2.0/mpich-4.2.0.tar.gz)

[netcdf-c-4.9.2](https://downloads.unidata.ucar.edu/netcdf-c/4.9.2/netcdf-c-4.9.2.zip)

[netcdf-fortran-4.6.1](https://downloads.unidata.ucar.edu/netcdf-fortran/4.6.1/netcdf-fortran-4.6.1.tar.gz)

[jasper-1.900.1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/jasper-1.900.1.tar.gz)

[libpng-1.2.50](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/libpng-1.2.50.tar.gz)

[zlib-1.2.11](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/zlib-1.2.11.tar.gz)

[szip-2.1.1](https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz)

[hdf5-1.12.1.8.21](https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.21/src/hdf5-1.8.21.tar)

**ATENÇÃO!!**

É importante compilar e instalar **todas** as bibliotecas com os mesmos compiladores.

1. Antes de instalar as bibliotecas, precisamos configurar uma série de variáveis de ambiente. 
    
    Crie e abra um arquivo com extensão .sh
    
    ```bash
    vi gnu11_env.sh
    ```
    
    Preencha o arquivo da seguinte forma:
    
    ```bash
    #!/bin/bash/
    
    export DIR=/path_to_directory/Build_WRF/LIBRARIES
    export CC=gcc
    export CXX=g++
    export FC=gfortran
    export FCFLAGS=-m64
    export F77=gfortran
    export FFLAGS=-m64
    export JASPERLIB=$DIR/grib2/lib
    export JASPERINC=$DIR/grib2/include
    export LDFLAGS=-L$DIR/grib2/lib
    export CPPFLAGS=-I$DIR/grib2/include
    ```
    
    Lembre-se de configurar os caminhos relacionados ao seu ambiente computacional.
    
    1. Mude a permissão do arquivo para que ele possa ser executado.
    
    ```bash
    chmod 755 gnu11_env.sh
    ```
    
    1. Para executá-lo, faça o seguinte comando:
    
    ```bash
    . $DIR/gnu11_env.sh
    ```
    
    **ATENÇÃO!!**
    
    Lembre-se de executar esse arquivo em todo novo terminal aberto que será utilizado.
    
    Lembre-se de executar o script toda vez que ele for alterado.
    
    1. Crie um novo diretório dentro de *LIBRARIES*. Dentro dele serão instaladas todas as bibliotecas necessárias.
    
    ```bash
    mkdir GNU11
    ```
    
    1. SZIP
    - Descompacte o arquivo baixado do szip e entre no diretório gerado.
    
    ```bash
    tar -xvf szip-2.1.1.tar.gz
    ```
    
    ```bash
    cd szip-2.1.1
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$DIR/GNU11***
    ```
    
    ```bash
    ***make***
    ```
    
    ```bash
    ***make check***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    cd ../
    ```
    
    1. ZLIB
    - Descompacte o arquivo baixado do slib e entre no diretório gerado.
    
    ```bash
    tar -xvf zlib-1.2.11.tar.gz
    ```
    
    ```bash
    cd zlib-1.2.11
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$DIR/GNU11***
    ```
    
    ```bash
    ***make***
    ```
    
    ```bash
    ***make check***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    cd ../
    ```
    
    1. Adicionar ***LD_LIBRARY_PATH,* LDFLAGS** e **CPPFLAGS** ao arquivo gnu11_env.sh
    
    ```bash
    #!/bin/bash/
    
    export DIR=/path_to_directory/Build_WRF/LIBRARIES
    export CC=gcc
    export CXX=g++
    export FC=gfortran
    export FCFLAGS=-m64
    export F77=gfortran
    export FFLAGS=-m64
    export JASPERLIB=$DIR/grib2/lib
    export JASPERINC=$DIR/grib2/include
    export LDFLAGS=-L$DIR/grib2/lib
    export CPPFLAGS=-I$DIR/grib2/include
    export LD_LIBRARY_PATH=$DIR/GNU11/lib:$LD_LIBRARY_PATH
    export LDFLAGS=-L$DIR/GNU11/lib
    export CPPFLAGS=-I$DIR/GNU11/include
    ```
    
    1. HDF5
    - Descompacte o arquivo baixado do hdf5 e entre no diretório gerado.
    
    ```bash
    tar -xvf hdf5-1.8.21.tar
    ```
    
    ```bash
    cd hdf5-1.8.21
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$DIR/GNU11 --enable-fortran \
    --enable-cxx --with-zlib=$DIR/GNU11 \
    --with-szip=$DIR/GNU11***
    
    ```
    
    ```bash
    ***make -j 4***
    ```
    
    ```bash
    ***make check***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    make check-install
    ```
    
    ```bash
    cd ../
    ```
    
    1. Adicionar o ***HDF5*** ao arquivo gnu11_env.sh
    
    ```bash
    #!/bin/bash/
    
    export DIR=/path_to_directory/Build_WRF/LIBRARIES
    export CC=gcc
    export CXX=g++
    export FC=gfortran
    export FCFLAGS=-m64
    export F77=gfortran
    export FFLAGS=-m64
    export JASPERLIB=$DIR/grib2/lib
    export JASPERINC=$DIR/grib2/include
    export LDFLAGS=-L$DIR/grib2/lib
    export CPPFLAGS=-I$DIR/grib2/include
    export LD_LIBRARY_PATH=$DIR/GNU11/lib:$LD_LIBRARY_PATH
    export LDFLAGS=-L$DIR/GNU11/lib
    export CPPFLAGS=-I$DIR/GNU11/include
    export HDF5=$DIR/GNU11
    ```
    
    1. MPICH (necessário caso deseje instalar as versões dmpar e dm + sm)
    - Descompacte o arquivo baixado do mpich e entre no diretório gerado.
    
    ```bash
    tar -xvf mpich-4.2.0.tar.gz
    
    ```
    
    ```bash
    cd mpich-4.2.0
    ```
    
    - Crie um diretório onde o mpich será instalado e navegue até ele. O diretório será criado no diretório-pai do $DIR, e será chamado de $PDIR:
    
    ```bash
    cd $DIR ;
    mkdir ../mpich-4.2.0 ;
    export PDIR=/path_to_directory/Build_WRF/mpich-4.2.0 ;
    cd mpich-4.2.0 
    
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$PDIR/mpich-4.2.0***
    ```
    
    ```bash
    ***make -j 4***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    cd ..
    ```
    
    1. Adicionar o **MPICH** ao arquivo gnu11_env.sh
    
    ```bash
    #!/bin/bash/
    
    export DIR=/path_to_directory/Build_WRF/LIBRARIES
    export CC=gcc
    export CXX=g++
    export FC=gfortran
    export FCFLAGS=-m64
    export F77=gfortran
    export FFLAGS=-m64
    export JASPERLIB=$DIR/grib2/lib
    export JASPERINC=$DIR/grib2/include
    export LDFLAGS=-L$DIR/grib2/lib
    export CPPFLAGS=-I$DIR/grib2/include
    export LD_LIBRARY_PATH=$DIR/GNU11/lib:$LD_LIBRARY_PATH
    export LDFLAGS=-L$DIR/GNU11/lib
    export CPPFLAGS=-I$DIR/GNU11/include
    export HDF5=$DIR/GNU11
    export PDIR=/home/numa23/Public/MPAS/WRF/Build_WRF
    export PATH=$PDIR/mpich-4.2.0/bin:$PATH
    ```
    
    **ATENÇÃO!!**
    
    A nossa compilação do NetCDF-Fortran retornou um erro que parecia ser de incompatibilidade de linguagem da biblioteca com o compilador. Dessa forma, adquirimos a NetCDF-Fortran na versão 4.6.1 do site [https://downloads.unidata.ucar.edu/netcdf/](https://downloads.unidata.ucar.edu/netcdf/).
    
    Às vezes, quando essa manobra não dá certo, pode-se tentar atualizar o compilador para uma versão anterior que seja compatível com a biblioteca.
    
    O que se faz, na verdade, é instalar outra versão separadamente. De preferência fora do diretório do sistema.
    
    Foi feita a configuração que retornou um erro especificando que a NetCDF-C deveria ser uma versão 4.7.4 ou maior.
    
    Adquirimos a NetCDF-C mais atual, versão 4.9.2.
    
    Na configuração da nova NetCDF-C retornou o seguinte erro:
    ”configure: error: curl required for byte range support. Install curl or buld without “***--enable-byterange”***.
    
    O curl já estava instalado, mas de alguma forma não estava sendo suficiente ou a versão era inferior, ou ele não estava enxergando o curl.
    
    A opção foi adicionar “***--disable-byterange***” na linha ”***./configure”.***
    
    A configuração foi realizada e toda a compilação do NetCDF-C correu sem problemas. Em seguida, instalamos o NetCDF-Fortran sem problemas também.
    
    Dessa forma, todo o passo a passo foi atualizado considerando essa observação.
    
    1. NetCDF-C
    - Descompacte o arquivo baixado do NetCDF-C e entre no diretório gerado.
    
    ```bash
    unzip netcdf-c-4.9.2.zip
    ```
    
    ```bash
    cd netcdf-c-4.9.2
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$DIR/GNU11 --disable-dap \
    --with-hdf5=$DIR/GNU11 --enable-netcdf4 \
    LDFLAGS=-L$DIR/GNU11/lib \
    CPPFLAGS=-I$DIR/GNU11/include \
    LD_LIBRARY_PATH=$DIR/GNU11/lib \
    --disable-byterange***
    ```
    
    ```bash
    ***make***
    ```
    
    ```bash
    ***make check***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    cd ../
    ```
    
    1. Adicionar o **NetCDF** ao arquivo gnu11_env.sh
    
    ```bash
    #!/bin/bash/
    
    export DIR=/path_to_directory/Build_WRF/LIBRARIES
    export CC=gcc
    export CXX=g++
    export FC=gfortran
    export FCFLAGS=-m64
    export F77=gfortran
    export FFLAGS=-m64
    export JASPERLIB=$DIR/grib2/lib
    export JASPERINC=$DIR/grib2/include
    export LDFLAGS=-L$DIR/grib2/lib
    export CPPFLAGS=-I$DIR/grib2/include
    export LD_LIBRARY_PATH=$DIR/GNU11/lib:$LD_LIBRARY_PATH
    export LDFLAGS=-L$DIR/GNU11/lib
    export CPPFLAGS=-I$DIR/GNU11/include
    export HDF5=$DIR/GNU11
    export PATH=$PDIR/mpich-4.2.0/bin:$PATH
    export NETCDF=$DIR/GNU11
    export WRFIO_NCD_LARGE_FILE_SUPPORT=1   # suporte a grandes arquivos
    ```
    
    1. NetCDF-Fortran
    - Descompacte o arquivo baixado do NetCDF-Fortran e entre no diretório gerado.
    
    ```bash
    tar -xvf [netcdf-fortran-4.6.1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/netcdf-fortran-4.5.2.tar.gz).tar.gz
    ```
    
    ```bash
    cd [netcdf-fortran-4.](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/netcdf-fortran-4.5.2.tar.gz)6.1
    ```
    
    - Siga as instruções abaixo para configurar, compilar e instalar.
    
    ```bash
    ***./configure --prefix=$DIR/GNU11 --disable-dap \
    --with-hdf5=$DIR/GNU11 --enable-netcdf4 \
    LDFLAGS=-L$DIR/GNU11/lib \
    CPPFLAGS=-I$DIR/GNU11/include \
    LD_LIBRARY_PATH=$DIR/GNU11/lib***
    ```
    
    É possível que algumas dessas diretrizes de configuração não sirvam para o NetCDF Fortran. Mas a tendência é o comando ignorar. Não deve dar erro.
    
    ```bash
    ***make***
    ```
    
    ```bash
    ***make check***
    ```
    
    ```bash
    ***make install***
    ```
    
    ```bash
    cd ../
    ```
    
    1. LIBPNG
- Descompacte o arquivo baixado do libpng e entre no diretório gerado.

```bash
tar -xvf [libpng-1.2.50](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/libpng-1.2.50.tar.gz).tar.gz
```

```bash
cd [libpng-1.2.50](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/libpng-1.2.50.tar.gz)
```

- Siga as instruções abaixo para configurar, compilar e instalar.

```bash
***./configure --prefix=$DIR/GNU11***
```

```bash
***make***
```

```bash
***make check***
```

```bash
***make install***
```

```bash
cd ../
```

1. JASPER
- Descompacte o arquivo baixado do jasper e entre no diretório gerado.

```bash
tar -xvf [jasper-1.900.1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/jasper-1.900.1.tar.gz).tar.gz
```

```bash
cd [jasper-1.900.1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compile_tutorial/tar_files/jasper-1.900.1.tar.gz)
```

- Siga as instruções abaixo para configurar, compilar e instalar.

```bash
***./configure --prefix=$DIR/GNU11***
```

```bash
***make***
```

```bash
***make check***
```

```bash
***make install***
```

```bash
cd ../
```

1. Adicionar o **JASPER** e outras linhas ao arquivo gnu11_env.sh

```bash
#!/bin/bash/

export DIR=/path_to_directory/Build_WRF/LIBRARIES
export CC=gcc
export CXX=g++
export FC=gfortran
export FCFLAGS=-m64
export F77=gfortran
export FFLAGS=-m64
export JASPERLIB=$DIR/grib2/lib
export JASPERINC=$DIR/grib2/include
export LDFLAGS=-L$DIR/grib2/lib
export CPPFLAGS=-I$DIR/grib2/include
export LD_LIBRARY_PATH=$DIR/GNU11/lib:$LD_LIBRARY_PATH
export LDFLAGS=-L$DIR/GNU11/lib
export CPPFLAGS=-I$DIR/GNU11/include
export HDF5=$DIR/GNU11
export PATH=$PDIR/mpich-4.2.0/bin:$PATH
export NETCDF=$DIR/GNU11
export WRFIO_NCD_LARGE_FILE_SUPPORT=1   # suporte a grandes arquivos
export JASPERLIB=$DIR/GNU11/lib
export JASPERINC=$DIR/GNU11/include
ulimit -s unlimited
```
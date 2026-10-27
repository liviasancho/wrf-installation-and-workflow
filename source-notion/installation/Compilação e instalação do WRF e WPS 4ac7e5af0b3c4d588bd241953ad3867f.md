# Compilação e instalação do WRF e WPS

Link de apoio: [https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP2](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP2)

**OBSERVAÇÃO!!**

A compilação e instalação do WRF e WPS, assim como das bibliotecas que eles necessitam, foram realizados em um sistema operacional Rocky Linux 9 e todos os comandos aqui utilizados são aceitos por esse sistema operacional.

Os compiladores usados são todos GNU.

Aplicações em outros sistemas operacionais podem utilizar comandos diferentes, os quais precisam ser adaptados neste passo a passo.

Problemas de compatibilidade das versões das bibliotecas e do WRF podem ocorrer. Dessa maneira, é interessante testar com bibliotecas mais atualizadas ou versões do WRF anteriores a versão atual.

Esse passo a passo prevê que o usuário tenha conhecimentos básicos de Linux.

**ATENÇÃO!!**

- É importante compilar e instalar **todas** as bibliotecas com os mesmos compiladores.
    - No caso desse passo a passo serão os compiladores GNU.
- O mesmo se aplica a compilação de todos os componentes relativos ao modelo WRF.
- Muitos dos problemas de compilação de modelos numéricos estão relacionados com os seguintes pontos:
    - Não compilar tudo o que é necessário (bibliotecas e o modelo) com o mesmo conjunto de compiladores. Essa regra se aplica não só a origem do compilador, mas também com a versão do compilador. Não se pode, por ex., compilar a NetCDF com a versão 8 dos compiladores e o WRF com a versão 11.
    - Para os compiladores (c, fortran, c++), a origem deles importa e deve ser sempre a mesma. É como se eles tivessem “marcas”. A linguagem de programação é a mesma, mas eles funcionam de maneira diferente dependendo da “marca”. Por isso é importante escolher uma “marca” e utilizar **todos** os compiladores daquela mesma “marca” do incío ao fim do processo.
        - Alguns exemplos de compiladores Fortran podem ser encontrados em [https://fortran-lang.org/compilers/](https://fortran-lang.org/compilers/)

[1 - Testes do ambiente do sistema](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/1%20-%20Testes%20do%20ambiente%20do%20sistema%201c28627ed45a4893bb32ad651a49a7a9.md)

[2 - Instalando as bibliotecas](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/2%20-%20Instalando%20as%20bibliotecas%20b8a7d5a0bea848f2b7447cd72042887d.md)

[3 - Testes de compatibilidade de bibliotecas](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/3%20-%20Testes%20de%20compatibilidade%20de%20bibliotecas%20eddf106a042b43de83655e004ba0cc91.md)

[4 - Compilando o WRF](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/4%20-%20Compilando%20o%20WRF%20e4be5112a1944071b40bc86558d6f0a5.md)

[5 - Compilando o WPS](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/5%20-%20Compilando%20o%20WPS%201856d0ac37f0480aa8180dafed85d6ae.md)

[6 - Dados geográficos estáticos](Compila%C3%A7%C3%A3o%20e%20instala%C3%A7%C3%A3o%20do%20WRF%20e%20WPS/6%20-%20Dados%20geogr%C3%A1ficos%20est%C3%A1ticos%207e21696ea633468fb1c8161941ed09c8.md)
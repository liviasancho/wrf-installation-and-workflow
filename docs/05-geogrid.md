# 5. GEOGRID: configure and generate model domains

**Source:** Notion “1 - Geogrid”, including the JSON/YAML and Python utilities.

1. Put `namelist.wps` in the WPS execution directory and configure: `max_dom`, dates, `parent_id`, `parent_grid_ratio`, `i_parent_start`, `j_parent_start`, `e_we`, `e_sn`, `dx`, `dy`, projection, coordinates and `geog_data_path`.
2. Ensure GEOGRID static geographical files exist and that `GEOGRID.TBL` can be found.
3. Run GEOGRID, inspect log and verify one `geo_em.d0*.nc` per domain.

```bash
cd /path/to/WPS
./geogrid.exe >& log.geogrid
grep -i 'successful completion' log.geogrid
ls -lh geo_em.d0*.nc
```

Or use the [safe helper scripts](../scripts/geogrid/README.md):

```bash
python scripts/geogrid/generate_grid.py --wps-dir /path/to/WPS
python scripts/geogrid/plot_domains_geogrid.py --input-dir /path/to/WPS --output domains.png
python scripts/geogrid/correct_truelat1.py /path/to/WPS/geo_em.d01.nc
```

Run these commands from the repository root. Install plotting dependencies with [`environment/geogrid-conda.yml`](../environment/geogrid-conda.yml).

The original JSON is an **illustrative independent domain**, not a default validated science setup. Examine its numeric geometry and output before running WRF. `correct_truelat1.py` performs diagnostics only; changing `truelat1` demands re-running GEOGRID and reviewing the result.


---

## Complete original walkthrough (Rocky Linux 9 / GNU toolchain)

The following procedures are reproduced **in full inside this repository**, based on the tutorials used by the NUMA/LAMCE group. They are in the original Portuguese to preserve precise instructions and historical troubleshooting. Replace machine-specific paths and check versions before executing. The current commands in the first part of this chapter are the portable orientation; the reproduced procedures below provide the detailed commands.


### Original procedure: 1 - Geogrid

# 1 - Geogrid

Em caso de dúvidas, utilizar o site de boas práticas e o tutorial:

[https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html](https://www2.mmm.ucar.edu/wrf/users/namelist_best_prac_wps.html)

[https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/compilation_tutorial.php#STEP1)

Os arquivos extras citados estão em anexo no fim da página.

Os domínios são configurados através do namelist.wps do WPS

Quando o WRF é compilado, ele gera um namelist.wps padrão.

A ideia é alterar esse namelist original para manter o padrão que o WRF já entende.

1. Copie esse namelist original para ter um namelist que não seja alterado. **Esse passo só deve ser executado 1x.**

```bash
cp ~/WRF/Build_WRF/serial/WPS/namelist.wps ~/WRF/Build_WRF/serial/WPS/ORI_namelist.wps
```

A ideia é sempre copiar o namelist (namelist.wps) para a sua pasta de interesse a alterar de lá. E caso ocorra algum erro nesse processo (caso esqueça de fazer essa cópia), o ORI_namelist.wps estará intacto.

1. Copie o namelist.wps para o seu diretório de interesse e modifique-o conforme o seu objetivo.
- A quantidade de domínios é definida pela variável *max_dom*.
- Para o caso de mais de um domínio, é necessário indicar qual é a grade mãe de cada domínio na variável *parent_id*.
- Para obter grades mais resolutas é necessário aninhar os domínios, com a razão entre as resoluções das grades (resolução da grade mãe/resolução da grade filha) sendo ímpar e menor que 7. Essa razão é definida pela variável *parent_grid_ratio*.

- Para definir a posição das grades aninhadas em relação à grade mãe são usadas as variáveis *i_parent_start* e *j_parent_start*.
- A melhor prática é manter cerca de 1/3 da grade mãe de distância dos limites da grade aninhada e 1/3 da grade de distância da região de interesse. Além de evitar que os limites passem por regiões muito elevadas.
- A quantidade de pontos em cada direção é definida por *e_we* e *e_sn*. Deve-se usar o mínimo de 100 pontos para cada domínio. Como 10 pontos em cada lado fazem parte da zona de fronteira, os domínios devem ser extensos o suficiente para que as grades aninhadas e a área de interesse nunca caiam dentro desses 10 pontos. Além disso, a quantidade de pontos menos um deve ser divisível pela razão entre as grades.
- A resolução horizontal da grade menos resoluta é definida em metros nas variáveis *dx* e *dy*, enquanto para as grades aninhadas é calculada a partir do *parent_grid_ratio*. Deve ser no máximo um décimo da resolução das condições iniciais e de contorno.
- A projeção do mapa ideal para latitude baixas é a de Mercator, que pode ser definida na variável *map_proj*.
- O ponto central do domínio mais externo é definido nas variáveis *ref_lat,* *ref_lon* e *stand_lon*, com *stand_lon* igual ao *ref_lon*.
- Lembre-se de verificar se o caminho do *geog_data_path* está configurado. A melhor prática é adicionar no PATH.
- A variável *truelat1* representa a latitude verdadeira e inicialmente deve ser usado o mesmo valor de *ref_lat* para rodar o geogrid.exe. Porém, com o arquivo *geo_em.d01.nc* podemos estimar o quanto os valores máximos e mínimos do fator escala de mapa se distanciaram do valor ideal (1 unidade). Com base nessa informação, podemos alterar o valor de *truelat1* até que a distorção do fator escala de mapa seja a menor possível.

1. Gere um link do executável do geogrid no diretório desejado:

```bash
ln -s ~/WRF/Build_WRF/serial/WPS/geogrid.exe geogrid.exe
```

1. Rode o geogrid e jogue o resultado para um log:

```bash
./geogrid.exe >& log.geogrid
```

**ATENÇÃO!!** A minha execução falhou com o seguinte erro: *ERROR: Could not open GEOGRID.TBL*. Tive que configurar o caminho até o diretório do GEOGRID.TBL no namelist na opção *opt_geogrid_tbl_path*.

Uma execução bem-sucedida retornará a mensagem:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!  Successful completion of geogrid.  !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

1. Caso dê tudo certo, rode o script para gerar a figura dos domínios. Essa figura nos ajuda a entender se os domínios estão exatamente onde queremos.
    1. Para rodar esse script, gera um ambiente no anaconda. O ambiente pode ser criado com o arquivo *env_cria_grades_wrf.yml*. **Esse passo só deve ser executado 1x.**
    2. Ative o ambiente Anaconda criado e abra o script *plot_domains_geogrid.py*.
    3. Altere a linha que começa com *input_path* para o diretório onde estão os arquivos gerados pelo geogrid. Esses arquivos têm nomes no padrão *geo_em.d0*.nc*.
    4. Se quiser, altere o nome da figura que será gerada na linha que começa com *plt.savefig*.
    5. Salve e feche o arquivo.
    6. Execute o arquivo *plot_domains_geogrid.py*.

1. Avalie a figura e os domínios criados.
    
    Caso necessite alterar alguns parâmetros do domínio, repita os processos 1, 3 e 4 até atingir o objetivo.
    
    Lembrar de evitar que os limites da grade atravessem maciços e áreas mais elevadas para não causar problemas numéricos.
    

**ALTERNATIVA USANDO SCRIPTS PYTHON**

O script em Python *create_namelist_wps.py* calcula o tamanho e a posição das grades com base em algumas informações iniciais e escreve o arquivo *namelist.wps*. As informações iniciais, como as coordenadas extremas da área de interesse e o número de domínios desejados, devem ser fornecidas no arquivo namelist_wps.json.

Já o script *generate_grid.py* utiliza o script *create_namelist_wps.py* para criar a grade, executa o *geogrid.exe* e, em seguida, executa o arquivo *plot_domains_geogrid.py.*

Para que esses scripts funcionem, o ambiente Anaconda, com todas as bibliotecas necessárias para rodar o script *plot_domains_geogrid.py*, deve estar ativo.

1. Com o domínio criado conforme os objetivos propostos, deve-se agora avaliar e corrigir o item *truelat1* do namelist.  O script correct_truelat1.py utiliza as informações do namelist.wps e do arquivo geo_em.d01.nc para buscar o melhor valor de truelat1 mais rapidamente; porém, cabe ao usuário fornecer os novos valores de truelat1 para teste.

[namelist_wps.json](1%20-%20Geogrid/namelist_wps.json)

[aux_func.py](1%20-%20Geogrid/aux_func.py)

[create_namelist_wps.py](1%20-%20Geogrid/create_namelist_wps.py)

[generate_grid.py](1%20-%20Geogrid/generate_grid.py)

[env_cria_grades_wrf.yml](1%20-%20Geogrid/env_cria_grades_wrf.yml)

[plot_domains_geogrid.py](1%20-%20Geogrid/plot_domains_geogrid.py)

[correct_truelat1.py](1%20-%20Geogrid/correct_truelat1.py)

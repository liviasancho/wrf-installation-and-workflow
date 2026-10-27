import xarray as xr
import os
import json
from aux_func import terminal
# Importar tipo Dataset do xarray
from xarray import Dataset
from typing import Dict

# Diretorio onde esta o namelist e o arquivo geo_em.d01.nc
os.chdir('/home/numa15/Documents/Livia/Projetos/WRF/teste_rodar_serial_paralelo')

def map_factor_info(
        dado: Dataset,
        truelat1_orig: float
) -> Dict[str, Dict[str, float]]:
    """
    Extrai valores máximos e mínimos do fator de escala do arquivo geo_em.d01.nc, 
    calcula a diferença entre eles e o valor ideal de fator de escala e
    salva as informações em um dicionário
    """
    str_truelat1_orig = str(truelat1_orig)
    fator_escala_mapa = {str_truelat1_orig: {}}
    # Selecionando os factores de escala do mapa máximo e mínimo do ponto central
    fator_escala_mapa[str_truelat1_orig]['max'] = dado['MAPFAC_M'].max(
    ).values.item()
    fator_escala_mapa[str_truelat1_orig]['min'] = dado['MAPFAC_M'].min(
    ).values.item()
    # Calculando a distancia entre os factores de escala máximo e mínimo e o valor ideal
    fator_escala_mapa[str_truelat1_orig]['1-x'] = 1 - \
        fator_escala_mapa[str_truelat1_orig]['min']
    fator_escala_mapa[str_truelat1_orig]['x-1'] = fator_escala_mapa[str_truelat1_orig]['max'] - 1
    # Calculando a diferença entre a distancia do valor ideal máximo e mínimo
    fator_escala_mapa[str_truelat1_orig]['diferenca'] = fator_escala_mapa[str_truelat1_orig]['1-x'] - \
        fator_escala_mapa[str_truelat1_orig]['x-1']
    return fator_escala_mapa


def verificar_valor_historico(
        truelat1: float
        ) -> bool:
    """
    Verifica se o valor de truelat1 já foi registrado no arquivo json de fator de escala
    """
    if not os.path.isfile('fator_escala_mapa.json'):
        return False
    with open('fator_escala_mapa.json') as f:
        fator_escala_mapa = json.load(f)
    if str(truelat1) in fator_escala_mapa.keys():
        return True
    return False


def salvar_json_fator_escala(
        fator_escala_mapa: Dict[str, Dict[str, float]]
        ) -> None:
    """
    Salva o fator de escala do mapa em um arquivo json conforme novas entradas de truelat1
    """
    if not os.path.isfile('fator_escala_mapa.json'):
        with open('fator_escala_mapa.json', 'w') as f:
            json.dump(fator_escala_mapa, f)
            print('Arquivo falor_escala_mapa.json criado com sucesso')
    else:
        with open('fator_escala_mapa.json') as f:
            # Carregando o arquivo json com as informações já existentes
            fator_escala_mapa_old = json.load(f)
            # Atualizando o dicionário com os novos valores
            fator_escala_mapa_old.update(fator_escala_mapa)
        # Salvar informações em um arquivo json
        with open('fator_escala_mapa.json', 'w') as f:
            json.dump(fator_escala_mapa_old, f)


def processar_fator_escala():
    """
    Processa o fator de escala do mapa e salva as informações em um arquivo json
    """
    dado = xr.open_dataset('geo_em.d01.nc')
    truelat1_orig = dado.attrs['TRUELAT1']

    if verificar_valor_historico(truelat1_orig):
        print(f'Fator de escala de truelat1 = {str(truelat1_orig)} já registrado')
    else:
        fator_escala_mapa = map_factor_info(dado, truelat1_orig)
        print(fator_escala_mapa)
        salvar_json_fator_escala(fator_escala_mapa)


processar_fator_escala()

continue_execution = True
while continue_execution:
    new_truelat1 = float(input('Digite o valor de truelat1: '))
    if verificar_valor_historico(new_truelat1):
        print(f'Fator de escala de truelat1 = {str(new_truelat1)} já registrado')
    else:
        # Atualizar o valor de truelat1 no arquivo namelist.wps
        with open('namelist.wps') as f:
            # abrir arquivo de texto
            namelist_wps = f.read()

        # Separar string em lista pelas quebras de linha
        namelist_wps = namelist_wps.split('\n')
        # Atualizar o valor de truelat1
        namelist_wps_novo = [f' truelat1 = {new_truelat1},' if "truelat1" in string else string for string in namelist_wps]
        namelist_wps_novo = '\n'.join(namelist_wps_novo)

        # Salvar o novo namelist.wps
        with open('namelist.wps', 'w') as f:
            f.write(namelist_wps_novo)

        # Rodar o geogrid.exe
        terminal('./geogrid.exe', verbose=True)

        # Processar o fator de escala
        processar_fator_escala()
    # Perguntar se deseja continuar
    continue_execution = input('Deseja continuar? (S/N) ').upper() == 'S'

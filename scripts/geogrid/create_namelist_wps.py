import json
import geopy.distance as gd
import numpy as np
from typing import List, Tuple


def compute_area_dimensions(
        lat_n: float | int,
        lat_s: float | int,
        lon_e: float | int,
        lon_w: float | int
) -> Tuple[int, int]:
    """
    Calcular a extensão da área de interesse em km em x e y
    """
    # Calcular extensão x em km
    x_dimension_km = round(gd.distance(
        (lat_n, lon_e), (lat_n, lon_w)).km)
    # Calcular extensão y em km
    y_dimension_km = round(gd.distance(
        (lat_n, lon_e), (lat_s, lon_e)).km)
    return int(x_dimension_km), int(y_dimension_km)


def compute_center_coordinates(
        lat_n: float | int,
        lat_s: float | int,
        lon_e: float | int,
        lon_w: float | int
) -> Tuple[float, float]:
    # Calcular ponto central da área de interesse
    latitude_midpoint = np.mean([lat_n, lat_s])
    longitude_midpoint = np.mean([lon_e, lon_w])
    return latitude_midpoint, longitude_midpoint


def compute_grid_resolutions(
        parent_grid_ratio: List[int],
        parent_grid_resolution: int
) -> List[int]:
    """
    Calcula a resolução em km de cada grade em cada domínio em km a partir da resolução da grade mãe.
    Retorna uma lista na ordem da pior resolução para a melhor.
    """
    grids_resolutions = [parent_grid_resolution/(1000*parent_grid_ratio[i]*parent_grid_ratio[i-1])
                         if i > 0 else parent_grid_resolution/(1000*parent_grid_ratio[0])
                         for i in range(len(parent_grid_ratio))]
    return grids_resolutions


def estimate_domain_size_km(
        interest_area_size: int,
        domain_area_extent_ratio: int | float,
        parent_grid_ratio: int | float
) -> List[int]:
    """
    Função que calcula a extensão em km de cada grade em cada domínio.
    Retorna uma lista na ordem da pior resolução para a melhor.
    """
    domains_size = [(interest_area_size * domain_area_extent_ratio * parent_grid_ratio[i])
                    if i == 0 else (interest_area_size * domain_area_extent_ratio * parent_grid_ratio[i] * parent_grid_ratio[i-1])
                    for i in range(len(parent_grid_ratio))[::-1]]

    return domains_size


def adjust_num_points(
        number_of_points: int,
        parent_grid_ratio: int
) -> int:
    """
    Função que testa se o número de pontos é múltiplo da razão de refinamento da grade
    """
    if (number_of_points - 1) % parent_grid_ratio == 0:
        return number_of_points
    while (number_of_points - 1) % parent_grid_ratio != 0:
        number_of_points = number_of_points + 1
        if (number_of_points - 1) % parent_grid_ratio == 0:
            return int(number_of_points)
            break


def estimate_number_of_points(
        domains_size: List[int],
        grid_resolutions: List[int],
        parent_grid_ratio: int
) -> List[int]:
    """
    Função que calcula o número de pontos em uma grade em função da extensão e resolução
    """
    number_of_points = [round(domains_size[i]/grid_resolutions[i])
                        for i in range(len(domains_size))]
    return [adjust_num_points(number_of_points[i], parent_grid_ratio[i]) for i in range(len(number_of_points))]


def adjust_domain_size(
        number_of_points: List[int],
        grid_resolutions: List[int]
) -> List[int]:
    """
    Função que recalcula a extensão da grade em função do número de pontos e resolução
    """
    domain_size = [number_of_points[i] * grid_resolutions[i]
                   for i in range(len(number_of_points))]
    return domain_size


def estimate_nested_grid_positions(grid_extensions: List[int],
                                   parent_grid_resolutions: List[int]
                                   ) -> List[int]:
    """
    Função que calcula a posição da grade aninhada em relação à grade mãe,
    em função do número de pontos e resolução de cada grade.
    Retorna uma lista na ordem da pior resolução para a melhor.
    """
    nested_grid_positions = [round((grid_extensions[i-1] - grid_extensions[i]) / (2 * parent_grid_resolutions[i-1]))
                             if i > 0 else 1
                             for i in range(len(grid_extensions))]
    return nested_grid_positions

def list_to_string(
        inputList: List[int]
) -> str:
    """
    Função que retorna uma lista como string
    """
    return ', '.join([str(item) for item in inputList])


def create_namelist_wps():
    # Abrir arquivo namelist_wps.json com as configurações iniciais do WPS
    with open('namelist_wps.json') as f:
        namelist_wps = json.load(f)

    parent_grid_ratio = namelist_wps['geogrid']['parent_grid_ratio']
    domain_area_extent_ratio = namelist_wps['extra']['domain_area_extent_ratio']
    max_dom = namelist_wps["share"]["max_dom"]

    lat_n = namelist_wps['extra']['lat_n']
    lat_s = namelist_wps['extra']['lat_s']
    lon_e = namelist_wps['extra']['lon_e']
    lon_w = namelist_wps['extra']['lon_w']

    parent_grid_dx = namelist_wps['geogrid']['dx']
    parent_grid_dy = namelist_wps['geogrid']['dy']

    # Criar lista com resoluções horizontais em km em cada domínio da melhor resolução para a pior
    grid_resolutions_km_x = compute_grid_resolutions(parent_grid_ratio,
                                                     parent_grid_dx)
    grid_resolutions_km_y = compute_grid_resolutions(parent_grid_ratio,
                                                     parent_grid_dy)

    # Definir extensão da área de interesse
    interest_area_size_x, interest_area_size_y = compute_area_dimensions(lat_n, lat_s,
                                                                         lon_e, lon_w)

    print(f'A extensão da área em x é de {interest_area_size_x} e em y é de {interest_area_size_y}')
    # Definir ponto central da área de interesse
    latitude_midpoint, longitude_midpoint = compute_center_coordinates(lat_n, lat_s,
                                                                       lon_e, lon_w)

    # Criar lista com extensões horizontais em km em cada domínio da melhor resolução para a pior
    domain_size_extentions_x = estimate_domain_size_km(interest_area_size_x,
                                                       domain_area_extent_ratio,
                                                       parent_grid_ratio)
    domain_size_extentions_y = estimate_domain_size_km(interest_area_size_y,
                                                       domain_area_extent_ratio,
                                                       parent_grid_ratio)

    # Criar lista com número de pontos em cada domínio da melhor resolução para a pior
    number_of_point_x = estimate_number_of_points(domain_size_extentions_x,
                                                  grid_resolutions_km_x,
                                                  parent_grid_ratio)
    number_of_points_y = estimate_number_of_points(domain_size_extentions_y,
                                                   grid_resolutions_km_y,
                                                   parent_grid_ratio)

    # Ajustar extensão da grade em função do número de pontos e resolução
    domain_size_extentions_x = adjust_domain_size(number_of_point_x,
                                                  grid_resolutions_km_x)
    domain_size_extentions_y = adjust_domain_size(number_of_points_y,
                                                  grid_resolutions_km_y)

    # Criar lista com posições dos pontos em cada domínio da melhor resolução para a pior
    grid_positions_x = estimate_nested_grid_positions(domain_size_extentions_x,
                                                      grid_resolutions_km_x)
    grid_positions_y = estimate_nested_grid_positions(domain_size_extentions_y,
                                                      grid_resolutions_km_y)

    for i in range(max_dom):
        print(f'O domínio {i+1} de extensão {domain_size_extentions_x[i]}x{domain_size_extentions_y[i]} terá {number_of_point_x[i]}x{number_of_points_y[i]} pontos, com a grade começando em {grid_positions_x[i]} e {grid_positions_y[i]}')


    with open('namelist.wps', 'w') as f:
        # Escrever seção share
        f.write('&share\n')

        f.write(f" wrf_core = 'ARW',\n")
        f.write(f' max_dom = {max_dom},\n')
        f.write(f' start_date = {", ".join(namelist_wps["share"]["start_date"])},\n')
        f.write(f' end_date = {", ".join(namelist_wps["share"]["end_date"])},\n')
        f.write(f' interval_seconds = {namelist_wps["share"]["interval_seconds"]},\n')

        f.write('/\n')
        f.write('\n')

        f.write('&geogrid\n')

        f.write(f' parent_id = {list_to_string(namelist_wps["geogrid"]["parent_id"])},\n')
        f.write(f' parent_grid_ratio = {list_to_string(parent_grid_ratio)},\n')
        f.write(f' i_parent_start = {list_to_string(grid_positions_x)},\n')
        f.write(f' j_parent_start = {list_to_string(grid_positions_y)},\n')
        f.write(f' e_we = {list_to_string(number_of_point_x)},\n')
        f.write(f' e_sn = {list_to_string(number_of_points_y)},\n')
        f.write(f' geog_data_res = {list_to_string(namelist_wps["geogrid"]["geog_data_res"])},\n')
        f.write(f' dx = {parent_grid_dx},\n')
        f.write(f' dy = {parent_grid_dy},\n')
        f.write(f' map_proj = {namelist_wps["geogrid"]["map_proj"]},\n')
        f.write(f' ref_lat = {latitude_midpoint},\n')
        f.write(f' ref_lon = {longitude_midpoint},\n')
        f.write(f' truelat1 = {latitude_midpoint},\n')
        f.write(f' truelat2 = 0,\n')
        f.write(f' stand_lon = {longitude_midpoint},\n')
        f.write(f' geog_data_path = {namelist_wps["geogrid"]["geog_data_path"]},\n')
        f.write(f' opt_geogrid_tbl_path = {namelist_wps["geogrid"]["opt_geogrid_tbl_path"]},\n')

        f.write('/\n')
        f.write('\n')

        f.write('&ungrib\n')
        f.write(f' out_format = WPS,\n')
        f.write(f' prefix = FILE,\n')

        f.write('/\n')
        f.write('\n')

        f.write('&metgrid\n')
        f.write(f' fg_name = FILE,\n')
        f.write(f' io_form_metgrid = 2,\n')
        f.write(f' opt_metgrid_tbl_path = {namelist_wps["metgrid"]["opt_metgrid_tbl_path"]},\n')

        f.write('/')

    print('Arquivo namelist.wps criado com sucesso!')


if __name__ == '__main__':
    import argparse
    import os
    import shutil
    import tempfile
    from pathlib import Path

    parser = argparse.ArgumentParser(description='Generate a preliminary WPS namelist from the tutorial JSON. Review geometry before using.')
    parser.add_argument('--config', type=Path, required=True, help='JSON configuration from the tutorial')
    parser.add_argument('--output', type=Path, required=True, help='Location for generated namelist.wps')
    parser.add_argument('--overwrite', action='store_true', help='Allow replacing an existing output file')
    args = parser.parse_args()
    configuration = args.config.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not configuration.is_file():
        parser.error(f'Configuration not found: {configuration}')
    if output.exists() and not args.overwrite:
        parser.error(f'Output already exists: {output}. Use --overwrite to replace.')
    cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix='wrf-namelist-') as tmp:
        work = Path(tmp)
        shutil.copyfile(configuration, work / 'namelist_wps.json')
        try:
            os.chdir(work)
            create_namelist_wps()
        finally:
            os.chdir(cwd)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / 'namelist.wps', output)
    print(f'Preliminary namelist saved at {output}; review domain geometry and paths.')

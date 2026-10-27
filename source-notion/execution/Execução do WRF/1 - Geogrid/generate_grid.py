from aux_func import terminal
import create_namelist_wps
# Rodar script que define os pontos de grade e posição da grade aninhada
create_namelist_wps.create_namelist_wps()

# Excluir arquivos antigos do geogrid
terminal('rm -r geo_em.d0*')
# Rodar geogrid.exe
terminal('geogrid.exe', verbose=True)

# Executar script para plotar a grade
terminal('python plot_domains_geogrid.py', verbose = True)


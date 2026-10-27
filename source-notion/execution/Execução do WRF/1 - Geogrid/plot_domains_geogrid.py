# -*- Coding: UTF-8 -*-

# Last update: 28/11/2022

import os, sys, glob
from turtle import color
import numpy as np
import xarray as xr
import netCDF4 as nc
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.patches as patches
import cartopy.crs as crs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature, NaturalEarthFeature, LAND, COASTLINE, STATES, OCEAN
from cartopy.io.shapereader import Reader
import geopandas as gpd

# Path files
input_path ='./'
os.chdir(input_path)
geo_files = sorted(glob.glob('geo_em.d0*.nc'))
#Shapefile
#Filtrando o poligono do municipio
#shape = gpd.read_file('C:\\Users\\mauri\\OneDrive\\Área de Trabalho\\Lab\\Uteis\Shapes\\RMs\\GEOFT_REGIAO_METROPOLITANA.shp')
#shape_filtrado = shape.query("RME_NM == 'Rio de Janeiro'")
#shape = 'C:\\Users\\mauri\\OneDrive\\Área de Trabalho\\Lab\\Uteis\Shapes\\RMs\\GEOFT_REGIAO_METROPOLITANA.shp'

fig = plt.figure(figsize=(12,6))
ax = plt.axes(projection=crs.PlateCarree())
states = cfeature.NaturalEarthFeature(category="cultural", scale="50m", facecolor="none", name="admin_1_states_provinces_lines")
ax.add_feature(states, linewidth=1, edgecolor="gray", zorder=2)
ax.coastlines('10m', linewidth=1, color='black', zorder=4)
ax.add_feature(cfeature.BORDERS, linewidth=1, edgecolor="black", zorder=3)
ax.add_feature(OCEAN, edgecolor='k', facecolor='lightblue', zorder=5)
#shape_feature = ShapelyFeature(shape_filtrado.geometry, crs.PlateCarree(), facecolor='none',  linewidth=1.0, edgecolor="black")
#ax.add_feature(shape_feature)

clevs = np.linspace(0,2000,200)
blevs = np.linspace(0,2000,11)
for file in geo_files:
    domain = str(file)[7:10]
    ncfile = nc.Dataset(file)
    # reading resolution
    dx = str(ncfile.getncattr('DX') / 1000.0)+' km'

    s_lat = np.min(ncfile['XLAT_M'][:])
    n_lat = np.max(ncfile['XLAT_M'][:])
    w_lon = np.min(ncfile['XLONG_M'][:])
    e_lon = np.max(ncfile['XLONG_M'][:])

    if file == geo_files[0]:
        lats = ncfile.variables['XLAT_M'][0,:,0]
        lons = ncfile.variables['XLONG_M'][0,0,:]
        topo = ncfile.variables['HGT_M'][0,:,:]
        plt.contourf(np.array(lons[:]), np.array(lats[:]), np.array(topo[:,:]),  levels=clevs, cmap='terrain', zorder=1)
        plt.colorbar(ax=ax, shrink=1., aspect=25, orientation='vertical', ticks=blevs, pad=0.03)
        # ploting label 'd0?: ?? km'
        plt.text(e_lon-4.5, s_lat+0.09, domain+': '+dx, fontsize=9, color='red', zorder=6) 
    else:
        # Create a Rectangle patch
        poligono = patches.Polygon([(w_lon,s_lat),(w_lon,n_lat),(e_lon,n_lat),(e_lon,s_lat)], closed=True, linewidth=1.5, edgecolor='r', facecolor='none', zorder=5)
        ax.add_patch(poligono)
        plt.text(e_lon-1.7, s_lat-0.25, domain+': '+dx, fontsize=9, color='red', zorder=6) 
# plt.text(e_lon-4.5, s_lat+0.09, domain+': '+dx, fontsize=9, color='red', zorder=6)
        
    # Plotando ponto com erro cfl. 
    # A ideia aqui é fixar apenas a grade de interesse na parte superior do codigo e plotar
    #plt.text(lons[64], lats[115], 'cfl', horizontalalignment='center', verticalalignment='center', fontsize=9, color='red')

# # Create a Rectangle patch
# poligono = patches.Polygon([(-41.32,-22.62),(-41.32,-21.8),(-40.55,-21.8),(-40.55,-22.62)], closed=True, linewidth=1.5, edgecolor='black', facecolor='none', zorder=5)
# ax.add_patch(poligono)
#plt.text(-40.55-4.5, -22.62+0.09, 'RJ-3 + Açu', fontsize=9, color='black', zorder=7) 
# plt.text(-40.5, -22.62+0.5, 'RJ-3 + Açu', fontsize=9, color='black', zorder=7) 

# # Plotar ponto no ponto central
# ax.scatter(-40.935, -22.21, zorder= 8)

ax.set_xticks(np.linspace(lons[0],lons[-1],5), minor=False, crs=crs.PlateCarree())
ax.set_yticks(np.linspace(lats[0],lats[-1],5), minor=False, crs=crs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True, number_format='.0f')
lat_formatter = LatitudeFormatter(number_format='.0f')
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.savefig('grade_teste_serial_dmpar.png', dpi=300, bbox_inches='tight')
#plt.show()


#etopo = xr.open_dataset('C:\\Users\\mauri\\OneDrive\\Área de Trabalho\\Lab\\Uteis\\ETOPO\\ETOPO1_Ice_g_gdal.grd.gz')
#spacing   = etopo['spacing'].values
#x_range   = etopo['x_range'].values
#y_range   = etopo['y_range'].values
#dimension = etopo['dimension'].values
#z = etopo['z'][:]
#print(z)
#longitude = x_range[0] + spacing[0] * np.arange(dimension[0])
#latitude  = y_range[0] + spacing[1] * np.arange(dimension[1])
#
#plt.contourf(np.array(longitude), np.array(latitude), np.array(z[:]),  cmap='terrain', zorder=1)
#plt.show()

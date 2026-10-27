#!/usr/bin/env python3
"""Plot a preview of WPS geo_em domains; requires netCDF4, matplotlib, cartopy."""
import argparse
from pathlib import Path
import numpy as np
from netCDF4 import Dataset
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir', type=Path, default=Path('.'))
    p.add_argument('--output', type=Path, default=Path('domains.png'))
    a = p.parse_args()
    files = sorted(a.input_dir.glob('geo_em.d0*.nc'))
    if not files: p.error('No geo_em.d0*.nc files found')
    fig, ax = plt.subplots(figsize=(11, 7), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines(resolution='110m', linewidth=.8)
    ax.add_feature(cfeature.BORDERS, linewidth=.5)
    for idx, filename in enumerate(files):
        with Dataset(filename) as ds:
            lat = np.asarray(ds.variables['XLAT_M'][0])
            lon = np.asarray(ds.variables['XLONG_M'][0])
            if idx == 0 and 'HGT_M' in ds.variables:
                topo = np.asarray(ds.variables['HGT_M'][0])
                mesh = ax.pcolormesh(lon, lat, topo, transform=ccrs.PlateCarree(), shading='auto', cmap='terrain')
                fig.colorbar(mesh, ax=ax, label='Terrain elevation (m)', shrink=.65)
            outline = [(lon[0,0], lat[0,0]), (lon[0,-1],lat[0,-1]), (lon[-1,-1],lat[-1,-1]),(lon[-1,0],lat[-1,0]),(lon[0,0],lat[0,0])]
            ax.plot([x[0] for x in outline], [x[1] for x in outline], linewidth=2, transform=ccrs.PlateCarree(), label=filename.stem)
    ax.legend(loc='best')
    ax.set_title('WRF geographical domains (GEOGRID)')
    a.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.output, bbox_inches='tight', dpi=180)
    print(f'Saved {a.output}')

if __name__ == '__main__': main()

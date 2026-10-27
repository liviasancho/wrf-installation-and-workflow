#!/usr/bin/env python3
"""Read-only MAPFAC_M inspection to help assess TRUELAT1 choices."""
import argparse
from pathlib import Path
import json
from netCDF4 import Dataset
import numpy as np

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('geo_em', type=Path, help='geo_em.d01.nc produced by GEOGRID')
    p.add_argument('--output', type=Path, default=None, help='Optional JSON report')
    a = p.parse_args()
    with Dataset(a.geo_em) as ds:
        m = np.asarray(ds.variables['MAPFAC_M'][:])
        result = {'source': str(a.geo_em), 'truelat1': float(ds.getncattr('TRUELAT1')),
                  'mapfac_min': float(np.nanmin(m)), 'mapfac_max': float(np.nanmax(m)),
                  'max_absolute_deviation_from_1': float(np.nanmax(np.abs(m-1)))}
    report = json.dumps(result, indent=2)
    print(report)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(report+'\n')
    print('This tool does NOT optimize or modify truelat1; test candidates through GEOGRID.')

if __name__ == '__main__': main()

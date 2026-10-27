#!/usr/bin/env python3
"""Run the GEOGRID executable and optionally plot the domains; never delete data."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--wps-dir', type=Path, required=True, help='Directory containing namelist.wps and geogrid.exe')
    p.add_argument('--plot', action='store_true', help='Plot geo_em files after a successful run')
    p.add_argument('--overwrite', action='store_true', help='Allow rerun when geo_em files exist (keep backups yourself)')
    a = p.parse_args()
    d = a.wps_dir.expanduser().resolve()
    if not (d/'namelist.wps').is_file():
        p.error(f'Missing {d / "namelist.wps"}')
    if not (d/'geogrid.exe').exists():
        p.error(f'Missing {d / "geogrid.exe"}')
    old = sorted(d.glob('geo_em.d0*.nc'))
    if old and not a.overwrite:
        p.error('Existing geo_em files detected. Back them up, then use --overwrite to rerun.')
    with (d/'log.geogrid').open('w') as log:
        res = subprocess.run([str(d/'geogrid.exe')], cwd=d, stdout=log, stderr=subprocess.STDOUT, check=False)
    if res.returncode:
        sys.exit(f'GEOGRID exited {res.returncode}. Inspect {d / "log.geogrid"}')
    print(f'GEOGRID finished; inspect {d / "log.geogrid"} and geo_em files')
    if a.plot:
        script = Path(__file__).with_name('plot_domains_geogrid.py')
        subprocess.run([sys.executable, str(script)], cwd=d, check=True)

if __name__ == '__main__':
    main()

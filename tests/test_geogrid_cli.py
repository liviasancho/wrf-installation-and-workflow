"""Safe static CLI smoke tests; no WRF binaries needed."""
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_generate_grid_help():
    p = subprocess.run([sys.executable, str(ROOT/'scripts/geogrid/generate_grid.py'), '--help'], capture_output=True, text=True)
    assert p.returncode == 0
    assert '--overwrite' in p.stdout

def test_generate_grid_rejects_missing_namelist(tmp_path):
    p = subprocess.run([sys.executable, str(ROOT/'scripts/geogrid/generate_grid.py'), '--wps-dir', str(tmp_path)], capture_output=True, text=True)
    assert p.returncode != 0
    assert 'Missing' in p.stderr

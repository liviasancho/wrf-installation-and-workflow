import importlib.util
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "forcing" / "download_gdas_fnl.py"
spec = importlib.util.spec_from_file_location("download_gdas_fnl", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_url_pattern():
    date = datetime(2022, 1, 1, 6, tzinfo=timezone.utc)
    url, name = module.file_url(date)
    assert url.endswith("/2022/202201/gdas1.fnl0p25.2022010106.f00.grib2")
    assert name == "gdas1.fnl0p25.2022010106.f00.grib2"

def test_inclusive_dates():
    start = datetime(2022, 1, 1, 0, tzinfo=timezone.utc)
    end = datetime(2022, 1, 1, 12, tzinfo=timezone.utc)
    assert len(list(module.dates(start, end))) == 3

def test_date_parser_rejects_other_hours():
    import argparse
    try:
        module.utc_datetime("2022-01-01T03:00")
    except argparse.ArgumentTypeError:
        return
    raise AssertionError("Expected argument error")

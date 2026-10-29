#!/usr/bin/env python3
"""Download NCAR GDAS/FNL 0.25-degree f00 analysis GRIB2 files.

Original downloading script by Elisa Passos (faz_download_gfs.py).
Adapted for this repository with CLI arguments, TLS verification,
response validation and failure reporting. Not validated against a live server.
"""
import argparse
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://osdf-director.osg-htc.org/ncar/gdex/d083003"


def utc_datetime(value):
    try:
        result = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Expected YYYY-MM-DDTHH:MM (UTC)") from exc
    if result.hour not in (0, 6, 12, 18) or result.minute:
        raise argparse.ArgumentTypeError("Use 00, 06, 12 or 18 UTC")
    return result.replace(tzinfo=timezone.utc)


def file_url(when, base_url=BASE_URL):
    stamp = when.strftime("%Y%m%d%H")
    name = f"gdas1.fnl0p25.{stamp}.f00.grib2"
    url = f"{base_url.rstrip('/')}/{when:%Y}/{when:%Y%m}/{name}"
    return url, name


def dates(start, end):
    if end < start:
        raise ValueError("End date must not precede start date")
    now = start
    while now <= end:
        yield now
        now += timedelta(hours=6)


def build_session():
    s = requests.Session()
    retry = Retry(total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    s.mount("https://", HTTPAdapter(max_retries=retry))
    return s


def download(session, url, destination, min_bytes=1024, retries=3):
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_name(destination.name + ".part")
    if destination.is_file():
        # Existing files cannot be declared valid solely from their size.
        print(f"EXISTS (not checksum-verified): {destination}")
        return True
    for attempt in range(1, retries + 1):
        tmp.unlink(missing_ok=True)
        try:
            with session.get(url, stream=True, timeout=(20, 90)) as response:
                response.raise_for_status()  # TLS certificate verification is enabled.
                length = response.headers.get("Content-Length")
                expected = int(length) if length and length.isdigit() else None
                total = 0
                with tmp.open("wb") as target:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            target.write(chunk)
                            total += len(chunk)
                if total < min_bytes:
                    raise IOError(f"Unexpectedly small response ({total} bytes)")
                if expected is not None and total != expected:
                    raise IOError(f"Content-Length mismatch ({total} != {expected})")
            tmp.replace(destination)
            print(f"DOWNLOADED: {destination} ({total} bytes)")
            return True
        except (requests.RequestException, OSError, ValueError) as exc:
            tmp.unlink(missing_ok=True)
            print(f"Attempt {attempt}/{retries} failed for {url}: {exc}", file=sys.stderr)
            if attempt < retries:
                time.sleep(2)
    return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=utc_datetime, required=True, help='UTC YYYY-MM-DDTHH:MM')
    parser.add_argument('--end', type=utc_datetime, required=True, help='UTC YYYY-MM-DDTHH:MM')
    parser.add_argument('--output-dir', type=Path, default=Path('data/raw/gdas_fnl'))
    parser.add_argument('--base-url', default=BASE_URL, help='GDEX OSDF endpoint (change only if necessary)')
    parser.add_argument('--dry-run', action='store_true', help='List URLs without downloading')
    args = parser.parse_args(argv)
    if args.end < args.start:
        parser.error('--end must be on or after --start')
    failures = []
    session = None if args.dry_run else build_session()
    try:
        for when in dates(args.start, args.end):
            url, filename = file_url(when, args.base_url)
            if args.dry_run:
                print(url)
            elif not download(session, url, args.output_dir / filename):
                failures.append(url)
    finally:
        if session:
            session.close()
    if failures:
        print(f"FAILED ({len(failures)}):\n" + "\n".join(failures), file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())

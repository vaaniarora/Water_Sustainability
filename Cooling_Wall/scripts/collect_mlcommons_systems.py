"""Collect MLPerf system descriptions (and the few power results) from MLCommons GitHub repos.

Why: MLPerf power results are too sparse to use as a time series, but every submission ships
a system-description JSON with accelerator model/count, node count, PSU rating and a free-text
`cooling` field. Across rounds this gives a multi-vendor record of which servers are air- vs
liquid-cooled (inputs to Fig 2b and Fig 3).

How: shallow, blob-filtered sparse clones that check out only `**/systems/*.json` and
`summary_results.json`, so nothing else is downloaded and no GitHub API rate limit applies.
Downloaded files are only parsed as JSON; nothing from the repos is executed.

Outputs (in --out):
  systems.csv        one row per system-description JSON
  power_results.csv  rows with measured power from summary_results.json (v5.0+ inference only)

Usage:
  python collect_mlcommons_systems.py                       # all known rounds
  python collect_mlcommons_systems.py --suites inference --rounds v4.1 v5.0 v5.1
  python collect_mlcommons_systems.py --skip-clone          # re-parse an existing cache
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]  # Cooling_Wall/
DEFAULT_OUT = ROOT / 'Data/downloaded/mlcommons'

ROUNDS = {
    'inference': ['v0.5', 'v0.7', 'v1.0', 'v1.1', 'v2.0', 'v2.1', 'v3.0', 'v3.1',
                  'v4.0', 'v4.1', 'v5.0', 'v5.1'],
    'training': ['v0.5', 'v0.6', 'v0.7', 'v1.0', 'v1.1', 'v2.0', 'v2.1', 'v3.0', 'v3.1',
                 'v4.0', 'v4.1', 'v5.0', 'v5.1'],
}
SPARSE_PATTERNS = ['**/systems/*.json', '/summary_results.json']

SYSTEM_FIELDS = [
    'system_name', 'submitter', 'division', 'status', 'system_type', 'number_of_nodes',
    'accelerator_model_name', 'accelerators_per_node', 'accelerator_memory_capacity',
    'host_processor_model_name', 'host_processors_per_node', 'cooling',
    'power_supply_quantity_and_rating_watts', 'power_supply_details', 'power_management', 'hw_notes',
]


def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)


def sparse_clone(repo, dest):
    """Shallow sparse clone of github.com/mlcommons/<repo>. Returns False if the repo doesn't exist."""
    url = f'https://github.com/mlcommons/{repo}.git'
    if dest.exists():
        print(f'  {repo}: cached')
        return True
    try:
        run(['git', 'ls-remote', '--exit-code', url, 'HEAD'])
    except subprocess.CalledProcessError:
        print(f'  {repo}: not found, skipping')
        return False
    print(f'  {repo}: cloning')
    run(['git', 'clone', '--depth', '1', '--filter=blob:none', '--no-checkout', url, str(dest)])
    run(['git', 'sparse-checkout', 'set', '--no-cone', *SPARSE_PATTERNS], cwd=dest)
    run(['git', 'checkout'], cwd=dest)
    return True


def cooling_class(text):
    """Bucket the free-text cooling field: liquid / air / liquid+air / immersion / unknown."""
    t = str(text or '').lower()
    if not t.strip() or t.strip() in {'n/a', 'na', 'none', '-'}:
        return 'unknown'
    if 'immers' in t:
        return 'immersion'
    liquid = bool(re.search(r'liquid|water|dlc|cold.?plate|direct.?to.?chip|d2c', t))
    # 'Passive OAM' / 'Passive & Active' describe heatsinks in fan-cooled chassis
    air = bool(re.search(r'\bair|passive|\bactive|\bfans?\b', t))
    if liquid and air:
        return 'liquid+air'
    if liquid:
        return 'liquid'
    if air:
        return 'air'
    return 'unknown'


def psu_total_watts(text):
    """Best-effort parse of PSU quantity and rating.

    Handles e.g. '6x 3000W', '4 x 2.7kW', '6x Delta Titanium 3,000-Watt Supplies', 'x2, 140W'.
    Returns quantity * rating, an upper bound on server power (PSUs are often redundant, N+1/N+N).
    """
    t = str(text or '')
    w = re.search(r'(\d[\d,]*(?:\.\d+)?)\s*-?\s*(kw|w)(?:att)?s?\b', t, re.I)
    if not w:
        return None
    watts = float(w.group(1).replace(',', '')) * (1000 if w.group(2).lower() == 'kw' else 1)
    q = re.search(r'(\d+)\s*[x×]', t[:w.start()], re.I) or re.search(r'[x×]\s*(\d+)', t[:w.start()], re.I)
    return (int(q.group(1)) if q else 1) * watts


def parse_systems(repo_dir, suite, version):
    rows = []
    for path in sorted(repo_dir.glob('**/systems/*.json')):
        rel = path.relative_to(repo_dir)
        if any('backup' in p.lower() for p in rel.parts):
            continue
        try:
            desc = json.loads(path.read_text(errors='replace'))
        except (json.JSONDecodeError, OSError) as e:
            print(f'    skip {rel}: {e}', file=sys.stderr)
            continue
        if not isinstance(desc, dict):
            continue
        parts = rel.parts  # closed/<submitter>/systems/x.json  or  <submitter>/systems/x.json
        row = {'suite': suite, 'round': version, 'path': str(rel),
               'path_division': parts[0] if len(parts) >= 4 else '',
               'path_submitter': parts[-3] if len(parts) >= 3 else ''}
        row.update({f: desc.get(f, '') for f in SYSTEM_FIELDS})
        row['cooling_class'] = cooling_class(row['cooling'])
        row['psu_total_W_upper_bound'] = psu_total_watts(row['power_supply_quantity_and_rating_watts'])
        rows.append(row)
    return rows


def parse_power(repo_dir, version):
    f = repo_dir / 'summary_results.json'
    if not f.exists():
        return []
    rows = []
    for r in json.loads(f.read_text()):
        if r.get('has_power') and r.get('Power_Result') not in (None, ''):
            rows.append({'round': version, **{k: r.get(k) for k in [
                'Submitter', 'Suite', 'Category', 'Availability', 'System', 'Platform', 'Model',
                'Scenario', 'Nodes', 'Accelerator', 'a#', 'Processor', 'Notes', 'Power_Result',
                'Power_Units', 'Performance_Result', 'Performance_Units', 'Details']}})
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--suites', nargs='+', default=list(ROUNDS), choices=list(ROUNDS))
    ap.add_argument('--rounds', nargs='+', help='e.g. v4.1 v5.0 (default: all known)')
    ap.add_argument('--out', type=Path, default=DEFAULT_OUT)
    ap.add_argument('--skip-clone', action='store_true', help='only parse repos already in the cache')
    args = ap.parse_args()

    cache = args.out / 'raw'
    cache.mkdir(parents=True, exist_ok=True)
    systems, power = [], []
    for suite in args.suites:
        for version in args.rounds or ROUNDS[suite]:
            repo = f'{suite}_results_{version}'
            dest = cache / repo
            if not args.skip_clone:
                try:
                    if not sparse_clone(repo, dest):
                        continue
                except subprocess.CalledProcessError as e:
                    print(f'  {repo}: git failed: {e.stderr.strip()}', file=sys.stderr)
                    continue
            if not dest.exists():
                continue
            s = parse_systems(dest, suite, version)
            p = parse_power(dest, version)
            print(f'  {repo}: {len(s)} systems, {len(p)} power rows')
            systems += s
            power += p

    sys_df = pd.DataFrame(systems)
    sys_df.to_csv(args.out / 'systems.csv', index=False)
    pd.DataFrame(power).to_csv(args.out / 'power_results.csv', index=False)
    print(f'\nWrote {len(sys_df)} systems and {len(power)} power rows to {args.out}')
    if len(sys_df):
        print(sys_df.groupby(['suite', 'round'])['cooling_class'].value_counts().unstack(fill_value=0))


if __name__ == '__main__':
    main()

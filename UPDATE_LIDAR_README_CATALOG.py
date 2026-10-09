from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / 'validation_framework' / 'integration' / 'master_catalog_0001_0050.csv'
README = ROOT / 'README.md'
START = '<!-- PAI-SG-LIDAR-CATALOG:START -->'
END = '<!-- PAI-SG-LIDAR-CATALOG:END -->'

if not MASTER.is_file():
    raise SystemExit(f'ERROR: missing master catalog: {MASTER}')
with MASTER.open('r', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    required = {'component_id', 'manufacturer', 'model', 'catalog_status', 'verification_status', 'algorithm_test_status'}
    if not required.issubset(set(reader.fieldnames or [])):
        raise SystemExit('ERROR: missing required master catalog columns')
    rows = list(reader)
ids = [r['component_id'] for r in rows]
expected = {f'CMP-LDR-{i:04d}' for i in range(1, 51)}
if len(rows) != 50 or len(set(ids)) != 50 or set(ids) != expected:
    raise SystemExit('ERROR: expected exactly 50 unique IDs CMP-LDR-0001 to 0050')
rows.sort(key=lambda r: int(r['component_id'].split('-')[-1]))
for r in rows:
    card = ROOT / 'component_cards' / (r['component_id'] + '.md')
    if not card.is_file():
        raise SystemExit(f'ERROR: missing component card: {card}')

def cell(v):
    return str(v or '').replace('|', r'\|').replace('\n', ' ').strip()

lines = [
    START,
    '## LiDAR Sensor Catalog — Component Index',
    '',
    f'**Registered: {len(rows)} / 80 (62.5%) · Waves 1–10**',
    '',
    'This index is generated from `validation_framework/integration/master_catalog_0001_0050.csv`.',
    'Manufacturer specifications are evidence-backed catalog claims, **not hardware or ROS2/algorithm test results**.',
    '',
    '| Component ID | Manufacturer | Model | Catalog status | Verification | Algorithm test |',
    '|---|---|---|---|---|---|',
]
for r in rows:
    cid = r['component_id']
    lines.append(f"| [{cid}](component_cards/{cid}.md) | {cell(r['manufacturer'])} | {cell(r['model'])} | {cell(r['catalog_status'])} | {cell(r['verification_status'])} | {cell(r['algorithm_test_status'])} |")
lines.extend(['', END])
block = '\n'.join(lines)
original = README.read_text(encoding='utf-8-sig') if README.exists() else '# PAI-SG LiDAR Sensor Catalog\n'
if START in original or END in original:
    if original.count(START) != 1 or original.count(END) != 1 or original.index(START) >= original.index(END):
        raise SystemExit('ERROR: README catalog markers are malformed')
    updated = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda m: block, original, count=1, flags=re.S)
else:
    updated = original.rstrip() + '\n\n' + block + '\n'
README.write_text(updated, encoding='utf-8', newline='\n')
print(f'SUCCESS: README.md catalog index updated; TOTAL={len(rows)} LINKS={len(rows)}')

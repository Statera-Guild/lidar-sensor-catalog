from pathlib import Path
import csv, sys
root=Path(__file__).resolve().parent
src=root/'validation_framework/wave_a/batch_0001_0005/inventory.csv'
dst=root/'validation_framework/integration/master_catalog_0001_0005.csv'
with src.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==5 and [r['component_id'] for r in rows]==[f'CMP-LDR-{i:04d}' for i in range(1,6)]
assert len({(r['manufacturer'].casefold(),r['model'].casefold(),r['orderable_sku'].casefold()) for r in rows})==5
for r in rows:
    assert (root/'component_cards'/f"{r['component_id']}.md").is_file()
fields=list(rows[0].keys())
if dst.exists():
    with dst.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f))
    if old!=rows: sys.exit('ERROR: master differs from Wave 1 inventory; manual review required')
    print('ALREADY APPLIED: Wave 1 unchanged');sys.exit(0)
dst.parent.mkdir(parents=True,exist_ok=True)
with dst.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('SUCCESS: Wave 1 integrated, 5 candidate IDs; no verified claims')

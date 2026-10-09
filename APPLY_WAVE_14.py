from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework'/'integration'
OLD=BASE/'master_catalog_0001_0065.csv'
NEW=BASE/'master_catalog_0001_0070.csv'
BATCH=ROOT/'validation_framework'/'wave_a'/'batch_0066_0070'/'inventory.csv'
def read(p):
 if not p.is_file(): raise SystemExit('ERROR: missing file '+str(p)+'; clone latest main first')
 with p.open(newline='',encoding='utf-8-sig') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
fields,old=read(OLD)
_,incoming=read(BATCH)
if len(old)!=65 or {r['component_id'] for r in old}!={f'CMP-LDR-{i:04d}' for i in range(1,66)}: raise SystemExit('ERROR: baseline master must contain 65 unique IDs 0001-0065')
if len(incoming)!=5 or {r['component_id'] for r in incoming}!={f'CMP-LDR-{i:04d}' for i in range(66,71)}: raise SystemExit('ERROR: Wave 14 must contain five unique IDs 0066-0070')
if set(fields)!=set(incoming[0]): raise SystemExit('ERROR: master schema mismatch')
for i in range(66,71):
 p=ROOT/'component_cards'/f'CMP-LDR-{i:04d}.md'
 if not p.is_file(): raise SystemExit('ERROR: missing card '+str(p))
allrows=old+[{k:r[k] for k in fields} for r in incoming]
ids=[r['component_id'] for r in allrows]
if len(allrows)!=70 or len(set(ids))!=70 or set(ids)!={f'CMP-LDR-{i:04d}' for i in range(1,71)}: raise SystemExit('ERROR: duplicate/missing IDs')
with NEW.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(allrows)
print('SUCCESS: Wave 14 0066-0070 integrated; TOTAL=70 UNIQUE=70 (not hardware-tested)')

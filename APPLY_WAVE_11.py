from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework'/'integration'
OLD=BASE/'master_catalog_0001_0050.csv'
NEW=BASE/'master_catalog_0001_0055.csv'
BATCH=ROOT/'validation_framework'/'wave_a'/'batch_0051_0055'/'inventory.csv'
def read(p):
 if not p.is_file(): raise SystemExit('ERROR: missing file '+str(p)+'; clone latest main first')
 with p.open(newline='',encoding='utf-8-sig') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
fields,old=read(OLD)
_,incoming=read(BATCH)
expected_old={f'CMP-LDR-{i:04d}' for i in range(1,51)}
expected_new={f'CMP-LDR-{i:04d}' for i in range(51,56)}
if len(old)!=50 or {r['component_id'] for r in old}!=expected_old: raise SystemExit('ERROR: baseline master must contain 50 unique IDs 0001-0050')
if len(incoming)!=5 or {r['component_id'] for r in incoming}!=expected_new: raise SystemExit('ERROR: Wave 11 must contain five unique IDs 0051-0055')
if set(fields)!=set(incoming[0]): raise SystemExit('ERROR: master schema mismatch')
for i in range(51,56):
 p=ROOT/'component_cards'/f'CMP-LDR-{i:04d}.md'
 if not p.is_file(): raise SystemExit('ERROR: missing card '+str(p))
allrows=old+[{k:r[k] for k in fields} for r in incoming]
ids=[r['component_id'] for r in allrows]
if len(allrows)!=55 or len(set(ids))!=55 or set(ids)!={f'CMP-LDR-{i:04d}' for i in range(1,56)}: raise SystemExit('ERROR: duplicate/missing IDs')
with NEW.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(allrows)
print('SUCCESS: Wave 11 0051-0055 integrated; TOTAL=55 UNIQUE=55 (not hardware-tested)')

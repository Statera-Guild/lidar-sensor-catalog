from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework'/'integration'
OLD=BASE/'master_catalog_0001_0025.csv'
NEW=BASE/'master_catalog_0001_0030.csv'
BATCH=ROOT/'validation_framework'/'wave_a'/'batch_0026_0030'/'inventory.csv'
if not OLD.is_file(): raise SystemExit('ERROR: missing baseline '+str(OLD)+'; clone latest main first')
if not BATCH.is_file(): raise SystemExit('ERROR: missing inventory '+str(BATCH))
def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
fields,old=read(OLD)
_,incoming=read(BATCH)
expected_old={'CMP-LDR-%04d'%i for i in range(1,26)}
expected_new={'CMP-LDR-%04d'%i for i in range(26,31)}
if len(old)!=25 or {r['component_id'] for r in old}!=expected_old:
 raise SystemExit('ERROR: baseline master must contain exactly 25 unique IDs 0001-0025')
if len(incoming)!=5 or {r['component_id'] for r in incoming}!=expected_new:
 raise SystemExit('ERROR: Wave 6 inventory must contain exactly 5 unique IDs 0026-0030')
new=[]
for row in incoming:
 new.append({'component_id':row['component_id'],'manufacturer':row['manufacturer'],'model':row['model'],'orderable_sku':row['orderable_sku'],'catalog_status':row['catalog_status'],'verification_status':row['verification_status'],'algorithm_test_status':row['algorithm_test_status'],'wave':'wave_06'})
if set(fields)!=set(new[0]): raise SystemExit('ERROR: master schema mismatch')
for i in range(26,31):
 p=ROOT/'component_cards'/('CMP-LDR-%04d.md'%i)
 if not p.is_file(): raise SystemExit('ERROR: missing card '+str(p))
allrows=old+new
ids=[r['component_id'] for r in allrows]
if len(allrows)!=30 or len(set(ids))!=30 or set(ids)!={'CMP-LDR-%04d'%i for i in range(1,31)}:
 raise SystemExit('ERROR: duplicate/missing IDs')
with NEW.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(allrows)
print('SUCCESS: Wave 6 0026-0030 integrated; TOTAL=30 UNIQUE=30 (not hardware-tested)')

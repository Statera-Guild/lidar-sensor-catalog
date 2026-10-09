from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework'/'integration'
OLD=BASE/'master_catalog_0001_0020.csv'
NEW=BASE/'master_catalog_0001_0025.csv'
BATCH=ROOT/'validation_framework'/'wave_a'/'batch_0021_0025'/'inventory.csv'
if not OLD.is_file(): raise SystemExit('ERROR: missing '+str(OLD)+'; clone latest main first')
if not BATCH.is_file(): raise SystemExit('ERROR: missing '+str(BATCH))
def read(p):
 with p.open(newline='',encoding='utf-8-sig') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
fields,old=read(OLD)
_,incoming=read(BATCH)
expected={'CMP-LDR-%04d'%i for i in range(1,26)}
old_ids=[x['component_id'] for x in old]
if len(old)!=20 or len(set(old_ids))!=20 or set(old_ids)!={'CMP-LDR-%04d'%i for i in range(1,21)}:
 raise SystemExit('ERROR: baseline master must contain unique IDs 0001-0020')
new=[]
for row in incoming:
 new.append({'component_id':row['component_id'],'manufacturer':row['manufacturer'],'model':row['model'],'orderable_sku':row['orderable_sku'],'catalog_status':row['catalog_status'],'verification_status':row['verification_status'],'algorithm_test_status':row['algorithm_test_status'],'wave':'wave_05'})
allrows=old+new
ids=[x['component_id'] for x in allrows]
if len(allrows)!=25 or len(set(ids))!=25 or set(ids)!=expected:
 raise SystemExit('ERROR: duplicate/missing IDs or incorrect Wave 5 inventory')
if set(fields)!=set(new[0]): raise SystemExit('ERROR: master schema differs from expected')
BASE.mkdir(parents=True,exist_ok=True)
with NEW.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(allrows)
for i in range(21,26):
 p=ROOT/'component_cards'/('CMP-LDR-%04d.md'%i)
 if not p.is_file():raise SystemExit('ERROR: missing card '+str(p))
print('SUCCESS: Wave 5 0021-0025 integrated; TOTAL=25 UNIQUE=25 (not hardware-tested)')

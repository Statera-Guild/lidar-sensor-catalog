from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework'/'integration'
OLD=BASE/'master_catalog_0001_0045.csv'
NEW=BASE/'master_catalog_0001_0050.csv'
BATCH=ROOT/'validation_framework'/'wave_a'/'batch_0046_0050'/'inventory.csv'
def read(p):
 if not p.is_file(): raise SystemExit('ERROR: missing file '+str(p)+'; clone latest main first')
 with p.open(newline='',encoding='utf-8-sig') as f:
  r=csv.DictReader(f);return r.fieldnames,list(r)
fields,old=read(OLD)
_,incoming=read(BATCH)
expected_old={'CMP-LDR-%04d'%i for i in range(1,46)}
expected_new={'CMP-LDR-%04d'%i for i in range(46,51)}
if len(old)!=45 or {r['component_id'] for r in old}!=expected_old:
 raise SystemExit('ERROR: baseline master must contain exactly 45 unique IDs 0001-0045')
if len(incoming)!=5 or {r['component_id'] for r in incoming}!=expected_new:
 raise SystemExit('ERROR: Wave 10 inventory must contain exactly 5 unique IDs 0046-0050')
new=[]
for row in incoming:
 new.append({'component_id':row['component_id'],'manufacturer':row['manufacturer'],'model':row['model'],'orderable_sku':row['orderable_sku'],'catalog_status':row['catalog_status'],'verification_status':row['verification_status'],'algorithm_test_status':row['algorithm_test_status'],'wave':'wave_10'})
if set(fields)!=set(new[0]): raise SystemExit('ERROR: master schema mismatch')
for i in range(46,51):
 p=ROOT/'component_cards'/('CMP-LDR-%04d.md'%i)
 if not p.is_file(): raise SystemExit('ERROR: missing card '+str(p))
allrows=old+new
ids=[r['component_id'] for r in allrows]
if len(allrows)!=50 or len(set(ids))!=50 or set(ids)!={'CMP-LDR-%04d'%i for i in range(1,51)}:
 raise SystemExit('ERROR: duplicate/missing IDs')
with NEW.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(allrows)
print('SUCCESS: Wave 10 0046-0050 integrated; TOTAL=50 UNIQUE=50 (not hardware-tested)')

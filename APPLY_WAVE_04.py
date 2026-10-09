from pathlib import Path
import csv,io,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'validation_framework/integration/master_catalog_0001_0015.csv'
OUT=ROOT/'validation_framework/integration/master_catalog_0001_0020.csv'
INV=ROOT/'validation_framework/wave_a/batch_0016_0020/inventory.csv'
def load(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
if not BASE.is_file() or not INV.is_file():sys.exit('ERROR: missing Wave 3 baseline or Wave 4 inventory')
base=load(BASE);new=load(INV)
expected=['CMP-LDR-%04d'%i for i in range(1,16)]
if [r['component_id'] for r in base]!=expected:sys.exit('ERROR: Wave 3 baseline IDs not 0001..0015')
if [r['component_id'] for r in new]!=['CMP-LDR-%04d'%i for i in range(16,21)]:sys.exit('ERROR: Wave 4 IDs not 0016..0020')
cols=list(base[0]);out=base[:]
for r in new:
 out.append(dict(component_id=r['component_id'],manufacturer=r['manufacturer'],model=r['model'],orderable_sku=r['orderable_sku'],catalog_status=r['catalog_status'],verification_status='not_verified',algorithm_test_status='not_tested',wave='wave_04'))
if len(out)!=20 or len({r['component_id'] for r in out})!=20:sys.exit('ERROR: master integrity failed')
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=cols,lineterminator='\n');w.writeheader();w.writerows(out)
OUT.write_text(s.getvalue(),encoding='utf-8')
print('SUCCESS: Wave 4 0016-0020 integrated; TOTAL=20 UNIQUE=20 (not hardware-tested)')

from pathlib import Path
import csv,io,sys
ROOT=Path(__file__).resolve().parent
B=ROOT/'validation_framework'/'wave_a'
MASTER=ROOT/'validation_framework'/'integration'/'master_catalog_0001_0010.csv'
NEW=ROOT/'validation_framework'/'integration'/'master_catalog_0001_0015.csv'
def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(path,rows,cols):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=cols,lineterminator='\n');w.writeheader();w.writerows(rows);path.write_text(s.getvalue(),encoding='utf-8')
def key(r):return r['component_id']
if not MASTER.is_file():sys.exit('ERROR: Wave 2 master catalog missing; run from cloned repository')
master=read(MASTER)
if len(master)!=10 or [key(r) for r in master]!=['CMP-LDR-%04d'%i for i in range(1,11)]:sys.exit('ERROR: baseline master 0001-0010 unexpected')
statuses={'0006':('LMS111-10100','listed'),'0007':('UTM-30LX','listed'),'0008':('','listed'),'0009':('','listed'),'0010':('','family_listed')}
for r in master:
 k=r['component_id'][-4:]
 if k in statuses:
  r['orderable_sku'],r['catalog_status']=statuses[k]
  r['verification_status']='not_verified';r['algorithm_test_status']='not_tested'
for i,m,n,sku,url,scope,status,cls in [
('0011','SICK','TiM781-2174101','TiM781-2174101','','','listed',''),
('0012','Hokuyo','UST-20LX','UST-20LX','','','listed',''),
('0013','SLAMTEC','RPLIDAR A3','','','','listed',''),
('0014','Livox','Avia 2','Avia 2','','','listed',''),
('0015','Ouster','OS2','','','','family_listed','')]:
 master.append(dict(component_id='CMP-LDR-'+i,manufacturer=m,model=n,orderable_sku=sku,catalog_status=status,verification_status='not_verified',algorithm_test_status='not_tested',wave='wave_03'))
write(NEW,master,list(master[0]))
inv=B/'batch_0006_0010'/'inventory.csv'
rows=read(inv)
for r in rows:
 k=r['component_id'][-4:];r['orderable_sku'],r['catalog_status']=statuses[k]
write(inv,rows,list(rows[0]))
# supplement source registry without losing original schema
reg=B/'batch_0006_0010'/'source_registry.csv'; rr=read(reg)
urls={
'0006':'https://www.sick.com/media/pdf/2/42/842/dataSheet_LMS111-10100_1041114_ko.pdf',
'0007':'https://www.hokuyo-aut.jp/search/single.php?serial=169',
'0008':'https://www.hesaitech.com/cn/news/1067',
'0009':'https://www.robosense.ai/en/resources-27',
'0010':'https://ouster.com/products/hardware/os0'}
for r in rr:
 k=r['component_id'][-4:];r.update(source_type='manufacturer_primary',source_url=urls[k],access_date='2026-10-10',claim_scope='model_specific_or_family_see_evidence_review',evidence_status='source_backed',review_note='See manufacturer_evidence_sources.csv; no hardware test')
write(reg,rr,list(rr[0]))
claims=B/'batch_0006_0010'/'spec_claims.csv'
cr=read(B/'batch_0006_0010'/'manufacturer_evidence_claims.csv')
if claims.is_file():
 old=read(claims)
 if old:
  if set(old[0])==set(cr[0]):
   cr=old+[r for r in cr if r not in old]
  else:
   # keep original file unchanged if incompatible; evidence claims remain in separate file
   cr=None
if cr is not None:write(claims,cr,list(cr[0]))
print('SUCCESS: Wave 2 evidence reconciled and Wave 3 0011-0015 integrated (not hardware-tested)')

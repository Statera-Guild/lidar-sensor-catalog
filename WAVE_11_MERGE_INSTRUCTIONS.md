# Wave 11 integration (Windows Anaconda Prompt)

Run from the **repository root** after cloning `https://github.com/Statera-Guild/lidar-sensor-catalog.git` and copying the `package` contents into it.

```bat
python APPLY_WAVE_11.py
python APPLY_WAVE_11.py
python UPDATE_LIDAR_README_CATALOG.py
python UPDATE_LIDAR_README_CATALOG.py
python -c "import csv; p='validation_framework/integration/master_catalog_0001_0055.csv'; r=list(csv.DictReader(open(p,encoding='utf-8-sig'))); ids=[x['component_id'] for x in r]; print('TOTAL:',len(r),'UNIQUE:',len(set(ids)),'PASS:',len(r)==55 and len(set(ids))==55)"
git diff --check
git add .
git diff --cached --check
git diff --cached --stat
git commit -m "Add Wave 11 LiDAR evidence and README catalog index for 55 devices"
git push origin main
git status
```

**Do not delete the clone until push succeeds and working tree is clean.** Manufacturer specifications are not hardware/ROS2 test results.

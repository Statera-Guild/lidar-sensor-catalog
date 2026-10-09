# Wave 6 Merge Instructions (Windows 10 Anaconda Prompt)

1. Clone https://github.com/Statera-Guild/lidar-sensor-catalog.git into Downloads.
2. Expand this ZIP to `C:\Users\abc\Downloads\PAI_SG_LiDAR_Wave06`.
3. From repository root: `xcopy "C:\Users\abc\Downloads\PAI_SG_LiDAR_Wave06\package\*" ".\" /E /I /Y`
4. Run `python APPLY_WAVE_06.py` twice, then validate `master_catalog_0001_0030.csv`.
5. Run `git diff --check` and `git status --short`; review before committing.

# Wave 5 Merge (Windows 10 Anaconda Prompt)

Clone repository into Downloads; unzip this package to `C:\Users\abc\Downloads\PAI_SG_LiDAR_Wave05`.

```bat
cd /d C:\Users\abc\Downloads\lidar-sensor-catalog
xcopy "C:\Users\abc\Downloads\PAI_SG_LiDAR_Wave05\package\*" ".\" /E /I /Y
python APPLY_WAVE_05.py
python APPLY_WAVE_05.py
git diff --check
git status --short
```

Only commit after confirming master IDs 0001-0025 and evidence files.

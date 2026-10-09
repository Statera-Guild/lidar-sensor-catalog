# Wave 4 merge — Windows Anaconda Prompt

1. Clone Statera-Guild/lidar-sensor-catalog into Downloads.
2. Extract ZIP to Downloads\PAI_SG_LiDAR_Wave04.
3. From inside the cloned repository run `xcopy "C:\Users\abc\Downloads\PAI_SG_LiDAR_Wave04\package\*" ".\" /E /I /Y`.
4. Run `python APPLY_WAVE_04.py` twice; both runs should succeed without duplicate IDs.
5. Check master 0001_0020, `git diff --check`, `git status --short`.
6. Review before commit/push.

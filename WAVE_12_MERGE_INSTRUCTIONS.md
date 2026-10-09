# Wave 12 integration and README index

1. Clone latest GitHub main into Downloads/lidar-sensor-catalog.
2. Extract ZIP to Downloads/PAI_SG_LiDAR_Wave12; copy package/* into clone.
3. Run `python APPLY_WAVE_12.py` twice; expect TOTAL=60 UNIQUE=60.
4. Run `python UPDATE_LIDAR_README_CATALOG.py` twice; expect TOTAL=60 LINKS=60.
5. Validate `git diff --check`, `git status --short`, `git add .`, `git diff --cached --check`, then commit/push after review.
6. Delete clone and extracted folder ONLY after successful push and clean status.

All status values remain not_verified / not_tested. Safety-rated devices are not automatically approved as complete robot safety systems.

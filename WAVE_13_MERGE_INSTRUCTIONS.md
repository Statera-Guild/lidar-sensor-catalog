# Wave 13 — Windows CMD merge instructions

1. Clone the latest GitHub `main` into `C:\Users\abc\Downloads\lidar-sensor-catalog`.
2. Extract the ZIP and copy `package\*` into the repository root (`xcopy /E /I /Y`).
3. Run `python APPLY_WAVE_13.py` twice. Both must print TOTAL=65 UNIQUE=65.
4. Run `python UPDATE_LIDAR_README_CATALOG.py` twice. Both must print TOTAL=65 LINKS=65.
5. Check `git diff --check`, `git status --short`, `git add .`, `git diff --cached --check`, and `git diff --cached --stat`.
6. Commit and push only after all checks pass; delete temporary directories only after `git status` is clean.

No physical LiDAR, ROS2, timing, SLAM, safety, or procurement validation is claimed.

# Wave 14 Merge Instructions

1. Clone latest GitHub `main` (Wave 13 commit `70bd387` or newer).
2. Copy `package/*` into repository root.
3. Run `python APPLY_WAVE_14.py` twice (70 unique IDs).
4. Run `python UPDATE_LIDAR_README_CATALOG.py` twice (70 links).
5. Check `git diff --check`, `git status --short`, then stage, check and commit once.
6. Push to `main`, verify clean working tree, then delete temporary folders.

All 5 devices are listed based on manufacturer evidence; no hardware or ROS2/algorithm tests.

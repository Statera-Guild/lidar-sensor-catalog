# Wave 16 Merge Instructions

1. Clone latest GitHub main (Wave 15 commit `bf71b3e` or newer).
2. Copy `package/*` into repository root.
3. Run `python APPLY_WAVE_16.py` twice (80 unique IDs).
4. Run `python UPDATE_LIDAR_README_CATALOG.py` twice (80 links).
5. Check `git diff --check`, `git status --short`, stage and commit once.
6. Push to main, verify clean working tree, then delete temporary folders.

80 catalog entries is a listing milestone only; no device or algorithm tests.

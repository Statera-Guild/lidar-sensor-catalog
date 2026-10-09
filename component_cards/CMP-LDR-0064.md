# CMP-LDR-0064 — SICK LRS4000

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D long-range LiDAR
- **Orderable/model designation:** LRS4000 family (specific SKU unconfirmed)
- **Official manufacturer source:** https://www.sick.com/media/familyoverview/4/94/594/familyOverview_LRS4000_g555594_en.pdf

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| horizontal_fov | 360 | deg |
| working_range_min | 0.2 | m |
| working_range_max | 300 | m |
| scanning_range_10pct | 80 | m |
| scanning_range_90pct | 250 | m |
| evaluated_echoes | 3 | echoes |
| scan_frequency | 12.5 or 25 | Hz |
| interface | Ethernet | text |

## Integration and evidence boundaries

Candidate use: outdoor long-range localization / obstacle detection candidate. This is a manufacturer-family evidence record; no hardware, ROS2, timing, algorithm, or system safety validation has been performed.

For safety-related use, the robot safety architecture and certification must be evaluated independently.

**Evidence reference:** SRC-LDR-0064. See `validation_framework/wave_a/batch_0061_0065/manufacturer_evidence_claims.csv`.

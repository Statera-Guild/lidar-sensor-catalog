# CMP-LDR-0065 — SICK LMS4xx

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D near-range contour LiDAR
- **Orderable/model designation:** LMS4xx family (specific SKU unconfirmed)
- **Official manufacturer source:** https://www.sick.com/media/familyoverview/0/10/910/familyOverview_LMS4xx_g91910_en.pdf

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| horizontal_fov | 70 | deg |
| working_range_min | 0.7 | m |
| working_range_max | 3 | m |
| scanning_range_10pct | 3 | m |
| scan_frequency | 230-500 | Hz |
| interface | Ethernet and serial | text |
| operating_temperature | 0 to 40 | degC |

## Integration and evidence boundaries

Candidate use: conveyor / pallet contour measurement candidate. This is a manufacturer-family evidence record; no hardware, ROS2, timing, algorithm, or system safety validation has been performed.

For safety-related use, the robot safety architecture and certification must be evaluated independently.

**Evidence reference:** SRC-LDR-0065. See `validation_framework/wave_a/batch_0061_0065/manufacturer_evidence_claims.csv`.

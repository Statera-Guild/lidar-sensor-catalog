# CMP-LDR-0061 — SICK LMS1000

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D measurement LiDAR
- **Orderable/model designation:** LMS1000 family (specific SKU unconfirmed)
- **Official manufacturer source:** https://www.sick.com/au/en/catalog/products/lidar-and-radar-sensors/lidar-sensors/lms1000/c/g387151

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| horizontal_fov | 275 | deg |
| working_range_min | 0.2 | m |
| working_range_max | 64 | m |
| scanning_range_10pct | 16 | m |
| scanning_range_90pct | 30 | m |
| scan_frequency | 150 | Hz |
| evaluated_echoes | 3 | echoes |
| interface | Ethernet | text |

## Integration and evidence boundaries

Candidate use: 2D obstacle detection / mapping candidate. This is a manufacturer-family evidence record; no hardware, ROS2, timing, algorithm, or system safety validation has been performed.

For safety-related use, the robot safety architecture and certification must be evaluated independently.

**Evidence reference:** SRC-LDR-0061. See `validation_framework/wave_a/batch_0061_0065/manufacturer_evidence_claims.csv`.

# CMP-LDR-0062 — SICK MRS1000

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 3D multilayer LiDAR
- **Orderable/model designation:** MRS1000 family (specific SKU unconfirmed)
- **Official manufacturer source:** https://cdn.sick.com/media/familyoverview/2/52/152/familyOverview_MRS1000_g387152_en.pdf

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| horizontal_fov | 275 | deg |
| vertical_fov | 7.5 | deg |
| scan_layers | 4 | layers |
| working_range_min | 0.2 | m |
| working_range_max | 64 | m |
| scanning_range_10pct | 16 | m |
| scanning_range_90pct | 30 | m |
| interface | Ethernet | text |

## Integration and evidence boundaries

Candidate use: multi-layer obstacle detection / 3D perception candidate. This is a manufacturer-family evidence record; no hardware, ROS2, timing, algorithm, or system safety validation has been performed.

For safety-related use, the robot safety architecture and certification must be evaluated independently.

**Evidence reference:** SRC-LDR-0062. See `validation_framework/wave_a/batch_0061_0065/manufacturer_evidence_claims.csv`.

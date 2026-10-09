# CMP-LDR-0063 — SICK MRS6000

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 3D multilayer LiDAR
- **Orderable/model designation:** MRS6000 family (specific SKU unconfirmed)
- **Official manufacturer source:** https://cdn.sick.com/media/docs/0/30/930/Product_overview_Detection_and_Ranging_Solutions_2D_laser_scanners_3D_laser_scanners_radar_sensors_en_IM0063930.PDF

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| horizontal_fov | 120 | deg |
| vertical_fov | 15 | deg |
| scan_layers | 24 | layers |
| working_range_min | 0.5 | m |
| working_range_max | 200 | m |
| scanning_range_10pct | 30 | m |
| scanning_range_90pct | 75 | m |
| scan_frequency | 10 | Hz |

## Integration and evidence boundaries

Candidate use: multi-layer 3D detection candidate. This is a manufacturer-family evidence record; no hardware, ROS2, timing, algorithm, or system safety validation has been performed.

For safety-related use, the robot safety architecture and certification must be evaluated independently.

**Evidence reference:** SRC-LDR-0063. See `validation_framework/wave_a/batch_0061_0065/manufacturer_evidence_claims.csv`.

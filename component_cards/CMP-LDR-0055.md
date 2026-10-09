# CMP-LDR-0055 — SLAMTEC LPX-E3P2

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D area monitoring sensor
- **Orderable/model designation:** E3P2
- **Official manufacturer source:** https://www.slamtec.com/en/e3/spec

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| distance_70pct_m | 0.05-40 | m |
| warning_distance_10pct_m | 0.05-15 | m |
| alarm_distance_2pct_m | 0.05-5 | m |
| scan_rate | 10/15/20 | Hz |
| angular_resolution_at_10hz | 0.1125 | deg |
| monitoring_field_sets_at_20hz | 64 | sets |
| field_output | IO | text |
| point_cloud_output | NIL | text |

## Integration and evidence boundaries

AREA MONITORING ONLY: manufacturer specifies point cloud output NIL; do not classify as raw LaserScan source or safety-rated scanner.

This card records manufacturer-stated claims only. No hardware inspection, timing validation, ROS2 integration test, safety validation, or independent benchmark has been performed.

**Evidence reference:** SRC-LDR-0055. See `validation_framework/wave_a/batch_0051_0055/manufacturer_evidence_claims.csv`.

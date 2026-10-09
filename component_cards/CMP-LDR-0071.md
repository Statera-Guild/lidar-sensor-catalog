# CMP-LDR-0071 — RoboSense Helios 16

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 16-beam rotating 3D LiDAR
- **Orderable/model designation:** confirm exact SKU and firmware
- **Official manufacturer source:** https://store.robosense.ai/products/helios-series?variant=44365449822261

## Manufacturer-stated specifications and classification

| Property | Value | Unit |
|---|---|---|
| laser_channels | 16 | beams |
| horizontal_fov | 360 | deg |
| vertical_fov | 30 | deg |
| range_at_10pct_nist | 110 | m |
| frame_rate_options | 5/10/20 | Hz |
| single_return_point_rate | 288000 | pts/s |
| power_consumption_10hz | 11 | W |

## Evidence scope and integration cautions

H16 variant; manufacturer specifications depend on stated measurement conditions.

Manufacturer materials are **catalog evidence, not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Check operating conditions, model variants, packet interfaces, firmware and timestamps before implementation.

**Evidence reference:** SRC-LDR-0071. See `validation_framework/wave_a/batch_0071_0075/manufacturer_evidence_claims.csv`.

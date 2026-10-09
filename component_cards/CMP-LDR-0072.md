# CMP-LDR-0072 — RoboSense Helios 32 H32F70

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 32-beam wide-vertical-FOV rotating 3D LiDAR
- **Orderable/model designation:** confirm exact SKU and firmware
- **Official manufacturer source:** https://store.robosense.ai/products/helios-series?variant=44365449822261

## Manufacturer-stated specifications and classification

| Property | Value | Unit |
|---|---|---|
| laser_channels | 32 | beams |
| horizontal_fov | 360 | deg |
| vertical_fov | 70 | deg |
| range_at_10pct_nist | 110 | m |
| frame_rate_options | 5/10/20 | Hz |
| single_return_point_rate | 576000 | pts/s |
| power_consumption_10hz | 12 | W |

## Evidence scope and integration cautions

H32F70 only; do not transfer 70-degree vertical FOV to H32F26.

Manufacturer materials are **catalog evidence, not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Check operating conditions, model variants, packet interfaces, firmware and timestamps before implementation.

**Evidence reference:** SRC-LDR-0072. See `validation_framework/wave_a/batch_0071_0075/manufacturer_evidence_claims.csv`.

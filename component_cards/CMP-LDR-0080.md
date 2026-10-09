# CMP-LDR-0080 — Innoviz Technologies InnovizTwo Slim

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Low-profile automotive long-range solid-state 3D LiDAR
- **Orderable/model designation:** InnovizTwo Slim; exact SKU and firmware to confirm
- **Official manufacturer source:** https://innoviz.tech/innoviztwo-slim

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| maximum_angular_resolution_h | 0.05 | deg |
| maximum_angular_resolution_v | 0.05 | deg |
| frame_rate_options | 10/20 | FPS |
| maximum_detection_range | 300 | m |
| maximum_horizontal_fov | 120 | deg |
| maximum_vertical_fov | 28.8 | deg |
| dimensions_h | 30 | mm |
| dimensions_w | 140 | mm |
| dimensions_d | 120 | mm |
| low_profile_height_min | 25 | mm |

## Evidence scope and integration cautions

Official page mentions reduced height as small as 25 mm and key-metrics dimensions 30 mm; these refer to different design statements, not a single verified SKU. Configurable operating modes require confirmation.

Potential use: Low-profile forward perception candidate. All specifications are manufacturer claims and are **not independent hardware, ROS2, algorithm, automotive functional safety or integrated robotic-system verification**. Confirm exact configuration, interfaces, timing, packet format and production availability before integration.

**Evidence reference:** SRC-LDR-0080. See `validation_framework/wave_a/batch_0076_0080/manufacturer_evidence_claims.csv`.

# CMP-LDR-0079 — Innoviz Technologies InnovizTwo

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Automotive long-range solid-state 3D LiDAR
- **Orderable/model designation:** InnovizTwo; exact SKU and firmware to confirm
- **Official manufacturer source:** https://innoviz.tech/innoviztwo

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| maximum_angular_resolution_h | 0.05 | deg |
| maximum_angular_resolution_v | 0.05 | deg |
| frame_rate_options | 10/20 | FPS |
| minimum_detection_range | 0.3 | m |
| maximum_detection_range | 300 | m |
| maximum_horizontal_fov | 120 | deg |
| maximum_vertical_fov | 43 | deg |
| dimensions_h | 46 | mm |
| dimensions_w | 137 | mm |
| dimensions_d | 132 | mm |

## Evidence scope and integration cautions

Published max metrics may depend on configuration; no assertion all maximum values occur simultaneously. Manufacturer safety compliance claim does not certify integrated robot.

Potential use: Automotive forward obstacle detection candidate. All specifications are manufacturer claims and are **not independent hardware, ROS2, algorithm, automotive functional safety or integrated robotic-system verification**. Confirm exact configuration, interfaces, timing, packet format and production availability before integration.

**Evidence reference:** SRC-LDR-0079. See `validation_framework/wave_a/batch_0076_0080/manufacturer_evidence_claims.csv`.

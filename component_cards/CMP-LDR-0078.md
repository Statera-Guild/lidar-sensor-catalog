# CMP-LDR-0078 — Innoviz Technologies SMART Hawk

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Wide-FOV short-to-mid-range solid-state 3D LiDAR
- **Orderable/model designation:** SMART Hawk; exact SKU and firmware to confirm
- **Official manufacturer source:** https://innoviz.tech/products

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| range_at_10pct_approx | 150 | m |
| horizontal_fov | 115.2 | deg |
| vertical_fov | 70 | deg |
| horizontal_angular_resolution | 0.08 | deg |
| vertical_angular_resolution | 0.15 | deg |
| maximum_digital_range | 150 | m |
| frame_rate | 10 | FPS |
| wavelength | 905 | nm |
| point_rate_approx | 8.76 | Mpixel/s |

## Evidence scope and integration cautions

Manufacturer lists availability Q3 2026; actual orderability and production status not independently verified. 10-percent-reflectivity range approximate.

Potential use: Wide vertical FOV obstacle perception candidate. All specifications are manufacturer claims and are **not independent hardware, ROS2, algorithm, automotive functional safety or integrated robotic-system verification**. Confirm exact configuration, interfaces, timing, packet format and production availability before integration.

**Evidence reference:** SRC-LDR-0078. See `validation_framework/wave_a/batch_0076_0080/manufacturer_evidence_claims.csv`.

# CMP-LDR-0077 — Innoviz Technologies SMART Raven+

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Long-range tall-FOV solid-state 3D LiDAR
- **Orderable/model designation:** SMART Raven+; exact SKU and firmware to confirm
- **Official manufacturer source:** https://innoviz.tech/products

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| range_at_10pct_approx | 300 | m |
| horizontal_fov | 120 | deg |
| vertical_fov | 38.4 | deg |
| horizontal_angular_resolution | 0.08 | deg |
| vertical_angular_resolution | 0.075 | deg |
| maximum_digital_range | 310 | m |
| frame_rate | 10 | FPS |
| wavelength | 905 | nm |
| point_rate_approx | 7.4 | Mpixel/s |

## Evidence scope and integration cautions

Manufacturer vertical angular resolution also lists parenthetical ±0.025 degrees; 0.075 degree is table headline. All values are manufacturer claims.

Potential use: Tall-FOV forward perception candidate. All specifications are manufacturer claims and are **not independent hardware, ROS2, algorithm, automotive functional safety or integrated robotic-system verification**. Confirm exact configuration, interfaces, timing, packet format and production availability before integration.

**Evidence reference:** SRC-LDR-0077. See `validation_framework/wave_a/batch_0076_0080/manufacturer_evidence_claims.csv`.

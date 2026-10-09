# CMP-LDR-0076 — Innoviz Technologies SMART Raven

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Long-range solid-state 3D LiDAR
- **Orderable/model designation:** SMART Raven; exact SKU and firmware to confirm
- **Official manufacturer source:** https://innoviz.tech/products

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| range_at_10pct_approx | 300 | m |
| horizontal_fov | 120 | deg |
| vertical_fov | 24 | deg |
| horizontal_angular_resolution | 0.1 | deg |
| vertical_angular_resolution | 0.05 | deg |
| maximum_digital_range | 450 | m |
| frame_rate | 10 | FPS |
| wavelength | 905 | nm |
| point_rate_approx | 5.8 | Mpixel/s |

## Evidence scope and integration cautions

Manufacturer comparison gives Raven vertical FOV 24 degrees with parenthetical 31 degrees alternative; record 24 only. Approximate 10-percent-reflectivity range is not max digital range.

Potential use: Forward long-range object detection candidate. All specifications are manufacturer claims and are **not independent hardware, ROS2, algorithm, automotive functional safety or integrated robotic-system verification**. Confirm exact configuration, interfaces, timing, packet format and production availability before integration.

**Evidence reference:** SRC-LDR-0076. See `validation_framework/wave_a/batch_0076_0080/manufacturer_evidence_claims.csv`.

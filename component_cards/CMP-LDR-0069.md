# CMP-LDR-0069 — Hesai JT32

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Compact 360-degree 3D LiDAR
- **Orderable/model designation:** JT32; confirm exact SKU and firmware
- **Official manufacturer source:** https://www.hesaitech.com/product/jt16/

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| channels | 32 | channels |
| range_max | 65 | m |
| horizontal_fov | 360 | deg |
| vertical_fov | 42.6 | deg |
| single_return_point_rate | 192000 | pts/s |
| power_typical | 4.3 | W |
| scan_frequency | 5/10 | Hz |

## Evidence scope and integration cautions

JT32 claims only; official shared JT32/16 page also describes JT16 separately.

Potential use: Compact robotic 3D obstacle perception candidate. Manufacturer web specifications are catalog evidence, **not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Confirm operating conditions, interfaces, firmware, timestamps and exact variant before implementation.

**Evidence reference:** SRC-LDR-0069. See `validation_framework/wave_a/batch_0066_0070/manufacturer_evidence_claims.csv`.

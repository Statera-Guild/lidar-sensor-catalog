# CMP-LDR-0067 — Hesai OT128

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 360-degree long-range 3D LiDAR
- **Orderable/model designation:** OT128; confirm exact SKU and firmware
- **Official manufacturer source:** https://www.hesaitech.com/product/ot128/

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| range_at_10pct | 200 | m |
| range_max | 230 | m |
| horizontal_fov | 360 | deg |
| vertical_fov | 40 | deg |
| single_return_point_rate | 3456000 | pts/s |
| dual_return_point_rate | 6912000 | pts/s |
| power_typical | 29 | W |

## Evidence scope and integration cautions

Manufacturer operating conditions apply; no vehicle or ROS2 validation.

Potential use: 360-degree outdoor 3D perception candidate. Manufacturer web specifications are catalog evidence, **not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Confirm operating conditions, interfaces, firmware, timestamps and exact variant before implementation.

**Evidence reference:** SRC-LDR-0067. See `validation_framework/wave_a/batch_0066_0070/manufacturer_evidence_claims.csv`.

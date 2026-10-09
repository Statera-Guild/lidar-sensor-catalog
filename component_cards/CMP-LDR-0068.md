# CMP-LDR-0068 — Hesai JT128

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Hyper-hemispherical short-range 3D LiDAR
- **Orderable/model designation:** JT128; confirm exact SKU and firmware
- **Official manufacturer source:** https://www.hesaitech.com/product/jt128/

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| channels | 128 | channels |
| range_at_10pct | 40 | m |
| range_max | 60 | m |
| horizontal_fov | 360 | deg |
| vertical_fov | 189 | deg |
| single_return_point_rate | 1152000 | pts/s |
| mass | 265 | g |

## Evidence scope and integration cautions

JT128 variant claims only; do not apply automatically to JT64P.

Potential use: Wide-FOV robotic SLAM / obstacle perception candidate. Manufacturer web specifications are catalog evidence, **not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Confirm operating conditions, interfaces, firmware, timestamps and exact variant before implementation.

**Evidence reference:** SRC-LDR-0068. See `validation_framework/wave_a/batch_0066_0070/manufacturer_evidence_claims.csv`.

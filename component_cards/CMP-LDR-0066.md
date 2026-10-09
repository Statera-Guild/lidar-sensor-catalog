# CMP-LDR-0066 — Hesai ATX

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Long-range forward-looking 3D LiDAR
- **Orderable/model designation:** ATX; confirm exact SKU and firmware
- **Official manufacturer source:** https://www.hesaitech.com/product/atx/

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| range_at_10pct | 230 | m |
| horizontal_fov | 120 | deg |
| vertical_fov | 20 | deg |
| highest_supported_channels | 256 | channels |
| max_single_return_point_rate | 3840000 | pts/s |
| power_typical | 8 | W |
| mass | 360 | g |

## Evidence scope and integration cautions

ATX model; supported channels and maximum rates are capability limits, not guaranteed concurrent operating settings.

Potential use: Long-range obstacle perception candidate. Manufacturer web specifications are catalog evidence, **not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Confirm operating conditions, interfaces, firmware, timestamps and exact variant before implementation.

**Evidence reference:** SRC-LDR-0066. See `validation_framework/wave_a/batch_0066_0070/manufacturer_evidence_claims.csv`.

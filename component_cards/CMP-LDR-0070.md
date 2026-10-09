# CMP-LDR-0070 — Hesai FTX

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** Solid-state ultra-wide short-range 3D LiDAR
- **Orderable/model designation:** FTX; confirm exact SKU and firmware
- **Official manufacturer source:** https://www.hesaitech.com/product/ftx/

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| variant_horizontal_fov | 180 | deg |
| variant_vertical_fov | 140 | deg |
| variant_range_at_10pct | 20 | m |
| variant_single_return_point_rate | 492000 | pts/s |
| variant_scan_frequency | 10 | Hz |
| variant_power_upper_bound | 6 | W |

## Evidence scope and integration cautions

Claims refer specifically to FTX HFOV 180-degree variant; 140-degree variant differs. Power value is upper bound (<6 W).

Potential use: Short-range blind-spot / close obstacle perception candidate. Manufacturer web specifications are catalog evidence, **not independent hardware, ROS2, algorithm, functional safety or system-level verification**. Confirm operating conditions, interfaces, firmware, timestamps and exact variant before implementation.

**Evidence reference:** SRC-LDR-0070. See `validation_framework/wave_a/batch_0066_0070/manufacturer_evidence_claims.csv`.

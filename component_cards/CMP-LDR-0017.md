# CMP-LDR-0017 — Hokuyo UST-05LX

- Manufacturer: Hokuyo
- Model: UST-05LX
- Orderable SKU: UST-05LX
- Sensor class: 2D planar
- Catalog status: listed
- Verification status: not_verified
- Algorithm test status: not_tested

## Manufacturer primary evidence

- URL: https://www.hokuyo-aut.jp/search/single.php?serial=227
- Access date: 2026-10-10
- Source type: manufacturer_model_spec

## Manufacturer-backed claims

- range_white: 0.06-5 m (white Kent sheet)
- range_10pct: 0.06-2 m (diffuse reflectance 10%)
- horizontal_fov: 270 deg (manufacturer spec)
- scan_period: 25 ms (manufacturer spec)
- interface: 100BASE-TX Ethernet (manufacturer spec)

## Qualification / open gates

15m maximum performance is not the specified 5m white-target range.

Manufacturer source review is not hardware verification. Driver, ROS2, synchronization and algorithm interoperability remain not_tested.

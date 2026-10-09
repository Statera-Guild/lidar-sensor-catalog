# CMP-LDR-0018 — SLAMTEC RPLIDAR C1

- Manufacturer: SLAMTEC
- Model: RPLIDAR C1
- Orderable SKU: TBD; see variant notes
- Sensor class: 2D planar
- Catalog status: listed
- Verification status: not_verified
- Algorithm test status: not_tested

## Manufacturer primary evidence

- URL: https://www.slamtec.com/en/c1/spec
- Access date: 2026-10-10
- Source type: manufacturer_model_spec

## Manufacturer-backed claims

- range_70pct: 0.05-12 m (70% reflectivity)
- range_10pct: 0.05-6 m (10% reflectivity)
- sample_rate: 5000 samples/s (manufacturer spec)
- scan_frequency: 8-12 Hz (10 Hz typical)
- interface: TTL UART 460800 (manufacturer spec)

## Qualification / open gates

Exact C1 kit SKU/revision unresolved; official ROS2 support statement is not a tested integration.

Manufacturer source review is not hardware verification. Driver, ROS2, synchronization and algorithm interoperability remain not_tested.

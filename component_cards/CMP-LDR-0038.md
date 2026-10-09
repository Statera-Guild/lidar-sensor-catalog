# CMP-LDR-0038 — Livox Mid-40

- Manufacturer: Livox
- Model: Mid-40
- Orderable SKU / revision: Not independently confirmed
- Class: 3D non-repetitive
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.livoxtech.com/mid-40-and-mid-100/specs
- Source type: manufacturer_product_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_10pct: **90 m** — 10% reflectivity at 100 klx
- range_20pct: **130 m** — 20% reflectivity at 100 klx
- range_80pct: **260 m** — 80% reflectivity at 100 klx; not 10% range
- fov: **38.4 deg circular** — Mid-40 variant
- point_rate: **100000 points/s** — Mid-40 variant
- interface: **Ethernet** — manufacturer published
- sync: **IEEE 1588-2008 PTPv2; PPS** — manufacturer capability; not bench-tested
- power_typical: **10 W** — start-up power higher; fan IP55

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, orderable SKU, and certification validity remain unverified. Not a machine-safety approval.

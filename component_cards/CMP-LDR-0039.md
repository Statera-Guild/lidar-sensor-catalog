# CMP-LDR-0039 — Livox Mid-100

- Manufacturer: Livox
- Model: Mid-100
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
- fov: **98.4 x 38.4 deg** — horizontal x vertical; Mid-100 variant
- point_rate: **300000 points/s** — Mid-100 variant
- interface: **Ethernet** — manufacturer published
- sync: **IEEE 1588-2008 PTPv2; PPS** — manufacturer capability; not bench-tested
- power_typical: **30 W** — start-up power higher; fan IP55

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, orderable SKU, and certification validity remain unverified. Not a machine-safety approval.

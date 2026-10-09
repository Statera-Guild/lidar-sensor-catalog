# CMP-LDR-0034 — Livox Horizon

- Manufacturer: Livox
- Model: Horizon
- Orderable SKU / revision: Not independently confirmed
- Class: 3D non-repetitive
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.livoxtech.com/3296f540ecf5458a8829e01cf429798e/assets/horizon/Livox%20Horizon%20user%20manual%20v1.0.pdf
- Source type: manufacturer_user_manual_v1.0
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_10pct: **90 m** — 10% reflectivity; 100 klx
- range_20pct: **130 m** — 20% reflectivity; 100 klx
- range_80pct: **260 m** — 80% reflectivity; 100 klx
- fov: **81.7 x 25.1 deg** — horizontal x vertical
- point_rate_single: **240000 points/s** — first or strongest return
- point_rate_dual: **480000 points/s** — dual return
- data_latency: **<=2 ms** — manufacturer published typical/limit

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, SKU availability, and certification validity remain unverified. This is not a machine-safety approval.

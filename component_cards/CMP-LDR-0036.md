# CMP-LDR-0036 — Hokuyo UST-10LX-H01

- Manufacturer: Hokuyo
- Model: UST-10LX-H01
- Orderable SKU / revision: Not independently confirmed
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=167
- Source type: manufacturer_product_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_white: **0.06-10 m** — white Kent sheet
- range_10pct: **0.06-4 m** — 10% diffuse reflectance
- max_data_distance: **30 m** — maximum output distance; not guaranteed detection
- scan_angle: **270 deg** — planar scan
- scan_period: **25 ms** — 40 Hz
- angular_resolution: **0.125 deg** — H01-specific; do not confuse with standard UST-10LX
- interface: **Ethernet 100BASE-TX** — manufacturer published
- ambient_light: **less than 15000 lx** — H01-specific; not standard variant

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, orderable SKU, and certification validity remain unverified. Not a machine-safety approval.

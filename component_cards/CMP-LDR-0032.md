# CMP-LDR-0032 — Hokuyo UXM-30LX-EW

- Manufacturer: Hokuyo
- Model: UXM-30LX-EW
- Orderable SKU / revision: Not independently confirmed
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=171
- Source type: manufacturer_product_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_assured: **0.1-30 m** — manufacturer assured detection; target/illumination conditions apply
- maximum_output_range: **100 m** — data-output limitation; not assured detection
- horizontal_fov: **190 deg** — scan angle
- scan_period: **50 ms** — 20 Hz nominal
- angular_resolution: **0.25 deg** — 360/1440
- interface: **Ethernet 100BASE-TX** — manufacturer specification
- multi_echo: **supported** — manufacturer product overview
- protection: **IP67** — manufacturer specification

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, SKU availability, and certification validity remain unverified. This is not a machine-safety approval.

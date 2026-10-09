# CMP-LDR-0031 — Hokuyo UTM-30LX-EW

- Manufacturer: Hokuyo
- Model: UTM-30LX-EW
- Orderable SKU / revision: Not independently confirmed
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=170
- Source type: manufacturer_product_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_white: **0.1-30 m** — guaranteed range; white Kent sheet; indoor <1000 lx
- maximum_range: **60 m** — maximum data range; not guaranteed
- horizontal_fov: **270 deg** — scan angle
- scan_period: **25 ms** — 40 Hz nominal
- angular_resolution: **0.25 deg** — 360/1440
- interface: **Ethernet 100BASE-TX** — manufacturer specification
- multi_echo: **supported** — manufacturer product overview
- protection: **IP67 optics** — excludes Ethernet connector

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, SKU availability, and certification validity remain unverified. This is not a machine-safety approval.

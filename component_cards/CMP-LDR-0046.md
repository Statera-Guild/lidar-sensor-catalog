# CMP-LDR-0046 — Hokuyo UST-05LN

- Manufacturer: Hokuyo
- Model: UST-05LN
- Orderable SKU / revision: not confirmed
- Class: 2D area configuration
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=159
- Source type: Manufacturer product specification
- Evidence review date: 2026-10-10

## Source-backed specifications

- detection_range_white: **0.06-5 m** — white Kent sheet
- detection_range_10pct: **0.06-2 m** — 10% diffuse reflectance
- scan_angle: **270 deg** — planar
- scan_period: **25 ms** — motor 2400 rpm
- angular_resolution: **0.5 deg** — planar
- response_time: **66 ms initial** — configurable output delay; not scan period
- interface: **USB** — configuration interface; area outputs are photocoupler open collector
- ingress_protection: **IP65** — manufacturer published
- supply: **DC 10-30 V** — nominal 12/24 V
- output_type: **NPN** — UST-05LN; UST-05LNP is PNP

## Validation boundary

Area configuration sensor: do not assume raw scan streaming or ROS2 LaserScan support; not a certified personnel-safety scanner.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability and safety suitability remain unverified.

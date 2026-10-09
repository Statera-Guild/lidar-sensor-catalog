# CMP-LDR-0027 — Hokuyo UST-15LX

- Manufacturer: Hokuyo
- Model: UST-15LX
- Orderable SKU / revision: TBD — confirm ordering code and hardware revision
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=245
- Source type: manufacturer_product_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_white: **0.05-15 m** — white Kent sheet
- range_10pct: **0.05-6 m** — 10% diffuse reflectance
- horizontal_fov: **270 deg** — scan angle
- scan_period: **25 ms** — 40 Hz
- interface: **Ethernet 100BASE-TX** — manufacturer spec
- ip_rating: **IP67** — manufacturer spec

## Validation boundary

Manufacturer published specifications only. Actual hardware measurements, firmware-specific behavior, ROS2 compatibility, algorithm benchmarking, lifecycle and procurement availability remain unverified. Never treat this card as machine-safety approval.

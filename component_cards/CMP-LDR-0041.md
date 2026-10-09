# CMP-LDR-0041 — Hokuyo UGM-50LXP

- Manufacturer: Hokuyo
- Model: UGM-50LXP
- Orderable SKU / revision: UUGM001
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=231
- Source type: manufacturer product page / manual
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_10pct: **0.1-50 m** — 10% reflectance black paper 500x500mm; guaranteed detection
- range_90pct: **0.1-120 m** — 90% reflectance white Kent paper 1400x1400mm; guaranteed detection
- scan_angle: **190 deg** — planar
- scan_period_normal: **20 ms** — normal mode 3000rpm
- angular_resolution_normal: **approx 0.32 deg** — normal mode
- angular_resolution_high: **approx 0.08 deg** — high resolution mode 80ms
- ingress_protection: **IP67** — manufacturer-published
- interface: **Ethernet** — M12 D-coded Ethernet connector
- power: **24 W or less** — sensor steady state; heater separate up to 48W
- output_type: **PNP** — UGM-50LXP only; NPN is UGM-50LXN

## Validation boundary

Manufacturer lists order code UUGM001; safety certification for personnel detection not established.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability, and safety suitability remain unverified. Do not infer personnel-safety certification from laser Class 1.

# CMP-LDR-0045 — Hokuyo UST-10LXB-H02

- Manufacturer: Hokuyo
- Model: UST-10LXB-H02
- Orderable SKU / revision: UUST163
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=256
- Source type: manufacturer product page / manual
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_white: **0.06-10 m** — white Kent sheet; guaranteed
- range_10pct: **0.06-4 m** — 10% diffuse reflectance; guaranteed
- max_output_distance: **30 m** — output limit; not guaranteed detection
- scan_angle: **270 deg** — planar
- scan_period: **25 ms** — 40Hz
- angular_resolution: **0.125 deg** — H02 PoE variant
- power_interface: **PoE IEEE 802.3af Class 0** — 37-57V; 3W normal 5W startup
- interface: **Ethernet 100BASE-TX** — single LAN cable via PoE
- ingress_protection: **IP40** — not weatherproof

## Validation boundary

Manufacturer lists order code UUST163; PoE module required; differs from UST-10LX-H01.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability, and safety suitability remain unverified. Do not infer personnel-safety certification from laser Class 1.

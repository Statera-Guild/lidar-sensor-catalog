# CMP-LDR-0042 — Hokuyo YVT-35LX-F0

- Manufacturer: Hokuyo
- Model: YVT-35LX-F0
- Orderable SKU / revision: Not independently confirmed
- Class: 3D scanning
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=224
- Source type: manufacturer product page / manual
- Evidence review date: 2026-10-10

## Source-backed specifications

- horizontal_fov: **210 deg** — horizontal steering
- vertical_fov: **40 deg** — -5 to +35 deg
- range_white_center: **0.3-35 m** — white paper; center forward sector -45 to +45 deg at vertical +15 deg
- range_10pct_center: **0.3-11 m** — 10% reflectance black paper; center forward sector
- points_per_frame: **2590 or more** — non-interlace at 20 fps
- frame_rate: **20 fps** — non-interlace mode
- multi_echo: **up to 4** — reported returns
- interface: **Ethernet 100BASE-TX** — TCP/IP
- time_sync: **PPS input** — not proof of PTP support
- ingress_protection: **IP67** — manufacturer conditions; not functional safety rated

## Validation boundary

Model F0 specifically; FK is quieter variant. Manufacturer explicitly says not certified for functional safety.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability, and safety suitability remain unverified. Do not infer personnel-safety certification from laser Class 1.

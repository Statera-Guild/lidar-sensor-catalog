# CMP-LDR-0048 — SLAMTEC RPLIDAR S2P

- Manufacturer: SLAMTEC
- Model: RPLIDAR S2P
- Orderable SKU / revision: S2M1-RxP
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.slamtec.com/en/s2/spec
- Source type: Manufacturer S2 model comparison
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_90pct: **0.05-50 m** — 90% reflectivity; S2P column only
- range_10pct: **0.05-15 m** — 10% reflectivity; S2P column only
- scan_angle: **360 deg** — planar rotation; series overview
- sampling_frequency: **32000 samples/s** — S2 family table
- scan_frequency: **10 Hz** — typical
- angular_resolution: **0.1125 deg** — typical
- interface: **UART serial 1 Mbps** — S2P; not S2E Ethernet
- ingress_protection: **IP65** — S2 series table

## Validation boundary

S2P is distinct from S2L and base S2; do not use S2L distance limits.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability and safety suitability remain unverified.

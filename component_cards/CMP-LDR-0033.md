# CMP-LDR-0033 — SLAMTEC RPLIDAR A2M7

- Manufacturer: SLAMTEC
- Model: RPLIDAR A2M7
- Orderable SKU / revision: A2M7
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.slamtec.com/en/lidar/a2spec
- Source type: manufacturer_variant_spec
- Evidence review date: 2026-10-10

## Source-backed specifications

- range: **0.2-16 m** — A2M7 only; do not substitute A2M8 or A2M12
- horizontal_fov: **360 deg** — planar scanning
- sample_rate: **16000 samples/s** — A2M7 variant
- scan_frequency: **5-15 Hz** — 10 Hz typical
- angular_resolution: **0.225 deg** — A2M7 nominal
- interface: **UART 256000 bps** — A2M7 variant
- supply: **5 V** — manufacturer specification

## Validation boundary

Manufacturer-published specifications only. Hardware measurement, ROS2 driver compatibility, algorithm benchmarking, firmware-specific behavior, SKU availability, and certification validity remain unverified. This is not a machine-safety approval.

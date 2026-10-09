# CMP-LDR-0028 — SLAMTEC RPLIDAR S1

- Manufacturer: SLAMTEC
- Model: RPLIDAR S1
- Orderable SKU / revision: TBD — confirm ordering code and hardware revision
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed, not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://wiki.slamtec.com/download/attachments/83066883/LD601_SLAMTEC_rplidar_datasheet_S1_v1.7_en.pdf?api=v2&modificationDate=1677815319000&version=1
- Source type: manufacturer_datasheet
- Evidence review date: 2026-10-10

## Source-backed specifications

- range_white: **40 m** — white target; datasheet v1.7
- range_black: **10 m** — black target; datasheet v1.7
- horizontal_fov: **360 deg** — 2D planar scanner
- sample_rate: **9200 samples/s** — typical at 10 Hz
- scan_frequency: **8-15 Hz** — adjustable; typical 10 Hz
- interface: **TTL UART** — datasheet

## Validation boundary

Manufacturer published specifications only. Actual hardware measurements, firmware-specific behavior, ROS2 compatibility, algorithm benchmarking, lifecycle and procurement availability remain unverified. Never treat this card as machine-safety approval.

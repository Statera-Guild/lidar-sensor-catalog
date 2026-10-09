# CMP-LDR-0043 — SLAMTEC RPLIDAR A1

- Manufacturer: SLAMTEC
- Model: RPLIDAR A1
- Orderable SKU / revision: Not independently confirmed
- Class: 2D planar
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.slamtec.com/en/lidar/a1spec
- Source type: manufacturer product page / manual
- Evidence review date: 2026-10-10

## Source-backed specifications

- measuring_range: **0.15-12 m** — manufacturer A1 spec; range depends on target
- scan_angle: **360 deg** — planar
- sampling_frequency: **8000 samples/s** — manufacturer A1 spec
- rotational_speed: **5.5 Hz** — nominal spec; adjustable 2-10Hz described on overview
- angular_resolution: **<=1 deg** — manufacturer spec
- output: **UART serial 3.3V** — electrical UART output; USB via adapter is distinct
- power: **0.5 W** — 5V 100mA nominal
- operating_temperature: **0 to 40 C** — manufacturer spec

## Validation boundary

A1 family; exact A1 hardware revision/SKU and driver behavior not established.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability, and safety suitability remain unverified. Do not infer personnel-safety certification from laser Class 1.

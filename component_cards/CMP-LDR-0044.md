# CMP-LDR-0044 — Hesai Pandar40P

- Manufacturer: Hesai
- Model: Pandar40P
- Orderable SKU / revision: Not independently confirmed
- Class: 3D spinning
- Catalog status: **listed** (manufacturer-source backed; not device-verified)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**

## Manufacturer evidence

- Official source: https://www.hesaitech.com/wp-content/uploads/2025/04/Pandar40P_User_Manual_402-en-241220.pdf
- Source type: manufacturer product page / manual
- Evidence review date: 2026-10-10

## Source-backed specifications

- laser_channels: **40** — Pandar40P channel distribution / model naming; see manufacturer manual
- range_10pct: **200 m** — 10% reflectivity; manufacturer Pandar40P product article and manual channel-dependent capability
- data_transmission: **100BASE-TX** — manufacturer manual
- single_return_points: **720000 points/s** — single-return configuration
- dual_return_points: **1440000 points/s** — dual-return configuration
- time_sync: **GPS/PTP** — PTP 1588v2 and 802.1AS listed
- power: **18 W typical** — manufacturer manual
- ingress_protection: **IP6K7** — manufacturer manual

## Validation boundary

Channel instrumented ranges vary; 200m reflectivity claim not universal for every channel. Confirm manual revision and purchase SKU.

Manufacturer-published specifications only. Hardware measurements, ROS2 driver compatibility, SLAM/obstacle detection benchmarks, procurement availability, and safety suitability remain unverified. Do not infer personnel-safety certification from laser Class 1.

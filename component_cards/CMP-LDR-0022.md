# CMP-LDR-0022 — Hokuyo UST-30LX

- Manufacturer: Hokuyo
- Model: UST-30LX
- Orderable SKU / revision: TBD
- Class: 2D planar
- Catalog status: listed (manufacturer-source-backed; not hardware-verified)
- Verification status: not_verified
- Algorithm test status: not_tested

## Manufacturer evidence

- Official source: https://www.hokuyo-aut.jp/search/single.php?serial=233
- Evidence scope: model_specific_evidence
- Reviewed on: 2026-10-10

## Source-backed claims

- range_white: 0.05-30 m (white Kent sheet)
- range_10pct: 0.05-12 m (10% diffuse reflectance)
- horizontal_fov: 270 deg (scan angle)
- scan_period: 25 ms (scan speed)
- interface: Ethernet 100BASE-TX (manufacturer spec)

## Limitations and next gate

UUST1** vs UUST2** firmware generations must not be interchanged; exact order code pending.

Evidence-backed catalog listing does not mean physical verification, current procurement availability, ROS2 interoperability, or safety certification.

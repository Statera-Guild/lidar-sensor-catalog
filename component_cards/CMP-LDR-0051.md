# CMP-LDR-0051 — SLAMTEC RPLIDAR S2E

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D scanner
- **Orderable/model designation:** S2M1-RxE
- **Official manufacturer source:** https://www.slamtec.com/en/s2/spec

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| distance_90pct_m | 0.05-30 | m |
| distance_10pct_m | 0.05-10 | m |
| scan_rate | 10 | Hz |
| sample_rate | 32000 | samples/s |
| angular_resolution | 0.1125 | deg |
| interface | Ethernet UDP 10/100M | text |
| voltage | 12 | V |
| protection | IP65 | rating |

## Integration and evidence boundaries

Ethernet UDP model; ROS2 interface must be validated with SDK and actual hardware.

This card records manufacturer-stated claims only. No hardware inspection, timing validation, ROS2 integration test, safety validation, or independent benchmark has been performed.

**Evidence reference:** SRC-LDR-0051. See `validation_framework/wave_a/batch_0051_0055/manufacturer_evidence_claims.csv`.

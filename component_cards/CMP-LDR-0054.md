# CMP-LDR-0054 — SLAMTEC LPX-T1M4

- **Catalog status:** listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D scanner
- **Orderable/model designation:** T1M4
- **Official manufacturer source:** https://www.slamtec.com/en/t1/spec

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| distance_70pct_m | 0.05-40 | m |
| distance_10pct_m | 0.05-15 | m |
| angular_range | 270 | deg |
| sample_rate | 60000 | samples/s |
| scan_rate_typical | 20 | Hz |
| scan_rate_range | 20-40 | Hz |
| angular_resolution | 0.12 | deg |
| interface | Ethernet | text |
| voltage | 9-28 | VDC |
| power_typical | 4 | W |

## Integration and evidence boundaries

SDK and ROS2 driver compatibility not validated; no safety certification inferred.

This card records manufacturer-stated claims only. No hardware inspection, timing validation, ROS2 integration test, safety validation, or independent benchmark has been performed.

**Evidence reference:** SRC-LDR-0054. See `validation_framework/wave_a/batch_0051_0055/manufacturer_evidence_claims.csv`.

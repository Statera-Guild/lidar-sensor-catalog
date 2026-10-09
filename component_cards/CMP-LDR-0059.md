# CMP-LDR-0059 — SICK nanoScan3

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D safety laser scanner
- **Orderable/model designation:** nanoScan3 family
- **Official manufacturer source:** https://www.sick.com/media/familyoverview/6/56/056/familyOverview_nanoScan3_g507056_en.pdf

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| protective_field_range | 3 | m |
| warning_field_range | 10 | m |
| scanning_angle | 275 | deg |
| safety_level | PL d / SIL 2 / Type 3 | text |
| number_of_fields | 8 or 128 depending on variant | fields |
| application | indoor | text |
| height | 80 | mm |

## Integration and evidence boundaries

SAFETY SENSOR: certified function needs exact SKU and system safety engineering; do not equate ROS2 stream with safety-rated protective output

This card records manufacturer-stated claims only. No independent hardware verification, ROS2 device integration, safety certification of the complete system, or algorithm benchmark has been performed.

**Evidence reference:** SRC-LDR-0059. See `validation_framework/wave_a/batch_0056_0060/manufacturer_evidence_claims.csv`.

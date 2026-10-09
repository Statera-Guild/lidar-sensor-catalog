# CMP-LDR-0060 — SICK outdoorScan3

- **Catalog status:** family_listed
- **Verification:** not_verified
- **Algorithm test:** not_tested
- **Sensor class:** 2D outdoor safety laser scanner
- **Orderable/model designation:** outdoorScan3 family
- **Official manufacturer source:** https://www.sick.com/media/docs/3/63/763/product_information_outdoorscan3_safety_laser_scanner_en_im0082763.pdf

## Manufacturer-stated specifications

| Property | Value | Unit |
|---|---|---|
| protective_field_range | 4 | m |
| warning_field_range | 40 | m |
| scanning_angle | 275 | deg |
| angular_resolution | 0.39 | deg |
| application | outdoor | text |
| safety_level | PL d / SIL 2 / Type 3 | text |
| number_of_fields | 8 or 128 depending on variant | fields |

## Integration and evidence boundaries

SAFETY SENSOR: certification is variant/application dependent; ROS2 measurement output and functional safety cannot be inferred from family listing

This card records manufacturer-stated claims only. No independent hardware verification, ROS2 device integration, safety certification of the complete system, or algorithm benchmark has been performed.

**Evidence reference:** SRC-LDR-0060. See `validation_framework/wave_a/batch_0056_0060/manufacturer_evidence_claims.csv`.

# Alignment & Calibration

This section covers the step-by-step procedures for aligning, calibrating, and commissioning
the NV2 instrument. Procedures should generally be performed in the order listed when bringing
up the system from scratch.

## Recommended Order

1. {doc}`Sample Mounting <sample_mounting>` — mount and verify the diamond sample
2. {doc}`Optics Alignment <optics_alignment>` — align excitation and collection paths
3. {doc}`Magnetic Field Alignment <magnetic_field_alignment>` — align bias field to an NV axis
4. {doc}`CW ODMR <cw_odmr>` — verify NV spin resonance and check overall sensitivity
5. {doc}`IQ Calibration <iq_calibration>` — calibrate IQ mixer for clean single-sideband output

## Quick Diagnostics

| Check | Expected | Action if failed |
|-------|----------|-----------------|
| Laser power at objective | | Realign AOM |
| APD count rate (no MW) | | Check collection path |
| ODMR contrast | | See {doc}`CW ODMR <cw_odmr>` |

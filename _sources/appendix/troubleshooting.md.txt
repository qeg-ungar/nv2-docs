# Troubleshooting

Diagnostic tools and known solutions for common problems with the NV2 setup.
For calibration-specific issues see the relevant pages in {doc}`Alignment & Calibration <../calibration/index>`.

---

## Optics & Detection

### No APD / SPCM counts

| Step | Check | Notes |
|------|-------|-------|
| 1 | Is the laser shutter open? | |
| 2 | Is the AOM RF drive on? | Check signal generator output |
| 3 | Is the APD power supply on? | |
| 4 | Re-run {doc}`optics alignment <../calibration/optics_alignment>` | |

### Low count rate (< expected)

*Add: threshold values, common causes (laser power drift, fiber coupling drift, objective contamination).*

### High background / low contrast

*Add: typical background sources (Raman from diamond, substrate autofluorescence, stray 532 nm), mitigation steps.*

---

## RF / MW

### No ODMR signal

| Step | Check | Notes |
|------|-------|-------|
| 1 | Is the signal generator output on and at correct frequency? | |
| 2 | Measure MW power at PCB with power meter | Expected: |
| 3 | Check SMA connections from chain to PCB | |
| 4 | Verify antenna S11 with VNA or power meter | |

### ODMR contrast suddenly dropped

*Add: common causes (IQ calibration drift, MW amplifier overheating, antenna contact issue).*

---

## Control Electronics

### OPX not responding

*Add: restart procedure, QUA connection debug steps.*

### NI card errors

*Add: common NI DAQmx error codes and fixes.*

### Piezo not scanning

*Add: voltage check, controller reset procedure.*

---

## Temperature Control

### Heater PID not stabilizing

*Add: tuning procedure, sensor check, heater continuity test.*

---

## Software

### Common error messages

| Error | Cause | Fix |
|-------|-------|-----|
| | | |

---

## Known Quirks

*Document persistent, non-critical oddities about the setup that are "normal" but could alarm a new user.*

- *Example: The XYZ piezo stage has ~5 µm backlash on the Z axis; always approach focus from below.*

# Experiments & Applications

This section documents the standard NV center experiments available on the NV2 instrument,
including control sequences, acquisition parameters, and analysis procedures.

The microwave power sets the timescale for Rabi oscillations, which ultimately determines the pulse durations for spin control (from tens of nanoseconds up to ~ 1 $\mu$s). For single NV experiments, the optimal green excitation power is around 0.5 mW. The timescale for optical initialization and readout are determined by the metastable state lifetime which is on the order of a few hundred nanoseconds (cite). In a typical confocal setup the light collection efficiency is below 10%, and typically collect ~ 50 kilocounts per second per NV over an integration time of ~ 500 ns, yielding ~ .025 photons per measurement. So our detectors must be sensitive and fast enough to detect single photons at this timescale. We run measurements with many repetitions to collect a statistically significant signal, usally averaging between 100k to 1M shots.


## Experiment Overview

| Experiment | Detection | Modality | Page |
|------------|-----------|----------|------|
| Confocal imaging & scanning | APD / SPCM | Spatial imaging | {doc}`Confocal Imaging <confocal_imaging>` |
| CW ODMR | APD / SPCM | MW spectroscopy | {doc}`CW ODMR <../calibration/cw_odmr>` |
| RF / nuclear spin control | APD / SPCM | Pulsed RF | {doc}`RF Nuclear Spin <rf_nuclear_spin>` |
| Wide-field SPAD array detection | SPAD array | Spatial + spin | {doc}`SPAD Array Detection <spad_array_detection>` |

## Control Software Quick Reference

| Experiment | QUA Program | Launch |
|------------|-------------|--------|
| Confocal scan | | |
| Pulsed ODMR | | |
| Rabi | | |
| T1 | | |
| T2* (Ramsey) | | |
| T2 (Hahn echo) | | |

```{toctree}
:maxdepth: 1

confocal_imaging
rf_nuclear_spin
spad_array_detection
automation
```

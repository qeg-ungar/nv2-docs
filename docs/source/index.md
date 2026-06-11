# NV2 Lab Manual

## Introduction

Welcome to the Quantum Engineering Group's NV2 lab manual. This experimental setup is used for controlling and imaging NV centers in diamond. The setup was originally designed and built by the first generation of students in QEG (Clarice Aiello, Masashi Hirose, Ashok Ajoy, Alexandre Cooper aka Alex C). It was originally built for single NV experiments based on a confocal microscope setup, and during the Alex C era was adapted to perform microwave control of S = 1/2. The diamond sample still used in the setup today was fabricated in 2014. This documentation covers the hardware assemblies, calibration procedures, and experimental protocols for operating the setup. The manual is organized into three main sections: {doc}`System Overview <system_overview/index>`, {doc}`Alignment & Calibration <calibration/index>`, and {doc}`Experiments & Applications <experiments/index>`.

## Contact Info

| | |
|---|---|
| PhD student | Alex Ungar |
| Email | <ungar@mit.edu> |
| Lab | 26-311 |
| Office | 26-317 |
| PI | Prof. Paola Cappellaro |
| Lab website | <http://qeg.mit.edu/> |

```{toctree}
:maxdepth: 2
:caption: System Overview

system_overview/index
system_overview/excitation_optics
system_overview/imaging
system_overview/rf_electronics
system_overview/diamond_sample_pcb
system_overview/software
```

```{toctree}
:maxdepth: 2
:caption: Alignment & Calibration

calibration/index
calibration/optics_alignment
calibration/magnetic_field_alignment
calibration/iq_calibration
calibration/sample_mounting
calibration/cw_odmr
```

```{toctree}
:maxdepth: 2
:caption: Experiments & Applications

experiments/index
experiments/confocal_imaging
experiments/rf_nuclear_spin
experiments/spad_array_detection
```

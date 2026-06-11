# System Overview

This section describes the hardware assemblies and software components of the NV2 confocal microscope.
The instrument integrates several subsystems: optical excitation and detection, RF/microwave electronics,
control hardware, and diamond sample mounting.

```{figure} ../_static/images/system_block_diagram.png
:alt: Full system block diagram
:width: 100%
:align: center

Full system block diagram showing signal flow between hardware assemblies.
*(Replace with finalized wiring diagram.)*
```

## Subsections

| Section | Description |
|---------|-------------|
| {doc}`Excitation Optics <excitation_optics>` | 532 nm laser, AOM, and excitation beam path |
| {doc}`Imaging <imaging>` | Camera, alignment laser, and wide-field imaging path |
| {doc}`RF & Control Electronics <rf_electronics>` | QM OPX, MW/RF chain, signal generators, NI I/O card |
| {doc}`Diamond Sample & PCB <diamond_sample_pcb>` | Sample holder, PCB antenna, and thermal assembly |
| {doc}`Software Organization <software>` | Control software architecture and data flow |

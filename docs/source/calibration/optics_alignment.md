# Optics Alignment

This procedure covers alignment of the 532 nm excitation path, the confocal collection path,
and verification using fluorescence from the diamond sample or a reference fluorescent bead slide.

## Required Equipment

- 532 nm experiment laser (on)
- Alignment laser (on, low power)
- Alignment card / IR viewer
- Power meter
- Reference slide (fluorescent beads or diamond surface)

## Safety

```{warning}
532 nm laser light is hazardous to eyes. Wear appropriate laser safety goggles (OD ≥ 4 at 532 nm)
at all times when the laser shutter is open.
```

## Procedure

### 1. Rough Beam Path Alignment

*Describe the coarse alignment steps: iris positions, mirror steering sequence, beam height references.*

```{figure} ../_static/images/excitation_alignment_overview.png
:alt: Excitation path alignment reference
:width: 75%
:align: center

Key alignment points along the excitation path.
*(Figure placeholder — add annotated photograph or schematic.)*
```

### 2. AOM Alignment and Diffraction Efficiency

1. With the AOM RF drive off, align zero-order beam through the aperture.
2. Turn on RF drive and steer to maximize first-order diffraction power.
3. Measure power before and after AOM; record diffraction efficiency.

*Expected diffraction efficiency: add typical value.*

| Measurement Point | Power (mW) | Notes |
|-------------------|-----------|-------|
| Before AOM | | |
| After AOM (1st order) | | |
| At objective back aperture | | |

### 3. Objective Coupling and Beam Expansion

*Describe filling the objective back aperture, collimation check, and beam diameter measurement.*

### 4. Confocal Collection Alignment

*Describe pinhole or fiber coupling alignment for APD/SPCM: back-reflected alignment, optimizing
count rate on a bright fluorescent reference.*

### 5. Verification

- [ ] Laser spot visible on camera at sample plane
- [ ] APD counts increase when laser is on and sample is in focus
- [ ] Count rate > (expected threshold) on reference sample
- [ ] No stray light artifacts in confocal image

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No APD counts | Collection path misaligned | Re-align fiber coupler |
| Low count rate | AOM misaligned or power low | Re-optimize AOM |
| Bright background | Stray scatter | Check beam dumps, irises |

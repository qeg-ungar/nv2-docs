# CW ODMR

Continuous-wave optically detected magnetic resonance (CW ODMR) is the primary diagnostic for
verifying NV spin resonance, checking sensitivity, and calibrating the MW frequency. It is the
first NV experiment to run on a new sample or after any major realignment.

## Background

In CW ODMR, the 532 nm laser continuously initializes and reads out the NV spin while an MW tone
is swept in frequency. At resonance (f = 2.87 GHz ± Zeeman splitting), the spin is driven to the
m_s = ±1 state, reducing fluorescence (negative contrast). The resonance linewidth is limited by
power broadening and T₂* in the CW regime.

```{figure} ../_static/images/cw_odmr_example.png
:alt: Example CW ODMR spectrum
:width: 70%
:align: center

Example CW ODMR spectrum at zero field showing the characteristic dip at 2.87 GHz.
*(Figure placeholder — add example data.)*
```

## Prerequisites

- Laser aligned and APD/SPCM counting (see {doc}`Optics Alignment <optics_alignment>`)
- MW chain connected and signal generator on
- Sample mounted and in focus (see {doc}`Sample Mounting <sample_mounting>`)

## Procedure

### 1. Configure the MW Sweep

| Parameter | Typical Value | Notes |
|-----------|--------------|-------|
| Sweep center | 2.87 GHz | Zero-field; shift with bias field |
| Sweep span | 100–300 MHz | Wider if field is applied |
| MW power at antenna | | dBm |
| Laser power at sample | | µW |
| Integration time per point | | ms |

### 2. Run the Sweep

*Add: which script or GUI panel to use, how to start the acquisition, where data is saved.*

### 3. Fit the Spectrum

Fit each resonance dip to a Lorentzian to extract:

- Resonance frequency f₀
- Linewidth (FWHM) Δf
- Contrast C = ΔF/F₀

*Add: fitting script location, expected values for this sample.*

### 4. Interpreting Results

| Measurement | Expected | Poor Result | Likely Cause |
|-------------|----------|-------------|--------------|
| Contrast | > 5% | < 1% | Low MW power, misaligned MW |
| Linewidth | 5–20 MHz | > 50 MHz | Power broadened, bad sample |
| Resonance frequency | 2.87 ± field shift | No dip visible | MW not reaching sample |

## Common Issues

- **No ODMR dip visible** — check MW power at PCB, verify antenna coupling, increase integration time.
- **Very low contrast** — reduce laser power (avoid saturation), increase MW power.
- **Broad or asymmetric lines** — reduce MW power, check for multiple NV axes contributing.
- **Unstable baseline** — check laser power stability, minimize mechanical vibrations.

## Recording Reference Data

After a successful CW ODMR run, save:

- Raw data file
- Fit parameters (f₀, Δf, contrast)
- Laser power, MW power, magnet position
- Date and sample ID

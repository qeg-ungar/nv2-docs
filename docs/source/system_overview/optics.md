# Optics & Imaging

This page summarizes the construction of the optical setup, which operates as an NV fluorescence
microscope and performs optical initialization and readout of the NV spin state for pulse-sequence
control.

## Design Requirements

Two components anchor the design: a high-NA microscope objective and a single-photon detector.
Together they set the resolution and sensitivity needed to resolve single NVs down to the
diffraction limit and detect single-photon emission. The setup must also switch between confocal
and widefield imaging by adjusting the excitation beam profile at the objective focal plane and
routing the detection path to the corresponding detector (SPCM or SPAD array); both detection
paths are co-aligned with the excitation focus.

For pulsed experiments, the excitation laser must be modulated with a rise time on the order of
100 ns and pulse durations on the order of 1 $\mu\text{s}$ for efficient spin polarization. The
extinction ratio (leakage light when the laser is gated off) must exceed 40 dB to avoid
repolarization during microwave control. For widefield experiments, the excitation intensity over
the full field of view must reach approximately the same intensity used for single-NV experiments,
where the light is focused to a diffraction-limited spot — this requires roughly 60 mW of power at
the sample (see {doc}`../calibration/optics_alignment` for the power calibration procedure).

## Setup Overview

{numref}`Figure %s <fig-optics-layout>` shows the full beam path from both excitation lasers,
through fiber coupling and the objective, to the two detection channels.

```{figure} ../_static/images/nv_optics_combined.png
:name: fig-optics-layout
:alt: Optics schematic
:width: 100%
:align: center

Schematic of the NV fluorescence microscope setup for confocal and widefield imaging.
```

```{raw} html
<figure style="margin: 1.5rem 0;">
  <div style="display: flex; gap: 0.75rem; align-items: center;">
    <div style="flex: 1.4; text-align: center;">
      <img src="../_static/images/excitation_photo.png" style="width: 100%; max-height: 500px; object-fit: contain;">
      <div style="font-size: 0.85em; margin-top: 0.25rem;">(a)</div>
    </div>
    <div style="flex: 1; text-align: center;">
      <img src="../_static/images/detection_photo.png" style="width: 100%; max-height: 500px; object-fit: contain;">
      <div style="font-size: 0.85em; margin-top: 0.25rem;">(b)</div>
    </div>
  </div>
  <figcaption style="text-align: center; font-size: 0.9em; margin-top: 0.5rem;">
    Photos of the excitation and collection optics outside the science box. (a) Excitation optics, with the science box at upper left and the collection box at upper right. (b) Collection optics.
  </figcaption>
</figure>
```

## Components

| Component | Model | Notes |
|---|---|---|
| Experiment laser | [Lighthouse Photonics Sprout G 5W](https://www.gophotonics.com/products/lasers/lighthouse-photonics/29-511-sprout-g-5w) | CW, 532 nm DPSS |
| Alignment laser | Labs Electronics DLnsec | Pulsed, 110 mW, 520 nm diode laser |
| AOM (Acousto-Optic Modulator) | IntraAction Corp AFM-804A1 | 80 MHz, 514 nm |
| Optical fiber | [Thorlabs P3-488PM-FC-2](https://www.thorlabs.com/polarization-maintaining-fcapc-fiber-optic-patch-cables?tabName=Overview) | Polarization-maintaining, FC/APC |
| Fiber collimator (laser side) | [Thorlabs CFC5-A](https://www.thorlabs.com/fcpc-adjustable-aspheric-collimators?tabName=Overview) | FC/PC adjustable aspheric collimator |
| Fiber collimator (objective side) | [Thorlabs RMS20X](https://www.thorlabs.com/item/RMS20X) | 20X Olympus Plan Achromat objective, 0.40 NA, 1.2 mm WD, used as an output coupler |
| Microscope objective | Nikon CFI Plan Fluor 100X Oil | 1.3 NA — focuses excitation light and collects NV fluorescence |
| AOM telescope lenses | Thorlabs LA1422-A ($f_1$ = 400 mm), LA1422-A ($f_2$ = 40 mm) | Matches beam size to the AOM aperture |
| Objective telescope lenses | Thorlabs LA1422-A ($f_1$ = 40 mm), LA1509-A ($f_2$ = 100 mm) | Magnifies beam to match the objective aperture |
| Dichroic mirror | [Thorlabs DMLP567](https://www.thorlabs.com/item/DMLP567) | 567 nm cut-on |
| SPCM (Single-Photon Counting Module) | [Excelitas SPCM-AQRH-15-FC](https://www.digikey.com/en/products/detail/excelitas-technologies/SPCM-AQRH-15-FC/6235282) | Confocal detection |
| SPAD camera | Micro Photon Devices SPC3 | Widefield detection, 64x32 pixel array |

```{note}
The alignment-laser link above is a placeholder from the original draft (it points to Labs
Electronics' general products page, not the specific DLnsec listing) — worth swapping for the
actual product page if you have it on hand.
```

## Excitation Path

The two lasers serve different roles and have changed over the years. The setup originally relied
on a single high-power laser (Lighthouse Photonics Sprout, 5 W, 532 nm), shared with NV1. Repeated
stability problems with that laser's power supply motivated a switch to a pulsed, low-power laser
(DLnsec, 110 mW, 520 nm). The DLnsec was sufficient for single-NV confocal experiments — the
maximum required power at the objective focal plane is only $\sim 0.5$ mW — but could not reach the
power needed for widefield experiments. The Sprout was later reinstalled to run both confocal and
widefield experiments, while the DLnsec was kept for alignment and navigation imaging, since its
output is directly TTL-modulated and easily controlled through Qudi.

Because the Sprout is CW, an AOM (IntraAction Corp) modulates its output. The AOM is aligned in a
single-pass configuration — the setup has enough free-space path length to isolate the 0th-order
beam with an iris — and the two AOM telescope lenses match the beam size to the AOM's optimal
aperture. An additional $f = 750$ mm lens corrects the beam collimation before the fiber coupler.
The DLnsec, in contrast, is directly modulated by a TTL signal from the OPX+. Its output beam is
elliptical (stretched along one axis relative to the other); this is partially corrected with a
2:1 anamorphic prism pair (see {doc}`../calibration/optics_alignment` for the alignment procedure).
A quarter-waveplate and half-waveplate tune the power reflected off the polarizing beam splitter,
compensating for a small amount of circular polarization observed in the beam.

The excitation fiber serves two purposes. First, as a single-mode fiber, it spatially filters the
beam to produce a clean Gaussian profile at its output. Second, it decouples the downstream
alignment (objective and sample) from the upstream laser-source alignment, which has changed
several times over the evolution of NV2 — when the high-power laser was reinstalled, only the
fiber coupling needed to be redone, since the objective-side alignment was untouched. Both lasers
are combined onto the same fiber with a polarizing beam splitter (PBS), each with its own pair of
steering mirrors for independent alignment (see {doc}`../calibration/optics_alignment` for the
exact procedure). The mirror pair closest to the fiber is fixed once both lasers are aligned to it;
each laser then has one additional pair of mirrors for coupling optimization (for the DLnsec, the
PBS itself serves as one of these).

## Objective & Sample Interface

For confocal imaging, the excitation light from the fiber is collimated and magnified by the
objective telescope lenses to overlap the objective aperture, $D$. The system uses a Nikon CFI
Plan Fluor 100X Oil, 1.3 NA objective, with effective focal length

$$
f_\text{obj} = \frac{200~\text{mm}}{100} = 2~\text{mm}.
$$

From geometric optics, the objective aperture is $D = 2\times\text{NA}\times f_\text{obj} \approx
5.2$ mm, so the excitation beam is magnified to a diameter of 5–6 mm to match it.

The excitation light enters the science box, reflects off the dichroic mirror, and passes through
the objective, which focuses it onto the sample ({numref}`Figure %s <fig-objective-schematic>`).
The diamond sample is mounted on a cover glass patterned with a microwave stripline (a coplanar
waveguide, CPW), with immersion oil between the objective's front lens and the cover glass. The
objective's working distance (WD) is 0.16 mm for a 0.17 mm cover glass, so the cover glass surface
closest to the objective sits 0.16 mm away when the objective is focused at the diamond surface
(the CPW itself is only $\sim 500$ nm thick, negligible on this scale).

```{figure} ../_static/images/objective.png
:name: fig-objective-schematic
:alt: Objective and sample schematic
:width: 60%
:align: center

Schematic of the objective, cover glass (CG), and diamond sample arrangement.
```

The current NV2 sample has NVs implanted at an approximate depth of 20 nm — well below the
diffraction limit, so the NV layer can be treated as effectively at the surface. To position the
diamond surface at the objective focal plane, a piezo scan along the axial (Z) direction records
the NV fluorescence profile on the SPCM (see {doc}`../calibration/sample_mounting` for details).

For a Gaussian beam matched to the objective aperture, the $1/e^2$ spot diameter at the focal plane
is given by[^Thorlabs]

$$
s \approx \frac{1.83\,\lambda}{2\,\text{NA}} \approx 374~\text{nm}.
$$

Both the optical initialization efficiency and the readout signal-to-noise of a single NV or
ensemble depend strongly on this intensity profile, since intensity is set by the incident power
divided by the focal-plane spot size. The average intensity optimized for a single NV also sets
the total illumination power required for widefield SPAD measurements over the larger NV array.

## Confocal Detection Path

NV fluorescence behaves as a point-source emission with a broad phonon-sideband band extending
from the 637 nm zero-phonon line out to roughly 800 nm at room temperature[^wiki1]. The
fluorescence returns along the excitation path through the objective, passes back through the
dichroic, and is filtered by a longpass filter to remove residual excitation light. The lateral
point-spread-function (PSF) resolution of the objective is given by[^Leica]

$$
\text{FWHM} \approx \frac{0.51\,\lambda}{\text{NA}} \approx 270~\text{nm} \quad (\sim 460~\text{nm},\ 1/e^2\text{ diameter}).
$$

Collected fluorescence splits into two paths: confocal imaging onto the SPCM, and widefield imaging
onto the SPAD array. For the confocal path, the light is first imaged onto a pinhole to reject
out-of-focus background and improve contrast. A free-space confocal detection path typically uses
two lenses after the pinhole — one to collimate the light passing through it, and one to focus that
light onto the detector — whereas a fiber-coupled path needs only a single lens after the
objective, since the fiber itself acts as the pinhole. This setup uses free-space detection but,
for space efficiency, only a single lens after the pinhole. That lens is positioned so the light
focuses onto the detector, following the thin-lens equation[^SalehTeich][^Approx]

$$
\frac{1}{z} + \frac{1}{z'} \approx \frac{1}{f},
$$

as shown in {numref}`Figure %s <fig-collection-rays>`.

```{figure} ../_static/images/nv_collection_rays.png
:name: fig-collection-rays
:alt: Collection path
:width: 60%
:align: center

Schematic of the collection path for the confocal microscope.
```

The lens after the pinhole has a focal length of 100 mm, giving an overall magnification of 50X
from the objective's focal plane to this lens's image plane. Assuming a Gaussian diffraction-limited
spot, the spot size at the image plane is 46 $\mu\text{m}$. A 50 $\mu$m pinhole rejects light
collected from outside the diffraction-limited spot; with this pinhole, the axial resolution of the
confocal PSF is approximately

$$
\frac{1.4\,\lambda\, n}{\text{NA}^2} \approx 1~\mu\text{m}.
$$

Applying the thin-lens magnification from {numref}`Figure %s <fig-collection-rays>`,

$$
M \approx \left| \frac{f}{z-f} \right| = \frac{2}{3},
$$

the spot size at the detector is $\approx 20~\mu\text{m}$, comfortably within the SPCM's 180
$\mu$m active-area diameter.

## Widefield / SPAD Detection Path

The widefield path images fluorescence onto the SPAD camera with a single lens. The array has
64$\times$32 pixels, each 150 $\mu$m wide ({numref}`Figure %s <fig-spad-array>`). To resolve
individual implantation spots — spaced 1 $\mu$m apart in the sample — with at least two pixels of
separation (producing a checkerboard pattern in the image), the imaging path needs 300X
magnification, achieved with a 600 mm imaging lens. At this magnification, the objective's full
field of view ($\sim 50~\mu\text{m}$) fits within the sensor area. Given the available laser power,
only a single 5$\times$5 NV array (spanning 9$\times$9 pixels) is illuminated at a time.

To illuminate the full array, collimated light is focused at the objective's back aperture using a
flip-mounted lens (allowing the setup to switch between confocal and widefield modes). This lens
has a 1 m focal length; combined with the objective as a telescope, it produces a collimated beam
at the sample plane with a 10 $\mu$m diameter — large enough to illuminate the array.

```{figure} ../_static/images/SPAD_array.png
:name: fig-spad-array
:alt: SPAD array
:width: 60%
:align: center

The SPAD array camera from Micro Photon Devices. Image adapted from Wang et al.[^Wang2023]
```

## Key Parameters

| Parameter | Value | Notes |
|---|---|---|
| Objective NA | 1.3 | Nikon CFI Plan Fluor 100X Oil |
| Objective working distance | 0.16 mm | For 0.17 mm cover glass |
| Excitation spot size ($1/e^2$) | $\approx 374$ nm | Diffraction-limited, Gaussian beam |
| Lateral PSF FWHM | $\approx 270$ nm | $\sim 460$ nm $1/e^2$ diameter |
| Axial PSF resolution | $\approx 1~\mu\text{m}$ | With 50 $\mu$m confocal pinhole |
| Confocal detection magnification | 50X | Objective focal plane to pinhole image plane |
| Widefield imaging magnification | 300X | Sets checkerboard sampling of the NV array |
| SPAD array format | 64$\times$32 pixels, 150 $\mu$m pitch | Micro Photon Devices SPC3 |
| Widefield excitation power (target) | $\sim 60$ mW | See {doc}`../calibration/optics_alignment` |

[^Thorlabs]: Thorlabs, *Spot Size Tutorial*, <https://www.thorlabs.com/high-power-microspot-r-focusing-objectives-for-vis-and-nir-lasers?tabName=Spot%20Size>
[^wiki1]: Wikipedia, *Nitrogen-vacancy center*, <https://en.wikipedia.org/wiki/Nitrogen-vacancy_center>
[^Leica]: Leica Microsystems, *Microscope Resolution: Concepts, Factors and Calculation*, <https://www.leica-microsystems.com/science-lab/life-science/microscope-resolution-concepts-factors-and-calculation/>
[^SalehTeich]: B. E. A. Saleh and M. C. Teich, *Fundamentals of Photonics*, 3rd ed., Wiley, 2019.
[^Approx]: This applies the ray-optics approximation, valid since $z - f \gg z_0$, where $z_0$ is the Rayleigh range.
[^Wang2023]: G. Wang, F. Madonini, B. Li, C. Li, J. Xiang, F. Villa, and P. Cappellaro, *Fast Wide-Field Quantum Sensor Based on Solid-State Spins Integrated with a SPAD Array*, Advanced Quantum Technologies, vol. 6, no. 9, 2023. <https://doi.org/10.1002/qute.202300046>

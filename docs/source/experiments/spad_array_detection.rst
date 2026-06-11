SPAD Array Detection
====================

A single-photon avalanche diode (SPAD) array enables parallel spatial detection of NV
fluorescence, supporting wide-field spin imaging and spatially resolved readout of NV ensembles
without point-by-point scanning.

Overview
--------

Unlike a single APD or SPCM (which integrates fluorescence from the confocal volume), the SPAD
array images the NV fluorescence onto a 2D detector where each pixel is an independent
single-photon detector. This enables:

- **Wide-field ODMR** — spatial maps of spin resonance frequency (e.g., magnetic field maps)
- **Parallel confocal** — simultaneous readout of multiple single NVs
- **Real-time spin imaging** — faster acquisition than sequential confocal scanning

.. figure:: ../_static/images/spad_widefield_overview.png
   :alt: SPAD array wide-field detection overview
   :width: 75%
   :align: center

   Wide-field NV imaging using the SPAD array: fluorescence from many NVs is imaged simultaneously.
   *(Figure placeholder — add schematic and example image.)*

SPAD Array Specifications
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 25 35

   * - Parameter
     - Value
     - Notes
   * - Array size
     -
     - pixels
   * - Pixel pitch
     -
     - µm
   * - Fill factor
     -
     - %
   * - Dark count rate per pixel
     -
     - cps
   * - Timing resolution (TCSPC)
     -
     - ps
   * - Maximum count rate per pixel
     -
     - Mcps

*Add: manufacturer, model, interface (USB, PCIe), readout software.*

Optical Configuration
---------------------

The SPAD array is placed at an image plane of the collection objective. A relay lens system
maps the NV plane to the SPAD pixel array.

*Add: relay lens magnification, resulting FOV and spatial resolution per pixel, how SPAD path
is selected (flip mirror, beam splitter).*

.. figure:: ../_static/images/spad_optical_path.png
   :alt: SPAD array optical path
   :width: 70%
   :align: center

   Optical path from sample to SPAD array, including relay optics and filter.
   *(Figure placeholder.)*

Readout Modes
-------------

Intensity Imaging
~~~~~~~~~~~~~~~~~

Sum photon counts per pixel over a fixed integration window. Used for sample navigation and
wide-field fluorescence mapping.

Time-Gated Detection
~~~~~~~~~~~~~~~~~~~~~

Use a time gate synchronized to the laser pulse (via OPX TTL) to collect NV fluorescence while
rejecting background.

*Add: gate timing parameters, improvement in SNR.*

TCSPC (Time-Correlated Single Photon Counting)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Record photon arrival times relative to the laser pulse for lifetime measurements and
correlation experiments.

Procedure
---------

1. Align SPAD Array
~~~~~~~~~~~~~~~~~~~~

*Describe alignment of the relay optics to image the NV plane onto the SPAD array: use bright
fluorescence reference, maximize counts across array, check image quality.*

2. Configure Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~

*Add: which software/driver is used, key acquisition parameters (integration time, gate window,
trigger source).*

3. Wide-Field ODMR
~~~~~~~~~~~~~~~~~~~

1. Set laser on (CW or pulsed).
2. Sweep MW frequency; at each frequency step, acquire a full SPAD frame.
3. For each pixel, fit the ODMR spectrum to extract resonance frequency and contrast.
4. Generate a 2D map of resonance frequency (proportional to local magnetic field).

*Add: acquisition script, typical measurement time, expected spatial resolution.*

.. figure:: ../_static/images/widefield_odmr_map.png
   :alt: Wide-field ODMR frequency map
   :width: 70%
   :align: center

   Example wide-field ODMR frequency map showing spatial variation of the magnetic field.
   *(Figure placeholder — add example data.)*

4. Data Analysis
~~~~~~~~~~~~~~~~~

*Add: analysis pipeline for pixel-wise ODMR fitting, noise characterization, image reconstruction.*

Notes
-----

- SPAD arrays have non-uniform pixel-to-pixel sensitivity; flat-field correction is important
  for quantitative imaging.
- High count rates can cause pile-up in TCSPC mode; keep per-pixel rates well below saturation.

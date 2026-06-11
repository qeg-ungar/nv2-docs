Imaging
=======

The imaging subsystem supports both confocal (APD/SPCM) detection and wide-field camera imaging
for diamond sample navigation and NV ensemble characterization.

Components
----------

- **Alignment laser** — low-power laser for sample navigation and wide-field illumination
- **Camera** — wide-field imaging of the diamond surface and NV ensemble fluorescence
- **APD (Avalanche Photodiode)** — single-photon confocal detection (fast, low dark count)
- **SPCM (Single-Photon Counting Module)** — high-efficiency single-photon counting
- **NV fluorescence detection optics** — collection objective, long-pass filter, beam splitter to APD/SPCM/camera

Detection Paths
---------------

.. figure:: ../_static/images/detection_paths.png
   :alt: Detection path schematic
   :width: 80%
   :align: center

   Schematic of NV fluorescence collection and routing to camera, APD, and SPCM.
   *(Figure placeholder — add annotated diagram.)*

Confocal Detection (APD / SPCM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NV fluorescence (> 650 nm) is collected through the objective, separated from the excitation by a dichroic,
filtered by a long-pass, and focused onto the APD or SPCM fiber coupler. The detector output (TTL pulses)
is read by the NI I/O card or QM OPX.

*Add: fiber NA, long-pass filter model, typical count rates, detector specs.*

Wide-Field Camera
~~~~~~~~~~~~~~~~~

The camera images the diamond surface using the alignment laser for navigation and can capture
NV ensemble fluorescence in wide-field mode.

*Add: camera model, pixel size, FOV, exposure settings for navigation.*

Key Parameters
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 25 35

   * - Parameter
     - Value
     - Notes
   * - Collection objective NA
     -
     -
   * - Long-pass filter cutoff
     -
     - nm
   * - APD dark counts
     -
     - cps
   * - Camera pixel size
     -
     - µm
   * - Camera FOV
     -
     - µm × µm

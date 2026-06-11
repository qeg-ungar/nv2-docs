Confocal Imaging
================

Confocal scanning maps NV fluorescence intensity across the diamond surface by raster-scanning
the sample (XYZ piezo) relative to the fixed laser focus. This is used to locate NV centers,
characterize sample quality, and select regions of interest.

Overview
--------

.. figure:: ../_static/images/confocal_scan_example.png
   :alt: Example confocal scan image
   :width: 70%
   :align: center

   Example confocal scan of the diamond surface showing individual NV centers as bright spots.
   *(Figure placeholder — add example image.)*

Scan Modes
----------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Mode
     - Description
   * - XY scan
     - Raster scan at fixed Z; generates 2D fluorescence map
   * - XZ / YZ scan
     - Cross-section scan for Z-focus optimization
   * - Line scan
     - Single line for fast diagnostics
   * - Point measurement
     - Fixed position for time-resolved measurements

Procedure
---------

1. Bring Sample into Focus
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the camera (alignment laser, wide-field) to navigate to the region of interest and
bring the diamond surface into rough focus.

2. Configure Scan Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Add: which GUI panel or script to use, parameter descriptions.*

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Parameter
     - Typical Value
     - Description
   * - Scan range X
     - 10–50 µm
     - Physical scan size
   * - Scan range Y
     - 10–50 µm
     -
   * - Pixels
     - 100 × 100
     - Resolution
   * - Pixel dwell time
     - 5–20 ms
     - Integration per pixel
   * - Laser power
     -
     - µW at objective

3. Run the Scan
~~~~~~~~~~~~~~~~

*Add: how to start the scan, estimated run time, live preview.*

4. Identify NV Centers
~~~~~~~~~~~~~~~~~~~~~~~

Individual NV centers appear as diffraction-limited bright spots (~300 nm FWHM for NA 0.9 objective).

*Add: how to identify single NVs (second-order photon correlation g²(0) < 0.5) vs. ensembles.*

5. Save Data
~~~~~~~~~~~~~

*Add: file naming convention, data format (HDF5, NPY), metadata to record.*

Optimizing Image Quality
------------------------

- **Focus drift** — check Z scan before each image session; update Z setpoint if needed.
- **Laser power** — balance signal-to-noise vs. bleaching / ionization of NV.
- **Scan speed** — faster scans give noisier images; use longer dwell for final images.

Post-Processing
---------------

*Add: standard analysis notebook for loading, displaying, and fitting confocal images.*

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   # data = np.load('scan_001.npy')
   # plt.imshow(data, cmap='hot', origin='lower')

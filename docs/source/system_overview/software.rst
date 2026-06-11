Software Organization
=====================

This page describes the software stack used to control the NV2 instrument, acquire data, and
run experiments.

Overview
--------

.. figure:: ../_static/images/software_architecture.png
   :alt: Software architecture diagram
   :width: 85%
   :align: center

   High-level software architecture and data flow.
   *(Figure placeholder — add diagram.)*

Repositories & Packages
------------------------

*List the relevant code repositories and their roles.*

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Repository
     - Language
     - Role
   * -
     -
     -

Control Software
----------------

*Describe the main control interface: GUI or script-based, how experiments are configured and launched.*

QUA Programs (QM OPX)
~~~~~~~~~~~~~~~~~~~~~~

Quantum Orchestration programs written in QUA define pulse sequences, timing, and real-time
processing on the OPX.

*Add: directory location, how to run a sequence, configuration files.*

NI I/O Control
~~~~~~~~~~~~~~

*Describe the Python/LabVIEW layer that interfaces with the NI card for piezo scanning, analog readout, etc.*

Piezo Scanner
~~~~~~~~~~~~~

*Describe the scanning control: how raster scan parameters are set (range, step size, dwell time),
how data is acquired and saved.*

Data Storage
------------

*Describe where data is saved: directory structure, file formats (HDF5, NPY, CSV), naming conventions.*

.. code-block:: text

   data/
   ├── YYYY-MM-DD/
   │   ├── confocal_scan_001.hdf5
   │   ├── odmr_sweep_001.hdf5
   │   └── ...

Analysis
--------

*Describe analysis tools and notebooks: libraries used (NumPy, SciPy, matplotlib), standard fitting routines.*

Dependencies & Environment Setup
---------------------------------

*List Python version, key packages, and how to set up the environment.*

.. code-block:: bash

   # Example environment setup
   conda create -n nv2 python=3.10
   conda activate nv2
   pip install -r requirements.txt

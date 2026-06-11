RF Nuclear Spin Control
=======================

The ¹⁴N (or ¹³C) nuclear spin coupled to the NV electron spin can be polarized and coherently
controlled using RF pulses. This enables multi-qubit operations, quantum memory protocols, and
enhanced sensing via ancilla-assisted readout.

Background
----------

The ¹⁴N nucleus (I = 1) is hyperfine coupled to the NV electron spin with A\ :sub:`∥` ≈ −2.16 MHz.
At high bias field (≳ 500 G), the nuclear spin quantization axis is set by the external field
and the nuclear spin levels are individually addressable via RF pulses at the nuclear Larmor
frequency (for ¹⁴N: γ\ :sub:`N` ≈ 3.08 kHz/G).

.. figure:: ../_static/images/nv_n14_energy_levels.png
   :alt: NV-N14 coupled energy level diagram
   :width: 65%
   :align: center

   Energy level diagram of the NV–¹⁴N coupled system showing electron and nuclear spin states.
   *(Figure placeholder — add level diagram.)*

Prerequisites
-------------

- Magnetic field aligned to NV axis (see :doc:`Magnetic Field Alignment <../calibration/magnetic_field_alignment>`)
- MW control working (verified by pulsed ODMR / Rabi)
- RF source connected to antenna and calibrated for correct frequency range

Pulse Sequences
---------------

Nuclear Spin Initialization (Polarization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nuclear spin is polarized via electron-nuclear SWAP or conditional rotation sequences.

*Add: specific QUA sequence used, typical polarization fidelity.*

.. figure:: ../_static/images/nuclear_init_sequence.png
   :alt: Nuclear spin initialization sequence
   :width: 70%
   :align: center

   Pulse sequence for ¹⁴N nuclear spin initialization.
   *(Figure placeholder.)*

Nuclear Rabi Oscillations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply an RF pulse at the nuclear transition frequency and vary pulse duration to observe Rabi
oscillations.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Parameter
     - Typical Value
   * - RF frequency
     - ≈ 3.08 kHz/G × \|B\|
   * - RF power at antenna
     -
   * - Rabi frequency
     -
   * - π pulse duration
     -

Nuclear Ramsey / Hahn Echo
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Add: sequence description, expected T₂* and T₂ for ¹⁴N.*

¹³C Bath
~~~~~~~~~

*If isotopically enriched or natural abundance: add notes on ¹³C hyperfine structure and addressing.*

Procedure
---------

1. Find Nuclear Transition Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a nuclear ODMR sweep (electron pre-selected in m\ :sub:`s` = −1) to identify the nuclear
transition frequency.

*Add: which script to use, sweep range, expected linewidth.*

2. Calibrate RF π Pulse
~~~~~~~~~~~~~~~~~~~~~~~~

Vary RF pulse duration at the transition frequency and fit the Rabi oscillation.

3. Run Target Sequence
~~~~~~~~~~~~~~~~~~~~~~~

*Add: specific experiment steps for the target protocol (Bell state, sensing, etc.).*

4. Data Analysis
~~~~~~~~~~~~~~~~~

*Add: analysis notebook, observable of interest, how to extract nuclear spin polarization from
electron readout.*

Notes
-----

- RF pulses require careful impedance matching to the PCB antenna in this frequency range.
- Temperature changes can shift the nuclear Larmor frequency via changes in the bias field (magnet drift).

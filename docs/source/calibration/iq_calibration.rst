IQ Calibration
==============

IQ calibration corrects the DC offsets, amplitude imbalance, and phase imbalance of the IQ mixer
used to generate single-sideband (SSB) MW pulses. Poor calibration results in LO leakage and
image sideband contamination, which degrade pulse fidelity.

Background
----------

The QM OPX outputs I and Q analog waveforms that drive the IF ports of an IQ mixer. The LO is
supplied by a signal generator. Ideal IQ modulation produces a single output sideband at
f_LO + f_IF. Non-idealities introduce:

- **LO leakage** — carrier at f_LO
- **Image sideband** — spurious tone at f_LO − f_IF

.. figure:: ../_static/images/iq_spectrum_before_after.png
   :alt: IQ mixer output spectrum before and after calibration
   :width: 75%
   :align: center

   Spectrum analyzer output showing LO leakage and image sideband before (left) and after (right) calibration.
   *(Figure placeholder — add example spectra.)*

Equipment
---------

- Spectrum analyzer (or vector signal analyzer)
- Signal generator (LO source)
- QM OPX with IQ outputs connected to mixer

Procedure
---------

1. DC Offset Correction (LO Leakage)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply a DC offset on the I and Q outputs to null the LO leakage at f_LO on the spectrum analyzer.

*Add: how offsets are set in QUA config, typical offset values, target LO suppression (dBc).*

.. code-block:: python

   # Example QUA config excerpt (placeholder)
   # "mixers": {
   #     "mixer_qubit": [
   #         {"intermediate_frequency": IF_freq, "lo_frequency": LO_freq,
   #          "correction": IQ_imbalance(0.0, 0.0)}
   #     ]
   # }

2. Amplitude and Phase Imbalance Correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply a correction matrix to equalize the I and Q amplitudes and set their phase difference to
exactly 90°. Minimize the image sideband at f_LO − f_IF.

*Add: the ``IQ_imbalance`` helper function, parameter scan procedure, target image rejection (dBc).*

3. Verification
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Metric
     - Target
     - Achieved
   * - LO leakage
     - < −40 dBc
     -
   * - Image sideband
     - < −40 dBc
     -
   * - Signal tone power
     -
     - dBm

4. Saving the Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Add: where calibration values are stored (config file, JSON, etc.) and how to reload them.*

Notes
-----

- Calibration should be re-run when the LO frequency is changed or after warm-up.
- Temperature drifts can shift offsets; re-check if sensitivity changes unexpectedly.

RF & Control Electronics
========================

The RF and control electronics generate and synchronize all microwave, RF, and TTL signals
for qubit control and readout.

Components
----------

- **QM OPX** — quantum control processor; generates arbitrary waveforms for MW/RF pulses and TTL triggers
- **MW/RF chain** — amplifiers, switches, combiners, and delivery to the sample PCB antenna
- **Signal generators** — auxiliary CW sources for IQ mixing and frequency references
- **NI I/O Card** — analog/digital I/O for slow control: piezo voltages, detector readout, analog monitoring

System Architecture
-------------------

.. figure:: ../_static/images/rf_electronics_diagram.png
   :alt: RF and control electronics block diagram
   :width: 90%
   :align: center

   Block diagram of the RF/electronics subsystem. Blue lines = MW/RF signals, black = TTL/control,
   orange = Ethernet/PCIe, purple = analog I/O.
   *(Figure placeholder — add annotated diagram.)*

QM OPX
------

The OPX is the central controller. It connects to the PC via PCIe and is programmed using QUA
(Quantum Orchestration Language).

*Add: OPX model, channel assignments, firmware version, QUA version.*

Channel Map
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - OPX Port
     - Signal
     - Destination
   * -
     -
     -
   * -
     -
     -

MW/RF Chain
-----------

*Describe the signal chain from OPX analog output to the sample antenna: mixers, amplifiers, switches, power levels.*

.. figure:: ../_static/images/mw_chain_schematic.png
   :alt: MW/RF chain schematic
   :width: 80%
   :align: center

   Schematic of the MW/RF signal chain.
   *(Figure placeholder.)*

IQ Modulation
~~~~~~~~~~~~~

*Add notes on IQ mixer configuration, LO source, IF bandwidth, image rejection.*

Signal Generators
-----------------

*List signal generators: model, role (LO source, reference, auxiliary), frequency range.*

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Instrument
     - Model
     - Role
   * -
     -
     -

NI I/O Card
-----------

The NI card handles slower analog and digital I/O that does not require the OPX's timing precision.

*Add: NI card model, analog input/output channel count and voltage range, digital I/O lines.*

NI Channel Map
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - NI Channel
     - Signal
     - Notes
   * - AI0
     -
     -
   * - AI1
     -
     -
   * - AO0
     -
     -

Diamond Sample & PCB
====================

The diamond sample is mounted on a custom PCB that provides the MW antenna for spin control and
interfaces with the temperature control and positioning hardware.

Components
----------

- **Diamond sample** — type, orientation, NV density, and surface treatment
- **PCB** — coplanar waveguide or loop antenna; mechanical mount; electrical connections
- **Heater PID** — temperature stabilization of the sample stage
- **XYZ Piezo** — nanometer-precision sample positioning for confocal scanning
- **Magnet stage** — permanent magnet positioning for static bias field alignment

Sample Holder Assembly
----------------------

.. figure:: ../_static/images/sample_pcb_photo.png
   :alt: Diamond sample and PCB assembly
   :width: 70%
   :align: center

   Photograph of the diamond sample mounted on the PCB.
   *(Figure placeholder — add annotated photo.)*

*Add: description of how diamond is fixed to PCB (crystal bond, silver paint, etc.),
wire bonding or direct contact, strain considerations.*

Diamond Specifications
----------------------

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Parameter
     - Value
     - Notes
   * - Type
     -
     - e.g., electronic grade, CVD
   * - NV density
     -
     - ppb
   * - Surface cut
     -
     - e.g., [100], [111]
   * - Surface treatment
     -
     - e.g., acid clean, annealing
   * - Dimensions
     -
     - mm × mm × mm

PCB Antenna
-----------

*Add: antenna geometry (loop, CPW, omega), characteristic impedance, resonance frequency, coupling to sample.*

.. figure:: ../_static/images/pcb_antenna_layout.png
   :alt: PCB antenna layout
   :width: 60%
   :align: center

   PCB antenna layout.
   *(Figure placeholder.)*

Temperature Control
-------------------

The Heater PID maintains the sample temperature.

*Add: PID controller model, setpoint range, sensor type and placement, typical stability.*

Positioning
-----------

The XYZ piezo scanner moves the sample relative to the fixed confocal spot for raster imaging.

*Add: piezo model, range (µm), voltage-to-displacement calibration, resonance frequency.*

The magnet stage positions a permanent magnet to apply a static bias field along a chosen NV axis.

*Add: magnet type, field strength at sample, angular and linear travel.*

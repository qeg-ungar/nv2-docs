# CPW Fabrication

Design files and fabrication process for the two-channel coplanar waveguide (CPW) and PCB described
in {ref}`Microwave & RF Electronics <cpw-design>`.

## Design Files

Both sets of files are stored in the QEG Dropbox.

| Item | Location | Notes |
|---|---|---|
| CPW layout (GDS) | `QEG/Research Projects/Microwave_Stripline/Nanofab_AU_BL_2025/cpw_20261008.GDS` | Layer 1: 18 × 18 mm cover glass outline. Layer 2: the gaps (bare glass); everything else is copper. |
| PCB design (Eagle) | `QEG/Research Projects/Microwave_Stripline/pcb/CPW 18_18_Mo` | Designed by Mo Chen (board `PCB181130`); Gerber and drill files in `CAMOutputs/` |

## Fabrication Process

The CPW was fabricated by Alex Ungar and Boning Li using the process below.

**Substrate:** 18 × 18 mm glass coverslip, 0.17 mm thick.

| Step | Process | Tool | Parameters |
|---|---|---|---|
| 1 | HMDS vapor prime | HMDS-TRL U10 | HMDS monolayer |
| 2 | Spin resist | Spinner-Resist-U12 | AZ 10XT (positive), 3000 rpm, 60 s; 7.8 µm film |
| 3 | Bake | Hotplate-Tower-U12 | 110 °C, 180 s |
| 4 | Direct-write lithography | MLA150 (DirectWrite-MLA150-AirAF) | 405 nm, 300 mJ/cm² |
| 5 | Develop | Develop-U12 | AZ 435 MIF, 225 s, 20 °C |
| 6 | Plasma ashing (descum) | Asher-TergeoPro-Strip U6 | O₂, 100 W, 30 s (recipe #16) |
| 7 | E-beam evaporation | EBeam-AJA | Ti adhesion layer, 10 nm at 1 Å/s |
| 8 | E-beam evaporation | EBeam-AJA | Cu, 500 nm at 3 Å/s |
| 9 | Lift-off | — | Acetone, 24 h at 20 °C; finish with 5 min sonication (power 5/10) |

Resist datasheet: [AZ 10XT](https://www.microchemicals.com/dokumente/datenblaetter/tds/merck/en/tds_az_10xt_photoresist.pdf).

# Magnetic Field Alignment

A static bias magnetic field is applied to lift the degeneracy of the NV spin sublevels and,
optionally, to align along a specific NV crystallographic axis for single-axis addressability.

## Background

The NV center has four possible orientations in the [100]-cut diamond lattice (along the four
⟨111⟩ directions). Applying a field along one of these axes splits all four NV families
differently; a field aligned exactly along one axis leaves that family with the largest splitting
while the other three are equivalent and have a smaller splitting.

```{figure} ../_static/images/nv_axes_field_alignment.png
:alt: NV axes and field alignment diagram
:width: 65%
:align: center

Schematic of the four NV orientations and bias field alignment.
*(Figure placeholder.)*
```

## Equipment

- Permanent magnet on XYZ/angular stage
- ODMR measurement capability (see {doc}`CW ODMR <cw_odmr>`)

## Procedure

### 1. Initial Magnet Positioning

Place the magnet at a safe working distance from the sample (~2–5 cm) and confirm a nonzero
ODMR splitting is visible.

*Add: starting position, approximate field strength at this distance.*

### 2. Rough Axis Alignment

Monitor the ODMR spectrum while adjusting the magnet angle. Watch for the splitting pattern to
simplify to two pairs of lines (one NV family aligned, three equivalent families off-axis).

```{figure} ../_static/images/odmr_field_alignment_spectra.png
:alt: ODMR spectra during field alignment
:width: 75%
:align: center

ODMR spectra at different field angles showing progression toward axis alignment.
*(Figure placeholder — add example data plots.)*
```

### 3. Fine Alignment

Maximize the frequency splitting of the target NV family while minimizing the splitting of
the off-axis families. A field perfectly along ⟨111⟩ gives the off-axis families equal,
smaller splittings.

### 4. Record and Lock Position

| Parameter | Value | Notes |
|-----------|-------|-------|
| Magnet stage X | | mm |
| Magnet stage Y | | mm |
| Magnet stage Z | | mm |
| NV splitting (aligned family) | | MHz |
| Estimated \|B\| at sample | | G |

## Verification

Run a pulsed ODMR or Ramsey sequence to confirm clean spin resonances and expected
coherence times at this field.

## Notes on Diamond Orientation

*Add the as-mounted diamond orientation relative to the lab frame, and which NV axis is targeted.*

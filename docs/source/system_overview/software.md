# Software Organization

This page describes the software that controls the NV2 setup: the two Python packages that run the
instruments (Qudi and QUA), how they are organized in a single workspace, how to set that workspace
up on a new computer, and how the code is kept under version control.

## Overview

The setup is controlled by two open-source Python packages, which divide the hardware in the
{doc}`system block diagram <index>` between them:

- **Qudi**[^Binder2017] runs the "slow" instruments and the imaging. It handles confocal scanning
  of the piezo stage with photon counting on the NI DAQ card, acquisition on the two widefield
  cameras (the SPC3 SPAD camera and the Hermes camera), wide-range CW ODMR scans, monitoring of the photodetector and SPCM signals, and control of the alignment
  laser and the digital switches.
- **QUA**[^QMdocs], the pulse-level language of Quantum Machines, programs the **QM OPX+** for
  pulsed experiments. The OPX+ acts as the arbitrary waveform generator (IQ waveforms for the MW
  chains, RF pulses, and TTL gating of the lasers) and counts photons by time-tagging the SPCM
  pulses on its analog input, all synchronized within one pulse sequence. The QUA scripts also set
  the SRS SG384 local oscillators before each run.

| Hardware (block diagram) | Controlled by | Module / element | Notes |
|---|---|---|---|
| QM OPX+ | QUA | `QuantumMachinesManager`; elements `NV`, `RF`, `AOM2`, `MW_switch`, `SPCM2` | Pulse sequencing and photon time-tagging |
| Signal generators (SRS SG384) | QUA, Qudi | `SG384.py` (QUA scripts); `mw_source_srssg` (Qudi CW ODMR) | Set over Ethernet (SCPI) |
| NI DAQ card | Qudi | `ni_finite_sampling_io`, `ni_ao`, `ni_instreamer`, `ni_finite_sampling_input` | Piezo voltages, photon counting, analog input |
| XYZ piezo | Qudi | `ni_scanner` (NI analog outputs `ao0`–`ao2`) | Confocal scanning and tracking |
| SPCM | Qudi, QUA | NI counter input `PFI15` (Qudi); OPX+ analog input (QUA) | Counts for scans and ODMR; time tags for pulsed readout |
| Photodetector | Qudi | `ni_instreamer` (NI analog input `ai0`) | Laser power monitoring |
| Cameras (SPC3 SPAD, Hermes) | Qudi | `camera_SPC3`, `camera_Hermes` | Widefield acquisition |
| Alignment laser (DLnsec) | Qudi | `dlnsec_laser` | Power and mode over USB serial |
| Experiment laser AOM | QUA | `AOM2` digital marker | TTL gating within pulse sequences |
| MW switch | QUA | `MW_switch` digital marker | MW gating within pulse sequences |
| Magnet stage | Qudi | `zaber_motor` | Magnet positioning |
| Heater PID | Separate controller | — | See {doc}`PID Heater <pid_heater>` |

Qudi can also run long experiments automatically. A script executed through Qudi's Jupyter kernel
periodically re-tracks the NV emitter (the scanning optimizer re-centers the piezo on the
fluorescence spot) and then sends a trigger to the OPX+ through an NI digital line (the
`AWG trigger` switch), so the OPX+ resumes the pulse sequence and data collection with the NV back
in focus. This lets an experiment average for hours while staying on the same emitter (see
{doc}`Automation <../experiments/automation>`).

### Environment and workflow

All of the control code lives in one workspace folder, opened as a single VS Code workspace and run
from a single Python virtual environment:

- **`qudi-iqo-modules/`**: our fork of the Qudi measurement modules, installed in editable mode so
  lab changes (e.g. the DLnsec laser driver) take effect without reinstalling.
- **`qua-libs/`**: our fork of the Quantum Machines example library; the NV2 scripts are in
  `Quantum-Control-Applications/Optically addressable spin qubits/NV2/`.
- **`qudi-configs/`**: the Qudi configuration files for NV2.
- **`python notebooks/`**: Jupyter notebooks that script Qudi through its kernel.

A typical session starts Qudi with the NV2 configuration, uses the confocal scanner to find the NV
or array of interest and optimize its position, and then runs QUA scripts from VS Code for
calibrations and pulsed experiments. Qudi saves its data to the data directory set in its
configuration, with daily subfolders, and the QUA scripts save to a `Data` folder next to the NV2
script folder.

## Qudi

Qudi is a modular Python suite for experiment control and data processing, developed at the
Institute for Quantum Optics in Ulm[^Binder2017]. It is split into two packages:

- **[qudi-core](https://github.com/Ulm-IQO/qudi-core)** is the framework: the module manager, the
  configuration system, the GUI manager, data storage, and the IPython kernel used by notebooks
  ([documentation](https://ulm-iqo.github.io/qudi-core/)).
- **[qudi-iqo-modules](https://github.com/Ulm-IQO/qudi-iqo-modules)** provides the measurement
  modules: confocal scanning, time series, CW ODMR, camera, laser, switches, and others. Its
  `docs/` folder has setup guides for the main toolchains.

### Hardware, logic, and GUI modules

Every Qudi measurement module is one of three types, arranged in a one-way hierarchy[^QudiModules]:

- **Hardware modules** wrap a single instrument behind an abstract interface (e.g. a microwave
  source, a finite-sampling input, a camera). They do not control other modules. Because logic
  only talks to the interface, a real instrument can be swapped for another model or a dummy
  without changing the logic.
- **Logic modules** are the core of a measurement: they run it, process and save the data, and
  coordinate one or more hardware (or other logic) modules. Each runs in its own thread, and its
  methods form the API that notebooks and scripts call.
- **GUI modules** are Qt windows built on top of logic modules. They contain no measurement logic of
  their own.

Modules declare their dependencies with *connectors*, their static settings with *config options*,
and any state to remember between sessions with *status variables*. The module manager loads and
activates modules (and everything they depend on) on request.

### Configuration file

A Qudi session is built from a configuration file: a YAML text file with a `.cfg` extension, read
once at startup[^QudiConfig]. It has a `global` section (data directory, startup modules, server
ports, GUI stylesheet) followed by `gui`, `logic`, and `hardware` sections. Each module entry gives
a unique name, the module class (`module.Class`), its `options`, and a `connect` block that wires
its connectors to other modules by name. For example, the confocal scanning toolchain in the NV2
configuration (trimmed):

```yaml
gui:
    scanner_gui:
        module.Class: 'scanning.scannergui.ScannerGui'
        connect:
            scanning_logic: scanning_probe_logic
            data_logic: scanning_data_logic
            optimize_logic: scanning_optimize_logic

logic:
    scanning_probe_logic:
        module.Class: 'scanning_probe_logic.ScanningProbeLogic'
        connect:
            scanner: ni_scanner

hardware:
    ni_scanner:
        module.Class: 'interfuse.ni_scanning_probe_interfuse.NiScanningProbeInterfuse'
        connect:
            scan_hardware: 'ni_finite_sampling_io'
            analog_output: 'ni_ao'
        options:
            ni_channel_mapping:
                x: 'ao0'
                y: 'ao1'
                z: 'ao2'
                APD1: 'PFI15'
```

Opening `scanner_gui` in the Qudi manager loads the whole chain down to the NI card. The NV2
configuration (`qudi-configs/SPUD202609.cfg`) defines these toolchains:

| Toolchain | GUI | Logic | Hardware |
|---|---|---|---|
| Confocal scanning | `scanner_gui` | `scanning_probe_logic`, `scanning_data_logic`, `scanning_optimize_logic`, `poi_manager_logic` | `ni_scanner` → `ni_finite_sampling_io`, `ni_ao` |
| SPC3 camera and scanning | `SPC3_gui`, `scanner_spad_gui` | `camera_logic`, `spad_probe_logic`, `spad_optimize_logic` | `ni_scanner`, `camera_SPC3` |
| Hermes camera and scanning | `hermes_gui`, `scanner_hermes_gui` | `camera_hermes_logic`, `hermes_probe_logic`, `hermes_optimize_logic` | `ni_scanner`, `camera_Hermes` |
| CW ODMR | `odmr_gui` | `odmr_logic` | `mw_source_srssg`, `ni_finite_sampling_input` |
| Time series (SPCM and photodetector) | `APD_gui` | `time_series_reader_logic` | `ni_instreamer` (`PFI15` counts, `ai0` photodetector) |
| Alignment laser | `laser_gui` | `laser_logic` | `dlnsec_laser` |
| Switches | `laser_switch_gui`, `qm_switch_gui` | `laser_switch_logic`, `qm_switch_logic` | `laser_switch_ni` (laser mode relay), `qm_switch_ni` (OPX+ trigger) |
| Magnet | — | — | `zaber_motor` |

The Hermes camera modules and the Zaber magnet-stage driver are not yet in the workspace
repository; the other toolchains run without them.

### Notebooks and scripting

Qudi serves its active modules to a Jupyter kernel, so experiments can be scripted in a notebook
using the same logic modules the GUIs use[^QudiJupyter]. The `qudi` kernel does not start Qudi
itself; it connects to a running Qudi instance through the local namespace server
(`namespace_server_port` in the configuration, 18861 by default) and exposes each active module by
its configured name. For example, with the `dlnsec_laser` module active:

```python
laser_control = dlnsec_laser
laser_control.set_power(10)  # mW
laser_control.on()
```

To run a notebook, start Qudi and load the NV2 configuration, activate the modules the notebook
uses in the Qudi manager, then open the notebook in VS Code and select the **qudi** kernel. The
workspace's `QUDI_MIGRATION.md` covers re-registering the kernel and fixing a stale kernel path in
VS Code.

## QUA

QUA is a Python-embedded language for pulse-level control[^QMdocs]. A QUA program describes which
pulses to play on which outputs, which signals to measure, the real-time variables and loops that
sweep parameters, and how results are processed. It is sent to the OPX+, which compiles it and
executes it in real time on its pulse processor, with deterministic timing in 4 ns clock cycles. Each NV2
script follows the same pattern: import the configuration, write the program inside a
`with program()` block, connect to the OPX+ with a `QuantumMachinesManager`, and either simulate
the program or open a quantum machine with the configuration and execute it, fetching and plotting
the results live.

### Configuration

The configuration is a Python dictionary (`config` in `NV2/configuration.py`) that maps the
physical OPX+ ports to the logical objects the program uses[^QMconfig]:

- **Controllers** list the OPX+ ports in use, with their DC offsets and delays.
- **Elements** are the components the program addresses. Each is assigned the OPX+ outputs that
  drive it (a single analog output, an I/Q pair of analog outputs, or a digital output), and a
  readout element is also assigned the OPX+ analog input it is read on. Each element also has an
  intermediate frequency (IF) and a set of named **operations**. The configuration keys are named
  from the element's point of view, so `singleInput`, `mixInputs`, and `digitalInputs` refer to
  OPX+ outputs, and an element's `outputs` refers to an OPX+ input.
- **Operations** point to **pulses**, which have a length and **waveforms**: one for an element on
  a single analog output, I and Q for an element on an I/Q pair. Measurement pulses also define how
  the signal on the OPX+ input is acquired. The **mixer** entry holds the IQ correction matrix from the
  {doc}`IQ calibration <../calibration/iq_calibration>`.

The NV2 elements map onto the {doc}`microwave and RF chain <rf_electronics>` as follows:

| Element | OPX+ ports | Operations | Role |
|---|---|---|---|
| `NV` | Analog outputs 1, 2 (I, Q) | `cw`, `x180`, `x90`, `-x90`, `y180`, `y90`, `-y90` | IQ drive of the NV through the SG384; the LO frequency is the SG384 carrier |
| `RF` | Analog output 3 | `const` | Nuclear-spin RF pulses |
| `AOM2` | Digital output 2 | `laser_ON` | TTL gating of the experiment laser AOM |
| `MW_switch` | Digital output 1 | `mw_switch_ON` | MW switch gating |
| `SPCM2` | Analog input 1 | `readout`, `long_readout` | Photon time-tagging, with the readout calibrated for `AOM2` |

`MW_switch` replaced the former `AOM1` laser element on digital output 1. `AOM1` and its readout
partner `SPCM1` are still defined in `configuration.py`, but `AOM1` now drives the MW switch output,
so NV2 sequences use `AOM2` and `SPCM2`.

`configuration.py` also connects to the SG384 through `SG384.py` (a small PyVISA driver) and sets
its frequency, amplitude, and IQ modulation when the configuration is imported. Running any NV2
script therefore reconfigures the SG384 to the values in `configuration.py`.

### Writing programs

The main QUA statements used in the NV2 scripts are:

- `play(operation, element)` plays a pulse on an element, modulated at the element's IF;
  `amp(...)` scales its amplitude and `duration=` sets its length in real time (in 4 ns clock
  cycles).
- `measure(operation, element, ...)` plays a readout and acquires the returning signal; for the
  SPCM, `time_tagging.analog(...)` records the arrival time of each photon pulse and returns the
  count.
- `align()` makes elements wait for each other before continuing (with no arguments, all
  elements), and `wait()` inserts a delay, so the MW, laser, and readout happen in the right
  order.
- `declare()` creates real-time variables, and `for_` loops sweep them on the OPX+ (with
  `from_array` from qualang-tools to loop over a NumPy array).
- `save()` sends values to streams, and the `stream_processing()` block buffers and averages them
  on the OPX+ before they are fetched.

For example, the core of the time-Rabi script, shown here with the NV2 elements, sweeps the MW
pulse duration `t` and reads out the fluorescence after each pulse:

```python
with for_(n, 0, n < n_avg, n + 1):
    with for_(*from_array(t, t_vec)):
        play("x180" * amp(1), "NV", duration=t)  # MW pulse of variable length
        align()                                  # laser readout after the MW pulse
        play("laser_ON", "AOM2")
        measure("readout", "SPCM2", time_tagging.analog(times, meas_len_2, counts))
        save(counts, counts_st)
        wait(wait_between_runs * u.ns)
```

The unmodified default scripts address `AOM1` and `SPCM1`. On NV2, switch them to `AOM2` and
`SPCM2`, as in the modified `05a_cw_odmr.py`.

### Default NV scripts

The NV2 scripts are adapted from the example folder for an NV center in a confocal setup that ships
with qua-libs (`Optically addressable spin qubits/NV center in a confocal setup/`). The table lists
the default scripts and marks the ones modified for NV2:

| # | Script | Purpose | Modified for NV2 |
|---|---|---|---|
| 00 | `00_hello_qua.py` | Minimal program for trying out QUA | Yes |
| 01 | `01_manual_mixer_calibration.py` | Manual correction of the IQ mixer imbalance | Yes |
| 02 | `02_raw_adc_traces.py` | Raw ADC traces of the SPCM signal, to check saturation and set the time-tagging threshold | |
| 03 | `03_counter.py` | Live photon counter | Yes |
| 04a | `04a_calibrate_delays.py` | MW pulse during a laser pulse with time-tagging, to measure system delays and the initialization time | |
| 04b | `04b_calibrate_delays_python_histogram.py` | Same as 04a with the histogram built in Python, for high count rates | |
| 05a | `05a_cw_odmr.py` | CW ODMR: MW and laser readout played together during a frequency sweep | Yes |
| 05b | `05b_pulsed_odmr.py` | Pulsed ODMR: MW pulse followed by laser readout | |
| 06 | `06_time_rabi.py` | Rabi oscillation vs. MW pulse duration | |
| 07 | `07_power_rabi.py` | Rabi oscillation vs. MW pulse amplitude | |
| 08 | `08_ramsey.py` | Ramsey measurement of $T_2^*$ | |
| 09a | `09a_hahn_echo.py` | Hahn echo measurement of $T_2$ | |
| 09b | `09b_xy8_tau.py` | XY8-N dynamical decoupling, sweeping the interpulse spacing | |
| 09c | `09c_xy8_order.py` | XY8 dynamical decoupling, sweeping the order N | |
| 10 | `10_T1.py` | $T_1$ relaxation from $\lvert 0 \rangle$ or $\lvert 1 \rangle$ | |
| 11 | `11_state_tomography.py` | Qubit state tomography from the three projections | |
| 12 | `12_randomized_benchmarking.py` | Single-qubit randomized benchmarking of the gate fidelity | |

The folder also contains:

- `configuration.py`: the NV2 configuration described above.
- `SG384.py`: the PyVISA driver for the SG384. This is a lab addition.
- `05a_cw_odmr_default.py`: the unmodified upstream CW ODMR script, kept for reference.
- The upstream `configuration_with_*.py` variants for Octave and FEM-based hardware, which NV2 does
  not use.

## Setting Up the Workspace

A clean copy of the NV2 workspace is maintained as a reference repository,
[qeg-ungar/nv2-workspace](https://github.com/qeg-ungar/nv2-workspace). It holds the two forks as git
submodules, plus the files needed to get started: the Qudi configurations, the QUA configuration,
and the SG384 driver. It is a copy of the workspace on the lab computer, updated whenever that
workspace is in a known-good state. The layout is:

```text
nv2-workspace/
├── .venv/                        Python virtual environment (not tracked)
├── qudi-iqo-modules/             submodule: fork of Ulm-IQO/qudi-iqo-modules (editable install)
├── qua-libs/                     submodule: fork of qua-platform/qua-libs
│   └── Quantum-Control-Applications/Optically addressable spin qubits/NV2/
├── qudi-configs/                 default.cfg and the NV2 configuration
├── python notebooks/             notebooks run on the qudi kernel
├── QUDI_MIGRATION.md             environment notes and troubleshooting
└── workspace_sam.code-workspace  VS Code workspace
```

The commands below are for the Windows lab computer, run from the workspace folder in a VS Code
terminal.

1. **Get the code.** Clone the workspace with both submodules (see
   {ref}`Version Control <software-version-control>`):

   ```powershell
   git clone --recurse-submodules https://github.com/qeg-ungar/nv2-workspace.git
   ```

   To build it from scratch instead, fork [qudi-iqo-modules](https://github.com/Ulm-IQO/qudi-iqo-modules)
   and [qua-libs](https://github.com/qua-platform/qua-libs) on GitHub and clone both forks into one
   folder.

2. **Create the Python environment.** Create a virtual environment with Python 3.11 in the
   workspace folder, select it as the interpreter in VS Code (**Python: Select Interpreter**), and
   save the workspace (**File → Save Workspace As**):

   ```powershell
   py -3.11 -m venv .venv
   ```

3. **Install the QUA packages.** Install the qua-libs requirements (including `qm-qua`,
   `qualang-tools`, and PyVISA):

   ```powershell
   .venv\Scripts\python.exe -m pip install -r qua-libs\requirements.txt
   ```

   The NV2 folder must contain `configuration.py` and `SG384.py`. They are already in the
   reference workspace; in a fresh fork, copy them into the NV directory. The OPX+ and SG384
   network addresses are set in `configuration.py`.

4. **Install Qudi.** Install qudi-core from PyPI (not from source), then install qudi-iqo-modules
   from the cloned fork in editable mode, following the qudi-iqo-modules
   [installation guide](https://github.com/Ulm-IQO/qudi-iqo-modules/blob/main/docs/installation_guide.md):

   ```powershell
   .venv\Scripts\python.exe -m pip install qudi-core
   ```

   ```powershell
   .venv\Scripts\python.exe -m pip install -e qudi-iqo-modules
   ```

   Then apply the two package fixes in `QUDI_MIGRATION.md`: pin PySide6 to 6.11.0 (6.12 blanks the
   scanner GUI's input boxes), and make sure `pyserial`, not the unrelated `serial` package, is
   installed.

5. **Set up the configuration.** Create `qudi-configs/` (already present in the reference
   workspace) and copy in `default.cfg` from `qudi-iqo-modules/src/qudi/default.cfg` and the NV2
   configuration (`SPUD*.cfg`). In the NV2 configuration, set `default_data_dir` to the data folder
   on this computer.

6. **Register the notebook kernel:**

   ```powershell
   .venv\Scripts\qudi-install-kernel.exe
   ```

7. **Start Qudi.** Run `qudi` from the workspace folder, then load the NV2 configuration in the
   Qudi manager (**File → Load configuration** → `qudi-configs/SPUD*.cfg`). Alternatively, pass it
   at startup:

   ```powershell
   .venv\Scripts\qudi.exe -c qudi-configs\SPUD202609.cfg
   ```

The environment currently runs with these versions:

| Package | Version | Notes |
|---|---|---|
| Python | 3.11.9 | |
| qudi-core | 1.8.0 | From PyPI |
| qudi-iqo-modules | 1.0.0.dev0 | Editable install from the fork |
| PySide6 | 6.11.0 | Pinned; 6.12 has a GUI bug |
| pyserial | 3.5 | Needed by the DLnsec driver |

Older lab modules written for PySide2 must be ported to PySide6 before they load. The porting
steps and a troubleshooting table are in `QUDI_MIGRATION.md`.

(software-version-control)=
## Version Control

The workspace is a git repository in its own right (the *parent*), with the two forks inside it as
**git submodules**:

| Folder | Repository | Contents |
|---|---|---|
| parent | [qeg-ungar/nv2-workspace](https://github.com/qeg-ungar/nv2-workspace) | Lab files: `qudi-configs/`, notebooks, notes, the VS Code workspace |
| `qudi-iqo-modules/` | [qeg-ungar/qudi-iqo-modules](https://github.com/qeg-ungar/qudi-iqo-modules/tree/nv2-qeg), branch `nv2-qeg` (fork of [Ulm-IQO/qudi-iqo-modules](https://github.com/Ulm-IQO/qudi-iqo-modules)) | Qudi modules, including the DLnsec laser and SPC3 camera |
| `qua-libs/` | [qeg-ungar/qua-libs](https://github.com/qeg-ungar/qua-libs/tree/nv2-qeg), branch `nv2-qeg` (fork of [qua-platform/qua-libs](https://github.com/qua-platform/qua-libs)) | QUA scripts, including the NV2 folder |

In the reference workspace, the lab code in each fork is on the `nv2-qeg` branch; the branch is also
recorded in the parent's `.gitmodules`. The forks' `main` branches hold an earlier version of the
lab code and are not used.

The parent stores the lab's own files and, for each fork, a pointer to one specific commit; it
does not store the fork files. Each fork keeps its own history, so it can still pull updates from
its upstream project. Every parent commit therefore records a combination of lab files and fork
versions that work together, and you can return to it if a later update breaks something. The rule
to remember is **commit in the fork first, then in the parent**.

All repositories are public, so never commit passwords, tokens, or measurement data. The
workspace's `.gitignore` excludes the virtual environment, data folders, and logs.

### First-time setup on a new computer

After cloning with `--recurse-submodules`, make `git push` also push any unpushed fork commits,
and put both forks on their `nv2-qeg` branch (a fresh clone leaves them at a fixed commit, and
commits made there would not belong to any branch):

```bash
git config push.recurseSubmodules on-demand
```

```bash
git submodule foreach git switch nv2-qeg
```

### Before you start working

```bash
git pull
```

```bash
git submodule foreach git pull
```

### Saving and sharing changes

- **Parent files only** (notebooks, configurations): commit and push as in any repository.
- **Files inside a fork** (e.g. a QUA script in `qua-libs`):

  1. Commit in the fork:

     ```bash
     git -C qua-libs add -A
     ```

     ```bash
     git -C qua-libs commit -m "Describe the change"
     ```

  2. Record the fork's new commit in the parent:

     ```bash
     git add qua-libs
     ```

     ```bash
     git commit -m "Update qua-libs: short summary"
     ```

  3. Push. This pushes the fork first, then the parent:

     ```bash
     git push
     ```

- **Both**: commit in each fork you changed, then make one parent commit with the parent files and
  the updated fork pointers, and push.

To bring in upstream updates to a fork, click **Sync fork** on its GitHub page, pull it locally
(`git -C qudi-iqo-modules pull`), check that Qudi and the QUA scripts still run, then commit the
updated pointer in the parent.

### Reading `git status`

| `git status` in the parent shows | Meaning | What to do |
|---|---|---|
| `modified: qua-libs (modified content)` | Uncommitted edits inside the fork | Commit in the fork |
| `modified: qua-libs (new commits)` | The fork has commits the parent has not recorded | `git add qua-libs`, commit, push |
| `modified: qua-libs (untracked content)` | New files in the fork | Commit them in the fork, or add them to its `.gitignore` |

VS Code's **Source Control** panel shows the parent and both forks side by side, so each can be
committed without typing `git -C` commands; the order is the same (forks first, then the parent).

[^Binder2017]: J. M. Binder, A. Stark, N. Tomek, J. Scheuer, F. Frank, K. D. Jahnke, C. Müller, S. Schmitt, M. H. Metsch, T. Unden, T. Gehring, A. Huck, U. L. Andersen, L. J. Rogers, and F. Jelezko, *Qudi: A modular python suite for experiment control and data processing*, SoftwareX, vol. 6, pp. 85–90, 2017. <https://doi.org/10.1016/j.softx.2017.02.001>
[^QudiModules]: qudi-core documentation, *Measurement modules*, <https://ulm-iqo.github.io/qudi-core/design_concepts/measurement_modules.html>
[^QudiConfig]: qudi-core documentation, *Configuration*, <https://ulm-iqo.github.io/qudi-core/design_concepts/configuration.html>
[^QudiJupyter]: qudi-core documentation, *Jupyter notebooks*, <https://ulm-iqo.github.io/qudi-core/setup/jupyter.html>
[^QMdocs]: Quantum Machines documentation, *QUA overview*, <https://docs.quantum-machines.co/latest/docs/Introduction/qua_overview/>
[^QMconfig]: Quantum Machines documentation, *The QUA configuration*, <https://docs.quantum-machines.co/latest/docs/Introduction/config/>

# Microwave & RF Electronics

This page describes the electronics that generate, amplify, and deliver the microwave (MW) and
radio-frequency (RF) pulses used for coherent spin control of the NV electronic spin, the dark
electronic spins in the sample (referred to here as X spins), and nearby nuclear spins.

## Design Requirements

The primary function of the MW electronics is control of the NV spin. The spin state is
manipulated with resonant MW pulses: the amplitude of the oscillating field at the NV resonance
sets how fast the spin is driven (its Rabi frequency $\Omega_R$), and the phase of the pulse sets
the axis of rotation on the Bloch sphere. For almost all of our experiments we drive the
$m_s = 0 \leftrightarrow m_s = -1$ transition, the lower-frequency of the two NV spin transitions,

$$
f_{-} = D - \gamma_e B_z,
$$

where $D \approx 2.87$ GHz is the zero-field splitting, $\gamma_e \approx 2.8$ MHz/G is the
electron gyromagnetic ratio, and $B_z$ is the bias field along the NV axis. Over the range of our
bias magnet this transition spans roughly 1.9–2.9 GHz ($B_z$ up to $\sim 350$ G).

The Rabi frequency is proportional to the MW field amplitude, and therefore to the square root of
the delivered power, $\Omega_R \propto B_1 \propto \sqrt{P}$. Typical single-qubit gate times
(rotations on the Bloch sphere) range from $\sim 100$ ns to 1 $\mu$s depending on the MW power;
halving a gate time requires four times (6 dB) more power. The maximum applied power is limited by
how much current can flow through the MW stripline (see {doc}`Diamond Sample & PCB <diamond_sample>`
for details on the coplanar waveguide design). The measured limit is about 27 dBm CW, which agrees
with the stripline's measured maximum DC current of 0.15 A: for a matched $Z_0 = 50~\Omega$ line, the peak
current at 27 dBm (0.5 W) is

$$
I_\text{peak} = \sqrt{\frac{2P}{Z_0}} = \sqrt{\frac{2 \times 0.5~\text{W}}{50~\Omega}} \approx 0.14~\text{A}.
$$

*Add: link to the stripline failure-mode testing log.*

Beyond NV control, the setup is configured for several experimental applications and spin systems.
It covers three frequency bands, each with its own amplifier chain:

| Chain | Target spins | Frequency range | Amplifier band |
|---|---|---|---|
| MW-NV | NV electronic spin ($m_s = 0 \leftrightarrow -1$) | 1.9–2.9 GHz | 1.8–4.0 GHz |
| MW-X | Dark electronic spins (X) | $\lesssim 1$ GHz | 20–1000 MHz |
| RF-n | Nuclear spins (¹⁵N, ¹H) | 0–10 MHz | 0.1–200 MHz |

For a dark electronic spin with $g \approx 2$, the resonance frequency is $f_X \approx \gamma_e B_z$,
which stays below $\sim 1$ GHz over the same field range. Lastly, not shown in the schematic, the
setup can also drive strong magnetic-field gradients using a high-power MOSFET switch
(*Add: link to the gradient switch design and implementation*).

## Setup Overview

{numref}`Figure %s <fig-mw-chain>` shows the full MW/RF chain, from the OPX+ analog outputs to
the stripline PCB.

```{figure} ../_static/images/mw_chain_schematic.png
:name: fig-mw-chain
:alt: MW/RF chain schematic
:width: 100%
:align: center

Schematic of the MW/RF chain, configured for control of all three spin species. Thin lines are
low-level signals from the OPX+ and SG384s; thick lines are amplified MW/RF delivered to the
stripline. The dotted path is the termination used in place of the X chain when only the NV and
nuclear spins are driven.
```

## Components

| Component | Model | Notes |
|---|---|---|
| Quantum controller | [Quantum Machines OPX+](https://www.quantum-machines.co/products/opx/) | 4 analog outputs, 2 analog inputs, 10 digital outputs; 1 GS/s, 16-bit, 400 MHz bandwidth |
| Signal generators (×2) | [SRS SG384](https://www.thinksrs.com/products/sg380.html), Opt. 03 | DC–4.05 GHz; external IQ modulation for carriers 400 MHz–4.05 GHz |
| NV amplifier | [Mini-Circuits ZHL-16W-43-S+](https://www.minicircuits.com/pdfs/ZHL-16W-43-S+.pdf) | 1.8–4.0 GHz, 45 dB gain, 16 W |
| X amplifier | [Mini-Circuits ZHL-20W-13+](https://www.minicircuits.com/pdfs/ZHL-20W-13+.pdf) | 20–1000 MHz, 50 dB gain, 20 W |
| RF amplifier | [Mini-Circuits LZY-22+](https://www.minicircuits.com/pdfs/LZY-22+.pdf) | 0.1–200 MHz, 43 dB gain, 30 W |
| RF switch | [Mini-Circuits ZASWA-2-50DR+](https://www.minicircuits.com/pdfs/ZASWA-2-50DR+.pdf) | Absorptive SPDT, DC–5 GHz, integrated TTL driver |
| Low-pass filter | [Mini-Circuits BLP-30+](https://www.minicircuits.com/pdfs/BLP-30+.pdf) | DC–32 MHz passband, 0.5 W max input |
| Attenuators | *Add: models* | 3 dB (Q2), 16 dB (RF chain), 2 × 20 dB (stripline terminations) |
| Terminations | *Add: model* | 50 Ω |
| MW stripline | Custom two-channel CPW | See {doc}`Diamond Sample & PCB <diamond_sample>` |

See {doc}`../appendix/documentations` for the full list of hardware manuals and spec sheets.

## Pulse Generation (QM OPX+)

The QM OPX+ is the central instrument for generating the pulsed MW and RF waveforms. Our unit has
four analog outputs, two analog inputs, and ten digital outputs. The analog outputs sample at
1 GS/s with 16-bit resolution, a 400 MHz (3 dB) bandwidth, and a 1 V peak-to-peak swing into
50 Ω. The pulse processor runs on a 250 MHz clock, so pulse timing has 4 ns granularity, with a
minimum pulse length of 16 ns[^OPX].

Pulse sequences are written in QUA, Quantum Machines' pulse-level programming language, from a
Python environment. Each program is compiled and executed in real time on the OPX+'s FPGA-based
pulse processor (see {doc}`Software Organization <software>`). The OPX+ also generates the laser
TTL pulses on its digital outputs and reads in the SPCM signal on an analog input, so laser
gating and photon acquisition are synchronized internally with the pulse sequence.

## IQ Modulation

The NV and X chains each use two analog channels, one for the in-phase (I) and one for the
quadrature (Q) waveform (I1/Q1 for the NV, I2/Q2 for X). These drive the external IQ inputs of an
SRS SG384 signal generator, whose internal IQ modulator mixes them onto its carrier (the local
oscillator, LO) at $f_\text{LO}$:

$$
s(t) = I(t)\cos(2\pi f_\text{LO} t) - Q(t)\sin(2\pi f_\text{LO} t).
$$

For $I(t) = A\cos(2\pi f_\text{IF} t + \phi)$ and $Q(t) = A\sin(2\pi f_\text{IF} t + \phi)$, the
output is a single tone,

$$
s(t) = A\cos\!\left[2\pi (f_\text{LO} + f_\text{IF})\, t + \phi\right],
$$

at the intermediate frequency (IF) $f_\text{IF}$ above the LO. The relative amplitudes of the I and
Q channels therefore set the phase $\phi$ of the pulse (the rotation axis), while their combined
amplitude $A$ sets its power (the Rabi frequency). The SG384 IQ inputs are 50 Ω with a full scale
of $\sqrt{I^2 + Q^2} = 0.5$ V, matching the ±0.5 V output range of the OPX+, and the modulation
bandwidth is 200 MHz[^SG384]. A real mixer adds DC offsets and I/Q amplitude and phase imbalance,
which produce LO leakage and an image sideband at $f_\text{LO} - f_\text{IF}$. These are corrected
in the QUA configuration (see {doc}`IQ Calibration <../calibration/iq_calibration>`).

The SG384's external IQ modulation only works for carrier frequencies between 400 MHz and
4.05 GHz[^SG384]. The NV band is well inside this range, but the X chain's LO must be set at or
above 400 MHz.

## NV and X Chains

The SG384 outputs are amplified by a Mini-Circuits ZHL-16W-43-S+ for the NV band (MW-NV) and a
ZHL-20W-13+ for the X band (MW-X). Both amplifiers can deliver far more power (+42 and +43 dBm
saturated) than the $\sim 27$ dBm the stripline tolerates, so in practice the stripline sets the
power limit, not the amplifiers.

```{warning}
With 45–50 dB of amplifier gain, an SG384 output of only about −20 dBm already reaches the
stripline's $\sim 27$ dBm limit. Check the power delivered to the stripline before increasing the
SG384 output level or the pulse amplitudes in the QUA configuration.
```

## RF Nuclear Spin Chain

Nuclear spin frequencies (below 10 MHz) are well within the OPX+ output bandwidth, so the RF pulses
are synthesized directly by the OPX+ without upconversion. With all four analog outputs already
used by the NV and X chains, we reuse the X chain's I channel (I2) for RF pulses, since RF and X
pulses are never applied simultaneously. A tee splits I2 between the X-chain SG384 and the RF chain.
The RF waveform therefore also reaches the X-chain SG384 during RF pulses, but the resulting
output is far off resonance from the X spins and has no effect.

Because of the tee, the OPX+ output on I2 drives two 50 Ω inputs in parallel (25 Ω), which reduces
its voltage to 2/3 of the value into a single matched load ($20\log_{10}(2/3) \approx -3.5$ dB). A
3 dB attenuator on Q2 applies nearly the same reduction to the Q channel, keeping the I and Q
amplitudes into the X-chain SG384 balanced. The small remaining imbalance is removed by the IQ
calibration.

A digital output from the OPX+ gates a ZASWA-2-50DR+ switch at the input of the RF chain. The
switch passes I2 into the RF chain only during RF pulses, which keeps the X waveforms out of the
RF chain and stops other low-frequency noise from passing through the amplifier onto the
stripline. (The LZY-22+ has a built-in blanking input, but its 64 ms turn-on time is far too slow
to gate individual pulses[^LZY].) After the switch, the signal is amplified by the LZY-22+
(0.1–200 MHz, 43 dB gain) and passes through a BLP-30+ low-pass filter before reaching the
stripline; the filter passes DC–32 MHz and rejects 61–200 MHz by more than 40 dB.

A 16 dB attenuator before the amplifier limits the maximum power of the RF signal to below 0.5 W
(27 dBm), the limit of both the stripline and the BLP-30+. At full OPX+ output (+4 dBm into
50 Ω), the tee (−3.5 dB), the switch insertion loss (−1.3 dB), the 16 dB attenuator, and the
43 dB amplifier gain give a maximum of about +26 dBm at the stripline.

## Stripline Connections

{numref}`Figure %s <fig-mw-chain>` shows the configuration for experiments with control of all
three spins. The NV and X amplifiers drive opposite ends of the same stripline (Ch1), and the RF
chain drives Ch2. Each stripline is a through line: power not dissipated along the strip exits at
the far end, where Ch2 is terminated into 50 Ω through a 20 dB attenuator.

Connecting both the NV and X amplifiers to one stripline is certainly not optimal, since each
amplifier's output is delivered into the other amplifier's output port. It is a workaround for not
having a high-power combiner covering both frequency bands. Both amplifiers are protected against
reflected power: the ZHL-16W-43-S+ is rated to survive an open or short load at full CW output, and
the ZHL-20W-13+ survives a full mismatch as long as its input power stays below −13 dBm[^ZHL20]. At
the power levels allowed by the stripline, both amplifiers operate far below these limits.

For experiments that don't require driving all three spins, the connections can be changed, since
the two striplines are equivalent. For example, for NV + nuclear spin experiments the X chain is
disconnected and Ch1 is terminated through a second 20 dB attenuator into 50 Ω (dotted path in
{numref}`Figure %s <fig-mw-chain>`).

[^OPX]: Quantum Machines, *OPX+ Specifications*, document v4.0 (QOP firmware v2.2).
[^SG384]: Stanford Research Systems, *SG380 Series RF Signal Generators* datasheet, <https://www.thinksrs.com/products/sg380.html>
[^LZY]: Mini-Circuits, *LZY-22+ High Power Amplifier* datasheet, <https://www.minicircuits.com/pdfs/LZY-22+.pdf>
[^ZHL20]: Mini-Circuits, *ZHL-20W-13+ High Power Amplifier* datasheet, <https://www.minicircuits.com/pdfs/ZHL-20W-13+.pdf>

# Temperature coefficient measurements
---

Total number of devices evaluated in this test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 4 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

Temperature is large factor and possible measurement error contributor of the laboratory instrument. Amplitude of temperature-related output change determines temperature coefficient and depends on many design features, such as materials, power distribution, physical layout and electrical circuit design. Minimizing temperature coefficient can be achieved by using material junctions with low parasitic EMF, careful thermal design with optimized uniformity and active heating/cooling stabilisation.

Buried zeners such as LTZ1000, ADR1000, LM399 and ADR1399 implement integrated on-chip heating to remove most of temperature coefficient. Residual coefficient mostly depends on circuit design and component choice. This can be measured by long-scale DVM with external environmental chamber with programmable temperature. ADR1000 modules temperature coefficient evaluated over the temperature range from +18 C to +28 C over the 24 hour test duration. Temperature coefficient test was performed with 8 steps. 

Instrument setup consisted of set of stable 3458A DMMs, programmable air-bath with TEC-based heatpump operated by Model 2510 SMU in bipolar mode. Air bath configured to provide both heating and cooling to allow temperatures above and below ambient. Temperature of the DUT module was measured separately by precision PT1000 RTD and Model 1529 temperature readout with uncertainty &plusmn;0.5 &deg;C. Modules under test were powered by battery pack, same one that used in noise measurement experiments.

![TC measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/tc_setup_blk.png)

* Step A: Set temperatre chamber to fixed +23.0 C and collect 2 hours of voltage output data with 8.5-digit DMMs.
* Step B: Ramp up temperatre chamber to +28.0 C with typical speed +0.01 &deg;C/minute while logging voltage output data with 8.5-digit DMMs.
* Step C: Set temperatre chamber to +28.0 C and collect few hours of voltage output data with 8.5-digit DMMs.
* Step D: Ramp down temperatre chamber to +23.0 C with typical speed -0.01 &deg;C/minute while logging voltage output data with 8.5-digit DMMs.
* Step E: Set temperatre chamber to +23.0 C and collect few hours of voltage output data with 8.5-digit DMMs.
* Step F: Ramp down temperatre chamber to +18.0 C with typical speed -0.01 &deg;C/minute while logging voltage output data with 8.5-digit DMMs.
* Step G: Set temperatre chamber to +18.0 C and collect few hours of voltage output data with 8.5-digit DMMs.
* Step H: Ramp up temperatre chamber to +23.0 C with typical speed +0.01 &deg;C/minute while logging voltage output data with 8.5-digit DMMs.
* Step I: Set temperatre chamber to +23.0 C and collect few hours of voltage output data with 8.5-digit DMMs.

This cycling sequence, data collection and communication with instruments over GPIB was automated with [open-source Python program called TECkit](https://xdevs.com/guide/teckit) running on single-board computer Raspberry Pi 3B. 

Based on this instrumentation following results were obtained:

## ADR1000AHZ module QVR4, four chips averaged

TBD

## ADR1000AHZ module QVR2, two chips averaged

![QVR Dual TC sweep](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_final_tc_sweep_blk.png)

[CSV RAW-datafile](https://xdevs.com/doc/xDevs.com/QVRA/qvr_dual_temperature_sweep_feb2024.csv)

Module under test was sweeped multiple times from +18.0 &deg;C to +28.0 &deg;C set temperature after initial warmup around 3-4 hours. Sweep Module was powered by Fluke 792A battery pack and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) continously. 

Temperature sweep rate varied from 0.1 &deg;C to 0.04 &deg;C/minute to verify settling time of the assembly under test. Then second order polynominal was best fit to the measured voltage points and temperature coefficients were calculated as result, with new final &alpha; = -0.040 &micro;V/V/K ; &beta; = +0.0017 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+34.5 &deg;C*. Summary table presented below.

| **Dual module**    | **Parameter**  | **Unit**     | **Notes**                         |
| :------------      | :-----------:  | :--------:   | :-------------------------------: |
| Calibration date   | FEB/4/2024     |              | +23 &deg;C ambient, by 3458 group |
| Reference Temp T   |       23.00    | &deg;C       |                                   |
| Nominal output     | 10.000000      | VDC          |                                   |
| 1st fit const      | -1.2009744E-6  |              |                                   |
| 2nd fit const      | 1.74072180E-8  |              |                                   |
| Gain const         | 10.0004070     | VDC          |                                   |
| EMF, T₂₃           | **10.0003886** | VDC          |                                   |
| &alpha; T₂₃        | -0.0400        | &micro;V/V/K |                                   |
| &beta;             | +0.0017        | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 34.5           | &deg;C       |                                   |
| TC, BOX, 18-28     | -0.0332        | &micro;V/V/K |                                   |
| Relative U, k=2    | 1.6            | &micro;V/V   | Within 24 hours                   |

Temperature chart in the programmable air-bath sensor, placed next to the DUT module is also available. Temperature sensor used is Honeywell HEL-705 PT1000 RTD, digitized with Fluke 1529 thermometer readout. Small +0.2 &deg;C offset was observed during the measurement due to local heating from the power dissipated in the module inside the airbath.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_tc_time_blk.png)

Environmental parameters such as ambient temperature, pressure and humidity were monitored by [Bosch BME280-based sensor](https://xdevs.com/guide/thp_rpi/), digitized directly with Raspberry Pi 3B I2C interface bus. This sensor provided reference data to ensure that ambient conditions were stable and within short-term 24-hour stability specificaitons of used DVMs. Overall ambient temperature change during the whole test duration was recorded at 0.36 &deg;C. No additional correction to DMM temperature coefficient applied.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_env_time_blk.png)

## ADR1000AHZ module QVR1, single chip

TBD

## LTZ1000ACH "FX" unit S/N 002 

TBD

## LTZ1000ACH "FX" prototype S/N 001

TBD

## HP 3458A unit 1, A9 LTZ1000ACH module voltage

TBD

## HP 3458A unit 2, A9 LTZ1000ACH module voltage

TBD

New Analog Devices ADR1000AHZ device in a typical application circuit can indeed demonstrate temperature stability better than &plusmn;0.05 &micro;V/V/K given the adequate parts selection. This is similar to LTZ1000/LTZ1000A solution which was proven by decades of operation in magnitude of design variations and commercial instruments.

Data set table with all measurement values is also presented below for further analysis. 


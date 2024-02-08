# Temperature coefficient measurements

---

Total number of devices evaluated in this test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 4 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

Temperature is large factor and possible measurement error contributor of the laboratory instrument. Amplitude of temperature-related output change determines temperature coefficient and depends on many design features, such as materials, power distribution, physical layout and electrical circuit design. Minimizing temperature coefficient can be achieved by using material junctions with low parasitic EMF, careful thermal design with optimized uniformity and active heating/cooling stabilization.

Buried zeners such as LTZ1000, ADR1000, LM399 and ADR1399 implement integrated on-chip heating to remove most of temperature coefficient. Residual coefficient mostly depends on circuit design and component choice. This can be measured by long-scale DVM with external environmental chamber with programmable temperature. ADR1000 modules temperature coefficient evaluated over the temperature range from +18 C to +28 C over the 24 hour test duration. The temperature coefficient test was performed with 8 steps. 

The instrument setup consisted of a set of stable 3458A DMMs, programmable air-bath with TEC-based heatpump operated by Model 2510 SMU in bipolar mode. The air bath is configured to provide both heating and cooling to allow temperatures above and below ambient. The temperature of the DUT module was measured separately by precision PT1000 RTD and Model 1529 temperature readout with uncertainty &plusmn;0.5 &deg;C. Modules under test were powered by battery pack, same one that used in noise measurement experiments.

![TC measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/tc_setup_blk.png)

* Step A: Set temperature chamber to fixed +23.0 C and collect 2 hours of voltage output data by DMMs.
* Step B: Ramp up temperature chamber to +28.0 C with a typical speed +0.01 &deg;C/minute while logging voltage output data by DMMs.
* Step C: Set temperature chamber to +28.0 C and collect a few hours of voltage output data by DMMs.
* Step D: Ramp down temperature chamber to +23.0 C with a typical speed -0.01 &deg;C/minute while logging voltage output data by DMMs.
* Step E: Set temperature chamber to +23.0 C and collect a few hours of voltage output data by DMMs.
* Step F: Ramp down temperature chamber to +18.0 C with a typical speed -0.01 &deg;C/minute while logging voltage output data by DMMs.
* Step G: Set temperature chamber to +18.0 C and collect a few hours of voltage output data by DMMs.
* Step H: Ramp up temperature chamber to +23.0 C with a typical speed +0.01 &deg;C/minute while logging voltage output data by DMMs.
* Step I: Set temperature chamber to +23.0 C and collect few hours of voltage output data by DMMs.

This cycling sequence, data collection and communication with instruments over GPIB was automated with [open-source Python program called TECkit](https://xdevs.com/guide/teckit) running on single-board computer Raspberry Pi 3B. Exact build used to perform these measurements is also [included in this repository](https://github.com/tin-/adr1000/tree/main/python). It is configured to run in console with python-vxi11 and Python 3.x environment.

Based on this instrumentation the following results were obtained:

## ADR1000AHZ module QVR4, four chips individual outputs, without trim

First test is to measure voltage stability against temperature change of individual zener output for each of the two populated circuits on the QVR module PCBA. This is achieved by removing the connection to averaging resistor network at the output of each cell and routing kelvin-connected 6.6 V to separate DMM. This way it is possible to evaluate ADR1000 circuit performance without the effects of the output gain 10 V amplifier added. ADR1000 circuit tempco can be compensated and adjusted to very low numbers by multiple methods, such as changing series resistance to zener cathode terminal or adding a weak feedback from voltage loop to oven control loop (with series resistor in order 100 k&Omega; to 1 M&Omega; between heater transistor emitter and ADR1000 zener anode pin 4). 

The module under test with dual ADR1000 zener IC swept multiple times from +17.0 &deg;C to +55.0 &deg;C set temperature after initial warmup around 3 hours. The test module was powered by linear triple channel power supply and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) and one Keithley 2002LTC continuously. 

| **Dual module**    | **Parameter for cel 1**    | **Parameter for cell 2**    | **Parameter for cell 3**   | **Parameter for cell 4**   | **Unit**     | **Notes**                         |
| :------------      | :-----------:              | :-----------:               | :-----------:              | :-----------:              | :--------:   | :-------------------------------: |
| Calibration date   | FEB/9/2024                 | FEB/9/2024                  | FEB/9/2024                 | FEB/9/2024                 |              | +23 &deg;C ambient, by 3458+2002 group |
| Reference Temp T   |       23.00                |       23.00                 |       23.00                |       23.00                | &deg;C       |                                   |
| Nominal output     | 6.62                       | 6.62                        | 6.62                       | 6.62                       | V            | 5 mA, +51 &deg;C 11.5k&Omega;/1k&Omega;|
| 1st fit const      | XXXXXXXXXXXXXX             | XXXXXXXXXXXXXX              | XXXXXXXXXXXXXX             | XXXXXXXXXXXXXX             |              |                                   |
| 2nd fit const      | XXXXXXXXXXXXXX             | XXXXXXXXXXXXXX              | XXXXXXXXXXXXXX             | XXXXXXXXXXXXXX             |              |                                   |
| Gain const         | XXXXXXXXXX                 | XXXXXXXXXX                  | XXXXXXXXXX                 | XXXXXXXXXX                 | V            |                                   |
| EMF, T₂₃           | **X.XXXXXXX**              | **X.XXXXXXX**               | **X.XXXXXXX**              | **X.XXXXXXX**              | V            |                                   |
| &alpha; T₂₃        | XXXXXXX                    | XXXXXXX                     | XXXXXXX                    | XXXXXXX                    | &micro;V/V/K |                                   |
| &beta;             | XXXXXXX                    | XXXXXXX                     | XXXXXXX                    | XXXXXXX                    | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | XXXX                       | XXXX                        | XXXX                       | XXXX                       | &deg;C       |                                   |
| Relative U, k=2    | 2.0                        | 2.0                         | 2.0                        | 2.0                        | &micro;V/V   | Within 1 week                     |

## ADR1000AHZ module QVR4, four chips individual outputs, after trim

## ADR1000AHZ module QVR4, four chips averaged

## ADR1000AHZ module QVR2, two chips, individual 6.62 V zener IC outputs

First test is to measure voltage stability against temperature change of individual zener output for each of the two populated circuits on the QVR module PCBA. This is achieved by removing the connection to averaging resistor network at the output of each cell and routing kelvin-connected 6.6 V to separate DMM. This way it is possible to evaluate ADR1000 circuit performance without the effects of the output gain 10 V amplifier added. ADR1000 circuit tempco can be compensated and adjusted to very low numbers by multiple methods, such as changing series resistance to zener cathode terminal or adding a weak feedback from voltage loop to oven control loop (with series resistor in order 100 k&Omega; to 1 M&Omega; between heater transistor emitter and ADR1000 zener anode pin 4). 

[CSV RAW-datafile](https://xdevs.com/doc/xDevs.com/QVRA/qvr_dual_raw_temperature_sweep_jan2024.csv)

The module under test with dual ADR1000 zener IC swept multiple times from +18.0 &deg;C to +28.0 &deg;C set temperature after initial warmup around 3-4 hours. The test module was powered by Fluke 792A battery pack and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) continuously. 

The temperature sweep rate varied from 0.005 &deg;C/minute to verify settling time of the assembly under test. Then the second order polynominal was best fit to the measured voltage points and temperature coefficients were calculated. First cell measured &alpha; = -0.0168 &micro;V/V/K ; &beta; = +0.0008 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+33.0 &deg;C*. Second cell measured slightly worse &alpha; = -0.0325 &micro;V/V/K ; &beta; = +0.018 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+33.0 &deg;C*. Both cells demonstrated excellent temperature stability performance after trimming.

Summary table presented below.

| **Dual module**    | **Parameter for output 1** | **Parameter for output 2**  | **Unit**     | **Notes**                         |
| :------------      | :-----------:              | :-----------:               | :--------:   | :-------------------------------: |
| Calibration date   | JAN/23/2024                | JAN/23/2024                 |              | +23 &deg;C ambient, by 3458 group |
| Reference Temp T   |       23.00                |       23.00                 | &deg;C       |                                   |
| Nominal output     | 6.623                      | 6.626                       | V            | 5 mA, +51 &deg;C 11.5k&Omega;/1k&Omega;|
| 1st fit const      | -3.67218517E-7             | -7.76239984E-7              |              |                                   |
| 2nd fit const      | 5.56469404E-9              | 1.21919328E-8               |              |                                   |
| Gain const         | 6.62362660                 | 6.62683645                  | V            |                                   |
| EMF, T₂₃           | **6.6236211**              | **6.6268250**               | V            |                                   |
| &alpha; T₂₃        | -0.0168                    | -0.0325                     | &micro;V/V/K |                                   |
| &beta;             | +0.0008                    | +0.0018                     | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 33.0                       | 31.8                        | &deg;C       |                                   |
| Relative U, k=2    | 2.0                        | 2.0                         | &micro;V/V   | Within 1 week                     |

Temperature chart in the programmable air-bath sensor, placed next to the DUT module is also available. Temperature sensor used is Honeywell HEL-705 PT1000 RTD, digitized with Fluke 1529 thermometer readout. Small +0.2 &deg;C offset was observed during the measurement due to local heating from the power dissipated in the module inside the airbath.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_6v6_final_tc_sweep_blk.png)

Environmental parameters such as ambient temperature, pressure and humidity were monitored by [Bosch BME280-based sensor](https://xdevs.com/guide/thp_rpi/), digitized directly with Raspberry Pi 3B I2C interface bus. This sensor provided reference data to ensure that ambient conditions were stable and within short-term 24-hour stability specifications of used DVMs. Overall ambient temperature change during the whole test duration was recorded at 1.5 &deg;C. No additional correction to DMM temperature coefficient applied.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_6v6_env_time_blk.png)

## ADR1000AHZ module QVR2, two chips averaged, 10 V amplified output

Same module as in test above with two-ADR PCBA but this time both zener 6.625V outputs were combined into average with pair of 100 &Omega; resistors and output amplifier to 10 V with precision gain stage.

![QVR Dual TC sweep](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_final_tc_sweep_blk.png)

[CSV RAW-datafile](https://xdevs.com/doc/xDevs.com/QVRA/qvr_dual_temperature_sweep_feb2024.csv)

The module under test with dual ADR1000 zener IC swept multiple times from +18.0 &deg;C to +28.0 &deg;C set temperature after initial warmup around 3-4 hours. The test module was powered by Fluke 792A battery pack and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) continuously. 

The temperature sweep rate varied from 0.1 &deg;C to 0.04 &deg;C/minute to verify settling time of the assembly under test. Then the second order polynominal was best fit to the measured voltage points and temperature coefficients were calculated as result, with new final &alpha; = -0.040 &micro;V/V/K ; &beta; = +0.0017 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+34.5 &deg;C*. Summary table presented below.

| **Dual module**    | **Parameter**  | **Unit**     | **Notes**                         |
| :------------      | :-----------:  | :--------:   | :-------------------------------: |
| Calibration date   | FEB/4/2024     |              | +23 &deg;C ambient, by 3458 group |
| Reference Temp T   |       23.00    | &deg;C       |                                   |
| Nominal output     | 10.000000      | V            |                                   |
| 1st fit const      | -1.2009744E-6  |              |                                   |
| 2nd fit const      | 1.74072180E-8  |              |                                   |
| Gain const         | 10.0004070     | V            |                                   |
| EMF, T₂₃           | **10.0003886** | V            |                                   |
| &alpha; T₂₃        | -0.0400        | &micro;V/V/K |                                   |
| &beta;             | +0.0017        | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 34.5           | &deg;C       |                                   |
| TC, BOX, 18-28     | -0.0332        | &micro;V/V/K |                                   |
| Relative U, k=2    | 1.6            | &micro;V/V   | Within 24 hours                   |

Temperature chart in the programmable air-bath sensor, placed next to the DUT module is also available. Temperature sensor used is Honeywell HEL-705 PT1000 RTD, digitized with Fluke 1529 thermometer readout. Small +0.2 &deg;C offset was observed during the measurement due to local heating from the power dissipated in the module inside the airbath.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_tc_time_blk.png)

Environmental parameters such as ambient temperature, pressure and humidity were monitored by [Bosch BME280-based sensor](https://xdevs.com/guide/thp_rpi/), digitized directly with Raspberry Pi 3B I2C interface bus. This sensor provided reference data to ensure that ambient conditions were stable and within short-term 24-hour stability specifications of used DVMs. Overall ambient temperature change during the whole test duration was recorded at 1.4 &deg;C. No additional correction to DMM temperature coefficient applied.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr2_10v_env_time_blk.png)

## ADR1000AHZ module QVR1, single chip, 10 V amplified output

![QVR Single TC sweep](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr1_10v_final_tc_sweep_blk.png)

[CSV RAW-datafile](https://xdevs.com/doc/xDevs.com/QVRA/qvr_single_temperature_sweep_oct2022.csv)

The module under with single ADR1000 zener IC test swept multiple times from +17.5 &deg;C to +35.3 &deg;C set temperature after initial warmup around 3-4 hours. The test module was powered by Fluke 792A battery pack and output digitized by [HP3458A DVM](https://xdevs.com/fix/hp3458a) continuously. 

The temperature sweep rate varied from 0.1 &deg;C to 0.04 &deg;C/minute to verify settling time of the assembly under test. Then the second order polynominal was best fit to the measured voltage points and temperature coefficients were calculated as result, with new final &alpha; = -0.0424 &micro;V/V/K ; &beta; = +0.0061 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+26.5 &deg;C*. Summary table presented below.

| **Dual module**    | **Parameter**  | **Unit**     | **Notes**                         |
| :------------      | :-----------:  | :--------:   | :-------------------------------: |
| Calibration date   | OCT/21/2022    |              | +23 &deg;C ambient, by 3458A      |
| Reference Temp T   |       23.00    | &deg;C       |                                   |
| Nominal output     | 10.000000      | V            |                                   |
| 1st fit const      | -3.3225975E-6  |              |                                   |
| 2nd fit const      | 6.0919734E-8   |              |                                   |
| Gain const         | 10.0000675     | V            |                                   |
| EMF, T₂₃           | **10.0000255** | V            |                                   |
| &alpha; T₂₃        | -0.0520        | &micro;V/V/K |                                   |
| &beta;             | +0.0061        | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 27.3           | &deg;C       |                                   |
| TC, BOX, 18-28     | -0.065         | &micro;V/V/K | In heating direction              |
| Relative U, k=2    | 1.8            | &micro;V/V   | Within 24 hours                   |

Temperature chart in the programmable air-bath sensor, placed next to the DUT module is also available. Temperature sensor used is Honeywell HEL-705 PT1000 RTD, digitized with Fluke 1529 thermometer readout. Small +0.2 &deg;C offset was observed during the measurement due to local heating from the power dissipated in the module inside the airbath.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr1_10v_tc_time_blk.png)

Environmental parameters such as ambient temperature, pressure and humidity were monitored by [Bosch BME280-based sensor](https://xdevs.com/guide/thp_rpi/), digitized directly with Raspberry Pi 3B I2C interface bus. This sensor provided reference data to ensure that ambient conditions were stable and within short-term 24-hour stability specifications of used DVMs. Overall ambient temperature change during the whole test duration was recorded at 0.36 &deg;C. No additional correction to DMM temperature coefficient applied.

![](https://xdevs.com/doc/xDevs.com/QVRA/qvr_adr1_10v_env_time_blk.png)

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

| **Device under test** | **Output**     | **&alpha; T₂₃**        | **&beta;**                 | **Test date**  |
| :------------         | :-----------:  | :--------------------: | :------------------------: | :------------: |
| Quad ADR1000 module   | xx.xxxxxxx V   | xx.xxxx &micro;V/V/K   | xx.xxxx &micro;V/V/K²      | xxx/x/2024     |
| Dual ADR1000 module   | 10.0003886 V   | -0.0400 &micro;V/V/K   | +0.0017 &micro;V/V/K²      | FEB/4/2024     |
| Single ADR1000 module | xx.xxxxxxx V   | xx.xxxx &micro;V/V/K   | xx.xxxx &micro;V/V/K²      | xxx/x/2024     |

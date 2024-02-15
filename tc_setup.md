# Temperature coefficient measurements

---

Total number of devices evaluated in this test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 4 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

Temperature is a large factor and possible measurement error contributor of the laboratory instrument. Amplitude of temperature-related output change determines temperature coefficient and depends on many design features, such as materials, power distribution, physical layout and electrical circuit design. Minimizing temperature coefficient can be achieved by using material junctions with low parasitic EMF, careful thermal design with optimized uniformity and active heating/cooling stabilization.

Buried zeners such as LTZ1000, ADR1000, LM399 and ADR1399 implement integrated on-chip heating to remove most of the temperature coefficient. Residual coefficient mostly depends on circuit design and component choice. This can be measured by long-scale DVM with external environmental chamber with programmable temperature. ADR1000 module's temperature coefficient evaluated over the temperature range from +18 C to +28 C over the 24-hour test duration. The temperature coefficient test was performed with 8 steps. 

The instrument setup consisted of a set of stable 3458A DMMs, programmable air-bath with TEC-based heat pump operated by Model 2510 SMU in bipolar mode. The air bath is configured to provide both heating and cooling to allow temperatures above and below ambient. The temperature of the DUT module was measured separately by precision PT1000 RTD and Model 1529 temperature readout with uncertainty &plusmn;0.5 &deg;C. Modules under test were powered by a battery pack, the same one that used in noise measurement experiments.

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

The first test is to measure voltage stability against temperature change of individual zener output for each of the two populated circuits on the QVR module PCBA. This is achieved by removing the connection to the averaging resistor network at the output of each cell and routing kelvin-connected 6.6 V to separate DMM. This way, it is possible to evaluate ADR1000 circuit performance without the effects of the output gain 10 V amplifier added. ADR1000s circuit temperature coefficient can be compensated and adjusted to very low numbers by multiple methods, such as changing series resistance to zener cathode terminal or adding a weak feedback from voltage loop to oven control loop (with series resistor in order 100 k&Omega; to 1 M&Omega; between heater transistor emitter and ADR1000 zener anode pin 4).

![https://xdevs.com/doc/xDevs.com/QVRA/qvrq_ref_1.jpg](https://xdevs.com/doc/xDevs.com/QVRA/qvrq_ref.jpg)

This PCBA was populated with four cells, each with own ADR1000 chip, opamps, resistors, heater transistor and all additional components. Each cell utilized OPA2140 opamp with temperature setpoint resistor divider VPG VHD200 11.5 k&Omega; | 1 k&Omega; and VPG VHP202 80 &Omega; for zener current setting.

![QVR4 Block diagram](https://xdevs.com/doc/xDevs.com/QVR/block_blk.png)

The module under test with quad ADR1000 zener ICs swept multiple times from a wider +17.0 &deg;C to +55.0 &deg;C set temperature after initial warmup around 3 hours. Excessive maximum temperature was set deliberately to determine actual ADR1000 integrated oven thermal margin.

[RAW-data file with 40-53 temperature range in CSV](https://github.com/tin-/adr1000/blob/main/raw/hp3458abc_k2002ltc_qvrq_raw6v6_tcr_pretrim_run_feb2024_40-53.csv)

The test module was powered by linear triple channel power supply and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) and one Keithley 2002LTC continuously. 

* Cell A ran out of the temperature margin at T = +48.6 &deg;C
* Cell B ran out of the temperature margin at T = +48.5 &deg;C
* Cell C ran out of the temperature margin at T = +46.0 &deg;C
* Cell D ran out of the temperature margin at T = +46.6 &deg;C

This data gives about 2...5 degree margin room between ambient temperature to calculated oven set point +51.0 °C which is pretty close to expected deviation. Some of the heat from the onboard oven is lost in thermal dissipation into PCB, cover and air around the chip, since ADR1000 does not use thermal insulation glass balls like the LTZ1000ACH. To be safe in a practical circuit, it would be reasonable to maintain at least 10 ° margin between maximum acceptable ambient/module temperature and actual ADR1000 oven temperature set point. For the completeness, here's calculated temperature coefficients with zener outside the temperature range with ambient temperature above oven set point.

| **QVR4 module**    | **CELL A**    | **CELL B**    | **CELL C**   | **CELL D**   | **Unit**     | **Notes**         |
| :------------:     | :-----------:  | :-----------:  | :-----------:   | :-----------:  | :--------:   | :-------------------------------: |
| Temperature range  | 50-53 | 50-53 | 50-53 | 50-53 | &deg;C | Out of temperature data |
| 1st fit const      | -1.31376006E-03 | -1.11909944E-03 | -2.00939698E-03 | -1.94526833E-03 |              |  |
| 2nd fit const      | 4.35502247E-06  | 2.18797005E-06  | 1.08683322E-05  | 9.95157673E-06  |              |  |
| Gain const         | 6.69299635      | 6.68675020      | 6.71047532      | 6.70819104      | V            |  |
| EMF, T₂₃           | **6.6650837**   | **6.6621683**   | **6.6700085**   | **6.6687143**   | V            |  |
| &alpha; T₂₃        | -167.05         | -152.87         | -226.31         | -223.06         | &micro;V/V/K |  |
| &beta;             | +0.654          | +0.328          | +1.629          | +1.492          | &micro;V/V/K²|  |
| Temp at &alpha;=0  | +150.8          | +255.7          | +92.4           | +97.7           | &deg;C       |  |

In the temperature range +23 &deg;C to +40 &deg;C, which is within the safe margin with the oven operating in proper regulation, temperature coefficient was measured and calculated from a single sweep from +23 +40 °C to +40 °C. This was done without any additional temperature trim resistor to compensate for the inherent negative temperature coefficient of the ADR1000 zener and voltage loop transistor.

[RAW-data file with 23-40 temperature range in CSV](https://github.com/tin-/adr1000/blob/main/raw/hp3458abc_k2002ltc_qvrq_raw6v6_tcr_pretrim_run_feb2024_23_40.csv)

| **QVR4 module**    | **CELL A**    | **CELL B**    | **CELL C**   | **CELL D**   | **Unit**     | **Notes**                         |
| :------------:     | :-----------:  | :-----------:  | :-----------:   | :-----------:  | :--------:   | :-------------------------------: |
| Calibration date   | FEB/8/2024     | FEB/8/2024     | FEB/8/2024      | FEB/8/2024     |              | +23 &deg;C ambient, by 3458+2002 group |
| Reference Temp T   |       23.00    |       23.00    |       23.00     |       23.00    | &deg;C       |                                   |
| Nominal output     | 6.63           | 6.63           | 6.63            | 6.63           | V            | 5 mA, +51 &deg;C 11.5k&Omega;/1k&Omega;|
| 1st fit const      | -3.01898268E-06 | -1.95303570E-06 | -2.50732921E-06 | -7.01969730E-07 |              |                                   |
| 2nd fit const      | 1.54335922E-08 | 4.20163160E-09 | 1.13442137E-08  | 4.22027591E-09 |              |                                   |
| Gain const         | 6.63889998     | 6.63667779     | 6.63802227      | 6.63969562     | V            |                                   |
| EMF, T₂₃           | **6.6388387**  | **6.6366351**  | **6.6379706**   | **6.6396817**  | V            |                                   |
| &alpha; T₂₃        | -0.3478        | -0.2652        | -0.2991         | -0.0765        | &micro;V/V/K |                                   |
| &beta;             | 0.0023         | 0.0006         | 0.0017          | 0.0006         | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 97.8           | 232.4          | 110.5           | 83.2           | &deg;C       |                                   |
| Relative U, k=2    | 2.0            | 2.0            | 2.0             | 2.0            | &micro;V/V   | Within 1 week                     |

Cell D temperature coefficient is not too bad, but all the other cells require additional trimming to reduce temperature coefficient.

## ADR1000AHZ module QVR4, four chips individual outputs, after trim

## ADR1000AHZ module QVR4, four chips averaged

## LTD-QVR module with mixed zeners, four chips individual outputs, with trim

Additional module was assembled fresh on February 11, 2024 with goal to run different chips in the same PCBA in same conditions and compare their long-term stability from first power on. 

![LTD QVR module](https://xdevs.com/doc/xDevs.com/QVRL/img/block_ltdb.png)

No magical special aging was performed on any of the chips. They sat on the shelf unused for some time and now just soldered on the board fresh.

| **Parameter**        | **Cell A** | **Cell B** | **Cell C** | **Cell D** |
| :------------------: | :-------: | :-------: | :-------: | :-------: |
|Zener type            |  LTZ1000CH | LTZ1000ACH | ADR1000AHZ | ADR1000AHZ |
|Date code             |   2128    | 2234 | 2333 | 1839 |
|Temp setpoint         | 13 k&Omega; / 1 k&Omega; VHD200 | 13 k&Omega; / 1 k&Omega; VHD200 | 16.0674 k&Omega; / 1.3015 k&Omega; | 13 k&Omega; / 1 k&Omega; VHD200 |
|Iz set resistor       |120 &Omega; VHP203T | 120 &Omega; VHP203T  | 80 &Omega; VHP202T | 100 &Omega; VHP202T |
|Temp point voltage, V | 0.506 | 0.511 | 0.495 | 0.472 |
|Iz voltage, measured V| 0.4240 | 0.429 | 0.4846 | 0.4734 |
|Iz current, calculated| 3.53 mA | 3.57 mA | 6.06 mA | 4.73 mA |
|Opamp                 | TI OPA2140 | TI OPA2140 | TI OPA2140 | TI OPA2140 |
|Q1 resistor           | Susumu 68 k&Omega; | Susumu 68 k&Omega; | MELF 62 k&Omega; | MELF 62 k&Omega; |
|Q2 resistor           | Susumu 68 k&Omega; | Susumu 68 k&Omega; | MELF 62 k&Omega; | MELF 62 k&Omega; |
|FB capacitors         | 0.15 uF 1206 film  | 0.15 uF 1206 film  | 0.15 uF 1206 film  | 0.15 uF 1206 film  |
|TC feedback           | 150 k&Omega; | 820 k&Omega; | 334 k&Omega; | 820 k&Omega; |
|Noise, 0.1 Hz - 10 Hz | 895 nV pk-pk | 957 nV pk-pk | 367 nV pk-pk | 410 nV pk-pk |
|[Output voltage, FEB.13.2024](https://xdevs.com/hp3458abc_k2002ltc_ltdqvr_qvrq_raw6v6fix_avg_tcr_40c_820kABD_trimmed10v_run_feb2024/) | 7.17232133 V | 7.09003609 V | 6.60987871 V | 6.62218042 V |

![LTD Board photo](https://xdevs.com/doc/xDevs.com/QVRL/img/ltdqvr_top_1.jpg)

| **LTD-QVR module** | **CELL A**    | **CELL B**    | **CELL C**   | **CELL D**   | **Unit**     | **Notes**                         |
| :------------:     | :-----------:  | :-----------:  | :-----------:   | :-----------:  | :--------:   | :-------------------------------: |
| Zener type         |  LTZ1000CH | LTZ1000ACH | ADR1000AHZ | ADR1000AHZ |
| Date code          |   2128    | 2234 | 2333 | 1839 |
| Calibration date   | FEB/16/2024    | FEB/16/2024    | FEB/16/2024     | FEB/16/2024    |              | +23 &deg;C ambient, by 3458+2002 group |
| Reference Temp T   |       23.00    |       23.00    |       23.00     |       23.00    | &deg;C       |                                   |
| Nominal output     | 7.2            | 7.1            | 6.6             | 6.6            | V            | |
| 1st fit const      | xxxxxxxxxxxxxxx | xxxxxxxxxxxxxxx | xxxxxxxxxxxxxxx | xxxxxxxxxxxxxxx |              |                                   |
| 2nd fit const      | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx | xxxxxxxxxxxxxx  | xxxxxxxxxxxxxx |              |                                   |
| Gain const         | xxxxxxxxxx     | xxxxxxxxxx     | xxxxxxxxxx      | xxxxxxxxxx     | V            |                                   |
| EMF, T₂₃           | **xxxxxxxxx**  | **xxxxxxxxx**  | **xxxxxxxxx**   | **xxxxxxxxx**  | V            |                                   |
| &alpha; T₂₃        | xxxxxxx        | xxxxxxx        | xxxxxxx         | xxxxxxx        | &micro;V/V/K |                                   |
| &beta;             | xxxxxx         | xxxxxx         | xxxxxx          | xxxxxx         | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | xxxx           | xxxxx          | xxxxx           | xxxx           | &deg;C       |                                   |
| Relative U, k=2    | 4.0            | 2.0            | 2.0             | 2.0            | &micro;V/V   | Within 1 week                     |

## ADR1000AHZ module QVR2, two chips, individual 6.62 V zener IC outputs

First test is to measure voltage stability against temperature change of individual zener output for each of the two populated circuits on the QVR module PCBA. This is achieved by removing the connection to averaging resistor network at the output of each cell and routing kelvin-connected 6.6 V to separate DMM. This way it is possible to evaluate ADR1000 circuit performance without the effects of the output gain 10 V amplifier added. ADR1000 circuit tempco can be compensated and adjusted to very low numbers by multiple methods, such as changing series resistance to zener cathode terminal or adding a weak feedback from voltage loop to oven control loop (with series resistor in order 100 k&Omega; to 1 M&Omega; between heater transistor emitter and ADR1000 zener anode pin 4). 

[CSV RAW-datafile](https://xdevs.com/doc/xDevs.com/QVRA/qvr_dual_raw_temperature_sweep_jan2024.csv)

The module under test with dual ADR1000 zener IC swept multiple times from +18.0 &deg;C to +28.0 &deg;C set temperature after initial warmup around 3-4 hours. The test module was powered by Fluke 792A battery pack and output digitized by three [HP3458A DVMs](https://xdevs.com/fix/hp3458a) continuously. 

The temperature sweep rate varied from 0.005 &deg;C/minute to verify settling time of the assembly under test. Then the second order polynominal was best fit to the measured voltage points and temperature coefficients were calculated. First cell measured &alpha; = -0.0168 &micro;V/V/K ; &beta; = +0.0008 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+33.0 &deg;C*. Second cell measured slightly worse &alpha; = -0.0325 &micro;V/V/K ; &beta; = +0.018 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+33.0 &deg;C*. Both cells demonstrated excellent temperature stability performance after trimming.

Summary table presented below.

| **Dual module**    | **Parameter for output 1** | **Parameter for output 2**  | **Unit**     | **Notes**                         |
| :------------:     | :-----------:              | :-----------:               | :--------:   | :-------------------------------: |
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
| :------------:     | :-----------:  | :--------:   | :-------------------------------: |
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
| :------------:      | :-----------:  | :--------:   | :-------------------------------: |
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

## LTZ1000ACH "FX" prototype S/N 001, trimmed 10V output

The module labelled [xDevs FX](https://xdevs.com/article/792x/) is populated with single LTZ1000A zener IC test swept multiple times from +17.0 &deg;C to +37.5 &deg;C set temperature after initial warmup around 4 hours. The test module was powered by Fluke 792A battery pack and output digitized by [HP3458A DVM](https://xdevs.com/fix/hp3458a) continuously. FX module utilized LTC1013 opamp with temperature setpoint resistor divider VPG VHD200 13 k&Omega; | 1 k&Omega; and VPG VHP202 120 &Omega; for zener current setting. 

![Resistor network on the FX module](https://xdevs.com/doc/xDevs.com/FX/usac/usac_rnet_1.jpg)

Output is amplified to +10 V with thin film NiCr resistor network and precision fine-tune resistor at the taps. Amplifier ADA4522-2 SOIC-8 IC was utilized to provide stable low-noise output

[RAW-file with data for FX prototype unit after trimming tempco](https://github.com/tin-/adr1000/blob/main/raw/fx001_ltz_tempco_hp3458abc_oct2022.csv)

| **FX001 module**   | **Parameter**   | **Unit**     | **Notes**                         |
| :-----------:      | :-----------:   | :----------: | :-------------------------------: |
| Calibration date   | OCT/21/2022     |              | +23 &deg;C ambient, by 3458A      |
| Reference Temp T   |       23.00     | &deg;C       |                                   |
| Nominal output     | 10.000000       | V            |                                   |
| 1st fit const      | -1.52635842E-06 |              |                                   |
| 2nd fit const      | 3.17024164E-08  |              |                                   |
| Gain const         | 10.0000298      | V            |                                   |
| EMF, T₂₃           | **10.0000115**  | V            |                                   |
| &alpha; T₂₃        | -0.0068         | &micro;V/V/K |                                   |
| &beta;             | +0.0032         | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 24.1            | &deg;C       |                                   |
| Relative U, k=2    | 1.5             | &micro;V/V   | Within 24 hours                   |

This prototype LTZ1000ACH-based reference demonstrated excellent temperature stability after trimming and adjustment.  Final temperature coefficients determined as &alpha; = -0.0068 &micro;V/V/K ; &beta; = +0.0032 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+24.1 &deg;C*. Summary table presented above as well.

## LTZ1000ACH "FX" for USA Calibration Club, trimmed 10V output

The module labelled [xDevs FX](https://xdevs.com/article/792x/) donated for USA Calibration club metrology enthusiasts is populated with single LTZ1000A zener IC and VHP resistors. It was swept multiple times from +18.0 &deg;C to +28.5 &deg;C set temperature during validation and calibration steps. The test module was powered by Fluke 792A battery pack and output digitized by [HP3458A DVM](https://xdevs.com/fix/hp3458a) continuously. This FX module utilized LTC1013 opamp with temperature setpoint resistor divider VPG VHD200 13 k&Omega; | 1 k&Omega; and VPG VHP202 120 &Omega; for zener current setting. 

![USAC FX Tempco data](https://xdevs.com/doc/xDevs.com/FX/usac/usac_fx_tc_jan2023.png)

| **USA Club module**    | **Parameter**   | **Unit**     | **Notes**                         |
| :-----------:      | :-----------:   | :----------: | :-------------------------------: |
| Calibration date   | JAN/15/2023     |              | +23 &deg;C ambient, by 3458A      |
| Reference Temp T   |       23.00     | &deg;C       |                                   |
| Nominal output     | 10.000000       | V            |                                   |
| 1st fit const      | 2.59343E-9      |              |                                   |
| 2nd fit const      | -3.61039E-7     |              |                                   |
| Gain const         | 9.9999691       | V            |                                   |
| EMF, T₂₃           | **9.99996217**  | V            |                                   |
| &alpha; T₂₃        | -0.0242         | &micro;V/V/K |                                   |
| &beta;             | +0.0003         | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 69.6            | &deg;C       |                                   |
| Relative U, k=2    | 0.55            | &micro;V/V   | Within 24 hours                   |

Module again demonstrated excellent temperature stability on the 10 V output after trimming and adjustment process.  Final temperature coefficients determined as &alpha; = -0.0242 &micro;V/V/K ; &beta; = +0.0003 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+69.6 &deg;C*. Summary table presented above as well.

## LTZ1000ACH "FX" prototype S/N "Echo", trimmed 10V output

Same design module was built with codename "Echo" as well with similar trimming and components used. This reference module utilized LTC1013 opamp with temperature setpoint resistor divider VPG VHD200 13 k&Omega; | 1 k&Omega; and VPG VHP202 120 &Omega; for zener current setting. 

| **Echo module**    | **Parameter**   | **Unit**     | **Notes**                         |
| :-----------:      | :-----------:   | :----------: | :-------------------------------: |
| Calibration date   | MAR/19/2019     |              | +23 &deg;C ambient, by 3458A      |
| Reference Temp T   |       23.00     | &deg;C       |                                   |
| Nominal output     | 10.000000       | V            |                                   |
| 1st fit const      | -8.911939E-08   |              |                                   |
| 2nd fit const      | 2.765246E-09    |              |                                   |
| Gain const         | 9.9999575       | V            |                                   |
| EMF, T₂₃           | **9.9999569**   | V            |                                   |
| &alpha; T₂₃        | +0.0038         | &micro;V/V/K |                                   |
| &beta;             | +0.0003         | &micro;V/V/K²|                                   |
| Temp at &alpha;=0  | 16.1            | &deg;C       |                                   |
| Relative U, k=2    | 4.1             | &micro;V/V   | Within 24 hours                   |

Module demonstrated excellent temperature stability on the 10 V output after trimming and adjustment process.  Final temperature coefficients determined as &alpha; = +0.0038 &micro;V/V/K ; &beta; = +0.0003 &micro;V/V/K² and zero TCR intersection crossover point calculated at *+16.1 &deg;C*. Summary table presented above as well.

## HP 3458A unit 1, A9 LTZ1000ACH module voltage

TBD

## HP 3458A unit 2, A9 LTZ1000ACH module voltage

TBD

New Analog Devices ADR1000AHZ device in a typical application circuit can indeed demonstrate temperature stability better than &plusmn;0.05 &micro;V/V/K given the adequate parts selection. This is similar to LTZ1000/LTZ1000A solution which was proven by decades of operation in magnitude of design variations and commercial instruments.

Data set table with all measurement values is also presented below for further analysis. 

| **Device under test**          | **Output**     | **&alpha; T₂₃**        | **&beta;**                 | Zero &alpha; temperature | **Test date**  |
| :------------                  | :-----------:  | :--------------------: | :------------------------: | :----: | :------------: |
| Quad ADR1000 module, cell A, pretrim |  6.6388387 V   | -0.3478 &micro;V/V/K   | +0.0023 &micro;V/V/K²      | +97.8 &deg;C | FEB/8/2024     |
| Quad ADR1000 module, cell B, pretrim |  6.6366351 V   | -0.2652 &micro;V/V/K   | +0.0006 &micro;V/V/K²      | +232 &deg;C | FEB/8/2024     |
| Quad ADR1000 module, cell C, pretrim |  6.6379706 V   | -0.2991 &micro;V/V/K   | +0.0017 &micro;V/V/K²      | +110.5 &deg;C | FEB/8/2024     |
| Quad ADR1000 module, cell D, pretrim |  6.6396817 V   | -0.0765 &micro;V/V/K   | +0.0006 &micro;V/V/K²      | +83.2 &deg;C | FEB/8/2024     |
| Dual ADR1000 module, cell 1, trimmed |  6.6236211 V   | -0.0168 &micro;V/V/K   | +0.0008 &micro;V/V/K²      | +33.0 &deg;C | JAN/23/2024    |
| Dual ADR1000 module, cell 2, trimmed |  6.6268250 V   | -0.0325 &micro;V/V/K   | +0.0018 &micro;V/V/K²      | +31.8 &deg;C | JAN/23/2024    |
| Dual ADR1000 module, 10V, trimmed | 10.0003886 V   | -0.0400 &micro;V/V/K   | +0.0017 &micro;V/V/K²      | +27.3 &deg;C | FEB/4/2024     |
| Single ADR1000 module          | xx.xxxxxxx V   | xx.xxxx &micro;V/V/K   | xx.xxxx &micro;V/V/K²      | +xx.x &deg;C | xxx/x/2024     |
| Single LTZ1000A module S/N 001 | 10.0000115 V   | -0.0068 &micro;V/V/K   | +0.0032 &micro;V/V/K²      | +24.1 &deg;C | OCT/21/2022    |
| Single LTZ1000A module S/N USAC | 9.9999622 V   | -0.0242 &micro;V/V/K   | +0.0003 &micro;V/V/K²      | +69.6 &deg;C | JAN/15/2023    |
| Single LTZ1000A module S/N Echo | 9.9999569 V   | +0.0038 &micro;V/V/K   | +0.0003 &micro;V/V/K²      | +16.1 &deg;C | MAY/19/2019    |


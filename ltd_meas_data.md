# Long-term drift measurement
---

Total number of devices evaluated in long-term drift test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 3 units
* Reference with mixed ADR1000AHZ and LTZ1000, LTZ1000A, 1 unit
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit
* Fluke 732C commercial standard - 1 unit (6 month test)

![Long-term drift measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/ltd_setup_chart_bk.png)

Chips were soldered on [xDevs.com QVR reference module](https://xdevs.com/article/qvref) replicating ADR1000/LTZ1000A circuit from datasheet. Raw 6.62/7.x V output signal routed to the output or to the bipolar output gain stage on PCB using kelvin connection. Each unit is assembled and enclosed in metal enclosure for shielding and protection purposes. PCBA is mounted with flexible padding to avoid transfer of mechanical stress of vibration from the exterior instrumentation and environment. Voltage outputs are terminated with bare copper low-thermal 5-way binding posts to minimize thermal EMF.

## Manufacturer specifications

Accurate determination of long-term stability and drift rate of a solid-state zener reference is complex subject, specially with stability levels below 50 &micro;V/V. Stability depends on design of the chip, application circuit components selection and performance, PCB layout design, shielding, environmental contributors and method of measurement. All components involved in the design contribute to final output voltage differently. With careful design and validation many of the negative effects can be measured and corrected, but some residual drift will be inherently develop over the long time scales. 

![Long-term drift spec](https://github.com/tin-/adr1000/blob/main/img/ltd_spec.png?raw=true)

Manufacturer long-term stability specifications can be used as a starting point to determine expected performance of the IC. For high performance ovenized zener references such parameter is often included in datasheet as "long-term drift" or "long-term stability". ADR1000 &Delta;VREF_LTD is specified for 5 mA Base-Zener current, 100 &micro;A Collector-Q1 current and ambient temperature +25 &deg;C. We are provided with five relative numbers which include early life drift &plusmn;8.9 &micro;V/V and final drift rate &plusmn; 0.5 &micro;V/V after first 3000 hours powered. Specification of the long-term stability this way departs from more common drift rate representation using &Sqrt;(kHours), such as LTZ1000's specification 2 &Sqrt;(kHours). Representation &Sqrt;(kHours) have own limitations as actual zeners reach small but linear drift rate over few years time, unlike larger theoretical reduction of drift rate over time.

Ideally, measuring the long-term drift of the DUT's output voltage would require a significantly more stable reference so that a direct comparison could be done. Both ADR1000 and LTZ1000 are best chips that are commercially available capable to maintain stability better than 1 &micro;V/V, so better reference requirement implies direct comparison to Josephson Voltage Standard over a long duration of time. Such standard was not available for the duration of this study, so instead bank of well aged constantly-powered zener standards was utilized. Bank was calibrated multiple times on the Josehpson Voltage Standard to accurately determine long-term drift.

All long-term stability study was performed on the [xDevs.com QVR evaluation modules](https://xdevs.com/article/qvref). Three separate modules were used:

* SN0002 : Single populated ADR1000 cell, ADA4522-2 output amplifier for 10V
* SN0003 : Dual populated ADR1000 cells, ADA4522-2 output amplifier for 10V
* SN0004 : Quad populated ADR1000 cells, OPA2182 output amplifier for 10V

Overall block diagram of the module with fully populated four zener cells is shown below.

![Block diagram](https://xdevs.com/doc/xDevs.com/QVR/block_blk.png)

Outputs of each zener cell is averaged with passive resistor network into combined low noise 6.6 V DC level, which is filtered and fed to zero-drift chopper amplifier with discrete bipolar trasistor output stage for current source/sink capability. Zener cells powered by low-noise LT3045 linear regulator, except heaters. Heaters were powered separately from direct DC input (usually +12.5 V ... +13 V). Output amplifier also powered directly from bipolar DC inputs (+12.5 V ... +13 V and -12.5 V ... -13 V). 

DC Voltage standard stability verification to levels below a few &micro;V/V and complicated analysis of results is not an easy challenge. Different solutions and approaches were tested in practice by xDevs.com members since 2016. One of very good solutions was acquisition of the specialized low thermal scanner, such as [Dataproof 160 or 320](https://xdevs.com/fix/dp160a) and measuring each DC Voltage reference output individually by some high-end long scale multimeter, such as Keysight 3458A or Datron 1281. But this method is prone to errors and would depend on noise and temperature stability of DMM. Gain errors can be cancelled out by using calibrated DC standard with known drift as a reference, but other issues remain in this method.

Better approach is to perform the comparison of voltage differential in series opposition between two different DC standards. This significantly reduced requirements for DVM performance and even lower-end 6&frac12;-digit instruments such as [HP 34401A](https://xdevs.com/fix/hp34401a) used in lowest 100mV range can be used now to obtain sub-ppm uncertainty. But best instrument for this task is often sensitive nanovoltmeter which can easily resolve even fractions of microvolt between loosely matched 10 V outputs of various standards. 1 &micro;V of 10V equals 0.1 ppm resolution, and nanovoltmeter like Keithley 2182A or [Keysight 34420A](https://xdevs.com/fix/hp34420a) have own noise floor around 0.03 &micro;V. Given internal zener reference noise in commercial DC standards at level around ~1 &micro;V such comparison method is well suited for detecting even minute changes in output voltage EMF with best uncertainty. This procedure is also [covered with diagrams in detail here](https://xdevs.com/article/792x_cal/#zenercal)

This method is also what Fluke recommends performing calibration of their own 732B/C standards. In fact, even in Josephson Voltage standard system such as [NIST SRI 6000](https://www.nist.gov/sri/standard-reference-instruments/sri-6000-series-programmable-josephson-voltage-standard-pjvs) or [Supracon](http://www.supracon.com/files/online/NormaleSpannungsnormal/AC_QuantumVoltmeter_cooler.pdf) the calibration of unknown source or DC standard is done in very same manner. JVS array +10 V output configured as quantum-accurate noiseless level and connected in opposite to the compared zener, with commercial nanovoltmeter like HP 34420A measuring difference in nanovolts. This provides a direct link to intrinsic realization of the voltage, limited only by quality of the scanner/switching system, parasitic EMFs and nanovoltmeter detector short-term noise. Any gain and linearity errors of the nanovoltmeter can be easily calibrated and cancelled out with programmable JVS array output as well.

Based on similar setup and 2182A nanovoltmeter + DP160A scanner instrumentation following results were obtained. Tests were performed on both 6.6V zener output voltage and with scaled 10V output voltages.

![Long-term results](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_588days_blk.png)

### Updated data to September 2025

![Long-term 2025 results](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/all_data_sep2025.png)

Drift trend of primary 732A and 792X FX standards (used as key reference array) stays <1ppm over 1027 days period, continously logged by series-opposition setup. Short gap in August 2025 is due to relocation to new lab location 600km away, during which 732A/732B and 792X were transported in hard-shell plastic Pelican cases under uninterrupted battery power, while test FX1 (LTZ1000A module) and QVR ADR1000 modules were travelled cold unpowered. Temperature in transit was monitored by small datalogger and kept in range between +21 to +29 °C.

Both 732A and 792X standards were in good agreement after xDevs bank reassembly, while ADR1000 modules demonstrated significant jump about +2-+3 ppm with slow recovery towards previous values. To remind, these ADR1000 modules were not baked or treated prior to connection to zener monitoring array setup. Close-up on last few months of data around relocation can be analyzed on chart below:

![Can move data zoom](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/drift_2025can_sep24.png)

Unbaked/untreated ADR1000 modules take long time to recover to previous values after a month of powered-off state. In next sections we could take a look on individual modules performance and some more details.

## ADR1000AHZ module QVR4, four chips averaged. amplified 10 V output

This quad-ADR1000 long-term drift after first 6200 hours follows linear -2.672 &micro;V/V/year trend for 10V output. There is visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. This module was not adjusted for low temperature coefficient initially, but was adjusted and provided with 10 V output around 17 February 2024 week. Values used to determine long-term drift presented in a table below.

| **Drift data**         | Voltage relative to power up data | Date |
| :------------------:   | :-------: | :-------: |
| Deviation on 6200 hour mark  | -5.11 &micro;V/V | 25 July, 2023 |
| Deviation on 14100 hour mark  | -7.52 &micro;V/V | 22 June, 2024 |
| Deviation on 24650 hour mark  | -8.3 &micro;V/V | 26 July, 2025 |

## ADR1000AHZ module QVR4, four chips averaged, averaged zener 6.625V output

This module long-term drift after first 6200 hours on the same module as above, but with averaged zener 6.625V output follows linear -3.060 &micro;V/V/year trend. This result suggests the additional positive drift characteristics of output amplifier, as long-term drift trend is flatter on 10V output. There is same visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. 

| **Drift data**         | Voltage relative to power up data | Date |
| :------------------:   | :-------: | :-------: |
| Deviation on 6200 hour mark  | -6.25 &micro;V/V | 25 July, 2023 |
| Deviation on 14100 hour mark  | -9.01 &micro;V/V | 22 June, 2024 |

## ADR1000AHZ module QVR2, two chips averaged, amplified 10 V output

Dual-ADR1000 module 10V amplified output long-term drift after first 6200 hours follows linear -3.054 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.048 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. Long term drift slope is also smaller than RAW zener output on either single or quad-ADR modules. RAW zener output of dual-ADR module was not measured. Dual ADR1000 demonstrated largest overall deviation from the power up, with final value -9.88 &micro;V/V.

| **Drift data**         | Voltage relative to power up data | Date |
| :------------------:   | :-------: | :-------: |
| Deviation on 6200 hour mark  | -7.23 &micro;V/V | 25 July, 2023 |
| Deviation on 13800 hour mark  | -8.6 &micro;V/V | 9 June, 2024 |
| Deviation on 24650 hour mark  | -9.7 &micro;V/V | 26 July, 2025 |

## ADR1000AHZ module QVR1, single chip, 6.625V output

| **Drift data**         | Voltage relative to power up data | Date |
| :------------------:   | :-------: | :-------: |
| Deviation on 6200 hour mark  | -5.74 &micro;V/V | 25 July, 2023 |
| Deviation on 13800 hour mark  | -8.45 &micro;V/V | 9 June, 2024 |

Single-ADR1000 module long-term drift after first 6200 hours follows linear -3.124 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.05 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. 

## [LTZ1000ACH "FX" unit S/N X102, 10 V output](https://xdevs.com/article/792x/)

![FX Long-term drift](https://xdevs.com/doc/xDevs.com/FX/792x/xbank_nov_792x_2023.png)

Single-LTZ1000 FX module long-term drift after from the very beginning follows linear -0.174 &micro;V/V/year trend over the period of this study and -0.24 &micro;V/V/year over a trend since March 2019 till January 2024. Temperature coefficient was adjusted to -0.03 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. This reference runs under constant power uninterrupted since January 2018. 

## Mixed QVR-module with ADR and LTZ combination, assembled in the early 2024 for new study

Current setup is undergoing modification to include additional modules with new ICs and better setup to collect larger dataset for more detailed analysis in future. Additional module was assembled fresh on February 11, 2024 with goal to run different chips in the same PCBA in same conditions and compare their long-term stability from first power on. 

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
|TC feedback           | 140 k&Omega; | 820 k&Omega; | 680 k&Omega; | 820 k&Omega; |
|Noise, 0.1 Hz - 10 Hz | 895 nV pk-pk | 957 nV pk-pk | 367 nV pk-pk | 410 nV pk-pk |
|[Output voltage, FEB.13.2024](https://xdevs.com/hp3458abc_k2002ltc_ltdqvr_qvrq_raw6v6fix_avg_tcr_40c_820kABD_trimmed10v_run_feb2024/) | 7.17232133 V | 7.09003609 V | 6.60987871 V | 6.62218042 V |

![LTD Board photo](https://xdevs.com/doc/xDevs.com/QVRL/img/ltdqvr_top_1.jpg)

Averaging of zener outputs is also unused (Z6 network is not populated), as only individual zener IC outputs will be monitored from this module. 

![Setup with LTD QVR build](https://xdevs.com/doc/xDevs.com/QVRL/img/ltdqvr_resn_1.jpg)

After tempco trimming and adjustments on module SN0005 completed this module was permanently connected to zener array bank per NIST TN430 with series-opposition connected scanned zeners and nanovoltmeter. This will allow us to collect long-term drift data with one sample/zener collected every 1.5 hours. 

You an check first some more data with details in [Mid-term drift page](mtd_drift.md)

### June 2024 data : 3120 hours

![June data](https://xdevs.com/doc/xDevs.com/QVRL/cal/ltd_qvr_3120hrs.png)

To stir things up a little bit the board was powered off on June 22, 2024 3:00pm and baked in the convection oven at around +115 &deg;C for 8 hours. Reference module was unpowered during whole baking duration.

###  July 2025 data : 12696 hours, 529 days

![July 2025 data](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/ltdqvr_2025_jul27.png)

This char presents all samples acquired after running this module since 8 hours baking unpowered board on June 22, 2024. Baking process caused a large shift for both ADR1000 and LTZ1000CH cells and smaller shift for LTZ1000ACH cell. This was quite fruitful test, revealing that baked ADR1000 running at +75 °C oven temperature now reached stable condition after only 2 months. ADR1000 cell running at +65 °C took much longer 6 month after baking to settle at steady rate. I was out on vacation during December holidays and forgot to close the window to the lab, causing a dip in ambient temperature below +18 °C. This caused visible jump for LTZ reference cells and no impact on ADR1000 +75.

Beginning of July 2025 I've replaced Keithley 2182A nanovoltmeter to HP 34420A in the zener bank array (that was used to measure these samples too). And since this board outputs just raw zener voltages at 7.x and 6.6x V gain difference of nanovoltmeter caused the clearly visible shift of datasamples. But stability behaviour remained quite similar to data from 2182A. 

## Fluke 732A unit, S/N 4045004

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear -0.045 &micro;V/V/year trend. 

## Fluke 732A unit, S/N 3195010

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear +0.304 &micro;V/V/year trend. 

RAW data set with all measurement value is also available in Excel and CSV-format in this repository for the further analysis. 

[Excel RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_samples4.xlsx)

[CSV RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_samples.csv)

## Fluke 732C unit, S/N redacted

This commercial modern standard was tested against two zener arrays (xDevs - orange markers, Niko Lab - blue triangles). This test goals were to determine agreement between two different friendly labs for DCV 10V measurements and to evaluate 732C performance over a period of 6 month.

![732C data](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/732c_test.png)

This particular standard demonstrated fairly linear drift downwards at a rate about -2.2 nV/V/day or -0.79 &micro;V/V/year which is within specifications. Old well aged 732A and 732B standards however demonstrate much better performance, often below 0.3 &micro;V/V/year.

## Future work

The study of long-term drift leaves some questions open, such as how oven set point temperature and zener current affect long-term drift, and require larger sample set to gain more confidence in results. In theory, higher current and higher temperature would cause drift rate to accelerate as well, but it's not so simple in the real world application. Experimental verification of these claims would be very useful and will be done at a later date. These initial results exhibit larger than expected 0.5 &micro;V/V/year initial drift of new ADR1000 zener IC after first 6200 hours after power up and highlight importance of careful procedures and possible need of selection to obtain desired long term stability better than 1 &micro;V/V per year.

## Other notable references

* [Forum page about ADR1000-based references](https://www.eevblog.com/forum/metrology/lowest-drift-lowest-noise-voltage-reference/) - branadic and Andreas also demonstrated long-term drift by ADR1000 with similar behavior, despite completely different instrumentation approach.

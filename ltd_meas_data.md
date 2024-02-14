# Long-term drift measurement
---

Total number of devices evaluated in long-term drift test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 3 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

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

Based on similar setup and 2182A nanovoltmeter + DP160A scanner instrumentation following results were obtained:

![Long-term results](https://xdevs.com/doc/xDevs.com/QVRA/ltd_chart_10khrs_blk.png)

## ADR1000AHZ module QVR4, four chips averaged. amplified 10 V output

This quad-ADR1000 long-term drift after first 6200 hours follows linear -1.813 &micro;V/V/year trend for 10V output. There is visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. This module was not adjusted for low temperature coefficient yet.

## ADR1000AHZ module QVR4, four chips averaged, averaged zener 6.625V output

This module long-term drift after first 6200 hours on the same module as above, but with averaged zener 6.625V output follows linear -2.607 &micro;V/V/year trend. This result suggests the additional positive drift characteristics of output amplifier, as long-term drift trend is flatter on 10V output. There is same visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. 

## ADR1000AHZ module QVR2, two chips averaged, amplified 10 V output

Dual-ADR1000 module 10V amplified output long-term drift after first 6200 hours follows linear -2.217 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.048 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. Long term drift slope is also smaller than RAW zener output on either single or quad-ADR modules. RAW zener output of dual-ADR module was not measured.

## ADR1000AHZ module QVR1, single chip, 6.625V output

Single-ADR1000 module long-term drift after first 6200 hours follows linear -2.711 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.05 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. Single ADR1000 demonstrated largest overall deviation from the power up, with final value -8.7 &micro;V/V.

## [LTZ1000ACH "FX" unit S/N X102, 10 V output](https://xdevs.com/article/792x/)

![FX Long-term drift](https://xdevs.com/doc/xDevs.com/FX/792x/xbank_nov_792x_2023.png)

Single-LTZ1000 FX module long-term drift after from the very beginning follows linear -0.174 &micro;V/V/year trend over the period of this study and -0.24 &micro;V/V/year over a trend since March 2019 till January 2024. Temperature coefficient was adjusted to -0.03 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. This reference runs under constant power uninterrupted since January 2018. 

## Fluke 732A unit, S/N 4045004

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear -0.045 &micro;V/V/year trend. 

## Fluke 732A unit, S/N 3195010

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear +0.304 &micro;V/V/year trend. 

RAW data set with all measurement value is also available in Excel and CSV-format in this repository for the further analysis. 

[Excel RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_cml.xlsx)

[CSV RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_samples.csv)

## Future work

The study of long-term drift leaves some questions open, such as how oven set point temperature and zener current affect long-term drift, and require larger sample set to gain more confidence in results. In theory, higher current and higher temperature would cause drift rate to accelerate as well, but it's not so simple in the real world application. Experimental verification of these claims would be very useful and will be done at a later date. These initial results exhibit larger than expected 0.5 &;micro;V/V/year initial drift of new ADR1000 zener IC after first 6200 hours after power up and highlight importance of careful procedures and possible need of selection to obtain desired long term stability better than 1 &micro;V/V per year.

Current setup is undergoing modification to include additional modules with new ICs and better setup to collect larger dataset for more detailed analysis in future.

## Other notable references

* [Forum page about ADR1000-based references](https://www.eevblog.com/forum/metrology/lowest-drift-lowest-noise-voltage-reference/) - branadic and Andreas also demonstrated long-term drift by ADR1000 with similar behavior, despite completely different instrumentation approach.

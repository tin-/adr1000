# Long-term drift measurement
---

Total number of devices evaluated in long-term drift test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 3 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

![Long-term drift measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/ltd_setup_chart_bk.png)

Chips were soldered on [xDevs.com QVR reference module](https://xdevs.com/article/qvr) replicating ADR1000/LTZ1000A circuit from datasheet. Raw 6.62/7.x V output signal routed to the output or to the bipolar output gain stage on PCB using kelvin connection. Each unit is assembled and enclosed in metal enclosure for shielding and protection purposes. PCBA is mounted with flexible padding to avoid transfer of mechanical stress of vibration from the exterior instrumentation and environment. Voltage outputs are terminated with bare copper low-thermal 5-way binding posts to minimize thermal EMF.

## Manufacturer specifications

Accurate determination of long-term stability and drift rate of a solid-state zener reference is complex subject, specially with stability levels below 50 &micro;V/V. Stability depends on design of the chip, application circuit components selection and performance, PCB layout design, shielding, environmental contributors and method of measurement. All components involved in the design contribute to final output voltage differently. With careful design and validation many of the negative effects can be measured and corrected, but some residual drift will be inherently develop over the long time scales. 

Manufacturer long-term stability specifications can be used as a starting point to determine expected performance of the IC. For high performance ovenized zener references such parameter is often included in datasheet as "long-term drift" or "long-term stability". ADR1000 &Delta;VREF_LTD is specified for 5 mA Base-Zener current, 100 &micro;A Collector-Q1 current and ambient temperature +25 &deg;C. We are provided with five relative numbers which include early life drift &plusmn;8.9 &micro;V/V and final drift rate &plusmn; 0.5 &micro;V/V after first 3000 hours powered. Specification of the long-term stability this way departs from more common drift rate representation using &Sqrt;(kHours), such as LTZ1000's specification 2 &Sqrt;(kHours). Representation &Sqrt;(kHours) have own limitations as actual zeners reach small but linear drift rate over few years time, unlike larger theoretical reduction of drift rate over time.

Ideally, measuring the long-term drift of the DUT's output voltage would require a significantly more stable reference so that a direct comparison could be done. Both ADR1000 and LTZ1000 are best chips commercially available to maintain stability better than 1 &micro;V/V, so better reference requirement implies direct comparison to Josephson Voltage Standard over a long duration of time. Such standard was not available for the duration of this study, so instead bank of well aged constantly-powered zener standards was utilized. Bank was calibrated multiple times on the Josehpson Voltage Standard to accurately determine long-term drift.

Based on this instrumentation following results were obtained:

![Long-term results](https://xdevs.com/doc/xDevs.com/QVRA/ltd_chart_10khrs_blk.png)

## ADR1000AHZ module QVR4, four chips averaged. amplified 10 V output

This quad-ADR1000 long-term drift after first 6200 hours follows linear -1.813 &micro;V/V/year trend for 10V output. There is visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. This module was not adjusted for low temperature coefficient yet.

## ADR1000AHZ module QVR4, four chips averaged, averaged zener 6.625V output

This module long-term drift after first 6200 hours on the same module as above, but with averaged zener 6.625V output follows linear -2.607 &micro;V/V/year trend. This result suggests the additional positive drift characteristics of output amplifier, as long-term drift trend is flatter on 10V output. There is same visible temperature coefficient impact from end of September 2023 to December 2023 due to daily temperature cycling. 

## ADR1000AHZ module QVR2, two chips averaged, amplified 10 V output

Dual-ADR1000 module 10V amplified output long-term drift after first 6200 hours follows linear -2.217 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.048 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. Long term drift slope is also smaller than RAW zener output on either single or quad-ADR modules. RAW zener output of dual-ADR module was not measured.

## ADR1000AHZ module QVR1, single chip, 6.625V output

Single-ADR1000 module long-term drift after first 6200 hours follows linear -2.711 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.05 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. Single ADR1000 demonstrated largest overall deviation from the power up, with final value -8.7 &micro;V/V.

## LTZ1000ACH "FX" unit S/N 001, 10 V output

Single-LTZ1000 FX module long-term drift after from the very beginning follows linear -0.174 &micro;V/V/year trend. Temperature coefficient was adjusted to -0.03 &micro;V/V/K in this module, so we don't see additional noise from daily temperature changes in the laboratory. This reference runs under constant power uninterrupted since January 2018. 

## Fluke 732A unit, S/N 4045004

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear -0.045 &micro;V/V/year trend. 

## Fluke 732A unit, S/N 3195010

Commercial 10V DC voltage standard that was serviced and continously powered up since summer 2022. Long-term drift after from the very beginning follows linear +0.304 &micro;V/V/year trend. 

RAW data set with all measurement value is also available in Excel and CSV-format in this repository for the further analysis. 

[Excel RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_cml.xlsx)

[CSV RAW-data file with all points used in analysis](https://xdevs.com/doc/xDevs.com/QVRA/ltd_data_samples.csv)

## Future work

The study of long-term drift leaves some questions open, such as how oven set point temperature and zener current affect long-term drift and require larger sample set to gain more confidence in results. These initial results exhibit larger than expected 0.5 uV/V/year initial drift of new ADR1000 zener IC after first 6200 hours after power up and highlight importance of careful procedures and possible need of selection to obtain desired long term stability better than 1 &micro;V/V per year. 

Current setup is undergoing modification to include additional modules with new ICs and better setup to collect larger dataset for more detailed analysis in future.

## Other notable references

* [Forum page about ADR1000-based references](https://www.eevblog.com/forum/metrology/lowest-drift-lowest-noise-voltage-reference/) - branadic and Andreas also demonstrated long-term drift by ADR1000 with similar behaviour, despite completely different instrumentation approach.
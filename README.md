# ADR1000 performance study
Data repository for Analog Devices ADR1000-based xDevs.com module voltage standards performance, collected by [xDevs.com lab](https://xdevs.com/).

Current Status
--------------
* Drift data collection/analysis : [437 days done, in progress](ltd_meas_data.md)
* Data processing: in progress
* Short-term noise evaluation: [done](lf_noise.md)
* Tempco evaluation: [in progress](tc_setup.md)
* PSRR evaluation: planned
* Power on/off hysteresis evaluation: planned

Introduction
------------

This repository contains the data collected on [xDevs.com QVR](https://xdevs.com/article/qvref/) and [xDevs.com FX](https://xdevs.com/article/792x/) voltage reference modules assembled with [Analog Devices ADR1000AHZ](https://xdevs.com/article/adr1000order/) buried zener IC. Consistent with my primary use cases for these devices in DC voltage metrology projects, these modules designed with focus on low noise (measured at ~500 nV pk-pk from 0.01-10 Hz) and good stability below 10 ppm/year. The project includes number of datasets, provided for analysis and educational use. 

Issues and caveats
------------------

1. Long-term dataset is generated by in-house zener array from opposite-difference data, following concept outlined in [NIST/NBS Technical note 430](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote430.pdf). The absolute values for each voltage zener standard is relative to primary group in the array, xDevs.com FX S/N 001, Fluke 732A S/N 404 and Fluke 732A S/N 319. There link between SI voltage representation by Josephson effect for each specific DUT is done via limited amount of transfers by travel DC zener array, done in August 2019, October 2020 and November 2022. 

2. Long-term drift data for single-chip QVR ADR1000 module is based on combined drift from ADR1000 cell and 6.62V>10V output boost stage. Long-term drift data for multi-chip QVR ADR1000 module is based on averaged output of 6.62V cells without boost stage. All LTZ1000A-based devices data based on boosted 10V output.

3. Thermal coefficient and humidity coefficient contributors are not removed from the long-term drift data.

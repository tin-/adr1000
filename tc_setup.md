# Temperature coefficient measurements
---

Total number of devices evaluated in this test:

* References with ADR1000AHZ manufactured with date code 39 week 2018, 4 units
* References with LTZ1000ACH#PBF production devices - 2 units
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network - 1 unit

Temperature is large factor and possible measurement error contributor of the laboratory instrument. Amplitude of temperature-related output change determines temperature coefficient and depends on many design features, such as materials, power distribution, physical layout and electrical circuit design. Minimizing temperature coefficient can be achieved by using material junctions with low parasitic EMF, careful thermal design with optimized uniformity and active heating/cooling stabilisation.

Buried zeners such as LTZ1000, ADR1000, LM399 and ADR1399 implement integrated on-chip heating to remove most of temperature coefficient. Residual coefficient mostly depends on circuit design and component choice. This can be measured by long-scale DVM with external environmental chamber with programmable temperature. ADR1000 modules temperature coefficient evaluated over the temperature range from +16 C to +40 C over the 24 hour test duration. Temperature coefficient test was performed with 8 steps. 

Instrument setup consisted of set of stable 3458A DMMs, programmable air-bath with TEC-based heatpump operated by Model 2510 SMU in bipolar mode. Air bath configured to provide both heating and cooling to allow temperatures above and below ambient. Temperature of the DUT module was measured separately by precision PT1000 RTD and Model 1529 temperature readout with uncertainty &plusmn;0.5 &deg;C. Modules under test were powered by battery pack, same one that used in noise measurement experiments.

![TC measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/tc_setup_blk.png)

* Step A: Set temperatre chamber to fixed +23.0 C and collect 2 hours of voltage output data with 8.5-digit DMM.
* Step B: Ramp up temperatre chamber to +40.0 C with 0.01C/second speed while logging voltage output data with 8.5-digit DMM.
* Step C: Set temperatre chamber to +40.0 C and collect 2 hours of voltage output data with 8.5-digit DMM.
* Step D: Ramp down temperatre chamber to +23.0 C with -0.01C/second speed while logging voltage output data with 8.5-digit DMM.
* Step E: Set temperatre chamber to +23.0 C and collect 2 hours of voltage output data with 8.5-digit DMM.
* Step F: Ramp down temperatre chamber to +16.0 C with -0.01C/second speed while logging voltage output data with 8.5-digit DMM.
* Step G: Set temperatre chamber to +16.0 C and collect 2 hours of voltage output data with 8.5-digit DMM.
* Step H: Ramp up temperatre chamber to +23.0 C with 0.01C/second speed while logging voltage output data with 8.5-digit DMM.
* Step I: Set temperatre chamber to +23.0 C and collect 2 hours of voltage output data with 8.5-digit DMM.

This cycling sequence, data collection and communication with instruments over GPIB was automated with open-source Python program called TECkit running on single-board computer Raspberry Pi. 

Based on this instrumentation following results were obtained:

Based on these values new Analog Devices ADR1000AHZ device in a typical application circuit can demonstrate temperature stability better than &plusmn;0.05 &micro;V/V/K given the adequate parts selection. This is similar to LTZ1000/LTZ1000A solution which was proven by decades of operation in magnitude of design variations and commercial instruments.

Data set table with all measurement values is also presented below for further analysis. 


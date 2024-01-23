# 0.1-10 Hz bandwidth noise measurement
---

Total number of devices evaluated in this test:

* 49 ADR1000AHZ production devices, manufactured with date code 39 week 2018
* 5 LTZ1000CH production devices, manufactured in 1986, 1990 and 2019
* 32 LTZ1000ACH#PBF production devices, manufactured in the end of 2019 and 2020
* Fluke 5720A multi-function calibrator with output 7.19 VDC configured on 11V DC Voltage range
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network

Noise floor of the measurement setup and shorted LNA input measured at **102 nV** with standard deviation **9 nV**. Setup utilize Tektronix DPO7104C real-time oscilloscope and battery-powered AC-coupled LNA with gain +80 dB and pass-band 0.1-10 Hz. All zener chips were evaluated with bipolar Fluke 792A battery power supply to avoid any electrical interference from power line or ground loops. 

Zener current on test FX module PCB was set to 4.05 mA for ADR1000 and about 5.0 mA for LTZ1000. This was achieved by populated 120 &Omega; high stability ametal foil resistor from zener chip anode diode pin 4 and reference return point pin 7. 

![Shielding can with zener board](https://xdevs.com/doc/xDevs.com/AFX/nstest_rig_1.jpg)

Chips were installed in a socket populated on [xDevs.com FX reference module](https://xdevs.com/article/792x) replicating LTZ1000A recommended circuit from datasheet. Raw 6.62/7.x V output signal routed directly to LNA input via shielded coaxial cable. Each chip was powered up for 30 minutes to reach stable oven operating point and settled voltage across LNA input DC block capacitor. Whole module shielded in a metal can to reduce ambient noise interference during the measurement time. 

![![Preview](https://xdevs.com/doc/xDevs.com/AFX/adr_noise_testa_1.png)](https://xdevs.com/doc/xDevs.com/AFX/adr_noise_testa.png)

Based on this instrumentation following results were obtained:

## ADR1000AHZ chips - 49 pcs

* Lowest noise was measured for chip 2, **441 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 22, **571 nV peak to peak**
* Difference between chip 2 and chip 22 is 130 nV peak to peak
* Average noise across all 49 chips is **486 nV peak to peak**
* Median noise across all 49 chips is **479 nV peak to peak**

## LTZ1000ACH#PBF chips - 32 pcs

* Lowest noise was measured for chip 2, **651 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 28, **1242 nV peak to peak**
* Difference between chip 2 and chip 28 is 591 nV peak to peak
* Average noise across all 32 chips is **858 nV peak to peak**
* Median noise across all 32 chips is **835 nV peak to peak**

## LTZ1000CH chips - 5 pcs

* Lowest noise was measured for chip 3, **801 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 4, **1428 nV peak to peak**
* Difference between chip 3 and chip 4 is 627 nV peak to peak
* Average noise across all 5 chips is **1012 nV peak to peak**
* Median noise across all 5 chips is **978 nV peak to peak**

## Other noise values and devices for reference

* LTZ1000A datasheet specification, 1200 nV typical, 2000 nV peak to peak maximum with Iz = 5mA, 0.1 Hz - 10 Hz and Q1 current 100 &micro;A.
* ADR1000 datasheet specification, 900 nV typical peak to peak, no maximum specification, with Iz = 5mA, 0.1 Hz - 10 Hz and Q1 current 100 &micro;A.
* xDevs.com QVR module with averaged output by 4 x LTZ1000ACH chip : **442 nV peak to peak, &sigma; = 44 nV**
* Fluke 5720A multi-function H1 calibrator configured @ 7.19 V output measured noise : **3790 nV peak to peak, &sigma; = 512 nV**
* Fluke 5720A multi-function H2 calibrator configured @ 7.19 V output measured noise : **TBD nV peak to peak, &sigma; = TBD nV**
* Fluke 5700A multi-function N3 calibrator configured @ 7.19 V output measured noise : **TBD nV peak to peak, &sigma; = TBD nV**
* Wavetek 4808 multi-function N3 calibrator configured @ 7.19 V output measured noise : **TBD nV peak to peak, &sigma; = TBD nV**
* HP 3245A universal source with LTZ1000A KX module reference configured @ 7.19 V DC output measured noise : **TBD nV peak to peak, &sigma; = TBD nV**
* Keithley 2400 SMU with LM399 reference configured @ 7.19 V DC output measured noise : **TBD nV peak to peak, &sigma; = TBD nV**

![Noise chart summary](https://xdevs.com/doc/xDevs.com/QVRA/lf_noise_chart.png)

Vertical axis represents measured noise voltage and horizontal axis represent sample number.

Based on these values new Analog Devices ADR1000AHZ device measured to have 55.4% less noise than older Linear Technology LTZ1000ACH IC. This conclusion also supported by matching noise performance of single ADR1000AHZ compared to combined averaged noise from array of four selected LTZ1000A at a fraction of the BOM cost and power consumption. New reference IC can be very helpful for applications where low frequency noise is a critical performance parameter.

Data set table with all results presented below.

| Device                  | Datecode      | Measured noise peak-to-peak, 0.1-10 Hz | Standard deviation, 1 &sigma;|
| :------------ | :-------------: | :---------: | :-------: |
| ADR1000AHZ chip 1       | 39 week 2018 | 442 nV | 34 nV  |
| ADR1000AHZ chip 2       | 39 week 2018 | 441 nV | 48 nV  |
| ADR1000AHZ chip 3       | 39 week 2018 | 460 nV | 46 nV  |
| ADR1000AHZ chip 4       | 39 week 2018 | 458 nV | 44 nV  |
| ADR1000AHZ chip 5       | 39 week 2018 | 473 nV | 40 nV  |
| ADR1000AHZ chip 6       | 39 week 2018 | 469 nV | 42 nV  |
| ADR1000AHZ chip 7       | 39 week 2018 | 477 nV | 50 nV  |
| ADR1000AHZ chip 8       | 39 week 2018 | 479 nV | 51 nV  |
| ADR1000AHZ chip 9       | 39 week 2018 | 452 nV | 55 nV  |
| ADR1000AHZ chip 10      | 39 week 2018 | 499 nV | 44 nV  |
| ADR1000AHZ chip 11      | 39 week 2018 | 446 nV | 68 nV  |
| ADR1000AHZ chip 12      | 39 week 2018 | 471 nV | 43 nV  |
| ADR1000AHZ chip 13      | 39 week 2018 | 473 nV | 50 nV  |
| ADR1000AHZ chip 14      | 39 week 2018 | 461 nV | 40 nV  |
| ADR1000AHZ chip 15      | 39 week 2018 | 446 nV | 40 nV  |
| ADR1000AHZ chip 16      | 39 week 2018 | 461 nV | 47 nV  |
| ADR1000AHZ chip 17      | 39 week 2018 | 451 nV | 39 nV  |
| ADR1000AHZ chip 18      | 39 week 2018 | 520 nV | 48 nV  |
| ADR1000AHZ chip 19      | 39 week 2018 | 465 nV | 41 nV  |
| ADR1000AHZ chip 20      | 39 week 2018 | 511 nV | 107 nV |
| ADR1000AHZ chip 21      | 39 week 2018 | 487 nV | 47 nV  |
| ADR1000AHZ chip 22      | 39 week 2018 | 571 nV | 51 nV  |
| ADR1000AHZ chip 23      | 39 week 2018 | 479 nV | 53 nV  |
| ADR1000AHZ chip 24      | 39 week 2018 | 462 nV | 48 nV  |
| ADR1000AHZ chip 25      | 39 week 2018 | 547 nV | 52 nV  |
| ADR1000AHZ chip 26      | 39 week 2018 | 472 nV | 48 nV  |
| ADR1000AHZ chip 27      | 39 week 2018 | 493 nV | 46 nV  |
| ADR1000AHZ chip 28      | 39 week 2018 | 481 nV | 62 nV  |
| ADR1000AHZ chip 29      | 39 week 2018 | 527 nV | 53 nV  |
| ADR1000AHZ chip 30      | 39 week 2018 | 499 nV | 78 nV  |
| ADR1000AHZ chip 31      | 39 week 2018 | 475 nV | 49 nV  |
| ADR1000AHZ chip 32      | 39 week 2018 | 470 nV | 42 nV  |
| ADR1000AHZ chip 33      | 39 week 2018 | 491 nV | 47 nV  |
| ADR1000AHZ chip 34      | 39 week 2018 | 462 nV | 48 nV  |
| ADR1000AHZ chip 35      | 39 week 2018 | 509 nV | 54 nV  |
| ADR1000AHZ chip 36      | 39 week 2018 | 503 nV | 43 nV  |
| ADR1000AHZ chip 37      | 39 week 2018 | 464 nV | 44 nV  |
| ADR1000AHZ chip 38      | 39 week 2018 | 506 nV | 24 nV  |
| ADR1000AHZ chip 39      | 39 week 2018 | 531 nV | 38 nV  |
| ADR1000AHZ chip 40      | 39 week 2018 | 462 nV | 48 nV |
| ADR1000AHZ chip 41      | 39 week 2018 | 503 nV | 81 nV|
| ADR1000AHZ chip 42      | 39 week 2018 | 480 nV | 36 nV|
| ADR1000AHZ chip 43      | 39 week 2018 | 534 nV | 130 nV|
| ADR1000AHZ chip 44      | 39 week 2018 | 556 nV | 59 nV    |
| ADR1000AHZ chip 45      | 39 week 2018 | 464 nV | 44 nV    |
| ADR1000AHZ chip 46      | 39 week 2018 | 503 nV | 43 nV    |
| ADR1000AHZ chip 47      | 39 week 2018 | 509 nV | 47 nV    |
| ADR1000AHZ chip 48      | 39 week 2018 | 506 nV | 38 nV    |
| ADR1000AHZ chip 49      | 39 week 2018 | 531 nV | 52 nV    |
| LTZ1000ACH chip 1       | 37 week 2020 | 776 nV | 72 nV   |
| LTZ1000ACH chip 2       | 39 week 2020 | 651 nV | 71 nV    |
| LTZ1000ACH chip 3       | 39 week 2020 | 881 nV | 78 nV    |
| LTZ1000ACH chip 4       | 39 week 2020 | 1044 nV | 98 nV   |
| LTZ1000ACH chip 5       | 39 week 2020 | 796 nV | 107 nV   |
| LTZ1000ACH chip 6       | 39 week 2020 | 936 nV | 125 nV   |
| LTZ1000ACH chip 7       | 37 week 2020 | 763 nV | 97 nV    |
| LTZ1000ACH chip 8       | 37 week 2020 | 804 nV | 67 nV    |
| LTZ1000ACH chip 9       | 37 week 2020 | 874 nV | 89 nV    |
| LTZ1000ACH chip 10      | 39 week 2020 | 818 nV | 99 nV   |
| LTZ1000ACH chip 11      | 39 week 2020 | 847 nV | 74 nV   |
| LTZ1000ACH chip 12      | 39 week 2020 | 836 nV | 86 nV   |
| LTZ1000ACH chip 13      | 39 week 2020 | 754 nV | 80 nV   |
| LTZ1000ACH chip 14      | 39 week 2020 | 725 nV | 76 nV   |
| LTZ1000ACH chip 15      | 39 week 2020 | 732 nV | 57 nV   |
| LTZ1000ACH chip 16      | 39 week 2020 | 821 nV | 79 nV   |
| LTZ1000ACH chip 17      | 48 week 2019 | 753 nV | 60 nV   |
| LTZ1000ACH chip 18      | 39 week 2020 | 834 nV | 78 nV   |
| LTZ1000ACH chip 19      | 48 week 2019 | 825 nV | 77 nV   |
| LTZ1000ACH chip 20      | 39 week 2020 | 939 nV | 62 nV   |
| LTZ1000ACH chip 21      | 39 week 2020 | 724 nV | 81 nV   |
| LTZ1000ACH chip 22      | 39 week 2020 | 913 nV | 120 nV  |
| LTZ1000ACH chip 23      | 39 week 2020 | 935 nV | 98 nV   |
| LTZ1000ACH chip 24      | 39 week 2020 | 959 nV | 140 nV  |
| LTZ1000ACH chip 25      | 39 week 2020 | 837 nV | 95 nV   |
| LTZ1000ACH chip 26      | 39 week 2020 | 867 nV | 112 nV  |
| LTZ1000ACH chip 27      | 39 week 2020 | 1102 nV|119 nV |
| LTZ1000ACH chip 28      | 39 week 2020 | 1242 nV|23 nV  |
| LTZ1000ACH chip 29      | 39 week 2020 | 782 nV|107 nV  |
| LTZ1000ACH chip 30      | 39 week 2020 | 1023 nV|108 nV |
| LTZ1000ACH chip 31      | 39 week 2020 | 842 nV|56 nV   |
| LTZ1000ACH chip 32      | 39 week 2020 | 816 nV|89 nV|
| LTZ1000CH chip 1        | 28 week 1986 | 987 nV|209 nV        |
| LTZ1000CH chip 2        | 48 week 2019 | 864 nV|82 nV         |
| LTZ1000CH chip 3        | 48 week 2019 | 801 nV|191 nV        |
| LTZ1000CH chip 4        | 15 week 1990 | 1428 nV|226 nV       |
| LTZ1000CH chip 5        | 15 week 1990 | 978 nV|187 nV        |
| QVR #2 , 4 x LTZ1000ACH | 30 week 2019 | 442 nV|44 nV |
| Fluke 5720A, 7.19VDC    |  N/A         | 3790 nV|512 nV |
| Setup BN floor          |  N/A         | 102 nV|9 nV |

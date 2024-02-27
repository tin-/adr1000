# Noise measurement in low frequency 0.1 Hz - 10 Hz bandwidth 
---

Total number of devices evaluated in this test:

* 56 pcs ADR1000AHZ production devices, manufactured with date code 39 week 2018, 7,9 week 2022 and 33 week 2023
* 34 pcs LTZ1000CH production devices, manufactured from 1986 to 2021
* 35 pcs LTZ1000ACH#PBF production devices, manufactured in the end of 2019, 2020 and 2022.
* Two Fluke 5720A multi-function calibrators with output 7.19 VDC configured on 11V DC Voltage range
* Wavetek 4808 multi-function calibrator
* Commercial Fluke 732C DC voltage standard (battery-operated)
* HP 3245A Universal source with LTZ1000A-based reference
* xDevs.com QVR device with four LTZ1000ACH averaged with passive resistor network

Noise floor of the measurement setup and shorted LNA input measured at **102 nV** with standard deviation **9 nV**. Setup utilize Tektronix DPO7104C real-time oscilloscope and battery-powered AC-coupled LNA with gain +80 dB and pass-band 0.1-10 Hz. All zener chips were evaluated with bipolar Fluke 792A battery power supply to avoid any electrical interference from power line or ground loops. 

![Low frequency noise measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/lf_noise_setup_blk.png)

Zener current on test FX module PCB was set to 5.0 mA for ADR1000 and about 3.6 mA for LTZ1000. This was achieved by populated (120 &Omega; = LTZ, 80 &Omega; = ADR) high stability resistor from zener chip anode diode pin 4 and reference return point pin 7. 

![Shielding can with zener board](https://xdevs.com/doc/xDevs.com/AFX/nstest_rig_1.jpg)

Chips were installed in a socket populated on [xDevs.com FX reference module](https://xdevs.com/article/792x) replicating LTZ1000A recommended circuit from datasheet. Raw 6.62/7.x V output signal routed directly to LNA input via shielded coaxial cable. Each chip was powered up for 30 minutes to reach stable oven operating point and settled voltage across LNA input DC block capacitor. Whole module shielded in a metal can to reduce ambient noise interference during the measurement time. 

![![Preview](https://xdevs.com/doc/xDevs.com/AFX/adr_noise_testa_1.png)](https://xdevs.com/doc/xDevs.com/AFX/adr_noise_testa.png)

Based on this instrumentation following results were obtained:

## ADR1000AHZ chips - 56 pcs

* Lowest noise was measured for chip 2, **441 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 53, **580 nV peak to peak**
* Difference between chip 2 and chip 53 is **139 nV peak to peak**
* Average noise across all 56 chips is **491 nV peak to peak**
* Median noise across all 56 chips is **481 nV peak to peak**

## LTZ1000ACH#PBF chips - 35 pcs

* Lowest noise was measured for chip 2, **651 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 34, **1399 nV peak to peak**
* Difference between chip 2 and chip 34 is **748 nV peak to peak**
* Average noise across all 35 chips is **883 nV peak to peak**
* Median noise across all 35 chips is **837 nV peak to peak**
* Median standard deviation across all 35 chips is **80 nV peak to peak**

## LTZ1000CH chips - 34 pcs

* Lowest noise was measured for chip 12, **678 nV peak to peak in 0.1 Hz - 10 Hz bandwidth**
* Highest noise was measured for chip 32, **1611 nV peak to peak**
* Difference between chip 12 and chip 32 is **933 nV peak to peak**
* Average noise across all 34 chips is **949 nV peak to peak**
* Median noise across all 34 chips is **897 nV peak to peak**
* Median standard deviation across all 34 chips is **91 nV peak to peak**

## Other noise values and devices for reference

* LTZ1000A datasheet specification, 1200 nV typical, 2000 nV peak to peak maximum with Iz = 5mA, 0.1 Hz - 10 Hz and Q1 current 100 &micro;A.
* ADR1000 datasheet specification, 900 nV typical peak to peak, no maximum specification, with Iz = 5mA, 0.1 Hz - 10 Hz and Q1 current 100 &micro;A.
* xDevs.com QVR module with averaged output by 4 x LTZ1000ACH chip, 7.16 V output : **442 nV peak to peak, &sigma; = 44 nV**
* xDevs.com QVR module with averaged output by 2 x ADR1000 chip, 10 V output : **670 nV peak to peak, &sigma; = 62 nV**
* Fluke 732C DC voltage standard @ 10 V output : **903 nV peak to peak, &sigma; = 84 nV**
* Fluke 5720A multi-function H1 calibrator configured @ 7.19 V output measured noise : **3790 nV peak to peak, &sigma; = 512 nV**
* Fluke 5720A multi-function H2 calibrator configured @ 7.19 V output measured noise : **3704 nV peak to peak, &sigma; = 480 nV**
* Wavetek 4808 multi-function calibrator configured @ 7.19 V output measured noise : **2995 nV peak to peak, &sigma; = 188 nV**
* Wavetek 4808 multi-function calibrator configured @ 10 V output measured noise : **2611 nV peak to peak, &sigma; = 233 nV**
* HP 3245A universal source with LTZ1000A KX module reference configured @ 7.19 V DC output measured noise : **54.4 &micro;V peak to peak, &sigma; = 5.1 &micro;V**

![Noise chart summary](https://xdevs.com/doc/xDevs.com/QVRA/lf_noise_chart_blk.png)

Vertical axis represents measured noise voltage and horizontal axis represent sample number. Blue round markers represent ADR1000 chips, triangles LTZ1000ACH and diamonds LTZ1000CH. Dashed line outline test setup noise floor limit.

Based on these values on average new Analog Devices ADR1000AHZ device measured to have 55.4% less noise than older Linear Technology LTZ1000ACH IC. This conclusion also supported by matching noise performance of single ADR1000AHZ compared to combined averaged noise from array of four selected LTZ1000A at a fraction of the BOM cost and power consumption. New reference IC can be very helpful for applications where low frequency noise is a critical performance parameter.

Data set table with all measurement values is also presented below for further analysis. 

| Device                       | Datecode     | Measured noise peak-to-peak, 0.1-10 Hz | Standard deviation, 1 &sigma;|
| :------------                | :----------: | :------------------------------------: | :--------------------------: |
| ADR1000AHZ chip 1            | 39 week 2018 | 442 nV                                 | 34 nV                        |
| ADR1000AHZ chip 2            | 39 week 2018 | 441 nV                                 | 48 nV                        |
| ADR1000AHZ chip 3            | 39 week 2018 | 460 nV                                 | 46 nV                        |
| ADR1000AHZ chip 4            | 39 week 2018 | 458 nV                                 | 44 nV                        |
| ADR1000AHZ chip 5            | 39 week 2018 | 473 nV                                 | 40 nV                        |
| ADR1000AHZ chip 6            | 39 week 2018 | 469 nV                                 | 42 nV                        |
| ADR1000AHZ chip 7            | 39 week 2018 | 477 nV                                 | 50 nV                        |
| ADR1000AHZ chip 8            | 39 week 2018 | 479 nV                                 | 51 nV                        |
| ADR1000AHZ chip 9            | 39 week 2018 | 452 nV                                 | 55 nV                        |
| ADR1000AHZ chip 10           | 39 week 2018 | 499 nV                                 | 44 nV                        |
| ADR1000AHZ chip 11           | 39 week 2018 | 446 nV                                 | 68 nV                        |
| ADR1000AHZ chip 12           | 39 week 2018 | 471 nV                                 | 43 nV                        |
| ADR1000AHZ chip 13           | 39 week 2018 | 473 nV                                 | 50 nV                        |
| ADR1000AHZ chip 14           | 39 week 2018 | 461 nV                                 | 40 nV                        |
| ADR1000AHZ chip 15           | 39 week 2018 | 446 nV                                 | 40 nV                        |
| ADR1000AHZ chip 16           | 39 week 2018 | 461 nV                                 | 47 nV                        |
| ADR1000AHZ chip 17           | 39 week 2018 | 451 nV                                 | 39 nV                        |
| ADR1000AHZ chip 18           | 39 week 2018 | 520 nV                                 | 48 nV                        |
| ADR1000AHZ chip 19           | 39 week 2018 | 465 nV                                 | 41 nV                        |
| ADR1000AHZ chip 20           | 39 week 2018 | 511 nV                                 | 107 nV                       |
| ADR1000AHZ chip 21           | 39 week 2018 | 487 nV                                 | 47 nV                        |
| ADR1000AHZ chip 22           | 39 week 2018 | 571 nV                                 | 51 nV                        |
| ADR1000AHZ chip 23           | 39 week 2018 | 479 nV                                 | 53 nV                        |
| ADR1000AHZ chip 24           | 39 week 2018 | 462 nV                                 | 48 nV                        |
| ADR1000AHZ chip 25           | 39 week 2018 | 547 nV                                 | 52 nV                        |
| ADR1000AHZ chip 26           | 39 week 2018 | 472 nV                                 | 48 nV                        |
| ADR1000AHZ chip 27           | 39 week 2018 | 493 nV                                 | 46 nV                        |
| ADR1000AHZ chip 28           | 39 week 2018 | 481 nV                                 | 62 nV                        |
| ADR1000AHZ chip 29           | 39 week 2018 | 527 nV                                 | 53 nV                        |
| ADR1000AHZ chip 30           | 39 week 2018 | 499 nV                                 | 78 nV                        |
| ADR1000AHZ chip 31           | 39 week 2018 | 475 nV                                 | 49 nV                        |
| ADR1000AHZ chip 32           | 39 week 2018 | 470 nV                                 | 42 nV                        |
| ADR1000AHZ chip 33           | 39 week 2018 | 491 nV                                 | 47 nV                        |
| ADR1000AHZ chip 34           | 39 week 2018 | 462 nV                                 | 48 nV                        |
| ADR1000AHZ chip 35           | 39 week 2018 | 509 nV                                 | 54 nV                        |
| ADR1000AHZ chip 36           | 39 week 2018 | 503 nV                                 | 43 nV                        |
| ADR1000AHZ chip 37           | 39 week 2018 | 464 nV                                 | 44 nV                        |
| ADR1000AHZ chip 38           | 39 week 2018 | 506 nV                                 | 24 nV                        |
| ADR1000AHZ chip 39           | 39 week 2018 | 531 nV                                 | 38 nV                        |
| ADR1000AHZ chip 40           | 39 week 2018 | 462 nV                                 | 48 nV                        |
| ADR1000AHZ chip 41           | 39 week 2018 | 503 nV                                 | 81 nV                        |
| ADR1000AHZ chip 42           | 39 week 2018 | 480 nV                                 | 36 nV                        |
| ADR1000AHZ chip 43           | 39 week 2018 | 534 nV                                 | 130 nV                       |
| ADR1000AHZ chip 44           | 39 week 2018 | 556 nV                                 | 59 nV                        |
| ADR1000AHZ chip 45           | 39 week 2018 | 464 nV                                 | 44 nV                        |
| ADR1000AHZ chip 46           | 39 week 2018 | 503 nV                                 | 43 nV                        |
| ADR1000AHZ chip 47           | 39 week 2018 | 509 nV                                 | 47 nV                        |
| ADR1000AHZ chip 48           | 39 week 2018 | 506 nV                                 | 38 nV                        |
| ADR1000AHZ chip 49           | 39 week 2018 | 531 nV                                 | 52 nV                        |
| ADR1000AHZ chip 50           | 7 week 2022  | 522 nV                                 | 42 nV                        |
| ADR1000AHZ chip 51           | 7 week 2022  | 533 nV                                 | 22 nV                        |
| ADR1000AHZ chip 52           | 9 week 2022  | 446 nV                                 | 32 nV                        |
| ADR1000AHZ chip 53           | 9 week 2022  | 580 nV                                 | 40 nV                        |
| ADR1000AHZ chip 54           | 9 week 2022  | 538 nV                                 | 73 nV                        |
| ADR1000AHZ chip 55           | 9 week 2022  | 522 nV                                 | 42 nV                        |
| ADR1000AHZ chip 56           | 33 week 2023 | 514 nV                                 | 35 nV                        |
| LTZ1000ACH chip 1            | 37 week 2020 | 776 nV                                 | 72 nV                        |
| LTZ1000ACH chip 2            | 39 week 2020 | 651 nV                                 | 71 nV                        |
| LTZ1000ACH chip 3            | 39 week 2020 | 881 nV                                 | 78 nV                        |
| LTZ1000ACH chip 4            | 39 week 2020 | 1044 nV                                | 98 nV                        |
| LTZ1000ACH chip 5            | 39 week 2020 | 796 nV                                 | 107 nV                       |
| LTZ1000ACH chip 6            | 39 week 2020 | 936 nV                                 | 125 nV                       |
| LTZ1000ACH chip 7            | 37 week 2020 | 763 nV                                 | 97 nV                        |
| LTZ1000ACH chip 8            | 37 week 2020 | 804 nV                                 | 67 nV                        |
| LTZ1000ACH chip 9            | 37 week 2020 | 874 nV                                 | 89 nV                        |
| LTZ1000ACH chip 10           | 39 week 2020 | 818 nV                                 | 99 nV                        |
| LTZ1000ACH chip 11           | 39 week 2020 | 847 nV                                 | 74 nV                        |
| LTZ1000ACH chip 12           | 39 week 2020 | 836 nV                                 | 86 nV                        |
| LTZ1000ACH chip 13           | 39 week 2020 | 754 nV                                 | 80 nV                        |
| LTZ1000ACH chip 14           | 39 week 2020 | 725 nV                                 | 76 nV                        |
| LTZ1000ACH chip 15           | 39 week 2020 | 732 nV                                 | 57 nV                        |
| LTZ1000ACH chip 16           | 39 week 2020 | 821 nV                                 | 79 nV                        |
| LTZ1000ACH chip 17           | 48 week 2019 | 753 nV                                 | 60 nV                        |
| LTZ1000ACH chip 18           | 39 week 2020 | 834 nV                                 | 78 nV                        |
| LTZ1000ACH chip 19           | 48 week 2019 | 825 nV                                 | 77 nV                        |
| LTZ1000ACH chip 20           | 39 week 2020 | 939 nV                                 | 62 nV                        |
| LTZ1000ACH chip 21           | 39 week 2020 | 724 nV                                 | 81 nV                        |
| LTZ1000ACH chip 22           | 39 week 2020 | 913 nV                                 | 120 nV                       |
| LTZ1000ACH chip 23           | 39 week 2020 | 935 nV                                 | 98 nV                        |
| LTZ1000ACH chip 24           | 39 week 2020 | 959 nV                                 | 140 nV                       |
| LTZ1000ACH chip 25           | 39 week 2020 | 837 nV                                 | 95 nV                        |
| LTZ1000ACH chip 26           | 39 week 2020 | 867 nV                                 | 112 nV                       |
| LTZ1000ACH chip 27           | 39 week 2020 | 1102 nV                                | 119 nV                       |
| LTZ1000ACH chip 28           | 39 week 2020 | 1242 nV                                | 23 nV                        |
| LTZ1000ACH chip 29           | 39 week 2020 | 782 nV                                 | 107 nV                       |
| LTZ1000ACH chip 30           | 39 week 2020 | 1023 nV                                | 108 nV                       |
| LTZ1000ACH chip 31           | 39 week 2020 | 842 nV                                 | 56 nV                        |
| LTZ1000ACH chip 32           | 39 week 2020 | 816 nV                                 | 89 nV                        |
| LTZ1000ACH chip 33           | 9 week 2022  | 1033 nV                                | 63 nV                        |
| LTZ1000ACH chip 34           | 34 week 2022 | 1399 nV                                | 46 nV                        |
| LTZ1000ACH chip 35           | 34 week 2022 | 1032 nV                                | 139 nV                       |
| LTZ1000CH chip 1             | 48 week 2019 | 848 nV                                 | 68  nV                       |
| LTZ1000CH chip 2             | 48 week 2019 | 947 nV                                 | 128 nV                       |
| LTZ1000CH chip 3             | 48 week 2019 | 984 nV                                 | 94  nV                       |
| LTZ1000CH chip 4             | 48 week 2019 | 805 nV                                 | 122 nV                       |
| LTZ1000CH chip 5             | 28 week 2021 | 952 nV                                 | 91  nV                       |
| LTZ1000CH chip 6             | 28 week 2021 | 887 nV                                 | 100 nV                       |
| LTZ1000CH chip 7             | 28 week 2021 | 763 nV                                 | 48  nV                       |
| LTZ1000CH chip 8             | 28 week 2021 | 754 nV                                 | 88  nV                       |
| LTZ1000CH chip 9             | 28 week 2021 | 946 nV                                 | 126 nV                       |
| LTZ1000CH chip 10            | 28 week 2021 | 891 nV                                 | 98  nV                       |
| LTZ1000CH chip 11            | 28 week 2021 | 887 nV                                 | 77  nV                       |
| LTZ1000CH chip 12            | 28 week 2021 | 678 nV                                 | 46  nV                       |
| LTZ1000CH chip 13            | 28 week 2021 | 944 nV                                 | 47  nV                       |
| LTZ1000CH chip 14            | 28 week 2021 | 930 nV                                 | 102 nV                       |
| LTZ1000CH chip 15            | 28 week 2021 | 830 nV                                 | 76  nV                       |
| LTZ1000CH chip 16            | 28 week 2021 | 874 nV                                 | 38  nV                       |
| LTZ1000CH chip 17            | 28 week 2021 | 950 nV                                 | 100 nV                       |
| LTZ1000CH chip 18            | 28 week 2021 | 749 nV                                 | 86  nV                       |
| LTZ1000CH chip 19            | 28 week 2021 | 934 nV                                 | 102 nV                       |
| LTZ1000CH chip 20            | 28 week 2021 | 836 nV                                 | 88  nV                       |
| LTZ1000CH chip 21            | 28 week 2021 | 768 nV                                 | 85  nV                       |
| LTZ1000CH chip 22            | 28 week 2021 | 1337 nV                                | 327 nV                       |
| LTZ1000CH chip 23            | 28 week 2021 | 784 nV                                 | 53  nV                       |
| LTZ1000CH chip 24            | 40 week 2019 | 770 nV                                 | 108 nV                       |
| LTZ1000CH chip 25            | 40 week 2019 | 681 nV                                 | 64  nV                       |
| LTZ1000CH chip 26            | 15 week 1990 | 1549 nV                                | 123 nV                       |
| LTZ1000CH chip 27            | 28 week 1986 | 1286 nV                                | 91  nV                       |
| LTZ1000CH chip 28            | 16 week 1987 | 927 nV                                 | 92  nV                       |
| LTZ1000CH chip 29            | 15 week 1990 | 1192 nV                                | 132 nV                       |
| LTZ1000CH chip 30            | 15 week 1990 | 904 nV                                 | 73  nV                       |
| LTZ1000CH chip 31            | 15 week 1990 | 1317 nV                                | 86  nV                       |
| LTZ1000CH chip 32            | 30 week 1988 | 1611 nV                                | 224 nV                       |
| LTZ1000CH chip 33            | 49 week 2016 | 966 nV                                 | 141 nV                       |
| LTZ1000CH chip 34            | 49 week 2016 | 804 nV                                 | 75  nV                       |
| QVR, 4 x LTZ1000ACH @ 6.62 V | 30 week 2019 | 442 nV                                 | 44 nV                        |
| QVR, 4 x ADR1000AHZ @ 6.62 V | 39 week 2018 | 242 nV                                 | 40 nV                        |
| QVR, 2 x ADR1000AHZ @ 6.62 V | 39 week 2018 | 378 nV                                 | 37 nV                        |
| Fluke 732C @ 10 V            |  N/A         | 903 nV                                 | 84 nV                        |
| Fluke 5720A/H1, @ 7.19 V     |  N/A         | 3790 nV                                | 512 nV                       |
| Fluke 5720A/H2, @ 7.19 V     |  N/A         | 3704 nV                                | 480 nV                       |
| Wavetek 4808 @ 7.19 V        |  N/A         | 2995 nV                                | 188 nV                       |
| Wavetek 4808 @ 10 V          |  N/A         | 2611 nV                                | 233 nV                       |
| HP3245A @ 7.19 V             |  N/A         | 54400 nV                               | 5100 nV                      |
| Setup BN floor               |  N/A         | 102 nV                                 | 9 nV                         |

## ADR1000 Noise performance relative to zener current setpoint

To investigate ADR1000's relationship between output 6.6V noise to zener current additional test setup was utilized with various paralleled resistances added to nominal 120 &Omega; current setting resistor. For this socketed xDevs.com FX module was utilized. Zener operated at +65 &deg;C with 70 k&Omega; bias resistors. Operational amplifier LT1013 was utilized in both oven and voltage control loops. Results provided in charts presented below:

![Measured noise relationship to zener current setpoint](https://github.com/tin-/adr1000/blob/main/noise/adr1000_en_vs_iz.png?raw=true)

Overall sweet spot for lower noise operation is around 60-80 &Omega; which corresponds to zener current around 6-8 mA and output zener noise measured around 390-440 nV peak to peak in 0.1 Hz to 10 Hz bandwidth. Driving ADR1000 with high current over 10 mA provide only marginal improvement.

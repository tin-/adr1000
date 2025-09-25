# Mid-term drift measurement on mixed zener module (multiple months)
---

Total number of devices evaluated in secondary medium-term drift test shown in list below. All chips are populated on same PCBA and powered by same regulator. They are monitored by same zener array and automated method used for long-term measurement.

* 1 x ADR1000AHZ manufactured with date code 39 week 2018
* 1 x ADR1000AHZ manufactured with date code 33 week 2023
* 1 x LTZ1000ACH manufactured with date code 34 week 2022
* 1 x LTZ1000CH manufactured with date code 28 week 2021

![Long-term drift measurement setup](https://xdevs.com/doc/xDevs.com/QVRA/ltd_setup_chart_bk.png)

Chips were soldered on [xDevs.com QVR reference module](https://xdevs.com/article/qvref) replicating ADR1000/LTZ1000A circuit from datasheet. Raw 6.62/7.x V output signal routed to the output or to the bipolar output gain stage on PCB using kelvin connection. Each unit is assembled and enclosed in metal enclosure for shielding and protection purposes. PCBA is mounted with flexible padding to avoid transfer of mechanical stress of vibration from the exterior instrumentation and environment. 

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
|Noise, 0.1 Hz - 10 Hz | 895 nV pk-pk | 957 nV pk-pk | 367 nV pk-pk | 410 nV pk-pk |
|Calculated temperature| +50 &deg;C | +55 &deg;C | +65 &deg;C | +75 &deg;C |
|Compensation resistor | 150 k&Omega; | 820 k&Omega; | 500 k&Omega; | 820 k&Omega; |
|Measured final &alpha;| -0.0203 &micro;V/V/&deg;C |+0.0067 &micro;V/V/&deg;C |-0.052 &micro;V/V/&deg;C |-0.0166 &micro;V/V/&deg;C |
|Measured final &beta; | +0.0014 &micro;V/V/&deg;C |+0.0010 &micro;V/V/&deg;C |+0.0035 &micro;V/V/&deg;C |+0.0004 &micro;V/V/&deg;C |
|Measured ZTC temp, &deg;C | +30.1 &deg;C | +19.5 &deg;C | +30.6 &deg;C | +42.7 &deg;C |
|[Output voltage, FEB.13.2024](https://xdevs.com/hp3458abc_k2002ltc_ltdqvr_qvrq_raw6v6fix_avg_tcr_40c_820kABD_trimmed10v_run_feb2024/) | 7.17232133 V | 7.09003609 V | 6.60987871 V | 6.62218042 V |

![LTD Board photo](https://xdevs.com/doc/xDevs.com/QVRL/img/ltdqvr_top_1.jpg)

Averaging of zener outputs is also unused (Z6 network is not populated), as only individual zener IC outputs will be monitored from this module. 

![Setup with LTD QVR build](https://xdevs.com/doc/xDevs.com/QVRL/img/ltdqvr_resn_1.jpg)

## March 2024 data : 700 hours 

![March results](https://xdevs.com/doc/xDevs.com/QVRL/cal/ltd_qvr_mar2024_1.png)

After running reference powered up for total 700 hours (first 140.5 hours are omitted from plot, "zero" reference taken on 19 February, 2024) drift difference between different chips is quite noticeable.

Both LTZ1000CH and LTZ1000ACH demonstrate clear absence of any significant drift, which underline excellent performance of LTZ design once again. All we can see on LTZ outputs is just residual temperature coefficient play and random noise walk up and down. Worst outlier points for these chips staying within &plusmn;0.4 &micro;V/V from initial point on 19 February, 2024. 

ADR1000 chips however are not so stable and have significant drift. Newer 33 week 2023 chip which is running at +65 &deg;C oven setpoint demonstrated upward +2.0 &micro;V/V drift in first 8 days from zero point and then somewhat stabilized with walk around &plusmn;0.3 &micro;V/V. Older 2018 week 39 chip running at hotter +75 &deg;C (as datasheet recommends to us) and demonstrate opposite drift of -4.2 &micro;V/V and still going. There is no visible stabilization time for this chip, just like with other 1839 chips from older module we explored in long-term drift study page.

Based on this time frame conclusion is:

1. LTZ1000-based solutions already able to stabilize in time period less than 140 hours after assembly.
2. New year 2023 week 33 ADR1000 chip shows promising stabilization time, more into future will determine if this statement holds.
3. Old year 2018 week 39 ADR1000 chip does not stabilize in 700 hours timeframe after assembly.

## April 2024 data : 1000 hours 

![April beginning](https://xdevs.com/doc/xDevs.com/QVRL/cal/ltd_qvr_mar2024_3d.png)

This time I've added some processing to cancel out systematic short-term errors from the measurement setup equipment in the zener array. This resulted in much nicer data set without much of noisy jumps due to temperature changes in the room. Overall behaviour of the references remained the same. LTZ-based cells wiggle very close to 0.0 &micro;V/V level, essentially staying stable since first 141 hours. ADR that runs at higher temperature continued it's down-ward drift, while ADR1000 at +65 &deg;C also started to drift down after spending a week at +2.2 &micro;V/V level.

### June 2024 data : 3120 hours

![June data](https://xdevs.com/doc/xDevs.com/QVRL/cal/ltd_qvr_3120hrs.png)

To stir things up a little bit the board was powered off on June 22, 2024 3:00pm and baked in the convection oven at around +115 &deg;C for 8 hours. Reference module was unpowered during whole baking duration.

### September 2024 data : 4440 hours

Here's zoomed in close data samples collected until October 2024, showcasing close look at behaviour after baking of assembled unpowered board for 8 hours.

![](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/bake_zoom.png)

Behaviour difference between LTZ1000,LTZ1000A cells and ADR1000 is clearly visible. New ADR1000 require about a month of time to resetlle in new operation "condition". We can also make a positive observation on performance of ADR1000 @ +75°C, which reached stable operation 3 month since baking. ADR1000 at lower temperature still drift down on this timescale. Both LTZ1000 cells demonstrate more or less stable linear drift.

###  July 2025 data : 12696 hours, 529 days

![July 2025 data](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/ltdqvr_2025_jul27.png)

This char presents all samples acquired after running this module since 8 hours baking unpowered board on June 22, 2024. Baking process caused a large shift for both ADR1000 and LTZ1000CH cells and smaller shift for LTZ1000ACH cell. This was quite fruitful test, revealing that baked ADR1000 running at +75 °C oven temperature now reached stable condition after only 2 months. ADR1000 cell running at +65 °C took much longer 6 month after baking to settle at steady rate. I was out on vacation during December holidays and forgot to close the window to the lab, causing a dip in ambient temperature below +18 °C. This caused visible jump for LTZ reference cells and no impact on ADR1000 +75.

Beginning of July 2025 I've replaced Keithley 2182A nanovoltmeter to HP 34420A in the zener bank array (that was used to measure these samples too). And since this board outputs just raw zener voltages at 7.x and 6.6x V gain difference of nanovoltmeter caused the clearly visible shift of datasamples. But stability behaviour remained quite similar to data from 2182A. 

### September 2025 data : 14160 : 590 days

![Sep 2025](https://xdevs.com/doc/xDevs.com/CalFest_2025/dcv/ltdqvr_2025_sep24.png)

Updated data after relocation of the lab 600km away and repower. This mixed zener LTD-QVR module was unpowered during the shipment transit.

## Other notable references

* [Forum page about ADR1000-based references](https://www.eevblog.com/forum/metrology/lowest-drift-lowest-noise-voltage-reference/) - branadic and Andreas also demonstrated long-term drift by ADR1000 with similar behavior, despite completely different instrumentation approach.

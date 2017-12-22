---
layout: default
---
# Shopping List
- WS281X LED Strip
- Power Supply (5V DC, #LED * 60mA)
-- 150 LEDs -> 150 * 60mA = 9000mA
- Power Adapter fittin Power Supply
- Raspberry Pi Zero with Raspbian
- Ikea Riba 50x50

# Setup Raspberry
- install [WS281X library](https://github.com/jgarff/rpi_ws281x)
```
sudo apt-get install build-essential python-dev unzip wget scons swig
```
```
wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && sudo scons && cd python && sudo python setup.py install
```

# Connect Raspberry And LED Strip (First Try)

- connect pi and strip
![](assets\images\pi_led_connect_test1.png)
- navigate to checked out WS281X library
```
#change variable LED_COUNT to actual led count of strip
nano python/examples/strandtest.py
```
```
python python/examples/strandtest.py
```
![](assets\images\pi_led_connect_test2.jpg)

# Build Clock
- cut strip into 11 strips with 10 leds
- place it in ribba
- solder strip back toggether
![](assets\images\led_wired.jpg)
- connect with raspberry pi
![](assets\images\pi_connected.jpg)
![](assets\images\pi_gpio.jpg)
- build grid for LEDs so they don't interfere with each other
 - 
```
#height 2.5cm
#width 9cm
|<-- 2cm -->|<-- 2cm -->|<-- 2cm -->|<-- 2cm -->|<- 1cm ->|
```
![](assets\images\led_grid.jpg)
- create letter stencil for glass
  - used black cardboard and excreted the letters based on the layout by [bk1285](https://github.com/bk1285/rpi_wordclock/tree/master/wordclock_layouts) 
![](assets\images\letter_stencil.jpg)
- put white paper on back of stencil to dim the leds 
- put everything together
- connect and test with python strandtest

# Software
## States (German)

- Es ist 
- X Uhr
- Fünf nach X
- Zehn nach X
- Viertel nach X
- Zwanzig nach X
- Fünf vor Halb X
- Halb X
- Fünf nach Halb X
- Zwanzig vor X
- Viertel vor X
- Zehn vor X
- Fünf vor X

## LED-ID Grid
```
9 10 29 30 49 50 69 70 89 90 109
8 11 28 31 48 51 68 71 88 91 108
7 12 27 32 47 52 67 72 87 92 107
6 13 26 33 46 53 66 73 86 93 106
5 14 25 34 45 54 65 74 85 94 105
4 15 24 35 44 55 64 75 84 95 104
3 16 23 36 43 56 63 76 83 96 103
2 17 22 37 42 57 62 77 82 97 102
1 18 21 38 41 58 61 78 81 98 101
0 19 20 39 40 59 60 79 80 99 100 
```

## Code
Python script can be found [here](https://github.com/thomcz/word-clock/blob/master/python/wordclock.py)

# References
- https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/
- http://dordnung.de/raspberrypi-ledstrip/ws2812
- https://github.com/bk1285/rpi_wordclock

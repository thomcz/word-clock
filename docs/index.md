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
now fun part begins!! 


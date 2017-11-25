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
- (TODO Image)
- navigate to checked out WS281X library
```
#change variable LED_COUNT to actual led count of strip
nano python/examples/strandtest.py
```
```
python python/examples/strandtest.py
```

# Build Clock
- cut strip
- place it in ribba
- TODO image
- solder strip back toggether
- TODO image
- connect with raspberry pi
- build grid for LEDs
- create letter stencil for glass

# Software
# Development Notes #

- configured rpi to boot into X and auto login
	- used the wiki to set this up
- configured rpi to auto login to wifi
	- used a adafruit tutorial for this
- ip address is 10.0.1.23
- ssh is working
- looking at inotool.org for arduino compilation from the command line
- [ ] screen is installed, how does that work again?
- needed to install python-dev fro inotool
- someone in a stackexchange gui said inotool is not supported any more
	- [ ] that you can use the official arduino ide now from the command line
	- https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc
- ** RAN OUT OF SPACE! **
- blasting away NOOBS and re-installing 2016-05-27-raspbian-jessie-lite.img
	- the lite version seems to not include X, which might be good if we can program without it
		- went with the lite version, it's going to run headless anyways
- had to change the keyboard type to USA to get a "#" working in the network files
- doing the wifi config like [1] didn't work i had to do it like [2] editing /etc/wpa-supplicant/wpa_supplicant.conf
	- [1] https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis
	- [2] https://www.raspberrypi.org/forums/viewtopic.php?t=44044
- ran an apt-get update and upgrade
- set the timezone
- ran sudo apt-get install arduino
	- needs 100MB of packages, quite a lot, but that's what you get when you start with lite!
- browsing around there are a couple links from the forums for web guis
	- https://github.com/dddomodossola/remi
		- really looks like exactly what i want, write python, get a web gui for free!
		- i installed this on the dell laptop and it works great, just what i'm looking for, really.
	- http://webiopi.trouch.com/
		- an IOT manager type thing, does more than i want
- have to install python-dev on the rpi to get pip!
- https://www.raspberrypi.org/documentation/remote-access/vnc/
- [x] probably need to install screen again
- tried to install the fast led library via arduino command line and got X errors
	- look in the bugs area and see it needs a dummy x server
		- https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc
	- followed those instructions and it doesnt work. silly hack
	- trying platformio
- installing vim
- [ ] task at startup / shutdown
	- https://www.raspberrypi.org/forums/viewtopic.php?t=33250&p=415144
- needed to install apt-get install python-setuptools
- then sudo easy_install pip
- then pip install platformio
- [X] install bonjour
	- http://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/
	- runnign by default, we are on at raspberrypi.local
- [ ] https://thepihut.com/blogs/raspberry-pi-tutorials/19668676-renaming-your-raspberry-pi-the-hostname
- pio lib search FastLED
		[ 126 ] FastLED          arduino, atmelavr, atmelsam, freescalekinetis, nordicnrf51, nxplpc, ststm32, teensy "Daniel Garcia, Mark Kriegsman": FastLED is a library for programming addressable rgb led strips (APA102/Dotstar, WS2812/Neopixel, LPD8806, and a dozen others) acting both as a driver and as a library for color management and fast math.
- [ ] serial and fastLED issues
	- https://github.com/FastLED/FastLED/wiki/Interrupt-problems
- [ ] read LED data directly from serial (Read RGB Data From Serial)
	- https://github.com/FastLED/FastLED/wiki/Controlling-leds
- [ ] search github for includes of fastled and neopixel
- [ ] "Hereby an example implementation to control FastLED with 11 byte commands"
	- https://plus.google.com/+KasperKamperman/posts/gsY84zrSc2f
- Homekit on rpi
	- http://www.instructables.com/id/Raspberry-Pi-2-Homekit-from-zero-to-Hey-Siri/?ALLSTEPS
	- https://github.com/nfarina/homebridge/blob/master/README.md
- need to run 
	- sudo npm install -g homebridge
	- need
		- sudo apt-get install npm first
			- this worked
	- installing homebridge didn't
		- 
npm WARN engine homebridge@0.3.4: wanted: {"node":">=0.12.0"} (current: {"node":"0.10.29","npm":"1.4.21"})

- following
	- https://www.raspberrypi.org/forums/viewtopic.php?f=34&t=140747
		pi@raspberrypi:~ $  node -v
		v0.10.29
		pi@raspberrypi:~ $  sudo su -
		root@raspberrypi:~ # apt-get remove --purge node* npm*
		root@raspberrypi:~ # curl -sL https://deb.nodesource.com/setup_5.x | sudo bash -
		root@raspberrypi:~# apt-get install nodejs -y
		root@raspberrypi:~# node -v
		v5.11.0
		root@raspberrypi:~# npm -v
		3.8.6		
	- nope that didn't work cause we aren't on pi3
	- going back to instructables instructions
		- note that instructables uses a different server for the homekit stuff
			- https://github.com/KhaosT/HAP-NodeJS
			- vs
			- https://github.com/nfarina/homebridge/blob/master/README.md
			- in the wiki for homebridge, it seems to imply that it uses HAP-NodeJS
				- This is required by the mdns package in HAP-NodeJS library.
				- also on the main page it credits HAP-NodeJS
			- going to follow the homebridge stuff
			- 
- [ ] rpi library to drive neopixels directly
	- https://github.com/ManiacalLabs/BiblioPixel/issues/51#issuecomment-228662943
- doing dev work for LED stuff on rpi is slow, it's slow to compile.
- like most things, best to do dev work on the actual computer now that we know we can do what we need to on the rpi
- to do this right, best to have all the stuff in a proper git repo for this work, put it on github for now, do we want github or bitbucket?
	- github since it's going to be a public thing. 


installed on the deck are 150+65 = 215 lights

in teh adafruit code, when i set pixel 214 , the last light in the strand is set

note that i can't actually see the first couple lights in the strand at index 0

= need to get comms between the pi and arduino going
	- [ ] https://www.arduino.cc/en/Reference/Firmata


## platform IO notes ##

- make sure to either use the .ino extension for arduino code or include Arduino.h
	- #include <Arduino.h>
- start a new project
	- platformio init --board uno 
- build
	- platformio run
- upload
	- platformio run --target upload


## git notes yet again ##

- following https://help.github.com/articles/set-up-git/


I ordered 5M strips with 30 LED per meter IP67. So that's 150 LED per strip, 300 LED total. 

- $3.98 x 3
	- 5050 silicon led strip clip for led tube,led strip accessories connector for fixing waterproof 3528 5050 strip 100pcs/lot
- $21.81 x 3
	- individually addressable 1m 4m 5m waterproof ip65 ip67 5050 rgb 30 60 144 led/m 5v ws2811 ws2812 ws2812b led strip
- $ 12.08 X1
	- waterproof ip65 250w 50a 5v power supply,ac 110v 220v to 5v dc switching power supply,outdoor use

There is a limit to how fast the lights can be pushed through. Even with no delay put in the code, it takes a certain amount of time for the full loop to be displayed with a rabbit being sent down the strip.


- https://www.adafruit.com/products/2238
	- 30 LED / m , $20 USD / M
	- 14' 2" (170") x 19' 1" (229")
	- 4.3 m x 5.8 = 10.1 m
	- gate is 41" = 1.0 m
	- so 9m of lights is good for min, 10 better for extra and get all the connectors
	- this uses a APA102C smart LED chip inside
	- 10 m would be $200 USD
- https://learn.adafruit.com/adafruit-dotstar-leds
- Estimate up to 60 milliamps peak for each pixel at full brightness white.
	- 10 m * 30 lights / m * 60 ma / light = 18000 ma = 18 A. so 2 or 3 10 A supplies
		- 5V 10A Supply $25 USD
			- https://www.adafruit.com/product/658
- looking at about 300 lights at 30/meter, 600 lights at 60/meter
- 30 / meter is going to be just fine

- LED Chips
	- APA102C (DotStar)
	- SK9822 (seen on aliexpress as newer version of APA102)
		- https://github.com/FastLED/FastLED/issues/291 , it's supported
	- ws2812b (neopixel) 
	- SK6812 (neopixel)
	- LPD8806  (Newer verson of my old strip)
		- https://www.adafruit.com/products/306
		- set and forget, can go do other things
	- WS2801 
		- older kind that allows for set and hold, slower
	- HL1606 (My old Strip)
	**- https://github.com/FastLED/FastLED/wiki/Chipset-reference **
	- https://forums.adafruit.com/viewtopic.php?f=47&t=40359
		- the neopixel chips dont have a clock line, so the data must come in at a perfect rate, saves a line, more complex timing
		- the LPD8806 has a clock line too, so simpler SPI interface
	- 
		
- electrical design notes
	- will need something in between rpi and strips if it is neopixel type (either arduino or something like FaceCandy)
	- if it's direct out of rpi and to 5V, will need 3.3V to 5V level shifter
	- https://learn.adafruit.com/adafruit-neopixel-uberguide/power
	- keep a power tap every meter for no brown outs
		- even if it's from one supply, attach the supply every meter or so so that the power doesn't need to come down the strip only
	- put a cap on the power line
	- put a 300 - 500 ohm resistor on the data line
	- [ ] is there a handy HAT for rpi for this ?
	- 
- electrical pieces
	- FadeCandy USB control of WS2811 ($25 USD)
		- can control up to 512 lights (we have 300ish in the deck design)
		- https://www.adafruit.com/product/1689

- using the facecandy software on our arduino might be useful (as an OPC server)
	- https://github.com/scanlime/fadecandy

- weather proofness ratings
	- IP 65: water jets 
	- IP 67: immersion 1meters 30mins
	- on ali saw IP65 was conformal coat, IP67 was in a sheathing 

- code 
	- https://github.com/jgarff/rpi_ws281x
	- https://github.com/zestyping/openpixelcontrol
	- https://github.com/plasticrake/OpcServer
		- receives using wifi, can it just be strings over usb instead?
	- http://www.st4makers.com/opc-server-for-arduino
		- this is not the OPC you are looking for
	- http://fastled.io/


- controllers
	- Symphony controller T-1000S-C Version $50 controller type thing so there is no extra programming
	- http://www.aliexpress.com/store/product/touch-panel-remote-control-full-color-rgb-led-wifi-spi-controller-support-ws2811-ws2801-lpd6803-iphone/110396_32268691946.html

- aliexpress
	- White 5m 30 IP67 $22 ( neopixel type ws2812b)
		- $22 for 5M 30 LED IP67
		- 10 meters would be $44 USD
		- http://www.aliexpress.com/item/individually-addressable-1m-2m-4m-5m-waterproof-ip65-ip67-5050-rgb-30-60-74-96-144/32243894576.html?spm=2114.10010108.100009.1.uNprI5&scm=1007.13482.37805.0&pvid=edfef1cc-3aca-43eb-bf1a-f99604480833&tpp=1
	- holder
		- http://www.aliexpress.com/store/product/3528-5050-silicon-led-strip-clip-for-led-tube-led-strip-accessories-connector-for-fixing-waterproof/110396_32306969416.html
	- White 5m 30 IP67 $19.86
		- http://www.aliexpress.com/item/1m-4m-5m-WS2812B-Smart-led-pixel-strip-Black-White-PCB-30-60-144-leds-m/32500778173.html?spm=2114.13010208.cb0001.11.c78gFE&scm=1007.13440.37933.0&pvid=a69aedac-751f-4027-b4bd-1bd1e1628dff&tpp=1
	- White 5m 60 IP67 $26.86
		- http://www.aliexpress.com/item/1m-4m-5m-WS2812B-Smart-led-pixel-strip-Black-White-PCB-30-60-144-leds-m/32500778173.html?spm=2114.13010208.cb0001.11.c78gFE&scm=1007.13440.37933.0&pvid=a69aedac-751f-4027-b4bd-1bd1e1628dff&tpp=1
	- 5V IP65 250W power supply $29.41 = $12.08 + $17.33 SH
		- http://www.aliexpress.com/store/product/waterproof-ip65-250w-50a-5v-power-supply-ac-110v-220v-to-5v-dc-switching-power-supply/110396_1941156635.html
- ebay
	-  $58.88 APA102C 30 led/m 5m white IP67 so ($120 USD for 10M)
		-  http://www.ebay.com/itm/1-100m-APA102-C-5050-RGB-SMD-30-36-60-144-leds-m-pixels-IP20-65-67-led-strip-5V-/381585501493?var=&hash=item58d844ad35:m:mhQloFdwnOhowGC70jNeIEw
	-  5V 300W IP65 $30.99
		-  http://www.ebay.com/itm/Waterproof-AC-85V-265V-To-DC-5V-12V-24V-Switching-Power-Supply-Driver-Adapter-/381646920264?var=&hash=item58dbedda48:m:mABykaeCE7Mq4Ijhoiyvy1g


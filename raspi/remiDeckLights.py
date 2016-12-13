"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App

import serial
import sys
import webcolors
import colorsys

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self, name='world'):
        #margin 0px auto allows to center the app to the screen
        wid = gui.VBox(width=300, height=200, margin='0px auto')
        lbl = gui.Label('Hello %s!' % name, width='80%', height='50%')
        lbl.style['margin'] = 'auto'

        #bt = gui.Button('Press me!', width=200, height=30)
        bt = gui.Button('Turn lights ON', width=200, height=30)
        bt.style['margin'] = 'auto 50px'

        # setting the listener for the onclick event of the button
        self.npressed = 0

        # connect to the arduino, read the default startup output
        # and set all the lights to be off
        self.ser = serial.Serial('/dev/ttyACM0',57600,timeout=1)
	hello = self.ser.readline()
	hello = self.ser.readline()
	self.ser.write(b'm42')

        
        bt.set_on_click_listener(self.on_button_pressed, lbl)
        bt.set_on_mousedown_listener(self.on_button_mousedown, 'data1', 2,'three')
        
        self.colorPicker = gui.ColorPicker('#ffbb00', width=200, height=20, margin='10px')
        self.colorPicker.set_on_change_listener(self.color_picker_changed,lbl)


        #this will never be called, can't register an event more than one time
        bt.set_on_mouseup_listener(self.on_button_mouseup, 'data1') 

	self.slider = gui.Slider(128, 0, 255, 1, width=200, height=20, margin='10px')
	self.slider.set_on_change_listener(self.slider_changed)

        # appending a widget to another, the first argument is a string key
        wid.append(lbl)
        wid.append(bt)
        wid.append(self.colorPicker)
	wid.append(self.slider)
        # returning the root widget
        return wid

    def slider_changed(self, widget, value):
        brightness = "b" + str(int(value))
	print "\n\n\nBrightness " + brightness
	self.ser.write(brightness)

    def setHue(self, hue):
	self.ser.write(b'm1')
	hueStr = 'a' + str(int(hue))
	print "\n\n\nHueStr " + hueStr
	self.ser.write(hueStr)

    def color_picker_changed(self, widget, value,lbl):
        hexValue = value
	rgbValue = webcolors.hex_to_rgb(hexValue)
	hsvValue = colorsys.rgb_to_hsv(rgbValue[0]/255.0,rgbValue[1]/255.0,rgbValue[2]/255.0)
	hue = round(hsvValue[0] * 255)
	print hexValue , rgbValue , hsvValue, hue	
        lbl.set_text('New color value: ' + value )
        self.setHue(hue)

# have a readline here to wait for the arduino to write "---SETUP COMPLETE---" 
# before we continue with the program


        
        
    def lightsOn(self):
        #ser = serial.Serial('/dev/ttyACM0',57600,timeout=5)
	#hello = self.ser.readline()
	self.ser.write(b'm42')
	#ser.close()

    def lightsOff(self):
        #ser = serial.Serial('/dev/ttyACM0',57600,timeout=5)
	#hello = ser.readline()
	self.ser.write(b'm0')
	#ser.close()

    # listener function
    def on_button_pressed(self, widget, lbl):
        
        if ( 0 == self.npressed % 2 ):
            self.lightsOn()
            widget.set_text('Turn Lights Off')
        else:
            self.lightsOff()
            widget.set_text('Turn Lights On')
	self.npressed += 1
        lbl.set_text('Button pressed %s times.' % self.npressed)
        #widget.set_text('Hi!')
        
    def on_button_mousedown(self, widget, x, y, mydata1, mydata2, mydata3):
        print("x:%s  y:%s  data1:%s  data2:%s  data3:%s"%(x, y, mydata1, mydata2, mydata3))
        
    def on_button_mouseup(self, widget, x, y, mydata1):
        print("x:%s  y:%s  data1:%s"%(x, y, mydata1))

    def on_button_mouseup2(self, widget, x, y):
        print("x:%s  y:%s  no userdata"%(x, y))

if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(MyApp, debug=True,address='0.0.0.0',port=80)
    #start(MyApp,address='0.0.0.0',port=80)

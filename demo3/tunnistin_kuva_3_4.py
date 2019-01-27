
# Ledi syttyy painikkeen painamisella
# ja nayttoon tulostuu tieto siita havaitseeko liiketunnistin liiketta

import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import sys

GPIO.setmode (GPIO.BCM)
GPIO.setup(21, GPIO.IN) # Luetaan pinnissa 21 kiinni olevaa PIR sensoria.

cam = PiCamera()
a = True

# Ohjelma pyorii niin kauan kun tunnistin havaitsee liiketta ja ottaa kuvan
while a==True:
    i=GPIO.input(21)
    if i==1:
        print "Liiketta havaittu -> kuva otettu"
	cam.start_preview()
	time.sleep(5)
	cam.capture('varas_kuvassa.jpg')
	cam.stop_preview()
	time.sleep(5)
	GPIO.cleanup ()
	a = False

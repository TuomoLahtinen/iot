# Liikennevalot 2.5

import RPi.GPIO as GPIO
import time

PAINIKE=5
SENSORI=18

GPIO.setmode (GPIO.BCM)
GPIO.setup(SENSORI, GPIO.IN) #PIR sensori
GPIO.setup (PAINIKE, GPIO.IN) #kavelijan painike
GPIO.setup (12, GPIO.OUT) #vihrea valo jalankulkija
GPIO.setup (16, GPIO.OUT) #vihrea valo autot
GPIO.setup (21, GPIO.OUT) #punainen valo jalankulkija
GPIO.setup (23, GPIO.OUT) #punainen valo autot
GPIO.setup (24, GPIO.OUT) #painikkeen rekisterointi valo keltainen
GPIO.setup (25, GPIO.OUT) #keltainen valo autot

def valot():
	GPIO.output(16,False)
	GPIO.output(25,True)
	time.sleep(2)
	GPIO.output(25,False)
	GPIO.output(23,True)
	time.sleep(2)
	GPIO.output(21,False)
	GPIO.output(24,False)
	GPIO.output(12,True)
	time.sleep(7)
	GPIO.output(12,False)
	GPIO.output(21,True)
	time.sleep(1)
	GPIO.output(25,True)
	time.sleep(1)
	GPIO.output(25,False)
	GPIO.output(23,False)
	GPIO.output(16,True)
	time.sleep(5)

def tunnistin():
	i=0
	while i<2:
		if GPIO.input (SENSORI) == True:
			print("liiketta") #Näkee miten liiketunnistin toimii
			time.sleep(4)
			i=i+1
		else:
			i=5
			print("ei liiketta") #Näkee miten liiketunnistin toimii

while True:
	GPIO.output(16,True)
	GPIO.output(21,True)
	if GPIO.input (PAINIKE) == True:
		GPIO.output(24,True)
		tunnistin()
	else:
		continue
	valot()
	break

GPIO.cleanup ()

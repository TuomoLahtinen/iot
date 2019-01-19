# Liikennevalot 2.4

import RPi.GPIO as GPIO
import time

PAINIKE=5

GPIO.setmode (GPIO.BCM)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (12, GPIO.OUT)
GPIO.setup (16, GPIO.OUT)
GPIO.setup (21, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (24, GPIO.OUT)
GPIO.setup (25, GPIO.OUT)

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

while True:
	GPIO.output(16,True)
	GPIO.output(21,True)
	if GPIO.input (PAINIKE) == True:
		GPIO.output(24,True)
		time.sleep(2)
		valot()
		break
	else:
		continue

GPIO.cleanup ()


import RPi.GPIO as GPIO
import time

PIN=4

GPIO.setmode (GPIO.BCM)
GPIO.setup (PIN, GPIO.OUT)

vilkku = time.time() + 0.5 #Ledi palaa kerrallaan 0.5sek
while time.time() < vilkku:
	GPIO.output(PIN,1)
GPIO.cleanup ()
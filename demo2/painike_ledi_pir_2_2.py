
# Ledi syttyy painikkeen painamisella
# ja nayttoon tulostuu tieto siitä havaitseeko liiketunnistin liiketta

import RPi.GPIO as GPIO
import time

LED=23 # Paikalla 23
PAINIKE=5 # Paikalla 5

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup(16, GPIO.IN) # Luetaan pinnissa 16 kiinni olevaa PIR sensoria.

loppu = time.time() + 20 # Virtaa syötetaan 20sek ajan ennenkuin ohjelma ja virransyotto katkaistaan
while time.time() < loppu:
	GPIO.output(LED, GPIO.input (PAINIKE))
	time.sleep (0.1) # ilman tata prossukaytto 100%
	i=GPIO.input(16)
    if i==0:
        print "Ei liiketta"
        time.sleep(0.1)
    elif i==1:
        print "Liiketta havaittu"
        time.sleep(0.1)

GPIO.cleanup ()
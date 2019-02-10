#include <stdio.h>
#include <wiringPi.h>


int main(){
	
	/* alustus BCM numeroinnille */
	wiringPiSetupGpio();
	
	/* pinnien määritys */
	pinMode(18, INPUT); /* SENSORI */
	pinMode(5, INPUT); /* PAINIKE */
	
	pinMode(12, OUTPUT); /* vihrea jalankulkija */
	pinMode(16, OUTPUT); /* vihrea autot */
	pinMode(21, OUTPUT); /* punainen jalankulkija */
	pinMode(23, OUTPUT); /* punainen autot */
	pinMode(24, OUTPUT); /* painikkeen rekisterointi valo keltainen */
	pinMode(25, OUTPUT); /* keltainen autot */	

	while( TRUE ) {
		digitalWrite(16, HIGH);
		digitalWrite(21, HIGH);
		
		if(digitalRead(5)) {
			digitalWrite(24, HIGH);
			tunnistin();
	
			digitalWrite(16, LOW);
			digitalWrite(25, HIGH);
			delay (5000);
			digitalWrite(25, LOW);
			digitalWrite(23, HIGH);
			delay (2000);
			digitalWrite(21, LOW);
			digitalWrite(24, LOW);
			digitalWrite(12, HIGH);
			delay (7000);
			digitalWrite(12, LOW);
			digitalWrite(21, HIGH);
			delay (1000);
			digitalWrite(25, HIGH);
			delay (1000);
			digitalWrite(25, LOW);
			digitalWrite(23, LOW);
			digitalWrite(16, HIGH);
			delay (5000);
			digitalWrite(16, LOW);
			digitalWrite(21, LOW);
			break;
		}
	}
	return 0;
}

int tunnistin(){
	int i=0;
	while (i<2) {
		if ( digitalRead(18) ) {
			printf( "Liiketta, odotetaan \n" );
			delay (4000);
			i=i+1;
		}
		else {
			i=5;
			printf( "Ei liiketta, vaihdetaan valot \n" );
		}
	}
	return 1;
}


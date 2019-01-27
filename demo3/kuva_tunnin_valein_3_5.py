import time
from picamera import PiCamera
import schedule

def job():
	cam = PiCamera()
	cam.capture('kuva.jpg')

schedule.every(1).minutes.do(job)
#schedule.every().minute.at(":45").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
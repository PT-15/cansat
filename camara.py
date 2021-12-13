from picamera import PiCamera
import time

camera = PiCamera()

camera.resolution = (1920, 1272)

while True:
	camera.capture('/home/pi/Documents/photoTime_%0.2f.jpg' % time.time())
	time.sleep(2)

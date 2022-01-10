import bme280
from time import sleep

bme280.init()

while (True):
	bme280.writeLogLine()
	sleep (0.1)

try:
	main()
except KeyboardInterrupt:
	bme280.close()
	print("Out")

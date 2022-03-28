import radio

SENSOR = "sensorData.txt"
GPS = "gpsData.txt"
radio.init()
i = 0
file = SENSOR

while True:
	if (i == 10):
		i = 0;
	msg = radio.rfm69.receive(timeout=2)
	if msg is None:
		print ("No message")
		i = 0
	else:
		data = msg.decode()
		if (i < 5):
			file = SENSOR
		else:
			file = GPS
		with open (file, 'at') as f:
			f.write(msg)
			f.flush()

radio.close()

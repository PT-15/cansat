import radio

radio.init()

while True:
	msg = radio.rfm69.receive(timeout=2)
	if msg is None:
		print ("No message")
	else:
		data = msg.decode()
		if (data == "GPS"):
			for x in range(5):
				msg = radio.rfm69.receive(timeout=2)
				data = msg.decode()
				with open ("gpsData.txt", 'at') as f:
					f.write(data + " ")
					f.flush()
			with open ("gpsData.txt", 'at') as f:
				f.write("\n")
				f.flush()
		else:
			with open ("sensorData.txt", 'at') as f:
				f.write(data + " ")
				f.flush()

radio.close()

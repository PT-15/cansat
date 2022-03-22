import busio
import board
import serial
import radio

radio.init()
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

while True:
	line = uart.readline()
	data = str(line).split(",", 9)
	if (data[0] == "b'$GNGGA"):
		with open ("infoGps.txt", 'at') as f:
			f.write(str(line) + "\n")
			f.flush()

		if (data[1]):
			time = bytes(data[1], "utf-8")
			radio.rfm69.send(time)
		else:
			error = bytes("-1", "utf-8")
			radio.rfm69.send(error)
		if (data[2]):
			degrees = data[2][:2]
			minutes = data[2][2:]
			minutes = str(float(minutes)/60)
			if (data[3] == "S"):
				degrees *= 1;
			coord = degrees + minutes[:4]
			longitude = bytes(coord, "utf-8")
			radio.rfm69.send(longitude)
		else:
			error = bytes("-1", "utf-8")
			radio.rfm69.send(error)
		if (data[4]):
			degrees = data[4][:3]
			minutes = data[4][3:]
			minutes = str(float(minutes)/60)
			if (data[5] == "W"):
				degrees *= -1
			coord = degrees + minutes[:4]
			latitude = bytes(coord, "utf-8")
			radio.rfm69.send(latitude)
		else:
			error = bytes("-1", "utf-8")
			radio.rfm69.send(error)
		if (data[6]):
			quality = bytes(data[6], "utf-8")
			radio.rfm69.send(quality)
		else:
			error = bytes("-1", "utf-8")
			radio.rfm69.send(error)
		if(data[7]):
			satelites = bytes(data[7], "utf-8")
			radio.rfm69.send(satelites)
		else:
			error = bytes("-1", "utf-8")
			radio.rfm69.send(error)
		sleep(0.5)

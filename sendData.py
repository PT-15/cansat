import busio
import board
import serial
import radio
import bme280
from time import sleep

radio.init()
bme280.init()
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

while True:
	#Recoger datos
	sensorLine = bme280.line()
	sensorD = sensorLine.split(" ")
	gpsLine = uart.readline()
	data = str(gpsLine).split(",", 9)

	#Guardar datos gps
	with open ("infoGps.txt", 'at') as f:
		f.write(str(gpsLine) + "\n")
		f.flush()


	#Enviar datos sensor
	with open ("data.txt", 'at') as f:
		f.write(sensorLine)
		f.flush()
	time = bytes(sensorD[0], "utf-8")
	radio.rfm69.send(time)
	d1 = bytes(sensorD[1], "utf-8")
	radio.rfm69.send(d1)
	d2 = bytes(sensorD[2], "utf-8")
	radio.rfm69.send(d2)
	d3 = bytes(sensorD[3], "utf-8")
	radio.rfm69.send(d3)
	d4 = bytes(sensorD[4], "utf-8")
	radio.rfm69.send(d4)

	#Enviar datos gps
	if (data[0] == "b'$GNGGA"):
		checker = bytes("GPS", "utf-8")
		radio.rfm69.send(checker)
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

bme280.close()

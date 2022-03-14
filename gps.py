import busio
import board
import serial

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)

while True:
	line = uart.readline()
	data = str(line).split(",", 9)
	if (data[0] == "b'$GNGGA"):
		with open ("infoGps.txt", 'at') as f:
			f.write(str(line) + "\n")
			f.flush()
		#ENVIAR ESTA INFORMACIÓN POR RADIO
		if (data[1]):
			print ("Time:" + data[1])
		else:
			print ("-1")
		if (data[2]):
			print ("Latitude:" + data[2] + data[3])
		else:
			print ("-1")
		if (data[4]):
			print ("Longitude:" + data[4] + data[5])
		else:
			print ("-1")
		if (data[6]):
			print ("Quality:" + data[6])
		else:
			print ("-1")
		if(data[7]):
			print ("Satelites:" + data[7])
		else:
			print ("-1")
		print ()

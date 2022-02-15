import serial
import time

self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:

	error = 0
	lectura = self.ser.readline()

	try:
		lectura = lectura.decode()
	except UnicodeDecodeError:
		print("Error de lectura")
		error = 1

	if not error and lectura[0:3] == "Hel":
		print (lectura)
	else
		print ("error")

	time.sleep(0.5)

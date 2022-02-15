import serial

CFG_REG = [b'\xC2\x00\x09\xFF\xFF\x00\x62\x00\x17\x03\x00\x00',
                   b'\xC2\x00\x09\x00\x00\x00\x62\x00\x17\x03\x00\x00']

ser = serial.Serial("/dev/ttyS0", 9600)
ser.flushInput()

try:
	if ser.isOpen():
		ser.write(CFG_REG[1])

	while True:
		mensaje = "Hola Mundo"
		print (mensaje)
		ser.write(mensaje.encode())
		time.sleep(10)

except:
	if ser.isOpen():
		ser.close()


#		if ser.inWaiting() > 0:
#			time.sleep(0.1) #Why?
#			r_buff = ser.read(ser.inWaiting())
#			#Se necesita mensaje
#			ser.write(mensaje.encode)()
	#Comprobar contexto
#	if ser.isOpen():
#		ser.close()

'''
Funciones librería
	.init (inicializar)
	.line (datos)
	.writeLogLine (escribir datos a fichero)
'''

import board
import busio
import adafruit_bme280
import time

outputLog = None
bme280 = None

#Inicicaliza el sensor
def init():
	global outputLog
	global bme280

	i2c = busio.I2C(board.SCL, board.SDA)
	bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

#Devuelve los datos del sensor
def line():
    return "%f %f %f %f\n" % (time.time(), bme280.temperature, bme280.humidity, bme280.pressure)

#Escribe los datos al archivo de texto
def writeLogLine():
	with open('data.txt', 'a') as log:
		log.write(line())
		log.flush()

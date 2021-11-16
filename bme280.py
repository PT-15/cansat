'''
Funciones librería
	.init (inicializar)
	.line (datos)
	.writeLogLine (escribir datos a fichero)
	.altitud (altitud)
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
	bme280.sea_level_pressure = 1004.8
	outputLog = open ('data.txt', 'a')

#Devuelve los datos del sensor
def line():
    return "%f %f %f %f %f\n" % (time.time(), bme280.temperature, bme280.humidity, bme280.pressure, bme280.altitude)

#Escribe los datos al archivo de texto
def writeLogLine():
	outputLog.write(line())
	outputLog.flush()

def close():
	outputLog.close()

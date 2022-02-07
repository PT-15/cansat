import bme280
import loraLibrary as lora
from time import sleep
lora.init()
bme280.init()

while True:
   logLine = bme280.line()
   with open('data.txt', 'at') as log:
      log.write(logLine)
      log.flush()

   sensorData = logLine.split()
   for num in sensorData:
      lora.send(num)
   print ("Line encoded")
   sleep(1)

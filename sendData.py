import sensor
import loraLibrary as lora
lora.init()
sensor.init()

while True:
   sensor.writeLogLine()

   with open ('data.txt', 'rt') as sensorLog:
      dataLine = sensorLog.readline()

   sensorData = dataLine.split()
   for num in sensorData:
      num.encode()
      node.send(num)

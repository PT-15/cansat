'''
Funciones librería
  .init (inicializar)
  .mensajePrueba (envía "Hola Mundo")
'''

import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer

def init():
  old_settings = termios.tcgetattr(sys.stdin)
  tty.setcbreak(sys.stdin.fileno())
  
  node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=433,addr=15,power=22,rssi=True,air_speed=2400,relay=False)

  
def mensajePrueba():
  print ("Enviando \"Hola Mundo"")
  mensaje = "Hola Mundo".encode()
  node.send(data)
  time.sleep(0.2)

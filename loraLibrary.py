import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer

node = None

def init():
   global node
   old_settings = termios.tcgetattr(sys.stdin)
   tty.setcbreak(sys.stdin.fileno())

   node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=433,addr=0,power=22,rssi=False,air_speed=2400,relay=False)

def send(num):
   node.send(num.encode())

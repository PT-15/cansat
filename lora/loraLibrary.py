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

def send(msg):
   #splitMsg = msg.split()
   offset_frequence = int(get_t[1])-(850 if int(get_t[1])>850 else 410)
   #data = bytes([int(get_t[0])>>8]) + bytes([int(get_t[0])&0xff]) + bytes([offset_frequence]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq]) + get_t[2].encode()
   data = bytes([int(msg) >> 8]) + bytes([int(msg)&0xff]) + bytes([offset_frequence]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq])
   node.send(data)

def receive():
   node.receive()

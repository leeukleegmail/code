from RPLCD import CharLCD
import socket
import fcntl
import struct
import time
from datetime import datetime
import logging
import pytz
from datetime import timedelta

lcd = CharLCD(cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd.write_string("IP Address:") 

lcd.cursor_pos = (1, 0)
lcd.write_string(get_ip_address('eth0'))

#lcd.cursor_pos = (2, 0)
#current_time = time.strftime("%Y-%m-%d %H:%M")
#lcd.write_string(current_time)

lcd.cursor_pos = (3, 0)
smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string(unichr(0))

while True:
    lcd.cursor_pos = (2, 0)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    #current_time = time.strftime("%a, %d %b %Y %X", time.localtime())    
    #cet = pytz.timezone('CET')    
    lcd.write_string(current_time)
    time.sleep(1)

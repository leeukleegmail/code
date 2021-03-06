import RPi.GPIO as GPIO
from time import sleep
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# initalise ports as outputs and switch them off
def initalise_ports():
    #ports = [3,5,7,8,10,12,16,18,22,24]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    ports = [29,31,7,33,10,12,16,18,22,24]
    for port in ports:
        port = int(port)
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.HIGH)
        #print "Port %s done" % port


def test():
    initalise_ports()
    count = 0
    timeout = time.time() + 30*1
    direction = 'asc'
    while True:
        sequence_gpio(count)

        if direction == 'asc' and count != 5:
            count +=1
            if direction == 'asc' and count == 5:
                direction = 'desc'
        elif direction == 'desc' and count != 1:
            direction = 'desc'
            count -=1
            if direction == 'desc' and count == 1:
                direction = 'asc'
        #print count
        time.sleep (50.0 / 1000.0);
        #sleep (1)
        if time.time() > timeout:
            GPIO.cleanup()
            break


def sequence_gpio(count):
    if count == 1:
        GPIO.output(29, GPIO.LOW)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
    elif count == 2:
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
    elif count == 3:
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
    elif count == 4:
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
    elif count == 5:
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)


if __name__ == '__main__':
    test()


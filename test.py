import RPi.GPIO as GPIO
from time import sleep
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# initalise ports as outputs and switch them off
def initalise_ports():
    all = ['10','11','12','13','14']
    for x in all:
        x = int(x)
        print (x)
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.LOW)

def test():
    initalise_ports()
    count = 0
    timeout = time.time() + 60*1
    direction = 'asc'
    while True:
        #sequence_gpio(count)

        if direction == 'asc' and count != 5:
            count +=1
            if direction == 'asc' and count == 5:
                direction = 'desc'
        elif direction == 'desc' and count != 1:
            direction = 'desc'
            count -=1
            if direction == 'desc' and count == 1:
                direction = 'asc'
        sleep (1)

        if time.time() > timeout:
            break


def sequence_gpio(count):
    if count == 0:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
    elif count == 1:
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
    elif count == 2:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
    elif count == 3:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
    elif count == 4:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(14, GPIO.LOW)
    elif count == 5:
        GPIO.output(10, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(14, GPIO.HIGH)


if __name__ == '__main__':
    test()


GPIO.cleanup()

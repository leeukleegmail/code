import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# initalise ports as outputs and switch them off
def initalise_ports():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    ports = [32, 36, 38]
    for port in ports:
        port = int(port)
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)


def test():
    initalise_ports()
    GPIO.output(32, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(36, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(38, GPIO.HIGH)


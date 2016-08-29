# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_MCP4725

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dac = Adafruit_MCP4725.MCP4725()

def my_callback():
    print "falling edge detected on 40"
    voltage = 4000
    dac.set_voltage(voltage)
    sleep(10)
    while voltage >= 2000:
        sleep(0.1)
        voltage = (voltage - 25)
        dac.set_voltage(voltage)

#GPIO.add_event_detect(40, GPIO.FALLING, callback=my_callback, bouncetime=300)

#voltage = 4000
#dac.set_voltage(voltage)

while True:
    try:  
        GPIO.wait_for_edge(40, GPIO.FALLING)  
        my_callback()
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
dac.set_voltage(0, True)


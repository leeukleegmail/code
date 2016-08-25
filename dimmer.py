from time import sleep
import os

import Adafruit_MCP4725

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725()

#dac = Adafruit_MCP4725.MCP4725(address=0x49, busnum=1)

print('Press Ctrl-C to quit...')
voltage = 4000
dac.set_voltage(voltage)

while voltage >= 2000:
    sleep(0.1)
    voltage = (voltage - 50)
    dac.set_voltage(voltage)

dac.set_voltage(0, True)

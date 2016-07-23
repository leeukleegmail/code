import time
import nightrider
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 8

try:
    while True:
        read = adc.read_adc(0, gain=GAIN)
        print(read)
        print time.strftime("%Y-%m-%d %H:%M")
        if read < 7000:
            print(read)
            nightrider.test()
        time.sleep(60)
except KeyboardInterrupt:

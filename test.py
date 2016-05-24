import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one input and one output
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# output to pin 12
GPIO.output(12, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)
GPIO.output(10, GPIO.HIGH)

#function = GPIO.gpio_function(12)
#print function

def test():
    all = ['10','11','12']
    for x in all:
        x = int(x)
        input_value = GPIO.input(x)
        print 'value for pin %s is %s' % (x, input_value)
        #for x in all:
        if input_value == 0:
            GPIO.output(x, GPIO.HIGH)
            input_value = GPIO.input(x)
            print 'value for pin %s is %s' % (x, input_value)
        else: 
            GPIO.output(x, GPIO.LOW)
            input_value = GPIO.input(x)
            print 'value for pin %s is %s' % (x, input_value)

if __name__ == '__main__':
    test()


GPIO.cleanup()

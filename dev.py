from time import sleep


def test():
    all = ['10','11','12']
    for x in all:
        x = int(x)
#        input_value = GPIO.input(x)
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

def test1():
    count = 0
    max = 10
    direction = 'asc'
    while count != 7:
        if count == 0:
            print 'value for pin 10 is 0'
            print 'value for pin 11 is 0'
            print 'value for pin 12 is 0'
            print 'value for pin 13 is 0'
            print 'value for pin 14 is 0'
        elif count == 1:
            print 'value for pin 10 is 1'
            print 'value for pin 11 is 0'
            print 'value for pin 12 is 0'
            print 'value for pin 13 is 0'
            print 'value for pin 14 is 0'
        elif count == 2:
            print 'value for pin 10 is 0'
            print 'value for pin 11 is 1'
            print 'value for pin 12 is 0'
            print 'value for pin 13 is 0'
            print 'value for pin 14 is 0'
        elif count == 3:
            print 'value for pin 10 is 0'
            print 'value for pin 11 is 0'
            print 'value for pin 12 is 1'
            print 'value for pin 13 is 0'
            print 'value for pin 14 is 0'
        elif count == 4:
            print 'value for pin 10 is 0'
            print 'value for pin 11 is 0'
            print 'value for pin 12 is 0'
            print 'value for pin 13 is 1'
            print 'value for pin 14 is 0'
        elif count == 5:
            print 'value for pin 10 is 0'
            print 'value for pin 11 is 0'
            print 'value for pin 12 is 0'
            print 'value for pin 13 is 0'
            print 'value for pin 14 is 1'

        if direction == 'asc' and count != 5:
            print "first if true"
            count +=1
            print count
            if direction == 'asc' and count == 5:
                direction = 'desc'
        elif direction == 'desc' and count != 1:
            print "first if false"
            direction = 'desc'
            count -=1
            print count
            if direction == 'desc' and count == 1:
                direction = 'asc'

        sleep (1)



if __name__ == '__main__':
    test1()



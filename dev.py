from time import sleep
import time


def test():
    count = 0
    timeout = time.time() + 60*1
    direction = 'asc'
    while True:
        sequence_test(count)

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


def sequence_test(count):
    if count == 0:
        print '====================='
        print 'value for pin 10 is 0'
        print 'value for pin 11 is 0'
        print 'value for pin 12 is 0'
        print 'value for pin 13 is 0'
        print 'value for pin 14 is 0'
        print '====================='
    elif count == 1:
        print '====================='
        print 'value for pin 10 is 1'
        print 'value for pin 11 is 0'
        print 'value for pin 12 is 0'
        print 'value for pin 13 is 0'
        print 'value for pin 14 is 0'
        print '====================='
    elif count == 2:
        print '====================='
        print 'value for pin 10 is 0'
        print 'value for pin 11 is 1'
        print 'value for pin 12 is 0'
        print 'value for pin 13 is 0'
        print 'value for pin 14 is 0'
        print '====================='
    elif count == 3:
        print '====================='
        print 'value for pin 10 is 0'
        print 'value for pin 11 is 0'
        print 'value for pin 12 is 1'
        print 'value for pin 13 is 0'
        print 'value for pin 14 is 0'
        print '====================='
    elif count == 4:
        print '====================='
        print 'value for pin 10 is 0'
        print 'value for pin 11 is 0'
        print 'value for pin 12 is 0'
        print 'value for pin 13 is 1'
        print 'value for pin 14 is 0'
        print '====================='
    elif count == 5:
        print '====================='
        print 'value for pin 10 is 0'
        print 'value for pin 11 is 0'
        print 'value for pin 12 is 0'
        print 'value for pin 13 is 0'
        print 'value for pin 14 is 1'
        print '====================='





if __name__ == '__main__':
    test()


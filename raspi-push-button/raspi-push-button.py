#!/usr/bin/env python

import RPi.GPIO as GPIO

def my_callback(self):
    GPIO.output(25, GPIO.input(4))

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(4, GPIO.BOTH, callback=my_callback)
run = 1
while (run != 0):
    try:
        pass
    except KeyboardInterrupt:
        run = 0
        GPIO.cleanup()
        print 'KeyboardInterrupt caught'
        break
GPIO.cleanup()
print 'EXITED!'


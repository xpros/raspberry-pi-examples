#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def on_callback(channel):
    GPIO.output(channel, GPIO.input(4))

def off_callback(channel):
    GPIO.output(channel, False)

GPIO.setmode(GPIO.BCM)
RED_LED = 25
BLUE_LED = 24
SWITCH_IN = 4
GPIO.setup(SWITCH_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BLUE_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(SWITCH_IN, GPIO.RISING, bouncetime=900)


led = BLUE_LED
nled = RED_LED
run = 1
while (run != 0):
    try:
        if GPIO.event_detected(4):
            print led
            led = BLUE_LED if (led == RED_LED) else RED_LED
            nled = RED_LED if (nled == BLUE_LED) else BLUE_LED

            on_callback(led)
            off_callback(nled)

        pass
    except KeyboardInterrupt:
        run = 0
        GPIO.cleanup()
        print 'KeyboardInterrupt caught'
        break
GPIO.cleanup()
print 'EXITED!'


#!/usr/bin/python

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Board pin-numbering scheme

relay1=17
relay2=18
relay3=27
relay4=22

print("Setting up pins:",relay1, relay2, relay3, relay4)

GPIO.setwarnings(False)

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

GPIO.output(relay1, GPIO.LOW)
time.sleep(0.5)
GPIO.output(relay2, GPIO.LOW)
time.sleep(0.5)
GPIO.output(relay3, GPIO.LOW)
time.sleep(0.5)
GPIO.output(relay4, GPIO.LOW)


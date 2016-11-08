#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24


GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


def measure():
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.5) #minimum 100 ms between readings
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001) #10 ms pulse triggers sensor
    GPIO.output(trig, GPIO.LOW)

    counter1 = 0
    while GPIO.input(echo) == 0 and counter1 < 20000:
        pulse_start = time.time()
        counter1 += 1

    counter2 = 0
    while GPIO.input(echo) == 1 and counter2 < 20000:
        pulse_end = time.time()
        counter2 += 1

    if counter1 < 20000 and counter2 < 20000:
        duration = pulse_end - pulse_start
        distance = duration * 17150
        distance = round(distance, 2)
    else:
        distance = 0

    return distance


print("Distance measurement starting")

count = 0
while (count < 1):
    dist=measure()
    print(dist)
    count+=1
















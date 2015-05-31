import RPi.GPIO as GPIO
import time

__author__ = 'Dani'


def setup(ports):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for row in ports:
        for port in row:
            GPIO.setup(port, GPIO.OUT)
            GPIO.output(port, 1)
            time.sleep(0.1)
    for row in ports:
        for port in row:
            GPIO.output(port, 0)
            time.sleep(0.1)
    time.sleep(0.5)


def output(port, value):
    GPIO.output(port, value)
